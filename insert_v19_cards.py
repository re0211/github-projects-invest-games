# -*- coding: utf-8 -*-
"""
第十九版增补：把第十四辑调研新发现的 1 个条目登记进 index.html。

主题：**「可达性」**——上一辑把"验证"单独拿出来看，这一辑再拆一层：
不只是"这条断言过没过"，而是"这条分支到底走得到走不到"。

这一张卡是**星级比主题高**的一个（2,103★，MIT），
它和本辑主线的关系是那条 commit：`Fix headless Playwright rendering`
—— 也就是"让 agent 能看见自己的输出"那段基础设施。

数据来源：2026-09-21 用 GitHub REST API 实测
（stars / forks / language / license / created_at / pushed_at），没有一个数字是估的。
幂等：已存在标记则退出 0。

用法：python insert_v19_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1072"'
FIRST_NEW_FOOTNOTE = 1073
MARKER = "第十九版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十八版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1073 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十九版增补 2026-09-21</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1074 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm19c1", name="threejs-game-skills（Agent 技能包）",
        url="https://github.com/majidmanzarpour/threejs-game-skills",
        lang="Python / Markdown", stars="2,103",
        tags=[("t-make", "游戏 × AI"), ("t-ok", "已登记未安装")],
        plain="一套给 Claude Code / Codex 用的 <strong>Agent Skill</strong>：分步骤教 agent 做一个"
              "「可玩且打磨过」的 Three.js 浏览器游戏，覆盖玩法、AAA 式画面、UI、质量保证，"
              "以及可选的 AI 生成 3D / 图像 / 音频资产。它不生成游戏——它给 agent 一张"
              "<strong>工作清单和验收顺序</strong>：先把车开起来、比赛能跑，再加赛道、灯光、菜单、音效，"
              "最后查手机上效果、运行报错和性能。",
        analogy="和本工作区攒了十三辑的 <code>game-production-pipeline.md</code> 是<strong>同一个东西的不同写法</strong>"
                "——把「先做小闭环、再叠表现」这条经验固化成 agent 每步都会读的文档。"
                "区别是它的载体是 skill（跟着仓库走），我们的载体是一份持续更新的 markdown。",
        ext=(70, "7.0/10", "结构可抄：把「玩法→表现→验收」拆成有序阶段、每阶段给可判定的出口。"
                            "这套组织方式与引擎无关，本工作区的 skills 目录可以直接借"),
        use=(20, "2.0/10", "本作是 Ren'Py 视觉小说，没有 Three.js 那一层；"
                            "而它真正值钱的那部分（让 agent 看见自己的输出）我们早就有了"
                            "——<code>testcases.rpy</code> + <code>_shots/</code>。只登记不安装"),
        warn="23 天涨到 2,103★（创建 2026-06-14、最近推送 2026-09-05）说明这个方向热度极高，"
             "但<strong>热度不是适配度</strong>：它的验收标准是「能在浏览器里跑起来、手机上不卡」，"
             "对纯文本游戏没有任何约束力。",
        src="创建 2026-06-14 · 最近推送 2026-09-05 · 213 forks · MIT · 信源 [1073]",
    ),
]

FOOTNOTES = [
    ("1073", "https://github.com/majidmanzarpour/threejs-game-skills",
     "majidmanzarpour/threejs-game-skills", "2,103 · 2026-09-05 · MIT · 213 forks"),
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

    desc = ('这一批只有一张卡：一套教 agent 做 Three.js 浏览器游戏的 <strong>Agent Skill</strong>。'
            '星级（2,103）比主题更打眼，但真正值得记的是它 commit 历史里那句 '
            '<code>Fix headless Playwright rendering</code> —— '
            '<strong>「让 agent 看得见自己的输出」这段基础设施</strong>，'
            '和本辑主线（可达性）、以及本工作区一直在做的 '
            '<code>testcases.rpy</code> + <code>_shots/</code>，是同一件事。'
            '星级 / 语言 / 协议 / forks 为 2026-09-21 用 GitHub API 实测。')

    block = ['    <div class="group" data-page-node-id="rpm19g">',
             '      <div class="group-title" data-page-node-id="rpm19gt">🆕 第十九版增补 · 让 agent 看得见自己的输出（1 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm19gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm19r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm19ra%s">%s</a> — %s</div>'
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
