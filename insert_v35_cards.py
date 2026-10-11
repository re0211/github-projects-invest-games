# -*- coding: utf-8 -*-
"""第三十五版增补：把第三十辑「Live2D 制作 · 实战测评 · 上新」的 24 个条目登记进 index.html。

本辑候选：gh 路 64 条（8 组搜索，去重后立条 55）、cn 路 14 条（采纳 10）、official 路 16 条。
与 `index.html`（1233 项）及全部历史存档机器比对，本版 24 条命中 **0**。

**本辑主线：前四辑一直在「找工具」，本辑第一次有了「尺子」和「账号」。**

1. **第一个端到端「单图 → 可编辑 Live2D」的系统 + 第一把打假尺子** ——
   `SparcAI-Inc/Bunraku`（arXiv 2607.27348，清华/南洋理工/SparcAI）：Stage1 分层扩散出 RGBA 层堆叠，
   Stage2 只凭每层 alpha 建三角网格、跨层自注意力联合预测顶点位移，发射 Live2D-Bench + 8,884 模型语料。
   但 `pith.science` 的公开审稿报告用**论文自己的数据**指出：头号指标 0.7676 测的是**美术手作网格**、
   部署用的 **alpha 自动网格从未被测**，且 **`ParamEyeLOpen/R`（眨眼）在自动分解层上直接失效**。
   → 这三条就是「以后拿什么筛『一键生成 Live2D』宣传」的检查表。
2. **官方口径两处被推翻** —— ① Cubism Editor 正式版**早已不是 5.3.00，是 5.3.04（2026-09-03）**
   （patch 号只藏在 `docs.live2d.com` 的 Release History 表，产品页只列大版本）；
   ② 学生优惠**简中站是 80% OFF（¥36,720 → ¥7,344 / 3yr，截止 2027-03-31）**，
   与 v29 引英文站的 76%（$238.20→$57.16）**打架** → **以所在区域结算页为准**。
3. **agent 桌宠这条线从「开源的少数玩具」变成了「有主干的生态」** ——
   `moeru-ai/airi`（MIT · **★50,263** · Windows 可用 · 当日仍在推）已是可以直接当底座的体量；
   本机在跑的 DSH 侧也出了 `Andersen216/dsh-whale-girl-live2d`（MIT · 一行 `dsh plugin` 装）。
4. **中文侧终于有可执行的立绘规范** —— 畅游引擎部《图形引擎实战：Live2D 项目应用及落地》把
   「画布该多大（角色高度 > 3000px / 官方示例 5800×8400）」「脸/眼/嘴/发/阴影怎么拆才不出血」
   「哪些图层效果在 Live2D 里是禁的（补色层直接禁）」「渐变减弱与穿帮」全落成规范。

**inbox 顺延**：房规压缩（连续第五轮欠账，现 200/200 行贴顶）；`/skill-doctor`（连续第九轮）。

数据来源：2026-10-11 GitHub REST API 实测（`gh api repos/<r>`）+ WebSearch/WebFetch 一手页面（`_r30/`）。
幂等：已存在本版标记则跳过。
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1232"'
FIRST_NEW_FOOTNOTE = 1233
MARKER = "第三十五版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十四版增补 2026-10-11',
    '共 1233 个项目',
    '第三十三版增补 16 项 + 第三十四版增补 18 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十五版增补 2026-10-11',
    '共 1257 个项目',
    '第三十三版增补 16 项 + 第三十四版增补 18 项 + 第三十五版增补 24 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm35c1", name="airi（自托管数字生命伴侣，五万★的主干）",
        url="https://github.com/moeru-ai/airi",
        lang="TypeScript", stars="50263",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="「自托管、**你拥有**的数字生命伴侣」—— 实时语音对话 + **Live2D / VRM 形象** + 桌宠形态，"
              "Web / macOS / Windows 三端，2026-10-11 仍在推送。定位是开源界的 Neuro-sama 平替。",
        analogy="前几辑这条路一直只有零星的个人玩具（1★、5★ 那种）。这条是**第一个有主干体量的**："
                "MIT、五万★、跨平台、活跃 —— 之前「Live2D 桌宠没有像样的开源底座」这句话，这一辑不能再说了。",
        warn="⚠️ **工程很大**，不是装上就懂的那种小脚本；它自己的定位是「你拥有的数字生命」，"
             "要真跑起来还得配 LLM / TTS 这些后端。⚠️ 拿来当**参考实现**读，比当成品用更划算。",
        ext=(90, "9.0/10", "MIT + 五万★ + 跨平台 + 当日活跃，是这条线目前最稳的开源底座"),
        use=(80, "8.0/10", "想搭 Live2D 桌宠/AI 伴侣，先读它而不是从零写 · MIT · 推送 2026-10-11"),
        src="推送 2026-10-11 · 50263★ · MIT · TypeScript · 信源 [1233]",
    ),
    dict(
        nid="rpm35c2", name="handcrafted-persona-engine（Live2D+LLM+ASR+TTS+RVC 的一体化引擎，1381★）",
        url="https://github.com/elevenyellow/handcrafted-persona-engine",
        lang="C#", stars="1381",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-warn", "星少但有用")],
        plain="C# 写的交互式虚拟形象引擎，把 **Live2D 形象 / LLM 对话 / ASR 语音识别 / TTS / RVC 变声**"
              "串成一条实时链路，定位 VTubing、直播、虚拟助手。功能面是本辑最全的一个。",
        analogy="它的价值不在「你该用它」，而在**它把每条链都接完了一遍** —— "
                "「音频怎么映射成口型/表情参数」「状态机怎么切」这些问题，读它的实现比看十篇教程快。",
        warn="⚠️ **未声明 license**（`none`）→ 只读不抄。⚠️ C#/.NET 桌面栈，"
             "对「Python / JS 主线 + 新手」偏重，上手成本比 airi 高。",
        ext=(75, "7.5/10", "全链路工程化范例，两个大模块可单独拆出来看"),
        use=(60, "6.0/10", "当**架构参考**读；能不能装要看你的 .NET 环境 · 未声明许可 · 推送 2026-05-20"),
        src="推送 2026-05-20 · 1381★ · 未声明许可 · C# · 信源 [1234]",
    ),
    dict(
        nid="rpm35c3", name="dsh-whale-girl-live2d（DSH 界面的鲸鱼娘桌宠，一行命令装）",
        url="https://github.com/Andersen216/dsh-whale-girl-live2d",
        lang="JavaScript", stars="28",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="挂在 **DSH（DeepSeek Harness）Web 界面**上的 Live2D 桌宠：跟着 agent 的**真实状态**"
              "换表情和动作，点一下直接跟 agent 说话，右键是钱包。装法就一行："
              "`dsh plugin --profile web add github:Andersen216/dsh-whale-girl-live2d`。",
        analogy="上一辑收了同层的 `cyanfish-x/dsh-live2d-pets`。这条是本辑**最新、最贴合本机**的一条 —— "
                "「agent 真实状态 → Live2D 表情」这个映射，是你可以直接平移到自己任何 agent 上的模式。",
        warn="⚠️ 28★、很新（2026-10-10 仍在推）。⚠️ 仍是**第三方插件**：往主力 agent 里装之前，"
             "**先人审一遍源码再装**，别让 agent 自己装（这条和上一辑的桌宠结论一致）。",
        ext=(70, "7.0/10", "插件形态挂载，不侵入 DSH 本体；状态→表情的映射可复用"),
        use=(85, "8.5/10", "用户本机就在跑 DSH，这条是**现成可装**的 · MIT · 推送 2026-10-10"),
        src="推送 2026-10-10 · 28★ · MIT · JavaScript · 信源 [1235]",
    ),
    dict(
        nid="rpm35c4", name="aituber-onair（做 Neuro-sama 式 AI VTuber 的 TS 工具箱）",
        url="https://github.com/shinshin86/aituber-onair",
        lang="TypeScript", stars="267",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="开源 TypeScript 工具包，用来搭「能聊天、说话、有记忆、对观众实时反应」的 Neuro-sama 式 AI VTuber，"
              "形象层支持 Live2D。作者 `shinshin86` 长期做 Live2D Web 相关项目（本索引已收其 "
              "`live2d-add-motion-sample-web-ui`）。",
        analogy="本辑三条 AI 主播路里，这条的**入门门槛最低** —— Web/TS 栈，接上本地 Ollama 就能起一个能播的。"
                "它和上面的 airi 是两种用法：airi 是「大而全的底座」，这条是「轻量脚手架」。",
        warn="⚠️ 它给你的是一套**工具箱**，不是成品角色；人设、模型、后端都要你自己配。"
             "⚠️ 与已收录的 `live2d-add-motion-sample-web-ui` 同一作者，别当成两套东西。",
        ext=(80, "8.0/10", "MIT + 当日活跃 + TS，模块可单拆；作者持续维护"),
        use=(75, "7.5/10", "想做 AI 主播 / 直播向，这是本辑最轻的起点 · MIT · 推送 2026-10-11"),
        src="推送 2026-10-11 · 267★ · MIT · TypeScript · 信源 [1236]",
    ),
    dict(
        nid="rpm35c5", name="Artemis（本地离线 AI 伴侣全家桶，8G 显存可跑）",
        url="https://github.com/momori777/Artemis",
        lang="Python", stars="381",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="本地离线 AI 女友系统：Agent + 画图/语音/向量库 + **Live2D 桌宠** + 酒馆角色卡导入 + webchat + "
              "QQ / Telegram 双通道，官方口径 **8G 显存可跑**（动态显存调度）。",
        analogy="它的关键词和你的基准几乎逐字重合：**离线**、**本地 LLM**、**8G 显存**、**Live2D 桌宠**、"
                "**记忆**。要抄「本地小显存怎么把这些拼起来」，这条比读一堆单点工具快。",
        warn="⚠️ 许可为 **NOASSERTION**（没有标准化 LICENSE）→ 家庭自用可以，**商用要谨慎**。"
             "⚠️ 功能面很宽 = 依赖很杂，装之前先看它的依赖清单。",
        ext=(75, "7.5/10", "模块化的本地 LLM + 记忆 + 形象栈，单块可拆"),
        use=(78, "7.8/10", "16GB 本机想搭「离线 + Live2D」样板，这条最贴 · 推送 2026-09-30"),
        src="推送 2026-09-30 · 381★ · NOASSERTION · Python · 信源 [1237]",
    ),
    dict(
        nid="rpm35c6", name="virtual-person（「小凡」：Cubism SDK + LLM 的网页版 AI 形象，中文项目）",
        url="https://github.com/ptghb/virtual-person",
        lang="TypeScript", stars="45",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="基于 **Live2D Cubism SDK** 的智能对话助手：Live2D 虚拟形象 + 实时 WebSocket 通信 + AI 对话，"
              "纯 Web 前端。中文项目，README 与目录结构对中文新手友好。",
        analogy="它的默认后端是 OpenAI，但结构上**把 API base 换成本地 Ollama 就是离线版** —— "
                "这正是「云上 demo」变「本地能用」的最短路径。",
        warn="⚠️ 许可 **NOASSERTION**，抄代码前先看清。⚠️ 「实时 WebSocket」是它自己的服务端，"
             "不是开箱即用的静态页。",
        ext=(70, "7.0/10", "Web 栈、结构清楚，可当「形象 ↔ 对话状态联动」的最小样板"),
        use=(72, "7.2/10", "想快速看「Live2D 形象接 LLM」长什么样，它最省事 · 推送 2026-10-08"),
        src="推送 2026-10-08 · 45★ · NOASSERTION · TypeScript · 信源 [1238]",
    ),
    dict(
        nid="rpm35c7", name="live2d-from-art（把「画作 → Live2D」封装成 Agent Skill，含 MOC3 生成与浏览器校验）",
        url="https://github.com/fifteen42/live2d-from-art",
        lang="Python", stars="11",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "星少但有用")],
        plain="实验性 **Agent Skill**：覆盖「美术图 → Live2D」工作流、**直接生成 MOC3**、以及浏览器端校验。"
              "把整条制作流程封装成 agent 可调用的 skill。",
        analogy="上一辑有 `Ariakage/live2d-agent-kit` 和 `RevStudio/Rev2D`。这条的重点不是能力上限，"
                "而是**它就是一个 `SKILL.md` 形状的东西** —— 想给自己的 agent 加 Live2D 能力，"
                "把它当**格式模板**抄最直接。",
        warn="⚠️ **未声明 license** + 11★ + 实验性 → 只当模板，别当产线。"
             "⚠️ 「直接生成 MOC3」这条要警惕：对照本辑 §Bunraku 与 v29 的失败实录，"
             "**单图自动生成的网格经常一动就散**，先按那三问核一遍。",
        ext=(75, "7.5/10", "skill 描述 + 脚本的结构可直接套用到自己的 agent"),
        use=(68, "6.8/10", "给 agent 加 Live2D 能力时当模板 · 未声明许可 · 推送 2026-09-15"),
        src="推送 2026-09-15 · 11★ · 未声明许可 · Python · 信源 [1239]",
    ),
    dict(
        nid="rpm35c8", name="Cortico（事件流驱动的 persona agent 框架，MIT · 198★）",
        url="https://github.com/Pal-AI-Lab/Cortico",
        lang="TypeScript", stars="198",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="面向 persona bot 的**事件流** AI Agent 框架，TS 实现，形象层支持 Live2D。"
              "核心是把「形象该摆什么表情/动作」挂在 agent 的事件上，而不是写死在渲染层。",
        analogy="「事件 → 形象」这层解耦，是本辑桌宠/AI 形象类的**公共架构**（airi、dsh-whale-girl 都在做同一件事）。"
                "这条把这一层单独做成了一个 MIT 框架，读它比读一堆成品快。",
        warn="⚠️ 它是个**通用 agent 底座**，偏重；你要的是「读事件→形象那一段」，"
             "别被整套框架拖住。⚠️ 不是 Live2D 专用项目。",
        ext=(80, "8.0/10", "MIT + 事件流抽象清晰 + 当日活跃"),
        use=(65, "6.5/10", "想给桌宠做「状态驱动形象」时，读它的那层即可 · MIT · 推送 2026-10-11"),
        src="推送 2026-10-11 · 198★ · MIT · TypeScript · 信源 [1240]",
    ),
    dict(
        nid="rpm35c9", name="renpy-live2d-plus（Ren'Py 的 Live2D 增强模块，方向直指你的目标引擎）",
        url="https://github.com/GunGuyDude-Python/renpy-live2d-plus",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="给 Ren'Py 做 Live2D 支持的增强模块，方向与已收录的 `asfdfdfd/renpy-live2d` 完全同层。",
        analogy="**这条是本辑 gh 路唯一直接对着 Ren'Py 的**。但你做的是 Ren'Py，就值得花五分钟看它跟官方那份"
                "「装 `CubismSdkForNative-5-r.1.zip`」的路子差在哪 —— 也可能正是别人踩过的坑的答案。",
        warn="⚠️ **0★、描述为空、2026-05-15 之后未再更新** → **可信度低，必须自己核对是否真能用**。"
             "⚠️ 拉下来先跑 `renpy lint`，别直接进项目。",
        ext=(55, "5.5/10", "方向对口但没有生态，属个人实验品"),
        use=(50, "5.0/10", "当线索看，别当依赖 · GPL-3.0 · 推送 2026-05-15"),
        src="推送 2026-05-15 · 0★ · GPL-3.0 · Python · 信源 [1241]",
    ),
    dict(
        nid="rpm35c10", name="renderkit（把 PMX/VRM/MOC3 批量渲染成 albedo/depth 的 CLI，Unlicense）",
        url="https://github.com/KurisuMakise004/renderkit",
        lang="Jupyter Notebook", stars="29",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="命令行工具：把 **PMX / VRM / MOC3** 等模型批量渲染成 **albedo / depth** 图。"
              "用于数据集、预览图、素材预处理。",
        analogy="本辑「无头/批处理渲染」这条线上的实用件。**MOC3 支持**是关键 —— "
                "配上一辑 Rev2D 的「确定性地出图」，你就有了「模型改动前后自动出对比图」的自动化基础。",
        warn="⚠️ 实现语言是 **Jupyter Notebook**（不是打包好的 CLI 二进制），"
             "要自己看 notebook 怎么调。⚠️ Unlicense 虽然最自由，但也意味着**没人兜底**。",
        ext=(75, "7.5/10", "Unlicense（公共领域）+ 支持 MOC3，容易被别的流水线嵌进去"),
        use=(70, "7.0/10", "做素材预处理 / 出预览图 / 建数据集时现成可用 · Unlicense · 推送 2026-10-02"),
        src="推送 2026-10-02 · 29★ · Unlicense · Jupyter Notebook · 信源 [1242]",
    ),
    dict(
        nid="rpm35c11", name="moc3-json-viewer（单文件 HTML 的 moc3 JSON 查看器，零依赖）",
        url="https://github.com/Hana-ame/moc3-json-viewer",
        lang="HTML", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="**一个 HTML 文件**：纯 Canvas2D 写的 moc3 JSON 查看器，零依赖、上传即看、"
              "**不存储任何模型数据**（隐私友好）。",
        analogy="你不用把它当「工具」用 —— 它的正确用法是**拖进你自己的 GitHub Pages 索引站当一个小功能**。"
                "一个文件、零依赖、不联外网，几乎零成本。",
        warn="⚠️ 0★、**未声明 license** → 挂到公开站点前先确认（既然要公开，就别用来源不明的代码）。"
             "⚠️ 它看的是 **moc3 的 JSON 表达**，不是渲染模型本体。",
        ext=(60, "6.0/10", "零依赖单文件，可整体嵌进任何静态站"),
        use=(72, "7.2/10", "给索引站加个「模型预览」小工具，几乎零成本 · 推送 2026-09-25"),
        src="推送 2026-09-25 · 0★ · 未声明许可 · HTML · 信源 [1243]",
    ),
    dict(
        nid="rpm35c12", name="live2d_models（网站看板娘模型集 + 加载代码，MIT · 28★）",
        url="https://github.com/jianchengwang/live2d_models",
        lang="JavaScript", stars="28",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="「萌萌哒的看板娘」—— 网站看板娘的 **Live2D 模型集 + 加载代码**，MIT、2026-10-08 仍在推。",
        analogy="你手上有个 GitHub Pages 索引站。这条是**「今天就能让站点多个会动的看板娘」**里最省事的一档 —— "
                "模型和加载代码都现成。",
        warn="⚠️ **模型版权归原画师**，仓库给的许可（MIT）通常只管**加载代码**，"
             "不等于模型本身可商用 —— 挂到公开站前看清每个模型各自的分发条款。",
        ext=(55, "5.5/10", "只是模型集 + 加载器，不是框架"),
        use=(75, "7.5/10", "给索引站加看板娘，用它最省事 · MIT（限代码）· 推送 2026-10-08"),
        src="推送 2026-10-08 · 28★ · MIT · JavaScript · 信源 [1244]",
    ),
    dict(
        nid="rpm35c13", name="pyqt-live2d-bridge（在 PyQt5 里渲染 Live2D，MIT + Python）",
        url="https://github.com/canyueY/pyqt-live2d-bridge",
        lang="Python", stars="1",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="在 **PyQt5** 里渲染 Live2D Cubism 模型，并做动作、表情、情绪绑定。",
        analogy="你的环境是 Python 主线。想在**纯 Python** 里做 Live2D 桌面程序（桌宠 / 工具），"
                "这条是最直接的桥 —— 不用学 C# 也不用学 Rust。",
        warn="⚠️ 1★、`pushed` 停在 2026-09-19，属个人小项目。⚠️ PyQt5 + Cubism 本体的"
             "部署（Core 动态库）仍要自己处理，别以为是 `pip install` 就完事。",
        ext=(60, "6.0/10", "Python 生态里的桥接层，MIT 干净"),
        use=(65, "6.5/10", "用 Python 写桌宠/工具时的现成起点 · MIT · 推送 2026-09-19"),
        src="推送 2026-09-19 · 1★ · MIT · Python · 信源 [1245]",
    ),
    dict(
        nid="rpm35c14", name="anime-desktop-pet（多角色 Live2D 桌宠，MIT + 轻量 JS）",
        url="https://github.com/SherlockYzz/anime-desktop-pet",
        lang="JavaScript", stars="9",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="AI 桌面宠物，支持**多个**动漫角色的 Live2D 形象，JS/Electron 栈。",
        analogy="桌宠这类项目最大的浪费是「每个都只管一个角色」。这条的**多角色管理**逻辑，"
                "是自建桌宠时可以直接拆出来用的那部分。",
        warn="⚠️ 9★、很新（2026-10-06）。⚠️ 「AI」部分是接你自己的后端还是内置，"
             "装之前先看 README，别默认它能离线跑。",
        ext=(65, "6.5/10", "MIT + 轻量 JS，多角色切换逻辑可复用"),
        use=(70, "7.0/10", "自建桌宠的现成骨架，装上即用 · MIT · 推送 2026-10-06"),
        src="推送 2026-10-06 · 9★ · MIT · JavaScript · 信源 [1246]",
    ),
    dict(
        nid="rpm35c15", name="emote-to-cubism（E-mote(PSB) → Live2D Cubism 的转换工具链与格式文档）",
        url="https://github.com/funlin724/emote-to-cubism",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="把 **E-mote 格式（PSB）转成 Live2D Cubism** 的转换工具链 + 格式文档；"
              "明确「不含游戏素材、无厂商密钥」（自带文件）。",
        analogy="本辑最冷门但可能最值钱的一条**格式文档**。E-mote 是视觉小说圈的另一套 2D 动画体系，"
                "两个格式之间的差异文档**中文圈几乎没人写**。你不一定需要转换器，但那份**格式对照**值得存。",
        warn="⚠️ 0★、小众格式。⚠️ 「自己提供文件」意味着它**不附带任何素材**，"
             "要转换得你有合法的源文件。⚠️ 逆向他方格式前先看各自 EULA。",
        ext=(60, "6.0/10", "MIT；格式文档本身可复用，工具链随格式变动"),
        use=(55, "5.5/10", "手上有 E-mote 资产时才用得上；否则当格式资料存着 · MIT · 推送 2026-09-19"),
        src="推送 2026-09-19 · 0★ · MIT · Python · 信源 [1247]",
    ),
    dict(
        nid="rpm35c16", name="Bunraku（首个端到端「单图 → 可编辑 Live2D」+ 首个基准）",
        url="https://github.com/SparcAI-Inc/Bunraku",
        lang="Python", stars="37",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="arXiv **2607.27348**（2026-07-29，清华 / 南洋理工 / SparcAI）的代码仓。**Stage 1** 用「懂 Live2D "
              "器官级 taxonomy」的分层扩散，从单图生成**有序 RGBA 图层堆叠 + 遮挡区补全**；**Stage 2** 只凭每层 "
              "alpha 建三角网格，把所有层顶点当**同一序列的 token**、自注意力**跨层**，**联合**预测关键姿势顶点位移。"
              "核心论点：**靠联合预测，不是靠堆网络**（放大 112× 无增益）。附带首个该任务基准 **Live2D-Bench**"
              "与 **8,884 个模型**的语料库。也因为网格只由 alpha 生成，**换装/改纹理可复用网格与动画**。",
        analogy="v29 我们有「单图自动生成会散架」的失败实录；这条是**正面顶上来**的第一个端到端系统 —— "
                "还顺手给了个可比的基准。**正反两面现在都有了**。",
        warn="⚠️ **无 license + 37★ + 创建即停更（pushed = 2026-07-31）** → **今天只能当「尺子」，不能当产线**。"
             "⚠️ **头号指标有水分**，见下一条（`pith.science` 的审稿报告）—— 用之前必须先读那三条。",
        ext=(70, "7.0/10", "发了 Live2D-Bench + 8884 模型语料，是这条赛道第一个可比的参照系"),
        use=(45, "4.5/10", "不能直接用；价值在「拿它的指标去筛别人的宣传」· 未声明许可 · 推送 2026-07-31"),
        src="推送 2026-07-31 · 37★ · 未声明许可 · 信源 [1248]",
    ),
    dict(
        nid="rpm35c17", name="hermes-live2d（把编码 agent 的 TTS 路由到桌面宠物，★115）",
        url="https://github.com/Soundpulse/hermes-live2d",
        lang="Rust", stars="115",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "星少但有用")],
        plain="给 NousResearch 的 **hermes agent** 配一个 Live2D 身体：把 agent 生成的 TTS 音频经 Tailscale 推到"
              "本机桌宠上做**口型同步 + 气泡**。栈 = **Tauri 2 + pixi-live2d-display**，带表情、鼠标追踪、"
              "本地 HTTP API，内置 Sparkle 模型。",
        analogy="这是 v29 记的「Live2D × 编码 agent 桌宠集群」的**又一条**（已有 dsh-live2d-pets / agent-avatar）。"
                "它 ★115 是集群里偏高的 —— 但**集群里同时出现了「许可证不详」和「渲染栈版本落后」两个通病**，"
                "这条两样都占。",
        warn="⚠️ **无 license**（NOASSERTION）+ 栈是 `pixi-live2d-display`（老 Cubism 分叉，"
             "**未确认 Core 版本**，与 v29 记的「停在 Core 4」同风险）。⚠️ `pushed` 停在 2026-08-03。"
             "→ **看它「agent→TTS→Live2D 参数」的接线，别先装它**。",
        ext=(65, "6.5/10", "Tauri 桌面壳 + 本地 HTTP API，接线思路可复用到自己 agent"),
        use=(55, "5.5/10", "方向同层，但许可与版本都有坑 → 观察 · 未声明许可 · 推送 2026-08-03"),
        src="推送 2026-08-03 · 115★ · 未声明许可 · Rust · 信源 [1249]",
    ),
    dict(
        nid="rpm35c18", name="Cubism Editor 官方 Release History（本辑最重要的一次「版本口径修正」）",
        url="https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="官方 docs 的 Release History 表：**09/03/2026 → Cubism 5.3.04（最新正式版）**、"
              "06/16/2026 → 5.3.03、04/02/2026 → 5.3.02、02/24/2026 → 5.3.01、01/20/2026 → 5.3.00。",
        analogy="⚠️ **上一辑写的「现在唯一该用的编辑器版本是 5.3.00」是过期口径。** 原因值得记住："
                "官方**产品页**只列大版本（5.3.00），**patch 号只藏在 docs 的 Release History 表里** —— "
                "**同一个官网两处口径不一致**。以后查版本，**要写清是哪一站哪一页**。",
        warn="⚠️ 本辑只核到版本号与日期，**未逐条读 5.3.01–5.3.04 各自更新了什么**（下辑可补）。"
             "⚠️ 对新项目的影响：装的应是 **5.3.04**，不是 5.3.00。",
        ext=(20, "2.0/10", "它不是工具；是一条**必须记进版本钉子的更正**"),
        use=(85, "8.5/10", "查版本号的权威落点；写「版本钉子」时的唯一依据 · 官方文档 · 信源 [1250]"),
        src="docs.live2d.com 官方 Release History · 2026-09-03 条目 · 本辑核实 · 信源 [1250]",
    ),
    dict(
        nid="rpm35c19", name="官方学生优惠（简中站 80% OFF，¥7,344 / 3yr，学信网验证码可申）",
        url="https://www.live2d.jp/chn/student-discount/",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="官方 Live2D 学生优惠的**中国大陆口径**：**2026 年度限定 80% OFF** —— "
              "正常价 RMB **1,552 [¥36,720]** → 学生价 RMB **310 [¥7,344] / 3 年**；"
              "**特别优惠截止 2027-03-31**；内容 = Cubism **PRO for indie 三年套餐**；"
              "**无学校邮箱者可用「学信网在线验证码」申请**（审查约 5–6 天）；非自动续费；"
              "毕业前购买可**用到订阅期满**。页面另含 LEAP（面向教育机构免费借出 Editor PRO）。",
        analogy="上一辑引英文站得 **76% OFF / $238.20→$57.16**，本辑引简中站得 **80% OFF / ¥36,720→¥7,344** —— "
                "**两个都是官网，区域不同、结算页不同**。→ 结论不是「哪个对」，而是"
                "**「以自己所在区域的结算页为准，别信首页宣传语」**。",
        warn="⚠️ 促销与学割**不是一回事**：本辑另有一条「秋季专享特惠 8 折 PRO **2026-10-11 截止**」"
             "（仅简中站有）→ **别为了那 20% 冲动买单，学割是 80% OFF、截止 2027-03-31，时间很宽**。"
             "⚠️ 优惠券的适用范围以结算页为准。",
        ext=(20, "2.0/10", "不是工具；但它会重估「绕开 Editor 的那一堆方案」的性价比"),
        use=(95, "9.5/10", "**在校生的直接省钱口子**：¥310 拿三年 PRO，学信网验证码通道不需要学校邮箱 · 信源 [1251]"),
        src="live2d.jp/chn 官方学生优惠页 · 2026-10-11 核实 · 信源 [1251]",
    ),
    dict(
        nid="rpm35c20", name="《Bunraku 的 0.768 是上限，不是交付精度》（公开审稿报告 = 打假清单）",
        url="https://www.pith.science/p/2607.27348",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="社区公开审稿报告，**用论文自己的数据**指出三条 major：① 头号指标 **0.7676（median 0.8278）"
              "测的是美术手作网格**，而部署管线实际用**由 alpha 推导的自动网格**（§3.4 Eq.3），"
              "论文**从未报告全管线对该指标的实测** —— 审稿人反推：重网格化 24% 的层就掉 0.063 cosine，"
              "是所研究「模型效应」的两倍，而部署 auto-mesh 平均每层 ~83 顶点（比美术网格更密）"
              "→ **0.768 是上限，不是交付精度**；② 与 image-to-video baseline 的比较**未在同一协议下跑**；"
              "③ **`ParamEyeLOpen/R`（眨眼）在自动分解层上直接失效**（驱动它会移动整个头部组），"
              "论文因此把眨眼排除出 in-the-wild 测试。",
        analogy="这是本辑**最值钱的一条**，而且价值不在它有答案，而在它给了**尺子**："
                "以后看到任何「一张图生成 Live2D」，先过三问 —— ① 主指标测的是**手作网格**还是**部署网格**？"
                "② baseline 是否**同协议**？③ **眨眼参数**在自动分解层上成没成？**三问有一不过，宣传就得打折。**",
        warn="⚠️ **页面未给发布日 → 日期未核实**（按房规如实标注）。⚠️ 二者合并读才有意义："
             "Bunraku 给「赛道参照系」，这份给「参照系的水分」；**单看任何一篇都会被带偏**。",
        ext=(45, "4.5/10", "作为**判据清单**可长期复用；作为文章不可拓展"),
        use=(90, "9.0/10", "**本辑最该读的一条** —— 配上 v29 的失败实录，正反两面就齐了 · 信源 [1252]"),
        src="pith.science 公开审稿报告 · 日期未核实 · 2026-10-11 核实 · 信源 [1252]",
    ),
    dict(
        nid="rpm35c21", name="《图形引擎实战：Live2D 项目应用及落地》（大厂引擎组写的立绘规范）",
        url="https://blog.csdn.net/qq_41166022/article/details/144141757",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="**畅游引擎部**的应用研发分享（**首发 2024-12-02**，CSDN 转载）。三块硬货："
              "① **Live2D vs Spine 选型**（NIKKE 从 Live2D 改用 Spine 的真实原因；"
              "Spine 无变形器概念、做转向透视效率低于 Live2D；Live2D 的「胶水权重」只作用于相邻两个旋转变形器；"
              "判据：**参数个数为 n 时表情复杂度可达 2ⁿ**）；② **原画拆分规范**"
              "（**角色高度 > 3000px、建议画布 > 4000px**，官方示例 **5800×8400**，"
              "「宁可大图缩小」；脸/眼/嘴/发/阴影逐项规范 + 常见错误清单；**补色层在 Live2D 中直接禁止**；"
              "「图像左侧是角色的右身，应以 R 为后缀」）；③ **Unity 落地两个坑**"
              "——**动态渐变减弱**（参数 A+B 叠加，本该闭眼却半睁）与**渐变穿帮**，"
              "解法是 SDK 的 **MotionFade**（可分设淡入/淡出时间）。",
        analogy="本辑**最贴你目标（Ren'Py 视觉小说立绘）的一条**：它把「立绘该画多大」「脸眼嘴发阴影怎么拆才不出血」"
                "「哪些图层效果在 Live2D 里是禁的」全落成了可执行规范 —— **可以直接抄进你自己的立绘规格书**。",
        warn="⚠️ CSDN 页面把「首发 2024-12-02」与「最新推荐 **2026-08-31**」并列，"
             "**易被误读成 2026 新文** → 引用时必须写首发日。⚠️ Unity 那节原理可平移到任何按参数插值的引擎（含 Ren'Py），"
             "但具体 API 是 Unity 的。",
        ext=(40, "4.0/10", "作为工程规范长期有效，但不是可执行代码"),
        use=(92, "9.2/10", "**做立绘前必读**：画布尺寸 / 拆层规范 / 禁用项 / 渐变两个坑 · 首发 2024-12-02 · 信源 [1253]"),
        src="CSDN qq_41166022（转载畅游引擎部）· 首发 2024-12-02 · 2026-10-11 核实 · 信源 [1253]",
    ),
    dict(
        nid="rpm35c22", name="《表情差分怎么跟身体拼接 + 在 Ren'Py 里怎么定位》（含 opencv 对齐脚本）",
        url="https://live2dhub.com/t/topic/6117/3",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="Live2DHub 论坛帖。楼主想**用 Ren'Py 做一个 Live2D 立绘播放器**，卡在「表情差分怎么拼 + 怎么定位」。"
              "两条可抄路线：① **VivaLaze 的 opencv 对齐脚本** `emo_face_match.py` —— "
              "用 `cv2.matchTemplate(..., TM_CCOEFF_NORMED)` 求差分小图在身体大图里的左上角偏移 `(x, y)`、"
              "低于 0.8 告警，再用透明 padding 贴到同尺寸 BGRA 画布、偏移写进 `match_log.log`；"
              "② **nozomi 的路线** —— 差分优先用 Ren'Py 的 **`layeredimage`**（但**必须先定义所有角色的所有参数**，"
              "角色一多就失控），静图给 `im.Composite((1058,1256),(0,0),\"stand.png\",(499,89),\"default.png\")` 示例。"
              "顺带纠正一个误解：**Ren'Py 加载前就会把图剪裁到非透明像素包围盒，自己裁图既不提速也不减尺寸**。",
        analogy="你正是「目标 Ren'Py + 要拼表情差分」的人。这条把两个具体问题都给了可跑代码 —— "
                "那个 opencv 脚本算出的 `(x,y)` **正好是 `im.Composite` 要的坐标**，两半能接上。",
        warn="⚠️ 脚本自带 `print(\"警告：匹配度{max_val}较低\")` —— **f-string 漏了 `f` 前缀**，"
             "那句永远不会插值 → 抄用时自己补。**不是编造功能，是作者笔误**。"
             "⚠️ 帖子只显示月日不含年份 → **年份未核实**。⚠️ 前置约束：差分图必须是身体图上某区域的**精确裁剪**（尺寸一致），"
             "且**输入路径避免非西文字符**。",
        ext=(55, "5.5/10", "脚本小而通用；「Ren'Py 会预剪裁包围盒」这条是通用知识"),
        use=(88, "8.8/10", "**本辑对你的 Ren'Py 主线最直接的一条** · 年份未核实 · 信源 [1254]"),
        src="live2dhub.com/t/topic/6117 · 年份未核实 · 2026-10-11 核实 · 信源 [1254]",
    ),
    dict(
        nid="rpm35c23", name="《在 Bianbu 桌面上养一只真正可用的 Live2D 桌宠》（RISC-V 上的完整工程记录）",
        url="https://forum.spacemit.com/t/topic/1621",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="在 **RISC-V 开发板**（SpacemiT K1/K3 + Bianbu LXQT + Wayland）上跑通 Live2D 桌宠的完整记录"
              "（作者 chenjiayi，2026-08-30；仓库 `gitee.com/achenjiayi/rv_ive2d_pet`）。架构 = "
              "**Cubism Web Runtime 画 → Headless Chromium 出 RGBA 帧 → GTK Overlay 贴桌面**。"
              "关键技术点：**透明区域点击穿透靠逐帧 alpha 分析、只把不透明区注册为输入 region**；"
              "明确踩坑 —— **Cubism Native SDK 没有 RISC-V 官方档位**、且 **moc3 受版权保护不能逆向拆解**，"
              "所以绕开 Native 走 Web；Wayland/X11 并存时 GTK3 会误走 X11，解法是显式 `GDK_BACKEND=wayland`。"
              "支持 **moc3 v2–v5**，**Cubism 2 的 `.moc` 不兼容**。",
        analogy="技术栈（Wayland/GTK/RISC-V）与你完全不同，**不能照抄**；但两条判据对你**判断 Ren'Py 走 Native 还是 Web**"
                "有旁证价值：① **Native SDK 在非主流架构上没有档位**；② **moc3 不可逆向** → 想支持它只能走官方 runtime。"
                "它还证明了**一个 Web runtime 可以通吃 moc3 v2–v5**。",
        warn="⚠️ 页面显示「8月 30 日」**不含年份**（据论坛当前年份推定为 2026-08-30）→ **年份未核实**。"
             "⚠️ 部分数字（如 `.deb` 版本 0.3.15→0.3.18、穿透 ~8Hz）来自正文自述。",
        ext=(65, "6.5/10", "「Web runtime + 无头浏览器 + overlay」这条路可移植到任何桌面"),
        use=(65, "6.5/10", "不当方案用，当**判据与旁证**用 · 年份未核实 · 信源 [1255]"),
        src="forum.spacemit.com/t/topic/1621 · 2026-08-30（年份推定）· 2026-10-11 核实 · 信源 [1255]",
    ),
    dict(
        nid="rpm35c24", name="dsh-live2d-companion（DSH 的 Live2D 监控面板/桌宠，带 8 态状态机）",
        url="https://dshbase.com/plugins/dsh-live2d-companion",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="把 Live2D 角色接进 **DSH Web GUI** 的桌宠/挂件（安装源 `github:Tisitan/dsh-live2d-companion`，"
              "目录页 ★7 / 最后推送 2026-08-24）。**8 态状态机**（空闲/思考/工作/等待确认/报错/完成/睡眠/离线）+ 状态灯；"
              "纯**用户级 patch 挂载**（对 DSH 本体零修改、**DSH 升级免疫**）；模型接入做**两级绑定** —— "
              "**第一级自动嗅探**（解析 `.model3.json` 的 `FileReferences`，按文件名关键词模糊匹配槽位，"
              "如 `shy`→害羞、`nod`→点头）+ **第二级手动绑定编辑器**（写 `profile.json` 热生效）。"
              "许可边界明确：**仓库 MIT，但不含任何模型与 `live2dcubismcore.min.js`**。"
              "记了一个真坑：**Idle 池守卫** —— 睡眠动作若也在 `Idle` 组，会被随机抽中的站立动作「睁眼诈尸」。",
        analogy="你维护的就是 DSH，这条是**最贴合你工具链**的一类。真正值钱的是那套**「自动嗅探 + profile.json 手动兜底」"
                "的绑定层设计** —— 可以直接借到「给模型做语义槽位」的任何场景上。",
        warn="⚠️ 这是**插件目录页**，不是实战复盘；**页面数字（★7 / 最后推送）未在本机复核**，当线索不当结论。"
             "⚠️ 与上一辑的 `cyanfish-x/dsh-live2d-pets`、`Andersen216/dsh-whale-girl-live2d` 是**同题竞品**，别装重。",
        ext=(70, "7.0/10", "两级绑定的设计可直接迁移；用户级 patch 不侵入本体"),
        use=(75, "7.5/10", "本机在跑 DSH，值得先读它的绑定层再决定装哪个 · 信源 [1256]"),
        src="dshbase.com 插件目录 · 最后推送 2026-08-24 · 2026-10-11 核实 · 信源 [1256]",
    ),
]

FOOTNOTES = [
    (1233, "https://github.com/moeru-ai/airi", "moeru-ai/airi",
     "50263★ · MIT · TypeScript · 推送 2026-10-11 · GitHub REST API 实测"),
    (1234, "https://github.com/elevenyellow/handcrafted-persona-engine",
     "elevenyellow/handcrafted-persona-engine",
     "1381★ · 未声明许可 · C# · 推送 2026-05-20 · GitHub REST API 实测"),
    (1235, "https://github.com/Andersen216/dsh-whale-girl-live2d", "Andersen216/dsh-whale-girl-live2d",
     "28★ · MIT · JavaScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1236, "https://github.com/shinshin86/aituber-onair", "shinshin86/aituber-onair",
     "267★ · MIT · TypeScript · 推送 2026-10-11 · GitHub REST API 实测"),
    (1237, "https://github.com/momori777/Artemis", "momori777/Artemis",
     "381★ · NOASSERTION · Python · 推送 2026-09-30 · GitHub REST API 实测"),
    (1238, "https://github.com/ptghb/virtual-person", "ptghb/virtual-person",
     "45★ · NOASSERTION · TypeScript · 推送 2026-10-08 · GitHub REST API 实测"),
    (1239, "https://github.com/fifteen42/live2d-from-art", "fifteen42/live2d-from-art",
     "11★ · 未声明许可 · Python · 推送 2026-09-15 · GitHub REST API 实测"),
    (1240, "https://github.com/Pal-AI-Lab/Cortico", "Pal-AI-Lab/Cortico",
     "198★ · MIT · TypeScript · 推送 2026-10-11 · GitHub REST API 实测"),
    (1241, "https://github.com/GunGuyDude-Python/renpy-live2d-plus", "GunGuyDude-Python/renpy-live2d-plus",
     "0★ · GPL-3.0 · Python · 推送 2026-05-15 · GitHub REST API 实测"),
    (1242, "https://github.com/KurisuMakise004/renderkit", "KurisuMakise004/renderkit",
     "29★ · Unlicense · Jupyter Notebook · 推送 2026-10-02 · GitHub REST API 实测"),
    (1243, "https://github.com/Hana-ame/moc3-json-viewer", "Hana-ame/moc3-json-viewer",
     "0★ · 未声明许可 · HTML · 推送 2026-09-25 · GitHub REST API 实测"),
    (1244, "https://github.com/jianchengwang/live2d_models", "jianchengwang/live2d_models",
     "28★ · MIT · JavaScript · 推送 2026-10-08 · GitHub REST API 实测"),
    (1245, "https://github.com/canyueY/pyqt-live2d-bridge", "canyueY/pyqt-live2d-bridge",
     "1★ · MIT · Python · 推送 2026-09-19 · GitHub REST API 实测"),
    (1246, "https://github.com/SherlockYzz/anime-desktop-pet", "SherlockYzz/anime-desktop-pet",
     "9★ · MIT · JavaScript · 推送 2026-10-06 · GitHub REST API 实测"),
    (1247, "https://github.com/funlin724/emote-to-cubism", "funlin724/emote-to-cubism",
     "0★ · MIT · Python · 推送 2026-09-19 · GitHub REST API 实测"),
    (1248, "https://github.com/SparcAI-Inc/Bunraku", "SparcAI-Inc/Bunraku",
     "37★ · 未声明许可 · 推送 2026-07-31 · arXiv 2607.27348 · GitHub REST API 实测"),
    (1249, "https://github.com/Soundpulse/hermes-live2d", "Soundpulse/hermes-live2d",
     "115★ · 未声明许可 · Rust · 推送 2026-08-03 · GitHub REST API 实测"),
    (1250, "https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title",
     "docs.live2d.com · Cubism Editor Release History",
     "官方 · 5.3.04（2026-09-03）为最新正式版 · 2026-10-11 核实"),
    (1251, "https://www.live2d.jp/chn/student-discount/", "live2d.jp/chn · Live2D 学生优惠（80% OFF）",
     "官方 · ¥36,720 → ¥7,344 / 3yr · 截止 2027-03-31 · 学信网验证码可申 · 2026-10-11 核实"),
    (1252, "https://www.pith.science/p/2607.27348", "pith.science · Bunraku 公开审稿报告",
     "三条 major 意见 = 一键生成 Live2D 打假清单 · 日期未核实 · 2026-10-11 核实"),
    (1253, "https://blog.csdn.net/qq_41166022/article/details/144141757",
     "CSDN qq_41166022 · 图形引擎实战：Live2D 项目应用及落地（畅游引擎部）",
     "立绘画布/拆层规范 + 渐变减弱与穿帮 · 首发 2024-12-02 · 2026-10-11 核实"),
    (1254, "https://live2dhub.com/t/topic/6117/3", "live2dhub.com/t/topic/6117 · 表情差分拼接与 Ren'Py 定位",
     "opencv 对齐脚本 + layeredimage/im.Composite · 年份未核实 · 2026-10-11 核实"),
    (1255, "https://forum.spacemit.com/t/topic/1621", "forum.spacemit.com/t/topic/1621 · RISC-V 上的 Live2D 桌宠",
     "Web runtime + headless Chromium + GTK overlay · 2026-08-30（年份推定）· 2026-10-11 核实"),
    (1256, "https://dshbase.com/plugins/dsh-live2d-companion", "dshbase.com · dsh-live2d-companion",
     "DSH 的 Live2D 桌宠插件 · 8 态状态机 + 两级绑定 · 最后推送 2026-08-24 · 2026-10-11 核实"),
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

    desc = ('第三十辑三路调研（gh 路 64 条 / cn 路 14 条 / official 路 16 条），本版取 24 项，'
            '主题 **Live2D 制作 · 实战测评 · 上新**。所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测。'
            '<strong>本辑主线：前四辑一直在「找工具」，本辑第一次有了「尺子」和「账号」——'
            '① 第一个端到端「单图 → 可编辑 Live2D」的系统 Bunraku 与首个基准 Live2D-Bench 出现，'
            '同时 pith.science 的公开审稿报告用论文自己的数据拆穿了它的头号指标（0.768 测的是美术手作网格、'
            '部署自动网格从未被测、眨眼参数在自动分解层直接失效）→ 这三点成了「一键生成 Live2D」的打假清单；'
            '② 官方两处口径被推翻（Cubism 正式版是 5.3.04 不是 5.3.00，patch 只藏在 docs 的 Release History；'
            '学生优惠简中站是 80% OFF 而非英文站的 76%）；'
            '③ agent 桌宠这条线有了主干（moeru-ai/airi · MIT · ★50,263）</strong>。'
            '中文侧补上了可执行的立绘规范（畅游引擎部：画布 >3000px、拆层规范、补色层禁用、渐变减弱/穿帮）。')

    block = ['    <div class="group" data-page-node-id="rpm35g">',
             '      <div class="group-title" data-page-node-id="rpm35gt">🆕 第三十五版增补 · Live2D 制作 × 实战测评 × 上新：第一把「打假尺子」、两处官方口径修正、agent 桌宠有了主干（24 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm35gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm35r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm35ra%s">%s</a> — %s</div>'
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
