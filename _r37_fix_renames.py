# -*- coding: utf-8 -*-
"""第三十七辑：修正 22 个改名仓库的 href + 显示名（来源：第三十五辑 GraphQL canonical 名）。

安全设计：
  - 只做「精确串替换」，不做正则模糊匹配；
  - 改前先断言每个旧路径出现次数 == 预期（2 个 href + 1 个脚注显示名）；
  - 改后断言旧路径计数 == 0、页头数字不变、div 计数不变；
  - --dry-run 只报告不落盘。
"""
import re
import sys
import shutil
from pathlib import Path

REPO = Path(r"D:\34498\Documents\github-projects-invest-games")
IDX = REPO / "index.html"

# (旧路径, 新路径, 旧短名(卡面显示，可为空=不改), 新短名)
RENAMES = [
    ("block/goose", "aaif-goose/goose", "", ""),
    ("Bin-Huang/chatbox", "chatboxai/chatbox", "", ""),
    ("hiyouga/LLaMA-Factory", "hiyouga/llamafactory", "LLaMA-Factory", "llamafactory"),
    ("pytorch/torchtune", "meta-pytorch/torchtune", "", ""),
    ("oobabooga/text-generation-webui", "oobabooga/textgen", "", ""),
    ("KwaiVGI/LivePortrait", "klingairesearch/liveportrait", "", ""),
    ("FunAudioLLM/CosyVoice", "qwenaudio/cosyvoice", "", ""),
    ("ltdrdata/ComfyUI-Manager", "comfy-org/comfyui-manager", "", ""),
    ("intel-analytics/ipex-llm", "intel/ipex-llm", "", ""),
    ("qodo-ai/pr-agent", "the-pr-agent/pr-agent", "", ""),
    ("sjtu-ipads/powerinfer", "tiiny-ai/powerinfer", "", ""),
    ("itzcrazykns/perplexica", "itzcrazykns/vane", "", ""),
    ("streetpea/chiaki-ng", "chiaki-ng/chiaki-ng", "", ""),
    ("RaiMan/SikuliX1", "oculix-org/sikulix1", "", ""),
    ("haosulab/maniskill", "mani-skill/maniskill", "", ""),
    ("kolbytn/mindcraft", "mindcraft-bots/mindcraft", "", ""),
    ("genesis-embodied-ai/genesis", "genesis-embodied-ai/genesis-world", "", ""),
    ("laude-institute/terminal-bench", "harbor-framework/terminal-bench-1", "", ""),
    ("riffusion/riffusion", "riffusion/riffusion-hobby", "", ""),
    ("RamiLego4Game/LIKO-12", "liko-12/liko-12", "", ""),
    ("Dryxio/auto-re-agent", "dryxio/reagent", "Dryxio/auto-re-agent", "dryxio/reagent"),
    ("JakeSelby/agent-harness", "jakeselby/model-citizen", "", ""),
]


def main() -> int:
    dry = "--dry-run" in sys.argv
    html = IDX.read_text(encoding="utf-8")
    orig = html

    # 页头数字（改前基线）
    m = re.search(r"共\s*([\d,]+)\s*个项目", html)
    head_before = m.group(1) if m else "?"
    div_before = (html.count("<div"), html.count("</div>"))

    print(f"[基线] 页头 {head_before} 项 · <div> {div_before[0]} / </div> {div_before[1]}")
    print(f"{'':2} {'旧路径':42} {'href改':>6} {'脚注改':>6} {'卡面改':>6}  备注")
    print("-" * 100)

    total_href = total_fn = total_card = 0
    problems = []

    for old, new, old_short, new_short in RENAMES:
        # 1) href（含引号边界，避免前缀误吞）
        href_old = f'https://github.com/{old}"'
        href_new = f'https://github.com/{new}"'
        n_href = html.count(href_old)
        # 2) 脚注显示名  >old</a>
        fn_old = f'>{old}</a>'
        fn_new = f'>{new}</a>'
        n_fn = html.count(fn_old)
        # 3) 卡面短名（可选）
        n_card = 0
        c_old = ""
        if old_short:
            c_old = f'>{old_short}</a>'
            if c_old == fn_old:
                # 短名 == 「owner/repo」型显示名：卡面与脚注是同一个串，fn 替换已一并处理
                c_old = ""
            else:
                n_card = html.count(c_old)
                if n_card != 1:
                    problems.append(f"{old}: 卡面短名 `{old_short}` 命中 {n_card}（预期 1）")

        note = ""
        if n_href != 2:
            problems.append(f"{old}: href 命中 {n_href}（预期 2）")
            note += f"⚠href={n_href} "
        if n_fn != 1:
            problems.append(f"{old}: 脚注显示名命中 {n_fn}（预期 1）")
            note += f"⚠fn={n_fn} "
        if old != new and n_href == 0 and n_fn == 0:
            note += "（已改过？）"

        print(f"  {old:42} {n_href:>6} {n_fn:>6} {n_card:>6}  {note}")
        total_href += n_href
        total_fn += n_fn
        total_card += n_card

        html = html.replace(href_old, href_new)
        html = html.replace(fn_old, fn_new)
        if c_old:
            html = html.replace(c_old, f'>{new_short}</a>')

    print("-" * 100)
    print(f"[合计] href {total_href} · 脚注 {total_fn} · 卡面 {total_card}")

    # 改后断言
    leftover = [(o, html.count(f'https://github.com/{o}"')) for o, n, *_ in RENAMES]
    bad = [x for x in leftover if x[1] != 0]
    div_after = (html.count("<div"), html.count("</div>"))
    m2 = re.search(r"共\s*([\d,]+)\s*个项目", html)
    head_after = m2.group(1) if m2 else "?"

    ok = True
    if bad:
        print(f"❌ 旧路径仍有残留：{bad}")
        ok = False
    if div_before != div_after:
        print(f"❌ div 计数变了：{div_before} -> {div_after}")
        ok = False
    if head_before != head_after:
        print(f"❌ 页头数字变了：{head_before} -> {head_after}")
        ok = False
    if problems:
        print("⚠ 预检问题：")
        for p in problems:
            print("   -", p)

    print(f"[改后] 页头 {head_after} 项 · <div> {div_after[0]} / </div> {div_after[1]}")

    if not ok:
        print("=> 未落盘（断言失败）")
        return 2
    if dry:
        print("=> dry-run：未落盘")
        return 0

    bak = REPO / "_r37" / "index.html.pre-rename.bak"
    bak.parent.mkdir(exist_ok=True)
    if not bak.exists():
        shutil.copy2(IDX, bak)
    if html == orig:
        print("=> 无变化，未写盘")
        return 0
    IDX.write_text(html, encoding="utf-8")
    print(f"=> 已落盘 index.html；备份 {bak}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
