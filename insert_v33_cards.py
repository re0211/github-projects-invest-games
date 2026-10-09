# -*- coding: utf-8 -*-
"""第三十三版增补：把第二十八辑「Live2D 全链路」的 16 个条目登记进 index.html。

本辑候选池约 90 条（GitHub 65 / 中文社媒 14 / 官方与海外 11 组），
三路交叉零重复；与 `index.html`（1199 项）及全部历史存档机器比对，命中 0。

**本辑主线：「Cubism 5 的 moc3 第三方库不吃」这句话，本轮终于有了机理。**
不是 moc3 的版本号在作怪，是 **Core 的 ABI 版本**：v5 ABI = Core 5.1（Editor 5.1 引入），
v6 ABI = Core 6.0（Editor 5.3 引入，官方承认「引入多个破坏性变更」）。
VTube Studio / 老版 Ren'Py / gd_cubism 停在 v5，**最新 Ren'Py 已经是 v6**。
→ 这条与本机 Ren'Py 8.5.3 源码 `renpy/gl2/live2d.py:86` 的
  `e.add_note("Live2D Cubism 5.3 or later is required.")` 互相印证（两个独立来源）。

**另一条主线是「商用红线」被钉死了**：Live2D 官方免费素材授权协议（中文版）§2.1.3.1
写明——年销售额 < 1000 万日元的个人/小规模事业者，**Live2D 原创角色可用于任何营利目的**，
但**合作角色（名執 尽、春傘 つみき）不得营利使用**；且一律禁转发、禁改编、禁反向工程。

**上轮欠账 #2 闭环（本机实测）**：Ren'Py 8.5.3 要求 Core **5.3 及以上**（v6 ABI），
因此中文圈流传的「装 `CubismSdkForNative-4-r.1`」这条 2022 年的教程**现在已经会失败**。
→ 已记为 **M-0030**：教程里的 SDK 版本号会过期，版本要求要从**被集成方自己的源码**里读。

数据来源：2026-10-10 GitHub REST API 实测（主 agent 抽 15 个复核）+ WebFetch 一手页面（`_r28/`）。
幂等：已存在本版标记则跳过。
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1198"'
FIRST_NEW_FOOTNOTE = 1199
MARKER = "第三十三版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十二版增补 2026-10-10',
    '共 1199 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项 + 第三十二版增补 16 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十三版增补 2026-10-10',
    '共 1215 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项 + 第三十二版增补 16 项 + 第三十三版增补 16 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm33c1", name="live2d-add-motion-sample-web-ui（不买 Editor，纯 JSON 给模型加动作）",
        url="https://github.com/shinshin86/live2d-add-motion-sample-web-ui",
        lang="HTML", stars="194",
        tags=[("t-make", "建模"), ("t-ok", "持续更新"), ("t-warn", "星少但有用")],
        plain="只在 `.motion3.json` 层面给**已有**模型追加动作：先分析模型有哪些参数、安全值域、"
              "**哪些参数是物理驱动的（不能直接打关键帧）**，再写关键帧 → 生成 → 独立校验器 → headless Chrome 截图验证。"
              "只依赖 Python 3 标准库。",
        analogy="上一辑给的 `live2d-motion3` 是「动作编辑器」，这条是「动作**流水线**」——"
                "它把「分析→写→生成→校验→肉眼验收」五步全串起来了，还带 `AGENTS.md`，"
                "让 Claude Code / Codex 这类 agent 能按规矩自动加动作。",
        warn="**物理驱动的参数不要直接给关键帧**（仓库写死的经验规则）；"
             "自带模型需另从官方样本页下载（注意合作角色禁商用）；本机未实跑（沙箱 git clone 被挡）。",
        ext=(88, "8.8/10", "和 `live2d-motion3` 同一层（改 JSON 不改二进制），天然绕开 ABI 坑；"
                           "`AGENTS.md` + `CLAUDE.md` 双份，接 agent 流水线最省事"),
        use=(92, "9.2/10", "本辑对用户最实用的一条：给自家角色加「害羞/点头/惊讶」这类表情动作"
                           "**一分钱 Editor 钱都不用花** · MIT · 推送 2026-10-08"),
        src="推送 2026-10-08 · 194★ · MIT · HTML · 信源 [1199]",
    ),
    dict(
        nid="rpm33c2", name="pixi-live2d5（专治「Cubism 5 的模型网页播放器不吃」）",
        url="https://github.com/omniwaifu/pixi-live2d5",
        lang="TypeScript", stars="12",
        tags=[("t-make", "建模"), ("t-ok", "持续更新"), ("t-warn", "星少但有用")],
        plain="`pixi-live2d-display` 的 **Cubism 5 分叉**：README 明确要求 PixiJS 8.19+ / "
              "Cubism SDK for Web R5（**Core 6.0.1**）/ WebGL2，`bun run setup` 会自己下载 Core 与 13 个 GLSL shader；"
              "保留原高层 API，去掉了 cubism2/4 子路径。",
        analogy="上一辑那条坑（Cubism 5 的 moc3 第三方库不吃）一直只有「降版本导出」这个笨办法。"
                "这个分叉是**正面解法**：它不是让你退回去，而是把运行时升上来配合新版 Core。",
        warn="安装顺序是坑：`bun install --ignore-scripts` → `bun run setup`（下载 Core）→ `bun run prepare`，"
             "**不能照搬旧习惯正常装**（README 专门解释过）。另附「模型是不可信输入」的安全告示。",
        ext=(82, "8.2/10", "解掉 ABI 坑的网页侧正路；另有 `easy-live2d v1.0.0`（已在索引 [1196]）可互为备选"),
        use=(86, "8.6/10", "做网页试玩页/宣传页时的**首选运行时** · MIT · 推送 2026-10-05 · ⚠️ 本机未实跑"),
        src="推送 2026-10-05 · 12★ · MIT · TypeScript · 信源 [1200]",
    ),
    dict(
        nid="rpm33c3", name="PurismCore（把「第三方吃不吃 Cubism 5」讲成 ABI 版本问题）",
        url="https://github.com/SakuraMotion/PurismCore",
        lang="C", stars="40",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="Cubism Core 的**开源 C99 重实现**（单头文件 bundle，覆盖 Win/macOS/Linux/iOS/Android/Emscripten）。"
              "真正的价值在它的 `docs/COMPAT.md`：给出 **v5 ABI = Core 5.1（Editor 5.1 引入）、"
              "v6 ABI = Core 6.0（Editor 5.3 引入）** 的对照表，并举例「VTube Studio 用 v5、"
              "老版 Ren'Py 用 v5、最新 Ren'Py 用 v6、gd_cubism 用 v5」。",
        analogy="过去三轮我们一直把「不兼容」当成玄学，只能靠试。这张表把它变成了**一个可以查的数字**——"
                "就像知道自己是 USB-C 还是 Micro-USB，不用再每个播放器插一遍。",
        warn="MIT 但项目年轻（★40，创建 2026-06-03）；`make ABI=v5` 可切 ABI 版本；"
             "README 自述「should be compatible with Ren'Py」——**未实测**。",
        ext=(90, "9.0/10", "C 核心最容易被别的语言 FFI 包一层；ABI 可选 = 一份代码同时伺候新旧生态"),
        use=(80, "8.0/10", "**本辑机理来源**：先读它的 COMPAT.md，再决定你的模型该用哪个 Editor 版本导出"),
        src="推送 2026-08-21 · 40★ · MIT · C · 信源 [1201]",
    ),
    dict(
        nid="rpm33c4", name="Live2D/CubismSpecs（官方文件格式规格，自己写解析器的唯一权威）",
        url="https://github.com/Live2D/CubismSpecs",
        lang="Python", stars="22",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="**官方**发布的 Cubism 文件格式规格（moc3 / model3 / motion3 / exp3 / pose3 / cdi3 等）。"
              "2026-08-05 合并了一个 PR：给 **exp3.json / pose3.json 加可选 Version 字段**——"
              "这是该仓 2017 年以来**第二次有人改**（上次 2024-04）。",
        analogy="逆向出来的格式说明是「别人猜的」，这个是「出题人自己给的」。"
                "想动手写转换器、校验器、或者自己生成动作文件，先读它能省掉几十小时试错。",
        warn="**NOASSERTION**（官方规格仓没声明开源许可证）；规格仓不是 SDK，不含运行时。"
             "另有 PR #5 提议给 cdi3 加 Drawables，**至今 open，不是可用功能**。",
        ext=(92, "9.2/10", "权威依据 = 第三方工具的地基；加了 Version 字段后，"
                           "第三方工具写出的 exp3/pose3 今后能自证版本"),
        use=(78, "7.8/10", "读文档为主、不动手也能受益；真正动手写解析器时才显出价值"),
        src="推送 2026-08-05 · 22★ · NOASSERTION · Python · 信源 [1202]",
    ),
    dict(
        nid="rpm33c5", name="see-through（SIGGRAPH 2026：一张插画自动分出可动层）",
        url="https://github.com/shitagaki-lab/see-through",
        lang="Python", stars="4497",
        tags=[("t-make", "建模"), ("t-ok", "持续更新"), ("t-new", "新收录")],
        plain="**SIGGRAPH 2026 论文官方实现**：单张二次元插画 → 带深度排序的可操作 2.5D 分层模型，"
              "**自动补全被遮挡区域**（后脑勺、衣服下面的身体），直接喂给下游绑骨工具。",
        analogy="上一辑那篇失败复盘的结论是「立绘本身不含让它动起来的信息，全得靠人补」。"
                "这个项目补的正是**「自动补」**这一步——它不吹「一键出 moc3」，"
                "而是把最卡脖子的自动拆层 + 遮挡补全做扎实。",
        warn="**本辑最有实操价值的信息**：它有 **HuggingFace 免费在线 demo 且免登录**"
             "（768 分辨率约 89 秒），**不碰本地显存** —— 这直接取消了「先确认显卡再决定」这个阻塞。"
             "本地跑仍有显存门槛。",
        ext=(94, "9.4/10", "Apache-2.0 + 学术背书 + ★4497，是「AI 自动拆图」目前最硬的一条"),
        use=(84, "8.4/10", "**先用在线 demo 试**，跑通了再考虑本地部署；产出是 PSD，不进产物链则无传染性风险"),
        src="推送 2026-10-05 · 4497★ · Apache-2.0 · Python · 信源 [1203]",
    ),
    dict(
        nid="rpm33c6", name="image2live2d（能直写 moc3，但作者自己说门槛是法务不是技术）",
        url="https://github.com/Wzhang3912/image2live2d",
        lang="Python", stars="43",
        tags=[("t-make", "建模"), ("t-warn", "有法务风险")],
        plain="输入**已分层的画**，全自动出 mesh / deformer / 物理 / 动作，可导出三种目标："
              "nijilive `.inp`（主力，完全验证）/ **Live2D `.moc3` 全套** / `.cmo3`（可在 Editor 里改）。"
              "moc3 codec 自称「完全逆向生成，与 5 个官方 v3 模型 byte-for-byte 验证」。",
        analogy="这是「完全不装 Editor 也能产出 moc3」这条路上走得最远的一个。"
                "但就像有人给你一把能开所有门的钥匙——**技术上成了，不代表你可以用**。",
        warn="⚠️ **硬红线**：作者原话「剩下的门槛是法务（Live2D 的 SDK license），不是技术」；"
             "官方免费素材授权协议 §4.1.3 **禁止反向工程**。**做原型/出 `.inp` 可以，"
             "要上架的商业作品不建议把产线建在这上面。**",
        ext=(86, "8.6/10", "一条链路出两种格式（.inp + .moc3），便于在开源/商业格式间横跳"),
        use=(45, "4.5/10", "技术冲击力满分，**商用适用性不及格**；Apache-2.0 但挡不住上游的契约限制"),
        src="推送 2026-09-07 · 43★ · Apache-2.0 · Python · 信源 [1204]",
    ),
    dict(
        nid="rpm33c7", name="moc3ingbird（CVE-2023-27566：模型文件是不可信输入）",
        url="https://github.com/OpenL2D/moc3ingbird",
        lang="C++", stars="98",
        tags=[("t-make", "建模"), ("t-warn", "安全风险")],
        plain="一份**能让读取方崩溃**的 `.moc3`。作者判断：Cubism Core 是 C 库，"
              "**对 MOC3 内的偏移不做边界检查，读写可越界**；自称尚未实现纯 Core 下的代码执行，"
              "但认为「几乎可以确定可行」。仓内含 ImHex 用的 `moc3.hexpat`。",
        analogy="我们一直把模型当成「图片」——图片顶多显示错。其实它是**可执行格式**："
                "里面全是偏移量和长度，读的一方若不做边界检查，就等于把地址交给陌生人填。",
        warn="**只加载自己做的模型时，这条与你无关**；但一旦计划「支持玩家导入模型 / UGC」，"
             "这就是一个真实的攻击面。中文与日文 Live2D 制作贴里**几乎没人提这件事**。",
        ext=(70, "7.0/10", "安全视角的补位；`moc3.hexpat` 本身也是好用的格式查看器"),
        use=(72, "7.2/10", "按「别踩」记：不做 UGC 则 0 成本，做 UGC 则是必做的工程项"),
        src="推送 2026-06-06 · 98★ · NOASSERTION · C++ · 信源 [1205]",
    ),
    dict(
        nid="rpm33c8", name="CLI-Anything 的 cli-anything-live2d（42 条命令，模型交付前的质检员）",
        url="https://github.com/HKUDS/CLI-Anything",
        lang="Python", stars="51790",
        tags=[("t-make", "建模"), ("t-ok", "持续更新"), ("t-new", "新收录")],
        plain="内含 `cli-anything-live2d`：**42 条命令**从命令行 inspect / validate / lint / "
              "runtime-check（Web SDK 兼容性）/ atlas / orphan / batch / flatten / pack "
              "`.model3.json`，**全程不需要 Cubism Editor**。",
        analogy="前几辑的痛点都在「做不出来」。但当你手里有几十个模型时，真正折磨人的是另一件事："
                "贴图路径断了、motion 淡入淡出时间不统一、一堆孤儿文件、想知道这批模型能不能被 Web SDK 吃。"
                "这就是个**交付前的质检员**。",
        warn="这是个超大的通用仓库（★5 万+），Live2D 只是其中一个子命令集，"
             "**别指望它只有你要的那部分**；Apache-2.0。",
        ext=(84, "8.4/10", "inspect+validate+pack 三件套可直接塞进 CI，模型一改就跑一遍"),
        use=(88, "8.8/10", "**本批唯一「今天装上今天就能省时间」的东西**；Python CLI，本机直接跑"),
        src="推送 2026-09-22 · 51790★ · Apache-2.0 · Python · 信源 [1206]",
    ),
    dict(
        nid="rpm33c9", name="umamo（真在读 .cmo3 的开源编辑器，但别等它）",
        url="https://github.com/umamoorg/umamo",
        lang="Kotlin", stars="149",
        tags=[("t-make", "建模"), ("t-warn", "早期阶段")],
        plain="直接对标 Cubism Editor 的开源跨平台绑骨编辑器，**读写 `.cmo3` 源格式**，"
              "一等公民笔/触控支持，Kotlin Multiplatform 便于二次开发。",
        analogy="它是本批唯一以「drop-in 替换 Cubism Editor」为目标的开源编辑器——"
                "但**它是唯一一个，也还没发布**。就像唯一的桥还在打地基。",
        warn="⚠️ **GPL-3.0**（商用闭源要留意）；官方自述 **early alpha、尚未公开发布**，"
             "建模/UV/物理在做、**动画功能未实现**，macOS/Android 被渲染器卡住。",
        ext=(80, "8.0/10", "格式级兼容 = 现有 Cubism 工程能直接打开，一旦成熟价值极高"),
        use=(42, "4.2/10", "**现在不能用**：alpha 未发布 + 动画功能缺失 + GPL-3.0 传染性"),
        src="推送 2026-10-09 · 149★ · GPL-3.0 · Kotlin · 信源 [1207]",
    ),
    dict(
        nid="rpm33c10", name="Live2D 免费素材授权协议（中文版）——官方免费模型能不能进你卖的游戏",
        url="https://www.live2d.com/eula/live2d-free-material-license-agreement_cn.html",
        lang="契约", stars="官方",
        tags=[("t-make", "建模"), ("t-ok", "一手权威")],
        plain="把「官方免费素材到底能不能进商业游戏」逐条钉死。素材分四类，分界线是"
              "**最近一个会计年度销售收入不足 1,000 万日元的个人/学生/小规模企业**："
              "在这个身份下，**Live2D 原创角色「可用于任何营利或非营利目的」**，"
              "而**合作角色「不得出于营利目的使用」**。",
        analogy="上一辑算的是「SDK 授权要不要钱」——那是**引擎侧**的账。"
                "这一条要回答的是**素材侧**的账：**你下载的那个官方示例模型本身，能不能放进你要卖的游戏里**。",
        warn="四类素材一律**禁止转发、禁止改编、禁止反向工程**（第 4.1 条）；派生作品须按要求标注著作权。"
             "合作角色 = **名執 尽、春傘 つみき**，做商业作品直接排除。"
             "另有个别角色硬约束：ミアラ/桃瀬ひより 完全不许改设计、にと 必须保持二头身。",
        ext=(76, "7.6/10", "不产生代码，但它决定你前面所有工具链能不能合法落地"),
        use=(96, "9.6/10", "**本辑最硬的一条**：把「先用官方 sample 跑通再换自己角色」"
                            "这条最短路径的合规风险归零了，代价只是下载前看清分类"),
        src="官方 EULA 中文版 · WebFetch 一手 · 信源 [1208]",
    ),
    dict(
        nid="rpm33c11", name="Cubism 5.4 alpha 公告（8 天后失效，别写进制做链）",
        url="https://www.live2d.com/en/information/cubism-5_4-alpha/",
        lang="公告", stars="官方",
        tags=[("t-make", "建模"), ("t-warn", "时效性")],
        plain="**alpha 可用到 2026-10-18，到期后不再提供**；官方 FAQ 原话「请勿销售或分发」"
              "用 alpha 做出的数据，只能个人使用。没有付费 license 也能装来试 5.4 新功能，"
              "但官方明确 **alpha→beta/release 的 SDK 迁移不作保证**，产出数据不提供任何质量保证。",
        analogy="这是一张**有截止日期的试玩券**：能提前摸到 Parameter Controller 这类新功能，"
                "但它的产出物被官方盖章「不许卖」。",
        warn="⚠️ **别把 5.4 写进第一款商业作品的制作链**——正式版出来前，模型工程一律用 **5.3.x** 产出。"
             "5.4 alpha 还第一次提供了官方 **External API**（从外部程序操作 Editor），"
             "这是未来「脚本/AI 驱动 Editor」的入口。",
        ext=(72, "7.2/10", "External API 是「Agent 驱动 Editor」的官方化起点，值得按季度复看"),
        use=(58, "5.8/10", "**只能尝鲜不能产出**；想试就这周抓，别用它的东西发版"),
        src="官方公告 2026-07-14（分类页 + 公告页两处互证）· 信源 [1209]",
    ),
    dict(
        nid="rpm33c12", name="官方样本数据利用条件（选模型前先看它属于哪一类）",
        url="https://www.live2d.com/learn/sample/model-terms/",
        lang="官方", stars="官方",
        tags=[("t-make", "建模"), ("t-ok", "一手权威")],
        plain="把官方样本分成三类：**Live2D 原创角色 / 合作角色 / 外部授权角色**，"
              "**每类适用条件不同**，且部分角色有**个别限制**（能不能改设计、要不要保留设定）。"
              "样本页还多出了 **Ren Foster**（学 Cubism 5.3 新绘制功能）、**Niziiro Mao**（Blend Shape）、"
              "**Kei**（MotionSync 真实口型同步）等新模型。",
        analogy="上一张卡（EULA）告诉你「原创角色能商用」，这张卡告诉你**具体哪个角色是原创角色**——"
                "规则和执行清单不是一回事。",
        warn="合作角色（名執 尽、春傘 つみき）明确**不得营利使用、不得改変・配布**；"
             "ミアラ/桃瀬ひより 一切设计改动被禁止；しずく 必须保留名字与设定。",
        ext=(70, "7.0/10", "选模型的准入清单；配合 EULA 一起读才完整"),
        use=(90, "9.0/10", "**要验证「Cubism 5.3 的 moc3 能不能在我的引擎里动」，"
                            "Ren Foster 是官方给的免费靶子**"),
        src="官方样本页 · WebFetch 一手 · 信源 [1210]",
    ),
    dict(
        nid="rpm33c13", name="nizima AI 政策（AI 图做的 Live2D 一律禁上架，但 Editor 辅助功能豁免）",
        url="https://www.live2d.com/en/information/",
        lang="政策", stars="官方",
        tags=[("t-make", "建模"), ("t-warn", "合规红线")],
        plain="禁止投稿/销售/交付「制作过程的全部或一部分使用了画像生成 AI 的插画，"
              "**以及用这些插画做成的 Live2D 作品**」，加笔修正、描摹、AI 补画物体同样在禁止列。"
              "**但例外条款点名豁免：Cubism Editor 中辅助 Live2D 制作的功能，包括「動きの自動生成機能」**"
              "——理由是与画像生成 AI 的「学习目的、学习过程、目的均不同」。",
        analogy="平台划的线不是「有没有用 AI」，而是**「AI 替你画了，还是 AI 替你动了」**。"
                "前者禁，后者放——这条区分很反直觉，但写得很清楚。",
        warn="⚠️ **「AI 生成立绘 → 模型 → 上架」在 nizima 一票否决**；别的平台规则不同（本轮未核）。"
             "另：官方自身的 AI 研究政策末次更新 **2022-04-25**，明确写「不做从零生成插画、不做从插画全自动建模」。",
        ext=(66, "6.6/10", "不产生工具，但直接否决掉一整条「AI 立绘全自动出模型再卖」的路线"),
        use=(88, "8.8/10", "**决定了素材策略**：Safe 做法仍是「人画 + 官方辅助功能」"),
        src="官方/平台政策页 · WebFetch 一手 · 信源 [1211]",
    ),
    dict(
        nid="rpm33c14", name="renpy.cn《Live2d 实验一则，有演示，附代码》（⚠️ 它的 SDK 版本号已过期）",
        url="https://www.renpy.cn/thread-1260-1-1.html",
        lang="Ren'Py", stars="社区",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-warn", "版本已过期")],
        plain="中文圈罕见的一篇**带完整可运行代码**的 Ren'Py × Live2D 实战："
              "`define config.gl2 = True` + `image natori close = Live2D(\"natori_pro_t06\", loop=True, base=.6)`；"
              "还写了 `CharacterPreprocessor` 类用 `os.walk` 自动扫描 `exp/` 和 `motions/` 目录、"
              "把表情名和动作名读出来直接生成按钮（省掉手抄 model3.json）。",
        analogy="上一辑只核实到「Ren'Py 原生支持 + 前置条件」，这条是**把后半段（游戏里怎么切表情/切动作）做出来的人**。"
                "`CharacterPreprocessor` 那段思路可以直接搬到视觉小说的调试界面上。",
        warn="⚠️ **它教的是装 `CubismSdkForNative-4-r.1`，这条在 2026 年已经会失败** —— "
             "本机 Ren'Py 8.5.3 源码 `live2d.py:86` 写着 `Live2D Cubism 5.3 or later is required`（需 **v6 ABI**）。"
             "另一个至今有效的坑：**runtime 文件夹里的东西拷进模型目录后，必须把 runtime 文件夹本身删掉，否则报错**。",
        ext=(80, "8.0/10", "自动扫描 exp/motions 生成按钮这一段，可直接抄进自己的调试 screen"),
        use=(70, "7.0/10", "**代码思想值钱、版本号别照抄**；日期未核实（正文取不到）"),
        src="renpy.cn 社区帖 · 日期未核实（正文仅搜索片段）· 信源 [1212]",
    ),
    dict(
        nid="rpm33c15", name="米画师建模橱窗（把「一个模型值多少钱」摊成部件级明细）",
        url="https://www.mihuashi.com/stalls/51760",
        lang="报价", stars="一手",
        tags=[("t-make", "建模"), ("t-new", "新收录")],
        plain="两份**逐项明码标价**的建模报价单（￥2631 / ￥3157）：高精 2500+（图层 350 以内，"
              "每超 100 图层加收 15%），含头部九轴（**X 30-45°、Y 10-15°**）、3×3 或 3×4 口型、"
              "呼吸动态、全身三段物理；加价项：表情 50 元/个、第二套衣服 1000+、动画 150+。",
        analogy="值钱的不只是那个 2631 元，而是它把「**一个模型由哪些可计价部件组成**」摊开了——"
                "以后不管是外包还是自己学，这都是一张**验收清单**。",
        warn="「图层 350 以内，超出加价」说明**拆图精细度本身就是计价单位**；"
             "退款规则「做完物理不退」说明**物理是建模里最不可逆的一步**。"
             "另一份给出工期分段：布点透视 7-10 天 + 物理调试 10-15 天，占 30-45 天总工期的**三分之二**。",
        ext=(64, "6.4/10", "不是工具，但它把「自己学 vs 外包」这笔账变成了可以算的数字"),
        use=(86, "8.6/10", "**头部九轴 X30-45 / Y10-15 是能直接拿去验收自己模型的规格数字**"),
        src="米画师橱窗 · WebFetch 页面所见（截稿 2026-10-05 / 2026-07-01）· 信源 [1213]",
    ),
    dict(
        nid="rpm33c16", name="whalegirl-pet 真 Live2D 实现记录（中文，把全自动链路跑通的那个人）",
        url="https://github.com/7l-ui/whalegirl-pet/blob/main/docs/%E7%9C%9FLive2D-%E5%AE%9E%E7%8E%B0%E8%AE%B0%E5%BD%95.md",
        lang="中文实践", stars="一手",
        tags=[("t-make", "建模"), ("t-ok", "持续更新"), ("t-new", "新收录")],
        plain="一条**跑通了**的全自动流水线（正文是中文）：AI 生成透明底立绘 → **See-through** 拆成 15 层语义分层 PSD"
              "（自动补全遮挡）→ **psd2live** 自动绑骨导出 `.moc3 + .model3.json + .physics3.json`；"
              "成品 5.0 MB、18 个标准参数。作者强调**中间两步全自动，没有任何手工美术操作**。",
        analogy="上一辑那篇失败复盘亲手**证伪**了全自动路线，这篇是同一条路线的**正面证据**。"
                "两篇合起来才是完整判断——**差别不在工具，在素材**。",
        warn="**可以写进立绘规格书的两条硬约束**：`mouth` 图层必须是**最大张口**原图（否则 `ParamMouthOpenY=0` 时嘴被压成一条线）；"
             "`eyelash` **只能含上睫毛**（混入下睫毛会闭眼撕裂）。另：**psd2live 要 JDK 21**；"
             "**psd2live 是 GPL-3.0**，商用前必须先确认产出物的传染性。",
        ext=(82, "8.2/10", "给了「AI 立绘 → 可动模型」这条链最完整的一份中文踩坑清单"),
        use=(80, "8.0/10", "**See-through 有免登录的免费 HF 在线 demo** —— 不碰本地显存就能先试"),
        src="GitHub 中文文档 · WebFetch 一手 · 日期未核实 · 信源 [1214]",
    ),
]

FOOTNOTES = [
    (1199, "https://github.com/shinshin86/live2d-add-motion-sample-web-ui",
     "shinshin86/live2d-add-motion-sample-web-ui",
     "194★ · MIT · HTML · 推送 2026-10-08 · GitHub REST API 实测"),
    (1200, "https://github.com/omniwaifu/pixi-live2d5", "omniwaifu/pixi-live2d5",
     "12★ · MIT · TypeScript · 推送 2026-10-05 · GitHub REST API 实测"),
    (1201, "https://github.com/SakuraMotion/PurismCore", "SakuraMotion/PurismCore",
     "40★ · MIT · C · 推送 2026-08-21 · GitHub REST API 实测"),
    (1202, "https://github.com/Live2D/CubismSpecs", "Live2D/CubismSpecs（官方格式规格）",
     "22★ · NOASSERTION · Python · 推送 2026-08-05 · GitHub REST API 实测"),
    (1203, "https://github.com/shitagaki-lab/see-through", "shitagaki-lab/see-through",
     "4497★ · Apache-2.0 · Python · 推送 2026-10-05 · GitHub REST API 实测"),
    (1204, "https://github.com/Wzhang3912/image2live2d", "Wzhang3912/image2live2d",
     "43★ · Apache-2.0 · Python · 推送 2026-09-07 · GitHub REST API 实测"),
    (1205, "https://github.com/OpenL2D/moc3ingbird", "OpenL2D/moc3ingbird（CVE-2023-27566）",
     "98★ · NOASSERTION · C++ · 推送 2026-06-06 · GitHub REST API 实测"),
    (1206, "https://github.com/HKUDS/CLI-Anything", "HKUDS/CLI-Anything（含 cli-anything-live2d）",
     "51790★ · Apache-2.0 · Python · 推送 2026-09-22 · GitHub REST API 实测"),
    (1207, "https://github.com/umamoorg/umamo", "umamoorg/umamo",
     "149★ · GPL-3.0 · Kotlin · 推送 2026-10-09 · GitHub REST API 实测"),
    (1208, "https://www.live2d.com/eula/live2d-free-material-license-agreement_cn.html",
     "Live2D 官方《无偿提供素材使用授权协议》（中文版）",
     "官方 EULA · WebFetch 一手 · 协议页无发布日期"),
    (1209, "https://www.live2d.com/en/information/cubism-5_4-alpha/",
     "Live2D 官方 · Cubism 5.4 Alpha 发布公告",
     "2026-07-14（分类页 + 公告页两处互证）· alpha 可用至 2026-10-18 · WebFetch 一手"),
    (1210, "https://www.live2d.com/learn/sample/model-terms/",
     "Live2D 官方 · 样本数据利用条件（分角色）",
     "官方样本页 · WebFetch 一手 · 页面无修订日"),
    (1211, "https://www.live2d.com/en/information/",
     "Live2D 官方信息页（本轮 nizima AI 政策与官方 AI 研究政策入口）",
     "官方/平台政策 · WebFetch 一手 · 政策末次更新 2022-04-25"),
    (1212, "https://www.renpy.cn/thread-1260-1-1.html",
     "renpy.cn《Live2d 实验一则，有演示，附代码》",
     "Ren'Py 中文社区 · 日期未核实（正文取不到，仅搜索片段）· ⚠️ 其 SDK 版本号已过期"),
    (1213, "https://www.mihuashi.com/stalls/51760",
     "米画师 · Live2D 建模橱窗（逐项报价单）",
     "¥2631 / ¥3157 两份 · WebFetch 页面所见（截稿 2026-10-05 / 2026-07-01）"),
    (1214, "https://github.com/7l-ui/whalegirl-pet/blob/main/docs/%E7%9C%9FLive2D-%E5%AE%9E%E7%8E%B0%E8%AE%B0%E5%BD%95.md",
     "whalegirl-pet《真 Live2D · 实现记录》（中文）",
     "GitHub 中文文档 · WebFetch 一手 · 文档无日期"),
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

    desc = ('第二十八辑三路调研（GitHub 65 / 中文社媒 14 / 官方与海外 11 组），本版取 16 项，'
            '主题 **Live2D 全链路**：优先「不买 Editor 也能干活」+「把玄学变成可查的数字」+「商用红线」。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测，主 agent 另抽 15 个复核。'
            '<strong>本辑主线：「Cubism 5 的 moc3 第三方库不吃」终于有了机理——不是 moc3 版本号，'
            '是 Core 的 ABI 版本（v5 = Core 5.1 / v6 = Core 6.0）</strong>；'
            '这与本机 Ren\'Py 8.5.3 源码 `live2d.py:86`「Live2D Cubism 5.3 or later is required」互相印证。'
            '另一条主线是商用红线：官方免费素材 EULA（中文版）§2.1.3.1 允许个人/小规模事业者'
            '**商用 Live2D 原创角色**，但合作角色不得营利、一律禁改编禁反向工程。')

    block = ['    <div class="group" data-page-node-id="rpm33g">',
             '      <div class="group-title" data-page-node-id="rpm33gt">🆕 第三十三版增补 · Live2D 全链路：ABI 之谜、不买 Editor 的工作流与商用红线（16 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm33gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm33r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm33ra%s">%s</a> — %s</div>'
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
