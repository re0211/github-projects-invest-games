# Live2D 制作全链路 · GitHub 新发现（第二十八辑 · 建模→绑骨→动画→引擎→驱动→分发）

> 去重基准：`_r28/_dedupe_gh.txt`（1189 行）+ 第二十六/二十七辑主题比对。
> 全部为 2025-10 之后仍有 push、或 2026 年新建的仓库。★ 与日期均来自 GitHub API 实时读取，未核实项已标注。

| owner/repo | ★ | 语言 | 最近更新 | 一句话是什么 | 可拓展性(能不能接进自己的流水线) | 实用性(16GB Windows 本机能不能真跑) | URL |
|---|---|---|---|---|---|---|---|
| **一、开源替代编辑器 / 建模·绑骨·动画** | | | | | | | |
| umamoorg/umamo | 149 | Kotlin | 2026-10-09 | 直接对标 Cubism Editor 的开源跨平台绑骨编辑器，读写 `.cmo3` 源格式，一等公民笔/触控支持 | **高**：目标是格式级 drop-in 替换，能直接打开现有 Cubism 工程；Kotlin Multiplatform 便于二次开发 | **中低**：官方自述 **early alpha、尚未公开发布**，建模/UV/物理在做，动画功能未实现；Windows/Linux 可构建（需 JDK 21），macOS/Android 被渲染器卡住 | https://github.com/umamoorg/umamo |
| CheshireMew/PuppetLoom | 245 | TypeScript | 2026-10-05 | 把分层角色 PSD 变成「可自动制作、可验证、可持续校准」的 2D 动态角色 | **高**：带 `AGENT_USAGE.md`，明确面向 Agent 自动化的流水线设计，可脚本化 | **中**：Web/TS 栈，本机跑得动；AGPL-3.0 对商用闭源有传染性 | https://github.com/CheshireMew/PuppetLoom |
| shinshin86/live2d-add-motion-sample-web-ui | 194 | HTML | 2026-10-08 | 纯网页 UI，给**已有** Live2D 模型追加动作（不装 Editor 也能改 motion） | **中**：前端直改 motion3 类数据，可嵌进自己的模型维护页 | **高**：零安装，浏览器打开即用，16GB 毫无压力 | https://github.com/shinshin86/live2d-add-motion-sample-web-ui |
| Yoru-KenomoVT/ayatsuri_2d | 2 | Rust | 2026-09-13 | 「操り２D」——自称 Cubism 的跨平台开源替代，端到端支持 moc3 v3→v6 | **中**：Rust 库形态，可当后端引擎接 | **低**：★2、作者单人，v6 支持声称未经验证，别押生产 | https://github.com/Yoru-KenomoVT/ayatsuri_2d |
| redchenk/yachiyo-live2d-studio | 25 | JavaScript | 2026-08-14 | 浏览器里的 Live2D studio（建模/预览一体化方向） | **中**：JS 前端可 fork 改 | **中**：无 README 描述，需自己摸 | https://github.com/redchenk/yachiyo-live2d-studio |
| **二、`.moc3` 运行时与渲染集成** | | | | | | | |
| Inochi2D/inochi2d | 1810 | D | 2026-10-03 | 老牌开源 2D puppet SDK（`.inp` 生态），非 Cubism 路线但定位完全重合 | **高**：有独立格式与完整工具链，是「彻底绕开 Cubism 授权」的现实选项之一 | **中**：D 语言工具链在 Windows 上要配 dmd/ldc；跑 demo 没问题 | https://github.com/Inochi2D/inochi2d |
| AyagamiDev/ayagami | 350 | Rust | 2026-09-14 | 兼容 Live2D 的 2D puppet 模型渲染器（Rust） | **高**：Rust crate 形态，可嵌进 Tauri/游戏引擎 | **高**：本机可编译，无 GPU 重负载 | https://github.com/AyagamiDev/ayagami |
| nanlingyin/soullink-emotion-sdk | 141 | TypeScript | 2026-09-30 | 框架无关的 Live2D 表情/动作 SDK：连续 VAD 情绪 + FACS/AU 合成 + 分层动画 + 模型自动适配 | **高**：就是要被集成的 SDK，自带「自动适配任意模型」这一层，省掉逐个模型调参 | **高**：纯前端 + 麦克风，16GB 绰绰有余 | https://github.com/nanlingyin/soullink-emotion-sdk |
| Untitled-Story/untitled-pixi-live2d-engine | 78 | TypeScript | 2026-09-20 | PixiJS v8 的 Live2D 引擎，**Cubism 2–5 全版本 SDK** + 原生渲染管线 + 口型同步 | **高**：直击上一辑「Cubism 5 的 moc3 第三方库不吃」这条坑；v8 原生管线性能好 | **高**：Node + 浏览器，本机直接跑 | https://github.com/Untitled-Story/untitled-pixi-live2d-engine |
| Eatgrapes/Mocari | 46 | Rust | 2026-07-13 | **纯 Rust**（非 FFI 包壳）的 Live2D/Cubism 运行时实验 | **高**：纯 Rust 意味着无官方 Core DLL 依赖路径，License 干净（MIT） | **中**：自称 experiment，需自己验证覆盖率 | https://github.com/Eatgrapes/Mocari |
| SakuraMotion/PurismCore | 40 | C | 2026-08-21 | 开源、Live2D 兼容的 MOC3 加载运行时（sakura2d.org 生态） | **高**：C 核心最容易被别的语言 FFI 包一层 | **中**：MIT 但项目年轻，★40 | https://github.com/SakuraMotion/PurismCore |
| marukun712/kokoro | 42 | TypeScript | 2026-10-06 | 「工程师用的 2D 角色网格变形库」——做网格/变形这一层的轮子 | **中高**：库形态，能替代 Cubism 的变形算法部分 | **高**：纯 TS，浏览器就能验证 | https://github.com/marukun712/kokoro |
| hacxy/l2d | 55 | TypeScript | 2026-05-15 | 让浏览器加载 Live2D 模型更简单（l2d 生态的核心库） | **中高**：MIT 轻封装，可当自己项目的底座 | **高**：前端，无压力 | https://github.com/hacxy/l2d |
| LIlGG/plugin-live2d | 251 | TypeScript | 2026-09-29 | Halo 博客的看板娘插件（最省事的 Web 落地形态） | **中**：只能用在 Halo，但插件写法可借鉴 | **高**：一键装 | https://github.com/LIlGG/plugin-live2d |
| jiangweifang/wp-live2d | 23 | 未核实 | 2026-06-02 | WordPress Live2D 插件 | **低中**：WordPress 专用 | **高**：PHP 主机即可 | https://github.com/jiangweifang/wp-live2d |
| Mozi216/Sparkle.Live2DView | 9 | C# | 2026-08-30 | 面向 Avalonia 的轻量 Live2D 渲染控件，支持视线跟随/拖动/缩放/切动作 | **中高**：Avalonia = 跨平台 .NET，Windows 桌面应用可直接用 | **高**：.NET 桌面，16GB 轻松 | https://github.com/Mozi216/Sparkle.Live2DView |
| Watunder/GDLive2D | 3 | C++ | 2026-05-18 | Godot 4 的 Live2D 模块（GDExtension） | **中**：GDExtension 可被 GDScript 调用，接 Godot 项目顺 | **低**：WIP、★3，别当主力 | https://github.com/Watunder/GDLive2D |
| linh18nd/flutter_live2d | 5 | C++ | 2026-05-15 | Flutter 的 Live2D 插件（C++ 侧实现） | **中**：Flutter 跨端可复用 | **低**：★5，成熟度存疑 | https://github.com/linh18nd/flutter_live2d |
| amaiichigopurin/flutter_live2d_ffi | 2 | C++ | 2026-09-08 | Flutter 侧 FFI 直连 Cubism Core 的另一种做法 | **中**：FFI 路线比插件路线更可控 | **低**：★2 | https://github.com/amaiichigopurin/flutter_live2d_ffi |
| qinyonghang/Live2D-Python | 21 | C++ | 2025-10-31 | PyLive2D：Cubism SDK 的 Python 封装（渲染 + 交互） | **中高**：Python 侧可脚本化控制模型 | **中**：需 Cubism Core；与已收录的 `live2d-py` 是不同实现，可对比 | https://github.com/qinyonghang/Live2D-Python |
| lsk-china/my-live2d-qt | 11 | C++ | 2026-06-10 | Qt（C++/WTFPL）上的 Live2D 渲染 | **中**：Qt 桌面应用可嵌 | **高**：本机 Qt 环境能编 | https://github.com/lsk-china/my-live2d-qt |
| EasyLive2D/Live2D-v2-Lua | 18 | Lua | 2026-08-12 | **纯 LuaJIT 实现**的 Live2D v2/v3/v4/v5 渲染引擎（不依赖官方 Core） | **高**：Lua 极易嵌入游戏/工具链，且绕开 Core 授权 | **中**：LGPL-3.0；v5 声称支持需实测 | https://github.com/EasyLive2D/Live2D-v2-Lua |
| Dingdang255/live2d-haxe | 11 | Haxe | 2026-07-13 | Haxe 版 Live2D 库（Haxe 可编译到多目标） | **中**：Haxe 小众但跨编译能力强 | **中**：需 Haxe 工具链 | https://github.com/Dingdang255/live2d-haxe |
| **三、PSD 图层拆分 / 素材准备** | | | | | | | |
| shitagaki-lab/see-through | 4497 | Python | 2026-10-05 | **SIGGRAPH 2026 论文官方实现**：单张二次元插画 → 可操作的 2.5D 分层模型（含深度排序），直接喂 Live2D | **极高**：这是「AI 自动拆图」目前最硬的学术背书实现，Apache-2.0 | **中**：Python + 深度学习权重，16GB 内存够，但显存是瓶颈（需实测，社区有 8GB 显存实测记录） | https://github.com/shitagaki-lab/see-through |
| shitagaki-lab/CubismPartExtr | 12 | C++ | 2026-05-04 | 同一实验室的 Cubism 部件提取（从 .cmo3/.moc3 侧反推部件） | **中**：C++ 可编成 CLI 接流水线 | **低**：无 README 描述 | https://github.com/shitagaki-lab/CubismPartExtr |
| Wzhang3912/image2live2d | 43 | Python | 2026-09-07 | 已拆好的角色分层 → 可复用可绑骨的 2D puppet，同时导出 nijilive `.inp` **和** Live2D `.moc3` | **高**：一条链路出两种格式，方便在开源/商业格式间横跳 | **中**：依赖链较长 | https://github.com/Wzhang3912/image2live2d |
| CVIndomitable/illust2psd | 8 | Python | 2026-03-29 | 动漫/游戏立绘 → Cubism Editor 可用的多图层 PSD（自动分层） | **中高**：产出的就是 PSD，天然接 Cubism Editor | **中**：作者标注「开发中」 | https://github.com/CVIndomitable/illust2psd |
| funlin724/emote-to-cubism | 0 | Python | 2026-09-19 | E-mote（`.psb`）→ Live2D Cubism 的转换工具链 + 格式文档 | **中**：跨 2D 动画格式迁移，附格式文档很有价值；明确声明不含游戏素材 | **中**：需自备文件，★0 但文档导向 | https://github.com/funlin724/emote-to-cubism |
| **四、面部/动作捕捉驱动** | | | | | | | |
| Arcelyth/live-ascii | 234 | Rust | 2026-08-29 | **终端里渲染** Live2D Cubism 模型，并支持面部追踪 | **中高**：Rust + 摄像头，可作为「低开销常驻桌宠/监控面板」底座 | **高**：ASCII 渲染，CPU 占用极低，16GB 随便跑 | https://github.com/Arcelyth/live-ascii |
| EnoxSoftware/CVVTuberExample | 99 | C# | 2026-09-26 | Unity 的 Computer-Vision VTuber 范例（WebCamTexture 驱动模型） | **中高**：Unity 项目可直接参考其追踪→参数映射 | **中高**：需 Unity，16GB 可跑 | https://github.com/EnoxSoftware/CVVTuberExample |
| DenchiSoft/VTubeStudio | 1312 | C# | 2026-09-28 | VTube Studio **官方 API** 开发页/SDK（不是模拟器，是接真 VTS 的正路） | **高**：想把自家驱动程序接进 VTube Studio 就必须读它 | **高**：文档/示例代码，纯读 | https://github.com/DenchiSoft/VTubeStudio |
| moonrailgun/vtubeleaf | 13 | TypeScript | 2026-10-09 | Tauri + MediaPipe 的**本地** Live2D 头像面捕，定位「开会时的虚拟化身」 | **高**：纯本地、不上传人脸，MediaPipe  landmark → Live2D 参数这一段可直接抄 | **高**：MediaPipe CPU 版在 16GB 机器上很轻 | https://github.com/moonrailgun/vtubeleaf |
| Voine/VirtualFaceCapture-MNN | 5 | C++ | 2026-06-01 | 安卓端皮套人面捕：MediaPipe landmark + **阿里 MNN** 推理 + 自定义追踪 | **中高**：移动端方案，MNN 比 TFLite 在国产机上更顺 | **中**：需 Android 设备调试 | https://github.com/Voine/VirtualFaceCapture-MNN |
| Lendic42/LumaStage | 1 | TypeScript | 2026-07-18 | 开源 VTuber 工作台：Windows/macOS 桌面端 + **局域网 iPhone Face ID（ARKit）** 面捕 | **中高**：正经的「iPhone 当摄像头」低成本高质量路线 | **低**：★1、NOASSERTION 许可，早期 | https://github.com/Lendic42/LumaStage |
| adrianiainlam/mouse-tracker-for-cubism | 15 | 未核实 | 2026-04-02 | 用鼠标/指针位置驱动 Cubism 参数（与已收录的同作者面部 landmark 版配套） | **中**：最简单的「无需摄像头」驱动，做交互反馈够用 | **高**：零依赖 | https://github.com/adrianiainlam/mouse-tracker-for-cubism |
| rotejin/MotionPNGTuber | 337 | Python | 2026-04-13 | 「PNGTuber 以上、Live2D 未满」：视频循环做头发飘动 + 实时口型 | **中**：不想做完整 Live2D 时的降级方案，成本骤降 | **高**：纯 Python + 视频循环，极轻 | https://github.com/rotejin/MotionPNGTuber |
| **五、AI 辅助（拆图 / 绑骨 / 口型 / AIGC 流水线 / 语音驱动）** | | | | | | | |
| luomo66ccff/Amahane-Hikari-Live2D | 112 | TypeScript | 2026-09-21 | 用 OpenAI Codex **主导**的 Live2D 制作实录：MIT 的 WebGL 查看器 + 已验证工具 + 可复用 production Skill | **高**：直接给「AI 做 Live2D」的可复制配方，查看器 MIT 可拿走 | **高**：Web 栈；注意角色素材另行授权 | https://github.com/luomo66ccff/Amahane-Hikari-Live2D |
| J621111/live2d-automation | 76 | Python | 2026-09-27 | **Live2D Automation MCP Server**——把 Live2D 制作流程暴露成 MCP 工具给 Agent 调 | **极高**：这是本批最「接得上 Agent 流水线」的一个，配 Codex/Claude 直接驱动建模步骤 | **中高**：Python MCP server，本机可起；但无 License 声明 | https://github.com/J621111/live2d-automation |
| Ariakage/live2d-agent-kit | 25 | Python | 2026-09-12 | 面向 Codex/AI Agent 的 Live2D 制作工作流：PSD/PNG 绑骨 + 动漫放大 + Core/WebGL 校验 + 一个可跑 VTube Studio 的示例模型 | **高**：自带示例模型 = 能立刻验证闭环；还有「校验」环节（上一辑痛点） | **高**：Python + 自带模型，16GB 友好 | https://github.com/Ariakage/live2d-agent-kit |
| sayaka-aiart/cubism-api-bridge | 11 | TypeScript | 2026-09-12 | Cubism Editor **External API** 的非官方 TS/Python 桥 + 本地 HTTP server，带 StandRig 集成 | **高**：把 Cubism Editor 变成可被脚本/HTTP 驱动的服务，自动化的关键缺口 | **中**：需本机装 Cubism Editor；标记为 Experimental | https://github.com/sayaka-aiart/cubism-api-bridge |
| fifteen42/live2d-from-art | 11 | Python | 2026-09-15 | 实验性 Agent Skill：立绘→Live2D 工作流、直接编写 MOC3、浏览器端校验 | **高**：Skill 形态，可按自己习惯改造后复用 | **中**：实验性，无 License | https://github.com/fifteen42/live2d-from-art |
| mw2wbyys6t-sudo/live2d-auto-pipeline | 10 | 未核实 | 2026-10-09 | 素材 → 可部署 Live2D 模型的**全自动**生成（端到端目标） | **中高**：流水线拼装思路可直接抄 | **中**：未核实语言/许可 | https://github.com/mw2wbyys6t-sudo/live2d-auto-pipeline |
| lTwTlol/Auto-live2D-beta | 28 | HTML | 2026-08-30 | 「一张图制作自己的虚拟形象」 | **中**：beta，一键流 | **高**：网页端 | https://github.com/lTwTlol/Auto-live2D-beta |
| Mitscherlich/live2d-mcp | 12 | JavaScript | 2026-08-10 | 另一个 Live2D MCP 服务（与 live2d-automation 互为备选） | **中高**：MCP 形态 | **中**：无描述、无 License | https://github.com/Mitscherlich/live2d-mcp |
| ai-zen/live2d-copilot | 19 | TypeScript | 2026-08-29 | 以 Live2D 为载体的 AI 桌面宠物（含语音/动作联动方向） | **中**：参考实现 | **中**：无 License | https://github.com/ai-zen/live2d-copilot |
| nanlingyin/SoulLink_Live2D | 38 | JavaScript | 2026-05-14 | 用 LLM 输出直接控制 Live2D 模型的方案（与上面 emotion-sdk 同作者） | **高**：把「LLM → 表情/动作参数」这层做成了可复用方案 | **高**：纯 JS | https://github.com/nanlingyin/SoulLink_Live2D |
| organics2016/pymouth | 10 | Python | 2026-02-09 | Python 的 Live2D **口型同步**库 | **高**：小库、单一职责，最容易嵌进自己的 TTS 链路 | **高**：纯 Python | https://github.com/organics2016/pymouth |
| LimiNode/speech-animation | 0 | 未核实 | 2026-10-08 | 引擎无关的实时语音动画：viseme / 口型 / 语音驱动的面部线索 | **中高**：强调 engine-agnostic，跨 Live2D/VRM 通用 | **低**：★0，需自测 | https://github.com/LimiNode/speech-animation |
| zziying/ai-live2d-body | 46 | 未核实 | 2026-09-05 | 「给已有 AI 装一个 Live2D 身体」——架构篇（不是再造桌宠，是解耦大脑与身体） | **高**：架构文档价值 > 代码，适合想把自家 Agent 接 Live2D 的人 | **高**：思路篇可直接读 | https://github.com/zziying/ai-live2d-body |
| **六、查看器 / 调试器 / 格式解析 / 转换** | | | | | | | |
| HKUDS/CLI-Anything | 51788 | Python | 2026-09-22 | 内含 `cli-anything-live2d`：**42 条命令**从命令行检查/校验/编辑/lint/diff/批量管理/打包 `.model3.json`，**全程不需要 Cubism Editor** | **极高**：inspect / validate / lint / runtime-check（Web SDK 兼容性）/ flatten / pack / batch —— 正是模型交付前最缺的那一步 | **高**：Python CLI，本机直接跑 | https://github.com/HKUDS/CLI-Anything |
| Live2D/CubismSpecs | 22 | Python | 2026-08-05 | **官方** Cubism 文件格式规格（moc3 / model3 / motion3 等的权威定义） | **极高**：想自己写解析器/转换器，这是唯一权威依据，比逆向稳 | **高**：文档 + 脚本，纯读 | https://github.com/Live2D/CubismSpecs |
| ihopenot/LpkUnpacker | 295 | Python | 2026-04-07 | 解包 Live2DViewerEx 的 `.lpk` 打包格式 | **高**：拿到分发包的原始模型资源的实用工具 | **高**：纯 Python | https://github.com/ihopenot/LpkUnpacker |
| UlyssesWu/D2Evil | 139 | C# | 2026-06-07 | 「Managed waifu model parsing libs」——.NET 侧的二次元模型解析库集合 | **中高**：.NET 生态里少见的模型解析层 | **中**：NOASSERTION 许可 | https://github.com/UlyssesWu/D2Evil |
| OpenL2D/moc3ingbird | 98 | C++ | 2026-06-06 | MOC3ingbird 漏洞（**CVE-2023-27566**）相关代码 | **中**：安全视角——加载来路不明的 moc3 前该知道的风险面 | **中**：研究用途，别用在生产 | https://github.com/OpenL2D/moc3ingbird |
| lmmtrr/spive2d | 137 | JavaScript | 2026-10-09 | 简洁的 Spine **与** Live2D 查看器（一个工具看两种格式） | **中高**：对比/验收两种 2D 格式时最省事 | **高**：轻量前端 | https://github.com/lmmtrr/spive2d |
| TSKI433/hime-display | 254 | JavaScript | 2026-03-30 | 通用桌面模型展示器：Live2D / Spine / MMD / VRoid 通吃 | **中**：统一预览入口，做素材管理面板可用 | **高**：GPL-3.0，桌面 Electron 类 | https://github.com/TSKI433/hime-display |
| KurisuMakise004/renderkit | 29 | Jupyter Notebook | 2026-10-02 | CLI 把 PMX/VRM/**MOC3** 渲染成 albedo/depth 等通道图 | **中高**：把 Live2D 模型转成机器学习/预渲染的输入，AIGC 复用场景 | **中**：需渲染环境 | https://github.com/KurisuMakise004/renderkit |
| Ludentes/py-moc3 | 4 | Python | 2026-04-08 | Python 版 `.moc3` 二进制**读 + 写** | **高**：读写都有 = 能改模型而不只是看 | **中**：★4，需自测兼容性 | https://github.com/Ludentes/py-moc3 |
| MahouTechnologies/moc3-rs | 6 | Rust | 2026-08-15 | Rust 的 moc3 处理（Apache-2.0） | **中**：Rust 侧解析层 | **中**：★6，描述为空 | https://github.com/MahouTechnologies/moc3-rs |
| **七、Cubism SDK 的语言绑定 / 封装 / 脚手架** | | | | | | | |
| Live2D/CubismWebSamples | 392 | 未核实 | 2026-04-02 | 官方 Web SDK 示例集合（最短可跑路径） | **高**：所有 Web 集成的事实起点 | **高**：Node 起静态服务即可 | https://github.com/Live2D/CubismWebSamples |
| Live2D/CubismNativeSamples | 239 | 未核实 | 2026-04-02 | 官方 Native SDK 示例（注意：公告称 Cocos2d-x 支持即将终止） | **中高**：Native/引擎侧起点 | **高** | https://github.com/Live2D/CubismNativeSamples |
| Live2D/CubismUnrealEngineComponents | 32 | C++ | 2026-09-29 | 官方 Unreal 组件（本批少见的 UE 侧官方更新） | **中高**：UE5 项目可用 | **中**：UE 本体比 Live2D 重得多，16GB 吃紧 | https://github.com/Live2D/CubismUnrealEngineComponents |
| Live2D/CubismJavaFramework | 16 | Java | 2026-06-04 | 官方 Java Framework（配 CubismJavaSamples ★31） | **中**：JVM 侧（安卓桌面/JVM 工具）集成 | **高**：JVM 轻量 | https://github.com/Live2D/CubismJavaFramework |
| Live2D/CubismUnityMotionSyncComponents | 3 | C# | 2026-08-25 | 官方 **MotionSync**（音频驱动口型）Unity 组件 | **高**：口型同步不必自己造，官方给了方案 | **中**：需 Unity；★3 说明用的人少 | https://github.com/Live2D/CubismUnityMotionSyncComponents |
| Live2D/CubismNativeMotionSyncComponents | 5 | C++ | 2026-08-25 | MotionSync 的 Native 版组件 | **高**：非 Unity 项目的官方口型同步路径 | **中** | https://github.com/Live2D/CubismNativeMotionSyncComponents |
| Live2D-Garage/CubismExternalAppPluginSamples | 9 | JavaScript | 2026-09-08 | 官方 Garage 出品的 **Cubism Editor 外部插件**示例 | **高**：做 Editor 插件/外部工具的官方模板，MIT | **高**：JS 插件，本机装了 Editor 就能试 | https://github.com/Live2D-Garage/CubismExternalAppPluginSamples |
| aethiopicuschan/cubism-go | 32 | Go | 2026-09-17 | 非官方 Go 版 Cubism SDK（MIT） | **中高**：Go 服务端/工具链场景独一份 | **高**：Go 编译即用 | https://github.com/aethiopicuschan/cubism-go |
| jz315/live2d-cubism-core-sys | 1 | Rust | 2026-04-04 | Cubism SDK Native Core **v5** 的原始 Rust FFI 绑定（`-sys` 层） | **中高**：给 Rust 项目接官方 Core 的底座 | **中**：需自备 Core 库；★1 | https://github.com/jz315/live2d-cubism-core-sys |
| Eatgrapes/Live2D-JavaBinding | 16 | Java | 2026-06-27 | Cubism SDK 的 Java 绑定（MIT，非官方） | **中**：比官方 Java Framework 更轻的封装 | **中** | https://github.com/Eatgrapes/Live2D-JavaBinding |
| **八、模型分发 / 版权 / 批量管理** | | | | | | | |
| wan-h/awesome-digital-human-live2d | 2424 | TypeScript | 2026-05-18 | 数字人（含 Live2D）Awesome 清单——选型地图 | **高**：快速横评整个赛道的入口 | **高**：纯文档 | https://github.com/wan-h/awesome-digital-human-live2d |
| Eikanya/Live2d-model | 3437 | Wolfram Language | 2026-10-03 | 大规模 Live2D 模型合集（**无 License 声明**） | **中**：模型源，但商用前必须逐个确认授权 | **高**：下载即可用；**版权风险高** | https://github.com/Eikanya/Live2d-model |
| imuncle/live2d | 1156 | JavaScript | 2026-01-28 | 模型收集 + 展示，可直接用于静态网站（**无 License**） | **中**：自带展示页，静态站可直接抄 | **高**；同样**版权需自行确认** | https://github.com/imuncle/live2d |
| Jelosus2/BD2-L2D-Viewer | 539 | Vue | 2026-10-08 | Brown Dust 2 的网页版 Live2D/Spine 交互查看器 | **中**：商业游戏模型解析/预览的参考实现（MIT） | **高**：纯前端 | https://github.com/Jelosus2/BD2-L2D-Viewer |
| HELPMEEADICE/BANDORI-PET-REV | 462 | Python | 2026-10-06 | 基于 Live2D + PySide6 的桌面宠物，支持 50+ 角色 / 300+ 服装——**批量模型管理**的成熟样本 | **高**：多模型索引、切换、服装管理的工程写法可直接借鉴 | **高**：PySide6 桌面，本机丝滑 | https://github.com/HELPMEEADICE/BANDORI-PET-REV |
| Halyul/aklive2d | 81 | Python | 2026-10-09 | 为「明日方舟」Live2D 干员生成展示网页（可作壁纸） | **中**：批量拉取 + 生成展示页的自动化脚本思路 | **高**：Python 脚本 | https://github.com/Halyul/aklive2d |
| respectZ/blue-archive-viewer | 201 | Rust | 2026-07-21 | 蔚蓝档案资源查看器（含 Live2D 资源） | **中**：资源解析/批量导出思路；**无 License** | **高**：Rust 单文件好跑 | https://github.com/respectZ/blue-archive-viewer |
| A-kirami/bestdori-live2d-downloader | 27 | Go | 2026-07-30 | BanG Dream! Live2D 模型**批量下载器** | **中**：批量获取 + 归档的标准做法（MIT） | **高**：Go 单二进制 | https://github.com/A-kirami/bestdori-live2d-downloader |
| hacxy/l2d-models | 160 | 未核实 | 2026-05-16 | 为 l2d 提供模型资源的静态资源仓库（CDN 化分发的范例） | **中高**：把模型当静态资源托管的组织方式，可直接照搬 | **高**：纯资源 | https://github.com/hacxy/l2d-models |

## 三到五条最值钱的发现

**1. `HKUDS/CLI-Anything` 里的 `cli-anything-live2d` —— 这条补的是整条链路唯一的空白：模型交付前的「质检 + 批量手术」。**
前两辑的痛点都集中在「做不出来」和「Cubism 5 模型第三方库不吃」。但当你手里已经有几十个模型时，真正折磨人的是另一件事：`.model3.json` 里引用的贴图路径断了、motion 的淡入淡出时间不统一、有一堆孤儿文件、想知道这批模型能不能被 Web SDK 吃。这 42 条命令（`inspect` / `validate` / `lint` / `runtime-check --target web-sdk` / `atlas` / `orphan` / `batch` / `flatten` / `pack`）就是照着这些场景设计的，而且**全程不需要打开 Cubism Editor**。上一辑 §五 说「真跑 Ren'Py 只差一个 `.moc3`」——拿到模型之后先用它的 `validate` + `runtime-check` 过一遍，能提前把「路径/版本/兼容性」这三类哑火一次性排掉。这是本批里唯一一个「今天装上今天就能省时间」的东西。

**2. `shitagaki-lab/see-through`（★4497, SIGGRAPH 2026, Apache-2.0）——上一辑那条反证，现在有正面答案了。**
第二十七辑最有价值的结论是「一张图全自动出 Live2D」做了 23 次测试后失败。这一批找到的是同一问题的学术级解法：单张二次元插画 → 带深度排序的可操作 2.5D 分层模型。它不是「一键出 moc3」，而是把最卡脖子的**自动拆层 + 遮挡补全**这一步做扎实了，然后交给下游（`psd2live` 已收录）去绑骨。配套还有同实验室的 `CubismPartExtr` 和一堆 2026 年的实测流水线仓库（`Wzhang3912/image2live2d`、`fifteen42/live2d-from-art`）。注意它不是零门槛：显存是瓶颈，社区有 8GB 显存的实测记录，本机跑之前先看那几份实测。

**3. `J621111/live2d-automation` + `sayaka-aiart/cubism-api-bridge` —— 两个合起来才完整：把 Cubism Editor 变成 Agent 能调用的服务。**
单看 `live2d-automation`（MCP Server，★76）只是「Agent 能发起建模步骤」；但它要真的改到 Editor 里的东西，必须有人把 Editor 的 External API 暴露出来——`cubism-api-bridge` 干的就是这个（本地 HTTP server + TS/Python 桥）。这两个加起来，等于把「人坐在 Cubism Editor 前面点鼠标」这件事换成了「Agent 通过 MCP 下发指令」。再叠上 `Live2D-Garage/CubismExternalAppPluginSamples`（官方插件模板，MIT）和 `Ariakage/live2d-agent-kit`（自带一个可直接跑 VTube Studio 验证的示例模型），这条链从「素材 → 拆层 → 绑骨 → 校验 → 上 VTS」第一次有了能自己搭起来的闭环。**唯一要盯的是 License**：`live2d-automation` 和 `fifteen42/live2d-from-art` 都没声明许可，商用前要问作者。

**4. `Untitled-Story/untitled-pixi-live2d-engine` —— 直接解掉上一辑记下的那条坑。**
第二十七辑白纸黑字写着「用 Cubism 5 导出的 `.moc3`（v4），pixi / AITuberKit 这类第三方库是不吃的」，结论是「别把 Cubism 5 的模型丢给第三方网页播放器」。这个 PixiJS v8 引擎把支持范围标到了 **Cubism 2–5 SDK**，还带原生渲染管线和口型同步。如果这个声称实测成立，上一辑那条限制在 Web 侧就不成立了——这是本批里最该优先实测的一条（先拿一个免费 Cubism 5 模型跑 `runtime-check` + 这个引擎，两条命令见分晓）。同类的备选还有 `AyagamiDev/ayagami`（Rust, ★350）和 `EasyLive2D/Live2D-v2-Lua`（纯 LuaJIT 声称支持 v2–v5，且**不依赖官方 Core**，对授权敏感的场景是条活路）。

**5. 关于「开源替代编辑器」，要泼一盆冷水：现在只有一个真的在动，而且还没发布。**
`umamoorg/umamo` 是唯一明确以「drop-in 替换 Cubism Editor、读写 `.cmo3`」为目标的开源编辑器，Kotlin Multiplatform、Windows/Linux 可构建。但它自己的 README 写的是 **early alpha、尚未公开发布**，建模/UV/物理在做、动画功能未实现，macOS/Android 被渲染器卡住。另外 `inochi2d/inochi-creator`（上一辑已收录）走的是完全独立的 `.inp` 生态。`CheshireMew/PuppetLoom`（★245）是更现实的中间态：不做编辑器，而是把「分层 PSD → 可自动制作、可验证、持续校准的 2D 角色」做成 Agent 可用的流水线（AGPL-3.0，商用要注意）。结论：**别等开源编辑器成熟**，眼下的正确姿势是 Cubism Editor Free 建模 + 上面第 1、3 条的 CLI/MCP 工具做自动化。
