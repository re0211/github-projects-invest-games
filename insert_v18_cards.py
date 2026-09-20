# -*- coding: utf-8 -*-
"""
第十八版增补：把第十三辑调研新发现的 2 个条目登记进 index.html。

主题：**「验证侧」**——AI 把"做出来"变便宜之后，焦点挪到"怎么证明它对"。
两张卡都是方向信号（一个 183★ 的论文代码、一个 0★ 的挑战赛作业），
评分口径不变：价值在方向信号不在成熟度。

数据来源：2026-09-20 用 GitHub REST API 实测（stars / language / license / pushed_at），
没有一个数字是估的。幂等：已存在标记则退出 0。

用法：python insert_v18_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1070"'
FIRST_NEW_FOOTNOTE = 1071
MARKER = "第十八版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十七版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1071 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十八版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1073 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm18c1", name="pwm（Programmable World Model）",
        url="https://github.com/AlayaLab/pwm",
        lang="论文配套代码", stars="183",
        tags=[("t-make", "世界模型"), ("t-ok", "方向信号")],
        plain="arXiv:2609.10540 的官方仓库。视频世界模型玩久了会「变糊」——状态只存在于生成的像素里。它的路线很决绝：<strong>别让像素管状态，让程序管</strong>。agent 把规则翻译成可执行程序，轻量引擎维护显式、持久的全局世界状态（含屏幕外实体和背包），预训练视频模型只当渲染器。",
        analogy="和第十辑那条「AI 的『合理』基于视觉常识、游戏的『可行走』基于数学碰撞」是<strong>同一个命题的另一面</strong>：状态也一样，靠概率模型记逻辑账必然漂。CombatStateBench 上自报 94% 计数 / 98% 状态准确率（自报数字，等独立复现）。",
        ext=(75, "7.5/10", "「程序管状态 + 模型管渲染」的分工可以直接抄到任何 LLM 驱动的模拟里；CombatStateBench 一起开源"),
        use=(25, "2.5/10", "要 GPU、偏研究，视觉小说用不上。登记它是方向信号：世界模型这条线的下一步是「可编程」，不是「更大」"),
        warn="GitHub API 未返回标准 license 文本，商用前自己核 LICENSE。",
        src="最近推送 2026-09-10 · 无协议文本 · 信源 [1071]",
    ),
    dict(
        nid="rpm18c2", name="AI-sandbox（Gemma 4 NPC 沙盒）",
        url="https://github.com/CrazyDashTool/AI-sandbox",
        lang="GDScript", stars="0",
        tags=[("t-make", "游戏 × AI"), ("t-ok", "附图提示词实证")],
        plain="Gemma 4 挑战赛参赛作：Godot 4 沙盒里住着一个 AI NPC。每次思考都把世界状态、玩家近期行为、对话记忆、天气，<strong>加一张 NPC 自己视角的 1280×720 截图</strong>发给 Gemma 4 31B，换回一个 JSON 决策（speech / action / emotion），解析成真实游戏行为。",
        analogy="「截图进提示词」在这里被用来当 <strong>NPC 的眼睛</strong>——按钮美术改了它也认识，不用写死坐标。和第十辑学的「附图 &gt; 写话」是同一个道理，这次是在感知侧。",
        ext=(55, "5.5/10", "MIT、Godot 4 + GDScript，NPC 感知-决策-执行这条链路的实现可读；提示词模板完整"),
        use=(30, "3.0/10", "0★ 挑战赛作业，NPC 要 31B 模型，本机跑不动。抄的是「截图当感知输入 + JSON 当动作接口」这个结构，不是代码"),
        warn="仓库推送日期是 2026-05-20，比挑战赛文章早——项目是老的，贴是补的宣传。按 M-0002 纪律照实记录。",
        src="最近推送 2026-05-20 · MIT · 信源 [1072]",
    ),
]

FOOTNOTES = [
    ("1071", "https://github.com/AlayaLab/pwm",
     "AlayaLab/pwm", "183 · 2026-09-10 · 无协议文本"),
    ("1072", "https://github.com/CrazyDashTool/AI-sandbox",
     "CrazyDashTool/AI-sandbox", "0 · 2026-05-20 · MIT"),
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

    desc = ('这一批只有两张卡，关键词是<strong>「验证侧」</strong>：一个把世界模型的状态交给程序管'
            '（像素只负责渲染），一个给沙盒 NPC 装上「自己的眼睛」（截图当感知输入）。'
            '<strong>星级都不高（183 / 0），价值在方向信号不在成熟度</strong>——'
            '它们和本工作区一直在做的「闸门 + 截图证据」是同一件事在不同尺度上的样子。'
            '星级 / 语言 / 协议为 2026-09-20 用 GitHub API 实测。')

    block = ['    <div class="group" data-page-node-id="rpm18g">',
             '      <div class="group-title" data-page-node-id="rpm18gt">🆕 第十八版增补 · 验证侧：程序管状态、截图当眼睛（2 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm18gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm18r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm18ra%s">%s</a> — %s</div>'
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
