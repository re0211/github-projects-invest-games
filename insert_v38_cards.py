# -*- coding: utf-8 -*-
"""第三十八版增补：把第三十三辑「轮子开始分叉」的 24 个条目登记进 index.html。

本辑候选：gh 路 33 条（+13 行边缘登记）、cn 路 19 条、official 路 26 条。
与 `index.html`（1301 项）及全部历史存档机器比对，本版 24 条命中 **0**。

**本辑主线：上一辑有人正面拆了「渲染 moc3」那堵墙；这一辑的看点不在墙，而在墙两侧长出了两丛完全不同的轮子。**

1. **一丛继续攻格式** —— `MahouTechnologies/moc3-rs`（★6，纯 Rust 直接解析 `.moc3` 二进制，不碰官方 Core）、
   `Heonys/live2d-web`（★2，**不用 PixiJS**、WebGL2 直渲 Cubism 3/4/5）、`shinkuan/Waifuland`（★81，
   Linux/Wayland 透明覆盖窗）、`Moebytes/live2d-renderer`（★19）。
2. **另一丛干脆不碰 `.moc3`** —— `lTwTlol/Auto-live2D-beta`（★28，分层 PSD 拖进浏览器即自动绑定，
   客户端本地处理免安装）、`Fenglin-Maple/AutoLive2d`（★19，**自写 `rig-validation-checklist.md` 验收清单**）、
   `goldimpact/Eviler`（★12，反着来：从 `.moc3` 里把 PSD 抠出来）。
3. **「大脑 / 身体分离」第一次被写成架构主张** —— `zziying/ai-live2d-body`（★46）主张桌宠**没有大脑**：
   不给你一个新 AI，而是**给你已有的 ta 装一具身体**（显示状态 / 回传触摸 / 身体 API）。
   配套「身体」侧供给本辑最密集：`zhuomianling` 桌面灵（★27，Windows + local-first + ADR 记忆账本）、
   `kiyotakali/Miru`（★175，三平台安装包）、`localai-rag-live2d`（★21）、`Firefly-Companion-AI-`（★27）、
   `xiaozhi-ios`（★128，移动端 + MCP）。
4. **官方 5.4 alpha2 手册正文第一次被读完**（official 路）—— ① **PSD 导入增强**：多层可合并当一个 ArtMesh，
   合图层组/合蒙版/除尘从 PS 脚本搬进编辑器（`*` 前缀的组不合并、别带调整图层）；
   ② **数据兼容是单向门**：alpha2 存的文件旧版打不开、未来 beta 也不保证；③ **可用期 10/18 到期**。
5. **本辑的「动手」部分**：静态核完 Inochi2D Win11 兼容性（下载 MSI + PE 解析，**无 OS 闸门**，
   真实风险是 VC++ 运行库与 OpenGL 驱动）；`Agent-desktop-pet` **许可读清但装不上**（要 CPython 3.12，本机没有）。
6. **AI 开发侧**：DSH 插件生态成形（`dsh-plugin-shop` ★1009 / `ds-harness-remote` ★309）；
   知识工程地图清单（`awesome-llm-knowledge-systems` ★93）；agent 记忆 MCP（`memorizer` ★215）。

**inbox 顺延**：`/skill-doctor`（连续第十二轮，下轮排在所有调研动作之前）。

数据来源：2026-10-11 GitHub REST API 实测（`gh api repos/<r>` 逐条，主 agent 已复验全部 34 个候选仓库，
与子 agent 汇报零出入）。幂等：已存在本版标记则跳过。
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1300"'
FIRST_NEW_FOOTNOTE = 1301
MARKER = "第三十八版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十七版增补 2026-10-11',
    '共 1301 个项目',
    '第三十六版增补 22 项 + 第三十七版增补 22 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十八版增补 2026-10-11',
    '共 1325 个项目',
    '第三十六版增补 22 项 + 第三十七版增补 22 项 + 第三十八版增补 24 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm38c1", name="moc3-rs —— 纯 Rust 直接解析 .moc3（不碰官方 Core）",
        url="https://github.com/MahouTechnologies/moc3-rs",
        lang="Rust", stars="6",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="一个**纯 Rust 的 `.moc3` 读取库** —— 不依赖 Live2D 官方 Core，直接自己解析那个二进制格式。",
        analogy="上一辑的 ayagami 也是走这条路。这是**「绕开 Cubism 授权」的正解方向**：官方 Core 是专有二进制，"
                "你只要不链接它、自己把格式读懂，就不欠它的许可。但代价是**一切都要自己来** —— "
                "这个库只做到「读」，没有渲染器、没有命令行、6★、一个人维护。",
        warn="⚠️ **玩具级，现在别用**：只有解析、没有渲染；6★；2023 年建仓至今只推过几次。"
             "登记它的价值在于**确认这条路上有哪些人**，避免下轮把同一个 6★ 当新发现。",
        ext=(40, "4.0/10", "方向对但推进极慢；同类只有 ayagami 一家在真做"),
        use=(20, "2.0/10", "不能当依赖；只能当「格式长什么样」的参考"),
        src="创建 2023-09-14 · 推送 2026-08-15 · 6★ · Apache-2.0 · Rust · 信源 [1301]",
    ),
    dict(
        nid="rpm38c2", name="live2d-web —— 不用 PixiJS 的 WebGL2 直渲运行时",
        url="https://github.com/Heonys/live2d-web",
        lang="TypeScript", stars="2",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="非官方 Web 运行时：**「Direct WebGL2 rendering without PixiJS」** —— 自带 **Framework 5-r.5 适配层**，"
              "支持 Cubism 3/4/5，含动作/序列/淡入淡出/加权 idle/表情/指针交互、"
              "**单个 canvas 上多模型共享 WebGL 上下文**、口型、MediaPipe 面捕（实验）与 devtools 面板。",
        analogy="已收录的 `pixi-live2d-display` 和 `easy-live2d` **都要求你先装 PixiJS**。"
                "这条是它们的**替代**而不是重复：它把 Pixi 那一层整个省掉，直接跟 WebGL2 打交道 —— "
                "少一层依赖、少一层 bug，代价是所有 2D 便利功能要自己写。",
        warn="⚠️ 2★、发布不足 3 个月；**Core 与模型一律不打包**（要自备 Cubism Core 和已授权的模型）。"
             "仓库里有 `AGENTS.md` + `CLAUDE.md` + soak 测试 —— 它是按「交给 agent 接手」的方式写的，可读性高。",
        ext=(72, "7.2/10", "省掉 Pixi 这一层是有真实价值的；5-r.5 适配层直接可抄"),
        use=(45, "4.5/10", "2★ 单人，别当依赖；做网页 Live2D 时值得先读它的渲染层"),
        src="创建 2026-07-29 · 推送 2026-09-01 · 2★ · MIT · TypeScript · 信源 [1302]",
    ),
    dict(
        nid="rpm38c3", name="Waifuland —— Linux/Wayland 的透明覆盖窗桌宠",
        url="https://github.com/shinkuan/Waifuland",
        lang="C++", stars="81",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="**Linux 桌面 Live2D 查看器**：用 `wlr-layer-shell` 把角色渲染成**透明的 Wayland 覆盖窗**。"
              "目录里是标准的 Cubism Native 示例骨架（`LAppLive2DManager.cpp` / `LAppModel.cpp` / `LAppWayland.cpp`）。",
        analogy="它是「把官方 Native 示例改造成 Linux 桌面挂件」的**完整范例** —— "
                "想抄的是**窗口穿透 + 区域命中**那套做法：怎么让角色剪影吃鼠标事件、而透明部分把点击还给桌面。",
        warn="⚠️ ①**平台是 Linux/Wayland**，对 Windows 用户没有直接价值；②**仓库未声明任何许可证** → 不要进任何发布物。"
             "价值只在读它的窗口处理思路。",
        ext=(55, "5.5/10", "覆盖窗 + 区域命中的参考实现，跨平台思路可迁移"),
        use=(15, "1.5/10", "Windows 上用不了；无许可不可复用代码"),
        src="创建 2026-04-11 · 推送 2026-04-14 · 81★ · 无许可证 · C++ · 信源 [1303]",
    ),
    dict(
        nid="rpm38c4", name="Auto-live2D-beta —— 分层 PSD 拖进浏览器就自动绑定",
        url="https://github.com/lTwTlol/Auto-live2D-beta",
        lang="HTML", stars="28",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="**把分层 PSD 拖进浏览器，自动切网格、自动变形、自动加物理，然后它就动起来了** —— "
              "客户端本地处理、免安装。桌面版走 WebView2（Win11 预装），可接 OpenSeeFace 做头/眨眼/口型/虹膜驱动。",
        analogy="它是**「拆图自动化」这条路最直白的一个**：缺闭眼/闭口差分时**自动生成通用差分**（按锚点缩放、"
                "颜色匹配睫毛和口部）；发丝按轮廓峰值检测、每层最多 6 束；低透明度噪点做连通域滤波；"
                "眼/眉/睫毛/闭眼还能**按重心自动分左右**。",
        warn="⚠️ **它驱动的不是 `.moc3`，是自家 2.5D 运行时** —— 所以做出来的东西**跨软件不通用**，"
             "不能拿去 VTube Studio 或 Cubism 里接着编。作者自己也在 README 里明说了这一点（这点很坦诚）。"
             "基于 `852wa/Anime2.5DRig` 二次开发。",
        ext=(70, "7.0/10", "自动差分 + 发丝分束 + 像素级连通域处理，是「拆图自动化」少见的完整实现"),
        use=(60, "6.0/10", "浏览器版双击即用、无依赖、MIT；适合快速验证「这张图能不能动」"),
        src="创建 2026-08-20 · 推送 2026-08-30 · 28★ · MIT · HTML · 信源 [1304]",
    ),
    dict(
        nid="rpm38c5", name="AutoLive2d —— 唯一自带「验收清单」的自动绑骨项目",
        url="https://github.com/Fenglin-Maple/AutoLive2d",
        lang="TypeScript", stars="19",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="面向二次元分层 PSD 的开源 Live2D 风格编辑器与运行时（React + TS + WebGL/Canvas + Electron），"
              "**不依赖 Cubism / Inochi2D 格式**；**内置经「低显存与 Windows 适配」的 see-through 源码**，"
              "可从单张图拆 PSD 再自动绑定。",
        analogy="它最值钱的不是代码，是 **`docs/rig-validation-checklist.md`** —— "
                "一份**固定验收清单**，写明「改算法必须回归」。自动绑骨这类东西最大的坑就是"
                "「改好了 A、悄悄弄坏了 B 而没人发现」，这个项目是**唯一把这件事写成文档的**。",
        warn="⚠️ 19★、单人、**自研运行时非标准格式**、无 release 二进制。"
             "目录里还有 `docs/cubism-5.4-alpha1-external-api.zh-CN.md`（它自己整理的中文版外部 API 文档）。",
        ext=(68, "6.8/10", "验收清单可整份抄走；伪 Z 只参与几何投影不抢 draw z 的做法值得记"),
        use=(42, "4.2/10", "低显存 + Windows 适配 + 内置 see-through，正对本机画像；但别当稳定依赖"),
        src="创建 2026-07-24 · 推送 2026-07-24 · 19★ · Apache-2.0 · TypeScript · 信源 [1305]",
    ),
    dict(
        nid="rpm38c6", name="ai-live2d-body —— 「你的桌宠不需要大脑」",
        url="https://github.com/zziying/ai-live2d-body",
        lang="文档", stars="46",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="一份**架构思路文档**（不是教程也不是代码）。核心命题是**大脑和身体分离**："
              "市面上的框架（airi / Open-LLM-VTuber）会**给你一个新的 AI** —— 人格来自框架自己的 prompt、"
              "记忆存在框架自己的库里；这篇主张桌宠**没有大脑**，只做三件事："
              "① 显示 ta 的状态 ② 把你的触摸传回 ta 的 session ③ 给 ta 一套身体 API。",
        analogy="如果你**已经有一个天天在用的 agent**（比如一个跑在本机的编码助手），"
                "那你要的不是「再养一个 AI」，而是**给现在这个 ta 装一具身体** —— "
                "让它说的话有表情、你摸它它有反应、它干活时你能看见。这篇把这个想法讲清楚了。"
                "配套代码版是 `zziying/ai-live2d-body-starter`（★17）。",
        warn="⚠️ **无许可证、仓库里只有两份 md** —— **不是能依赖的项目**，价值在被 downstream 引用当设计纲领。"
             "同类的还有 `Ariakage/live2d-agent-kit`（已在库）。",
        ext=(85, "8.5/10", "本辑唯一明确回答「为什么不用现成框架」的一份，思路可直接影响架构"),
        use=(30, "3.0/10", "没有代码可跑；只能当设计文档读"),
        src="创建 2026-07-06 · 推送 2026-09-05 · 46★ · 无许可证 · 信源 [1306]",
    ),
    dict(
        nid="rpm38c7", name="桌面灵 zhuomianling —— Windows + local-first 的桌宠框架",
        url="https://github.com/qiyueblues-design/zhuomianling",
        lang="TypeScript", stars="27",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "可用"), ("t-new", "新")],
        plain="开源、可自定义、**本地优先**的 Live2D 桌宠软件框架（Electron 43 + React 18 + TS5 + Vite6，"
              "**当前主平台 Windows**）。你导入自己的模型、配桌宠资料 / 人设 / 事件台词 / AI 聊天 / 视觉语音。"
              "**明确不内置受版权限制的模型、声音和 AI Key**。",
        analogy="它把最容易被做糊的一件事**写成了架构决策**：`docs/adr/0001-记忆权威账本.md` 与 "
                "`docs/adr/0002-本地中文记忆检索.md` —— 记忆归谁管、怎么检索，是先想清楚再写代码的。"
                "GPT-SoVITS 也走**配置文件**接入而不是写死。对「Windows + 自备模型 + 想自己改」的人，这是正面命中。",
        warn="⚠️ 27★、发布约 3 个月 → **先当框架读，别当稳定产品用**。",
        ext=(80, "8.0/10", "ADR 写记忆账本 + 框架化（模型自备）+ Windows 优先"),
        use=(68, "6.8/10", "MIT、Windows、local-first；本机画像的正面命中"),
        src="创建 2026-07-09 · 推送 2026-08-26 · 27★ · MIT · TypeScript · 信源 [1307]",
    ),
    dict(
        nid="rpm38c8", name="Miru —— 三平台都出安装包的本地优先伴侣",
        url="https://github.com/kiyotakali/Miru",
        lang="Python", stars="175",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="**「真的记得你、且完全跑在你自己机器上」的 AI 伴侣** —— 后端自托管、模型**任意 OpenAI 兼容**、"
              "长期记忆 + 主动陪伴 + 多端同步。**Windows / macOS / Android 三端都出安装包**"
              "（`Miru-Windows-x64-Setup.exe` / `.dmg` / `.apk`）。",
        analogy="本方向**「主干 vs 玩具」的分界线样本**：大多数桌宠项目只有源码、要你自己配环境；"
                "这个是**下载 exe 就能装**、而且手机端也有。想要「本地跑、但不想折腾」的话，这是本辑最成熟的入口。",
        warn="⚠️ Python 后端 + 566 项目录 → **二次改造成本不低**；「Windows 版具体用哪一套 Live2D 栈」需自行核实。",
        ext=(75, "7.5/10", "Apache-2.0 干净、三平台安装包齐全，本辑桌宠线最成熟"),
        use=(62, "6.2/10", "能直接装；想深度改造则偏重"),
        src="创建 2026-07-03 · 推送 2026-09-23 · 175★ · Apache-2.0 · Python · 信源 [1308]",
    ),
    dict(
        nid="rpm38c9", name="localai-rag-live2d —— 已有 Ollama 时改造成本最低的一份骨架",
        url="https://github.com/ice-only/localai-rag-live2d",
        lang="Python", stars="21",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="本地 AI 聊天 + **本地 RAG**：数据不上传云端，可自行导入记忆文件、改角色形象、记忆对话，"
              "**记忆库支持导入或对话后自动记录**。",
        analogy="把「本地 RAG + 长期记忆 + Live2D 形象」三件事打了个包，体量小、上手快。"
                "**如果你本机已经跑着 Ollama，这是这个方向上改造成本最低的一份起点。**",
        warn="⚠️ 推送停在 2026-07-30，近两个多月没动。",
        ext=(58, "5.8/10", "体量小、概念完整，适合当自建起点"),
        use=(66, "6.6/10", "MIT + 小体量 + 对接本地模型，对 16GB Windows 友好"),
        src="创建 2026-07-30 · 推送 2026-07-30 · 21★ · MIT · Python · 信源 [1309]",
    ),
    dict(
        nid="rpm38c10", name="Firefly-Companion-AI —— 双窗口解耦 + 鼠标穿透的工程样本",
        url="https://github.com/hhjk21/Firefly-Companion-AI-",
        lang="Python", stars="27",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-warn", "版权风险")],
        plain="基于《崩坏：星穹铁道》「流萤」的桌面 Live2D AI 伴侣（Win / macOS / Linux）。"
              "卖点是**双窗口解耦 + 鼠标穿透**、流式对话、**本地 ONNX 语义记忆**、双引擎主动关怀、"
              "GPT-SoVITS 原声 TTS、MCP 工具链 + Skill 插件体系。",
        analogy="**双窗口解耦 + 鼠标穿透**是 Live2D 桌宠的通用难点（怎么让角色剪影吃鼠标、"
                "透明处把点击还给桌面），它把方案写清楚了。本地 ONNX 记忆 + GPT-SoVITS 也正对「16GB + 本地模型」的画像。",
        warn="⛔ **角色素材版权归米哈游**，README 自述「仅个人学习交流、禁商用」—— "
             "**这套角色素材绝不可进任何发布物**。代码结构可以参考，美术资源不行。",
        ext=(60, "6.0/10", "双窗口解耦 + 事件穿透的方案值得抄"),
        use=(35, "3.5/10", "结构可参考，但自带素材不可用，等于要重做美术"),
        src="创建 2026-08-04 · 推送 2026-08-05 · 27★ · MIT · Python · 信源 [1310]",
    ),
    dict(
        nid="rpm38c11", name="xiaozhi-ios —— 把 Live2D 形象塞进移动 App 并接 MCP",
        url="https://github.com/goodko/xiaozhi-ios",
        lang="C++", stars="128",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="基于 SwiftUI 的「小智」AI 助手 **iOS 客户端**：集成 **Live2D 虚拟形象**、实时语音对话、"
              "**MCP 工具调用**与多模态交互（视觉 / 地图 / 小红书 / 抖音 / 本地音乐）。",
        analogy="本辑**唯一像样的移动端**（128★、MIT）。它回答的是一条很实际的问题："
                "**「我的 Live2D 形象怎么跟手机上的 agent 挂在一起、还让它会调工具」** —— 用 MCP 接，而不是自己造协议。",
        warn="⚠️ 对 Windows 桌面开发者价值有限；但对「跨端」这件事有启发（索引站也有移动入口的需求）。",
        ext=(65, "6.5/10", "移动端 + Live2D + MCP 的完整参考，生态位稀缺"),
        use=(40, "4.0/10", "iOS 专属；Windows 桌宠用不上"),
        src="创建 2026-08-10 · 推送 2026-08-10 · 128★ · MIT · C++ · 信源 [1311]",
    ),
    dict(
        nid="rpm38c12", name="SnekStudio —— Godot 写的 VTuber 软件（生产跑了 3 年）",
        url="https://github.com/ExpiredPopsicle/SnekStudio",
        lang="GDScript", stars="418",
        tags=[("t-make", "建模"), ("t-warn", "非Live2D"), ("t-ok", "可用")],
        plain="**用 Godot 4.7 写的开源 VTuber 软件**（自称 Super ~~Secret~~ Public Alpha），"
              "作者自述**自 2022 年起就在生产直播里用它**。只支持 **VRM 0.x**（VRM 1.x 会有严重问题），"
              "用 MediaPipe 做摄像头面捕，Win/Linux 有二进制 release，三平台 CI + 夜构建。",
        analogy="Live2D 的人常常忽略「3D 路线」这个分支。**如果你想的是「VRM + 面捕」而不是「Live2D 绑骨」**，"
                "这是本辑里唯一「生产环境跑了 3 年 + 三平台 CI」的存在；Godot 栈也比 Electron 轻、无商业授权问题。",
        warn="⚠️ **它不是 Live2D**：只吃 VRM 0.x，与 `.moc3` 完全不互通。别拿它当 Live2D 方案看。",
        ext=(78, "7.8/10", "GPL-3.0 + 三平台 CI + 真实生产使用史，3D 路线的重量级选项"),
        use=(50, "5.0/10", "走 3D 路线的话是首选之一；只想做 2D 立绘则不适用"),
        src="创建 2024-09-23 · 推送 2026-09-27 · 418★ · GPL-3.0 · GDScript · 信源 [1312]",
    ),
    dict(
        nid="rpm38c13", name="astrbot 直播陪伴插件 —— B站弹幕 → LLM → VTS → OBS 一条链",
        url="https://github.com/menglimi/astrbot_plugin_live_stream_companion",
        lang="Python", stars="58",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="面向 AstrBot 的直播陪伴插件：把**B 站弹幕读取 + LLM 自动回应 + VTube Studio 表情动作 + "
              "TTS 嘴型联动 + OBS 字幕层**组织进**同一条直播链路**。目录自带 `blivedm/`（B 站弹幕库）"
              "与 `l2d_mixin.py`（Live2D 演出混入）。",
        analogy="「直播集成」方向里**唯一把全链打通且日更的项目**。做直播的人最痛的是每个环节各写一套、"
                "时间戳对不上；它把这条链组织进一个插件里，`clients/open_live.py` 与 `l2d_mixin.py` 的拆分方式可直接借。",
        warn="⚠️ 依赖 AstrBot 生态；**VTube Studio 的模型需付费购买**。",
        ext=(70, "7.0/10", "全链打通 + 日更 + MIT，直播场景的唯一完整解"),
        use=(58, "5.8/10", "要用 AstrBot 与 VTS；对纯本地桌宠场景偏重"),
        src="创建 2026-06-09 · 推送 2026-10-11 · 58★ · MIT · Python · 信源 [1313]",
    ),
    dict(
        nid="rpm38c14", name="Brioche-Puppet —— 纯 C++ + 真三平台构建脚本的 VTuber 软件",
        url="https://github.com/HanetakaChou/Brioche-Puppet",
        lang="C++", stars="14",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="免费开源的 VTuber 软件（纯 C++），带三平台 CI 构建（Linux 侧含 `Android.mk` / `Application.mk`，"
              "macOS 侧含 `.xcodeproj`，另有 Windows workflow）。",
        analogy="**纯 C++ + LGPL-3.0 + 真正的三平台构建脚本**这个组合在这个方向很少见 —— "
                "大多数桌宠是 Electron 或 Python 套壳。想做「原生、低占用」路线的话，这套工程骨架值得读。",
        warn="⚠️ 14★、没有二进制 release、成熟度待验。",
        ext=(62, "6.2/10", "原生 C++ 工程骨架 + 真三平台 CI，生态位稀缺"),
        use=(25, "2.5/10", "要自己编译；无 release，上手门槛高"),
        src="创建 2025-02-06 · 推送 2026-07-21 · 14★ · LGPL-3.0 · C++ · 信源 [1314]",
    ),
    dict(
        nid="rpm38c15", name="dsh-plugin-shop —— 本机所跑运行时的插件市场",
        url="https://github.com/LivXue/dsh-plugin-shop",
        lang="TypeScript", stars="1009",
        tags=[("t-mod", "模块化"), ("t-ok", "可用"), ("t-new", "新")],
        plain="**DSH（DeepSeek Harness）插件市场** —— 自称「最全面的 DSH 插件市场，每日刷新、全网取材、发布前审核」。",
        analogy="**本机就跑在 DSH 上**，所以这是唯一千星级、且**直接决定「你能装到什么插件」**的入口。"
                "第一次把 `dsh plugin add …` 的**发现层**做成了基础设施。",
        warn="⚠️ 第三方市场，**「发布前审核」是作者自述** —— 装之前仍应逐条看源码。",
        ext=(82, "8.2/10", "本机生态的入口级基础设施，日更 + Apache-2.0"),
        use=(75, "7.5/10", "本机就是 DSH，装了就能用；注意第三方代码风险"),
        src="创建 2026-08-25 · 推送 2026-10-11 · 1009★ · Apache-2.0 · TypeScript · 信源 [1315]",
    ),
    dict(
        nid="rpm38c16", name="ds-harness-remote —— 在手机上操控本机的 DSH",
        url="https://github.com/liguobao/ds-harness-remote",
        lang="TypeScript", stars="309",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="基于 DSH 插件机制的多端远程访问方案：通过**端到端加密、P2P 优先**的网络，"
              "从 PC / Android / Web 随时访问并操作远程的 Harness 与 CodeX。",
        analogy="**「出门在外也能让 agent 改 index.html」**这件事对本机维护索引站有实际价值 —— "
                "不用把机器开着跑远程桌面，而是走 P2P 直连。",
        warn="⚠️ **未声明许可证 + 涉及远程访问与加密网络，安全面很大** —— 只作思路参考，别直接暴露。",
        ext=(75, "7.5/10", "P2P + E2E 的移动端操控，日更 309★"),
        use=(40, "4.0/10", "无许可 + 安全面大，不建议现在就用"),
        src="创建 2026-08-14 · 推送 2026-10-11 · 309★ · 无许可证 · TypeScript · 信源 [1316]",
    ),
    dict(
        nid="rpm38c17", name="memorizer —— 向量检索驱动的 agent 记忆 MCP",
        url="https://github.com/petabridge/memorizer",
        lang="C#", stars="215",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="**向量检索驱动的 agent 记忆 MCP server**（.NET / Akka 系）。",
        analogy="说明「agent 记忆」这件事已经从概念进入了**工程化竞品期** —— "
                "同题还有 `mtrnix/metronix-memory`（★107）、`ipiton/agent-memory-mcp`（★42）等一堆。"
                "本方向质量与活跃度最靠前的一个。",
        warn="⚠️ **栈是 .NET**，与「Windows + Ollama + Python/TS」这条路不同；"
             "向量检索会引入额外的模型与依赖（对 16GB 机器是负担）。登记为主。",
        ext=(70, "7.0/10", "MIT + 日更；但换栈成本高"),
        use=(28, "2.8/10", ".NET 栈不匹配；记忆方案可借鉴其接口设计"),
        src="创建 2025-07-15 · 推送 2026-10-09 · 215★ · MIT · C# · 信源 [1317]",
    ),
    dict(
        nid="rpm38c18", name="awesome-llm-knowledge-systems —— 给「选题」用的知识工程地图",
        url="https://github.com/kennethlaw325/awesome-llm-knowledge-systems",
        lang="HTML", stars="93",
        tags=[("t-mod", "模块化")],
        plain="一份「2026 年 LLM 知识工程」**地图式清单**：把 RAG、Context Engineering、Harness Engineering、"
              "Skill Systems、Agent Memory、MCP、Progressive Disclosure 串成一张统一图谱。",
        analogy="**它是给「选题」用的，不是给「用」用的** —— 可以直接当下几轮调研的方向盘，"
                "避免再零散地想到哪搜到哪。注意：是清单不是代码。",
        warn="⚠️ 清单类，不含实现；条目质量需自己抽查。",
        ext=(60, "6.0/10", "帮你把「该往哪搜」这件事本身结构化了"),
        use=(55, "5.5/10", "读一遍就能用；不产生任何代码"),
        src="创建 2026-04-06 · 推送 2026-09-15 · 93★ · MIT · HTML · 信源 [1318]",
    ),
    dict(
        nid="rpm38c19", name="awesome-digital-human-live2d —— ★2425 的数字人整套应用",
        url="https://github.com/wan-h/awesome-digital-human-live2d",
        lang="TypeScript", stars="2425",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "可用")],
        plain="名字像清单、**实为一整套数字人应用**：Docker 快速部署、**低于 2 核 2G** 就能跑、"
              "可接 Dify / FastGPT / Coze，ASR / LLM / TTS / Agent 模块化，"
              "**Live2D 模型与控制方式可扩展**，PC + 移动端 web。",
        analogy="2425★ 是本辑候选里体量最大的之一，而且**「低于 2 核 2G 即可运行」**这个数字很关键 —— "
                "它意味着这条路不吃本地显卡，走的是「服务端跑模型 + 前端放形象」。"
                "⚠️ 但它推送停在 2026-05-18，已经 5 个月没动。",
        warn="⚠️ **本辑只做了登记，没有深评**（时间不够，不假装核实过）—— "
             "**下轮正面评一次**，重点核：它到底是不是「Dify 生态壳 + Live2D 前端」。",
        ext=(70, "7.0/10", "★2425 + Docker 一键 + 模块化，体量极大"),
        use=(45, "4.5/10", "半年未动 + 低配数字人路线与绑骨主线不同；待下轮深评"),
        src="创建 2024-05-15 · 推送 2026-05-18 · 2425★ · MIT · TypeScript · 信源 [1319]",
    ),
    dict(
        nid="rpm38c20", name="live2dManager —— 把 CubismSdkForWeb 当 submodule 管理的样板",
        url="https://github.com/madosuki/live2dManager",
        lang="TypeScript", stars="1",
        tags=[("t-mod", "模块化")],
        plain="Live2D Cubism SDK for Web 的非官方库（`live2dManager.ts` / `live2dModel.ts` / `live2dViewer.ts` / "
              "`touchmanager.ts` / `lappwavfilehandler.ts`），以 **git submodule** 引官方 `CubismSdkForWeb`，"
              "配 Vite + oxlint/oxfmt + Nix flake。",
        analogy="它做的事跟 `easy-live2d` / `pixi-live2d-display` 同类（把官方 Web SDK 包一层），"
                "**不是 Editor 自动化** —— 上一辑已经确认「Editor 自动化」这条线被吃满了。"
                "它 1★，但工程配置（Nix + lint 全家桶 + submodule）比一般个人件规范。",
        warn="⚠️ 1★；**登记以免下轮当成新发现重复捡**。",
        ext=(45, "4.5/10", "submodule + Nix 的工程组织方式可参考"),
        use=(20, "2.0/10", "同类已被 easy-live2d 覆盖"),
        src="创建 2023-10-03 · 推送 2026-09-15 · 1★ · 许可不明 · TypeScript · 信源 [1320]",
    ),
    dict(
        nid="rpm38c21", name="Eviler —— 反着来：从 .moc3 里把 PSD 抠出来",
        url="https://github.com/goldimpact/Eviler",
        lang="Python", stars="12",
        tags=[("t-make", "建模"), ("t-warn", "逆向")],
        plain="**从 `.moc3` 里把 PSD 抠出来**的工具。README 特意强调「IT IS NOT USING ANY CODE FROM LIVE2D」"
              "（不依赖官方代码，纯逆向）。",
        analogy="别人做「图 → 模型」，它做「**模型 → 图**」——**用途是 reclaim 你已经买过的模型的源分层**，"
                "好拿去改、或拿去做别的尺寸。这是本辑唯一走反方向的工具。",
        warn="⚠️ ①推送停在 2025-03；②**许可不明（NOASSERTION）**；③**涉及逆向与授权边界**，仅登记，自己用之前想清楚。",
        ext=(35, "3.5/10", "方向独特但停更且许可不明"),
        use=(22, "2.2/10", "只能用来看思路；许可与逆向风险自担"),
        src="创建 2025-03-23 · 推送 2025-03-29 · 12★ · 许可不明 · Python · 信源 [1321]",
    ),
    dict(
        nid="rpm38c22", name="@laplace.live/three-live2d —— 把 Live2D 接到 three.js 的 WebGPU 渲染器",
        url="https://www.npmjs.com/package/@laplace.live/three-live2d",
        lang="npm", stars="0.10.1",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="面向 **three.js `WebGPURenderer`** 的 Live2D Cubism 渲染器（npm 包，`0.10.1` = 2026-10-03）。"
              "源码在 monorepo `github.com/laplace-live/persona` 的 `packages/three-live2d`。",
        analogy="**注意这不是 Pixi 系**。npm 上已有的 Live2D 轮子（`easy-live2d` / `pixi-live2d-display`）"
                "全是 Pixi 路线，这条走的是 **three.js + WebGPU** —— 说明 Web 侧开始分叉了。",
        warn="⚠️ 对本地 Ren'Py / 桌宠项目**直接不可用**（吃不了 npm）；登记是为了记「Web 侧的技术路线在分叉」这件事。",
        ext=(55, "5.5/10", "WebGPU 路线的新入口，方向意义大于当下可用性"),
        use=(15, "1.5/10", "纯 Web 前端；本地项目用不上"),
        src="npm latest 0.10.1 · 发布 2026-10-03 · 信源 [1322]",
    ),
    dict(
        nid="rpm38c23", name="XiaoMate —— 一个 app 同时挂 Live2D 与 3D 模型",
        url="https://github.com/oddmeta/xiaomate-desktop",
        lang="JavaScript", stars="4",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="桌宠应用（v2.0.7，原名 `Charlotty`）。**同一个 app 内挂 Live2D + VRM + GLB + GLTF 四类模型**："
              "Live2D 走 PIXI.js + Cubism 4，3D 走 Three.js，**按扩展名自动选渲染适配器**；"
              "首次启动默认加载 Hiyori。只发 **Windows 绿色便携包**（解压 `start.bat`）。",
        analogy="它记录的都是「**两种引擎同台**」的真实毛病：切换时旧画布残留遮挡新模型、"
                "VRM 播完动画卡 T-pose、Live2D 与 3D 尺寸不同步、长跑内存增长；"
                "并新增了**透明区域点击穿透**（只有角色剪影吃鼠标事件）。"
                "对「我到底只做 Live2D 还是也做 3D」这个决策有直接参考价值。",
        warn="⚠️ 4★、**未声明许可**；作者明确「在线功能依赖后端，Live2D/3D 展示与本地设置不依赖后端」。",
        ext=(60, "6.0/10", "2D/3D 双引擎同台的工程记录，坑点写得很具体"),
        use=(35, "3.5/10", "4★ 小件；双引擎同台的坑值得先读一遍"),
        src="创建 2026-09-16 · 推送 2026-10-04 · 4★ · 无许可证 · JavaScript · 信源 [1323]",
    ),
    dict(
        nid="rpm38c24", name="Cubism Editor 5.4 alpha2 手册 —— PSD 多层合并 + 数据单向门",
        url="https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html",
        lang="官方文档", stars="alpha2",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-warn", "有期限")],
        plain="官方 **5.4 alpha2 用户手册**（页首 `09/07/2026`）。两条关键正文："
              "① **PSD 导入增强** —— 以前必须「1 层 = 1 ArtMesh」，现在**多层可以合并当一个 ArtMesh**；"
              "合并图层组 / 合并蒙版 / 除尘从 Photoshop 脚本搬进编辑器（不想合并的图层组名前加 `*`、别带调整图层）；"
              "② **数据兼容** —— alpha2 存的文件**在 alpha1 与 5.3 之前打不开**，且**不保证未来 beta 能打开**。",
        analogy="**这是本辑对做模型的人最有用、同时也最需要小心的一条。**"
                "有用：PSD 不必再「一层一个网格」，拆图流程直接变了。"
                "小心：**alpha2 存过的东西是单向门** —— 论坛已有用户正好踩坑求回退，官方回复明确「不支持前向兼容」。"
                "做法：**另存副本再试，绝不覆盖原文件。**",
        warn="⏰ **alpha 可用期 2026-10-18 到期**（本辑发布时仅剩 7 天），过期后这一入口整体下线、只能等 beta。"
             "另：5.4 的**贴图集 auto layout 换了打包算法**，**同设置结果与 5.3 也不同**，别拿 5.3 的图集布局当基准。",
        ext=(70, "7.0/10", "PSD 合并是真的省事；但只在 alpha，且数据不可逆"),
        use=(50, "5.0/10", "10/18 前可试；正式工程请继续用 5.3.04"),
        src="官方手册 2026-09-07 · 可用期至 2026-10-18 · 信源 [1324]",
    ),
]

FOOTNOTES = [
    (1301, "https://github.com/MahouTechnologies/moc3-rs", "MahouTechnologies/moc3-rs",
     "6★ · Apache-2.0 · Rust · 创建 2023-09-14 · 推送 2026-08-15 · GitHub REST API 实测"),
    (1302, "https://github.com/Heonys/live2d-web", "Heonys/live2d-web",
     "2★ · MIT · TypeScript · 创建 2026-07-29 · 推送 2026-09-01 · GitHub REST API 实测"),
    (1303, "https://github.com/shinkuan/Waifuland", "shinkuan/Waifuland",
     "81★ · 无许可证 · C++ · 创建 2026-04-11 · 推送 2026-04-14 · GitHub REST API 实测"),
    (1304, "https://github.com/lTwTlol/Auto-live2D-beta", "lTwTlol/Auto-live2D-beta",
     "28★ · MIT · HTML · 创建 2026-08-20 · 推送 2026-08-30 · GitHub REST API 实测"),
    (1305, "https://github.com/Fenglin-Maple/AutoLive2d", "Fenglin-Maple/AutoLive2d",
     "19★ · Apache-2.0 · TypeScript · 创建 2026-07-24 · 推送 2026-07-24 · GitHub REST API 实测"),
    (1306, "https://github.com/zziying/ai-live2d-body", "zziying/ai-live2d-body",
     "46★ · 无许可证 · 文档 · 创建 2026-07-06 · 推送 2026-09-05 · GitHub REST API 实测"),
    (1307, "https://github.com/qiyueblues-design/zhuomianling", "qiyueblues-design/zhuomianling",
     "27★ · MIT · TypeScript · 创建 2026-07-09 · 推送 2026-08-26 · GitHub REST API 实测"),
    (1308, "https://github.com/kiyotakali/Miru", "kiyotakali/Miru",
     "175★ · Apache-2.0 · Python · 创建 2026-07-03 · 推送 2026-09-23 · GitHub REST API 实测"),
    (1309, "https://github.com/ice-only/localai-rag-live2d", "ice-only/localai-rag-live2d",
     "21★ · MIT · Python · 创建 2026-07-30 · 推送 2026-07-30 · GitHub REST API 实测"),
    (1310, "https://github.com/hhjk21/Firefly-Companion-AI-", "hhjk21/Firefly-Companion-AI-",
     "27★ · MIT · Python · 创建 2026-08-04 · 推送 2026-08-05 · 角色素材版权归米哈游 · GitHub REST API 实测"),
    (1311, "https://github.com/goodko/xiaozhi-ios", "goodko/xiaozhi-ios",
     "128★ · MIT · C++ · 创建 2026-08-10 · 推送 2026-08-10 · GitHub REST API 实测"),
    (1312, "https://github.com/ExpiredPopsicle/SnekStudio", "ExpiredPopsicle/SnekStudio",
     "418★ · GPL-3.0 · GDScript · 创建 2024-09-23 · 推送 2026-09-27 · 仅支持 VRM 0.x · GitHub REST API 实测"),
    (1313, "https://github.com/menglimi/astrbot_plugin_live_stream_companion",
     "menglimi/astrbot_plugin_live_stream_companion",
     "58★ · MIT · Python · 创建 2026-06-09 · 推送 2026-10-11 · GitHub REST API 实测"),
    (1314, "https://github.com/HanetakaChou/Brioche-Puppet", "HanetakaChou/Brioche-Puppet",
     "14★ · LGPL-3.0 · C++ · 创建 2025-02-06 · 推送 2026-07-21 · GitHub REST API 实测"),
    (1315, "https://github.com/LivXue/dsh-plugin-shop", "LivXue/dsh-plugin-shop",
     "1009★ · Apache-2.0 · TypeScript · 创建 2026-08-25 · 推送 2026-10-11 · GitHub REST API 实测"),
    (1316, "https://github.com/liguobao/ds-harness-remote", "liguobao/ds-harness-remote",
     "309★ · 无许可证 · TypeScript · 创建 2026-08-14 · 推送 2026-10-11 · GitHub REST API 实测"),
    (1317, "https://github.com/petabridge/memorizer", "petabridge/memorizer",
     "215★ · MIT · C# · 创建 2025-07-15 · 推送 2026-10-09 · GitHub REST API 实测"),
    (1318, "https://github.com/kennethlaw325/awesome-llm-knowledge-systems",
     "kennethlaw325/awesome-llm-knowledge-systems",
     "93★ · MIT · HTML · 创建 2026-04-06 · 推送 2026-09-15 · GitHub REST API 实测"),
    (1319, "https://github.com/wan-h/awesome-digital-human-live2d", "wan-h/awesome-digital-human-live2d",
     "2425★ · MIT · TypeScript · 创建 2024-05-15 · 推送 2026-05-18 · GitHub REST API 实测"),
    (1320, "https://github.com/madosuki/live2dManager", "madosuki/live2dManager",
     "1★ · 许可不明 · TypeScript · 创建 2023-10-03 · 推送 2026-09-15 · GitHub REST API 实测"),
    (1321, "https://github.com/goldimpact/Eviler", "goldimpact/Eviler",
     "12★ · 许可不明 · Python · 创建 2025-03-23 · 推送 2025-03-29 · GitHub REST API 实测"),
    (1322, "https://www.npmjs.com/package/@laplace.live/three-live2d", "@laplace.live/three-live2d",
     "npm latest 0.10.1 · 发布 2026-10-03 · 源码 monorepo github.com/laplace-live/persona · npm registry 实测"),
    (1323, "https://github.com/oddmeta/xiaomate-desktop", "oddmeta/xiaomate-desktop",
     "4★ · 无许可证 · JavaScript · 创建 2026-09-16 · 推送 2026-10-04 · GitHub REST API 实测"),
    (1324, "https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html",
     "Cubism Editor 5.4 alpha2 用户手册",
     "官方手册 · 页首 2026-09-07 · alpha 可用期至 2026-10-18 · 原始 HTML 已读"),
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

    desc = ('第三十三辑三路调研（gh 路 33 条 + 13 行边缘登记 / cn 路 19 条 / official 路 26 条），本版取 24 项，'
            '主题 **轮子开始分叉：一边继续攻 moc3，一边干脆绕开**。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/&lt;r&gt;` 逐条实测（主 agent 已复验全部 34 个候选仓库）。'
            '<strong>本辑主线：① 上一辑有人正面拆了「渲染 moc3」那堵墙，这一辑看点不在墙 —— '
            '而在墙两侧长出两丛完全不同的轮子：一丛继续攻格式（moc3-rs 纯 Rust 解析 / live2d-web 不用 Pixi 的 WebGL2 直渲 / '
            'Waifuland 的 Wayland 透明覆盖窗），另一丛干脆不碰 .moc3（Auto-live2D-beta 把分层 PSD 拖进浏览器自动绑定 / '
            'AutoLive2d 自带 rig 验收清单 / Eviler 反着来从 moc3 抠 PSD）；'
            '② 桌宠线第一次出现被写成架构主张的范式 —— 「你的桌宠不需要大脑」，'
            '不给新的 AI，而是给已有的 ta 装一具身体（ai-live2d-body ★46），配套「身体」侧供给本辑最密集'
            '（桌面灵 ★27 / Miru ★175 三平台安装包 / localai-rag-live2d ★21 / SnekStudio ★418 的 3D 对照）；'
            '③ 官方 5.4 alpha2 手册正文第一次读完：PSD 多层可合并当一个 ArtMesh（对做模型的人直接有用），'
            '但 alpha2 存的文件旧版打不开、未来 beta 也不保证 —— 是单向门，且可用期 2026-10-18 到期；'
            '④ 本辑的动手部分：静态核完 Inochi2D 的 Win11 兼容性（下载 MSI + PE 解析，无 OS 闸门，'
            '真实风险是 VC++ 运行库与 OpenGL 驱动）；Agent-desktop-pet 许可读清但装不上（要 CPython 3.12）；'
            '⑤ AI 开发侧：DSH 插件生态成形（dsh-plugin-shop ★1009 / ds-harness-remote ★309）。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm38g">',
             '      <div class="group-title" data-page-node-id="rpm38gt">🆕 第三十八版增补 · 轮子开始分叉：一边继续攻 moc3，一边干脆绕开 + 「你的桌宠不需要大脑」（24 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm38gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm38r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm38ra%s">%s</a> — %s</div>'
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
