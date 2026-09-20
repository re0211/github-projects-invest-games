# -*- coding: utf-8 -*-
"""
第十六版增补：把第十一辑调研新发现的 5 个条目登记进 index.html。

为什么继续用脚本而不是手改 HTML（沿用上一版的三条理由）：
  1) 一张卡片有 20 多个 `data-page-node-id`，手写必然漏；
  2) 先断言"锚点存在且只出现一次"，**全部通过才落盘** —— 避免写出一个
     半改半没改的页面（同 amphoreus-roast/tools/insert_sprites.py 的纪律）；
  3) 顺手把页头计数与信源脚注一起改掉，三处改动不会漏。

这一版的主题和历史几版不一样：**不再是"用 AI 写代码"，而是"AI agent 直接驱动引擎"。**
所以这批项目清一色是 MCP 服务器 —— 而且第一次出现了 Ren'Py 的 MCP 生态
（在此之前 Ren'Py 被本项目判定为"纯文本，不需要 MCP"）。
⭐ 这 5 个都不大（4~60 星），价值在**方向信号**，不在成熟度。

数据来源：2026-09-20 用 GitHub REST API 实测（stars / language / license / pushed_at），
**没有一个数字是估的**（房规 9：别编造内容）。

幂等：脚本开头检查目标标记是否已存在，已存在则退出 0，不会重复插入。

用法：python insert_v16_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

# 插在「游戏拓展与解包」section 之前 = 「游戏制作（含 AI 制作游戏专题）」的末尾
SECTION_S3 = '<section id="s3"'
# 最后一条脚注的起点（脚注编号实测 1~1059）
LAST_FOOTNOTE_MARK = '<div id="r1059"'
FIRST_NEW_FOOTNOTE = 1060
MARKER = "第十六版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十五版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1060 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十六版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1065 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项（均与上版零重复）</span>',
]

# ---------------------------------------------------------------------------
# 卡片内容。stars / lang / license / 推送日期全部来自 2026-09-20 的 GitHub API 实测。
# ---------------------------------------------------------------------------
CARDS = [
    dict(
        nid="rpm16c1", name="renpy_mcp_server",
        url="https://github.com/banjtheman/renpy_mcp_server",
        lang="TypeScript", stars="60",
        tags=[("t-make", "视觉小说"), ("t-ok", "4 个同类里星最多")],
        plain="Ren'Py 的 MCP 服务器：让 AI 助手直接建项目、出背景、出带 5 档表情的立绘、写分支剧本、再编译成网页版预览。走的是 Gemini 2.5 Flash Image 出图，立绘<b>自带背景移除</b>，所以出来就是透明底。一条 setup.sh 把 SDK 和 web 支持模块一起装好。",
        analogy="它把<b>视觉小说这一套流水线整条端上来了</b>——我们做《翁法罗斯吐槽实录》时，绿幕生图、抠图、写脚本、lint、打包是五六个手工环节拼起来的，它是把它们串成一串工具调用。",
        ext=(70, "7.0/10", "MIT，工具按环节切分，能只用其中几步（比如只要出图那两步）；不锁死客户端"),
        use=(60, "6.0/10", "60★ 是这批里最成熟的；但最后推送是 2026-02，比其它几个旧，用前先看它认不认你的 SDK 版本"),
        src="最近推送 2026-02-01 · MIT · 信源 [1060]",
    ),
    dict(
        nid="rpm16c2", name="Muanchen2/renpy-mcp（CJK 自动配字体）",
        url="https://github.com/Muanchen2/renpy-mcp",
        lang="Python", stars="21",
        tags=[("t-make", "中文字体"), ("t-warn", "字体授权有坑")],
        plain="7 个工具、570 行纯 Python 的 Ren'Py MCP：列 label、读某个 label 的全文、<b>按 7 种定位模式注入代码</b>、编译、lint、拷素材、量图片尺寸。它的卖点是<b>检测到中文就自动配字体</b>。",
        analogy="本项目踩过的第 1 号坑就是\u201c中文满屏豆腐块\u201d，看到\u201c自动配字体\u201d很容易想装。<b>实测结论是别装</b>：它的判据是\u201c字体名不在我的白名单里就需要修\u201d，于是把我们合规的思源黑体换成了系统的中易黑体（simhei）—— 后者是商业字体，拷进游戏发行 = 版权风险。详见下面的自测结论。",
        ext=(55, "5.5/10", "工具切得干净（读 / 写 / 编译 / lint 各自独立），exec_rpy 的 7 种定位模式值得抄"),
        use=(35, "3.5/10", "对**已经配好 CJK 字体**的项目是负收益；它真正有用的场景是\u201c从零新建一个中文项目\u201d，而且必须自己把字体换成 OFL 的"),
        warn="实测：把 gui.rpy 里 3 处 `fonts/SourceHanSansLite.ttf` 全部替换成 `simhei.ttf`，并从 C:\\Windows\\Fonts 拷贝该字体进 game/。**能跑，但商用有版权风险。**（它改了会先写 gui.rpy.bak 备份，这点比多数工具强）",
        src="最近推送 2026-06-01 · MIT · 信源 [1061]",
    ),
    dict(
        nid="rpm16c3", name="fracturedring/renpy-mcp（带浏览器编辑器）",
        url="https://github.com/fracturedring/renpy-mcp",
        lang="Python", stars="16",
        tags=[("t-make", "74 工具"), ("t-warn", "AGPL-3.0 有传染性")],
        plain="Ren'Py 的\u201c<b>三条路都能走</b>\u201d工具包：一个浏览器里的 Ren'Py 编辑器，加一个 74 个工具的 MCP 服务器。喜欢点鼠标的用编辑器，喜欢写代码的写代码，喜欢说话的就跟 Claude Code / Cursor 说。",
        analogy="很多工具会逼你选一种姿势（要么全自动、要么全手写）。它是<b>在同一个项目上留下三种入口</b>——改一个场景用编辑器、批量改五十处用代码、想不清楚的时候问 AI。",
        ext=(65, "6.5/10", "74 个工具的覆盖面是这批里最宽的；但 AGPL-3.0 传染性强，**商用前一定要确认自己的用法**"),
        use=(50, "5.0/10", "16★、最后推送 2026-04；当\u201cRen'Py 能被 MCP 玩到什么程度\u201d的参考样本更合适"),
        src="最近推送 2026-04-26 · AGPL-3.0 · 信源 [1062]",
    ),
    dict(
        nid="rpm16c4", name="renpy-mcp-pro-public",
        url="https://github.com/youichi-uda/renpy-mcp-pro-public",
        lang="Python · 另有网页版", stars="4",
        tags=[("t-make", "剧情地图"), ("t-warn", "无 LICENSE 文件")],
        plain="60 个工具的 Ren'Py MCP，外加**剧情地图**、实时面板和一个独立 CLI。它的定位不是\u201c帮我写代码\u201d，而是<b>\u201c让我看清楚这个项目长什么样\u201d</b>——分支走到哪、哪条线还没写、谁的台词占比最高。",
        analogy="写剧本写到第七天，人已经记不清\u201c第三天那个选项到底通向哪里\u201d。剧情地图就是<b>把脑内那张图搬到屏幕上</b>——这类工具解决的不是产能，是失控。",
        ext=(60, "6.0/10", "有独立 CLI，不接 MCP 也能用；有公开的网页版可以直接看界面"),
        use=(40, "4.0/10", "4★、**仓库里没有 LICENSE 文件**（默认保留全部权利），当参考可以，别直接拿来嵌进产品"),
        warn="无许可证文件 = 默认版权归作者所有，不授予使用许可。想用先联系作者。",
        src="最近推送 2026-03-17 · 无 LICENSE · 信源 [1063]",
    ),
    dict(
        nid="rpm16c5", name="mosaic-bridge（Unity，约 290 个工具）",
        url="https://github.com/MosaicXR-AI/mosaic-bridge",
        lang="C#", stars="10",
        tags=[("t-make", "Unity"), ("t-ok", "工具面最大")],
        plain="Unity 编辑器插件 + MCP 服务器，<b>约 290 个专门化工具</b>，覆盖程序化生成、模拟、物理、渲染、AI 行为，很多来自已发表的论文。支持 Claude / Cursor / Gemini 等 MCP 客户端。",
        analogy="别的 Unity MCP 给你\u201c建对象、改材质\u201d这类积木，它给的是<b>\u201c跑一遍这套物理、按这篇论文生成这个行为\u201d</b>这种已经组装好的模块。工具多到 290 个也意味着：模型选错工具的概率同步上升。",
        ext=(75, "7.5/10", "工具按域切分且有论文出处，可以只要自己那一个域；仓库自述 Apache 2.0"),
        use=(45, "4.5/10", "10★、2026-04 建。工具面大是优点也是负担——**先想清楚要它做什么，再装**，否则光是工具选择就把上下文吃光"),
        warn="GitHub API 返回的 license 是 NOASSERTION（仓库自述 Apache 2.0，但仓库里可能不是标准文本）。商用前请自己核一遍 LICENSE。",
        src="最近推送 2026-09-16 · 自述 Apache 2.0 · 信源 [1064]",
    ),
]

FOOTNOTES = [
    ("1060", "https://github.com/banjtheman/renpy_mcp_server",
     "banjtheman/renpy_mcp_server", "60 · 2026-02-01 · MIT"),
    ("1061", "https://github.com/Muanchen2/renpy-mcp",
     "Muanchen2/renpy-mcp", "21 · 2026-06-01 · MIT"),
    ("1062", "https://github.com/fracturedring/renpy-mcp",
     "fracturedring/renpy-mcp", "16 · 2026-04-26 · AGPL-3.0"),
    ("1063", "https://github.com/youichi-uda/renpy-mcp-pro-public",
     "youichi-uda/renpy-mcp-pro-public", "4 · 2026-03-17 · 无 LICENSE"),
    ("1064", "https://github.com/MosaicXR-AI/mosaic-bridge",
     "MosaicXR-AI/mosaic-bridge", "10 · 2026-09-16 · 自述 Apache 2.0"),
]


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
           plain=c["plain"], analogy=c["analogy"], extra=extra,
           ew=c["ext"][0], en=c["ext"][1], ev=c["ext"][2],
           uw=c["use"][0], un=c["use"][1], uv=c["use"][2], src=c["src"])


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

    # 同名仓库不能重复登记
    for c in CARDS:
        if c["url"] and c["url"].split("github.com/")[-1].lower() in src.lower():
            bad.append("仓库已存在，别重复登记：%s" % c["url"])

    si = src.find(SECTION_S3)
    if src.count(SECTION_S3) != 1:
        bad.append("%s 出现 %d 次（要求 1）" % (SECTION_S3, src.count(SECTION_S3)))
        ins = -1
    else:
        ins = si
        seg = src[src.find("<section", 10000):si]
        d = 0
        for m in re.finditer(r"<div[\s>]|</div>", seg):
            d += 1 if m.group(0).startswith("<div") else -1
        if d != 0:
            bad.append("插入点前 div 深度为 %d（应为 0），会嵌错层" % d)

    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次（要求 1）" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if bad:
        print("锚点校验失败，未改动文件：")
        for b in bad:
            print("  " + b)
        return 1

    block = ['    <div class="group" data-page-node-id="rpm16g">',
             '      <div class="group-title" data-page-node-id="rpm16gt">🆕 第十六版增补 · AI agent 直接驱动引擎（Unity / Ren\'Py 的 MCP 接入，5 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm16gd">这一批和前几版的方向不一样：不再是「用 AI 写代码」，而是<strong>让 AI agent 直接操作引擎</strong>。五个都是 MCP 服务器，而且第一次出现了 Ren\'Py 的 MCP 生态。共同点：<strong>星都不多（4~60），价值在方向信号，不在成熟度</strong>；三个 Ren\'Py 项目里有 1 个已知的字体授权坑（见第 2 张卡）。星级 / 语言 / 协议为 2026-09-20 用 GitHub API 实测。</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm16r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm16ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]

    for old, new in zip(HEAD_OLD, HEAD_NEW):
        src = src.replace(old, new, 1)

    open(HTML, "w", encoding="utf-8", newline="\n").write(src)

    print("OK  插入 %d 张卡片 + %d 条信源脚注（[%s]-[%s]）+ 3 处页头计数"
          % (len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE,
             FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
