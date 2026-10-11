# -*- coding: utf-8 -*-
"""第四十版增补：把第三十五辑「AI 拆层→自动绑定流水线成形 + 桌宠宿主换代」的 24 个条目登记进 index.html。

本辑候选：gh 路 49 条（子 agent）+ 22 条（主 agent 直接检索补位）、cn 路 24 条、official 路 5 条。
与 `index.html`（1355 项）及全部历史存档机器比对，本版 24 条命中 **0**。

**本辑主线：上一辑「轮子长出两丛」，这一辑「轮子自己长成了一条流水线」——
「立绘 → AI 拆层 → 自动绑定 → moc3」第一次出现四个独立仓库互相引用的完整链路，且有人把显存实测贴了出来；
同时桌宠「身体」侧的宿主技术栈整体换代（Electron → Tauri / Rust / 原生 OpenGL / 纯浏览器）。**

另：本辑顺带完成了**欠了两轮的待办①** —— 给 1338 张旧卡回填 `pushed_at / updated_at`（1212 处），
格式与 v40 新卡一致；并抓到 22 个**改过 owner/name 的仓库**（链接腐化清单，见 csdn 汇总 §5.2）。

数据来源：2026-10-11 GitHub REST / GraphQL API 逐条实测（★ / license / 语言 / 创建 / 推送 / 更新）。
幂等：已存在本版标记则跳过。v39 已通过 `insert_guard_probe`（P0 语法 + 1 正 5 反）。
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1354"'
FIRST_NEW_FOOTNOTE = 1355
MARKER = "第四十版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十九版增补 2026-10-11',
    '共 1355 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11',
    '共 1379 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项（均与上版零重复）',
]

CARDS = [
    # ---------- A. AI「拆层 → 自动绑定」流水线（本辑最重） ----------
    dict(
        nid="rpm40c1", name="live2d-psd-generator —— 一张正面立绘到分层 PSD，遮挡处用 AI 补（★1）",
        url="https://github.com/bluewakame/live2d-psd-generator",
        lang="Python", stars="1",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="日文项目：**从一张正面立绘生成 Live2D 用的分层 PSD**，**被挡住的部分用 AI 补全**。",
        analogy="前面几条流水线做的是「拆层 + 绑定」的整条链，这一条**只做第一站，但做得更专**：把「补图」这步交给 AI。"
                 "**补图（画出被遮住的眼白、耳后、头发内面）是新手最容易漏、又最容易在转头时崩掉的一步** —— "
                 "拿 AI 攻这一步，是这一类工具里最实在的切入点。",
        warn="⚠️ ★1、文档是**日文**；创建 2026-09-15 后只在 09-21 更新过一次 → 早期实验，**别当依赖**。",
        ext=(65, "6.5/10", "拆层链条的第一站；「AI 补图」这个切入点选得准"),
        use=(50, "5.0/10", "Python + MIT；但★1 且文档为日文，要自己读代码"),
        src="创建 2026-09-15 · 最近更新 2026-09-21（推送 2026-09-15）· 1★ · MIT · Python · 信源 [1355]",
    ),
    dict(
        nid="rpm40c2", name="still2rig-psd —— 静态立绘变成「带 QA 自检」的结构化 PSD（★130）",
        url="https://github.com/shinshin86/still2rig-psd",
        lang="JavaScript", stars="130",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="绑定侧★最高的另一条：**把一张静态二次元立绘变成「结构化、且过了 QA 自检」的 PSD**（分层 + 检查 + 动作预演）。"
              "自述写明它跑在 **Codex + 用户授权的 Google Colab GPU 会话**上。",
        analogy="它比「一句 prompt 出图」靠谱的地方在于**自带 QA 自检**：拆完的层要先过检查，而不是直接喂给绑定。"
                 "**先验后绑**这个顺序，和你维护索引时「改完必跑闸门」是同一个思路。",
        warn="⚠️ 算力在**云端 Colab GPU**（需你自己授权）→ 你的 16GB 机器跑得动流程，但**素材要出本机**，敏感内容要权衡。",
        ext=(75, "7.5/10", "拆层 + QA + 预演三件套；MIT；与 psd2live 正好互补（它管拆，psd2live 管绑）"),
        use=(55, "5.5/10", "MIT + JS，流程可读；但要接 Colab GPU，且★130 说明仍在早期"),
        src="创建 2026-08-29 · 最近更新 2026-10-09（推送 2026-09-29）· 130★ · MIT · JavaScript · 信源 [1356]",
    ),
    dict(
        nid="rpm40c3", name="StandRig —— 把「2D 建模」做成 MCP 工具，让 agent 直接调（★82）",
        url="https://github.com/sayaka-aiart/StandRig",
        lang="TypeScript", stars="82",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：AI-editable 2D modeling and playback **via MCP** —— 输入已拆好的 PSD，输出**可编辑、可回放**的 2D 模型，"
              "中间是**一个独立本地服务 + 一个可嵌入的 runtime**。",
        analogy="**这条和别家都不一样**：别人在「让 AI 帮你建模」，它是**把「建模能力」本身包装成 agent 能调用的工具（MCP）**。"
                 "不是 AI 替你点鼠标，而是**你的 agent 拿它当一件工具使**。你手上正好有 MCP 生态，这个抽象层级值得单独看一眼。",
        warn="⚠️ 创建于 2026-09-09，**推送停在 09-13**（元数据更新在 10-07）→ 先确认还活着再投入。",
        ext=(85, "8.5/10", "「建模 = MCP 工具」是本辑最可复用的一个想法，与 agent 生态直接对接"),
        use=(45, "4.5/10", "Apache-2.0 + 本地服务；但★82、推送停了一个月，先把架构读明白"),
        src="创建 2026-09-09 · 最近更新 2026-10-07（推送 2026-09-13）· 82★ · Apache-2.0 · TypeScript · 信源 [1357]",
    ),
    dict(
        nid="rpm40c4", name="puppet-part-splitter —— 纯客户端把插画/PSD 拆成部件层（★4）",
        url="https://github.com/0ran/puppet-part-splitter",
        lang="JavaScript", stars="4",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：为 **Live2D / Spine / Wallpaper Engine** 做的客户端素材拆分器 —— 把插画或 PSD 拆成部件层，并自动打包贴图。",
        analogy="**「纯客户端」这三个字是关键**：不用装 AI 环境、不用 GPU、不用上传到别人的服务器，"
                 "打开网页就能拆。对「只是想把手头一张图拆成能用的部件」这个最实际的需求，它比那些要炼丹的流水线近得多。",
        warn="⚠️ ★4、**无许可证（licenseInfo 为空 = 默认保留全部权利）** → **不能直接拿来用**，只能读做法或自己重写；"
             "① 推送停在 2026-09-06。",
        ext=(60, "6.0/10", "零依赖的拆层入口；思路可直接借鉴"),
        use=(45, "4.5/10", "无许可证是硬伤；但纯前端、门槛最低"),
        src="创建 2026-09-06 · 最近更新 2026-09-30（推送 2026-09-06）· 4★ · 无许可证 · JavaScript · 信源 [1358]",
    ),
    dict(
        nid="rpm40c5", name="pixijs-live2d-spine-viewer —— 一个 PixiJS 舞台同时放 Live2D 与 Spine（★2）",
        url="https://github.com/4163/pixijs-live2d-spine-viewer",
        lang="JavaScript", stars="2",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：基于 **PixiJS + WebGL** 的独立网页渲染器，**同时显示 Live2D（Cubism 2/3）与 Spine（2.x）动画**。",
        analogy="**「一个页面里同时放两种动画格式」是实际一定会撞上的需求**（比如 Live2D 角色配 Spine 特效）。"
                 "多数方案要各引一套宿主，这一条把两者塞进同一个 PixiJS 舞台 —— 给静态站加动态素材时能省一整套胶水代码。",
        warn="⚠️ ★2、MIT；只支持 **Cubism 2/3，不支持 4/5** —— 手上有 5.x 模型的人要看清这条边界。",
        ext=(60, "6.0/10", "双格式同台渲染，Web 端少一套宿主"),
        use=(60, "6.0/10", "MIT + 纯前端，打开就能跑；但格式上限停在 Cubism 3"),
        src="创建 2026-07-19 · 最近更新 2026-09-30（推送 2026-09-30）· 2★ · MIT · JavaScript · 信源 [1359]",
    ),
    dict(
        nid="rpm40c6", name="live2d-auto-pipeline（daoming07280）—— 同链路的 RTX 4060 实测（★0）",
        url="https://github.com/daoming07280/live2d-auto-pipeline",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="自述：Live2D auto pipeline —— See-Through 768/30 + psd2live 工作流笔记、脚本与样例 moc3 结果（**RTX 4060**）。",
        analogy="**注意它和 `mw2wbyys6t-sudo/live2d-auto-pipeline`（已在索引）是「同名不同 owner」**，上一辑已判定纯属巧合，"
                 "本辑复现该结论：两者内容不同，但**都指向同一条 See-Through + psd2live 链路**。"
                 "值得记的不是这条本身，而是「**这条链路已经有多个人在各自跑**」这件事。",
        warn="⚠️ 「768/30」这个参数在仓库外**未得到证实**，照录不自证。",
        ext=(55, "5.5/10", "第三个同类实测点，用来确认「这条链不是孤例」"),
        use=(45, "4.5/10", "★0、内容以笔记为主；当作别人的实验记录读"),
        src="最近更新 2026-09-18（推送 2026-09-18）· 0★ · MIT · Python · 信源 [1360]",
    ),
    dict(
        nid="rpm40c7", name="ComfyUI-See-through —— 在 ComfyUI 里做「深度分层」拆图（★0）",
        url="https://github.com/Bellpepperknuthamsun280/ComfyUI-See-through",
        lang="Python", stars="0",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：把二次元插画转成**分层的 2.5D PSD**（按深度切层 + 导出工具），**直接服务 Live2D 工作流**。",
        analogy="前面几条流水线的第一站（拆层）大多是脚本；**这一条把它做成了 ComfyUI 节点**。"
                 "如果你已经有一台跑 ComfyUI 的机器，这条路是「用现成工作流搭，而不是自己写脚本」。",
        warn="⚠️ ★0、**无许可证（licenseInfo 为空 = 默认保留全部权利）** → **不能拿来直接用**，只能读它的做法。",
        ext=(60, "6.0/10", "把拆层接进 ComfyUI 生态；思路可借鉴"),
        use=(30, "3.0/10", "无许可证 + ★0，本机不可直接采用"),
        src="创建 2026-04-24 · 最近更新 2026-10-11（推送 2026-10-11）· 0★ · 无许可证 · 信源 [1361]",
    ),
    dict(
        nid="rpm40c8", name="PSLayerLRSplitter —— 一个 Photoshop 脚本，专拆「左右对称」部件（★1）",
        url="https://github.com/satoxpochi/PSLayerLRSplitter",
        lang="JavaScript", stars="1",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="一个 **Photoshop 脚本**：把名字带 LR 后缀的文件夹**自动拆成左右两份独立部件**（Live2D 的パーツ分け／素材分け用途）。",
        analogy="**别小看这一步**：拆层里最烦的活之一就是「左边头发和右边头发要分开做物理」。"
                 "这类「一个脚本解决一个具体痛点」的小工具，往往比大而全的流水线更耐用。",
        warn="⚠️ ★1，2026-09-12 创建后**基本没再推**（推送 09-13），当成「可以抄的小脚本」而不是依赖。",
        ext=(50, "5.0/10", "单点工具，思路清晰；MIT 可自由改写"),
        use=(60, "6.0/10", "纯 PS 脚本、MIT，看得懂就能改；无外部依赖"),
        src="创建 2026-09-12 · 最近更新 2026-09-13（推送 2026-09-13）· 1★ · MIT · JavaScript · 信源 [1362]",
    ),

    # ---------- B. 桌宠「身体」侧：宿主技术栈换代 ----------
    dict(
        nid="rpm40c9", name="plugin-2d-skel —— 给「Live2DViewerEX」补数据格式支持（★1）",
        url="https://github.com/hoardodile/plugin-2d-skel",
        lang="TypeScript", stars="1",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：**Live2DViewerEX 的数据格式支持** —— 让 hoardodile 这个查看器能读 Live2D、Spine 与 DragonBones 三种动画。",
        analogy="**生态位值得记**：Live2DViewerEX 是桌面上很流行的一类「壁纸/桌宠播放器」，"
                 "它有自己的数据格式。**「为一个已有播放器写格式适配插件」这条路，比自己从零写桌宠省事得多** —— "
                 "对只想让角色出现在桌面上的人，这是一条近路。",
        warn="⚠️ ★1、MIT；创建 2026-08-31，属早期；宿主 `hoardodile` 本体不在本卡范围内。",
        ext=(55, "5.5/10", "「适配已有播放器」的路线，比自建桌宠成本低"),
        use=(45, "4.5/10", "★1、生态小；适合已经用 Live2DViewerEX 的人"),
        src="创建 2026-08-31 · 最近更新 2026-09-29（推送 2026-09-20）· 1★ · MIT · TypeScript · 信源 [1363]",
    ),
    dict(
        nid="rpm40c10", name="Mio —— Windows 本地优先的个人 AI Agent（★49）",
        url="https://github.com/ochiru520/Mio",
        lang="Python", stars="49",
        tags=[("t-make", "建模"), ("t-ok", "近期活跃"), ("t-new", "新")],
        plain="自述：Windows 本地优先的个人 AI Agent —— 对话、记忆、日记、语音、QQ、**Live2D**、屏幕感知。",
        analogy="**MIT + Python + Windows 本地优先**，和你的栈（本地 Ollama、Windows、Python）逐条对得上；"
                 "功能面「对话 + 记忆 + 日记 + 语音 + QQ + Live2D + 屏幕感知」正好是**「一个人怎么把 Live2D 塞进一个完整 agent 应用」的参考架构**。",
        warn="⚠️ **功能多 = 每个都浅**。当架构参考，别当全能工具。",
        ext=(80, "8.0/10", "功能性最全的单体参考；MIT 可读可改"),
        use=(75, "7.5/10", "Python + MIT + 当天仍在推送；本机可直接跑起来看"),
        src="最近更新 2026-10-11（推送 2026-10-11）· 49★ · MIT · Python · 信源 [1364]",
    ),
    dict(
        nid="rpm40c11", name="waifu-companion —— 纯浏览器的 Live2D 伴侣，许可最宽松（★38）",
        url="https://github.com/waifuai/waifu-companion",
        lang="JavaScript", stars="38",
        tags=[("t-make", "建模"), ("t-ok", "近期活跃"), ("t-new", "新")],
        plain="自述：浏览器里的 AI 伴侣 —— Live2D 角色、语音对话、长期记忆。",
        analogy="**MIT-0 是本辑遇到最宽松的许可证**（≈公共领域，连署名都不要求），而且**纯浏览器**、不用装任何桌面运行时。"
                 "对「静态索引站想挂一个会聊天的看板娘」这条需求，它是最贴近的起点。",
        warn="⚠️ 跑在浏览器里 → **模型与推理得外接**（自述没说是否本地推理）。",
        ext=(70, "7.0/10", "MIT-0 + Web 栈，改造自由度最高"),
        use=(70, "7.0/10", "无需桌面运行时；但推理后端要自己接"),
        src="最近更新 2026-10-11（推送 2026-10-11）· 38★ · MIT-0 · JavaScript · 信源 [1365]",
    ),
    dict(
        nid="rpm40c12", name="charivo —— 模块化的 Live2D AI 角色框架（★23）",
        url="https://github.com/zeikar/charivo",
        lang="TypeScript", stars="23",
        tags=[("t-tool", "工具"), ("t-ok", "近期活跃"), ("t-new", "新")],
        plain="自述：交互式 Live2D AI 角色 —— **模块化 TypeScript 框架**，覆盖 LLM、TTS、STT 与实时语音。",
        analogy="和上面那些「一整坨应用」不同，它是**框架**：LLM / TTS / STT / 实时语音各自成模块，你可以只换其中一块。"
                 "**想自己拼而不想抄别人整个工程时，框架比应用好用。**",
        warn="⚠️ ★23 意味着生态很小，遇到问题基本只能自己读源码。",
        ext=(75, "7.5/10", "模块化 = 可替换；MIT；适合当自己项目的骨架"),
        use=(65, "6.5/10", "TypeScript + MIT；比单体应用更适合改造"),
        src="创建 2025-09-16 · 最近更新 2026-10-09（推送 2026-10-06）· 23★ · MIT · TypeScript · 信源 [1366]",
    ),
    dict(
        nid="rpm40c13", name="Nexus —— 本地优先的桌面 AI 伴侣（★20）",
        url="https://github.com/FanyinLiu/Nexus",
        lang="TypeScript", stars="20",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="自述：本地优先的桌面 AI 伴侣 —— 一个 Live2D 或立绘傀儡角色待在桌面上，**记住要紧的事**，靠（语音）说话。",
        analogy="把「记忆」当成一等公民来写（「remembers what matters」）—— 这正是桌宠和普通聊天窗口的分水岭："
                 "**没有记忆的桌宠，第二天还是陌生人**。",
        warn="⚠️ ★20，创建于 2026-03-28，属早期项目。",
        ext=(70, "7.0/10", "本地优先 + 记忆侧设计；MIT"),
        use=(60, "6.0/10", "桌面端 TypeScript，需要读代码才能改"),
        src="创建 2026-03-28 · 最近更新 2026-10-10（推送 2026-10-03）· 20★ · MIT · TypeScript · 信源 [1367]",
    ),
    dict(
        nid="rpm40c14", name="suzuran-pet —— Q 版狐狸医师桌宠，本地语音克隆（★17）",
        url="https://github.com/sslbs09/suzuran-pet",
        lang="JavaScript", stars="17",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="中文项目：Q 版狐狸医师桌面宠物，深浅双主题，**任意 OpenAI 兼容 API**，**本地语音克隆（中 / 日）**，"
              "支持 Spine / Live2D / GIF 多种形态。",
        analogy="**「任意 OpenAI 兼容 API」这个设计很关键** —— 它意味着你可以把后端指向**本地 Ollama**，"
                 "整条链路不出本机。加上本地语音克隆，这是本辑里**最接近「全本地桌宠」的一个**。",
        warn="⚠️ 许可证 NOASSERTION；语音克隆涉及声音版权，**只用自己有权利的声音**。",
        ext=(70, "7.0/10", "多形态（Spine/Live2D/GIF）+ OpenAI 兼容接口，接本地模型最省事"),
        use=(65, "6.5/10", "中文项目、JS 栈；★17 但当天仍在推"),
        src="创建 2026-08-20 · 最近更新 2026-10-09（推送 2026-10-11）· 17★ · NOASSERTION · JavaScript · 信源 [1368]",
    ),
    dict(
        nid="rpm40c15", name="EmaAgent —— Tauri 桌面伴侣，「叙事记忆」单独存（★3）",
        url="https://github.com/chengyuZou/EmaAgent",
        lang="TypeScript", stars="3",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="自述：桌面优先的 AI 伴侣 agent，Tauri + React + Fastify，**一个 Live2D 舞台 + 本地 SQLite 记忆 + 独立的叙事 RAG**。",
        analogy="亮点是**把「叙事 RAG」和普通记忆分开存**：事实归事实、故事归故事。"
                 "这在角色扮演类应用里是个真问题 —— 混在一起存，角色很快就会「记得自己没经历过的事」。",
        warn="⚠️ ★3，早期项目；Tauri 栈比 Electron 轻，适合 16GB 机器。",
        ext=(70, "7.0/10", "记忆分层设计可借鉴；Tauri 轻量"),
        use=(55, "5.5/10", "★3；架构值得读，成品度低"),
        src="最近更新 2026-10-11（推送 2026-10-11）· 3★ · MIT · TypeScript · 信源 [1369]",
    ),
    dict(
        nid="rpm40c16", name="NekoPapa —— Tauri + Rust + C++/OpenGL 原生舞台（★0）",
        url="https://github.com/Hisakazu333/NekoPapa",
        lang="TypeScript", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="自述：基于 Tauri、React、Rust 与 **C++/OpenGL 原生舞台**构建的跨平台 Live2D 桌面伴侣。",
        analogy="**Apache-2.0 是本辑里对商用最友好的许可之一**（明确授权、含专利条款）。"
                 "但「原生 OpenGL 舞台」那层意味着**编译门槛高** —— 想跑起来得先过构建这一关。",
        warn="⚠️ ★0；C++/OpenGL 那层要自己编，**本机过这一关不轻松**。",
        ext=(65, "6.5/10", "许可证宽容（Apache-2.0）+ 原生渲染路线"),
        use=(35, "3.5/10", "★0 且要编 C++/OpenGL，短期投入产出比低"),
        src="最近更新 2026-10-10（推送 2026-10-10）· 0★ · Apache-2.0 · TypeScript · 信源 [1370]",
    ),

    # ---------- C. 格式 / 渲染线 ----------
    dict(
        nid="rpm40c17", name="Neocari —— Mocari 的纯 Rust 派生版，专攻原生 Cubism V2（★0）",
        url="https://github.com/HELPMEEADICE/Neocari",
        lang="Rust", stars="0",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：**Mocari 的纯 Rust 派生版**，专注原生 Cubism V2 模型的加载与渲染。",
        analogy="**它和已在索引里的 `Eatgrapes/Mocari` 有血缘**（自述就写着 derivative of Mocari）—— 这条不算新项目，"
                 "而是**同一条技术路线的分家**。记它的理由：① 说明 Rust 侧有人在持续投入；② **GPL-3.0** 会传染。",
        warn="⚠️ **GPL-3.0** —— 改它再分发必须开源；★0、创建 2026-09-26 后基本未动。",
        ext=(55, "5.5/10", "Rust 格式解析支线的继承者，登记以免下轮重复发现"),
        use=(25, "2.5/10", "GPL-3.0 + ★0 + 派生项目，短期不用"),
        src="创建 2026-09-26 · 最近更新 2026-09-27（推送 2026-09-27）· 0★ · GPL-3.0 · Rust · 信源 [1371]",
    ),
    dict(
        nid="rpm40c18", name="embedded-live2d —— 把 Live2D 塞进嵌入式（PainterEngine 生态）（★0）",
        url="https://github.com/sdegfd/embedded-live2d",
        lang="C", stars="0",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：PainterEngine 的 Live2D 编辑器、引擎与模型。技术栈是 **C**。",
        analogy="**本辑最意外的一条**：别人在讨论 WebGL / Unity / Godot 时，这条在往**嵌入式**方向搬。"
                 "对你没有直接用途，但它说明「Live2D 的运行时」这件事已经有人做到了 C 这一层 —— **对理解 moc3 的解析边界有用**。",
        warn="⚠️ ★0、描述极简；**MIT 但生态极小**。",
        ext=(40, "4.0/10", "极端平台的方向参考；MIT"),
        use=(20, "2.0/10", "与桌面/Web 需求无关，仅作生态观察"),
        src="创建 2026-09-28 · 最近更新 2026-10-03（推送 2026-10-02）· 0★ · MIT · C · 信源 [1372]",
    ),
    dict(
        nid="rpm40c19", name="vega-plugin-cubism —— 「插件宿主 + Cubism 插件」的分层结构（★0）",
        url="https://github.com/haneoka-gakuen/vega-plugin-cubism",
        lang="TypeScript", stars="0",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：为 Vega 提供 Live2D Cubism 2–5 角色与口型同步。同组织下另有一个宿主（`vega`）与若干同级插件。",
        analogy="**Live2D 生态里基本都是单体应用，这个分层结构很少见**：宿主一套、Cubism 支持单独一个插件。"
                 "好处是「换渲染后端」不用重写整个应用。**MPL-2.0 是文件级 copyleft，比 GPL 温和。**",
        warn="⚠️ ★0（全部同级仓库都是 0）；早期项目。",
        ext=(60, "6.0/10", "插件化分层是个好架构参考；MPL-2.0 许可温和"),
        use=(35, "3.5/10", "★0、无文档，只能读源码"),
        src="最近更新 2026-10-11（推送 2026-10-11）· 0★ · MPL-2.0 · TypeScript · 信源 [1373]",
    ),
    dict(
        nid="rpm40c20", name="live2dqt —— 把 Live2D 做成透明置顶的桌面覆盖层（★1）",
        url="https://github.com/davidleonstr/live2dqt",
        lang="Python", stars="1",
        tags=[("t-tool", "工具"), ("t-new", "新")],
        plain="自述：把 Live2D 模型显示成**透明、始终置顶的桌面覆盖层**，或嵌进 Qt 窗口里。",
        analogy="**「透明 + 置顶」是所有桌宠的入场券**，但每个宿主平台做法都不同。这是个最小实现，"
                 "**想用 Python + Qt 自己做桌宠时，这就是那段样板代码。**",
        warn="⚠️ ★1、2026-09-29 创建后**没有后续推送**。",
        ext=(50, "5.0/10", "最小可用的透明覆盖层样板；MIT"),
        use=(60, "6.0/10", "Python + MIT，读一遍就知道 Qt 这条路怎么走"),
        src="创建 2026-09-29 · 最近更新 2026-09-29（推送 2026-09-29）· 1★ · MIT · Python · 信源 [1374]",
    ),

    # ---------- D. 一手资料与价格锚（非 GitHub） ----------
    dict(
        nid="rpm40c21", name="给网站挂看板娘：把默认「拉远程模型」改成自托管（掘金）",
        url="https://juejin.cn/post/7439232445470359552",
        lang="教程", stars="—",
        tags=[("t-make", "资源"), ("t-new", "新")],
        plain="用 `live2d-widget` 一行脚本挂看板娘的完整本地化改法：**复制 `autoload.js` 与模型定义文件，把 "
              "`isLocalModel` / `modelsPath` / `modelListPath` 三项指向本地 `model/`**，再重新打包。",
        analogy="**这条和你的索引站场景几乎逐条对得上**：离线自托管看板娘的正解就是「改 autoload 本地化 + 起静态服务器」，"
                 "**不需要任何后端**。",
        warn="⚠️ 两个真坑：① **直接双击 HTML 打开会失败**（浏览器禁止 `file://` 直载资源）→ 必须起本地服务器；"
             "② 模型文件通常几 MB 到几十 MB，**静态站挂上去很吃带宽**。另：`live2d-widget` 是 **GPL-3.0**，商业站要小心传染。",
        ext=(75, "7.5/10", "自托管看板娘的操作手册；场景与本索引站重合度极高"),
        use=(85, "8.5/10", "可以当场照做；唯一成本是模型体积与流量"),
        src="掘金 · 作者「程序员鱼皮」· 2024-11 · 2026-10-11 取正文 · 信源 [1375]",
    ),
    dict(
        nid="rpm40c22", name="Live2D 建模的真实市场报价（B 站工房在售橱窗）",
        url="https://mall.bilibili.com/neul-next/index.html?itemsId=1100321012&page=mall-up_itemDetail",
        lang="价格锚", stars="—",
        tags=[("t-make", "资源"), ("t-new", "新")],
        plain="**可以直接当「模型值多少钱」的现价锚点**：A 档 ¥800 起（头部单 X+Z、身体 XYZ 平移、单段物理、3×2 口型）；"
              "B 档 ¥1200 起（头 25° X+Y、身体转面、二段物理、3×4 口型）；C 档 ¥1800 起（头 45°、双段 Z、多段物理、含 VB）。"
              "按键表情 ¥50–100（现白送），按键动画 ¥100 起；**复杂模「有效图层 >200」做得很慢**，且**不接原画、只接拆好的 PSD**。",
        analogy="**「九轴 / 物理段数 / 口型格数」这些技术档位，就是价格阶梯本身** —— 这张表把「贵在哪」写清楚了。"
                 "判断「自己学还是花钱买」时，它比任何教程都直接。",
        warn="⚠️ B 站工房与米画师是**两类平台**，报价口径不同，别混着比。",
        ext=(60, "6.0/10", "现价锚点，非工具；做预算判断时最省事"),
        use=(70, "7.0/10", "打开就能看；建议与索引里已有的米画师橱窗卡对照读"),
        src="B 站工房橱窗（itemsId 1100321012）· 2026-10-11 取数 · 信源 [1376]",
    ),
    dict(
        nid="rpm40c23", name="CLIP STUDIO 官方：Live2D 数据的「补图」该怎么做（中文）",
        url="https://tips.clip-studio.com/zh-cn/articles/674",
        lang="教程", stars="—",
        tags=[("t-make", "资源"), ("t-new", "新")],
        plain="**官方（CSP）给「拆分/补图」这件事的标准答案**：身体要在部件图层下方新建「基础」层填底色 → 保护不透明度画阴影 → "
              "上方补线稿 → 用蒙版融合接缝；脸部易漏点：**被睫毛遮住的眼睛要补成完整圆形**、**眼白要补眼球背面**"
              "（移瞳孔时会露）、轮廓要挖出眼睑、**眼睑单独建部件**（闭眼用）；**布料正反面要拆成两个部件**。",
        analogy="「补图」是新手最容易跳过、又最容易在做动画时崩掉的一步 —— **你没画的部分，转头的时候就会露出来**。"
                 "这是官方出的、带图的、有中文版的一手说明。",
        warn="⚠️ 是 CSP 官方 tips（不是 Live2D 官方），**流程通用但软件操作是 CSP 的**。",
        ext=(70, "7.0/10", "官方一手、中文、带图；做模型的前置必读"),
        use=(80, "8.0/10", "读完可直接照做；补图规范是所有后续步骤的地基"),
        src="CLIP STUDIO 官方 tips（繁/简中文）· 2026-10-11 取正文 · 信源 [1377]",
    ),
    dict(
        nid="rpm40c24", name="官方论坛：物理完全不动，`Maximum Output` 卡在 0（2026-10-06）",
        url="https://community.live2d.com/discussion/2389/why-won-t-my-live2d-physics-move-maximum-output-is-stuck-at-0",
        lang="一手帖", stars="—",
        tags=[("t-warn", "存疑"), ("t-new", "新")],
        plain="用户用 Cubism 5.3：给 `Hair Front` 做了 keyform，物理里配了 `Inputs: Angle X / Angle Z / Body rotation X / Z`、"
              "`Output: Hair Front`，结果**鼠标移动时摆锤完全不动**；且该输出的 **`Maximum Output` 显示 0 且改不了**。"
              "**截至采集没有回复。**",
        analogy="**没有官方解答的帖也值得记** —— 因为它把「配了却一动不动」这个模糊症状，"
                 "和 `Maximum Output = 0 且不可编辑` 这个**具体可观察量**绑在了一起。下次遇到，先查这一项，不必从头翻教程。",
        warn="⚠️ **无解答**，别当成权威结论；它只是一条**排查线索**。",
        ext=(50, "5.0/10", "症状与可观察量对应表，排查时省时间"),
        use=(55, "5.5/10", "遇到物理不动时按这条先查 Maximum Output"),
        src="Live2D 官方论坛 Help 区 · 2026-10-06 · 无回复 · 2026-10-11 取正文 · 信源 [1378]",
    ),
]

FOOTNOTES = [
    (1355, "https://github.com/bluewakame/live2d-psd-generator", "bluewakame/live2d-psd-generator",
     "1★ · MIT · Python · 创建 2026-09-15 · 推送 2026-09-15 · 更新 2026-09-21 · GraphQL 实测 · 日文项目，遮挡部分用 AI 补全"),
    (1356, "https://github.com/shinshin86/still2rig-psd", "shinshin86/still2rig-psd",
     "130★ · MIT · JavaScript · 创建 2026-08-29 · 推送 2026-09-29 · 更新 2026-10-09 · GraphQL 实测 · 依赖用户授权的 Colab GPU 会话"),
    (1357, "https://github.com/sayaka-aiart/StandRig", "sayaka-aiart/StandRig",
     "82★ · Apache-2.0 · TypeScript · 创建 2026-09-09 · 推送 2026-09-13 · 更新 2026-10-07 · GraphQL 实测 · 定位是 MCP 工具"),
    (1358, "https://github.com/0ran/puppet-part-splitter", "0ran/puppet-part-splitter",
     "4★ · **无许可证** · JavaScript · 创建/推送 2026-09-06 · 更新 2026-09-30 · GraphQL 实测 · 无许可证 = 默认保留全部权利"),
    (1359, "https://github.com/4163/pixijs-live2d-spine-viewer", "4163/pixijs-live2d-spine-viewer",
     "2★ · MIT · JavaScript · 创建 2026-07-19 · 推送/更新 2026-09-30 · GraphQL 实测 · 支持 Cubism 2/3 与 Spine 2.x，不含 4/5"),
    (1360, "https://github.com/daoming07280/live2d-auto-pipeline", "daoming07280/live2d-auto-pipeline",
     "0★ · MIT · Python · 推送/更新 2026-09-18 · REST API 实测 · 与 mw2wbyys6t-sudo/live2d-auto-pipeline 同名不同 owner（复现上辑结论）"),
    (1361, "https://github.com/Bellpepperknuthamsun280/ComfyUI-See-through", "Bellpepperknuthamsun280/ComfyUI-See-through",
     "0★ · **无许可证** · 创建 2026-04-24 · 推送/更新 2026-10-11 · REST API 实测 · 无许可证 = 默认保留全部权利"),
    (1362, "https://github.com/satoxpochi/PSLayerLRSplitter", "satoxpochi/PSLayerLRSplitter",
     "1★ · MIT · JavaScript · 创建 2026-09-12 · 推送/更新 2026-09-13 · GraphQL 实测 · Photoshop 脚本"),
    (1363, "https://github.com/hoardodile/plugin-2d-skel", "hoardodile/plugin-2d-skel",
     "1★ · MIT · TypeScript · 创建 2026-08-31 · 推送 2026-09-20 · 更新 2026-09-29 · GraphQL 实测 · Live2DViewerEX 数据格式支持"),
    (1364, "https://github.com/ochiru520/Mio", "ochiru520/Mio",
     "49★ · MIT · Python · 推送/更新 2026-10-11 · REST API 实测"),
    (1365, "https://github.com/waifuai/waifu-companion", "waifuai/waifu-companion",
     "38★ · **MIT-0** · JavaScript · 推送/更新 2026-10-11 · REST API 实测 · 本辑最宽松许可"),
    (1366, "https://github.com/zeikar/charivo", "zeikar/charivo",
     "23★ · MIT · TypeScript · 创建 2025-09-16 · 推送 2026-10-06 · 更新 2026-10-09 · GraphQL 实测"),
    (1367, "https://github.com/FanyinLiu/Nexus", "FanyinLiu/Nexus",
     "20★ · MIT · TypeScript · 创建 2026-03-28 · 推送 2026-10-03 · 更新 2026-10-10 · GraphQL 实测"),
    (1368, "https://github.com/sslbs09/suzuran-pet", "sslbs09/suzuran-pet",
     "17★ · NOASSERTION · JavaScript · 创建 2026-08-20 · 推送 2026-10-11 · 更新 2026-10-09 · GraphQL 实测 · 中文项目，支持任意 OpenAI 兼容 API"),
    (1369, "https://github.com/chengyuZou/EmaAgent", "chengyuZou/EmaAgent",
     "3★ · MIT · TypeScript · 推送/更新 2026-10-11 · GraphQL 实测"),
    (1370, "https://github.com/Hisakazu333/NekoPapa", "Hisakazu333/NekoPapa",
     "0★ · Apache-2.0 · TypeScript · 推送/更新 2026-10-10 · REST API 实测"),
    (1371, "https://github.com/HELPMEEADICE/Neocari", "HELPMEEADICE/Neocari",
     "0★ · GPL-3.0 · Rust · 创建 2026-09-26 · 推送/更新 2026-09-27 · GraphQL 实测 · 自述为 Mocari 的纯 Rust 派生（Mocari 已在索引）"),
    (1372, "https://github.com/sdegfd/embedded-live2d", "sdegfd/embedded-live2d",
     "0★ · MIT · C · 创建 2026-09-28 · 推送 2026-10-02 · 更新 2026-10-03 · GraphQL 实测 · PainterEngine 生态"),
    (1373, "https://github.com/haneoka-gakuen/vega-plugin-cubism", "haneoka-gakuen/vega-plugin-cubism",
     "0★ · MPL-2.0 · TypeScript · 推送/更新 2026-10-11 · REST API 实测 · 同组织另有宿主 vega 等 5 个仓库，只收本插件"),
    (1374, "https://github.com/davidleonstr/live2dqt", "davidleonstr/live2dqt",
     "1★ · MIT · Python · 创建/推送/更新 均为 2026-09-29 · GraphQL 实测"),
    (1375, "https://juejin.cn/post/7439232445470359552", "掘金《1 分钟，让你的网站充满吸引力！》（程序员鱼皮）",
     "cn 路 · 看板娘自托管：改 `isLocalModel` / `modelsPath` / `modelListPath` 指向本地；两个真坑 = file:// 直载失败须起服务器、模型几 MB~几十 MB 吃流量；"
     "`live2d-widget` 为 GPL-3.0"),
    (1376, "https://mall.bilibili.com/neul-next/index.html?itemsId=1100321012&page=mall-up_itemDetail", "B 站工房《Live2D 建模》在售橱窗",
     "cn 路价格锚 · A ¥800 / B ¥1200 / C ¥1800 起的档位差（九轴角度、物理段数、口型格数）；按键表情 ¥50-100、按键动画 ¥100 起；复杂模「有效图层&gt;200」做得很慢；不接原画"),
    (1377, "https://tips.clip-studio.com/zh-cn/articles/674", "CLIP STUDIO 官方 tips《在 CLIP STUDIO PAINT 中制作 Live2D 数据【下篇】》",
     "cn 路 · 官方「补图」标准：眼白要补眼球背面 / 被睫毛遮住的眼睛补成完整圆形 / 眼睑单独建部件 / 布料正反面拆两个部件；补图缺失会在转动时露出"),
    (1378, "https://community.live2d.com/discussion/2389/why-won-t-my-live2d-physics-move-maximum-output-is-stuck-at-0",
     "官方论坛《Why won't my Live2D physics move? Maximum Output is stuck at 0》",
     "official 路 · 2026-10-06 一手帖 · **截至采集无回复** · 症状：物理摆锤不动 + 输出参数的 `Maximum Output` 为 0 且不可编辑（Cubism 5.3）"),
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

    desc = ('第三十五辑三路调研（gh 路 49 条 + 主 agent 补位 22 条 / cn 路 24 条 / official 路 5 条），本版取 24 项，'
            '主题 **「轮子长成了一条流水线」+ 桌宠宿主技术栈换代**。'
            '所有 ★ / 许可证 / 语言 / 创建·推送·更新日全部走 GitHub API 逐条实测（子 agent 报的重点候选已由主 agent 逐条复验）。'
            '<strong>本辑主线：① 「立绘 → AI 拆层 → 自动绑定 → moc3」这条链第一次出现多个仓库互相引用 —— '
            '绑定核心件 psd2live（★614）**第 31 版就已收录**（本辑只复验：当天仍在推、许可证当时记的是 GPL-3.0），'
            '本版新增的是链条两端：still2rig-psd（★130 MIT，拆层 + QA 自检，跑在用户授权的 Colab GPU 上）、'
            'StandRig（★82 Apache-2.0，**把绑定做成 MCP 工具**，让 agent 直接调）、'
            'live2d-psd-generator（生成分层 PSD 时**用 AI 补被遮挡的部分**）、'
            'puppet-part-splitter（**纯客户端**把手头一张图拆成部件层，零依赖零上传）；'
            '② 桌宠「身体」侧宿主换代：Tauri / Rust / 原生 OpenGL / 纯浏览器明显变多，且「给某个 AI 编码工具配一个 Live2D 身体」'
            '已成重复模式（Codex / DSH / MaiBot 各有实现）；③ 格式线本辑增量小，但出现「Mocari 的 Rust 派生版 Neocari」'
            '与「把 Live2D 搬进嵌入式」两条侧面消息；④ 附四张非 GitHub 一手卡：看板娘自托管手册、B 站工房现价锚（¥800/1200/1800）、'
            'CSP 官方补图规范、官方论坛「物理不动且 Maximum Output 卡 0」的排查线索。'
            '⑤ **本辑顺带完成欠了两轮的待办①** —— 给 1338 张旧卡回填 pushed_at / updated_at（**1212 处**），'
            '新卡 src 行格式与之一致；另抓到 **22 个改过 owner/name 的仓库**（链接腐化清单）。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm40g">',
             '      <div class="group-title" data-page-node-id="rpm40gt">🆕 第四十版增补 · 轮子长成了一条流水线：AI 拆层→自动绑定→moc3（24 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm40gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm40r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm40ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]

    for o, n in zip(HEAD_OLD, HEAD_NEW):
        if src.count(o) != 1:
            print("二次校验失败：页头锚点 %s 现在出现 %d 次" % (o[:40], src.count(o)))
            return 1
        src = src.replace(o, n)

    open(HTML, "w", encoding="utf-8").write(src)
    print("✅ 已插入 %s：%d 张卡 + %d 条脚注（[%d]-[%d]）"
          % (MARKER, len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE, FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    print("   页头：1355 → 1379 项；卡片 1338 → %d" % (1338 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
