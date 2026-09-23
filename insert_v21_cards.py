# -*- coding: utf-8 -*-
"""
第二十一版增补：把第十五辑调研（GitHub 那一路）新发现的 4 个条目登记进 index.html。

注：这一轮的 GitHub 调研一共产出 21 条候选，全部通过 grep 去重 + `gh api` 逐条核实
（stars / license / language / pushed_at / archived 无一虚构）。
这里只登记与本工作区**直接对话**的 4 条，其余 17 条以链接形式留在
`csdn-social-summary.md` 第十五辑的表格里 —— **索引的容量不该被"顺手看到的"占满。**

数据来源：2026-09-21 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v21_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1074"'
FIRST_NEW_FOOTNOTE = 1075
MARKER = "第二十一版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十版增补 2026-09-21</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1075 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十一版增补 2026-09-21</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1079 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm21c1", name="opencodex（客户端与模型解耦的代理网关）",
        url="https://github.com/lidge-jun/opencodex",
        lang="TypeScript", stars="15,728",
        tags=[("t-make", "AI × 工具链"), ("t-ok", "已登记未安装")],
        plain="一个<strong>代理网关</strong>：把 Codex / Claude Code 这类编码 agent 发出的请求，"
              "转发到<strong>任意模型</strong>上。换句话说，它把「用哪个 agent 客户端」和"
              "「用哪个模型」这两件事<strong>拆开了</strong>。",
        analogy="本工作区的 <code>ccgs-cn-config</code> 解决的是<strong>同一件事</strong> —— "
                "把 Claude Code 桥接到上财的远程模型上。区别是：我们在本机自建、只为自己的场景；"
                "它是给所有人的通用网关。",
        ext=(80, "8.0/10", "「客户端与模型解耦」这个思路我们可以直接借："
                            "现在桥的目标是写死的，做成可配置的引擎层之后换模型只改一行"),
        use=(50, "5.0/10", "本机已有 <code>ccgs-cn-config</code> 且端到端验过，"
                            "<strong>现在不换</strong>；但它是同一问题的另一个实现，值得对照读一遍"),
        warn="<strong>15,728★ 这种体量意味着它的迭代非常快</strong> —— "
             "接口、支持的客户端版本都会变。要接的话先确认它支持哪个版本的哪个客户端，"
             "别照着半年前的教程配。",
        src="创建 2026 年 · 最近推送 2026-09-21 · 15,728★ · MIT · TypeScript · 信源 [1075]",
    ),
    dict(
        nid="rpm21c2", name="moyu（跨平台视觉小说引擎）",
        url="https://github.com/Icemic/moyu",
        lang="Rust", stars="97",
        tags=[("t-make", "游戏引擎"), ("t-ok", "已登记未安装")],
        plain="一个<strong>跨平台视觉小说引擎</strong>：用 React 写界面、用 QuickJS 跑脚本逻辑，"
              "输出到多个平台。作者是 Icemic（AVG.js / 「异次元」系列的作者），"
              "在这个方向上做了很多年。",
        analogy="它和 Ren'Py 是<strong>解决同一个问题的两条技术路线</strong> —— "
                "Ren'Py 是 Python + 自有脚本语言、生态成熟；它是 JS/Web 生态、偏前端思路。"
                "本作不会换引擎，但「<strong>别人怎么设计一个 VN 引擎</strong>」值得看。",
        ext=(60, "6.0/10", "可以对照它的「渲染与逻辑分层」看我们的 "
                            "<code>00_config.rpy</code> / <code>script.rpy</code> 切得对不对"),
        use=(20, "2.0/10", "本作已用 Ren'Py 跑到 v1.9（含中英双语 + 五道闸门），"
                            "<strong>不会换</strong>；作为引擎设计的参照物收录"),
        src="创建 2025 年 · 最近推送 2026-09-19 · 97★ · MPL-2.0 · Rust · 信源 [1076]",
    ),
    dict(
        nid="rpm21c3", name="agent-md（生产级 agent 指令集）",
        url="https://github.com/iamfakeguru/agent-md",
        lang="Shell", stars="968",
        tags=[("t-make", "AI × 工作流"), ("t-ok", "已登记未安装")],
        plain="一套<strong>写给编码 agent 的生产级指令集</strong>（<code>CLAUDE.md</code> / "
              "<code>AGENTS.md</code> 那一类），主流 agent 客户端即插即用。",
        analogy="和本工作区的 <code>agent-house-rules.md</code>（<strong>32 条房规</strong>）"
                "是同一个东西 —— 只不过它是<strong>公开分发的通用版</strong>，"
                "我们的是<strong>踩着自己的坑长出来的定制版</strong>。",
        ext=(70, "7.0/10", "**拿它的条目当外部对照**：看「别人普遍会踩什么」我们漏了哪些形态 —— "
                            "这是给房规做一次外部审计的现成材料"),
        use=(60, "6.0/10", "我们的房规更贴身（每条都对应一次真实踩坑），"
                            "但**通用版能补上「我们没遇到过的坑」**，值得花半小时对一遍"),
        src="创建 2025 年 · 最近推送 2026-09-21 · 968★ · MIT · Shell · 信源 [1077]",
    ),
    dict(
        nid="rpm21c4", name="gdmutant（变异测试：闸门自己也要被验）",
        url="https://github.com/kphutt/gdmutant",
        lang="Python", stars="3",
        tags=[("t-make", "测试 × 工具"), ("t-ok", "已登记未安装")],
        plain="<strong>变异测试</strong>工具：自动往代码里塞一个个小改动（“变异”），"
              "看测试还能不能抓住。抓不住 —— 说明那行代码<strong>根本没被真正测到</strong>。",
        analogy="这正是本工作区一直在做的事的**自动化版本**：第 9 轮我们手工把 "
                "<code>snark()</code> 的默认值从 2 改回 1，看 <code>check_balance.py</code> "
                "会不会报红；第 10 轮写了 <code>_tools/negcase_i18n.py</code> 做同样的事。"
                "**「闸门报绿」这件事本身要有证据** —— 它把这个思路变成了通用工具。",
        ext=(90, "9.0/10", "**这是本批里最值得借的一条思路**：把「反例实测」从手工脚本"
                            "升级成「自动变异 + 看闸门抓不抓得住」，"
                            "我们的 <code>check_*.py</code> 体系可以直接用这个方法体检"),
        use=(60, "6.0/10", "它是 GDScript 专用（本作用不了），**但方法论是通用的**；"
                            "3★ 说明还很新，别指望工具成熟 —— **价值在方法论，不在工具本身**"),
        warn="star 只有 3 —— 这不是「没人用」，是「刚起步」。"
             "收录它是因为**变异测试这件事本身**，不是因为它现在好用。",
        src="创建 2026 年 · 最近推送 2026-09-21 · 3★ · MIT · Python · 信源 [1078]",
    ),
]

FOOTNOTES = [
    ("1075", "https://github.com/lidge-jun/opencodex",
     "lidge-jun/opencodex", "15,728 · 2026-09-21 · MIT · TypeScript"),
    ("1076", "https://github.com/Icemic/moyu",
     "Icemic/moyu", "97 · 2026-09-19 · MPL-2.0 · Rust"),
    ("1077", "https://github.com/iamfakeguru/agent-md",
     "iamfakeguru/agent-md", "968 · 2026-09-21 · MIT · Shell"),
    ("1078", "https://github.com/kphutt/gdmutant",
     "kphutt/gdmutant", "3 · 2026-09-21 · MIT · Python"),
]


def b(s):
    """把 markdown 的 **粗体** 转成 HTML 的 <strong>。

    （写卡片文案时混用了两种写法，统一在这里转一次 —— 直接输出会显示成字面星号。）
    """
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

    desc = ('第十五辑的 GitHub 那一路一共产出 21 条候选，<strong>全部做过 grep 去重 + '
            '<code>gh api</code> 逐条核实</strong>（stars / license / language / pushed_at / archived，'
            '无一虚构）。这里只登记<strong>与本工作区直接对话的 4 条</strong>，'
            '其余 17 条以链接形式留在 <code>csdn-social-summary.md</code> 第十五辑里 —— '
            '<strong>索引的容量不该被「顺手看到的」占满</strong>：'
            '这 4 条各自回答了一个我们已经在做的事情（客户端与模型解耦 / 引擎设计 / agent 房规 / '
            '闸门自己也要被验）。')
    # 注意：上面这一段里两处全角括号是为了避开 .format —— 这里没用 format，但保持一致更安全

    block = ['    <div class="group" data-page-node-id="rpm21g">',
             '      <div class="group-title" data-page-node-id="rpm21gt">🆕 第二十一版增补 · 与前十四辑在做的四件事正面照面（4 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm21gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm21r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm21ra%s">%s</a> — %s</div>'
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
