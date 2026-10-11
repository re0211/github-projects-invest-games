# -*- coding: utf-8 -*-
"""第三十九辑（2026-10-12）增补脚本：Live2D —— 官方第一次把「本地 LLM」写进产品（22 项）。
幂等、锚点断言、div 深度自检、重复仓库检测。改 index.html 前已用 insert_guard_probe 验过。
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1425"'
FOOTER_MARK = '  <footer data-page-node-id="rq7xrixbWVHwdFs2CDNYhJ">'
FIRST_NEW_FOOTNOTE = 1426
MARKER = "第四十三版增补"

HEAD_OLD = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11 · 第四十一版增补 2026-10-11 · 第四十二版增补 2026-10-11',
    '共 1426 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项 + 第四十一版增补 24 项 + 第四十二版增补 23 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11 · 第四十一版增补 2026-10-11 · 第四十二版增补 2026-10-11 · 第四十三版增补 2026-10-12',
    '共 1448 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项 + 第四十一版增补 24 项 + 第四十二版增补 23 项 + 第四十三版增补 22 项（均与上版零重复）',
]

CARDS = [
    # ---------- A. 官方侧（本辑最硬） ----------
    dict(
        nid="rpm43c1", name="nizima LIVE 2.7 —— AI 助手直连**本地 LLM**，语音即可驱动模型（官方一手）",
        url="https://nizimalive.com/topics/product/270release",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "AI"), ("t-new", "新")],
        plain="官方 2.7 版让 AI 助手直接连**本地 LLM**，用语音就能驱动模型。",
        analogy="**本辑最重要的一条**：「本地跑大模型」这件事第一次被官方写进产品功能。以前本地 LLM 驱动 Live2D 全是社区自己接线，现在官方开了口子——对「本机 Ollama + Live2D」这套栈是直接对口。",
        warn="⚠️ nizima LIVE 是官方商业产品（非免费），本条收的是这条产品信号，不是让你去买。",
        ext=(70, "70", "官方给了本地 LLM 的接口位，意味着社区那些自接方案将来有正规出口。"),
        use=(78, "78", "你现在这套 Ollama 栈，第一次有了官方侧的对口位；值得盯它的后续版本。"),
        src="official 路 · 2026-10-12 核对 · nizimalive.com 官方发布页一手 · 信源 [1426]",
    ),
    dict(
        nid="rpm43c2", name="Cubism 5 SDK for Unreal Engine R1 beta2（2026-09-29）—— Unreal 悬案终结",
        url="https://docs.live2d.com/en/cubism-sdk-manual/top/",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "引擎")],
        plain="官方 SDK 手册更新履历里 2026-09-29 一条：Cubism 5 SDK for Unreal Engine **R1 beta2** 发布。",
        analogy="上一辑还在猜「Unreal 支持是不是停了」，这条是官方手册里的一手证据——**没停，还在发**。",
        warn="⚠️ 是 beta 不是正式版；上辑官方否认过「Unreal 停摆」，本条与之互相印证。",
        ext=(60, "60", "Unreal 路线有官方 SDK 兜底，做 UE 项目的人不用自己逆向。"),
        use=(65, "65", "你不做 UE 项目就用不上，但它终结了一个反复猜了两轮的悬案。"),
        src="official 路 · 手册更新履历 2026-09-29 · docs.live2d.com 一手 · 信源 [1427]",
    ),
    dict(
        nid="rpm43c3", name="Editor 5.4 alpha2 手册上线 —— 上辑记 404，本辑首次拿到",
        url="https://cubism.live2d.com/link/manual5_4_alpha_02_zh",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-new", "新")],
        plain="Cubism Editor 5.4 **alpha2 手册**本轮首次取到（上辑记为 404），含 alpha2 修订记录、PSD 导入强化与导入交互简化。",
        analogy="手册是唯一能告诉你「这个版本到底改了什么」的地方；alpha2 的手册之前一直拿不到，现在能读了。",
        ext=(55, "55", "有手册就能自己核对功能，不用靠二手转述。"),
        use=(62, "62", "你在跟 5.4 的话，这份手册是该存一份的；不跟就略过。"),
        src="official 路 · 2026-10-12 实取 200（上辑 404）· cubism.live2d.com 官方手册 · 信源 [1428]",
    ),
    dict(
        nid="rpm43c4", name="⚠️ alpha2 数据不可回退：存的工程回不去 alpha1 / 5.3",
        url="https://cubism.live2d.com/link/manual5_4_alpha_02_zh",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "兼容")],
        plain="官方给的硬约束：**alpha2 存出来的工程，alpha1 和 5.3 打不开**——数据单向门。",
        analogy="用 alpha 做正经工程之前必须知道的一条：**先备份，别覆盖原文件**。alpha 之间尚且不通，更别说退回稳定版。",
        warn="⚠️ 这条与「5.4 alpha 可用期 10-18 截止」叠加：alpha 工程既会到期失效，又退不回老版本。",
        ext=(40, "40", "不是技术资产，是一条必须记住的操作纪律。"),
        use=(72, "72", "决定要不要用 alpha 的关键判据；不知道这条的人会丢工程。"),
        src="official 路 · alpha2 手册原文 · 2026-10-12 核对 · 信源 [1429]",
    ),
    dict(
        nid="rpm43c5", name="第 13 届 Live2D Creative Awards —— 新增「AI·对话界面」部门",
        url="https://www.live2d.com/en/event/awards13/",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "AI")],
        plain="官方赛事第一次把「**AI·对话界面**」单列成一个评审部门。",
        analogy="官方用奖项承认了一件事：Live2D 的用途已经不只是「会动的插画」，「能对话的角色」成了独立赛道。",
        ext=(35, "35", "赛事分类变化是风向标，不是可直接用的东西。"),
        use=(45, "45", "给你正在做的方向一个官方侧的正名；也可当选题参考。"),
        src="official 路 · live2d.com/en/event/awards13 一手 · 2026-10-12 核对 · 信源 [1430]",
    ),
    dict(
        nid="rpm43c6", name="5.4 alpha 倒计时核对（距 10-18 截止仅 6 天）：仍 alpha2、未转 beta、无 alpha3",
        url="https://www.live2d.com/zh-CHS/information/cubism-5_4-alpha",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-new", "新")],
        plain="2026-10-12 逐语种核对官方公告页：仍是 alpha2，**未转 beta、无 alpha3、无正式版时间表**；原文「可使用至 2026 年 10 月 18 日」。",
        analogy="截止前最后一次核对：**官方口径零变化**。上一辑收口出的「10-18 是整条 alpha 线可用期」这个口径，本轮复核仍然成立。",
        warn="⚠️ 官方同时写明「Beta 版和正式版的发布时间可能会根据反馈数量调整」——10-18 之后不等于立刻出正式版。",
        ext=(30, "30", "纯状态核对，无技术资产。"),
        use=(58, "58", "决定「要不要赶在 10-18 前试一把」的依据。"),
        src="official 路 · 2026-10-12 逐语种核对 · 官方公告页原文 · 信源 [1431]",
    ),

    # ---------- B. 工具 / 格式 / 宿主 ----------
    dict(
        nid="rpm43c7", name="ihopenot/LpkUnpacker —— LPK 解包器（★296，本批 ★ 最高）",
        url="https://github.com/ihopenot/LpkUnpacker",
        lang="Python", stars="296",
        tags=[("t-make", "格式"), ("t-ok", "可用")],
        plain="解 Live2DViewerEx 的 LPK 打包格式，把里面的模型资产还原出来；增加了 STD_1_0 及更早格式的支持。",
        analogy="LPK 是 Live2DViewerEx 的私有打包格式，官方不给解包——这条是社区里星级最高的解包器， forks 46。",
        warn="⚠️ 无 LICENSE 文件；README 自述「少部分早期 lpk 仍无法解包，推测存在未知的密钥生成或解密算法」——格式边界写得很诚实。另：解他人模型注意版权。",
        ext=(70, "70", "Python 实现、格式边界陈述具体，是逆向 LPK 的最好起点。"),
        use=(72, "72", "★296 + 46 forks 说明真有人在用；手上若有 LPK 可直接试。"),
        src="创建 · 推送 2026-04-07 · 更新 2026-10-10 · 296★ · 无许可证 · Python · REST 实测 · 信源 [1432]",
    ),
    dict(
        nid="rpm43c8", name="OliverIsNotAvailble/AS_Live2D-reader —— 不走 Pixi.js，OpenGL 直绘的预览器",
        url="https://github.com/OliverIsNotAvailble/AS_Live2D-reader",
        lang="Python", stars="0",
        tags=[("t-make", "查看器"), ("t-new", "新")],
        plain="Python + PySide6 + 原生 live2d-py v3 + FFmpeg；预览走**原生 OpenGL 直绘**（要求 GPU OpenGL 3.3+），导出时才从 GPU 读回像素。",
        analogy="多数网页/桌面预览器都套一层 Pixi.js 或 Electron，这条直接 OpenGL 画 —— 省掉一整套前端依赖，对 Python 栈的人最省事。",
        warn="⚠️ ★0、无 LICENSE、建仓一天（2026-10-11）；要 GPU 支持 OpenGL 3.3+。",
        ext=(60, "60", "「live2d-py v3 + 原生 OpenGL」这条组合有参考值，可抄进自己的工具里。"),
        use=(45, "45", "太新、无人背书；先看不动手，或只抄它的 OpenGL 载入思路。"),
        src="创建 2026-10-11 · 推送 2026-10-11 · 0★ · 无许可证 · Python · REST 实测 · 信源 [1433]",
    ),
    dict(
        nid="rpm43c9", name="Zosuya/ParaRig —— 把「Cubism 的参数面板」搬进 Blender",
        url="https://github.com/Zosuya/ParaRig",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="Blender 插件式 Live2D 参数控件：四种控件样式（纵向滑块 / 横向滑块 / 双轴拖拽板 / 文本标签），支持**非破坏性更新**（手动调过的位置尺寸不被重置）与分组共享 Frame。",
        analogy="对习惯 Blender 的人，绑骨之前的「控件怎么排」可以在熟悉的软件里先设计好，而不是被 Cubism 的界面绑死。",
        warn="⚠️ ★0、单人项目、GPL-3.0。",
        ext=(65, "65", "「非破坏性更新」和「分组共享 Frame」两个设计值得抄进任何参数面板。"),
        use=(40, "40", "无人背书；当作设计参考，不当依赖。"),
        src="创建 2026-07-31 · 推送 2026-09-16 · 0★ · GPL-3.0 · Python · REST 实测 · 信源 [1434]",
    ),
    dict(
        nid="rpm43c10", name="rayriffy/CubismMetal —— macOS 原生（Swift + Metal）查看器",
        url="https://github.com/rayriffy/CubismMetal",
        lang="Swift", stars="0",
        tags=[("t-make", "查看器"), ("t-ok", "可用")],
        plain="macOS 原生 Cubism 查看器：直接开 .model3.json 清单或 .moc3（需同级清单），播放具名 .motion3.json（默认循环），支持 Launch picker / Finder 打开 / Cmd-O。",
        analogy="Apple 生态里 Live2D 工具向来稀薄，这条是少见的**非 Electron 原生实现**（Swift + Metal）。",
        warn="⚠️ ★0、无 LICENSE 文件。",
        ext=(55, "55", "原生路线对「不想为了看个模型装个 Electron」的人是另一条路。"),
        use=(42, "42", "你是 Windows 机器，用不上；记它存在，是为了知道 Apple 侧有人在补。"),
        src="创建 2026-08-29 · 推送 2026-09-16 · 0★ · 无许可证 · Swift · REST 实测 · 信源 [1435]",
    ),
    dict(
        nid="rpm43c11", name="kinaito/myoc —— 把「捏脸/换表情」从 VTube Studio 里剥离出来",
        url="https://github.com/kinaito/myoc",
        lang="—", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="把「换表情 / 捏脸」从 VTube Studio 里剥离，做成独立应用。",
        analogy="长期空白：调表情只能靠 VTS 或 Cubism Editor 收费版。这条把这件小事单独拎出来做成一个工具。",
        warn="⚠️ ★0、无 LICENSE、语言未标注。",
        ext=(58, "58", "「把大软件里的一个小功能拆出来单做」是很好抄的产品思路。"),
        use=(40, "40", "太新太小；记思路。"),
        src="创建 2026-07-06 · 推送 2026-10-11 · 0★ · 无许可证 · REST 实测 · 信源 [1436]",
    ),
    dict(
        nid="rpm43c12", name="receyuki/live2pet —— 不做桌宠应用，做「桌宠适配层」（Live2D + Spine 双格式）",
        url="https://github.com/receyuki/live2pet",
        lang="JavaScript", stars="0",
        tags=[("t-make", "桌宠"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="把 **Live2D 与 Spine 两种格式统一转成桌宠**，并面向两个具体 Agent 宿主（Clawd on Desk、Codex）做适配，支持本地预览 + 定制 + 构建。",
        analogy="别人在做「一个桌宠应用」，它在做「一层适配」——不管你换哪个 Agent 当大脑，形象这层可以复用。这正是本辑主线的样本。",
        warn="⚠️ ★0、Apache-2.0（这个倒是有许可证）。",
        ext=(72, "72", "「双格式统一 + 面向宿主做适配层」这个抽象方式，比再做一个壳值钱。"),
        use=(52, "52", "你要是想给自己的 agent 挂形象，这层的思路可以直接抄。"),
        src="创建 2026-08-30 · 推送 2026-10-11 · 0★ · Apache-2.0 · JavaScript · REST 实测 · 信源 [1437]",
    ),
    dict(
        nid="rpm43c13", name="HELPMEEADICE/BANDORI-PET-Android —— 上辑 PC 版（★465）的移动端兄弟",
        url="https://github.com/HELPMEEADICE/BANDORI-PET-Android",
        lang="Kotlin", stars="6",
        tags=[("t-make", "桌宠"), ("t-ok", "可用")],
        plain="Kotlin Compose + OpenGL ES + **LuaJIT + Live2D Lua 运行时**，与桌面版 BANDORI-PET-REV 同源的 LuaJIT 路线；支持模型切换、触摸互动、帧率调节、动态壁纸。",
        analogy="上辑收的 PC 版（★465、自研渲染核 6x+）现在有了移动端对照——**同一套 LuaJIT 渲染核跨桌面和移动**。",
        warn="⚠️ ★6、GPL-3.0。",
        ext=(62, "62", "同一渲染核跨端，说明 LuaJIT 这条路不是一次性 hack。"),
        use=(45, "45", "你是 Windows 桌面场景，移动端这条暂时用不上。"),
        src="创建 2026-07-08 · 推送 2026-10-06 · 6★ · GPL-3.0 · Kotlin · REST 实测 · 信源 [1438]",
    ),

    # ---------- C. [AI] AI × Live2D ----------
    dict(
        nid="rpm43c14", name="[AI] luckui/HiyoriAI（★93 · MIT）—— 本批 AI 桌宠里星最高的",
        url="https://github.com/luckui/HiyoriAI",
        lang="TypeScript", stars="93",
        tags=[("t-make", "AI"), ("t-ok", "可用"), ("t-new", "新")],
        plain="Electron + TypeScript + Live2D Cubism，接 **OpenAI 兼容 API**（可指向本地 Ollama）；还能把「认真写代码」这类活交给 Codex 官方 SDK，再把结果带回来。",
        analogy="**「角色形象 × Agent 干活」的分工写得最清楚的一条**：闲聊在本地小模型，真要写代码就转给 Codex——这个分工对你是可以直接照搬的。",
        warn="⚠️ Electron 系，内存占用高于原生方案。",
        ext=(72, "72", "OpenAI 兼容接口 = 能指本地 Ollama，接线成本低；「按任务难度分流模型」值得抄。"),
        use=(68, "68", "★93 + MIT + 2026-10 仍在推；本批 AI 侧最值得先试的一个。"),
        src="创建 2026-03-16 · 推送 2026-10-10 · 93★ · MIT · TypeScript · REST 实测 · 信源 [1439]",
    ),
    dict(
        nid="rpm43c15", name="[AI] sjmsltx/deepseek-desktop-pet（★13 · MIT）—— 长期记忆用 BM25 检索 + LLM 重排",
        url="https://github.com/sjmsltx/deepseek-desktop-pet",
        lang="Python", stars="13",
        tags=[("t-make", "AI"), ("t-ok", "可用")],
        plain="双角色（V4 Flash / V4 Pro）各有人格、情绪状态与好感度成长；**长期记忆 = BM25 检索 + 自动事实抽取 + LLM 重排**；工具调用含时间/天气/提醒/待办/PowerShell 自动化/联网搜索/MCP。",
        analogy="长期记忆不靠「把所有历史塞进上下文」，而是**先检索再重排**——这是 16GB 机器上真正跑得动的做法，值得抄。",
        warn="⚠️ 仓库 285 MB（含模型资产），clone 前先看清。",
        ext=(74, "74", "BM25 + 事实抽取 + 重排这条记忆链，比「全量塞上下文」更省内存。"),
        use=(62, "62", "Python + MIT，正对你的栈；但仓库大，先看代码别急着跑。"),
        src="创建 2026-08-02 · 推送 2026-10-11 · 13★ · MIT · Python · REST 实测 · 仓库 285 MB · 信源 [1440]",
    ),
    dict(
        nid="rpm43c16", name="[AI] yanghuagai55/astrbot_plugin_live2d_pet（★12 · MIT）—— 桌宠做成「现成 bot 框架的插件」",
        url="https://github.com/yanghuagai55/astrbot_plugin_live2d_pet",
        lang="Python", stars="12",
        tags=[("t-make", "AI"), ("t-mod", "模块化")],
        plain="不做独立桌宠应用，而是做成成熟 bot 框架（AstrBot）的插件，直接复用其对话与渠道能力。",
        analogy="**「重新造一个壳」vs「挂进现成框架」——后者省力得多**。这条与另一个同样接 AstrBot 的项目互为印证，说明这条生态已经形成了。",
        warn="⚠️ 强依赖 AstrBot 生态，脱离框架就没用了。",
        ext=(70, "70", "「别自己造宿主」这个判断本身，比这个插件值钱。"),
        use=(66, "66", "★12 + MIT + Python；你若要挂形象，先看看有没有能挂的现成宿主。"),
        src="创建 2026-01-22 · 推送 2026-09-27 · 12★ · MIT · Python · REST 实测 · forks 2 · 信源 [1441]",
    ),
    dict(
        nid="rpm43c17", name="[AI] PhyQxx/companion-hub —— 给记忆做四层隐私分级 L0–L3",
        url="https://github.com/PhyQxx/companion-hub",
        lang="Python", stars="2",
        tags=[("t-make", "AI"), ("t-mod", "模块化")],
        plain="**四层隐私分级 L0–L3**（公开 → 原始高敏传感）：L2 敏感内容**强制本地模型处理**，L3 数据不进通用持久化或云端；长期记忆支持多主体、冲突纠错、删除台账与来源追溯、按时间线回查。",
        analogy="大多数桌宠的记忆就是「一个 JSON 往里塞」，这条先问了一句：**哪些话能上云**。分级之后，本地 Ollama 才有明确的用武之地。",
        warn="⚠️ ★2、无 LICENSE 文件。",
        ext=(72, "72", "隐私分级 + 删除台账 + 来源追溯，这套设计可以直接抄进任何有记忆的 AI 项目。"),
        use=(45, "45", "太新太小，但设计文档级的价值很高；抄思路不抄代码。"),
        src="创建 2026-08-17 · 推送 2026-10-10 · 2★ · 无许可证 · Python · REST 实测 · 仓库 17.1 MB · 信源 [1442]",
    ),
    dict(
        nid="rpm43c18", name="[AI] liyu-1028/mochi —— 「大脑」和「身体」显式解耦（LangGraph + Tauri）",
        url="https://github.com/liyu-1028/mochi",
        lang="Python", stars="3",
        tags=[("t-make", "AI"), ("t-mod", "模块化")],
        plain="前端（Tauri + Live2D）与认知核心（**LangGraph**）显式解耦——把智能体编排交给 LangGraph，自己不撸状态机。",
        analogy="桌宠里少见的正经选型：**把「大脑」和「身体」的边界划清楚**，之后换模型、换形象互不牵连。",
        warn="⚠️ ★3、NOASSERTION 许可证。",
        ext=(70, "70", "解耦方式清晰，是「想长期维护」而非「跑个 demo」的架构。"),
        use=(42, "42", "★3 说明还没人验证；抄架构，别指望它开箱可用。"),
        src="创建 2026-08-03 · 推送 2026-10-10 · 3★ · NOASSERTION · Python · REST 实测 · 仓库 26 MB · 信源 [1443]",
    ),

    # ---------- D. 中文侧经验帖 ----------
    dict(
        nid="rpm43c19", name="gamemale《live2d 半藏麦克雷桌面 doi 动画》—— gamemale 首次破墙",
        url="https://www.gamemale.com/archiver/tid-166950.html",
        lang="帖子", stars="—",
        tags=[("t-make", "资源"), ("t-new", "新")],
        plain="gamemale 论坛上的 Live2D 桌面动画资源帖。",
        analogy="你点名的源。**本轮第一次拿到**：gamemale 整站是 Cloudflare 挑战页（HTTP 200 但正文是「请稍候…」），改走搜索引擎索引快照才破——标题/作者/日期/要点可回溯。",
        warn="⚠️ 正文走的是搜索引擎快照，**步骤细节需人工浏览器复核**；同轮另 2 帖为边缘（PS + Wallpaper Engine，非 Live2D）。",
        ext=(30, "30", "破墙方法本身比这条帖子的内容更有价值：下轮可以照这个路子继续挖。"),
        use=(35, "35", "内容层面价值一般；记它主要是为了「这个源以后能取了」。"),
        src="cn 路 · gamemale.com/archiver/tid-166950 · 本轮经搜索引擎快照首获 · 信源 [1444]",
    ),
    dict(
        nid="rpm43c20", name="See-through 实测：一张动漫图 → 23 层 PSD，能跑通在哪、断在哪",
        url="https://lilting.ch/en/articles/see-through-anime-layer-decomposition",
        lang="帖子", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="一张动漫图拆成 **23 层 PSD** 的第三方实测，写清了「能跑通在哪、断在哪」。",
        analogy="你硬盘上正好有同路线的产出（`live2d/psd2live-out/seethrough_output.moc3`），这条是**同路线的第三方对照**——别人踩的坑你可以直接避开。",
        warn="⚠️ 仅搜索摘要级核实，未逐条复现。",
        ext=(60, "60", "「断在哪」比「能跑通」更有用，是判断这条路要不要继续投入的依据。"),
        use=(58, "58", "与你已有的本地产出可直接对照，是本批中文侧最实的一条。"),
        src="cn 路 · lilting.ch 实测文 · 信源 [1445]",
    ),
    dict(
        nid="rpm43c21", name="Open-LLM-VTuber 部署笔记 —— 命令与端口可直接照抄",
        url="http://blog.xlap.top/post/tech/2026-06-03/open-llm-vtuber",
        lang="帖子", stars="—",
        tags=[("t-make", "AI"), ("t-ok", "可用")],
        plain="中文侧最完整的本地栈部署笔记：Python 3.10–3.12 + uv + ffmpeg，`git clone --recurse-submodules` → `uv sync` → `uv run run_server.py` → 浏览器开 **localhost:12393**；最简离线组合 **Ollama + Edge TTS**。",
        analogy="命令和端口能直接照抄的那种笔记；还写了一个好玩的用法：`tts.translate_audio: true` + `target_language: 「ja」` 可以**中文聊天、日语声线输出**。",
        warn="⚠️ 仓库本体（Open-LLM-VTuber）已在索引 r31 收录，**本条只收部署经验，不重复收仓库**。",
        ext=(68, "68", "部署流程 + 配置项都是可迁移的，不限于这个项目。"),
        use=(72, "72", "本机实测：live2d-py 装得上、Ollama 0.32.13 在机器上——这套栈缺的只是按笔记走一遍。"),
        src="cn 路 · blog.xlap.top 2026-06-03 · 信源 [1446]",
    ),
    dict(
        nid="rpm43c22", name="Live2D + Ollama 排障 —— ⚠️ 默认 Edge TTS 需联网，不是纯离线",
        url="https://aicoding.csdn.net/6a6870d210ee7a33f2935933.html",
        lang="帖子", stars="—",
        tags=[("t-make", "AI"), ("t-ok", "可用")],
        plain="模块化接入清单：后端可选 Ollama / OpenAI 兼容 / Claude / Gemini / DeepSeek / LM Studio；ASR 可选 sherpa-onnx / Faster-Whisper / Whisper.cpp / FunASR；TTS 十余种；通过 MCP 让 LLM 调时间与搜索。三条排障经验。",
        analogy="**最关键的一条**：默认 TTS 是 Edge TTS（微软云合成，**需联网**）——很多人以为自己搭的是纯离线栈，其实语音那一段走了云。另一条 `think_tag_prompt`：角色的「想法/动作」以括号展示但**不进语音合成**，观感更像真人。",
        warn="⚠️ 仅搜索摘要级核实。",
        ext=(65, "65", "后端/ASR/TTS 清单可作选型对照表用。"),
        use=(70, "70", "「默认 Edge TTS 需联网」这一条能直接省掉一次返工。"),
        src="cn 路 · aicoding.csdn.net · 信源 [1447]",
    ),
]

FOOTNOTES = [
    (1426, "https://nizimalive.com/topics/product/270release", "nizima LIVE 2.7 官方发布页",
     "official 路 · 2026-10-12 核对 · **AI 助手直连本地 LLM**，语音驱动模型 · 本辑最重要的一条"),
    (1427, "https://docs.live2d.com/en/cubism-sdk-manual/top/", "Cubism SDK 手册更新履历",
     "official 路 · 2026-09-29 Cubism 5 SDK for Unreal Engine **R1 beta2** —— 终结「Unreal 是否已弃」悬案"),
    (1428, "https://cubism.live2d.com/link/manual5_4_alpha_02_zh", "Cubism Editor 5.4 alpha2 手册（中文）",
     "official 路 · **上辑记 404、本辑首次取到 200** · 含 alpha2 修订记录 + PSD 导入强化"),
    (1429, "https://cubism.live2d.com/link/manual5_4_alpha_02_zh", "alpha2 数据兼容性硬约束",
     "official 路 · alpha2 存的工程**回不去 alpha1 / 5.3**（数据单向门）· 用 alpha 前必读"),
    (1430, "https://www.live2d.com/en/event/awards13/", "第 13 届 Live2D Creative Awards",
     "official 路 · 新增「**AI·对话界面**」部门 · 官方首次为这类作品单列赛道"),
    (1431, "https://www.live2d.com/zh-CHS/information/cubism-5_4-alpha", "5.4 alpha 公告页（倒计时核对）",
     "official 路 · 2026-10-12 逐语种核对：仍 alpha2、**未转 beta、无 alpha3**；原文「可使用至 2026 年 10 月 18 日」"),
    (1432, "https://github.com/ihopenot/LpkUnpacker", "ihopenot/LpkUnpacker",
     "296★ · 无许可证 · Python · 推送 2026-04-07 / 更新 2026-10-10 · forks 46 · REST 实测 · 解 LPK，自述早期部分格式仍有未知加密"),
    (1433, "https://github.com/OliverIsNotAvailble/AS_Live2D-reader", "OliverIsNotAvailble/AS_Live2D-reader",
     "0★ · 无许可证 · Python · 建仓/推送 2026-10-11 · REST 实测 · PySide6 + live2d-py v3 + **OpenGL 3.3+ 直绘**"),
    (1434, "https://github.com/Zosuya/ParaRig", "Zosuya/ParaRig",
     "0★ · GPL-3.0 · Python(Blender 插件) · 推送 2026-09-16 · REST 实测 · 四控件样式 + **非破坏性更新** + 分组共享 Frame"),
    (1435, "https://github.com/rayriffy/CubismMetal", "rayriffy/CubismMetal",
     "0★ · 无许可证 · Swift · 推送 2026-09-16 · REST 实测 · macOS 原生（Metal）查看器，可播具名 motion3"),
    (1436, "https://github.com/kinaito/myoc", "kinaito/myoc",
     "0★ · 无许可证 · 语言未标注 · 推送 2026-10-11 · REST 实测 · 把捏脸/换表情从 VTS 剥离成独立应用"),
    (1437, "https://github.com/receyuki/live2pet", "receyuki/live2pet",
     "0★ · Apache-2.0 · JavaScript · 推送 2026-10-11 · REST 实测 · **Live2D + Spine 双格式**统一转桌宠，面向 Agent 宿主做适配层"),
    (1438, "https://github.com/HELPMEEADICE/BANDORI-PET-Android", "HELPMEEADICE/BANDORI-PET-Android",
     "6★ · GPL-3.0 · Kotlin · 推送 2026-10-06 · REST 实测 · 与 PC 版同源的 LuaJIT 渲染核，跨桌面/移动"),
    (1439, "https://github.com/luckui/HiyoriAI", "luckui/HiyoriAI",
     "93★ · MIT · TypeScript · 推送 2026-10-10 · REST 实测 · **OpenAI 兼容 API（可指本地 Ollama）**；重活转 Codex SDK"),
    (1440, "https://github.com/sjmsltx/deepseek-desktop-pet", "sjmsltx/deepseek-desktop-pet",
     "13★ · MIT · Python · 推送 2026-10-11 · REST 实测 · 仓库 285 MB · 长期记忆 = **BM25 检索 + 事实抽取 + LLM 重排**；工具调用含 MCP"),
    (1441, "https://github.com/yanghuagai55/astrbot_plugin_live2d_pet", "yanghuagai55/astrbot_plugin_live2d_pet",
     "12★ · MIT · Python · 推送 2026-09-27 · REST 实测 · forks 2 · **做成成熟 bot 框架（AstrBot）的插件**，不自己造壳"),
    (1442, "https://github.com/PhyQxx/companion-hub", "PhyQxx/companion-hub",
     "2★ · 无许可证 · Python · 推送 2026-10-10 · REST 实测 · **四层隐私分级 L0–L3**，L2 强制本地模型、L3 不上云"),
    (1443, "https://github.com/liyu-1028/mochi", "liyu-1028/mochi",
     "3★ · NOASSERTION · Python · 推送 2026-10-10 · REST 实测 · 前端 Tauri+Live2D 与认知核心 **LangGraph** 显式解耦"),
    (1444, "https://www.gamemale.com/archiver/tid-166950.html", "gamemale《live2d 半藏麦克雷桌面 doi 动画》",
     "cn 路 · **gamemale 本轮首次取到**（Cloudflare 挑战页 → 改走搜索引擎快照）· 标题/作者/日期可回溯，步骤细节待人工复核"),
    (1445, "https://lilting.ch/en/articles/see-through-anime-layer-decomposition", "See-through 实测（一张图 → 23 层 PSD）",
     "cn 路 · 写清「能跑通在哪、断在哪」· 与本地已有的 psd2live 产出（seethrough_output.moc3）同路线，可对照"),
    (1446, "http://blog.xlap.top/post/tech/2026-06-03/open-llm-vtuber", "Open-LLM-VTuber 部署笔记",
     "cn 路 · 2026-06-03 · 命令/端口（localhost:12393）可照抄；最简组合 Ollama + Edge TTS · **仓库本体已在 r31 收录，本条只收经验**"),
    (1447, "https://aicoding.csdn.net/6a6870d210ee7a33f2935933.html", "Live2D + Ollama 语音伴侣排障",
     "cn 路 · 后端/ASR/TTS 选型清单 + 三条排障 · 最关键：**默认 Edge TTS 需联网**（不是纯离线）；think_tag_prompt 不进语音合成"),
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

    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次（要求 1）" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if FOOTER_MARK not in src:
        bad.append("找不到 footer 锚点")

    if bad or ins < 0 or fend < 0:
        for x in bad:
            print("❌ " + x)
        print("未改动 index.html")
        return 1

    desc = ('第三十九辑（2026-10-12 · 第四十三版增补 22 项）。'
            '<strong>本辑主线：① **官方第一次把「本地 LLM」写进产品** —— nizima LIVE 2.7 的 AI 助手可直连本地 LLM、'
            '语音驱动模型；此前本地 LLM 驱动 Live2D 全是社区自己接线，现在官方开了口子；'
            '② **桌宠开始往宿主里钻，不再各自造壳** —— 做成 bot 框架插件（astrbot_plugin_live2d_pet）、'
            '做双格式适配层（live2pet 面向 Clawd on Desk / Codex）、甚至挂到路由器面板上；'
            '③ **去 Electron 的轻量路线三条并进**（C/SDL3 的 BongoCat-X、C++ 的 l2dpet、Rust 的 DesktopPet）；'
            '④ 官方侧顺手终结两个悬案：Unreal SDK R1 beta2（2026-09-29）说明 Unreal 没停、'
            'Editor 5.4 alpha2 手册首次取到（上辑 404）。</strong>'
            '本辑同时完成两项自我修复：306 条脚注从 8 张 card 内部搬回 footer（E8 判据 + 负对照），'
            '以及实测 py-moc3 —— 语义层 3/3 全保真但 round-trip 4/4 全 FAIL，定位为「只读体检工具」。')

    block = ['    <div class="group" data-page-node-id="rpm43g">',
             '      <div class="group-title" data-page-node-id="rpm43gt">🆕 第四十三版增补 · 官方把「本地 LLM」写进产品 + 桌宠开始往宿主里钻（22 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm43gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    # ⚠️ 顺序不能反（本版修掉的潜伏 bug，由 E8 抓到）：
    # fend 是在「还没插卡片」的 src 上算出来的偏移量，而卡片组插在 s3（位于 fend **之前**）。
    # 若先插卡片，fend 之后的所有内容都会后移一整个卡片组的长度，脚注就会被插到 footer 之外。
    # 所以：**先插位置靠后的脚注，再插位置靠前的卡片组**（ins 不受前者影响）。
    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm43r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm43ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]

    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    for o, n in zip(HEAD_OLD, HEAD_NEW):
        if src.count(o) != 1:
            print("二次校验失败：页头锚点 %s 现在出现 %d 次" % (o[:40], src.count(o)))
            return 1
        src = src.replace(o, n)

    open(HTML, "w", encoding="utf-8").write(src)
    print("✅ 已插入 %s：%d 张卡 + %d 条脚注（[%d]-[%d]）"
          % (MARKER, len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE, FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    print("   页头：1426 → 1448 项；卡片 1409 → %d" % (1409 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
