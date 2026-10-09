# 第二十六辑 · Live2D 制作专题 —— GitHub 路

> 调研日期：2026-10-10
> 主题：Live2D（Cubism）制作与工程化开源项目
> 基准用户画像：16GB 内存 Windows 学生，做 Ren'Py 视觉小说，想把立绘做成会动的 Live2D，本地跑 Ollama

## 一、条目（32 条）

### 01. psd2live（tsunehimatoi/psd2live）
- 链接：https://github.com/tsunehimatoi/psd2live
- 核实：⭐ 598 · GPL-3.0 · Kotlin · updated_at 2026-10-09（命令：`gh api repos/tsunehimatoi/psd2live`）
- 一句话：把分层好的 PSD 直接变成可编辑的 Live2D 模型——自动绑骨、生成网格和变形器、加物理和动画，最后导出 .cmo3 / .moc3。
- 可拓展性：这是"让立绘动起来"这条链上最省人工的一环。可以跟拆层工具（ComfyUI-See-through）串成流水线：一张立绘 → 分层 PSD → cmo3 → 用官方 Cubism Editor 精修 → moc3 → 挂到 Ren'Py 或网页上。注意 GPL-3.0 有传染性，作品要闭源发售的话得先想清楚。
- 实用性：落地（自动绑骨是刚需；许可要提前确认）

### 02. umamo（umamoorg/umamo）
- 链接：https://github.com/umamoorg/umamo
- 核实：⭐ 148 · GPL-3.0 · Kotlin · updated_at 2026-10-09（命令：`gh api repos/umamoorg/umamo`）
- 一句话：一个开源、跨平台的 2D 木偶绑定编辑器，明确定位成 Live2D Cubism Editor 的替代品，对手写笔和触屏有一等支持。
- 可拓展性：Cubism Editor 免费版有功能限制、Pro 版要钱，学生党这是条不用掏钱的路。Kotlin 写的跨平台项目，Windows 上能跑。项目很新（star 只有 148），当成"未来可选项"盯着比现在就上更稳。
- 实用性：参考（方向对，成熟度不够）

### 03. renpy-live2d（asfdfdfd/renpy-live2d）
- 链接：https://github.com/asfdfdfd/renpy-live2d
- 核实：⭐ 89 · NOASSERTION · C · updated_at 2026-04-09，pushed_at 2021-03-02（命令：`gh api repos/asfdfdfd/renpy-live2d`）
- 一句话：给 Ren'Py 写的 Live2D 模块，让 Ren'Py 能直接加载并驱动 Cubism 模型。
- 可拓展性：正对画像——做视觉小说想让立绘动起来，这是最短路径（Ren'Py 原生吃它，不用绕网页）。但要注意最后一次提交代码是 2021-03-02，年代久远，接新版 Ren'Py / 新版 Cubism 5 大概率要自己动手改，而且许可没写清。
- 实用性：参考（唯一对口的 Ren'Py 方案，但基本停更）

### 04. pixi-live2d-display（guansss/pixi-live2d-display）
- 链接：https://github.com/guansss/pixi-live2d-display
- 核实：⭐ 1507 · MIT · TypeScript · updated_at 2026-10-08，pushed_at 2024-08-20（命令：`gh api repos/guansss/pixi-live2d-display`）
- 一句话：一个 PixiJS 插件，在网页里显示任意版本（Cubism 2/3/4）的 Live2D 模型。
- 可拓展性：网页方案里生态最成熟的一个，MIT 可商用，216 个 fork。Ren'Py 不直接吃 JS，但可以拿它做一个本地预览器调模型，或者做游戏的网页端宣传页。注意主分支代码停在 2024 年。
- 实用性：落地（网页侧的事实标准）

### 05. CubismWebFramework（Live2D/CubismWebFramework）
- 链接：https://github.com/Live2D/CubismWebFramework
- 核实：⭐ 237 · NOASSERTION · TypeScript · updated_at 2026-10-06（命令：`gh api repos/Live2D/CubismWebFramework`）
- 一句话：Live2D 官方的网页端 SDK 框架源码（Cubism SDK for Web 的核心）。
- 可拓展性：官方出品，所有第三方网页库（pixi-live2d-display、easy-live2d）都是架在它上面的。许可显示 NOASSERTION，是因为官方 SDK 用的是 Live2D 自己的协议（免费版和 Pro 版权利不同），真要商用得去读它的条款。
- 实用性：参考（底座，一般间接用）

### 06. CubismWebSamples（Live2D/CubismWebSamples）
- 链接：https://github.com/Live2D/CubismWebSamples
- 核实：⭐ 392 · NOASSERTION · 语言为空 · updated_at 2026-10-09（命令：`gh api repos/Live2D/CubismWebSamples`）
- 一句话：官方 Web SDK 的示例工程，带能直接跑起来的 Demo。
- 可拓展性：上手最快的材料——先把官方 sample 跑通，再把里面的模型换成自己的。仓库语言字段为空（主要是示例和资源合集，不是单一语言的代码库）。官方 SDK 许可同上。
- 实用性：落地（照着抄最快）

### 07. CubismUnityComponents（Live2D/CubismUnityComponents）
- 链接：https://github.com/Live2D/CubismUnityComponents
- 核实：⭐ 263 · NOASSERTION · C# · updated_at 2026-09-29（命令：`gh api repos/Live2D/CubismUnityComponents`）
- 一句话：官方给 Unity 用的 Cubism 组件集（"Open Cubism Components for Unity"）。
- 可拓展性：想在 Unity 里做 Live2D 立绘或虚拟主播，这是标准起点。对 Ren'Py 用户来说是旁路，但它的代码结构（怎么用参数驱动模型、怎么管动作和表情）值得读一遍，理解了再回头看别的实现会轻松很多。
- 实用性：参考（不直接用，但可读）

### 08. easy-live2d（Panzer-Jack/easy-live2d）
- 链接：https://github.com/Panzer-Jack/easy-live2d
- 核实：⭐ 213 · MIT · TypeScript · updated_at 2026-10-03（命令：`gh api repos/Panzer-Jack/easy-live2d`）
- 一句话：把 Live2D 封装成"操作起来跟操控一个 Pixi sprite 一样简单"，基于 Pixi.js 的轻量网页 SDK。
- 可拓展性：中文 README，对国内学生友好，MIT 授权。想在网页里快速挂一个会动的立绘，几行代码搞定；也能挂到 OBS 的浏览器源里当直播挂件。
- 实用性：落地（轻量、中文、MIT）

### 09. gd_cubism（MizunagiKB/gd_cubism）
- 链接：https://github.com/MizunagiKB/gd_cubism
- 核实：⭐ 301 · NOASSERTION · C++ · updated_at 2026-10-03，pushed_at 2025-04-01（命令：`gh api repos/MizunagiKB/gd_cubism`）
- 一句话：Godot 引擎的非官方 Live2D 播放器插件。
- 可拓展性：Ren'Py 做对话演出很舒服，但要做复杂演出会受限；如果哪天想换 Godot，这是现成的桥。它也证明了 Cubism 原生 SDK 可以被第三方引擎接进去——Ren'Py 那条路在技术上同样成立。
- 实用性：参考（换引擎时才用得上）

### 10. inochi-creator（Inochi2D/inochi-creator）
- 链接：https://github.com/Inochi2D/inochi-creator
- 核实：⭐ 1240 · BSD-2-Clause · D · updated_at 2026-10-08，pushed_at 2025-06-16（命令：`gh api repos/Inochi2D/inochi-creator`）
- 一句话：Inochi2D 官方的绑定（rigging）应用软件，一个完全开源的 2D 木偶动画编辑器。
- 可拓展性：BSD-2-Clause 比 GPL 宽松太多，商用基本无负担。这是 Live2D 之外的"全开源路线"：编辑器、文件格式、运行时全都有，不用看 Cubism 的脸色。缺点是用 D 语言写的，想二次开发门槛高。
- 实用性：参考（想绕开 Cubism 许可时的首选备选）

### 11. nijigenerate（nijigenerate/nijigenerate）
- 链接：https://github.com/nijigenerate/nijigenerate
- 核实：⭐ 313 · BSD-2-Clause · D · updated_at 2026-10-09（命令：`gh api repos/nijigenerate/nijigenerate`）
- 一句话：nijilive 木偶格式的开源编辑器，技术源自 Inochi2D v0.8，可以给游戏或 VTuber 做模型。
- 可拓展性：Inochi2D 主线迭代慢，这个是活跃的分叉（当天还在推代码）。下面第 13 条 image2live2d 那条链路输出的就是 nijilive 的 .inp 格式——两者是一对。
- 实用性：参考（开源替代路线里最活跃的一支）

### 12. iki（zeikar/iki）
- 链接：https://github.com/zeikar/iki
- 核实：⭐ 14 · MIT · TypeScript · updated_at 2026-10-09（命令：`gh api repos/zeikar/iki`）
- 一句话：自称"AI 也能搭的开源 Live2D 替代"——MIT 授权的网页 2D 木偶引擎，.iki 格式开放，自带 AI 自动绑骨和 Claude Code 插件。
- 可拓展性：思路很新：绑骨这件事不让人干，让 AI agent 干，格式开放所以不怕被锁。star 只有 14、项目很早期，现在不能指望它出活，但方向跟"AI × Live2D"完全对上，值得加进观察列表。
- 实用性：参考（太早期，只观察）

### 13. image2live2d（Wzhang3912/image2live2d）
- 链接：https://github.com/Wzhang3912/image2live2d
- 核实：⭐ 43 · Apache-2.0 · Python · updated_at 2026-10-09（命令：`gh api repos/Wzhang3912/image2live2d`）
- 一句话：把分好层的角色立绘转成可复用的 2D 木偶，同时能输出 nijilive 的 .inp 和 Live2D 的 .moc3 两种格式。
- 可拓展性：Apache-2.0 很宽松，Python 写的（本地跑 Ollama 的人对这套工具链熟）。是"一张图 → 可动模型"这条链上少见的能同时吐两种格式的——可以先用免费开源的 nijilive 路线练手，验证通过了再走 Live2D。
- 实用性：落地（许可友好 + Python 栈）

### 14. PuppetLoom（CheshireMew/PuppetLoom）
- 链接：https://github.com/CheshireMew/PuppetLoom
- 核实：⭐ 245 · AGPL-3.0 · TypeScript · updated_at 2026-10-06（命令：`gh api repos/CheshireMew/PuppetLoom`）
- 一句话：把分层角色 PSD 变成"可自动制作、可验证、可继续校准"的 2D 动态角色（README 原文），Electron 桌面应用 + CLI，带 Windows 支持。
- 可拓展性：topics 里带 live2d、psd、codex-skill、windows——是给"AI agent 自动做立绘"设计的，跟第 12 条 iki 一个路子但更成熟（245 star）。不用开 Cubism Editor 就能处理 PSD 分层。AGPL-3.0 传染性强，商用要谨慎。
- 实用性：参考（思路好，许可偏重）

### 15. ComfyUI-See-through（jtydhr88/ComfyUI-See-through）
- 链接：https://github.com/jtydhr88/ComfyUI-See-through
- 核实：⭐ 832 · NOASSERTION · Jupyter Notebook · updated_at 2026-10-09（命令：`gh api repos/jtydhr88/ComfyUI-See-through`）
- 一句话：把 See-through 包装成 ComfyUI 插件——See-through 能把单张动漫插画拆成带深度顺序、可操控的 2.5D 分层模型，拆完就能接 Live2D 流程。
- 可拓展性：整条 AI 流水线的第一环。ComfyUI 本地部署、8G 显存就能试，学生党负担得起。拆出来的层再喂给 psd2live 绑骨，就能做到"一张图进，一个会动的模型出"。许可没标，商用前要问清楚。
- 实用性：落地（拆层是这个专题里最卡人的一步）

### 16. AnimeSR（TencentARC/AnimeSR）
- 链接：https://github.com/TencentARC/AnimeSR
- 核实：⭐ 373 · NOASSERTION · Python · updated_at 2026-10-06，pushed_at 2023-08-18（命令：`gh api repos/TencentARC/AnimeSR`）
- 一句话：腾讯 ARC 的动漫专用超分辨率，论文 "Learning Real-World Super-Resolution Models for Animation Videos" 的官方代码。
- 可拓展性：立绘分辨率不够时，先超分再拆层，后面每一步质量都会好一截。代码 2023 年后没再推，但权重和思路都能用；嫌重可以换成 Real-CUGAN 或 waifu2x（更省显存）。
- 实用性：参考（有用，但不是必选项）

### 17. UnityLive2DExtractor（Perfare/UnityLive2DExtractor）
- 链接：https://github.com/Perfare/UnityLive2DExtractor
- 核实：⭐ 634 · MIT · C# · updated_at 2026-10-05，pushed_at 2023-05-17（命令：`gh api repos/Perfare/UnityLive2DExtractor`）
- 一句话：从 Unity 游戏里把 Live2D Cubism 3 的模型资源提出来。
- 可拓展性：学绑骨最快的方式是拆一个别人做好的现成模型看——网格怎么切、参数怎么配、动作怎么排。工具本身是 MIT，但拿去拆商业游戏的资源有法律风险，只能当学习用途。
- 实用性：参考（学结构用，别用于分发）

### 18. Eviler（goldimpact/Eviler）
- 链接：https://github.com/goldimpact/Eviler
- 核实：⭐ 12 · NOASSERTION · Python · updated_at 2026-04-15，pushed_at 2025-03-29（命令：`gh api repos/goldimpact/Eviler`）
- 一句话：从 .moc3 成品文件里把 PSD 图层抠出来（作者声明没使用任何 Live2D 的代码）。
- 可拓展性：反向工程方向——只有成品模型、把源工程弄丢了的时候能救回分层图。star 很少、许可没标，属于应急工具而不是日常工具。
- 实用性：不采用（许可不明，且只在丢文件时才用得上）

### 19. lpk2moc3（Arkueid/lpk2moc3）
- 链接：https://github.com/Arkueid/lpk2moc3
- 核实：⭐ 18 · NOASSERTION · Python · updated_at 2026-04-13，archived=true（命令：`gh api repos/Arkueid/lpk2moc3`）
- 一句话：带图形界面的工具，从 .lpk 文件里提取 moc3 模型（.lpk 是 Cubism Editor 的工程打包格式）。
- 可拓展性：能解包工程文件本身有价值——拿到别人的 .lpk 就能看完整工程结构。但仓库已被作者归档（archived=true），代码停在 2023 年，许可也没写。
- 实用性：不采用（已归档 + 许可不明）

### 20. moc3ingbird（OpenL2D/moc3ingbird）
- 链接：https://github.com/OpenL2D/moc3ingbird
- 核实：⭐ 98 · NOASSERTION · C++ · updated_at 2026-08-17，archived=true（命令：`gh api repos/OpenL2D/moc3ingbird`）
- 一句话：针对 Live2D 的 "MOC3ingbird" 漏洞利用代码（CVE-2023-27566）。
- 可拓展性：这是个安全研究样本，证明 moc3 文件可以被做成恶意载荷的意义大于工具本身——**提醒价值**：网上随便下的 .moc3 / .cmo3 模型，别在主力机器上乱开（第 31 条那种模型合集尤其要注意）。仓库已归档。
- 实用性：不采用（安全 PoC，只当警示）

### 21. live2d-widget（stevenjoezhang/live2d-widget）
- 链接：https://github.com/stevenjoezhang/live2d-widget
- 核实：⭐ 10986 · GPL-3.0 · TypeScript · updated_at 2026-10-09（命令：`gh api repos/stevenjoezhang/live2d-widget`）
- 一句话：博客"看板娘"挂件的老牌方案，一段脚本就能在网页角上放一个会动的 Live2D 小人。
- 可拓展性：2603 个 fork，生态最大，配套模型资源也最多（可配 xiazeyu/live2d-widget-models）。可以直接搬到游戏的官网或 itch.io 页面当活立绘。GPL-3.0 有传染性，商业项目慎用。
- 实用性：落地（网页挂件的默认选择）

### 22. l2d-widget（hacxy/l2d-widget）
- 链接：https://github.com/hacxy/l2d-widget
- 核实：⭐ 639 · MIT · TypeScript · updated_at 2026-10-09（命令：`gh api repos/hacxy/l2d-widget`）
- 一句话：一次函数调用就能在任意网页上放一个 Live2D 角色，零框架依赖。
- 可拓展性：跟第 21 条干一样的事，但 MIT 授权——放进商业项目没有任何负担。给 Ren'Py 游戏做个展示页、或者给直播间做个 OBS 浏览器源挂件，直接塞进去就行。
- 实用性：落地（比 GPL 的老牌看板娘更适合商业用）

### 23. live2d-viewer-web（guansss/live2d-viewer-web）
- 链接：https://github.com/guansss/live2d-viewer-web
- 核实：⭐ 175 · MIT · TypeScript · updated_at 2026-09-29，pushed_at 2023-02-03（命令：`gh api repos/guansss/live2d-viewer-web`）
- 一句话：Live2D 官方桌面版 Viewer 的网页实现。
- 可拓展性：本地起一个页面就能预览和调试自己的模型——看参数对不对、动作和表情有没有跑偏，比每次都开 Cubism Editor 轻得多。代码 2023 年后没动，但对 Cubism 4 时代的模型够用。
- 实用性：参考（调试模型很好用）

### 24. spive2d（lmmtrr/spive2d）
- 链接：https://github.com/lmmtrr/spive2d
- 核实：⭐ 137 · MIT · JavaScript · updated_at 2026-10-09，pushed_at 2026-10-09（命令：`gh api repos/lmmtrr/spive2d`）
- 一句话：一个简单的查看器，Spine 和 Live2D 两种格式通吃。
- 可拓展性：做 Ren'Py 项目时经常要纠结"这块用 Spine 还是 Live2D"，一个查看器能同时开两种格式很省事。而且它当天还在推代码，是这一批里维护最勤的之一。
- 实用性：落地（活跃维护 + 双格式）

### 25. VTuber-Python-Unity（mmmmmm44/VTuber-Python-Unity）
- 链接：https://github.com/mmmmmm44/VTuber-Python-Unity
- 核实：⭐ 557 · MIT · C# · updated_at 2026-09-28，pushed_at 2022-05-17（命令：`gh api repos/mmmmmm44/VTuber-Python-Unity`）
- 一句话：用 Python + Unity 做的 VTuber 方案，3D 和 Live2D 都支持，纯 CPU 实现面部移动追踪、眨眼检测、虹膜追踪和嘴部追踪。
- 可拓展性：**"纯 CPU"是这条最值钱的地方**——16GB 内存、没有独显的笔记本也能跑面捕，不用为了动捕去买显卡。想给立绘加"跟着摄像头动"的效果，这是门槛最低的参考实现。代码停在 2022 年。
- 实用性：参考（低配友好，但已停更）

### 26. VTS-Fullbody-Tracking（jellydreams/VTS-Fullbody-Tracking）
- 链接：https://github.com/jellydreams/VTS-Fullbody-Tracking
- 核实：⭐ 34 · NOASSERTION · Python · updated_at 2026-09-16，pushed_at 2025-03-05（命令：`gh api repos/jellydreams/VTS-Fullbody-Tracking`）
- 一句话：只用一个摄像头做 Live2D VTuber 的全身追踪，是 VTube Studio 和 Nizima LIVE 的插件。
- 可拓展性：常见面捕只动脸，这个连身体一起动，效果差别很大。Python 写的，读它的代码能搞明白"摄像头姿态怎么映射成 Live2D 参数"，学会了可以照搬进自己的项目。许可没标。
- 实用性：参考（思路可抄，项目小众）

### 27. VTS-Sharp（FomTarro/VTS-Sharp）
- 链接：https://github.com/FomTarro/VTS-Sharp
- 核实：⭐ 50 · MIT · C# · updated_at 2026-08-19（命令：`gh api repos/FomTarro/VTS-Sharp`）
- 一句话：用 C# 操作 VTube Studio API 的库。
- 可拓展性：想自己写 VTube Studio 插件（比如让本地 Ollama 输出的情绪标签直接驱动模型表情），这是最省事的入口，MIT 授权、维护正常。同作者还有 vts-heartrate 这类小插件可以当范例。
- 实用性：参考（要接 VTS 时的起点）

### 28. facial-landmarks-for-cubism（adrianiainlam/facial-landmarks-for-cubism）
- 链接：https://github.com/adrianiainlam/facial-landmarks-for-cubism
- 核实：⭐ 75 · MIT · C++ · updated_at 2026-07-11（命令：`gh api repos/adrianiainlam/facial-landmarks-for-cubism`）
- 一句话：用 OpenSeeFace 从摄像头取面部关键点，转换成 Live2D Cubism SDK 能直接用的参数。
- 可拓展性：这正是自己搭面捕时最缺的那段"胶水代码"——上游（面捕软件）和下游（Live2D 参数）之间的桥。同一作者还写了 mouse-tracker-for-cubism（用鼠标位置+麦克风驱动模型），两个合起来可以做出"没人盯着摄像头时也不会僵住"的效果。
- 实用性：落地（MIT + 补上关键一环）

### 29. Live2DFrequencyLipSync（DenchiSoft/Live2DFrequencyLipSync）
- 链接：https://github.com/DenchiSoft/Live2DFrequencyLipSync
- 核实：⭐ 53 · MIT · C# · updated_at 2026-07-03，pushed_at 2018-08-09（命令：`gh api repos/DenchiSoft/Live2DFrequencyLipSync`）
- 一句话：用频域分析给 Live2D 模型做口型同步的示例代码。
- 可拓展性：比"音量大就嘴张大"聪明得多——按声音的频率分频段驱动不同口型，说话看起来才真。代码 2018 年后没更新，但思路很短也很好抄，几行就能移植进自己的项目（Ren'Py 里配合语音播放做口型也能用）。
- 实用性：参考（代码老，思路值钱）

### 30. Open-LLM-VTuber（Open-LLM-VTuber/Open-LLM-VTuber）
- 链接：https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
- 核实：⭐ 14025 · NOASSERTION · Python · updated_at 2026-10-09（命令：`gh api repos/Open-LLM-VTuber/Open-LLM-VTuber`）
- 一句话：跨平台本地运行的语音对话 + Live2D 形象项目，支持免提语音交互和语音打断，后端可以接任意 LLM。
- 可拓展性：**对画像最贴合的一条**——Python 栈、本地跑、能接 Ollama 这类本地模型，前端直接就是 Live2D。想让视觉小说里的角色"会说话、会动、会眨眼"，可以直接扒它前端的 Live2D 调度、口型和动作管理逻辑，跟 Ren'Py 的对话系统对接。
- 实用性：落地（本地 LLM + Live2D 的完整范本）

### 31. Live2d-model（Eikanya/Live2d-model）
- 链接：https://github.com/Eikanya/Live2d-model
- 核实：⭐ 3437 · NOASSERTION · 语言 Wolfram Language · updated_at 2026-10-09（命令：`gh api repos/Eikanya/Live2d-model`）
- 一句话：Live2D 模型收集仓库，主要是从各类游戏里提取整理出来的模型资源。
- 可拓展性：练手素材库——想学绑骨但手上没模型时，这里有现成的 moc3 可以拆开研究。但两个警告：一、这些模型版权归原作者/厂商，只能学习，不能放进自己的作品发布；二、结合第 20 条（moc3 可被植入恶意载荷），来历不明的模型别在主力机上直接打开。
- 实用性：参考（只能当学习样本）

### 32. CubismExternalEditMCP（nana7chi/CubismExternalEditMCP）
- 链接：https://github.com/nana7chi/CubismExternalEditMCP
- 核实：⭐ 33 · MIT · Python · updated_at 2026-10-09（命令：`gh api repos/nana7chi/CubismExternalEditMCP`）
- 一句话：给 Live2D Cubism Editor 5.4 alpha1 的"外部应用联动"功能做的 MCP 服务。
- 可拓展性：把官方编辑器变成能被 AI agent 直接驱动的工具——配合本地 Ollama 或 Claude Code，让 agent 自己去改模型参数、查状态。star 只有 33，非常早期，但它指了一条路：**Cubism 官方编辑器本身在向 AI 开放接口**，这个趋势比项目本身更值得记。
- 实用性：参考（早期项目，但方向对）

## 二、去重报告

#### 2.1 与索引/历史汇总的交叉查重（结果：全部 0 命中）

对 32 条候选逐个执行：

```bash
export PATH=/usr/bin:$PATH; cd D:/34498/Documents/github-projects-invest-games
grep -iF "<owner/repo>" index.html csdn-social-summary.md csdn-social-summary-v23.md csdn-social-summary-v22.md csdn-social-summary-v21.md
```

32 条候选在 `index.html`（1168 项）和四个历史汇总文件（v25/v23/v22/v21）中**全部 0 命中**。
补充确认：`grep -ci 'live2d' csdn-social-summary.md csdn-social-summary-v23.md csdn-social-summary-v22.md csdn-social-summary-v21.md`
四份汇总文件均为 **0**，即此前二十五辑从未做过 Live2D 主题，本辑是纯增量区。

索引里 `live2d` 相关仅 `live2d/cubismnativeframework`（脚注 [765]）一项，本路未重复收录；
骨骼动画组的 `dragonbonesjs` 属通用 Spine/DragonBones 路线，与本辑无关，未触碰。

#### 2.2 候选池内部剔除名单（同主题撞车，只留一条）

| 剔除对象 | 保留对象 | 形态 | 理由 |
|---|---|---|---|
| `zwa73/UnityLive2DExtractor-Unofficial`（⭐57） | `Perfare/UnityLive2DExtractor`（⭐634） | 换名 / 派生 | 同一工具的"非官方续作"分支，功能与描述逐字相同，收原项目 |
| `NovaPlayzGames/model-reaper`（⭐0） | `goldimpact/Eviler`（⭐12） | 换名 / 转载 | 描述一字不差（"It is a live2d extractor to rip the psd out of moc3 files IT IS NOT USING ANY CODE FROM LIVE2D"），典型改名重发 |
| `xiazeyu/live2d-widget.js`（⭐1578） | `stevenjoezhang/live2d-widget`（⭐10986） | 同功能撞车 | 两者都做博客看板娘，只收体量最大的那条；模型库 `xiazeyu/live2d-widget-models` 同理未单列 |
| `Inochi2D/inochi2d`（⭐1810） | `Inochi2D/inochi-creator`（⭐1240） | 同组织上下游 | SDK 与编辑器是同一条产品线，收编辑器即可，SDK 在条目内说明 |
| `UlyssesWu/D2Evil`（⭐139） | `goldimpact/Eviler`（⭐12） | 同源家族 | 同为 waifu 模型解析库，主题重复，按条目上限让位给更贴合的项 |
| `Konata09/Live2dOnWeb`（⭐86） | `hacxy/l2d-widget`（⭐639） | 同功能撞车 | 都是网页挂件，收 MIT + 更活跃的 |
| `Veykril/cubism-rs`、`aethiopicuschan/cubism-go`、`qinyonghang/Live2D-Python`、`SakuraMotion/PurismCore`、`Ludentes/py-moc3` | （未收） | 同类 SDK 绑定 | 五种语言的 Cubism SDK 封装功能高度同构，按 32 条上限只保留主流的 Web/引擎路线 |
| `Jelosus2/BD2-L2D-Viewer`、`respectZ/blue-archive-viewer`、`kiraio-moe/NikkeViewerEX` 等游戏专用查看器 | `lmmtrr/spive2d`（⭐137） | 垂直重复 | 一批"某游戏的 Live2D 查看器"，彼此只差游戏名，收一个通用查看器代表 |
| `P1kaj1uu/ChattyPlay-Agent`（⭐948） | （未收） | 主题漂移 | 搜索命中但描述是"20+ 平台视频解析/下载"的大杂烩工具，与 Live2D 制作无关，疑为关键词堆砌 |

#### 2.3 六种重复形态逐条核对

- **换名**：见 2.2 前两行（UnityLive2DExtractor-Unofficial / model-reaper）。✅ 已剔
- **旧闻换日期**：本路数据全部来自本轮 `gh api repos/...` 实时拉取，非二手文章，不适用。✅
- **转载**：候选全部为 GitHub 原始仓库，无转载站。✅
- **ID 新 ≠ 内容新**：已对每条核对 `pushed_at` vs `updated_at`，对停更项目在条目里明确写出年份
  （如 `renpy-live2d` pushed 2021-03-02、`AnimeSR` pushed 2023-08-18、`Live2DFrequencyLipSync` pushed 2018-08-09）。✅
- **SEO 镜像站（hqwc.cn / mhpn.cn）**：本路为 GitHub 路，未引入任何站外内容农场链接。✅
- **同日双发内容农场**：不适用（同上）；另对 2026-10-09 同日更新的多条做了人工比对，均为不同作者的独立项目。✅

## 三、本路小结

- **条数**：32 条，全部带完整 GitHub URL，全部附 `gh api repos/{owner}/{repo}` 取数命令原文。
- **star / license / 语言 / updated_at**：全部来自本轮真实 API 返回，无一项来自记忆；
  其中 3 条额外标注了 `archived=true`（lpk2moc3、moc3ingbird）与多处 `pushed_at` 远早于 `updated_at` 的停更情况。
- **可复用性分布**：落地 10 条、参考 19 条、不采用 3 条。
- **最反直觉的一件事**：见下方返回给主 agent 的汇总。
