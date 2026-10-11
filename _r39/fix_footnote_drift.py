# -*- coding: utf-8 -*-
"""修复「脚注区漂移」：把嵌在 card 容器内 / 游离在 section 内的脚注搬回 footer 的 srcs 容器。

背景：某版增补把脚注块插进了「上一版最后一张卡片」的内部，之后每版沿用同一锚点，
雪球从 v24 滚到 v42 —— 共 8 张 card 被撕开、306 条脚注落在 card / section 里。
index_metrics 的 E1–E7 只审数量与平衡、不审位置，所以照样全绿（本轮新增 E8/E9 补上）。

用法：
  python _r39/fix_footnote_drift.py --dry-run   # 只报告，不写盘
  python _r39/fix_footnote_drift.py             # 写盘（先自动备份 .bak2）
"""
import re, os, sys, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "index.html")
BAK = HTML + ".bak2"

FOOTNOTE_RE = re.compile(r'<div id="r(\d+)"[^>]*>.*?</div>')


def scan(lines):
    """返回 (footnotes, srcs_start, srcs_end)
    footnotes: [(lineno1based, container, snippet)]，container ∈ card / srcs / other
    """
    stack = []
    footnotes = []
    srcs_start = srcs_end = None
    for i, line in enumerate(lines):
        for m in re.finditer(r'<div\b([^>]*)>|</div>', line):
            tok = m.group(0)
            if tok == "</div>":
                if stack:
                    c, d, ln = stack.pop()
                    if d == "__SRCS__":
                        srcs_end = i
                continue
            attrs = m.group(1) or ""
            cls = re.search(r'class="([^"]*)"', attrs)
            did = re.search(r'id="([^"]*)"', attrs)
            c = cls.group(1) if cls else ""
            d = did.group(1) if did else ""
            if "srcs" in c.split():
                srcs_start = i
                stack.append((c, "__SRCS__", i))
                continue
            stack.append((c, d, i))
            if re.fullmatch(r"r\d+", d):
                anc = stack[:-1]
                in_card = any("card" in x[0].split() for x in anc)
                in_srcs = any(x[1] == "__SRCS__" for x in anc)
                in_footer = any(x[0] == "__FOOTER__" for x in anc)
                cont = "card" if in_card else ("srcs" if in_srcs else ("footer" if in_footer else "other"))
                footnotes.append((i + 1, cont, None))
    return footnotes, srcs_start, srcs_end


def scan_with_footer(lines):
    """同上，但把 <footer> 也压进栈，用于区分 footer 内/外。"""
    stack = []
    footnotes = []
    srcs_start = srcs_end = None
    for i, line in enumerate(lines):
        # footer 开标签（非 div）
        if re.search(r"<footer\b", line):
            stack.append(("__FOOTER__", "__FOOTER__", i))
        if re.search(r"</footer>", line):
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][1] == "__FOOTER__":
                    stack = stack[:j]
                    break
        for m in re.finditer(r'<div\b([^>]*)>|</div>', line):
            tok = m.group(0)
            if tok == "</div>":
                if stack:
                    c, d, ln = stack.pop()
                    if d == "__SRCS__":
                        srcs_end = i
                continue
            attrs = m.group(1) or ""
            cls = re.search(r'class="([^"]*)"', attrs)
            did = re.search(r'id="([^"]*)"', attrs)
            c = cls.group(1) if cls else ""
            d = did.group(1) if did else ""
            if "srcs" in c.split():
                srcs_start = i
                stack.append((c, "__SRCS__", i))
                continue
            stack.append((c, d, i))
            if re.fullmatch(r"r\d+", d):
                anc = stack[:-1]
                in_card = any("card" in x[0].split() for x in anc)
                in_srcs = any(x[1] == "__SRCS__" for x in anc)
                in_footer = any(x[1] == "__FOOTER__" for x in anc)
                cont = "card" if in_card else ("srcs" if in_srcs else ("footer" if in_footer else "other"))
                footnotes.append((i + 1, cont, m.group(0)))
    return footnotes, srcs_start, srcs_end


def main():
    dry = "--dry-run" in sys.argv
    raw = open(HTML, encoding="utf-8").read()
    lines = raw.split("\n")

    footnotes, srcs_start, srcs_end = scan_with_footer(lines)
    print(f"脚注 div 共 {len(footnotes)} 处（含非自闭合开标签计数）")

    # ⚠️ 只抽 card / other 里的脚注；srcs / footer 内的原地不动（上一版误删了它们）
    cont_by_line = {}
    for ln, cont, _ in footnotes:
        cont_by_line.setdefault(ln, cont)

    moved = []          # (行号, container, snippet)
    new_lines = []
    removed_rows = []
    for i, line in enumerate(lines):
        cont = cont_by_line.get(i + 1)
        if cont not in ("card", "other"):
            new_lines.append(line)
            continue
        if not FOOTNOTE_RE.search(line):
            new_lines.append(line)
            continue
        rest = line
        for m in FOOTNOTE_RE.finditer(line):
            moved.append((i + 1, cont, m.group(0)))
            rest = rest.replace(m.group(0), "", 1)
        if rest.strip():
            new_lines.append(rest)
        else:
            removed_rows.append(i + 1)

    bad = [x for x in moved if x[1] in ("card", "other")]
    print(f"可搬动脚注：共 {len(moved)} 条；其中需搬出（card/other）{len(bad)} 条")
    from collections import Counter
    print("  分布:", dict(Counter(x[1] for x in moved)))
    print(f"整行变空被删：{len(removed_rows)} 行")
    if bad:
        print(f"  需搬编号范围: {min(int(re.search(r'r(\d+)', s).group(1)) for _,_,s in bad)}"
              f" - {max(int(re.search(r'r(\d+)', s).group(1)) for _,_,s in bad)}")

    if dry:
        print("\n[dry-run] 不写盘")
        return

    # 备份
    shutil.copy2(HTML, BAK)
    print("已备份:", BAK)

    # 重新定位 srcs（行号已变）
    footnotes2, s2, e2 = scan_with_footer(new_lines)
    if s2 is None or e2 is None:
        print("!! 找不到 srcs 容器，终止"); return
    print(f"srcs 容器：开标签行 {s2+1} → 闭标签行 {e2+1}")

    # 按原行号顺序（=视觉顺序）插入 srcs 开头
    bad_sorted = sorted(bad, key=lambda x: x[0])
    ins = ["      " + s for _, _, s in bad_sorted]
    out = new_lines[:s2 + 1] + ins + new_lines[s2 + 1:]

    # ---- 写盘前三道自检（不通过就不落盘：脚本自己的失败模式不许是「沉默」）----
    text = "\n".join(out)
    n_before = len(FOOTNOTE_RE.findall(raw))
    n_after = len(FOOTNOTE_RE.findall(text))
    ok = True
    if n_after != n_before:
        print(f"!! 脚注总数变了 {n_before} -> {n_after}，拒绝写盘"); ok = False
    if text.count("<div") != text.count("</div>"):
        print(f"!! div 不平衡 {text.count('<div')}/{text.count('</div>')}，拒绝写盘"); ok = False
    fn_after, _, _ = scan_with_footer(out)
    if any(f[1] == "card" for f in fn_after):
        print(f"!! 仍有 {sum(1 for f in fn_after if f[1]=='card')} 条脚注在 card 内，拒绝写盘"); ok = False
    if not ok:
        print("未写盘，index.html 保持原样"); return

    open(HTML, "w", encoding="utf-8", newline="\n").write(text)
    print(f"已写盘：搬入 {len(ins)} 条脚注到 srcs 开头（脚注总数 {n_before} → {n_after} 不变）")


if __name__ == "__main__":
    main()
