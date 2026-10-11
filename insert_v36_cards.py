# -*- coding: utf-8 -*-
"""第三十六版增补：把第三十一辑「不买 Cubism Editor 的那条路，第一次有了完整栈」的 22 个条目登记进 index.html。

本辑候选：gh 路 37 条（20+ 组查询，双时间窗）、cn 路 8 条（采纳 3）、official 路 29 条。
与 `index.html`（1257 项）及全部历史存档机器比对，本版 22 条命中 **0**。

**本辑主线：前五辑在 Live2D 上一直是「找工具」，这一辑第一次出现了「一整套不买 Editor 的替代栈」。**

1. **开源替代从「只有个编辑器」补齐成了「SDK 本体 + 绑定界面 + 自动化 CLI」** ——
   `Inochi2D/inochi2d`（★1811 · BSD-2-Clause，**SDK 本体此前一直漏收，只收过它的编辑器**）
   + `nijigenerate/nijigenerate`（★314，配套绑定编辑器）
   + `CheshireMew/PuppetLoom`（★245，PSD→绑定自动化 + Codex skill，明确标 Windows）。
2. **「单图/PSD → 可用模型」这条流水线开始分叉成两条路** ——
   一条**只在网格层动手**（`shinshin86/mesh-avatar-studio` ★597、`marukun712/kokoro` ★42），
   天然绕开前几辑反复撞的 **Cubism Core ABI** 那道墙；
   另一条**直接对 moc3**（`J621111/live2d-automation`，但导出的是 mock；无许可证）。
3. **官方侧两处口径冲突被定位** —— ① **学生优惠的「76% vs 80%」不是两站打架，是同一张英文首页新旧文案没统一**，
   权威值 **80%**（学生专页 + 结算页一致，截止 2027-03-31）；
   ② LEAP 覆盖校数**首页写 200+、专页写 450+**（截至 2025-03）。
   SDK 侧修正上一辑「全线 5-r.5」的说法：**是分线各自版本**（Unreal R1 beta2 = 2026-09-29 为最新一次更新）。
4. **一个必读的破坏性变更**：`live2d-py` 升 **1.0.0**（2026-09-30）——
   统一 `live2d.Model` 加载、**移除 `live2d.v3` 与 `live2d.v2cpp` 模块** → 旧代码会直接跑不起来。

**inbox 顺延**：房规压缩（**连续第六轮欠账**，现 200/200 行贴顶）；`/skill-doctor`（连续第十轮）。

数据来源：2026-10-11 GitHub REST API 实测（`gh api repos/<r>` 逐条）+ 一手页面（`_r31/`）。
幂等：已存在本版标记则跳过。
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1256"'
FIRST_NEW_FOOTNOTE = 1257
MARKER = "第三十六版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十五版增补 2026-10-11',
    '共 1257 个项目',
    '第三十四版增补 18 项 + 第三十五版增补 24 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十六版增补 2026-10-11',
    '共 1279 个项目',
    '第三十四版增补 18 项 + 第三十五版增补 24 项 + 第三十六版增补 22 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm36c1", name="inochi2d（Live2D 的开源替代：木偶 SDK 本体）",
        url="https://github.com/Inochi2D/inochi2d",
        lang="D", stars="1811",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="开源 2D 木偶（puppet）动画 SDK —— 把分层立绘绑成**可实时驱动、带表情与物理**的 2D 角色，"
              "定位就是 Live2D Cubism 的开源替代，用于 VTubing、游戏与实时应用。",
        analogy="前几辑只收过它的**编辑器** inochi-creator，**SDK 本体一直漏在外面** —— "
                "等于只记了「有把螺丝刀」，没记「有个电动工具台」。这条补上的是整套路线的根。",
        warn="⚠️ 语言是 **D**（不是 Python / JS），要自己编译；生态比 Cubism 小得多，"
             "**缺现成模型与教程**，遇到问题也没有中文答案。",
        ext=(85, "8.5/10", "BSD-2 许可宽松 + 开放格式，可直接嵌进自研渲染管线"),
        use=(70, "7.0/10", "「不买 Cubism Editor」路线唯一成熟的开源选择 · 代价是 D 语言 + 生态小"),
        src="推送 2026-10-03 · 1811★ · BSD-2-Clause · D · 信源 [1257]",
    ),
    dict(
        nid="rpm36c2", name="nijigenerate（配 inochi2d 的绑定编辑器）",
        url="https://github.com/nijigenerate/nijigenerate",
        lang="D", stars="314",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="面向 nijilive 木偶格式（从 Inochi2D v0.8 派生）的开源**绑定编辑器** —— "
              "给模型绑骨、绑定，输出供游戏或 VTubing 实时使用。可以理解成 Inochi2D 生态里的「Cubism Editor 角色」。",
        analogy="只有 SDK 是没法干活的，必须有一个能看见、能拖参数的界面。上一条负责引擎，这条负责**手**。"
                "两者配齐，开源替代才从「一个库」变成「一条流水线」。",
        warn="⚠️ 同样是 **D** 语言，Windows 上装它要走 dub 工具链；"
             "⚠️ 它的格式与 Cubism 不互通，**不能拿它去开 .moc3**。",
        ext=(70, "7.0/10", "输出开放格式，方便脚本化批量处理"),
        use=(65, "6.5/10", "与 inochi2d 配套使用 · 推送 2026-10-10，仍在活跃"),
        src="推送 2026-10-10 · 314★ · BSD-2-Clause · D · 信源 [1258]",
    ),
    dict(
        nid="rpm36c3", name="mesh-avatar-studio（一张插画 + 编码 agent → 可动 2D 网格形象）",
        url="https://github.com/shinshin86/mesh-avatar-studio",
        lang="TypeScript", stars="597",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-mod", "模块化")],
        plain="把**一张插画**变成可动画的 2D 网格（mesh）虚拟形象 —— 用「编码 agent + 本地编辑器」"
              "跑绑定与驱动，主打一条 agent 流程出可动立绘。",
        analogy="**建仓 7 天就 597★**，说明「让 agent 来干绑定」这个念头大家都在想。"
                "它的取巧之处是**只在网格层动手、不碰 `.moc3`** —— 于是天然绕开了前几辑反复撞的 "
                "Cubism Core ABI 那道墙。",
        warn="⚠️ **极新**（2026-10-04 建仓），没有历史沉淀，也别指望教程；"
             "⚠️ 输出的是自有网格格式，**不是 Cubism 工程**，导不进 VTube Studio。",
        ext=(80, "8.0/10", "MIT + 网格层开放，容易接到自己的渲染器"),
        use=(75, "7.5/10", "与「agent 驱动内容生产」这条主线高度吻合 · 但属尝鲜，别当生产依赖"),
        src="推送 2026-10-11 · 597★ · MIT · TypeScript · 信源 [1259]",
    ),
    dict(
        nid="rpm36c4", name="PuppetLoom（分层 PSD → 可自动制作、可校验的 2D 角色）",
        url="https://github.com/CheshireMew/PuppetLoom",
        lang="TypeScript", stars="245",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="把分层角色 PSD 变成「**可自动制作、可验证、可继续校准**」的动态角色 —— "
              "Electron 桌面应用 + CLI + 一个 **Codex skill**。仓库 topics 直接写着 "
              "`live2d` / `psd` / `vtuber` / `windows`，README 有中英日三语。",
        analogy="它的卖点不是「一键出模型」，而是**每一步都能被校验、被回退**。"
                "这正好对上前几辑反复说的那句：「AI 写标准模块可信，手感 / 边界 / 性能必须亲手验」。",
        warn="⚠️ **AGPL-3.0**：自己是工具自用没问题，但要当对外服务或分发，传染性很强；"
             "⚠️ GitHub 上的仓库描述是**空的**，以上是读 README 得到的（**仅 README 级核实**）。",
        ext=(75, "7.5/10", "CLI + skill 双入口，可被 agent 编排进流水线"),
        use=(70, "7.0/10", "明确标 Windows / Codex，与本机场景直接相关"),
        src="推送 2026-10-05 · 245★ · AGPL-3.0 · TypeScript · 信源 [1260]",
    ),
    dict(
        nid="rpm36c5", name="iki（Web 侧的开源木偶引擎 + AI 自动绑骨）",
        url="https://github.com/zeikar/iki",
        lang="TypeScript", stars="15",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="面向浏览器的一套开放 2D 木偶引擎，自带开放 `.iki` 格式、一个 **AI 自动绑骨器**，"
              "还捆了一个 **Claude Code 插件** —— 口号是「AI 能直接构建」。",
        analogy="前几辑的开源替代都偏桌面（D / C# / Rust），这条是少见的 **Web 侧**实现，"
                "而且是目前唯一**自带 agent 插件**的。",
        warn="⚠️ 只有 **15★**，个人项目早期；「AI 自动绑骨」的实际效果**没有任何第三方验证** —— "
             "对照上一辑立的打假三问：自动绑骨的头号毛病恰好就是**眨眼这类参数在自动分层上失效**。",
        ext=(70, "7.0/10", "开放格式 + agent 插件，接口设计偏「可编程」"),
        use=(55, "5.5/10", "星少、需自验；当 Web 侧思路参考，别当依赖"),
        src="推送 2026-10-10 · 15★ · MIT · TypeScript · 信源 [1261]",
    ),
    dict(
        nid="rpm36c6", name="Inkinesis（文本 / 图片 → Inochi2D 与 Live2D 双格式 rig）",
        url="https://github.com/codewayco/Inkinesis",
        lang="TypeScript", stars="6",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="把一张插画或一段文字变成「可移植的 2D 角色绑定」—— **同时输出 Inochi2D 和 Live2D 两种 rig**，"
              "并拿官方运行时做校验。",
        analogy="「一张图 → 可用模型」这条流水线和前几辑的 psd2live / See-through 同源，"
                "但它是**唯一双格式输出、且拿官方运行时自我校验**的。",
        warn="⚠️ **6★**，建仓不到三周；「用官方运行时校验」是作者自述，**未实测**。",
        ext=(75, "7.5/10", "Apache-2.0，双格式输出便于以后换栈"),
        use=(55, "5.5/10", "思路正、体量太小，仅登记观察"),
        src="推送 2026-10-05 · 6★ · Apache-2.0 · TypeScript · 信源 [1262]",
    ),
    dict(
        nid="rpm36c7", name="cubism-api-bridge（用脚本 / agent 驱动 Cubism Editor）",
        url="https://github.com/sayaka-aiart/cubism-api-bridge",
        lang="TypeScript", stars="11",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-warn", "实验性")],
        plain="Cubism Editor 官方 **External API** 的非官方 TS / Python 桥 + 本地 HTTP 服务，"
              "附 StandRig 集成 —— 让你能用脚本或 agent 去自动化 Editor。",
        analogy="前几辑的结论一直是「Editor 授权买的是**绑骨**，渲染用的 Core 免费」。"
                "这条正面回答「那绑骨这步能不能自动化」。",
        warn="⚠️ 官方 External API 是**付费版功能**；⚠️ 非官方桥意味着官方一改 API 就可能断，"
             "作者自己也标了 **Experimental**。",
        ext=(65, "6.5/10", "提供本地 HTTP 服务，接 MCP 很容易"),
        use=(50, "5.0/10", "只有在你已经有 Editor 授权时才谈得上有用"),
        src="推送 2026-09-12 · 11★ · MIT · TypeScript · 信源 [1263]",
    ),
    dict(
        nid="rpm36c8", name="live2d-auto-pipeline（素材 → 可部署模型的 Python 全流程）",
        url="https://github.com/mw2wbyys6t-sudo/live2d-auto-pipeline",
        lang="Python", stars="10",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "需自验")],
        plain="Live2D 全流程自动化：从素材出发，覆盖**拆分 / 绑定 / 导出**，"
              "目标是全自动产出「可部署运行」的 Live2D 模型。",
        analogy="它的野心和上一辑 `SparcAI-Inc/Bunraku` 是同一个方向。区别是 Bunraku 有论文有基准有审稿，"
                "这条什么都没有 —— **越是「全自动」的宣传，越要先过打假三问**。",
        warn="⚠️ **10★**；「全自动产出可部署模型」是本辑最需要打问号的一句，"
             "请对照三问：指标测的是手作网格还是自动网格 / 与 baseline 是否同协议 / 眨眼参数成没成。",
        ext=(65, "6.5/10", "Apache-2.0 + Python，便于塞进现有流水线"),
        use=(45, "4.5/10", "登记为主，**不要当能力已证实的工具**"),
        src="推送 2026-10-10 · 10★ · Apache-2.0 · Python · 信源 [1264]",
    ),
    dict(
        nid="rpm36c9", name="live2d-automation（单图 → Live2D 的 MCP Server）",
        url="https://github.com/J621111/live2d-automation",
        lang="Python", stars="77",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-warn", "无许可")],
        plain="Live2D 自动化的 **MCP Server** —— 提供图像分析、人脸提取、图层生成、绑骨、物理、动作、导出"
              "等一批 MCP 工具，从单张角色图生成中间态 Live2D 包；导出的是 **mock `.moc3`** 并带校验契约。",
        analogy="「让 agent 通过 MCP 去产模型」这条线，前几辑都是零散玩具；"
                "这是**第一个把工具面做全**的，也是最容易被 agent 编排的一个。",
        warn="⚠️ **无许可证**（只读参考）；⚠️ 导出的是 **mock `.moc3`，不是真能跑的模型**；"
             "作者自己标了并发 / TTL 等实验性约束。",
        ext=(70, "7.0/10", "MCP 工具面最全，天然可被 agent 调"),
        use=(50, "5.0/10", "方向对，但停在 mock + 无许可 → 不装、不当依赖"),
        src="推送 2026-09-27 · 77★ · 无许可证 · Python · 信源 [1265]",
    ),
    dict(
        nid="rpm36c10", name="BD2-L2D-Viewer（Web 端 Live2D + Spine 查看器）",
        url="https://github.com/Jelosus2/BD2-L2D-Viewer",
        lang="Vue", stars="540",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="《Brown Dust 2》的 **Web 端 Live2D 与 Spine 动画交互查看器**，纯浏览器渲染。",
        analogy="前几辑遇到的 viewer 都是 0★ 个人件；这条 540★、持续更新，"
                "是 Web 侧渲染**可以直接抄的成熟参考**。",
        warn="⚠️ 它是「查看器」不是「制作器」；⚠️ 内置模型是**游戏资产**，"
             "**别把它的模型拿去商用**。",
        ext=(70, "7.0/10", "MIT，组件可拆出来单用"),
        use=(65, "6.5/10", "想在网页里放个「能动的立绘」时最省事的一条"),
        src="推送 2026-10-08 · 540★ · MIT · Vue · 信源 [1266]",
    ),
    dict(
        nid="rpm36c11", name="warudo-agent-bridge（让 agent「看到并驱动」WARUDO）",
        url="https://github.com/StudioRaming/warudo-agent-bridge",
        lang="C#", stars="9",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="一个 **MCP server + CLI**，让 Claude / Codex / 任意 MCP 客户端能**看到并操作**正在运行的 WARUDO："
              "资产、角色姿势与 IK、表情、蓝图、相机、截图。已发 npm 包 `@studioraming/warudo-agent-bridge`。",
        analogy="这是「agent 直接操控虚拟形象」少见的**工程化**产物 —— "
                "不是再写一个桌宠，而是**把别人的演播软件变成 agent 的手脚**。这个思路比工具本身值钱。",
        warn="⚠️ **9★ 极新**；⚠️ WARUDO 本体是**付费商用软件**，桥免费但底座要钱。",
        ext=(70, "7.0/10", "走标准 MCP 接法，工具集清晰，可拆去看它怎么暴露场景 API"),
        use=(55, "5.5/10", "思路值得借；但你手上没有 WARUDO，落地不了"),
        src="推送 2026-10-10 · 9★ · MIT · C# · 信源 [1267]",
    ),
    dict(
        nid="rpm36c12", name="my-neuro（自制 AI 桌面伴侣的成熟基线）",
        url="https://github.com/morettt/my-neuro",
        lang="JavaScript", stars="1389",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="自制 AI 桌面伴侣：可定制角色 + 语音对话，**响应 1 秒内**，含长期记忆、视觉识别、"
              "声音克隆与 LLM 训练，兼容多种 Live2D 定制。",
        analogy="上一辑才说「agent 桌宠有了主干（airi ★50k）」。这条是**第二梯队里最成熟的一条** —— "
                "★1389、2024 年底建仓、持续维护。拿它当对照，能把「主干 / 玩具」的分界线画出来。",
        warn="⚠️ 默认栈偏重（视觉识别 + 声音克隆都要算力），**16GB 机器要按需关模块**。",
        ext=(80, "8.0/10", "MIT，模块较多、可裁剪"),
        use=(70, "7.0/10", "想抄「伴侣感」的交互设计，读它比读一堆教程快"),
        src="推送 2026-10-05 · 1389★ · MIT · JavaScript · 信源 [1268]",
    ),
    dict(
        nid="rpm36c13", name="Cyrene-Agent（带虚拟形象的桌面 agent）",
        url="https://github.com/Playa-Cyrene/Cyrene-Agent",
        lang="TypeScript", stars="697",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="开源桌面 AI 智能体，基于「昔涟」形象 —— 属于「带虚拟形象的桌面 agent」这条线。",
        analogy="和上一条同属一个赛道，但侧重不同：my-neuro 重「伴侣感」，这条重「agent 本体」。"
                "两条并排看，能看出这个赛道实际上在分叉。",
        warn="⚠️ 形象资产涉及**角色版权**（二次元角色图），自用与商用要分开看。",
        ext=(75, "7.5/10", "MIT，代码结构可参考"),
        use=(65, "6.5/10", "桌宠线可当第二个对照"),
        src="推送 2026-10-09 · 697★ · MIT · TypeScript · 信源 [1269]",
    ),
    dict(
        nid="rpm36c14", name="AgentPet（Electron 桌面助手 + Live2D 外观 + ACP 多 agent 调度）",
        url="https://github.com/cqzaaa/AgentPet",
        lang="TypeScript", stars="262",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-warn", "无许可")],
        plain="Electron + React 的桌面 AI 助手：**Live2D 动态外观** + 自主决策 Agent 引擎，"
              "支持 SSH 远程、Computer Use、工具箱与 MCP，并基于 **ACP** 支持多 Agent 本地 / 远程调度。",
        analogy="功能面对「agent 桌宠」这条线来说是最全的之一 —— 既管形象又管 agent 调度，"
                "而且用的是 ACP 这种协议化的接法。",
        warn="⚠️ **无许可证** → 只读参考；⚠️ Computer Use / SSH 远程意味着**权限面很大**，"
             "真要装必须先读代码（房规：第三方插件先人审）。",
        ext=(75, "7.5/10", "ACP + MCP 双协议，编排接口齐"),
        use=(50, "5.0/10", "无许可 + 高权限 → 不装主力，只作参考"),
        src="推送 2026-10-10 · 262★ · 无许可证 · TypeScript · 信源 [1270]",
    ),
    dict(
        nid="rpm36c15", name="Eridanus（bot 框架，含「不接 QQ 的纯 Live2D 桌宠模式」）",
        url="https://github.com/AOrbitron/Eridanus",
        lang="Python", stars="206",
        tags=[("t-make", "建模"), ("t-warn", "许可不明")],
        plain="基于 OneBot 协议的多功能 bot 兼开发框架，以 **LLM function calling** 为核心；"
              "支持「**不接 QQ 的纯 Live2D 桌宠模式**」。",
        analogy="「桌宠」通常要绑一个聊天平台才能有交互，这条反过来 —— "
                "**把平台那层剥掉，只留形象**。对只想摆个桌宠、不想接任何 IM 的人反而干净。",
        warn="⚠️ 许可证是 **NOASSERTION**（GitHub 识别不出，等于没声明）→ 只读。",
        ext=(65, "6.5/10", "以 function calling 为核心，容易换自家模型"),
        use=(55, "5.5/10", "许可证不明，登记但**不推荐**"),
        src="推送 2026-10-10 · 206★ · 许可证不明 · Python · 信源 [1271]",
    ),
    dict(
        nid="rpm36c16", name="JPet（C++ 原生 Live2D 桌宠，2020 年维护至今）",
        url="https://github.com/Xinrea/JPet",
        lang="C++", stars="105",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="C++ 实现的 Live2D 桌面宠物，2020 年建仓、**一路维护到本月**。",
        analogy="前面那些桌宠全是 Electron / Python / TS —— **启动就吃几百 MB**。"
                "这条是原生 C++，在 16GB 机器上，「**低占用**」这个维度目前只有它值得看。",
        warn="⚠️ 原生 C++ 意味着**改起来门槛高**；⚠️ 它用的 Live2D 渲染栈版本要自己核 —— "
             "前几辑反复撞的 Cubism Core ABI 坑就在这里。",
        ext=(60, "6.0/10", "老项目，扩展要动 C++，边际收益递减"),
        use=(70, "7.0/10", "Windows + 低占用，与你的硬件硬约束最合"),
        src="推送 2026-10-09 · 105★ · MIT · C++ · 信源 [1272]",
    ),
    dict(
        nid="rpm36c17", name="D_sakiko（Live2D + AI Agent + GPT-SoVITS 的数字角色）",
        url="https://github.com/MacchaPafe/D_sakiko",
        lang="Python", stars="96",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="把 **Live2D 形象 + AI Agent + GPT-SoVITS 声音克隆**组合起来的桌面 AI 数字角色。",
        analogy="形象 + 对话 + 声音，这三件事前面几条都各做了一部分；"
                "这条的价值是**把「声音克隆」也接进来了** —— 本地音色一致性是桌宠体验里最后一块拼图。",
        warn="⚠️ **GPL-3.0**（分发注意）；⚠️ GPT-SoVITS 要另下模型、另吃算力，16GB 上要算清楚。",
        ext=(70, "7.0/10", "三条链路都开源，可单独拆用"),
        use=(60, "6.0/10", "语音链路的参考 · 整包跑起来偏重"),
        src="推送 2026-10-08 · 96★ · GPL-3.0 · Python · 信源 [1273]",
    ),
    dict(
        nid="rpm36c18", name="vtubeleaf（Tauri + MediaPipe 的本地面捕形象）",
        url="https://github.com/moonrailgun/vtubeleaf",
        lang="TypeScript", stars="13",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="用于**会议场景**的本地 Live2D 虚拟形象**面部捕捉 / 跟踪**，技术栈 Tauri + MediaPipe。",
        analogy="「开会不想露脸、又想有个形象」这个需求很小众但真实；"
                "Tauri 栈体积小，比 Electron 方案轻得多，是 16GB 机器上更现实的选择。",
        warn="⚠️ **13★** 早期项目，功能面还薄。",
        ext=(65, "6.5/10", "Tauri 栈易二次开发"),
        use=(55, "5.5/10", "面捕场景的轻量选项 · 需自验"),
        src="推送 2026-10-10 · 13★ · MIT · TypeScript · 信源 [1274]",
    ),
    dict(
        nid="rpm36c19", name="awesome-ai-companion（AI 伴侣 / 桌宠项目大全）",
        url="https://github.com/DasterProkio/awesome-ai-companion",
        lang="HTML", stars="914",
        tags=[("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="AI 伴侣 / 桌宠 / 长期记忆 / 主动对话方向的 **awesome 清单**。",
        analogy="**它不是代码，是清单** —— 但正因如此，可以直接当下几轮的**选题地图**用："
                "本辑桌宠这一簇能找到这么多条，一半靠的就是这类目录。",
        warn="⚠️ 清单类项目**天然带时效**，条目里的星数与活跃度要自己复核，"
             "**别直接采信清单里的描述**（房规：先核实再下结论）。",
        ext=(70, "7.0/10", "CC0-1.0，可自由摘编作为选题源"),
        use=(65, "6.5/10", "下几轮调研的入口，省一轮搜索"),
        src="推送 2026-10-10 · 914★ · CC0-1.0 · HTML · 信源 [1275]",
    ),
    dict(
        nid="rpm36c20", name="gd_cubism（Godot 的 Cubism 集成，带批渲染与屏幕空间遮罩图集）",
        url="https://github.com/pakholeung37/gd_cubism",
        lang="C++", stars="0",
        tags=[("t-make", "建模"), ("t-warn", "0★")],
        plain="Godot 的 **Cubism 集成**，带批渲染与屏幕空间遮罩图集。",
        analogy="Godot + Cubism 正是「在游戏引擎里用 Live2D」最缺的一块 —— 之前这条路只有 "
                "`MizunagiKB/gd_cubism`（已在库）。这是**新的第二个**实现。",
        warn="⚠️ **0★、许可证不明、建仓不足一个月** → 仅 README 级核实，**不要当依赖**；"
             "⚠️ 而且它没说吃哪一版 Cubism Core —— 这正是前几辑判定「能不能用」的关键数字。",
        ext=(50, "5.0/10", "Godot 侧空白位，值得盯后续"),
        use=(35, "3.5/10", "仅登记，需实测后才能谈可用"),
        src="推送 2026-09-16 · 0★ · 许可证不明 · C++ · 信源 [1276]",
    ),
    dict(
        nid="rpm36c21", name="kokoro（面向工程师的 2D 角色网格变形库）",
        url="https://github.com/marukun712/kokoro",
        lang="TypeScript", stars="42",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="提供 **2D 角色网格（mesh）变形**能力的库，可当作立绘驱动 / 变形的底层组件。",
        analogy="前面那些都是「完整应用」，这条是**地基** —— 想让立绘按参数扭动，"
                "底层就是把网格顶点搬来搬去这一件事。它只做这一件事，所以容易嵌。",
        warn="⚠️ 42★，纯库、无成品界面；文档薄，需要自己读源码。",
        ext=(75, "7.5/10", "MIT + 纯库形态，最容易嵌进自研渲染"),
        use=(55, "5.5/10", "自建桌宠 / 看板娘时的渲染底座候选"),
        src="推送 2026-10-06 · 42★ · MIT · TypeScript · 信源 [1277]",
    ),
    dict(
        nid="rpm36c22", name="A.R.I.A（跨平台 Avatar Studio：Live2D / PNG / VRM 统一输出）",
        url="https://github.com/NekoUnix/A.R.I.A",
        lang="Rust", stars="10",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="Rust 写的跨平台 Avatar Studio（**Alpha**）：支持 Live2D、PNG/GIF、VRM 及实验性 GLB，"
              "共享跟踪、弹性骨骼、灯光、可视化动作与**多形象 OBS 输出**。",
        analogy="它的野心是「一个工作室管所有形象格式」—— 这对直播场景很实用"
                "（一场直播里同时挂 Live2D 和 VRM 两种形象）。"
                "这个方向目前没有成熟品，所以哪怕 10★ 也值得记一笔。",
        warn="⚠️ **Alpha**；Rust 栈，改起来门槛高。",
        ext=(65, "6.5/10", "多格式统一抽象，接口若稳则可复用"),
        use=(45, "4.5/10", "方向值得盯，现在还不能用"),
        src="推送 2026-10-05 · 10★ · MIT · Rust · 信源 [1278]",
    ),
]

FOOTNOTES = [
    (1257, "https://github.com/Inochi2D/inochi2d", "Inochi2D/inochi2d",
     "1811★ · BSD-2-Clause · D · 推送 2026-10-03 · GitHub REST API 实测"),
    (1258, "https://github.com/nijigenerate/nijigenerate", "nijigenerate/nijigenerate",
     "314★ · BSD-2-Clause · D · 推送 2026-10-10 · GitHub REST API 实测"),
    (1259, "https://github.com/shinshin86/mesh-avatar-studio", "shinshin86/mesh-avatar-studio",
     "597★ · MIT · TypeScript · 创建 2026-10-04 · GitHub REST API 实测"),
    (1260, "https://github.com/CheshireMew/PuppetLoom", "CheshireMew/PuppetLoom",
     "245★ · AGPL-3.0 · TypeScript · 推送 2026-10-05 · GitHub REST API 实测"),
    (1261, "https://github.com/zeikar/iki", "zeikar/iki",
     "15★ · MIT · TypeScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1262, "https://github.com/codewayco/Inkinesis", "codewayco/Inkinesis",
     "6★ · Apache-2.0 · TypeScript · 推送 2026-10-05 · GitHub REST API 实测"),
    (1263, "https://github.com/sayaka-aiart/cubism-api-bridge", "sayaka-aiart/cubism-api-bridge",
     "11★ · MIT · TypeScript · 推送 2026-09-12 · GitHub REST API 实测"),
    (1264, "https://github.com/mw2wbyys6t-sudo/live2d-auto-pipeline", "mw2wbyys6t-sudo/live2d-auto-pipeline",
     "10★ · Apache-2.0 · Python · 推送 2026-10-10 · GitHub REST API 实测"),
    (1265, "https://github.com/J621111/live2d-automation", "J621111/live2d-automation",
     "77★ · 无许可证 · Python · 推送 2026-09-27 · GitHub REST API 实测"),
    (1266, "https://github.com/Jelosus2/BD2-L2D-Viewer", "Jelosus2/BD2-L2D-Viewer",
     "540★ · MIT · Vue · 推送 2026-10-08 · GitHub REST API 实测"),
    (1267, "https://github.com/StudioRaming/warudo-agent-bridge", "StudioRaming/warudo-agent-bridge",
     "9★ · MIT · C# · 推送 2026-10-10 · GitHub REST API 实测"),
    (1268, "https://github.com/morettt/my-neuro", "morettt/my-neuro",
     "1389★ · MIT · JavaScript · 推送 2026-10-05 · GitHub REST API 实测"),
    (1269, "https://github.com/Playa-Cyrene/Cyrene-Agent", "Playa-Cyrene/Cyrene-Agent",
     "697★ · MIT · TypeScript · 推送 2026-10-09 · GitHub REST API 实测"),
    (1270, "https://github.com/cqzaaa/AgentPet", "cqzaaa/AgentPet",
     "262★ · 无许可证 · TypeScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1271, "https://github.com/AOrbitron/Eridanus", "AOrbitron/Eridanus",
     "206★ · 许可证不明（NOASSERTION）· Python · 推送 2026-10-10 · GitHub REST API 实测"),
    (1272, "https://github.com/Xinrea/JPet", "Xinrea/JPet",
     "105★ · MIT · C++ · 推送 2026-10-09 · GitHub REST API 实测"),
    (1273, "https://github.com/MacchaPafe/D_sakiko", "MacchaPafe/D_sakiko",
     "96★ · GPL-3.0 · Python · 推送 2026-10-08 · GitHub REST API 实测"),
    (1274, "https://github.com/moonrailgun/vtubeleaf", "moonrailgun/vtubeleaf",
     "13★ · MIT · TypeScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1275, "https://github.com/DasterProkio/awesome-ai-companion", "DasterProkio/awesome-ai-companion",
     "914★ · CC0-1.0 · HTML · 推送 2026-10-10 · GitHub REST API 实测"),
    (1276, "https://github.com/pakholeung37/gd_cubism", "pakholeung37/gd_cubism",
     "0★ · 许可证不明 · C++ · 推送 2026-09-16 · GitHub REST API 实测"),
    (1277, "https://github.com/marukun712/kokoro", "marukun712/kokoro",
     "42★ · MIT · TypeScript · 推送 2026-10-06 · GitHub REST API 实测"),
    (1278, "https://github.com/NekoUnix/A.R.I.A", "NekoUnix/A.R.I.A",
     "10★ · MIT · Rust · 推送 2026-10-05 · GitHub REST API 实测"),
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

    desc = ('第三十一辑三路调研（gh 路 37 条 / cn 路 8 条 / official 路 29 条），本版取 22 项，'
            '主题 **不买 Cubism Editor 的那条路，第一次有了完整栈**。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/&lt;r&gt;` 逐条实测。'
            '<strong>本辑主线：① 开源替代从「只有个编辑器」补齐成「SDK 本体 + 绑定界面 + 自动化 CLI」'
            '（Inochi2D/inochi2d ★1811 的 SDK 本体此前一直漏收 + nijigenerate ★314 + PuppetLoom ★245）；'
            '②「单图/PSD → 可用模型」这条线开始分叉 —— 一条只在网格层动手、天然绕开 Cubism Core ABI 的墙'
            '（mesh-avatar-studio ★597 / kokoro ★42），另一条直接对 moc3 但导出的是 mock（live2d-automation，无许可）；'
            '③ 官方两处口径冲突被定位（学生优惠的「76% vs 80%」是同一张英文首页新旧文案没统一，权威值 80%；'
            'LEAP 覆盖校数首页 200+ vs 专页 450+），且上一辑「SDK 全线 5-r.5」应修正为「分线各自版本」'
            '（Unreal R1 beta2 = 2026-09-29 为最新一次更新）；'
            '④ 一个必读的破坏性变更：live2d-py 升 1.0.0（2026-09-30），移除 live2d.v3 / live2d.v2cpp</strong>。')

    block = ['    <div class="group" data-page-node-id="rpm36g">',
             '      <div class="group-title" data-page-node-id="rpm36gt">🆕 第三十六版增补 · 不买 Cubism Editor 的那条路，第一次有了完整栈：SDK 本体 + 绑定界面 + 自动化 CLI（22 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm36gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm36r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm36ra%s">%s</a> — %s</div>'
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
