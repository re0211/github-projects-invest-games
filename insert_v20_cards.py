# -*- coding: utf-8 -*-
"""
第二十版增补：把第十五辑调研新发现的 1 个条目登记进 index.html。

主题：**「把人工环节交给工具」**——上一辑讲"可达性"（验的那一侧），
这一辑看"做"的那一侧：凡是能自动化的环节，都不该继续靠人对账。

这一张卡和第 10 轮（英文版）直接相关：
Ren'Py 本地化这件事，本工作区是**手工对账**做完的（586 条中文字面量里 166 条提取不到），
而社区里已经有人把它做成了工具。

数据来源：2026-09-21 用 GitHub REST API 实测
（stars / forks / language / license / created_at / pushed_at），没有一个数字是估的。
幂等：已存在标记则退出 0。

用法：python insert_v20_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1073"'
FIRST_NEW_FOOTNOTE = 1074
MARKER = "第二十版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十九版增补 2026-09-21</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1074 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十版增补 2026-09-21</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1075 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm20c1", name="RenLocalizer（Ren'Py 多引擎翻译器）",
        url="https://github.com/Lord0fTurk/RenLocalizer",
        lang="Python", stars="35",
        tags=[("t-make", "游戏 × AI"), ("t-ok", "已登记未安装")],
        plain="一个<strong>桌面软件</strong>（不是命令行脚本）：打开就能自动翻译 Ren'Py 视觉小说的 "
              "<code>.rpy</code> 文件，可以切换多个翻译引擎，也支持走<strong>本地模型</strong>。"
              "换句话说，它把本工作区第 10 轮手工做过的那条链——"
              "「从 <code>.rpy</code> 里抽出所有要翻的字 → 翻译 → 回填」——做成了工具。",
        analogy="它和本作的 <code>tl/english/</code> 官方翻译层是<strong>两条路</strong>："
                "它省力（一键跑完），我们可维护（走引擎的翻译层 + 五道闸门验漏）。"
                "已经在做的项目继续走官方层更划算，新项目可以拿它省第一遍的力。",
        ext=(70, "7.0/10", "「多翻译引擎可切换」这个设计值得抄："
                            "我们现在要换翻译模型就等于改流程，换成引擎层之后只改一个配置"),
        use=(30, "3.0/10", "本作英文版已翻完且过了 R1~R5 五道闸门，再用它跑一遍"
                            "只会覆盖掉已经人工校对过的译文。"
                            "正确用法是「下一个项目的第一遍」或「新增大量台词后的初翻」"),
        warn="协议是 <code>NOASSERTION</code>（仓库里没有标准 license 文件）——"
             "自己用没问题，<strong>要分发或商用之前先看清它的授权说明</strong>。",
        src="创建 2025-09-10 · 最近推送 2026-09-13 · 35★ · 11 forks · Python · 信源 [1074]",
    ),
]

FOOTNOTES = [
    ("1074", "https://github.com/Lord0fTurk/RenLocalizer",
     "Lord0fTurk/RenLocalizer", "35 · 2026-09-13 · Python · 11 forks"),
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

    desc = ('这一批只有一张卡：一个 Ren\'Py 视觉小说的<strong>多引擎自动翻译器</strong>。'
            '收录它的理由不是"它能替我们干活"，而是 —— '
            '<strong>第 10 轮做英文版时我们手工对账了 586 条中文字面量、其中 166 条 SDK 提取不到</strong>，'
            '而这种"提取不到"的边角（角色名、<code>textbutton</code>、<code>renpy.input</code>、'
            'screen 里的 <code>text</code>、数据表）<strong>任何同类工具都必须面对同一批</strong>。'
            '读它怎么处理，比再读一遍官方文档快。'
            '星级 / 语言 / 协议 / forks 为 2026-09-21 用 GitHub API 实测。')

    block = ['    <div class="group" data-page-node-id="rpm20g">',
             '      <div class="group-title" data-page-node-id="rpm20gt">🆕 第二十版增补 · 把人工环节交给工具（1 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm20gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm20r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm20ra%s">%s</a> — %s</div>'
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
