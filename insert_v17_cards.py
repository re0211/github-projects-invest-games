# -*- coding: utf-8 -*-
"""
第十七版增补：把第十二辑调研新发现的 7 个条目登记进 index.html。

主题和前两版都不一样：
  · 第十六版是「AI agent 直接驱动引擎」（清一色 MCP 服务器）
  · 这一版是「**AI 做游戏这件事，开始被拆开看**」——
    两个是「把 agent 框架拆成零件做消融实验」（含一篇 arXiv 论文的官方仓库），
    两个是「把中文语音合成拆到能离线跑」（本项目的第 6 轮配音就是靠它落地的），
    一个是「把图生 3D 拆到本地桌面」，两个是「在既有游戏外面套一层 AI」。

所以这批的星级跨度很大：从 5 星到 14864 星。**别按星看，按「它拆开了什么」看。**

数据来源：2026-09-20 用 GitHub REST API 实测（stars / language / license / pushed_at），
**没有一个数字是估的**（房规 9：别编造内容）。

幂等：脚本开头检查目标标记是否已存在，已存在则退出 0，不会重复插入。

用法：python insert_v17_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

# 插在「游戏拓展与解包」section 之前 = 「游戏制作（含 AI 制作游戏专题）」的末尾
SECTION_S3 = '<section id="s3"'
# 最后一条脚注的起点（脚注编号实测 1~1064）
LAST_FOOTNOTE_MARK = '<div id="r1064"'
FIRST_NEW_FOOTNOTE = 1065
MARKER = "第十七版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十六版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1065 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十七版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1071 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项（均与上版零重复）</span>',
]

Q1 = "「"
Q2 = "」"

# ---------------------------------------------------------------------------
# 卡片内容。stars / lang / license / 推送日期全部来自 2026-09-20 的 GitHub API 实测。
# 注意：正文里的强调统一用「」，**不要用 ASCII 双引号**（会截断 Python 字符串）。
# ---------------------------------------------------------------------------
CARDS = [
    dict(
        nid="rpm17c1", name="HarnessOfHarness（多日自主开发的改进环）",
        url="https://github.com/Flesymeb/HarnessOfHarness",
        lang="论文配套代码", stars="138",
        tags=[("t-make", "Agent 工程"), ("t-ok", "有对照实验")],
        plain="arXiv:2609.01481 的官方仓库。它不造新的 agent 框架，而是<strong>操作现有的框架</strong>（Codex+GPT-5.5 / OpenCode+DeepSeek-V4-Pro / Pi+MiniMax-M3），把它们的执行组织成迭代的「计划-编码-测试」环，靠五条机制跨环保持改进：平衡「修」与「长能力」、把开发切成<strong>小而可验证的增量</strong>、把实现期测试与独立评估分开、约束可验证的产出而不是规定工作流、渐进式暴露工具与技能并鼓励复用。",
        analogy="别的项目在教你「怎么让 AI 更强」，这个在教你<strong>「怎么让 AI 连续干很多天还不跑偏」</strong>。三个基准、三对模型组合，平均相对提升 52.25%、最大 82.86%；多日部署跑到 70+ 轮迭代时，它自主做出了一款第一人称射击游戏。",
        ext=(80, "8.0/10", "不绑定某个框架，换模型 / 换 harness 都能套；五条机制里前两条可以直接抄"),
        use=(65, "6.5/10", "对「一次只做一晚上」的用法收益有限（差异在第三次迭代后才拉开）；对长期项目的方法论价值很高"),
        src="最近推送 2026-09-08 · MIT · 信源 [1065]",
    ),
    dict(
        nid="rpm17c2", name="kokoro-onnx（含中文语音包）",
        url="https://github.com/thewh1teagle/kokoro-onnx",
        lang="Python", stars="2736",
        tags=[("t-make", "本地 TTS"), ("t-ok", "离线零成本")],
        plain="ONNX 版 Kokoro 语音合成。它的 <code>model-files-v1.1</code> release 里放了<strong>中文专用模型</strong>：<code>kokoro-v1.1-zh.onnx</code>（310MB）/ <code>.fp16</code>（156MB）/ <code>.int8</code>（108MB）+ <code>voices-v1.1-zh.bin</code>（51MB）。本机实测加载后 <code>get_voices()</code> 返回 <strong>103 个音色</strong>，中文部分是 55 个 <code>zf_*</code>（女）+ 48 个 <code>zm_*</code>（男）。",
        analogy="中文配音的开源方案过去问题不是「没有」，是「只有一个声音」——<strong>一个声音就分不出角色</strong>。这个的意义是「够多、能挑、还离线」。本项目第 6 轮就是用它给《翁法罗斯吐槽实录》配的音。",
        ext=(75, "7.5/10", "MIT，模型和代码分离，可以只拿模型接自己的推理；103 个音色够按角色分声"),
        use=(70, "7.0/10", "CPU 就能跑（本机实测约 3 秒/句），零 API 成本、可无限重跑。选音色要按<strong>量出来的高频能量</strong>挑，别按角色性别挑——实测女声普遍有电音、男声干净"),
        warn="清华 PyPI 镜像里没有这个包（from versions: none），必须走默认源；运行前要 unset PYTHONPATH（否则 WorkBuddy 的 safe-delete 保护会把 HuggingFace / onnx 的临时文件清理误判成批量删除）。另外：<b>中英混排选 Kokoro 而不是纯中文模型</b>（判据来自 sherpa-onnx 的文档，那个项目本索引第 [466] 条已收）。",
        src="最近推送 2026-09-01 · MIT · 信源 [1066]",
    ),
    dict(
        nid="rpm17c4", name="Modly（本地图生 3D 桌面工具）",
        url="https://github.com/lightningpixel/modly",
        lang="TypeScript", stars="7635",
        tags=[("t-make", "3D 资产"), ("t-ok", "离线不上传")],
        plain="把「图生 3D」做成<strong>桌面程序</strong>：本地 GPU 跑模型，图片不出本机；扩展系统可接 <strong>Hunyuan3D / TripoSG / Trellis2</strong> 等开源 3D 生成模型；输出 GLB / OBJ / STL；Windows / Linux / Apple Silicon 都有安装包。",
        analogy="AI 3D 资产一直有个别扭的地方：要么把素材传上去，要么按量付费。它把这两件事一起解决掉——<strong>一次性装好，之后随便用</strong>。对「用 AI 出 2D 做游戏、想顺手试试 3D」的人是零风险入口。",
        ext=(70, "7.0/10", "插件式架构，能换不同开源 3D 生成模型；输出通用格式，不锁工具链"),
        use=(45, "4.5/10", "要本地 GPU；视觉小说用不上。登记它是方向信号：3D 资产「离线 + 免费」这一档已经有人做了"),
        warn="GitHub API 返回的 license 是 NOASSERTION（不是标准协议文本）。商用前请自己核一遍 LICENSE。",
        src="最近推送 2026-09-19 · NOASSERTION · 信源 [1067]",
    ),
    dict(
        nid="rpm17c5", name="D.O.L.I（给既有游戏接 LLM）",
        url="https://github.com/ArsNativa/Degrees-of-Lewdity-Intelligence",
        lang="TypeScript", stars="25",
        tags=[("t-mod", "Modding × AI"), ("t-ok", "活的 mod")],
        plain="给一款成熟的既有游戏接上 LLM：提供<strong>智能 Agent 对话</strong>和 <strong>AI 战斗文本生成</strong>。今天（2026-09-20）还在推。",
        analogy="这类 mod 的正确姿势是<strong>「在外面套一层」，不是「重做游戏」</strong>——因为原版的数值体系本身就是最好的规格说明书，你不用重新发明平衡。对做游戏的人来说，这比任何「AI 原生引擎」的 demo 都更有参考价值。",
        ext=(60, "6.0/10", "TypeScript 写，接在既有游戏上，可以只开一部分功能（比如只要战斗文本）"),
        use=(35, "3.5/10", "25★ 且是特定游戏的 mod，不能直接拿来用。价值在「怎么把 LLM 塞进已有玩法而不破坏平衡」这个问题上的现成答案"),
        src="最近推送 2026-09-20 · NOASSERTION · 信源 [1068]",
    ),
    dict(
        nid="rpm17c6", name="WovenRealm 织境空间（AI 剧情扩展层）",
        url="https://github.com/Kanna-hanabi/WovenRealm",
        lang="Ren'Py · Python", stars="5",
        tags=[("t-mod", "AI 剧情层"), ("t-ok", "同引擎")],
        plain="<strong>Ren'Py 项目</strong>（同一款引擎）的 AI 剧情扩展：在原版的世界、人物和数值体系之上加一层「可控的 AI 剧情扩展」——动态剧情、场景配图、<strong>剧情记忆</strong>、道具与补位装备；本体是主模组，另有生活 / 料理 / 战斗等辅助扩展陆续开放。",
        analogy="注意它的用词：<strong>「可控的」</strong>。它不吹「世界观无限生成」，而是给了剧情记忆和装备补位这两件很具体的事。对同引擎的项目来说，这是「AI 扩展怎么做才不崩」的第一个可读样本。",
        ext=(55, "5.5/10", "MIT；同引擎（Ren'Py）+ Python，架构可以直接读；模块化拆成了多个扩展模组"),
        use=(30, "3.0/10", "5★、面向特定游戏，只登记不采用。本项目 ROADMAP 的「明确不做」里已经写过：吐槽向短篇的台词是手写的笑点，交给模型生成只会变平"),
        src="最近推送 2026-09-16 · MIT · 信源 [1069]",
    ),
    dict(
        nid="rpm17c7", name="claude-skills（含 game-developer）",
        url="https://github.com/Jeffallan/claude-skills",
        lang="Python", stars="11546",
        tags=[("t-ok", "Skills 合集"), ("t-warn", "通用 3D 向")],
        plain="一个 Claude Code / Codex 的 Skills 合集。其中 <code>game-developer</code> 那个的结构值得抄：<strong>每个阶段带 validation checkpoint</strong>（实现 → 跑 Profiler 确认帧时间 ≤16ms 再往下），以及两张明确到可判定的表——MUST DO / MUST NOT DO（不在 Update 里 Instantiate、不用字符串比较 tag 而用 CompareTag、不在循环里调 Find、不硬编码数值）。",
        analogy="它的价值在<strong>结构</strong>：把「不许做什么」写成能判定的句子，而不是写成叮嘱。这正是本项目房规在做的事（判据取属性，不取名字）。",
        ext=(70, "7.0/10", "MIT，skill 之间独立，可以只拿其中一个；文件结构本身是可复用的模板"),
        use=(30, "3.0/10", "内容对本项目基本不适用——它面向 Unity / Unreal、60FPS、对象池、联机补偿，Ren'Py 视觉小说一条都用不上。抄的是「怎么组织约束」，不是「约束了什么」"),
        warn="这类通用引擎 skill 容易给人一种「装了就懂游戏开发」的错觉。实测判断：它写的都是正确的常识，但常识不是你的项目。先想清楚要它解决什么，再装。",
        src="最近推送 2026-08-07 · MIT · 信源 [1070]",
    ),
]

FOOTNOTES = [
    ("1065", "https://github.com/Flesymeb/HarnessOfHarness",
     "Flesymeb/HarnessOfHarness", "138 · 2026-09-08 · MIT"),
    ("1066", "https://github.com/thewh1teagle/kokoro-onnx",
     "thewh1teagle/kokoro-onnx", "2736 · 2026-09-01 · MIT"),
    ("1067", "https://github.com/lightningpixel/modly",
     "lightningpixel/modly", "7635 · 2026-09-19 · NOASSERTION"),
    ("1068", "https://github.com/ArsNativa/Degrees-of-Lewdity-Intelligence",
     "ArsNativa/Degrees-of-Lewdity-Intelligence", "25 · 2026-09-20 · NOASSERTION"),
    ("1069", "https://github.com/Kanna-hanabi/WovenRealm",
     "Kanna-hanabi/WovenRealm", "5 · 2026-09-16 · MIT"),
    ("1070", "https://github.com/Jeffallan/claude-skills",
     "Jeffallan/claude-skills", "11546 · 2026-08-07 · MIT"),
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

    desc = ('这一批的关键词是<strong>「拆开」</strong>：把 agent 框架拆成零件做消融实验'
            '（含一篇 arXiv 论文的官方仓库）、把中文语音合成拆到能离线跑（本项目的配音就是靠它落地的）、'
            '把图生 3D 拆到本地桌面、把「给既有游戏接 LLM」拆成一个个可开关的扩展。'
            '<strong>星级跨度从 5 到 14864，别按星看，按「它拆开了什么」看</strong>。'
            '星级 / 语言 / 协议为 2026-09-20 用 GitHub API 实测。')

    block = ['    <div class="group" data-page-node-id="rpm17g">',
             '      <div class="group-title" data-page-node-id="rpm17gt">🆕 第十七版增补 · 把「AI 做游戏」拆开看（6 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm17gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm17r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm17ra%s">%s</a> — %s</div>'
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
