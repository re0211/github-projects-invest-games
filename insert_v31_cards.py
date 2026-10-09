# -*- coding: utf-8 -*-
"""第三十一版增补：把第二十六辑「Live2D 制作专题」的 15 个条目登记进 index.html。

本辑候选池 86 条（GitHub 32 / 中文社媒 28 / 官方与海外 26），
其中 GitHub 路 32 个仓库全部走 `gh api repos/<r>` 实测（★ / 许可证 / 语言 / 推送日无一估算），
主 agent 另抽 5 个仓库复核（psd2live / renpy-live2d / CubismExternalEditMCP / Open-LLM-VTuber / gd_cubism），
数字与子 agent 一致。

本版取 15 项，优先「能省掉拆图与绑骨这两段人力的工具」+「接得进游戏/网页/直播的运行时」+「AI × Live2D」。

主线：**Live2D 的钱不是花在软件上，是花在拆图上** ——
官方免费版（30 参数 / 100 ArtMesh）对「只播预设表情和动作」够用，学生三年 PRO 折后约 ¥7,344；
真正贵的是把一张画完的立绘拆成能动的图层（有画师实录：画 7 小时、拆 14 小时）。
所以本辑把票投给「拆图/绑骨自动化」和「AI 补间」，而不是更贵的编辑器插件。

数据来源：2026-10-10 GitHub REST API 实测（`_r26/_r26_gh.md`）。
幂等：已存在标记则退出 0。
用法：python insert_v31_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1167"'
FIRST_NEW_FOOTNOTE = 1168
MARKER = "第三十一版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十版增补 2026-09-24',
    '共 1168 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十一版增补 2026-10-10',
    '共 1183 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm31c1", name="psd2live（PSD 直接出 Cubism 工程，省掉最贵的一段人力）",
        url="https://github.com/tsunehimatoi/psd2live",
        lang="Kotlin", stars="598",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="把分好层的 **PSD 直接转成 .cmo3 工程**并自动做一部分绑定，是「画完 → 能动」之间最短的那条路。"
              "Kotlin / ★598 / 最近推送 2026-10-09，本辑 GitHub 路里活跃度最高的一条。",
        analogy="手工做 Live2D 像把一张画**剪成几十片再逐片缝上线**；它是给你一把**自动裁剪+预缝线的机器**。"
                "省的不是技巧，是那 14 小时的重复劳动。",
        warn="**GPL-3.0**：你自己用没问题，若要把它的代码并进商业发行物，需要先想清楚传染性。",
        ext=(85, "8.5/10", "接在「分层规范 → 自动绑骨 → 导出」这条链的最前段；"
                           "与 AI 拆层工具（本组 See-through）串起来就是半自动流水线"),
        use=(78, "7.8/10", "建议路线：先用免费版 Cubism 手动做一次搞懂原理，再用它批量化；⚠️ 未本机实测"),
        src="最近推送 2026-10-09 · 598★ · GPL-3.0 · Kotlin · 信源 [1168]",
    ),
    dict(
        nid="rpm31c2", name="renpy-live2d（唯一正对 Ren'Py 的 Live2D 模块，但已停更）",
        url="https://github.com/asfdfdfd/renpy-live2d",
        lang="C", stars="89",
        tags=[("t-make", "动画"), ("t-warn", "已停更")],
        plain="给 Ren'Py 加 Live2D 支持的第三方模块（C 扩展）。★89 / **最近推送停在 2021-03-02**（已五年不动）。",
        analogy="这条的价值是**反面路标**：它证明「Ren'Py 接 Live2D」这条路早就有人走过，"
                "但今天**不该再走这条** —— Ren'Py 官方从 8.x 起已原生支持 Cubism 3/4/5（见本辑经验帖 §三）。",
        warn="**别直接装**：pushed_at 停在 2021，且官方方案已在文档里。留作「旧项目迁移」时的参考实现。",
        ext=(40, "4.0/10", "接口设计（在 Ren'Py 里怎么声明模型、怎么播动作）仍有参考价值"),
        use=(30, "3.0/10", "已停更 + 官方原生方案在位 → **不采用**，只登记"),
        src="最近更新 2026-04-09（推送停在 2021-03-02）· 89★ · NOASSERTION · C · 信源 [1169]",
    ),
    dict(
        nid="rpm31c3", name="CubismWebFramework（官方 Web 运行时，网页里放立绘的正路）",
        url="https://github.com/Live2D/CubismWebFramework",
        lang="TypeScript", stars="237",
        tags=[("t-make", "运行时"), ("t-ok", "持续更新")],
        plain="Live2D **官方**的 TypeScript/Web 运行时：把 .moc3 模型加载进网页、播动作、跟随鼠标。"
              "★237 / 最近更新 2026-10-06。",
        analogy="做网页版立绘时，它是**官方出的发动机**；社区那些「看板娘挂件」都是在它上面套的壳。",
        ext=(80, "8.0/10", "任何 Web 场景（官网角色、itch.io 页面、Ren'Py Web 版）都绕不开它"),
        use=(70, "7.0/10", "⚠️ **Cubism Core 不在 GitHub**：只 clone 这个仓库编译不出能跑的东西，"
                           "必须去官网下载分发包（本辑官方路核实）"),
        src="最近更新 2026-10-06 · 237★ · NOASSERTION · TypeScript · 信源 [1170]",
    ),
    dict(
        nid="rpm31c4", name="CubismUnityComponents（官方 Unity SDK 部件，旧仓库名已 404）",
        url="https://github.com/Live2D/CubismUnityComponents",
        lang="C#", stars="263",
        tags=[("t-make", "运行时"), ("t-ok", "持续更新")],
        plain="Live2D 官方 Unity SDK 的组件仓库。★263 / 最近更新 2026-09-29。",
        analogy="网上教程里到处引用的 `Live2D/CubismSdkForUnity` **现在已经是 404** —— 官方把 SDK 拆成了若干部件仓库。"
                "照着老教程找仓库，第一步就撞墙。",
        warn="**避坑**：SDK 已改名拆分，且 Cubism Core 需官网单独下载；老教程的 clone 命令基本都失效。",
        ext=(72, "7.2/10", "Unity 是 Live2D 最成熟的落点，组件齐全（口型、视线跟随、动作淡入淡出）"),
        use=(62, "6.2/10", "只在做 Unity 项目时才需要；做 Ren'Py / Web 的用不到"),
        src="最近更新 2026-09-29 · 263★ · NOASSERTION · C# · 信源 [1171]",
    ),
    dict(
        nid="rpm31c5", name="pixi-live2d-display（把 Live2D 塞进 PixiJS，社区事实标准）",
        url="https://github.com/guansss/pixi-live2d-display",
        lang="TypeScript", stars="1507",
        tags=[("t-make", "运行时"), ("t-warn", "低频更新")],
        plain="在 **PixiJS（2D 网页渲染引擎）**里显示并驱动 Live2D 模型的插件，★1507 / MIT。"
              "社区里做网页 Live2D 游戏最常用的一个。",
        analogy="官方 Web 框架是发动机，它是**装好座椅和方向盘的整车** —— 你只管踩油门（写播哪段动作）。",
        warn="最近推送 2024-08-20，但 ★1507 的存量说明生态还在用；MIT 比多数同类宽松。",
        ext=(82, "8.2/10", "PixiJS 生态可直接接粒子、滤镜、UI，做 2D 网页游戏时一层搞定"),
        use=(75, "7.5/10", "MIT + 文档全 + 用的人多 → 网页路线的**首选**；⚠️ 未本机实测"),
        src="最近更新 2026-10-08（推送 2024-08-20）· 1507★ · MIT · TypeScript · 信源 [1172]",
    ),
    dict(
        nid="rpm31c6", name="gd_cubism（Godot 4 的 Live2D 原生插件）",
        url="https://github.com/MizunagiKB/gd_cubism",
        lang="C++", stars="301",
        tags=[("t-make", "运行时"), ("t-ok", "持续更新")],
        plain="让 **Godot 4** 直接加载和驱动 Cubism 3/4 模型的 GDExtension 插件（C++）。★301 / 推送 2025-04-01。",
        analogy="Godot 官方一直没有 Live2D 支持，它是社区补上的那块拼图 —— "
                "如果你想用 Godot 做带 Live2D 立绘的视觉小说，这是**唯一像样的选项**。",
        warn="**NOASSERTION**（许可证不明确）：商用前必须去仓库确认授权条款，别默认 MIT。",
        ext=(70, "7.0/10", "Godot 4 是眼下最热的开源引擎，插件 + 引擎全链路开源，可改造空间大"),
        use=(55, "5.5/10", "只在你选 Godot 时才成立；我们是 Ren'Py 路线 → 参考级"),
        src="最近更新 2026-10-03（推送 2025-04-01）· 301★ · NOASSERTION · C++ · 信源 [1173]",
    ),
    dict(
        nid="rpm31c7", name="inochi-creator（Live2D 的开源平替，D 语言写的）",
        url="https://github.com/Inochi2D/inochi-creator",
        lang="D", stars="1240",
        tags=[("t-mod", "替代方案"), ("t-ok", "持续更新")],
        plain="**Inochi2D** 的官方创作工具：一套与 Live2D 思路相同（图层+网格变形）但**完全开源**的方案，"
              "BSD-2-Clause / ★1240。",
        analogy="Live2D 是 Adobe  Photoshop（贵、闭源、行业标准）；Inochi2D 是它的**免费开源远亲**，"
                "文件格式不同、生态小很多，但**没有授权费这回事**。",
        warn="生态与教程量级远小于 Live2D；想接 Ren'Py 得自己写一层（没有现成模块）。",
        ext=(68, "6.8/10", "BSD-2 授权 + 格式公开 → 想做**商业发行且完全不想谈授权**时，它是唯一干净的路"),
        use=(45, "4.5/10", "教程少、工具链窄；建议**先学会 Live2D 的思路再来看它**，迁移成本才看得清"),
        src="最近更新 2026-10-08 · 1240★ · BSD-2-Clause · D · 信源 [1174]",
    ),
    dict(
        nid="rpm31c8", name="CubismExternalEditMCP（让 AI 通过 MCP 直接操作 Cubism）",
        url="https://github.com/nana7chi/CubismExternalEditMCP",
        lang="Python", stars="33",
        tags=[("t-make", "AI × 建模"), ("t-ok", "已核实待试")],
        plain="一个 **MCP 服务器**：把 Cubism Editor 的操作暴露给 AI 客户端，让模型能读工程结构、改参数、"
              "批量做重复操作。★33（很新）/ MIT / Python / 推送 2026-08-03。",
        analogy="以前让 AI 帮你做 Live2D，只能是**它说你做**（复制粘贴教程）；"
                "有了 MCP 是**它伸手进软件里做** —— 这才是「AI 建模」该有的形态。",
        warn="⚠️ 本辑中文路有一手反例：有人问 AI 解 Live2D 的坑，AI **持续编造软件里根本没有的选项**"
             "（见 `M-0028`）。让 AI 操作软件前，先确认它调用的**是真接口，不是想象的接口**。",
        ext=(78, "7.8/10", "MCP 是可组合的：接上自家 Ollama 就能本地跑，不必依赖云端模型"),
        use=(58, "5.8/10", "★33 说明还在很早期；**值得盯**，但现在别押宝（且需 Cubism Pro 才能导出）"),
        src="最近推送 2026-08-03 · 33★ · MIT · Python · 信源 [1175]",
    ),
    dict(
        nid="rpm31c9", name="ComfyUI-See-through（AI 把一张平图拆成带遮挡补全的分层）",
        url="https://github.com/jtydhr88/ComfyUI-See-through",
        lang="Jupyter Notebook", stars="832",
        tags=[("t-make", "AI × 建模"), ("t-ok", "持续更新")],
        plain="**See-through**（SIGGRAPH 2026）的 ComfyUI 节点封装：输入单张插画，"
              "输出**分层且补好了被遮挡部分**的图层栈。★832 / 最近更新 2026-10-09。",
        analogy="拆图最痛苦的不是「切开」，是**切开后头发后面的脸得自己补画**。"
                "它补的正是这一刀 —— 这也是全自动 Live2D 流水线里唯一刚需的 AI 环节。",
        ext=(88, "8.8/10", "ComfyUI 节点 = 可插进任意工作流；与本组 psd2live 串起来就是「平图 → 工程」"),
        use=(72, "7.2/10", "⚠️ 需要能跑 ComfyUI 的显卡（16GB 内存机器可以，慢）；建议先跑官方 demo 验证效果"),
        src="最近更新 2026-10-09 · 832★ · NOASSERTION · Jupyter Notebook · 信源 [1176]",
    ),
    dict(
        nid="rpm31c10", name="AnimeSR（二次元立绘超分，把小图修成大图）",
        url="https://github.com/TencentARC/AnimeSR",
        lang="Python", stars="373",
        tags=[("t-make", "AI × 素材"), ("t-warn", "低频更新")],
        plain="腾讯 ARC 的**二次元图像超分**：把低分辨率动漫图修复放大。★373 / 推送停在 2023-08-18。",
        analogy="Live2D 对纹理尺寸很敏感（免费版单张上限 2048）。素材不够大时，"
                "它是**把图放大又不变糊**的那一档工具。",
        warn="推送停在 2023，属「成熟但不再更新」；对 Windows 用户环境配置有一定门槛。",
        ext=(60, "6.0/10", "超分是素材管线的通用一环，不只服务 Live2D（UI、立绘、CG 都用得上）"),
        use=(52, "5.2/10", "非必需：**画的时候就按 2048 以上画**比事后超分更省事"),
        src="最近更新 2026-10-06（推送 2023-08-18）· 373★ · NOASSERTION · Python · 信源 [1177]",
    ),
    dict(
        nid="rpm31c11", name="l2d-widget（一行代码把看板娘挂上网页，MIT）",
        url="https://github.com/hacxy/l2d-widget",
        lang="TypeScript", stars="639",
        tags=[("t-make", "网页挂件"), ("t-ok", "持续更新")],
        plain="网页**看板娘挂件**：一个函数调用把 Live2D 模型放到页面角落，会跟随鼠标、可换装。"
              "★639 / **MIT** / 最近更新 2026-10-09。",
        analogy="同类最有名的 `stevenjoezhang/live2d-widget` 有 ★10986，但它是 **GPL-3.0** ——"
                "往商业站点里挂会有传染性。这条是**同功能的 MIT 替代**。",
        ext=(65, "6.5/10", "适合做游戏官网/itch.io 页面的角色；换模型、换对话都能改"),
        use=(70, "7.0/10", "MIT + 轻量 + 活跃 → 想给自己的游戏站加个会动的角色时**首选**"),
        src="最近更新 2026-10-09 · 639★ · MIT · TypeScript · 信源 [1178]",
    ),
    dict(
        nid="rpm31c12", name="live2d-viewer-web（拖进去就能看的模型检查器）",
        url="https://github.com/guansss/live2d-viewer-web",
        lang="TypeScript", stars="175",
        tags=[("t-make", "工具"), ("t-warn", "低频更新")],
        plain="**网页版 Live2D 模型查看器**：把模型文件拖进浏览器就能看动作、表情、参数，不用开 Cubism。"
              "★175 / MIT / 推送 2023-02-03。",
        analogy="它是 Live2D 界的**图片查看器** —— 你不会用它修图，但你会天天用它「先看看这模型对不对」。",
        ext=(58, "5.8/10", "接模型管理/批量预览时可直接复用其渲染内核"),
        use=(66, "6.6/10", "零安装、MIT、够用 → **建议装一个备用**；⚠️ 推送停在 2023，功能已够"),
        src="最近更新 2026-09-29（推送 2023-02-03）· 175★ · MIT · TypeScript · 信源 [1179]",
    ),
    dict(
        nid="rpm31c13", name="UnityLive2DExtractor（从 Unity 游戏里提取 Live2D 资源）",
        url="https://github.com/Perfare/UnityLive2DExtractor",
        lang="C#", stars="634",
        tags=[("t-mod", "逆向/资产"), ("t-warn", "低频更新")],
        plain="从 **Unity 打包好的游戏**里把 Live2D 的 .moc3 / 贴图 / 动作文件**还原出来**的工具。"
              "★634 / MIT / 推送 2023-05-17。",
        analogy="跟你解包 73 款游戏是一个工种 —— 只是这次的目标换成了**别人的 Live2D 模型**。",
        warn="⚠️ **只用于学习你自己有权处理的资源**。提取他人作品的模型再分发，授权上是另一回事。",
        ext=(62, "6.2/10", "作为「看别人怎么分层、怎么绑骨」的学习样本来源，价值高于工具本身"),
        use=(60, "6.0/10", "对口现有技能（解包）；⚠️ 用途边界要自己守住"),
        src="最近更新 2026-10-05（推送 2023-05-17）· 634★ · MIT · C# · 信源 [1180]",
    ),
    dict(
        nid="rpm31c14", name="Open-LLM-VTuber（本地大模型 + Live2D 的 AI 虚拟主播）",
        url="https://github.com/Open-LLM-VTuber/Open-LLM-VTuber",
        lang="Python", stars="14025",
        tags=[("t-make", "AI × Live2D"), ("t-ok", "持续更新")],
        plain="**本辑 ★ 最高**的一条：本地跑的 AI 虚拟主播，前端是 Live2D，后端可接**本地 Ollama** 等推理后端，"
              "带语音识别与合成。★14025 / Python / 最近更新 2026-10-09。",
        analogy="它把「本地模型 + 会动的立绘 + 能听会说」这三件事**整套拼好了** ——"
                "即便你不做 VTuber，这也是**本地 LLM 怎么驱动一个角色**的最佳现成参考。",
        warn="**NOASSERTION**：许可证未在 GitHub 上标明，商用前必须核实。",
        ext=(90, "9.0/10", "前端调度、动作触发、语音流水线都可拆出来复用；与本地 Ollama 路线同构"),
        use=(80, "8.0/10", "★14025 + 活跃 + 可接本地模型 → 本辑**最该先跑一遍**的一条"),
        src="最近更新 2026-10-09（推送 2026-05-15）· 14025★ · NOASSERTION · Python · 信源 [1181]",
    ),
    dict(
        nid="rpm31c15", name="facial-landmarks-for-cubism（用摄像头驱动 Live2D 表情）",
        url="https://github.com/adrianiainlam/facial-landmarks-for-cubism",
        lang="C++", stars="75",
        tags=[("t-make", "面捕"), ("t-ok", "已核实待试")],
        plain="把**摄像头人脸关键点**映射成 Cubism 参数，用自己的表情驱动模型。★75 / MIT / C++。",
        analogy="VTube Studio 那套「你眨眼它也眨眼」的能力，拆开来看就是这个 —— "
                "它给你的是**最小可改的实现**，不是黑盒软件。",
        ext=(70, "7.0/10", "接上以后可长出自家面捕方案；也可降级成「录音 → 口型」的轻量版"),
        use=(58, "5.8/10", "★75 属小众但干净（MIT）；做 VTuber 或直播时值得挖，做单机游戏用不上"),
        src="最近更新 2026-07-11 · 75★ · MIT · C++ · 信源 [1182]",
    ),
]

FOOTNOTES = [
    (1168, "https://github.com/tsunehimatoi/psd2live", "tsunehimatoi/psd2live",
     "598★ · GPL-3.0 · Kotlin · 2026-10-09 · GitHub REST API 实测"),
    (1169, "https://github.com/asfdfdfd/renpy-live2d", "asfdfdfd/renpy-live2d",
     "89★ · NOASSERTION · C · 推送 2021-03-02 · GitHub REST API 实测"),
    (1170, "https://github.com/Live2D/CubismWebFramework", "Live2D/CubismWebFramework",
     "237★ · NOASSERTION · TypeScript · 2026-10-06 · GitHub REST API 实测"),
    (1171, "https://github.com/Live2D/CubismUnityComponents", "Live2D/CubismUnityComponents",
     "263★ · NOASSERTION · C# · 2026-09-29 · GitHub REST API 实测"),
    (1172, "https://github.com/guansss/pixi-live2d-display", "guansss/pixi-live2d-display",
     "1507★ · MIT · TypeScript · 推送 2024-08-20 · GitHub REST API 实测"),
    (1173, "https://github.com/MizunagiKB/gd_cubism", "MizunagiKB/gd_cubism",
     "301★ · NOASSERTION · C++ · 推送 2025-04-01 · GitHub REST API 实测"),
    (1174, "https://github.com/Inochi2D/inochi-creator", "Inochi2D/inochi-creator",
     "1240★ · BSD-2-Clause · D · 2026-10-08 · GitHub REST API 实测"),
    (1175, "https://github.com/nana7chi/CubismExternalEditMCP", "nana7chi/CubismExternalEditMCP",
     "33★ · MIT · Python · 推送 2026-08-03 · GitHub REST API 实测"),
    (1176, "https://github.com/jtydhr88/ComfyUI-See-through", "jtydhr88/ComfyUI-See-through",
     "832★ · NOASSERTION · Jupyter Notebook · 2026-10-09 · GitHub REST API 实测"),
    (1177, "https://github.com/TencentARC/AnimeSR", "TencentARC/AnimeSR",
     "373★ · NOASSERTION · Python · 推送 2023-08-18 · GitHub REST API 实测"),
    (1178, "https://github.com/hacxy/l2d-widget", "hacxy/l2d-widget",
     "639★ · MIT · TypeScript · 2026-10-09 · GitHub REST API 实测"),
    (1179, "https://github.com/guansss/live2d-viewer-web", "guansss/live2d-viewer-web",
     "175★ · MIT · TypeScript · 推送 2023-02-03 · GitHub REST API 实测"),
    (1180, "https://github.com/Perfare/UnityLive2DExtractor", "Perfare/UnityLive2DExtractor",
     "634★ · MIT · C# · 推送 2023-05-17 · GitHub REST API 实测"),
    (1181, "https://github.com/Open-LLM-VTuber/Open-LLM-VTuber", "Open-LLM-VTuber/Open-LLM-VTuber",
     "14025★ · NOASSERTION · Python · 2026-10-09 · GitHub REST API 实测"),
    (1182, "https://github.com/adrianiainlam/facial-landmarks-for-cubism",
     "adrianiainlam/facial-landmarks-for-cubism",
     "75★ · MIT · C++ · 2026-07-11 · GitHub REST API 实测"),
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

    desc = ('第二十六辑三路调研（GitHub 32 / 中文社媒 28 / 官方与海外 26），本版取 15 项，'
            '主题 **Live2D 制作**：优先「省拆图与绑骨人力」+「接得进游戏/网页/直播的运行时」+「AI × Live2D」。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测，主 agent 另抽 5 个复核。'
            '<strong>本辑主线：Live2D 的钱不是花在软件上，是花在拆图上</strong> ——'
            '官方免费版（30 参数 / 100 ArtMesh）对「只播预设表情和动作」够用；'
            '真正贵的是把画完的立绘拆成能动的图层（画师实录：画 7 小时、拆 14 小时）。')

    block = ['    <div class="group" data-page-node-id="rpm31g">',
             '      <div class="group-title" data-page-node-id="rpm31gt">🆕 第三十一版增补 · Live2D 制作与立绘动效（15 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm31gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm31r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm31ra%s">%s</a> — %s</div>'
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
