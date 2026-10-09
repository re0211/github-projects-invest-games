# 第二十七辑 · Live2D —— GitHub 路
> 调研日期：2026-10-10 · 路线：GitHub · 去重基线：_r27/_dedupe_gh.txt（1182 项）+ _dedupe_urls.txt + _r26/_r26_gh.md

**本轮定位**：第二十六辑已收 32 条（psd2live / umamo / renpy-live2d / pixi-live2d-display / CubismWebFramework / CubismNativeFramework / Open-LLM-VTuber 等）。本轮只报**上一辑正文与剔除清单都没出现过的**仓库，沿 10 个新方向深挖：**SDK 各语言封装、模型查看器/调试器、格式转换与互操作、非 Ren'Py 引擎集成、AI 拆图后置流水线、桌宠/壁纸生态、面捕与 VTS 配套、moc3 逆向、Web 自研 runtime、停更考古**。

**贯穿全轮的一条成本事实（本轮最该记住的）**：Cubism **Core（运行时库）可在官网免费下载并接受协议后使用**，真正需要付费的是 **Cubism Editor / Pro 授权**。本轮大量项目（live2d-py、live-ascii、cubism-core-sys、live2d-web）都在 README 里明确写着「本仓库不含 Core，请自行从官网下载」——也就是说「预算有限」卡的是**做模型（绑骨）**，不是**跑模型（渲染）**。授权与价格细节见第二十六辑「授权与价格」分节，本轮不重复。

---

## 一、条目（32 条）

### 01. live2d-py（EasyLive2D/live2d-py）
- 链接：https://github.com/EasyLive2D/live2d-py
- 核实：⭐ 576 · MIT · C++ · updated_at 2026-10-01（pushed_at 2026-09-30）（命令：`gh api repos/EasyLive2D/live2d-py`）
- 一句话：用 Python C Extension 直接封装 Live2D Native SDK，在 Pygame / PySide6 / GLFW 等任何 OpenGL 窗口里加载并操作模型，支持 Cubism 2.1 与 3.0+。
- 可拓展性：**本轮对用户画像适配度最高的一条**。用户会 Python 不熟前端/着色器，而这是整个 GitHub 上唯一把 Live2D 运行时拉进 Python 主线的活跃项目（README 明确兼容 Pygame / PyQt5 / PySide2/6 / GLFW / pyopengltk / FreeGlut）。功能正好覆盖 VN 需要的东西：视线跟踪、口型同步、部件级透明度、**精确到部件的点击检测**、动作播放回调。和 Ollama 的接法很直接：qwen3 输出文本 → 自己写一层「情绪 → 参数名」映射 → `SetParameterValue` 推表情；这比 Open-LLM-VTuber（上一辑已收）那整套 Web 前端轻一个数量级。注意坑：README 明说**不含 Cubism Core 与 Framework**，需自行从官网下载（Core 免费，见开头说明），源码编译要 C++17 + CMake 3.26 + Python 3.11+。
- 实用性：**落地** —— 唯一与用户语言栈对得上的运行时，且 2026-09-30 仍在 push，MIT。

### 02. live2d-motion3（EasyLive2D/live2d-motion3）
- 链接：https://github.com/EasyLive2D/live2d-motion3
- 核实：⭐ 31 · MIT · Python · updated_at 2026-08-10（pushed_at 2026-05-15）（命令：`gh api repos/EasyLive2D/live2d-motion3`）
- 一句话：纯 Python 读写 `motion3.json`，附一个 PySide6 曲线编辑器，还能用 matplotlib 把动作曲线可视化。
- 可拓展性：**直接补上用户"买不起 Cubism Pro"的最大缺口**——Pro 授权买的是 Editor，而做动作动画的 Editor 功能被这个 31 star 的项目拆成了三块 Python 脚本：`motion_interpolate.py`（读 motion3 并用 `live2d-py` 的 `SetParameterValue` 播放）、`motion_visualize.py`（matplotlib 画曲线）、`Main.py`（能新建/打开/保存 `.motion3.json` 的动作编辑器，支持直线/三次贝塞尔/水平插值四种段类型）。意味着**不改一行前端、不装 Editor，就能给现成模型加自定义动作**。和 01 是同一作者的上下游，配合食用。依赖 PySide6 + live2d-py + matplotlib，Python 3.10+。
- 实用性：**落地** —— 用户是「会 Python 但没钱买 Editor」的典型受害者，这条就是他的解法；star 低不代表价值低。

### 03. Mocari（Eatgrapes/Mocari）
- 链接：https://github.com/Eatgrapes/Mocari
- 核实：⭐ 46 · MIT · Rust · updated_at 2026-10-07（pushed_at 2026-07-13）（命令：`gh api repos/Eatgrapes/Mocari`）
- 一句话：不依赖闭源 Cubism Core 的**纯 Rust 重实现 Live2D 兼容运行时**，默认不带渲染器，可选开启 wgpu 后端。
- 可拓展性：README 的动机写得比代码更有价值——「Live2D Cubism Core is closed source，长期只能用 native binding 调它，限制了可移植性」。它给出的是一条**彻底绕开 Core 授权**的路线：解析 + 参数/动作运行时 + 后端无关的 `render::common`（顶点、绘制排序、遮罩布局），自己接任何图形 API。已发 crates.io（`cargo add mocari`）。但版本 0.1、README 的 Status 段落是截断的，离"能跑通任意模型"还远。用户不熟 Rust，短期用不上。
- 实用性：**参考** —— 方向性标杆而非今日可用工具；价值在于验证「自研 runtime 可行」，且它选的 wgpu 后端是 WebGPU 路线（方向 9）。

### 04. live2d-cubism-core-sys（jz315/live2d-cubism-core-sys）
- 链接：https://github.com/jz315/live2d-cubism-core-sys
- 核实：⭐ 1 · MIT · Rust · updated_at 2026-04-05（pushed_at 2026-04-04）（命令：`gh api repos/jz315/live2d-cubism-core-sys`）
- 一句话：Cubism SDK Native Core **v5** 的裸 Rust FFI 绑定，通过环境变量指定 SDK 目录编译。
- 可拓展性：只做一件事——把 Core v5 的 C API 暴露给 Rust，且 README 给出了 Windows PowerShell 下 `$env:LIVE2D_CUBISM_SDK_NATIVE_DIR` / `CUBISM_CORE_LIB_DIR` 的完整配置。许可边界写得比同类清楚：MIT 只覆盖绑定代码，不覆盖 Core 本体。但对用户的实际帮助接近于零：他不用 Rust，且 01（live2d-py）已经把同一件事在 Python 侧做完了。
- 实用性：**剔除** —— 1 star、2026-04 后无更新、Rust 栈与用户完全不搭；保留它只为说明本方向已搜到底（Rust 侧目前只有这一条 v5 绑定）。

### 05. live2d-web（Heonys/live2d-web）
- 链接：https://github.com/Heonys/live2d-web
- 核实：⭐ 2 · MIT · TypeScript · updated_at 2026-09-01（pushed_at 2026-09-01）（命令：`gh api repos/Heonys/live2d-web`）
- 一句话：不依赖 PixiJS 的**自研 WebGL2 Live2D runtime**（React 组件 + hooks），自带 devtools 面板、**model inspector** 与 MediaPipe 面捕（实验性）。
- 可拓展性：star 只有 2，但它是本轮方向 2「调试器」里功能最全的一个——同类项目只做"能看"，它额外给了 **Model inspector**（在线逐参数检查模型结构）和 **devtools panel**，这正是用户调模型时最缺的东西（不用开 Cubism Editor 就能看到模型有哪些参数、动作、表达式）。同时支持 Cubism 3/4/5、多模型共享一个 WebGL 上下文、按音量或 wLipSync 的口型同步。代价：npm 包 + TypeScript，用户不熟前端；Core 与模型文件需自托管。
- 实用性：**参考** —— 不是让他拿去做产品，是让他拿 **inspector** 当免费的"模型体检工具"，抄它的参数枚举思路回 Python（01）用。

### 06. untitled-pixi-live2d-engine（Untitled-Story/untitled-pixi-live2d-engine）
- 链接：https://github.com/Untitled-Story/untitled-pixi-live2d-engine
- 核实：⭐ 78 · MIT · TypeScript · updated_at 2026-09-28（pushed_at 2026-09-20，open issues 12）（命令：`gh api repos/Untitled-Story/untitled-pixi-live2d-engine`）
- 一句话：面向 **PixiJS v8 + Cubism 5** 重写的 Live2D 渲染引擎，原生 Render Pipe、纹理 LOD、自动高精度遮罩。
- 可拓展性：上一辑收的 `guansss/pixi-live2d-display` 卡在 PixiJS v6/v7 且多年不 push；这条是它的**代际继承者**（README 自述 fork 自 Sekai-World 的 mulmotion 分支后大幅重构）。对用户唯一但很实在的价值是 **Texture LOD**：4096px 以上大图集可选 `single-auto`（按模型实际屏幕尺寸按需生成低分辨率纹理，降低显存）——16GB 内存 + 集显/入门独显的机器上，这条直接关系到 VN 会不会卡。另外它注册了原生 Render Pipe，能参与 zIndex 排序与混合模式，不会像老方案那样在滤镜下糊掉。
- 实用性：**参考** —— 技术选型是对的（PixiJS v8 + Cubism 5 是当前 Web 正路），但用户不熟前端，短期只能作为"将来要做 Web 版/网页特典时"的备案。

### 07. live2d-moc3（LitStronger/live2d-moc3）
- 链接：https://github.com/LitStronger/live2d-moc3
- 核实：⭐ 92 · NOASSERTION（无明确许可）· JavaScript · updated_at 2026-10-08（pushed_at 2021-02-05）（命令：`gh api repos/LitStronger/live2d-moc3`）
- 一句话：网页加载新版 **moc3** 模型的轻量方案（基于 AzurLaneL2DViewer 修改），可选宽高/定位/透明度/移动端开关。
- 可拓展性：价值在于它证明「不引官方 Framework 也能在浏览器里跑 moc3」，且参数化做得很省事（`basePath` + `role` 两个必填项就能挂一个模型）。对用户的用处：拿它当**本地模型快检页**——把 psd2live/拆图流水线产出的模型丢进去看有没有破面，比装 Editor 快。但两个硬伤必须写清楚：**NOASSERTION（无许可证）**，商用有风险；**pushed_at 2021-02-05**，五年没动，`updated_at` 新只是因为有人点 star/watch。
- 实用性：**参考** —— 停更 + 无许可，只借鉴思路，不直接进工程。

### 08. Live2dV3（HCLonely/Live2dV3）
- 链接：https://github.com/HCLonely/Live2dV3
- 核实：⭐ 61 · MIT · JavaScript · **archived=true** · updated_at 2026-08-29（pushed_at 2020-04-18）（命令：`gh api repos/HCLonely/Live2dV3`）
- 一句话：在网页上添加 moc3 格式 Live2D 模型的看板娘挂件（已被作者归档）。
- 可拓展性：与 07 同属"免 Framework 网页挂件"，但**是 MIT**，许可干净，代码量小、好读。对一个想把 VN 宣传页/itch.io 页面挂上会动立绘的学生来说，MIT 的停更项目反而比无许可的活跃项目更可抄。缺点是 2020 年停更，只覆盖当时（Cubism 3）的模型结构。
- 实用性：**参考** —— 明确停更（archived），仅供抄结构与挂件定位逻辑；许可干净是它相对 07 的优势。

### 09. live2d-interactive-viewer（jason71708/live2d-interactive-viewer）
- 链接：https://github.com/jason71708/live2d-interactive-viewer
- 核实：⭐ 1 · NOASSERTION · HTML · updated_at 2026-04-15（pushed_at 2025-11-02）（命令：`gh api repos/jason71708/live2d-interactive-viewer`）
- 一句话：带完整**表达式与动作控制面板**的浏览器端 Cubism 3 模型查看器，支持键盘快捷键。
- 可拓展性：典型"star 低但对这个人有用"：它不需要 npm、不需要构建，是个纯 HTML 页——用户最怕的正是前端工具链。用法是把它扔到本地、指到模型目录，就能逐个试表达式（exp3）和动作（motion3），确认哪些参数名可用，**再把参数名抄回 01/02 的 Python 代码里**。1 star 意味着没人维护，出问题是常态。
- 实用性：**参考** —— 零构建的参数面板，配合 01/02 当作"模型参数字典生成器"用；无许可，别分发。

### 10. live2d-lipsync-viewer（NyarchLinux/live2d-lipsync-viewer）
- 链接：https://github.com/NyarchLinux/live2d-lipsync-viewer
- 核实：⭐ 8 · GPL-3.0 · JavaScript · updated_at 2026-09-07（pushed_at 2026-08-20）（命令：`gh api repos/NyarchLinux/live2d-lipsync-viewer`）
- 一句话：在浏览器里预览 Live2D 模型并同步口型。
- 可拓展性：把"口型对不对"从 VN 工程里独立出来单独验——用户如果要接 TTS（哪怕只是 Ren'Py 里已有的语音），口型不同步是最容易被玩家察觉的破绽。它把 wLipSync / 音量驱动这一层单独做成一个可交互页，可以直接拿来标定自己模型的口型参数范围。GPL-3.0 有传染性，抄代码进闭源 VN 要慎重。
- 实用性：**参考** —— 用途窄（只验口型）但不可替代；GPL-3.0 是进工程的障碍。

### 11. renderkit（KurisuMakise004/renderkit）
- 链接：https://github.com/KurisuMakise004/renderkit
- 核实：⭐ 29 · Unlicense · Jupyter Notebook · **archived=true** · updated_at 2026-10-02（pushed_at 2026-10-02）（命令：`gh api repos/KurisuMakise004/renderkit`）
- 一句话：CLI 工具，把 MMD / VRM / **MOC3** 模型渲染成 albedo、depth、法线、UDP 坐标图。
- 可拓展性：本轮方向 3 里唯一做「**模型 → 训练数据**」这一侧的：把 moc3 渲成 depth/normal/UDP 贴图，可用于给 ControlNet / 图生图做条件。和用户手上 Ollama 的接法：Ollama 是 LLM，不能直接吃图；但如果他将来要给角色做「同姿势不同服装/不同光照」的批量出图，这条能批量产出条件图。有 Windows 预编译 zip（README 给了链接）。注意 **archived=true**，且 Unlicense 虽然宽松但仓库归档说明作者已不维护。
- 实用性：**参考** —— 有 Windows 可执行包、方向独特，但用户当前目标是「让立绘动起来」而不是「造训练数据」，优先级靠后。

### 12. moc3-reader-re（QiE2035/moc3-reader-re）
- 链接：https://github.com/QiE2035/moc3-reader-re
- 核实：⭐ 17 · NOASSERTION · Java · **archived=true** · updated_at 2026-06-07（pushed_at 2022-07-21）（命令：`gh api repos/QiE2035/moc3-reader-re`）
- 一句话：通过**逆向** Live2D Cubism 得到的 moc3 文件读写器（能读结构，写回需先清 offset list）。
- 可拓展性：**⚠️ 法律风险提示（必须随条保留）**——这是逆向私有二进制格式的产物，作者自己标注「some names may be wrong」，仓库 NOASSERTION 且已归档。合理用途只有一种：**在本地读源码学习 moc3 的结构布局**（配合 03 Mocari 的公开重实现交叉验证，理解 moc3 段表是怎么组织的）。**不要**把它的产物用于分发、二次发布模型、或任何商业场景；也不要据此声称自己"还原了"官方格式。作者 TODO 里还留着「Reverse to cmo3」的划线项，说明工程止步于半途。
- 实用性：**参考**（限学习用途）—— 方向 8 唯一找到的成型逆向产物；价值在"看懂格式"，不在"拿来用"。

### 13. LpkUnpacker（ihopenot/LpkUnpacker）
- 链接：https://github.com/ihopenot/LpkUnpacker
- 核实：⭐ 295 · NOASSERTION · Python · updated_at 2026-10-03（pushed_at 2026-04-07，open issues 8）（命令：`gh api repos/ihopenot/LpkUnpacker`）
- 一句话：解包 Live2DViewerEx 的 `.lpk` 文件，带 GUI 版 exe，还能在软件内直接预览模型（软件渲染 + 网页渲染两种）。
- 可拓展性：上一辑收了 `Arkueid/lpk2moc3`（同用途、Python、已归档），这条是**另一个作者、仍在维护、且提供 GUI exe** 的平行实现——用户是 Windows 且不愿折腾命令行的话，exe 直接双击就能用。README 承认对 STD_1_0 之前的早期 lpk 仍有少部分解不开。**⚠️ 法律提示**：lpk 是 Live2DViewerEx 的加密封装格式，解包只应用于**自己合法获得/购买**的模型（比如自己导出的备份），把 Steam 创意工坊的他人作品解包再分发是明确的侵权+违反平台条款的行为。NOASSERTION 也意味着代码本身没有授予你使用许可。
- 实用性：**参考** —— 工具能力真实且 Windows 友好，但用途本身站在法律灰区，且下一辑不该再往这个方向扩；给"参考"而非"剔除"是因为它对"找回自己买过的模型"有正当用途。

### 14. CubismNativeSamples（Live2D/CubismNativeSamples）
- 链接：https://github.com/Live2D/CubismNativeSamples
- 核实：⭐ 239 · NOASSERTION ·（语言字段为空，实为 C++ 官方样例集）· updated_at 2026-09-21（pushed_at 2026-04-02）（命令：`gh api repos/Live2D/CubismNativeSamples`）
- 一句话：官方 Native SDK 的配套示例集（README 顶部挂着 Cubism 5 SDK for Native R2 将终止 Cocos2d-x 支持的通知）。
- 可拓展性：上一辑收了 `Live2D/CubismNativeFramework`（框架层），这条是**官方样例层**，两者是同一产品线的不同层。对用户的价值很具体：01（live2d-py）就是对这套 Native SDK 的 Python 封装，**读这里的样例能看懂参数/动作/表达式的官方 API 语义**，比读 live2d-py 的二次封装更接近源头。另外 README 那份"Cocos2d-x 支持终止"通知是本轮方向 4 的重要情报——意味着 16（Cocos 路线）之类的集成正在失去官方支持。
- 实用性：**参考** —— 官方文档性质的代码库，不直接进工程，但是理解 01 底层的必备读物。

### 15. UnrealLive2D（Arisego/UnrealLive2D）
- 链接：https://github.com/Arisego/UnrealLive2D
- 核实：⭐ 153 · MIT · C++ · **archived=true** · updated_at 2026-09-08（pushed_at 2025-02-26，open issues 7）（命令：`gh api repos/Arisego/UnrealLive2D`）
- 一句话：UE4 的 Live2D 模型插件。
- 可拓展性：UE4 插件、已归档、153 star 但 issues 挂着 7 个未处理。用户在做 Ren'Py 视觉小说，UE4 是完全不同的技术栈（C++ 蓝图 + 数 GB 引擎体积，对 16GB 内存学生也不友好）。
- 实用性：**剔除** —— 栈不匹配 + 已归档。本条的存在只为证明方向 4（引擎集成）已覆盖到 UE 分支。

### 16. Live2dForCocosCreator（playnb/Live2dForCocosCreator）
- 链接：https://github.com/playnb/Live2dForCocosCreator
- 核实：⭐ 72 · NOASSERTION · TypeScript · updated_at 2026-09-19（pushed_at **2019-12-23**，open issues 6）（命令：`gh api repos/playnb/Live2dForCocosCreator`）
- 一句话：Cocos Creator 的 Live2D 集成组件。
- 可拓展性：三重问题叠加——① `pushed_at` 停在 2019-12-23，`updated_at` 新只是 star 数变动，典型「僵尸仓库」；② NOASSERTION 无许可；③ 结合 14 的官方通知，**Cubism 5 SDK for Native 将终止对 Cocos2d-x 的支持**，这条路线的官方上游正在关闭。用户做 Ren'Py VN，Cocos 也非其栈。
- 实用性：**剔除** —— 停更 + 无许可 + 官方上游终止支持，三重劝退。

### 17. GDLive2D（Watunder/GDLive2D）
- 链接：https://github.com/Watunder/GDLive2D
- 核实：⭐ 3 · NOASSERTION · C++ · updated_at 2026-05-01（pushed_at 2026-05-18，open issues 2）（命令：`gh api repos/Watunder/GDLive2D`）
- 一句话：**Godot 4** 的 Live2D 模块（GDExtension），README 自称 WIP。
- 可拓展性：上一辑收的 `MizunagiKB/gd_cubism` 是 Godot 3/4 的 C++ 玩家实现，这条是**另一个独立作者的 GDExtension 路线**，3 star 且 WIP、无许可。对用户有意义的点不在项目本身，而在它指向的方向：**Godot 4 有成熟的开源 VN 框架（Dialogic 之类）且完全免费**，是"Ren'Py 的 Live2D 太难接"时的 B 计划。但本项目本身成熟度不足以支撑 B 计划。
- 实用性：**参考** —— 只看不碰；它的价值是提醒用户存在 Godot 4 这条备用路线，真正的落地要等 gd_cubism 或本项目成熟。

### 18. Tyrano-Live2d-Plugin（FlowerCat-chen/Tyrano-Live2d-Plugin）
- 链接：https://github.com/FlowerCat-chen/Tyrano-Live2d-Plugin
- 核实：⭐ 0 · MIT · JavaScript · updated_at 2025-04-05（pushed_at 2025-04-05，创建于 2025-04-05）（命令：`gh api repos/FlowerCat-chen/Tyrano-Live2d-Plugin`）
- 一句话：TyranoScript（网页版 VN 引擎）的 Live2D 补丁，作者标注为修改版本。
- 可拓展性：**0 star、创建当天即停更**，单看数据应当剔除。留它的理由是方向 4 的完整性：TyranoScript 是**纯 HTML/JS 的视觉小说引擎**，和 Ren'Py 是同类竞品，而"网页引擎 + Live2D"的耦合天然比"Python 引擎 + 原生 SDK"顺畅得多（上一辑的 renpy-live2d 停在 2021，正是卡在这里）。用户如果哪天受够了 Ren'Py 的 Live2D 接入，TyranoScript 是迁移成本最低的替代品之一（脚本写法与 Ren'Py 相似，且自带中文社区）。MIT 许可。
- 实用性：**参考** —— 代码本身不可用（0 star / 单日提交），价值是标记出"TyranoScript 这条网页 VN 替代路线"存在。

### 19. rievegh（lightlyss/rievegh）
- 链接：https://github.com/lightlyss/rievegh
- 核实：⭐ 12 · NOASSERTION · Ren'Py · updated_at 2026-06-18（pushed_at 2019-11-06）（命令：`gh api repos/lightlyss/rievegh`）
- 一句话：Ren'Py 里 **Live2D + 动态视差相机**的可运行模板，README 说在 Ren'Py 7.3.0.271 / Windows 7 下测试过。
- 可拓展性：上一辑收了 `asfdfdfd/renpy-live2d`（纯 Live2D 模块，2021 停更）；这条是**同一个圈子里唯一把 Live2D 和视差相机拼在一起、且仓库里直接带了 Cubism 3 SDK Core 以便跑起来**的模板——对"我想立刻看到效果"的学生来说，"能跑起来"比"设计优雅"重要得多。两个必须知道的坑：作者自己写「Live2D coupling is fairly experimental」并建议「如果需要这类 mod，不如换 Unity」；另外 README 的 Disclaimer 明说**随仓库附带的 Core 仅供跑 demo，商用需自行遵守相应许可**（这与本轮开头那条"Core 免费下载"并不冲突——免费下载 ≠ 可随项目再分发）。另 2019 停更、Ren'Py 7 时代，Ren'Py 8 需自行移植。
- 实用性：**参考（考古）** —— 与用户核心栈完全对口但停在 2019；抄它的相机 + Live2D 联动写法，Core 自己另下一份。

### 20. RenpyLive2DEyeFollowDemo（rc14193/RenpyLive2DEyeFollowDemo）
- 链接：https://github.com/rc14193/RenpyLive2DEyeFollowDemo
- 核实：⭐ 4 · MIT · Ren'Py · updated_at 2026-06-18（pushed_at **2025-09-26**）（命令：`gh api repos/rc14193/RenpyLive2DEyeFollowDemo`）
- 一句话：Ren'Py + Live2D 下让**模型眼睛跟随鼠标光标**、点击时切换动作的演示工程。
- 可拓展性：**本轮最"小而准"的一条**。4 star 但它是 2025 年的、MIT 的、纯 Ren'Py 脚本的——正好填上一辑 renpy-live2d（2021 停更）留下的空档，证明"Ren'Py 8 时代仍然有人在做这件事"。眼睛跟随 + 点击反馈是 VN 里性价比最高的两种"活起来"效果（不需要绑骨、不需要动捕，只要有模型参数就能做）。用户会 Python/Ren'Py 脚本，这个 demo 的 `rpy` 文件可以直接抄进自己的工程。
- 实用性：**落地** —— 许可干净、年份新、与用户栈 100% 对口、改动量小。star 数低在这里是纯噪声。

### 21. RenpyLive2DTraceSample（kojimio/RenpyLive2DTraceSample）
- 链接：https://github.com/kojimio/RenpyLive2DTraceSample
- 核实：⭐ 1 · Apache-2.0 · C#（仓库主体实为 Ren'Py 脚本 + 外部进程集成）· updated_at 2026-08-15（pushed_at 2025-07-04）（命令：`gh api repos/kojimio/RenpyLive2DTraceSample`）
- 一句话：用 Pymouth（口型）+ OpenSeeFace（面捕）通过**端口通信**驱动 Ren'Py 里的 Live2D 模型的示例工程。
- 可拓展性：**把用户的三件家当串成一条线的接线图**——Ren'Py（他的引擎）+ OpenSeeFace（免费面捕，上一辑已在去重基线里）+ 端口通信。README 说明思路是"在 Pymouth / OpenSeeFace 侧处理好动作数据后，通过端口把数据送进 Ren'Py"。这意味着他可以照同样的结构，把 Ollama（qwen3）当成一个"数据源"塞进同一个端口协议里：LLM 输出情绪标签 → 转成参数 → 推给 Ren'Py 的 Live2D。Apache-2.0 是同类里最宽松的许可之一。1 star、2025-07 后未更新，工程规模是 demo 级。
- 实用性：**落地** —— 与其说是成品，不如说是一张"Ren'Py ← 外部进程"的拓扑图；对想接 Ollama 的用户，这张图比代码值钱。

### 22. seethrough-live2d-pipeline（Kota-Ohno/seethrough-live2d-pipeline）
- 链接：https://github.com/Kota-Ohno/seethrough-live2d-pipeline
- 核实：⭐ 9 · MIT · Python · updated_at 2026-10-08（pushed_at 2026-09-21）（命令：`gh api repos/Kota-Ohno/seethrough-live2d-pipeline`）
- 一句话：把 ComfyUI-See-through 的粗糙分层输出，加工成**Cubism 能读、能绑骨的高质量分层 PSD**（再投影 → 边缘细化 → 面部清理 → ag-psd 写 PSD）。
- 可拓展性：**本轮对用户"静态立绘 → 会动的 Live2D"这个核心诉求贡献最大的一条**。上一辑只收了 `ComfyUI-See-through`（产出分层 PSD 的那一半），而实践中的共识是：**See-through 的直接产物离"能绑骨"还差三步**——这个 9 star 的 Python 项目就是那三步（`reproject.py` 用原图像素重投影 + 按 Live2D 标准图层顺序重组 + 放大到 4096px；`refine_edges.py` 原图软遮罩替换轮廓 alpha 去光晕；`clean_face.py` 清 face 层细线/污点），最后用 Node 的 `ag-psd` 写出 Cubism 一定读得开的 PSD。README 里还留了一条**花钱买不到的硬知识**：「Python 的 pytoshop 写出的 PSD，在 Cubism Editor 里会出现『图层名能识别但什么都不显示』，动/静 PSD 结构 diff 后发现分水岭是 header channels=4 / layer_count 为负 / global layer mask info 的有无」。文档另外还有失败排查表与检查点模板。作者诚实声明"并非全工程自动实现，也不保证静止 PSD 的绑骨品质"。依赖 Python（作者 3.14 验证）+ Node（v26）+ Real-ESRGAN ncnn-vulkan。
- 实用性：**落地** —— 用户会 Python、想从单张立绘起步、买不起 Editor 手工重绘；这条正好补上一辑断掉的那半截链路，且 MIT。

### 23. puppet-part-splitter（0ran/puppet-part-splitter）
- 链接：https://github.com/0ran/puppet-part-splitter
- 核实：⭐ 4 · NOASSERTION · JavaScript · updated_at 2026-09-30（pushed_at 2026-09-06，创建于 2026-09-06）（命令：`gh api repos/0ran/puppet-part-splitter`）
- 一句话：**纯浏览器端**的拆图工作台：把插画/PSD 拆成可绑骨的部件层，或把多个透明素材自动打包成一张 sprite sheet。
- 可拓展性：三个特性正好命中用户约束——① **全本地、不上服务器**（16GB 机器也能跑，且不用把未公开立绘上传到任何在线服务）；② **不用装 Photoshop**（README 明说它是 Photoshop「导出图层到文件」的轻量替代，能批量把 PSD 图层导出成 PNG）；③ 自动连通域检测 + 三种分组模式（面积均衡/数量均衡/方向条带）+ 输出 JSON manifest，产物可直接给 Live2D / Spine / Wallpaper Engine / Unity / Godot 用。NOASSERTION 是唯一顾虑。与 22 的关系：22 走"AI 自动分层 + Python 精修"，这条走"半自动连通域拆分 + 人工核对"，**两条互补**，遇到 AI 分层翻车的图可以退回用这条手动兜底。
- 实用性：**落地** —— 无需 PS、无需上传、开箱即用，是拆图环节最低成本的兜底工具；许可未声明需自行向作者确认。

### 24. bongo-cat-next（liwenka1/bongo-cat-next）
- 链接：https://github.com/liwenka1/bongo-cat-next
- 核实：⭐ 151 · MIT · TypeScript · updated_at 2026-09-26（pushed_at 2026-08-16，open issues 5）（命令：`gh api repos/liwenka1/bongo-cat-next`）
- 一句话：现代化桌面宠物应用，内置 Live2D 猫咪，跟随打字/操作做动作。
- 可拓展性：Bongo Cat 一脉（用户画像方向 6 点名要找）。对 VN 作者的实际价值不在"养猫"，而在**它是一个 Live2D 模型的现成宿主**：把自己的模型换进去，就能零成本验证"这个模型在真实运行时里动作/口型/遮罩有没有问题"，比在 Ren'Py 里debug 快。MIT + 2026-08 仍有 push，是目前桌宠生态里最活跃的一条。
- 实用性：**参考** —— 不是用户主线产品，但作为"模型验收器"和"桌宠集成样例"值得留档。

### 25. petto（funnycups/petto）
- 链接：https://github.com/funnycups/petto
- 核实：⭐ 119 · GPL-3.0 · Dart · updated_at 2026-10-08（pushed_at 2025-12-05）（命令：`gh api repos/funnycups/petto`）
- 一句话：Flutter 写的智能 Live2D 桌面助手。
- 可拓展性：119 star、2025-12 仍在 push，项目本身是活的。但对**这个具体用户**三重不匹配：① Dart/Flutter 技术栈与他会的 Python 毫无交集，想改一行 UI 就得先学一套框架；② GPL-3.0 传染性许可，与他"做 VN 可能要分发"的目标冲突；③ 桌面助手不是他的产品形态（他要做的是视觉小说里的立绘）。同类需求 24 已用 MIT + TypeScript 覆盖。
- 实用性：**剔除** —— 栈、许可、产品形态三项全不匹配；24 已代表桌宠方向。

### 26. nep-live2d（guansss/nep-live2d）
- 链接：https://github.com/guansss/nep-live2d
- 核实：⭐ 73 · MIT · TypeScript · updated_at 2026-08-14（pushed_at 2023-01-04，open issues 20）（命令：`gh api repos/guansss/nep-live2d`）
- 一句话：跑在 Wallpaper Engine 上的 Live2D 动态壁纸（作者与已收的 pixi-live2d-display 是同一人）。
- 可拓展性：与上一辑的 `guansss/pixi-live2d-display` 是**同一作者的上下游关系**（那条是渲染库，这条是该库的壁纸应用），属于跨辑关联而非重复收录。价值有两点：① 它是"把 Live2D 塞进任意 WebView 宿主"的最小范本，用户想做 **itch.io 页面 / VN 宣传页 / 桌面壁纸**都能照抄；② 它演示了 Wallpaper Engine 场景下如何做资源打包与性能取舍（20 个 open issues 里大量是兼容性问题，本身就是一份"坑列表"）。停在 2023-01，MIT。
- 实用性：**参考** —— 停更 3 年，但作为"Web 宿主集成"的参考实现仍可读；MIT 保证可抄。

### 27. aklive2d（Halyul/aklive2d）
- 链接：https://github.com/Halyul/aklive2d
- 核实：⭐ 81 · GPL-3.0 · Python · updated_at **2026-10-09**（pushed_at **2026-10-09**）（命令：`gh api repos/Halyul/aklive2d`）
- 一句话：Python 工程，抓取官方数据为《明日方舟》的 Live2D 干员批量生成展示网页，可作 Windows 壁纸使用。
- 可拓展性：本轮**唯一在 2026-10-09 当天仍有真实 push 的 Python 项目**，且它示范了一件对用户有用的事：**用 Python 批量处理一批 Live2D 模型的元数据并生成可播放页面**（`pnpm run update` 拉数据、`build` 生成页面、可按单个角色构建）。他如果有一批自己做的模型要批量生成预览页/角色图鉴，这套脚本结构可以照搬。两点硬约束：① **GPL-3.0**；② 抓取的是商业游戏的运营资源，**照搬其抓取逻辑到别的游戏上有明确的侵权风险**，只能借鉴"生成展示页"的框架，不能借鉴数据源。
- 实用性：**参考** —— 框架可学、数据源不可学；GPL-3.0 也限制直接集成。

### 28. open-vt（erodozer/open-vt）
- 链接：https://github.com/erodozer/open-vt
- 核实：⭐ 282 · MIT · GDScript · updated_at 2026-10-06（pushed_at 2026-09-25，open issues 10）（命令：`gh api repos/erodozer/open-vt`）
- 一句话：**Godot 写的开源 2D VTuber 软件**，支持 OpenSeeFace 与 VTubeStudio（Wi-Fi TCP）两种追踪源，透明窗口便于 OBS 采集。
- 可拓展性：本轮方向 7「Open-LLM-VTuber 的替代品」里最值得写的一条，理由有四点：① **MIT + 2026-09-25 仍在 push**，是活项目；② 用 **Godot 而非 Unity** 构建——用户 16GB 内存跑不动 Unity 那套，Godot 是几十 MB 的事；③ **与 VTube Studio 资产兼容**（README 明确说两边可共用同一套文件、OpenVT 特有设置单独命名空间存放），意味着他不绑定任何商业软件；④ 支持 OpenSeeFace（免费面捕）与 VTS 两种输入。和 Ollama 的接法：把 qwen3 的输出经 29（pyvts）或 OpenSeeFace 通道送进来即可。与其 README 自称追求"feature parity with VTS"但不含插件生态与 VNet。
- 实用性：**落地** —— 如果用户的目标从"VN 立绘"外扩到"能动的角色 + 直播/录屏"，这是成本最低的开源宿主。

### 29. pyvts（Genteki/pyvts）
- 链接：https://github.com/Genteki/pyvts
- 核实：⭐ 133 · MIT · Python · updated_at 2026-10-04（pushed_at 2025-07-23，open issues 2）（命令：`gh api repos/Genteki/pyvts`）
- 一句话：Python 封装的 **VTube Studio API** 客户端库。
- 可拓展性：**把用户手上的 Ollama 变成"会动的角色"所需的最短一段胶水**。Open-LLM-VTuber（上一辑已收）是一整套解决方案，重、依赖多、且自带前端；pyvts 只做一件事——让 Python 能对 VTS 发指令（切换表情、触发动作、改参数）。于是链路变成：本机 Ollama qwen3 出文本 → 十几行 Python 做情绪判定 → pyvts 推给 VTS → 画面动起来。**全程 Python，不碰前端，不碰着色器**，正中用户的能力圈。MIT、133 star、issues 只有 2 个。注意 pushed_at 停在 2025-07-23，需确认对当前 VTS API 版本的兼容性（**未核实**）。
- 实用性：**落地** —— 对用户而言这是本轮"Ollama → Live2D"最短的路径；许可干净、语言对口。

### 30. live-ascii（Arcelyth/live-ascii）
- 链接：https://github.com/Arcelyth/live-ascii
- 核实：⭐ 234 · MIT · Rust · updated_at 2026-09-19（pushed_at 2026-08-29）（命令：`gh api repos/Arcelyth/live-ascii`）
- 一句话：在**终端里**渲染 Live2D Cubism 模型，支持面捕（OpenSeeFace UDP 11573）与热键动作面板。
- 可拓展性：star 数（234）在 Rust 侧一众绑定里最高，但要如实说明它对**这个用户**的门槛：需要 Rust 工具链 + 自行下载 **Cubism Core 5-r.5** + 另跑 OpenSeeFace，Windows 下 `.env` 指向 SDK 目录后才能 `cargo run`。所以不是"拿来即用"。它真正的价值是**证明一件事**：只要拿到免费的 Core，自己写渲染后端（这里是终端字符画）完全可行、且不需要 Cubism Editor 参与——这个结论对 01/02/03 那条"绕开 Pro 授权"的路线是重要旁证。另外它还示范了 `model_name.live.json` 这种**外挂式交互配置**（热键 → 动作映射），用户可以直接把这种配置思路搬到 Ren'Py 侧。
- 实用性：**参考** —— 概念价值 > 实用价值；Windows + 非 Rust 用户的上手成本偏高。

### 31. CubismViewer（Live2D/CubismViewer）
- 链接：https://github.com/Live2D/CubismViewer
- 核实：⭐ 46 · NOASSERTION · C# · updated_at 2026-10-02（pushed_at **2018-04-20**）（命令：`gh api repos/Live2D/CubismViewer`）
- 一句话：**官方**的 Cubism 模型查看器，README 首行即写明「[CAUTION] This repository is not actively maintained.」
- 可拓展性：纯考古条目。官方自己承认停更（最后一次 push 是 2018-04），NOASSERTION 无开放许可。它值得记一笔的理由是：它是**官方参数面板的最早形态**，想理解"一个 Live2D 调试器应该暴露哪些参数、怎么组织动作/表达式/部件三组面板"，这是源头参考；同类现代替代应看 05（live2d-web 的 inspector）与 09。C#/Windows 形态与用户环境兼容，但代码已 8 年无人维护。
- 实用性：**参考（仅供考古）** —— 官方明示不再维护；只用于理解调试器的信息架构，不要指望它能打开 Cubism 4/5 的新模型（**未核实**其兼容上限）。

### 32. Cubism3-ARKit（matsune/Cubism3-ARKit）
- 链接：https://github.com/matsune/Cubism3-ARKit
- 核实：⭐ 56 · NOASSERTION · C++ · updated_at 2025-10-11（pushed_at **2018-08-18**，创建于 2018-08-18 当天）（命令：`gh api repos/matsune/Cubism3-ARKit`）
- 一句话：用 **ARKit 面部捕捉**驱动 Cubism 3（Live2D）模型的 Demo App。
- 可拓展性：方向 7「iFacialMocap 开源替代」这条线上能找到的**最早公开样例**：它演示的是"ARKit 的面捕 blendshape → Cubism 参数"的映射关系。上一辑收的 `adrianiainlam/facial-landmarks-for-cubism` 走的是 **OpenSeeFace（摄像头）** 路线，这条走的是 **ARKit（深度摄像头 / TrueDepth）** 路线，两者是不同的输入源与精度层级，**不构成重复**。但对这个用户几乎不可复现：需要 iPhone（带 TrueDepth）+ Xcode + macOS 编译，他是 Windows 学生；且创建当天即停更、NOASSERTION。
- 实用性：**参考（仅供考古）** —— 2018 单日提交、需 Apple 全家桶；价值只在"ARKit → Cubism 参数映射表"这份历史资料，可与 28/21 的 OpenSeeFace 路线对照理解。

---

## 二、本路统计与给主 agent 的三句话总结

### 2.1 去重执行情况

**执行的检查**（每条候选在写入前都跑过）：

```bash
# ① 1182 项 owner/repo 基线（整行精确匹配）
grep -qi -- "^<owner/repo>$" D:/34498/Documents/github-projects-invest-games/_r27/_dedupe_gh.txt
# ② URL 基线
grep -qi -- "<owner/repo>" D:/34498/Documents/github-projects-invest-games/_r27/_dedupe_urls.txt
# ③ 上一辑原始稿
grep -qi -- "<owner/repo>" D:/34498/Documents/github-projects-invest-games/_r26/_r26_gh.md
```

**本轮剔除 / 让位的对象与理由：**

| 对象 | 命中来源 | 形态 | 处置 |
|---|---|---|---|
| `zwa73/UnityLive2DExtractor-Unofficial`、`UlyssesWu/D2Evil`、`Konata09/Live2dOnWeb`、`Veykril/cubism-rs`、`SakuraMotion/PurismCore`、`Jelosus2/BD2-L2D-Viewer` | `_r26_gh.md` §2.2 剔除清单 | 上一辑已评估并剔除 | 继承结论，不重复收录 |
| `aethiopicuschan/cubism-go`、`qinyonghang/Live2D-Python`、`Ludentes/py-moc3`、`respectZ/blue-archive-viewer`、`kiraio-moe/NikkeViewerEX`、`NovaPlayzGames/model-reaper`、`xiazeyu/live2d-widget.js`、`Inochi2D/inochi2d`、`P1kaj1uu/ChattyPlay-Agent` | 同上 | 上一辑剔除清单点名 | 同上；其中 `cubism-go`/`Live2D-Python`/`py-moc3` 三个语言绑定本轮改用**上一辑没见过的** Rust/Java/Lua 侧条目填补方向 1 |
| `guansss/pixi-live2d-display`（上一辑 04） | `_r26_gh.md` | 同作者上下游 | 本轮 26（nep-live2d）是其壁纸应用，属跨辑关联，已在条目内说明关系，不算重复 |
| `asfdfdfd/renpy-live2d`（上一辑 03） | `_r26_gh.md` | 同主题 | 本轮 19/20/21 均为**不同的** Ren'Py Live2D 工程（视差相机版 / 2025 眼随版 / 面捕接线版），非换名复现 |
| `jtydhr88/ComfyUI-See-through`（上一辑 15） | `_r26_gh.md` | 上下游 | 本轮 22 是其**后置精修流水线**，条目内已显式说明是"补上一辑断掉的半截链路" |
| `Bellpepperknuthamsun280/ComfyUI-See-through`、`untrained-devilray248/ComfyUI-See-through` | 本轮检索发现 | **同稿多镜像 / 抄袭改名**（与 `jtydhr88/ComfyUI-See-through` 描述逐字相同） | 剔除，未写入条目 |
| `Chaoray/AzurLane-Live2D-Viewer`、`kongbaiku/Live2D-M`、`rogeraabbccdd/SDVX-Wallpaper`、`moonheart/mementomori-models`、`namv22/GFL-Live2D-Viewer`、`ImDuck42/Live2D-Viewer` 等一批"某游戏模型查看器" | 本轮检索发现 | 垂直重复（彼此只差游戏名） | 只保留 2 条代表：07（免 Framework 派，游戏侧来源）与 08（MIT 派，许可干净可抄），其余让位 |
| `momori777/Artemis`、`DasterProkio/awesome-ai-companion`、`Voine/ChatWaifu_Mobile`、`morettt/my-neuro`、`xiazeyu/live2d-widget` 系 | 本轮检索发现 | 主题漂移（主体是 AI 伴侣 / 资源收集 / 榜单，Live2D 只是其中一个组件） | 剔除，避免与前几辑的"AI 伴侣"主题撞车 |
| 各类 `CubismSdkForWeb-5-r.X` / `CubismSdkForJava-5-r.X` 私人副本（`lindenthink`、`johnnywang1994`、`Jinggege123`、`ltarcher`、`anining`、`Nareerat-65` 等 7+ 个） | 本轮检索发现 | **ID 新 ≠ 内容新**（官方 SDK 的私人拷贝/微调，0 star） | 全部剔除 |
| `HELPMEEADICE/Neocari`（Mocari 派生）、`impossibletea/liver`、`KuroZetsubou/Live2DViewer`（macOS-only）、`shinkuan/Waifuland`（Linux Wayland-only） | 本轮检索发现 | 换名派生 / 平台不匹配（用户 Windows） | 剔除 |

**五种去重形态核对**：① 换名（ComfyUI-See-through 两个换名镜像、Neocari 派生）✅ 已剔；② 旧闻换日期（本路全部数据来自本轮 `gh api` 实时拉取）✅ 不适用；③ 转载（全部为 GitHub 原始仓库）✅；④ **ID 新 ≠ 内容新**（7 个官方 SDK 私人副本、多个 0 star 新建仓库，已逐个比对 `pushed_at`）✅；⑤ SEO 镜像站（本路为 GitHub 路，未引入 hqwc.cn / mhpn.cn 等站外链接）✅。

### 2.2 统计

- **条数**：32 条，全部附完整 GitHub URL 与 `gh api repos/...` 取数命令原文；star / 许可 / 语言 / updated_at / pushed_at / archived 全部来自本轮真实 API 返回，**无一项凭记忆填写**。
- **三档分布**：**落地 8 条**（01、02、20、21、22、23、28、29）；**参考 20 条**（03、05、06、07、08、09、10、11、12、13、14、17、18、19、24、26、27、30、31、32）；**剔除 4 条**（04、15、16、25）。
- **停更/考古专项**（方向 10）：08（archived，2020）、11（archived）、12（archived，2022）、19（2019）、31（官方明示停更，2018）、32（2018 单日提交）——6 条，全部在条目内标注了 `pushed_at` 年份与「仅供考古」。
- **法律风险专项**：12（moc3 逆向）、13（lpk 解包）、27（抓取商业游戏资源）——3 条，均在条目内以 ⚠️ 段落写明边界。
- **许可分布**：MIT **16** 条（01/02/03/04/05/06/08/15/18/20/22/24/26/28/29/30）、NOASSERTION（未识别到开放许可）**11** 条（07/09/12/13/14/16/17/19/23/31/32）、GPL-3.0 **3** 条（10/25/27）、Apache-2.0 **1** 条（21）、Unlicense **1** 条（11）。合计 32。**NOASSERTION 占比超过三分之一，是本轮的结构性特征**——Live2D 生态里大量"能用的小工具"从不声明许可，这对一个要分发 VN 作品的用户是实打实的障碍，已在上述 11 条中逐一标出。

### 2.3 给主 agent 的三句话总结

1. **本轮最重要的认知修正**：用户「买不起 Cubism Pro」卡的是**绑骨（Editor）**，不是**渲染（Core）**——Cubism Core 可免费下载，本轮 01（live2d-py，Python 直接封装 Native SDK）+ 02（live2d-motion3，纯 Python 编辑 motion3.json）组合起来，**让"不买 Editor 也能加载模型并自己编动作"成立**，这是上一辑没有给出的结论。
2. **对用户最该先做的三件事**（按 ROI 排序）：① 用 22（seethrough-live2d-pipeline）把 psd2live/ComfyUI-See-through 的粗糙分层 PSD 精修到可绑骨；② 用 23（puppet-part-splitter）当免 PS、免上传的拆图兜底；③ 用 20 + 21 的 Ren'Py 工程结构，把 Ollama qwen3 的情绪输出经 29（pyvts）或端口协议推进 Live2D——**全程 Python，不碰前端与着色器**。
3. **值得警惕的一件事**：本轮 9 条是 NOASSERTION（无开放许可），且 12（moc3 逆向）、13（lpk 解包）、27（抓商业游戏资源）三条站在法律灰区——用户是要做**可能分发的 VN** 的人，索引里凡涉及这三条，必须连同风险提示一起呈现，不能只报"工具很好用"。

### 2.4 本轮未核实到的空白（如实记录）

- **Cubism Editor / Pro 的具体价格与免费版条款**：本轮沿上一辑分工不碰授权与价格，所有"免费 / 付费"判断均来自各仓库 README 的自述（如"本仓库不含 Core，请自行下载"），**未核实官方定价页**。
- **29（pyvts）对当前 VTube Studio API 版本的兼容性**：`pushed_at` 停在 2025-07-23，VTS API 版本演进情况**未核实**，需在条目内提示用户自行验证。
- **31（CubismViewer）能打开的最高 Cubism 版本**：仓库 2018 年停更，**未核实**其对 Cubism 4/5 模型的兼容上限。
- **03（Mocari）的已实现功能清单**：README 的 `## Status` 段落在 API 返回中是截断的，只确认了"解析 + 参数/动作运行时 + 可选 wgpu 后端"，**具体支持到哪一步未核实**。
- **17（GDLive2D）、18（Tyrano-Live2d-Plugin）的实际可运行性**：两者均 star 极低且 README 极简（GDLive2D 自标 WIP），**未做克隆编译验证**，仅按元数据与文档判断。
- **11（renderkit）对 MOC3 的具体支持深度**：README 只在输入格式列表里提到 MOC3，示例全是 MMD/VMD/BVH，**MOC3 路径是否完整可用未核实**。
