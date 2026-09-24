# -*- coding: utf-8 -*-
"""第二十六版增补：把第二十辑 GitHub 那一路新发现的 8 个条目登记进 index.html。

本辑 GitHub 调研：逐仓库 `gh api repos/<r>` 实测（stars / forks / license / language /
pushed_at / created_at 全部走 REST API，无一估算）→ 逐条 grep 过 19 份存档 + 1112 项索引。
剔掉的已收录项：`gamedev-skills/awesome-gamedev-agent-skills` · `wellingfeng/UltraGameStudio` ·
`IvanMurzak/Godot-MCP` · `CoplayDev/unity-mcp` · `hi-godot/godot-ai`；
另剔一批 0–1★ 同模板空壳与 4 个 laya/dsh 压缩变体（只留机制最清楚的 `dsh-argp`）。

本辑主线：**「判据外移」** —— 不只是"错不起的步骤"要确定性化（第十九辑 open-code-review），
规格（词表）、记忆（五道外部验证测试）、压缩裁决（LLM 只提议、守卫裁决）、
安全（472 条确定性规则）都在往外移。

数据来源：2026-09-24 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v26_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1111"'
FIRST_NEW_FOOTNOTE = 1112
MARKER = "第二十六版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第二十五版增补 2026-09-23',
    '共 1112 个项目',
    '第二十三版增补 9 项 + 第二十四版增补 10 项 + 第二十五版增补 8 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第二十六版增补 2026-09-24',
    '共 1120 个项目',
    '第二十三版增补 9 项 + 第二十四版增补 10 项 + 第二十五版增补 8 项 + 第二十六版增补 8 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm26c1", name="waku-agent（刻意可读可改的本地优先 agent 骨架）",
        url="https://github.com/ShenSeanChen/waku-agent",
        lang="Python", stars="1,825",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="**本批星数最高的一个（1,825★ / MIT / Python）。** 它的卖点不是能力更强，"
              "而是**刻意保持可读、可改**：把 loop、**语义/情节/程序性三类记忆**、检索门、"
              "**确定性测试**、LLM-as-judge 和发布闸门**全部塞在一个能读完的 Python 项目里**。"
              "记忆是**单个本地 SQLite 文件**，`pip install waku-agent` 即可跑。",
        analogy="第十九辑 `alibaba/open-code-review`（40,091★）给的是「错不起的步骤要确定性化」的结论，"
                "但它是生产黑盒，**看不到内部怎么切的**。waku-agent 是同一条路线的**透明版** —— "
                "我们六道 `check_*.py` 是自己摸出来的，它可以当对照图纸。",
        ext=(90, "9.0/10", "**三类记忆的划分可以直接抄**：语义（事实）/ 情节（发生过什么）/ "
                           "程序性（怎么做）。我们的 `mistakes/` 只覆盖后两类，"
                           "**「事实类」目前散在 MEMORY.md 里，没有独立结构**"),
        use=(72, "7.2/10", "`pip install waku-agent` 一行可跑、SQLite 单文件、无需外部服务；"
                           "⚠️ 官方 provider 偏云端，**接 Ollama 要先验 OpenAI-compatible adapter** "
                           "（按 M-0002，装之前先实测，不要假设能接）"),
        warn="同类 `dcellison/kai`（36★）用 **SQLite append-only event log** 存会话/任务/记忆，"
             "思路与我们的 `mistakes/` + 每日日志同构，可对照看。",
        src="最近推送 2026-09-23 · 1,825★ · MIT · Python · 信源 [1112]",
    ),
    dict(
        nid="rpm26c2", name="unity-cli-loop（最少工具覆盖「编译→跑→截图→验证」闭环）",
        url="https://github.com/hatayama/unity-cli-loop",
        lang="C#", stars="568",
        tags=[("t-make", "游戏 × 引擎"), ("t-ok", "已登记未安装")],
        plain="**让 agent 从 CLI 驱动 Unity 2022.3+ 的编译、测试、日志、场景编辑、"
              "**截图**、**输入回放**、断点与热更新** —— 形成从编辑到 Play Mode 的**完整闭环**。",
        analogy="**这就是第十四辑「可达性」主线在工具层的样子。** 我们第十七辑总结过一条选型判据："
                "**看工具清单里有没有 run / input / screenshot 三个动词，只有 create 和 edit 的都是半成品。** "
                "这个项目把那三个动词做成了 CLI。",
        ext=(88, "8.8/10", "**可映射到 Ren'Py 的最小闭环**：`launch`（启动）→ `lint` → "
                           "`test`（跑 testcases.rpy）→ `_shots/`（截图）→ `check_release.py`。"
                           "**我们其实已经有了，但没把它当成一个「闭环」来命名和对外暴露**"),
        use=(45, "4.5/10", "**Unity 包本身不适用**（本作 Ren'Py，且游戏线 2026-09-23 已终止）；"
                           "取的是**闭环的形状** —— 这是本批唯一一个真把「验证」做成一等公民的项目"),
        src="最近推送 2026-09-23 · 568★ · MIT · C# · 信源 [1113]",
    ),
    dict(
        nid="rpm26c3", name="model-serving-minefield（按「症状」索引的部署地雷证据库）",
        url="https://github.com/Blackwellboy/model-serving-minefield",
        lang="Python", stars="134",
        tags=[("t-make", "AI × 验证"), ("t-ok", "已登记未安装")],
        plain="**和我们的 `mistakes/` 完全同构，只是对象是模型部署**：按**症状**整理 chat template、"
              "tool parser、reasoning 字段、量化 kernel、CUDA、KV/统一内存、版本漂移的「地雷」，"
              "每条给**可复现的检查步骤**，并且**收录负结果**。带 **Ollama 专页**与只读诊断 CLI/MCP。",
        analogy="**这是「按症状索引」这件事的样板。** 我们 `mistakes/` 的 `retrievalKeys.errorStrings` "
                "做的就是同一件事 —— 让人在**看到报错那一刻**能检索到，而不是按主题分类去找。"
                "它提醒我们的缺口：**我们的条目没有「可复现的检查步骤」这一栏**，"
                "只有 `regressionTest.command`，很多条写的是 `n/a`。",
        ext=(86, "8.6/10", "**「收录负结果」是一个我们没有的纪律** —— "
                           "我们只记录「错了什么」，不记录「试过什么、发现不行」。"
                           "后者在换模型/换版本时价值极高"),
        use=(55, "5.5/10", "⚠️ **license 未声明（GitHub API `license=null`）** → "
                           "**可以读、可以引用结论，不要把代码复制进项目**；"
                           "Ollama 专页对我们排查桥（8787）的问题有直接价值"),
        src="最近推送 2026-09-23 · 134★ · 未声明协议 · Python · 信源 [1114]",
    ),
    dict(
        nid="rpm26c4", name="deepseek-harness-for-vscode（不用另装 CLI 的 DSH 工作台）",
        url="https://github.com/skymecode/deepseek-harness-for-vscode",
        lang="TypeScript", stars="148",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已登记未安装")],
        plain="**把 DeepSeek Harness 做成原生 VS Code 工作台**：内置经过兼容测试的 runtime，"
              "支持会话**持久化 / 分叉 / 归档 / 导入导出**、**文件上下文卡**、模型与推理控制、插件中心。"
              "有平台 VSIX、**简体中文**、Windows 历史目录说明。",
        analogy="第十七辑我们确认了 **DSH 是本机真在用的外壳**（`dsh 0.1.0-rc.6`），"
                "但一直卡在 rc 且要走 CLI。这个扩展给了**第二条路** —— "
                "**不换外壳，只换进入方式**，风险比换壳小得多。",
        ext=(80, "8.0/10", "**「会话分叉」是一个我们没有的能力**：我们现在一个任务一条线，"
                           "想试另一条路只能重跑。**分叉 + 归档**让「试错」这件事变便宜"),
        use=(62, "6.2/10", "⚠️ 两条硬提醒：① 共享会话日志必须遵守 **V4 格式 + 单写者锁**；"
                           "② **先备份再切换**官方 CLI ↔ 扩展。148★ / 2026-09 新项目，按 M-0002 先看不装"),
        src="最近推送 2026-09-22 · 148★ · MIT · TypeScript · 信源 [1115]",
    ),
    dict(
        nid="rpm26c5", name="coddy-agent（单二进制 harness + 项目可信门）",
        url="https://github.com/coddy-project/coddy-agent",
        lang="Go", stars="154",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已登记未安装")],
        plain="**一个静态 Go 二进制**的统一 Agent Harness：TUI / ACP / Web-API / 定时任务 / 多节点入口，"
              "内置技能、子 Agent、MCP、后台任务、上下文压缩、长期记忆，"
              "以及一个我们特别关心的东西 —— **项目可信门**（阻止仓库自带的 hook / MCP 自动执行）。",
        analogy="**「项目可信门」是 supply-chain 防线在 harness 层的落地。** "
                "第十六辑记过 slopsquatting（AI 幻觉依赖 = 恶意包）这个风险，"
                "而我们克隆过 `refs/` 下的第三方 skill —— **克隆即信任，目前没有任何闸门**。",
        ext=(84, "8.4/10", "**可直接抄的判据**：**仓库自带的 hook / MCP 默认不执行，"
                           "要显式授信。** 我们 `refs/` 里放过 `renpy-mcp`、`renpy-android-packager-skill`，"
                           "**这道门现在是敞开的**"),
        use=(68, "6.8/10", "发布 **Windows 二进制**且支持 Ollama / llama.cpp / OpenAI-compatible，"
                           "16GB 机器配小模型可用；定时任务正好能跑索引站更新"),
        warn="README badge 里残留旧 owner `EvilFreelancer/coddy-agent` —— "
             "**已在三份基线里 grep 过，旧路径 0 命中，不是换名重复收录**。",
        src="最近推送 2026-09-23 · 154★ · MIT · Go · 信源 [1116]",
    ),
    dict(
        nid="rpm26c6", name="gai（Godot Agent CLI：把「不可覆盖源文件」写进约束）",
        url="https://github.com/godot-fun/gai",
        lang="GDScript", stars="170",
        tags=[("t-make", "游戏 × 引擎"), ("t-ok", "已登记未安装")],
        plain="**Godot 的 Agent CLI/GUI + 跨 harness 技能集合 + 轻量游戏框架**："
              "提供音频、图片、视频、分镜的**批处理**与单元/集成测试等制作发行辅助能力。"
              "最值得注意的是一条硬约束：**不可覆盖源文件**。",
        analogy="**「不可覆盖源文件」是我们自己踩过没总结的一条。** "
                "M-0012 记录过水印压在人物肩上导致「右下角清零」挖出矩形缺口 —— "
                "**根因就是流水线允许覆盖原图**。人家把它写成了框架级约束，我们只在 mistake 里写着。",
        ext=(82, "8.2/10", "**素材管线的三条约束可移植到 Ren'Py**："
                           "① 原始素材只读 ② 中间产物可重生成 ③ 批处理前后数文件（M-0006 同族）"),
        use=(42, "4.2/10", "GDScript 代码与 `zfoo/` 框架不能直接复用；"
                           "**取的是约束，不是实现**"),
        src="最近推送 2026-09-23 · 170★ · MIT · GDScript · 信源 [1117]",
    ),
    dict(
        nid="rpm26c7", name="nl-veil（Windows 原生桌面 agent，跨会话记忆 + Ollama）",
        url="https://github.com/gary23w/nl-veil",
        lang="Zig", stars="204",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已登记未安装")],
        plain="**Windows / macOS / Linux 桌面编码 Agent**：可并行分派专家、**保留跨会话项目记忆**，"
              "模型三选一（内置 / **Ollama** / OpenAI-compatible endpoint）。Zig 写的原生应用。",
        analogy="**它是「跨会话项目记忆」这个需求的又一个独立样本。** "
                "第十九辑 `tigerless-labs/agent-memory`（966★）的口号是"
                "「plain Markdown as the source of truth」，我们 `.workbuddy/memory/` 走的就是这条路。"
                "**三个独立来源指向同一个答案：记忆是文件，不是上下文。**",
        ext=(78, "7.8/10", "**Windows 原生 + Ollama 后端**正好对上本机配置；"
                           "「把检索/改脚本/跑测试/记命令拆给不同 agent」与我们单 agent 串行相反，"
                           "**第十六辑已记：>2 并行只增协调税** → 要试也只开 2 个"),
        use=(58, "5.8/10", "⚠️ **内置 12B 模型会挤占 16GB**，必须换成已装的小量化 Ollama 模型；"
                           "204★ / MIT，可作为 `waku-agent` 之外的备选，**二选一不要都装**"),
        src="最近推送 2026-09-23 · 204★ · MIT · Zig · 信源 [1118]",
    ),
    dict(
        nid="rpm26c8", name="defold-agent-config（给引擎项目写的 AGENTS.md 样板）",
        url="https://github.com/indiesoftby/defold-agent-config",
        lang="Python", stars="95",
        tags=[("t-make", "AI × 约定"), ("t-ok", "已登记未安装")],
        plain="**Defold 的 `AGENTS.md` 与技能配置样板**：可把依赖源码 / API 下载到**只读 `.deps/`**，"
              "支持 Claude Code / Copilot / Windsurf / Trae / CodeBuddy，"
              "并明确建议**单任务会话**与 **65% 上下文上限**。",
        analogy="**本辑 §十二那条「模型换谁都能换，质量门禁不能省」在这里有了具体形态。** "
                "我们 `AGENTS.md` 是 2026-09-23 才建的（103 行，本辑补到 118 行），"
                "这份样板给了一个**引擎项目版本**作对照 —— 特别是「依赖文档 JIT 拉取到只读目录」这一招。",
        ext=(80, "8.0/10", "**两条能直接抄**：① 依赖源码**只读化**（AI 能读不能改，避免它「顺手修依赖」）"
                           "② **65% 上下文水位线**（我们有 50–70% 手动压缩的民间说法，这里是框架级默认值）"),
        use=(52, "5.2/10", "⚠️ **license 未声明（API `license=null`）** → 抄思路不抄文件；"
                           "技能内容是 Defold/Python 专用，需改写"),
        src="最近推送 2026-09-18 · 95★ · 未声明协议 · Python · 信源 [1119]",
    ),
]

FOOTNOTES = [
    ("1112", "https://github.com/ShenSeanChen/waku-agent",
     "ShenSeanChen/waku-agent", "1,825 · 2026-09-23 · MIT · Python"),
    ("1113", "https://github.com/hatayama/unity-cli-loop",
     "hatayama/unity-cli-loop", "568 · 2026-09-23 · MIT · C#"),
    ("1114", "https://github.com/Blackwellboy/model-serving-minefield",
     "Blackwellboy/model-serving-minefield", "134 · 2026-09-23 · 未声明 · Python"),
    ("1115", "https://github.com/skymecode/deepseek-harness-for-vscode",
     "skymecode/deepseek-harness-for-vscode", "148 · 2026-09-22 · MIT · TypeScript"),
    ("1116", "https://github.com/coddy-project/coddy-agent",
     "coddy-project/coddy-agent", "154 · 2026-09-23 · MIT · Go"),
    ("1117", "https://github.com/godot-fun/gai",
     "godot-fun/gai", "170 · 2026-09-23 · MIT · GDScript"),
    ("1118", "https://github.com/gary23w/nl-veil",
     "gary23w/nl-veil", "204 · 2026-09-23 · MIT · Zig"),
    ("1119", "https://github.com/indiesoftby/defold-agent-config",
     "indiesoftby/defold-agent-config", "95 · 2026-09-18 · 未声明 · Python"),
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

    desc = ('第二十辑的 GitHub 那一路逐仓库走 REST API 实测'
            '（stars / forks / license / language / pushed / created 无一估算），'
            '再逐条 grep 过 19 份存档 + 1112 项索引。'
            '剔掉的已收录项：<code>awesome-gamedev-agent-skills</code> · '
            '<code>UltraGameStudio</code> · <code>IvanMurzak/Godot-MCP</code> · '
            '<code>CoplayDev/unity-mcp</code> · <code>hi-godot/godot-ai</code>。'
            '<strong>本版主线是「判据外移」—— '
            '规格钉进词表、记忆做成可测、压缩让确定性守卫裁决、安全做成不调模型的规则层。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm26g">',
             '      <div class="group-title" data-page-node-id="rpm26gt">🆕 第二十六版增补 · 判据外移（8 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm26gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm26r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm26ra%s">%s</a> — %s</div>'
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
