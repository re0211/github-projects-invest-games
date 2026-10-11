# -*- coding: utf-8 -*-
"""E8 负对照探针：证明「脚注嵌进 card 内」是 E1–E7 的盲区，E8 才抓得住。

做法：在 index.html 的**副本**上，把一条已在 srcs 里的脚注**原样搬进**一张 card 内部
（总数、编号、卡片数、div 平衡全部不变），然后跑 index_metrics：
  - 期望 E1–E7 全绿（证明老判据看不见）
  - 期望 E8 报红（证明新判据抓得住）
再跑一次「不改动」的副本做正对照，期望全绿。

用法：python _r39/e8_negative_probe.py
"""
import os, re, shutil, sys, tempfile

sys.path.insert(0, r"D:\34498\Documents\_tools")
import index_metrics as im

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "index.html")
SNAP = os.path.join(BASE, "index_groups_snapshot.json")
TMP = os.path.join(BASE, "_r39", "_e8_fixture.html")

FN_RE = re.compile(r'<div id="r(\d+)"[^>]*>.*?</div>')


def build_fixture(move=True):
    src = io_open(HTML)
    m = FN_RE.search(src)
    if not m:
        raise SystemExit("找不到任何脚注")
    snip = m.group(0)
    if move:
        # 从原位删除
        src = src.replace(snip, "", 1)
        # 塞进第一张 card 的内部（card 开标签之后）
        card = re.search(r'<div class="card"[^>]*>', src)
        if not card:
            raise SystemExit("找不到 card")
        pos = card.end()
        src = src[:pos] + "\n      " + snip + src[pos:]
    return src


def io_open(p):
    import io
    return io.open(p, encoding="utf-8").read()


def check(src, label, expect_e8):
    import io
    io.open(TMP, "w", encoding="utf-8", newline="\n").write(src)
    m = im.measure(TMP)
    errs, warns, info = im.evaluate(m, im.snap_load(SNAP))
    e8 = [e for e in errs if e.startswith("E8")]
    others = [e for e in errs if not e.startswith("E8")]
    ok = (bool(e8) == expect_e8) and not others
    print(f"[{label}] E8={len(e8)} 条 | 其它判据报错={len(others)} 条 -> {'✅' if ok else '❌'}")
    for e in e8:
        print("      " + e[:110])
    for e in others:
        print("      其它: " + e[:110])
    return ok


def main():
    src = io_open(HTML)
    print("基准（未改动副本）：")
    ok0 = check(src, "正对照", expect_e8=False)
    print("\n负对照（把 1 条脚注搬进 card 内）：")
    ok1 = check(build_fixture(move=True), "负对照", expect_e8=True)
    if os.path.exists(TMP):
        os.remove(TMP)
    print("\n结论：", "✅ E8 有效且 E1–E7 确实是盲区" if (ok0 and ok1)
          else "❌ 探针未通过（E8 可能没接上，或引入了假警）")
    return 0 if (ok0 and ok1) else 1


if __name__ == "__main__":
    raise SystemExit(main())
