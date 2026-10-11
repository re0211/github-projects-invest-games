# -*- coding: utf-8 -*-
"""第三十九辑补录（2026-10-12）：gh 路收尾时补交的 2 条高价值候选。
与 insert_v43_cards.py 同构（幂等/锚点断言/div 自检/重复仓库检测），但 MARKER 不同，可独立运行。
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1447"'
FIRST_NEW_FOOTNOTE = 1448
MARKER = "第四十三版补录"

HEAD_OLD = [
    '第四十三版增补 2026-10-12',
    '共 1448 个项目',
    '第四十三版增补 22 项（均与上版零重复）',
]
HEAD_NEW = [
    '第四十三版增补 2026-10-12 · 第四十三版补录 2026-10-12',
    '共 1450 个项目',
    '第四十三版增补 22 项 + 第四十三版补录 2 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm43c23",
        name="[AI] whymycompilefail/cpu-only-ai-tuber —— 纯 CPU 跑通整条 AI 主播链，三条结论全部反直觉",
        url="https://github.com/whymycompilefail/cpu-only-ai-tuber",
        lang="C++", stars="0",
        tags=[("t-make", "AI"), ("t-new", "新")],
        plain="**没有独显也能跑**的 AI 主播栈实测：Ultra 7 155H 核显跑通整条链路，含 llama.cpp 的 CPU 特化 fork。README 给了硬数字。",
        analogy="**三条结论全是反直觉的**：① **LLM 根本不是瓶颈** —— 391 ms 的 TTFT 只占整轮耗时 **2.7%**；"
                "② **压量化不提速反降速** —— Q8_0 35.3 → Q5_0 **28.3 GB/s**（内存带宽才是墙）；"
                "③ **人设跑偏不是 prompt 写得不好** —— 破人设率 3/15 → **0/15**，解法在**对话历史**里，不在 system prompt。",
        warn="⚠️ ★0、当天建仓（2026-10-11）、未经他人验证；但数字给得具体，可自行复现。"
             "另有一条容量上限：8 条/分钟，而直播间实际是 10–50 条/分钟。",
        ext=(72, "72", "「压量化不提速」「人设在对话历史里」两条是可直接迁移的结论，不限这个项目。"),
        use=(80, "80", "**对 16GB + 无独显的基准命中度最高的一条** —— 你就是这台机器，这三条能直接改你的用法。"),
        src="创建 2026-10-11 · 推送 2026-10-11 · 0★ · MIT · C++ · REST 实测 · 信源 [1448]",
    ),
    dict(
        nid="rpm43c24",
        name="[AI] Hayliy/naixi-desktop —— 规模最硬的量化样本（7.9 万行 / 222 端点 / 29 张表）",
        url="https://github.com/Hayliy/naixi-desktop",
        lang="Python", stars="0",
        tags=[("t-make", "AI"), ("t-mod", "模块化")],
        plain="第一方代码约 **7.9 万行**（Python 43,083 / 前端 35,331 / Rust 571），**56** 个 Python 模块、**222** 个 REST 端点、**29** 张 SQLite 表、633 次提交；架构是 **Python sidecar（aiohttp）+ PySide6 桌宠 + Live2D/VRM 双格式 + 内置 SearXNG**。",
        analogy="别的项目 README 写「能聊天能记忆」，这条直接把**体量数字**摊开 —— 7.9 万行是什么概念：**它不是 demo，是真做完的工程量**。",
        warn="⚠️ ★0、Apache-2.0、仓库 89.4 MB；双格式（Live2D + VRM）同一宿主。",
        ext=(68, "68", "「Python sidecar + 桌面壳」这个切法值得抄：大脑用 Python，壳用 Qt。"),
        use=(45, "45", "★0 没人背书，别指望开箱即用；当作「这类项目做到底有多大」的标尺。"),
        src="创建 2026-07-24 · 推送 2026-10-10 · 0★ · Apache-2.0 · Python · REST 实测 · v1.2.0 · 信源 [1449]",
    ),
]

FOOTNOTES = [
    (1448, "https://github.com/whymycompilefail/cpu-only-ai-tuber", "whymycompilefail/cpu-only-ai-tuber",
     "0★ · MIT · C++ · 建仓/推送 2026-10-11 · REST 实测 · **纯 CPU（无独显）跑通 AI 主播链**；"
     "硬数字：TTFT 391 ms 占整轮 2.7% / Q8_0 35.3→Q5_0 **28.3 GB/s（压量化反降速）** / 破人设 3/15→**0/15（解法在对话历史）**"),
    (1449, "https://github.com/Hayliy/naixi-desktop", "Hayliy/naixi-desktop",
     "0★ · Apache-2.0 · Python · 推送 2026-10-10 · REST 实测 · v1.2.0 · **7.9 万行 / 56 模块 / 222 REST 端点 / 29 张 SQLite 表**；"
     "Python sidecar(aiohttp) + PySide6 桌宠 + Live2D/VRM + 内置 SearXNG"),
]


def b(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)


def render_card(c):
    n = c["nid"]
    name_inner = ('<a href="%s" target="_blank" data-page-node-id="%sn">%s</a>'
                  % (c["url"], n, c["name"])) if c["url"] else c["name"]
    tags = "\n".join(
        '          <span class="tag %s" data-page-node-id="%st%d">%s</span>'
        % (cls, n, i, txt) for i, (cls, txt) in enumerate(c["tags"], 1))
    extra = ""
    if c.get("warn"):
        extra += ('        <div class="analogy" data-page-node-id="%sw"><b data-page-node-id="%swb">'
                  '注意：</b>%s</div>\n' % (n, n, c["warn"]))
    return '''      <div class="card" data-page-node-id="{n}">
        <div class="card-top" data-page-node-id="{n}t">
          <span class="card-name" data-page-node-id="{n}mn">{name}</span>
          <span class="lang" data-page-node-id="{n}l">{lang}</span>
          <span class="stars" data-page-node-id="{n}s">{stars}</span>
{tags}
        </div>
        <p class="plain" data-page-node-id="{n}p">{plain}</p>
        <div class="analogy" data-page-node-id="{n}a"><b data-page-node-id="{n}ab">打个比方：</b>{analogy}</div>
{extra}        <div class="grid2" data-page-node-id="{n}g">
          <div class="mini" data-page-node-id="{n}m1"><span class="lbl" data-page-node-id="{n}m1l">可拓展性</span><div class="bar" data-page-node-id="{n}m1b"><div class="bar-track" data-page-node-id="{n}m1t"><div class="bar-fill" style="width:{ew}%;background:var(--make)" data-page-node-id="{n}m1f"></div></div><span class="bar-num" data-page-node-id="{n}m1n">{en}</span></div><div class="val" style="margin-top:6px" data-page-node-id="{n}m1v">{ev}</div></div>
          <div class="mini" data-page-node-id="{n}m2"><span class="lbl" data-page-node-id="{n}m2l">实用性</span><div class="bar" data-page-node-id="{n}m2b"><div class="bar-track" data-page-node-id="{n}m2t"><div class="bar-fill" style="width:{uw}%;background:var(--make)" data-page-node-id="{n}m2f"></div></div><span class="bar-num" data-page-node-id="{n}m2n">{un}</span></div><div class="val" style="margin-top:6px" data-page-node-id="{n}m2v">{uv}</div></div>
        </div>
        <div class="src-line" data-page-node-id="{n}c">{src}</div>
      </div>
'''.format(n=n, name=name_inner, lang=c["lang"], stars=c["stars"], tags=tags,
           plain=b(c["plain"]), analogy=b(c["analogy"]), extra=b(extra),
           ew=c["ext"][0], en=c["ext"][1], ev=b(c["ext"][2]),
           uw=c["use"][0], un=c["use"][1], uv=b(c["use"][2]), src=c["src"])


def main():
    src = open(HTML, encoding="utf-8").read()

    if MARKER in src:
        print("已存在%s，跳过（幂等）" % MARKER)
        return 0

    bad = []
    for o in HEAD_OLD:
        if src.count(o) != 1:
            bad.append("页头锚点出现 %d 次（要求 1）：%s" % (src.count(o), o[:60]))
    for num, _u, _s, _m in FOOTNOTES:
        if ('id="r%s"' % num) in src:
            bad.append("信源 [%s] 已被占用" % num)
    for c in CARDS:
        if c["url"] and "github.com/" in c["url"]:
            slug = c["url"].split("github.com/")[-1].lower()
            if slug in src.lower():
                bad.append("仓库已存在，别重复登记：%s" % c["url"])

    si = src.find(SECTION_S3)
    if src.count(SECTION_S3) != 1:
        bad.append("%s 出现 %d 次" % (SECTION_S3, src.count(SECTION_S3)))
        ins = -1
    else:
        ins = si

    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if bad or ins < 0 or fend < 0:
        for x in bad:
            print("❌ " + x)
        print("未改动 index.html")
        return 1

    desc = ('第三十九辑补录（2 项）：gh 路收尾时补交的两条高价值候选。**① 纯 CPU（无独显）跑通整条 AI 主播链** —— '
            '三条结论全部反直觉：LLM 只占整轮耗时 2.7%、压量化反而降速、人设跑偏的根源在对话历史而非 system prompt；'
            '**② 规模最硬的量化样本** —— 7.9 万行 / 222 个 REST 端点 / 29 张 SQLite 表，是判断「这类项目做到底有多大」的标尺。')

    block = ['    <div class="group" data-page-node-id="rpm43bg">',
             '      <div class="group-title" data-page-node-id="rpm43bgt">🆕 第四十三版补录 · 纯 CPU 主播链的三条反直觉结论 + 规模最硬的样本（2 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm43bgd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')

    # ⚠️ 顺序同 v43：先插位置靠后的脚注，再插位置靠前的卡片组
    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm43br%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm43bra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    for o, n in zip(HEAD_OLD, HEAD_NEW):
        if src.count(o) != 1:
            print("二次校验失败：页头锚点 %s 出现 %d 次" % (o[:40], src.count(o)))
            return 1
        src = src.replace(o, n)

    open(HTML, "w", encoding="utf-8").write(src)
    print("✅ 已插入 %s：%d 张卡 + %d 条脚注（[%d]-[%d]）"
          % (MARKER, len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE, FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    print("   页头：1448 → 1450 项；卡片 1431 → %d" % (1431 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
