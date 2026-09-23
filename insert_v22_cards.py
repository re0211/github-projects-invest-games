# -*- coding: utf-8 -*-
"""第二十二版增补：把第十六辑 GitHub 那一路新发现的 6 个条目登记进 index.html。

本辑 GitHub 调研：19 个查询 → 268 条原始候选 → 自动去重 + 相关性筛 → 160 条
→ 人工挑出 6 条"与本工作区直接对话"的。
全部经 `gh search repos` / `gh api repos/<r>` 逐条实测（stars / license / language /
pushed_at / created_at / archived，无一虚构）。剔除了 4 条已收录（ueboxai/uebox、
wilsjo2/OptiScaler…、XuanwnOvO/DroidSpy、bebabinlarsson-blip/Godot-MCP）与 14 个
同模板 SEO 站（`*-dev.github.io`，2026-09-21/22 批量创建、~10★）。

数据来源：2026-09-23 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v22_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1078"'
FIRST_NEW_FOOTNOTE = 1079
MARKER = "第二十二版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十一版增补 2026-09-21</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1079 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十二版增补 2026-09-23</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1085 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项 + 第二十二版增补 6 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm22c1", name="open-alternative-jev（把 System 1 决策搬回本地）",
        url="https://github.com/ikermoel/open-alternative-jev",
        lang="Python", stars="51",
        tags=[("t-make", "AI × 模型"), ("t-ok", "已登记未安装")],
        plain="一个**开源版 System 1 模型层**：让手上已有的开源权重模型，在**一次前向**里给出"
              "「有类型的、带校准概率的」决策 —— **不生成文本**，只从下一个 token 的分布里，"
              "在你给的选项上取概率。",
        analogy="第七辑我们完整实测过 `laya`（421M，纯 CPU，0.64s/次）。它是**同一个位置上的"
                "另一条路线**：laya 是「训一个小模型专门做判断」，它是「**不改模型，只改调用方式**」"
                "——把共享的上下文**只写一遍**，N 个问题都从同一个位置取答案。",
        ext=(80, "8.0/10", "「**共享状态只写一遍**」是通用手法：我们有大量「读同一份材料、"
                            "问 N 个问题」的脚本（闸门报告、翻译探针），packing 能把 token 降下来"
                            "（作者实测 **2.5x**）"),
        use=(30, "3.0/10", "**要 CUDA 显卡**（作者实测跑在 H200 MIG / 35GB）；本机 16GB 无独显。"
                            "**先记着这条路线，等有卡再试**"),
        warn="**⚠️ 文档写了 `pip install open-alternative-jev`，但 PyPI 上根本没有这个包** —— "
             "本辑实测：PyPI JSON 返回 404，`pip install` 直接报「No matching distribution found」。"
             "要装只能从仓库 `pip install git+…`，或用它的 Hugging Face Space 在线 demo。"
             "**「README 里写着」不等于「能装」**，这条已记进 `mistakes/`。",
        src="创建 2026-09-18 · 最近推送 2026-09-22 · 51★ · Apache-2.0 · Python · 信源 [1079]",
    ),
    dict(
        nid="rpm22c2", name="agent-harness（让每条规则自己报「我触发了几次」）",
        url="https://github.com/JakeSelby/agent-harness",
        lang="Python", stars="15",
        tags=[("t-make", "AI × 工作流"), ("t-ok", "已登记未安装")],
        plain="一句话：**查出你的 agent 规则里，哪几条真的生效过。** 它的铁规矩 —— "
              "每条规则要么配一个**确定性检测器**（在 agent 自己的对话记录里可判定的东西），"
              "要么**在规则里写明「转录里没有东西能判定它」**，两者都没有 → lint 直接让提交失败。"
              "然后 `harness usage --rules` 报出每条规则**触发了几次**，按仓库分组。",
        analogy="本工作区的 `agent-house-rules.md` 是 **32 条「写了就指望它生效」的规则** —— "
                "和它开篇吐槽的一模一样（原话：*Every project in this field writes instructions "
                "and hopes*）。它把这句吐槽**做成了工具**。",
        ext=(90, "9.0/10", "**本批最值得借的一条**：房规可以照它的方式补一列 —— "
                            "「检测器」或「判定不了的原因」；本辑已按这个口径给 32 条房规做了登记"),
        use=(70, "7.0/10", "它是 Claude Code / Codex 专用（要把 hooks 装进 runtime），"
                            "**我们的 runtime 不是它**；但**方法论当天就吸收**了"),
        warn="它自曝：用这套工具**抓出自己仓库里两个「上线了但其实什么都没做」的功能**，"
             "并且把它们挂成 issue 而不是藏起来 —— 又一个「闸门自己也要有证据」的实证。",
        src="创建 2026-09-16 · 最近推送 2026-09-23 · 15★ · MIT · Python · 信源 [1080]",
    ),
    dict(
        nid="rpm22c3", name="ai-model-world（556 个大模型拟人化成像素小人）",
        url="https://github.com/liyupi/ai-model-world",
        lang="TypeScript", stars="171",
        tags=[("t-make", "模型对比"), ("t-ok", "已登记未安装")],
        plain="一个**中文的模型对比可视化站**：把 **556 个大模型**做成像素小人 —— 进来一眼看到"
              "「此刻谁最聪明 / 谁最会写代码 / 谁最便宜 / 谁刚发布」，往下是国内与国外分区的"
              "厂商广场、完整发布时间线、多维排行榜；搜索认模型名、厂商和能力。",
        analogy="我们一直靠「逐条读官方发布 + 记进备注」来选型（Qwen3-Max 管创意、DeepSeek 管代码、"
                "本地 Ollama 管离线）。它**把这个动作做成了一个可查询的界面**。",
        ext=(70, "7.0/10", "它的**数据源**（Epoch AI / models.dev / LiveBench / HuggingFace）"
                            "值得单独记下来 —— 以后要自己拉模型数据，就用这几家"),
        use=(60, "6.0/10", "选型时当下就能用；但它是**第三方聚合**，"
                            "关键结论仍要回到官方页复核（M-0002）"),
        warn="作者是「鱼皮」（国内知名编程教育博主），**这个站是给大众看的概览，不是评测** —— "
             "当「索引」用，别当「证据」用。",
        src="创建 2026-09-17 · 最近推送 2026-09-23 · 171★ · MIT · TypeScript · 信源 [1081]",
    ),
    dict(
        nid="rpm22c4", name="gamenumerics（游戏数值的确定性引擎）",
        url="https://github.com/26048608982lp-ai/gamenumerics",
        lang="TypeScript", stars="0",
        tags=[("t-make", "游戏 × 数值"), ("t-ok", "已登记未安装")],
        plain="一句话：**把「游戏数值」从「凭感觉调」变成「可复算」** —— 一个 **17 个工具的 MCP 服务**："
              "导入 xlsx 数值表、**审曲线**（成长曲线、掉落概率是否合理）、跑战斗与抽卡模拟。",
        analogy="本作第 9 轮找到的那个「结局四走不到」的 bug，本质就是**数值区间与产出上限没对上**"
                "（我们补了 `check_balance.py`）。它把这个思路从「我们自己写一条断言」"
                "扩展成**一整套可复用的数值审查口径**。",
        ext=(80, "8.0/10", "「**数值要可复算**」可以直接接到 `check_balance.py`："
                            "以后若要加数值系统（掉落 / 成长），先过一遍它的曲线审查口径"),
        use=(40, "4.0/10", "本作是纯叙事 VN，**现在没有数值系统**（吐槽值是叙事计数，不是数值设计）；"
                            "0★ + 很新，别指望成熟"),
        src="创建 2026-09-13 · 最近推送 2026-09-16 · 0★ · MIT · TypeScript · 信源 [1082]",
    ),
    dict(
        nid="rpm22c5", name="game-apk-reverse-engineering（把 APK 逆向写成 AI 能跑的清单）",
        url="https://github.com/sayic/game-apk-reverse-engineering",
        lang="—", stars="9",
        tags=[("t-make", "游戏 × 逆向"), ("t-ok", "已登记未安装")],
        plain="一句话：一套**可复用的手游 APK 逆向工作流** —— 资源提取、代码还原、数值表分析、"
              "Unity 资产导入，**每一步配好 AI skill 与任务模板**。",
        analogy="你的强项正是**解包 + 跨引擎对比**（73 款游戏的积累）。它的价值不是「教你解包」，"
                "而是**把解包经验沉淀成「AI 能照着跑的清单」** —— 第六辑「把人工流程写成 skill」"
                "的同一条思路，换到逆向这个场景。",
        ext=(70, "7.0/10", "「把成手经验写成 AI skill」这个形式，可以照搬到我们自己的"
                            "「立绘绿幕流水线 / 配音流水线」上"),
        use=(50, "5.0/10", "面向 Unity 手游；与本作（Ren'Py）不同引擎，**当方法论模板收**"),
        warn="9★、**无 license、无语言标识**（多半是 prompt / skill 集合而非代码） → "
             "当「笔记」看，别当「工具」用。",
        src="创建 2026-09-22 · 最近推送 2026-09-22 · 9★ · 无 license · 信源 [1083]",
    ),
    dict(
        nid="rpm22c6", name="sprite-generator（四方向角色精灵图生成）",
        url="https://github.com/envy-ai/sprite-generator",
        lang="Python", stars="0",
        tags=[("t-make", "美术 × 管线"), ("t-ok", "已登记未安装")],
        plain="一句话：用 **ComfyUI** 生成**四方向（上 / 下 / 左 / 右）角色精灵图与动画**，"
              "有网页界面也有命令行。",
        analogy="我们的立绘走的是「AI 生成绿幕图 → 抠图去绿边 → 体型归一」这条自建管线（第 3 轮）。"
                "差别在于：**我们做的是「立绘」，它做的是「行走图 / 精灵表」** —— "
                "正好是「本作若加小人 / 像素角色」那类需求的前置工具。",
        ext=(70, "7.0/10", "「**四方向**」这个约束很实用：四方向是最小可用集，"
                            "比八方向省一半成本，又能支撑一批玩法"),
        use=(30, "3.0/10", "依赖 ComfyUI（本机没装）；本作 v1.9 是立绘 VN，**不需要行走图** —— "
                            "先登记，等真做像素玩法再说"),
        src="创建 2026-09-19 · 最近推送 2026-09-19 · 0★ · AGPL-3.0 · Python · 信源 [1084]",
    ),
]

FOOTNOTES = [
    ("1079", "https://github.com/ikermoel/open-alternative-jev",
     "ikermoel/open-alternative-jev", "51 · 2026-09-22 · Apache-2.0 · Python"),
    ("1080", "https://github.com/JakeSelby/agent-harness",
     "JakeSelby/agent-harness", "15 · 2026-09-23 · MIT · Python"),
    ("1081", "https://github.com/liyupi/ai-model-world",
     "liyupi/ai-model-world", "171 · 2026-09-23 · MIT · TypeScript"),
    ("1082", "https://github.com/26048608982lp-ai/gamenumerics",
     "26048608982lp-ai/gamenumerics", "0 · 2026-09-16 · MIT · TypeScript"),
    ("1083", "https://github.com/sayic/game-apk-reverse-engineering",
     "sayic/game-apk-reverse-engineering", "9 · 2026-09-22 · 无 license"),
    ("1084", "https://github.com/envy-ai/sprite-generator",
     "envy-ai/sprite-generator", "0 · 2026-09-19 · AGPL-3.0 · Python"),
]


def b(s):
    """把 markdown 的 **粗体** 转成 HTML 的 <strong>。"""
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
        for x in bad:
            print("  " + x)
        return 1

    desc = ('第十六辑的 GitHub 那一路跑了 <strong>19 个查询、268 条原始候选</strong>，'
            '自动去重 + 相关性筛后剩 160 条，<strong>再逐条 grep 过 14 份存档 + 1079 项索引</strong>。'
            '剔掉的：4 条已收录（uebox / OptiScaler / DroidSpy / Godot-MCP）、'
            '14 个同模板 SEO 站（<code>*-dev.github.io</code>，09-21/22 批量创建、约 10★）。'
            '这里只登记<strong>与本工作区直接对话的 6 条</strong>，其余以链接形式留在 '
            '<code>csdn-social-summary.md</code> 第十六辑里 —— '
            '<strong>索引的容量不该被「顺手看到的」占满</strong>。')
    # 注：下方两处全角括号与 &amp; 是为了避开 .format —— 这里没用 format，保持写法一致

    block = ['    <div class="group" data-page-node-id="rpm22g">',
             '      <div class="group-title" data-page-node-id="rpm22gt">🆕 第二十二版增补 · 同题海啸里，怎么分辨（6 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm22gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm22r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm22ra%s">%s</a> — %s</div>'
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
