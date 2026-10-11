# 第三十二辑 · gh 路调研（主题：Live2D 制作 × 实战测评 × 上新）

> 执行者：general-purpose-1（gh 路）
> 环境：Windows + gh api（git clone 不通）
> 基准人物：16GB RAM Windows + 本地 Ollama + 维护静态索引站的个人（游戏制作小白，主要用 Ren'Py）
> 说明：本辑为 Live2D 连续第七轮，重点找**未覆盖的新角度**。

## 子方向与命中情况
1. Cubism 5.3.x 版本更新 / 迁移工具
2. AI 驱动 Live2D（音频/摄像头/LLM 桌宠栈）
3. 运行时集成（Unity/UE/Godot/Web/Python）
4. 替代栈（Inochi2D/Spine/3D 化/单图转模型）
5. moc3 解析 / 逆向 / 压缩 / 优化
6. PSD 分层 / 自动切图 / 自动绑定
7. 商用授权 / 许可证清单

---

<!-- 以下为逐条调研结果，增量追加 -->

## 一、替代栈 / 开源木偶引擎（Inochi2D 生态新件 + 全新 Rust 栈）

### inox2d ★298 · Rust · NOASSERTION · 推送 2026-09-23
- 地址：https://github.com/Inochi2D/inox2d
- 一句话：Inochi2D 的**原生 Rust 重写版**运行时——不做 D 语言那套依赖，直接把傀儡（puppet）渲染带进 Rust 生态，附 OpenGL 与 WebGL 两个可跑示例。
- 为什么新：索引里 Inochi2D 只收了 D 语言的本体（inochi2d ★1811）与配它的编辑器（nijigenerate、iki）；**Rust 重写的运行时此前从未收录**，是一条独立的「把 Inochi2D 搬进非 D 栈」的新路。
- 可复用性：**参考** —— 基准人物不写 Rust 也不会编译它；但它的价值在于「Inochi2D 阵营在补运行时」这一信号：等它成熟，Web 端就有了不依赖 Cubism Core 的公开渲染路径。先记着，不现在动手。
- 证据：`gh api repos/Inochi2D/inox2d` → `{"stars":298,"license":"NOASSERTION","lang":"Rust","pushed":"2026-09-23T17:55:50Z"}`；`gh api repos/Inochi2D/inox2d/git/trees/HEAD?recursive=1` → 含 `examples/render-opengl/`、`examples/render-webgl/`、`Cargo.toml`
- 坑：license 显示 NOASSERTION（GitHub 没识别出标准 SPDX），商用前必须去仓库根看 LICENSE 原文。

### inochi-viewer ★47 · D 语言 · BSD-2-Clause · 推送 2026-09-15
- 地址：https://github.com/Inochi2D/inochi-viewer
- 一句话：官方出的**最小傀儡查看器**——只干一件事：打开 Inochi2D 傀儡文件看长什么样，不建模不改文件。
- 为什么新：这是 Inochi2D 官方工具链里「查看器」这一环，索引此前的 31 辑补了 SDK 本体 + 编辑器，但**查看器没单列**；对「先看成品再决定要不要接」的评估流程是刚需件。
- 可复用性：**不采用** —— 它是 D 语言 GUI 程序，Windows 上要现成二进制才行；对不碰 D 工具链的人来说价值有限。列出来只为让索引的 Inochi2D 工具链闭环。
- 证据：`gh api repos/Inochi2D/inochi-viewer` → `{"stars":47,"license":"BSD-2-Clause","lang":"D","pushed":"2026-09-15T08:59:37Z"}`
- 坑：D 语言项目在 Windows 上编译门槛高；优先找 Release 里的预编译包。

### inochi2d-toolkit ★0 · Python · MIT · 推送 2026-09-24
- 地址：https://github.com/yanjingzhaisun/inochi2d-toolkit
- 一句话：给 Inochi2D 写的**命令行 + MCP 服务**——在「只有 GUI 编辑器」的傀儡格式上做文件级读写、结构校验、往返自检（TRNSRTS 容器 I/O）。
- 为什么新：这是「用 agent/CLI 去操作一个**只提供 GUI** 的格式」的思路，索引里前一辑刚补了针对 **Cubism Editor** 的 MCP（nana7chi/CubismExternalEditMCP），这里是**同一思路换到 Inochi2D 侧**，且强调「文件级」而非「模拟点击 UI」。
- 可复用性：**参考** —— 不直接用（不玩 Inochi2D），但它揭示一条通用做法：GUI-only 的创作工具，可以用 CLI+MCP 在文件层绕过 UI，把「人点」变成「脚本改」。这对以后想自动化任何美术格式都有借。
- 证据：`gh api repos/yanjingzhaisun/inochi2d-toolkit` → `{"stars":0,"license":"MIT","lang":"Python","pushed":"2026-09-24T12:52:39Z"}`；desc 明写 "CLI first, MCP server on the same core … TRNSRTS container I/O, structural validation, round-trip self-checks"
- 坑：★0、单人、9 月刚建，API 会变；别写进正式流水线。

### inochi2d-autorig-claude ★0 · Python · 无 license · 推送 2026-10-05
- 地址：https://github.com/henceketh/inochi2d-autorig-claude
- 一句话：用 Claude 给 **Inochi2D** 做自动绑骨的项目——并在 README 里**明确划了硬边界**：Cubism 根本不能被全自动绑骨。
- 为什么新：它的价值不在代码，在**那句断言**。索引里已有多条「单图→模型自动化」的乐观项目（psd2live、image2live2d 等），这是第一条公开把话说明白的：「Inochi2D 能/ Cubism 不能」是**结构性硬限**，不是工程量问题。作者还给了折中方案——对 Cubism 只产出「绑骨配方」（图层改名、参数表、变形器规划、keyform 清单）交给人执行。
- 可复用性：**参考** —— 不采用它的 Prompt/脚本，但把「Cubism 自动绑骨 = 伪需求 / Inochi2D 自动绑骨 = 可行」这个判断抄进认知，能省掉大量试错。
- 证据：`gh api repos/henceketh/inochi2d-autorig-claude` → `{"stars":0,"license":null,"lang":"Python","pushed":"2026-10-05T01:40:14Z"}`；desc 原文含 "This rigs Inochi2D, not Live2D Cubism — Cubism cannot be autorigged at all."
- 坑：无 license；纯个人观点项目，断言需自己复核，勿当权威结论引用。

### ayatsuri_2d（操り2D） ★2 · Rust · GPL-3.0 · 推送 2026-09-13
- 地址：https://github.com/Yoru-KenomoVT/ayatsuri_2d
- 一句话：一个**从零写的开源替代栈**——Rust 实现 2D 傀儡实时变形 + 绑骨编辑器，宣称端到端支持 **moc3 v3 到 v6**，并自带 C ABI 让 Unity/UE/Godot/Python/JS 都能嵌入。
- 为什么新：索引里的开源替代（Inochi2D / nijigenerate / umamo / iki）要么做 Inochi2D 自己的格式，要么只读 `.cmo3`；**ayatsuri_2d 是目前唯一公开宣称「直接吃 moc3（v3–v6）」的独立运行时**，并自创 `.aom`（Ayatsuri Open Model，MessagePack 载荷）作为自己的保存格式。这是个敢正面碰 moc3 的新玩家。
- 可复用性：**不采用** —— 早期（README 自标 status: Early）、★2、GPL-3.0、且宣称的 moc3 支持未经第三方验证。但**列进索引很重要**：它是「开源替代」这条线第一次有人把枪口对准 moc3 兼容层，值得盯。
- 证据：`gh api repos/Yoru-KenomoVT/ayatsuri_2d` → `{"stars":2,"license":"GPL-3.0","lang":"Rust","pushed":"2026-09-13T12:58:51Z"}`；`gh api repos/Yoru-KenomoVT/ayatsuri_2d/git/trees/HEAD?recursive=1` → 含 `crates/openmoc3`、`crates/ayatsuri_format`、`crates/ayatsumi_abi`；README 徽章 `moc3 v3 to v6`
- 坑：①「支持 moc3 v3–v6」是作者**单方宣称**，README 也写 status=Early，勿轻信；②GPL-3.0 有传染性；③项目名/品牌（Ayatsuri/Yoru-KenomoVT）疑似新号，无历史信誉。

### live2drust ★0 · Rust · 无 license · 推送 2026-09-23
- 地址：https://github.com/rydanee/live2drust
- 一句话：一个 Rust 写的极简 `.moc3` 模型查看器（作者自谦 "more to come :)")。
- 为什么新：索引里 moc3 查看/解析工具此前是 C++（moc3ingbird）、JS（moc3-json-viewer）、Python；**Rust 侧读 moc3 是新语言实现**，正好和 inox2d、ayatsuri_2d 一起说明「Rust 正在成为 Live2D 逆向/运行时的活跃方向」。
- 可复用性：**不采用** —— ★0、无 license、功能仅查看。仅作为生态信号记录。
- 证据：`gh api repos/rydanee/live2drust` → `{"stars":0,"license":null,"lang":"Rust","pushed":"2026-09-23T12:28:00Z"}`
- 坑：无 license = 保留所有权利，默认不可复用其代码。

---

## 二、PSD / 资产流水线（自动切图 = 本轮最硬的新角度）

### illust2psd ★8 · Python · MIT · 推送 2026-03-29（仓库更新 2026-10-07）
- 地址：https://github.com/CVIndomitable/illust2psd
- 一句话：**单张角色立绘 → 可直接导入 Cubism 建模的多图层 PSD**——自动去背景 + 语义分割 + 面部精细拆分 + 遮挡区修复，输出符合 Cubism 图层命名规范的 RGB 8-bit PSD。
- 为什么新：索引里的「单图→模型」线此前全靠 **See-through** 那一套（Depth 拆层），而 illust2psd 走的是**另一条技术栈**：ISNet 去背景 + SAM2 语义分割 + OpenCV inpaint 补遮挡，并且**直接产出 Cubism 能吃的分层 PSD**（含固定图层命名表）。这是「PSD 分层规范/自动切图」子方向第一次有可跑的开源实现，且带 MCP server，可被 agent 调用。
- 可复用性：**参考（潜力高，但现在别押）** —— 自标 Alpha、★8、作者说「接口和输出格式可能随时变更，不建议生产环境」。但它给的**图层结构表**（Hair_Back→…→Hair_Front 从下到上、每层命名）可以直接抄进自己的立绘规格书；且它有 `configs/layer_taxonomy.yaml`，命名可配置。等它稳定值得再评。
- 证据：`gh api repos/CVIndomitable/illust2psd` → `{"stars":8,"license":"MIT","lang":"Python","pushed":"2026-03-29T03:28:19Z"}`；`gh api repos/CVIndomitable/illust2psd/git/trees/HEAD?recursive=1` → 含 `configs/layer_taxonomy.yaml`、`illust2psd/mcp_server/server.py`、`illust2psd/steps/s1_preprocess.py … s6_inpaint.py`
- 坑：①README 首行自标「实验性/Alpha，不建议生产」；②要跑 SAM2 + ISNet，16GB RAM 的机器对显存/内存是压力（未标最低配置）；③输出是「能导入」，**不是「绑好骨」**——绑骨仍要人。

### cormy-live2d ★0 · JavaScript · GPL-3.0 · 推送 2026-10-10
- 地址：https://github.com/jcs130/cormy-live2d
- 一句话：一个「可复现的 Live2D 角色制作源文件」合集——把某个角色的模型、表情、动作与**制作源文件**一起公开。
- 为什么新：索引里收的多是「工具」或「成品模型」，**「制作源文件 + 可复现 rig」这种教学/模板型仓库是空档**。对「想做第一个模型但不知道正规工程长什么样」的小白，这类仓库是拆解范本。
- 可复用性：**参考** —— 不采用其角色资产（别用别人的版权角色），但可以**下载它的源文件逐层对照**，学「正规的 Cubism 工程目录 / 参数 / 变形器」长什么样。属「看一眼少走弯路」类。
- 证据：`gh api repos/jcs130/cormy-live2d` → `{"stars":0,"license":"GPL-3.0","lang":"JavaScript","pushed":"2026-10-10T19:09:17Z"}`
- 坑：★0、2026-10-10 当天建仓；「可米 Cormy」是第三方角色，源文件**仅供学习**，商用必侵权；GPL-3.0 对衍生也有限制。

### whale-maid-svg-layers ★0 · Python · 无 license · 推送 2026-09-21（同源候选见去重报告）
- 地址：https://github.com/daoming07280/whale-maid-svg-layers
- 一句话：一个具体案例的**分层原始素材**——用 SVG 重绘的「蓝胖鲸女仆」，拆成 **59 层 PSD/SVG**，走 psd2live → moc3 流水线。
- 为什么新：这是「**先用矢量重绘再分层**」的路径（与 See-through 的位图拆层相反）：矢量重绘天然干净、层可无损缩放，代价是重绘的人工。索引里此前没有「矢量重绘 → 分层 → Live2D」这条具体做法。
- 可复用性：**参考** —— 采用它的「思路」（矢量重绘降低绑骨难度），不采用其素材。同时它和 daoming07280/live2d-auto-pipeline 是同作者，说明这是一条被反复走的私家流水线。
- 证据：`gh api repos/daoming07280/whale-maid-svg-layers` → `{"stars":0,"license":null,"lang":"Python","pushed":"2026-09-21T16:40:44Z"}`；desc 含 "59-layer PSD/SVG split for Live2D (psd2live → moc3 pipeline)"
- 坑：①无 license；②★0、个人实验；③「59 层」是否每层都合规可用未经验证。

---

## 三、moc3 逆向 / 迁移（老格式迁移是有历史包袱项目的新痛点）

### UnityLive2DExtractor-Unofficial ★57 · C# · MIT · 推送 2024-08-21（仓库更新 2026-10-05）
- 地址：https://github.com/zwa73/UnityLive2DExtractor-Unofficial
- 一句话：**社区维护版**的 Unity Live2D 提取器——原版 Perfare 的提取器（★634）早已不更新，这个 fork 继续修，把 Unity 工程里的 Live2D 资源扒回成 `motion3/physics3/model3`。
- 为什么新：索引里收的是**上游** perfare/UnityLive2DExtractor（★634，已停更）与另一个 fork UnityPyLive2DExtractor；这个 **zwa73 的 Unofficial 分支**没被单列，而它恰恰是「原版停更后能不能继续用」这个实际问题的答案。
- 可复用性：**参考（解包老游戏才有用）** —— 只有当你手上是 Unity 打包的 Live2D 游戏、想把里面的模型/动作掏出来时才有用；不做这个就无关。★57 说明确有需求存在。
- 证据：`gh api repos/zwa73/UnityLive2DExtractor-Unofficial` → `{"stars":57,"license":"MIT","lang":"C#","pushed":"2024-08-21T17:43:45Z"}`；`gh api repos/zwa73/UnityLive2DExtractor-Unofficial/git/trees/HEAD?recursive=1` → 含 `UnityLive2DExtractor/CubismModel3Json.cs`、`CubismMotion3Converter.cs`、`CubismPhysics3Json.cs`
- 坑：①代码停更在 2024-08；②**提取他人游戏模型有版权风险**，仅限自有/授权内容；③依赖 AssetStudio.dll 等预编译库。

### bang-dream-old-moc-game-import-workflow ★0 · 无语言 · 无 license · 推送 2026-10-07
- 地址：https://github.com/xez65/bang-dream-old-moc-game-import-workflow
- 一句话：一份「把 Bang Dream **老式 MOC 模型迁移到 MOC3 + Unity**」的可复核工作流文档。
- 为什么新：索引此前收的 moc3 都是「读」或「看」，**「旧格式→新格式的迁移流程」是没覆盖的场景**；且它强调「可复核」（每步可验证），是文档型而非工具型，适合当 checklist。
- 可复用性：**参考** —— 只有做「老资产翻新」才用得上；但对任何「手上有一堆旧模型要迁移」的人，这份分步流程有借鉴价值。
- 证据：`gh api repos/xez65/bang-dream-old-moc-game-import-workflow` → `{"stars":0,"license":null,"lang":null,"pushed":"2026-10-07T14:03:06Z"}`
- 坑：无 license、无语言（纯文档）、★0；Bang Dream 素材版权归武士道，**流程可学、素材不可用**。

### nnnotes ★15 · Python · MIT · 推送 2026-10-10
- 地址：https://github.com/MetaSekaiLab/nnnotes
- 一句话：BanG Dream! Our Notes **游戏文件的离线数据工具箱**——catalog/打包资源/masterdata/剧情/Live2D/音频 一站式解包。
- 为什么新：这是「从商业手游里把 Live2D 资源规范化提取出来」的完整工具链，索引里此前只有零散的 UnityLive2DExtractor，**没有面向具体游戏、成体系的数据工具箱**。
- 可复用性：**不采用** —— 版权用途明确（研究单个商业游戏），对自研项目无直接用途。列它为「游戏资产提取」补一个实例。
- 证据：`gh api repos/MetaSekaiLab/nnnotes` → `{"stars":15,"license":"MIT","lang":"Python","pushed":"2026-10-10T05:10:26Z"}`；desc 含 "catalogs, bundles, masterdata, stories, Live2D, audio and live charts"
- 坑：①解包商业游戏资产**仅供研究，不可商用/分发**；②另有同源 `empty-sekai/nnnotes-standalone`（★0），疑为同项目独立版（见去重报告）。

---

## 四、运行时集成（本轮最大发现：一个真能读 moc3 的开源渲染器）

### ayagami（彩紙） ★351 · Rust · Apache-2.0 / MIT 双许可 · 推送 2026-09-14
- 地址：https://github.com/AyagamiDev/ayagami（Web Demo: https://demo.ayagami.dev）
- 一句话：一个**从零黑盒逆向、完全开源**的 2D 木偶加载与渲染库——**直接读 Live2D 的 `.moc3`**，渲染器用 wgpu（Vulkan/Metal/DX/OpenGL/WebGL/WebGPU 全后端），作者宣称「不用付任何版税、无需任何人许可，商用/内置模型/加载用户模型的软件都能用」。
- 为什么新：这是本辑**最硬的一条**。索引里此前的「开源替代」要么不碰 moc3（Inochi2D 自己格式、umamo 只读 `.cmo3`），要么只做 JSON 不做网格（moc3ingbird/相关工具）。**ayagami 是第一条公开、活跃、且声称已实现 MOC3 加载 + 「SDK 5.3 features（advanced blend & off screen rendering）」的开源渲染器**，且 3 个月涨到 ★351。README 明确「support 到 SDK 5.0 的 MOC3 特性：Parts、ArtMeshes、旋转/弯曲变形器、Glue、Blendshape 参数；物理引擎已完成」。作者还特别划线：**只用黑盒逆向，从不反汇编/反编译专有软件**（并写了 contributor policy 保证），这是绕开 Live2D 专有许可的一个法律姿态。
- 可复用性：**参考（盯，别现在押）** —— ①API 自认 unstable、无文档、crates.io 还没发；②表达式/pose/动作文件仍是 TODO（只有加载 + 参数驱动 + 物理），做不了完整 VTuber；③对「用 Ren'Py 的个人」暂时接不上。但它是「**不买 Cubism、也能合法读 moc3 渲染**」这条链里目前最像样的候选，值得每辑复查一次进度。
- 证据：`gh api repos/AyagamiDev/ayagami` → `{"stars":351,"license":"Apache-2.0","lang":"Rust","pushed":"2026-09-14T14:19:06Z","created":"2026-07-11T13:51:22Z"}`；README 含 "Support MOC3 file loading & features up to SDK 5.0"、"SDK 5.3 features (advanced blend & off screen rendering) [x]"、"developed strictly using black-box reverse engineering only"
- 坑：①作者本人说 "API is pretty unstable … no documentation yet"；②LICENSE 双许可（README 说 MIT+Apache2，但 API 的 spdx 只识别出 Apache-2.0）——**引用时以仓库内 LICENSE 文件为准**；③「黑盒逆向合法」是作者法务主张，商用建议自行复核（尤其在日本/欧盟，专有格式逆向的法律地位各地不同）；④动作/表情文件未支持，模型「能动」但不完整。

### ayagami-gd ★39 · Rust · MIT · 推送 2026-09-15
- 地址：https://github.com/AyagamiDev/ayagami-gd
- 一句话：**Ayagami 的 Godot 绑定**——把上面那个 moc3 渲染器接进 Godot 引擎（另有官方 Web demo，见 AyagamiDev/demo）。
- 为什么新：索引里 Godot 侧的 Live2D 方案此前是 **gd_cubism**（MizunagiKB ★301，走官方 Cubism Native SDK）与 pakholeung37/gd_cubism（★0，批渲染优化）；**ayagami-gd 是「Godot + 非官方 moc3 渲染器」这条新组合**，且和 ★351 的母项目同一组织、更新同步。
- 可复用性：**参考** —— 不用 Godot 就不采用；但若哪天想「不装 Cubism SDK 也在 Godot 里放 Live2D」，这是目前唯一在维护的开源路线。
- 证据：`gh api repos/AyagamiDev/ayagami-gd` → `{"stars":39,"license":"MIT","lang":"Rust","pushed":"2026-09-15T14:45:20Z"}`
- 坑：依赖母项目 Ayagami，母项目 API 不稳定 → 绑定也不稳定；Godot 需 4.7（见 manosaba-live2d 说明）。

### Godot-Live2D（GDLive2D） ★17 · GPL-3.0 · 推送 2022-05-28（仓库更新 2026-08-26）
- 地址：https://github.com/qzwxsaedc/Godot-Live2D
- 一句话：Godot 里用 C++（GDNative）写的 Live2D 插件——把 Cubism 模型塞进 Godot 4，Node2D 上挂脚本即可。
- 为什么新：Godot 侧索引收了官方路线的 gd_cubism，但这是**另一套独立实现**；且它的 README 把「`Model Name` 必须 = 目录名 = `.model3.json` 名」这条**硬约束**写得很清楚，是个好排错范本。
- 可复用性：**参考（但注意停更）** —— 代码停在 2022-05，target Godot 4.3 ABI；只是为了对比「Godot 接 Live2D 有几种写法」时才看。实际用请走 gd_cubism 或 ayagami-gd。
- 证据：`gh api repos/qzwxsaedc/Godot-Live2D` → `{"stars":17,"license":"GPL-3.0","lang":null,"pushed":"2022-05-28T14:56:48Z"}`；README 含「模型名称要求模型名称=模型目录名称=模型的.model3.json文件名」
- 坑：①已停更（2022）；②GPL-3.0；③GDNative 是 Godot 旧扩展方式，新版本推荐 GDExtension。

### manosaba-live2d ★0 · C++ · 无 license · 推送 2026-09-16
- 地址：https://github.com/pakholeung37/manosaba-live2d
- 一句话：一份 **Godot 4 的端到端 Live2D 对比 demo**——同一个模型、两条运行时并行跑：一条走 gd_cubism v0.9.1 + Cubism Native 5-r.5，另一条走 Ayagami（Rust）。
- 为什么新：它的价值是**对照实验台**：索引里没有任何条目把「官方 SDK 路线」与「开源渲染器路线」放在同一个 Godot 工程里现场比。而且它顺带暴露两个实测事实：gd_cubism 的二进制仍 target **Godot 4.3 ABI**，而内置的 Ayagami 扩展需要 **Godot 4.7**。
- 可复用性：**参考** —— ★0、无 license、单人；不能直接用。但它是「想知道 ayagami 到底能不能在 Godot 里跑起来」时最快的一手信号源。
- 证据：`gh api repos/pakholeung37/manosaba-live2d` → `{"stars":0,"license":null,"lang":"C++","pushed":"2026-09-16T07:51:48Z"}`；README 含 "gd_cubism v0.9.1 + Live2D Cubism SDK for Native 5-r.5"、"Ayagami Rust runtime"、"requires Godot 4.7"
- 坑：①无 license；②★0、路径写死 macOS（README 里全是 `/Applications/...`）；③只是 demo，非产品。

### ZerolanPlayground ★32 · C# · 无 license · 推送 2025-07-01（仓库更新 2026-09-15）
- 地址：https://github.com/AkagawaTsurunaki/ZerolanPlayground
- 一句话：用 Unity + Vuforia 做的 **AR 虚拟角色展示**——把 Cubism Live2D 模型叠到摄像头实拍上。
- 为什么新：索引里 Live2D 呈现全在「2D 屏幕 / 桌面 / 网页」；**AR（增强现实）叠加是首次出现的呈现形态**，而且是「Live2D + Vuforia（图像识别）」的具体组合。这是一个之前完全没碰过的落地场景（如实体卡片触发看板娘）。
- 可复用性：**不采用** —— AR + Unity + Vuforia 对「16GB Windows 的 Ren'Py 用户」门槛过高，且无 license。列它是为呈现形态补一个维度。
- 证据：`gh api repos/AkagawaTsurunaki/ZerolanPlayground` → `{"stars":32,"license":null,"lang":"C#","pushed":"2025-07-01T07:25:53Z"}`
- 坑：①无 license；②代码停在 2025-07；③Vuforia 有自有商用条款，需单独看。

---

## 五、AI / Agent 驱动桌宠（新角度：表情由「Agent 状态」驱动，非人手动切）

### AAAAGENT ★143 · TypeScript · NOASSERTION（README 写非商用）· 推送 2026-10-10
- 地址：https://github.com/phoiex/AAAAGENT
- 一句话：带语音、情绪记忆、微信接入、能跟 Codex / DeepSeek Harness 联动的 **Live2D 伴侣**（macOS 优先，Windows 开发中）——仓库里直接放了角色设计稿 `whale-layers.psd`。
- 为什么新：索引里的 AI 桌宠多是「LLM 聊天 + Live2D 立绘」；AAAAGENT 把**「与编码 Agent 联动 + 情绪记忆 + IM（微信）」**捆在一起，且**公开了角色的分层 PSD 设计稿**（对想知道「一个能上线的伴侣角色工程长什么样」的人是稀缺素材）。★143 说明这类「Agent 伴侣」已形成需求。
- 可复用性：**参考** —— ①README 明写 **Noncommercial only; attribution required**，商用直接排除；②macOS 优先、Windows 还在做，基准人物（Windows）现在装了也跑不动。但可**下载 `assets/original-design/whale-layers.psd` 当分层规范范本**。
- 证据：`gh api repos/phoiex/AAAAGENT` → `{"stars":143,"license":"NOASSERTION","lang":"TypeScript","pushed":"2026-10-10T18:12:26Z"}`；desc 含 "Noncommercial only; attribution required"、"macOS-first; Windows in development"；文件树含 `assets/original-design/whale-layers.psd`、`assets/previews/v2-flow-workbench-original.jpg`
- 坑：①**非商用**许可；②Windows 支持未完成；③NOASSERTION 的许可需读 LICENSE 全文确认边界。

### Agent 桌宠（CodexPet 2.0） ★20 · Python · NOASSERTION · 推送 2026-10-11
- 地址：https://github.com/shicheng5589-oss/Agent-desktop-pet
- 一句话：贴在 Windows 桌面上的 Live2D 小桌宠——**它跟着 Codex / Claude Code / Gemini 等 12 个 Agent 的实时状态换表情**（思考中/执行中/等你/出错/完成…共 9 个状态），眼睛带惯性跟鼠标，`只读本地会话记录、不联网`。
- 为什么新：这是「**Agent 状态 → 表情映射**」这个具体机制的完整实现（状态源是各 agent 写在本地会话文件里的数据）。索引里同类桌面宠物都是「你手动切表情」或「LLM 对话驱动」，**把「编码 agent 的工作状态」当作表情信号源是头一次**；对维护本地索引站、天天盯 agent 跑任务的人，这几乎是量身定做。
- 可复用性：**落地（条件性）** —— ①Windows 原生、Python、★20、活跃（2.0 于 2026-10-11）；②只读本地不联网，隐私友好；③它允许换自己的 Live2D 模型（README「换成你自己的 Live2D 模型」）。但 NOASSERTION 许可需先读 LICENSE；对基准人物是「明天可试装」级别。
- 证据：`gh api repos/shicheng5589-oss/Agent-desktop-pet` → `{"stars":20,"license":"NOASSERTION","lang":"Python","pushed":"2026-10-11T06:08:24Z"}`；文件树含 `agent_state.py`、`codex_state.py`、`status-bridge.py`、`docs/实现笔记.md`、`pet-launcher.ps1`
- 坑：①NOASSERTION（有 THIRD-PARTY.md，装前务必读）；②需自备 Live2D 模型（仓库不含）；③状态解析依赖各 agent 的本地会话文件格式，agent 更新可能解析失败。

### interactive_assistent ★11 · Rust · NOASSERTION · 推送 2026-08-19（更新 2026-10-09）
- 地址：https://github.com/kiskaserver/interactive_assistent
- 一句话：Windows 桌面动漫助手——一个有反应的动画角色贴在屏幕上（Rust 实现）。
- 为什么新：Rust 写桌面 Live2D 助手的案例在索引里几乎没有；它和 rydanee/live2drust、ayagami 一起说明 **Rust 正在成为 Live2D 宿主/渲染的新语言**。
- 可复用性：**不采用** —— ★11、无清晰文档、NOASSERTION 许可。仅记录语言趋势。
- 证据：`gh api repos/kiskaserver/interactive_assistent` → `{"stars":11,"license":"NOASSERTION","lang":"Rust","pushed":"2026-08-19T22:46:12Z"}`
- 坑：NOASSERTION；文档稀薄。

### live2d-desktop-pet-electron ★0 · TypeScript · MIT · 推送 2026-09-19
- 地址：https://github.com/fyisgod/live2d-desktop-pet-electron
- 一句话：把 **VTube Studio 导出的 Live2D 模型**变成桌面宠物：Electron + Cubism 5 SDK for Web，**自带 VTS 导入器 + 逐像素点击穿透**。
- 为什么新：索引里桌面宠物多用 Electron 但少见两件事——**①「VTube Studio 导入器」**（打通 VTS 生态的现成模型），**②「逐像素点击穿透」**（不规则形状下鼠标能穿过透明区，这是桌面宠物真正能用起来的关键细节）。这两点都是可抄的具体做法。
- 可复用性：**参考** —— ★0、单人、刚建仓；不建议直接用，但「VTS 导入」+「逐像素命中测试」两个实现思路值得学（尤其做网页看板娘的人）。
- 证据：`gh api repos/fyisgod/live2d-desktop-pet-electron` → `{"stars":0,"license":"MIT","lang":"TypeScript","pushed":"2026-09-19T15:48:09Z"}`
- 坑：★0、无使用验证；Electron 打包体积大。

---

## 六、Cubism Editor 自动化（新角度：官方 External API 开放了「编辑」，第三方开始围它建工具）

> 背景：这一簇是本辑新冒出来的。官方 Cubism Editor 有本机 External API（默认端口 **22033**），2026 起第三方开始用它做「插件 / agent / 项目管理」，且 **5.4 alpha 首次放出「编辑 API」样例**（04_EditSample）。索引此前只有零散的 MCP（nana7chi / sayaka-aiart），这次成簇。

### Turboism ★3 · Java · AGPL-3.0-only · 推送 2026-10-08
- 地址：https://github.com/turboism/Turboism
- 一句话：**Windows 优先的 Cubism Editor 运行时增强工具 + 插件框架**——用 Java agent + 公开 SDK 给编辑器加「参数/网格工具、PSD 工具、调色板增强、本地自动化」。
- 为什么新：这是本辑对 **Cubism 5.3.x 版本更新**这条线最直接的第三方证据：它的支持表列出 **5.2.03 / 5.3.02 / 5.3.03 各配「精确版本适配器（Exact-version adapters）」**——说明 5.3.x 的内部接口在变，社区为此逐版本适配。索引里此前没有任何「针对 Cubism Editor 做插件框架」的条目。
- 可复用性：**参考** —— ①**AGPL-3.0-only**（传染性强）；②**它不分发 Cubism Editor、也不绕过其许可**，你必须已有合法授权的编辑器；③Windows 优先 = 基准人物环境对口。若你重度用 Editor，值得关注它能不能把「重复建模动作」自动化。
- 证据：`gh api repos/turboism/Turboism` → `{"stars":3,"license":"AGPL-3.0","lang":"Java","pushed":"2026-10-08T12:17:43Z"}`；README 表格含 `5.2.03 | Exact-version adapters`、`5.3.02 | Exact-version adapters`、`5.3.03 | Exact-version adapters`；声明 "not affiliated with … Live2D Inc."、"does not distribute Cubism Editor or grant, replace or bypass its license"
- 坑：①★3、很新（建仓 2026-07）；②AGPL-3.0-only + 另有 EULA 声明，商用务必通读；③插件改动**会改工程内容**，作者明确「用前自行备份」。

### cubism-editor-computer-use ★0 · Python · MIT · 推送 2026-09-16
- 地址：https://github.com/pakholeung37/cubism-editor-computer-use
- 一句话：**Cubism Editor 外部应用 API 的样例集 + 新增的异步 Python 客户端**——fork 自官方 `Live2D-Garage/CubismExternalAppPluginSamples` 的 `54alpha` 分支，并补了 `cubism_async/`（session/dispatcher/identity 一应俱全）。
- 为什么新：它是「**官方 5.4 alpha 的编辑 API**」目前最完整的一手样例封装：README 直接列出 `04_EditSample`（`Cubism5.4alpha の編集APIのサンプル`）。索引里的 MCP 工具都是「读/控制参数」，**这里是「写（编辑）」的官方样例 + Python 异步封装**，是「从控制走向真实建模自动化」的分水岭物料。
- 可复用性：**参考** —— 要吃 5.4 alpha 且已有正版 Editor 才用得上；但 `cubism_async/` 的会话/身份/错误分层是**可直接照抄的「如何跟本机 GUI 程序握手」范式**，对任何想自动化本机工具的人有借。
- 证据：`gh api repos/pakholeung37/cubism-editor-computer-use` → `{"stars":0,"license":"MIT","lang":"Python","pushed":"2026-09-16T13:31:03Z"}`；文件树含 `cubism_async/client.py`、`session.py`、`dispatcher.py`、`specs.py`、`04_EditSample/ceplugin.py`；README 含 "Cubism5.4alpha の編集APIのサンプル"
- 坑：①上游是 54alpha（**alpha**），接口随时变；②需本机装 Cubism Editor 5.4 alpha 并开 External API；③安全上，HTML 样例每次加载都要在编辑器里手动授权。

### NanaBetterCubism ★0 · Rust · MIT · 推送 2026-09-07
- 地址：https://github.com/sena-nana/NanaBetterCubism
- 一句话：**对话驱动的 Cubism Editor Agent 桌面应用**——通过 `127.0.0.1:22033` 连本机 Editor，用官方 External API 全量工具，结构编辑统一走「preview → 确认 → 后端事务 → 回读验证」。
- 为什么新：它把「**用自然语言让 agent 改 Cubism 工程**」做成了完整产品形态，且最关键的一步设计是**事务化 + 回读校验 + 可取消**——这正好回应了「用 agent 改美术资产怕改坏」的核心顾虑。索引里没有任何条目给出这种「可回滚的模型编辑」范式。
- 可复用性：**参考** —— ★0、需要正版 Editor 5.4；不直接用。但「preview→confirm→transaction→verify」这套对话式编辑的安全模式，是**任何想给美术工具接 AI 的人都该抄的设计**。
- 证据：`gh api repos/sena-nana/NanaBetterCubism` → `{"stars":0,"license":"MIT","lang":"Rust","pushed":"2026-09-07T15:45:26Z"}`；README 含「Cubism Editor 连接（本机 127.0.0.1，默认端口 22033）」「所有结构编辑统一走 preview → 确认 → 后端事务 → 回读验证」「不做权限批准门，也不提供本地文件直接编辑」
- 坑：①★0、依赖 Tauri + Node 26.5/Yarn 4.17，环境偏重；②「不做权限批准门」= 安全边界全靠模型自觉，谨慎；③LiliaCode 特化精简版，通用性未知。

### cubihub ★0 · Rust · MIT · 推送 2026-03-21
- 地址：https://github.com/RainTrap341/cubihub
- 一句话：**Cubism Editor 的离线项目管理器**（Tauri 2 + React）——自动扫描本机装了哪些 Cubism 版本（4/5 系列）、维护项目库、绑定启动版本一键开项目、读写**网格布点预设（Mesh Presets）**、工程备份、**粘贴编辑器日志自动出问题摘要**。
- 为什么新：索引里没有「**管 Cubism 工程本身**」的工具（都在做模型/运行时）。它戳中一个真实痛点：多个 Cubism 版本共存时，项目该用哪个版本开、工程怎么备份、报错日志怎么读。尤其「**读/存 Mesh Preset**」和「**日志→建议**」这两点很实用。
- 可复用性：**参考** —— ★0、Windows 优先、Rust/Tauri；不做重度多版本 Cubism 管理就用不上，但「按版本绑定启动 + 工程备份」的思路值得自建脚本时借鉴。
- 证据：`gh api repos/RainTrap341/cubihub` → `{"stars":0,"license":"MIT","lang":"Rust","pushed":"2026-03-21T12:32:33Z"}`；README 含「自动扫描本机已安装的 Live2D Cubism 版本（支持 4/5 系列）」「读取/保存 Cubism 布点预设（Mesh Presets）」「粘贴并解析 Cubism 编辑器日志，输出问题摘要与处理建议」
- 坑：①★0、单人、3 月建仓后无更新；②备份是「打开备份文件夹，用户手动替换」，非自动还原。

### GFLMotionConverter ★10 · C# · GPL-3.0 · 推送 2022-05-25（仓库更新 2025-05-11）
- 地址：https://github.com/SuomiKP31/GFLMotionConverter
- 一句话：把从 **UABE 导出的《少女前线》Live2D 动作/物理文件**，转换成能用的 `motion3.json` / `physics3.json`。
- 为什么新：索引里 moc3 相关的转换工具多为「读/看」，**「把游戏内自定义动作/物理格式转回标准 motion3/physics3」的转换器此前没有**。它是「模型能读但动作是私有格式」这一具体困境的解法示例，也是**motion/physics 迁移**子方向的唯一命中。
- 可复用性：**不采用** —— 只针对《少女前线》一种游戏格式、代码停更、GPL-3.0，对自研项目无用。列它是为「动作/物理文件格式迁移」补一个实例。
- 证据：`gh api repos/SuomiKP31/GFLMotionConverter` → `{"stars":10,"license":"GPL-3.0","lang":"C#","pushed":"2022-05-25T11:17:01Z"}`
- 坑：①停更；②仅适配单一商业游戏格式；③游戏素材版权风险。

### web-vtuber ★1 · JavaScript · MIT · 推送 2026-03-23
- 地址：https://github.com/gcpd141/web-vtuber
- 一句话：**纯浏览器里的实时面捕 VTuber**——MediaPipe 做人脸关键点，Three.js 驱动 **VRM（3D）** 模型。
- 为什么新：索引里的「面捕」此前是 Live2D 侧（OpenSeeFace/VMC/MediaPipe→Live2D）或 Unity 侧；**「浏览器 + MediaPipe + VRM」这条零安装直播路线**是新的对照物——它说明「用摄像头驱动虚拟形象」在 Web 上已能纯前端跑完，代价是走 3D 而非 Live2D。
- 可复用性：**参考** —— ★1、很轻量，不能直接拿来用；但若想做「摄像头控制看板娘」，它的「浏览器内 MediaPipe 取关键点」这一段可直接借鉴（配合 Live2D 的 ParamAngle/ParamEye 参数映射）。
- 证据：`gh api repos/gcpd141/web-vtuber` → `{"stars":1,"license":"MIT","lang":"JavaScript","pushed":"2026-03-23T13:40:37Z"}`
- 坑：★1、单人、`pushed` 停在 2026-03；VRM 不等于 Live2D，映射逻辑不通用。

---

## 七、其他边缘条目（未单列，登记备查）

- **UFOnian/.physics3.json-Editor**（★1 · 无 license · HTML · 推送 2026-03-01）：一个**在线编辑 `.physics3.json` 摆锤物理参数**的小工具。索引里物理参数调节多靠 Cubism Editor 本体，独立物理编辑器是空档——但★1、无许可、功能单一，暂不单列。地址：https://github.com/UFOnian/.physics3.json-Editor
- **live2d-sdk-ios**（xiaoyvyv，★1 · MIT · C++ · 推送 2025-01-18）：把 Live2D V5 集成进 iOS 的 CocoaPods 库。对 Windows/Ren'Py 基准人物无关，仅登记「iOS 集成」这一平台维度。
- **arm-editor-launcher**（Birch-san，★13 · Java · 无 license · 推送 2023-03-28）：**M1 macOS 下启动 Cubism Editor** 的启动器。只对 Apple Silicon + Editor 用户有意义，与基准人物（Windows）无关，登记不展开。
- **Type010/live2d-web**（★0 · TS · 推送 2026-09-30）：把 moc3 用作网站看板娘 + 面板控制（切背景/装饰/表情）。与已收录的 hacxy/l2d-widget、so0420/doro-live2d-web 高度同质，**不单列**。
- **ZophiaWong/desk-mate-kira / nguyen-van-phuoc/HoloCore**：均为 ★0–★2 的 Live2D 桌宠/助手，与已收录同类重复度高，**不单列**。

---

## 八、子方向覆盖小结

| 子方向 | 本轮命中 | 说明 |
|---|---|---|
| 1. Cubism 5.3.x 更新 / 迁移 | ✅ | Turboism 的 5.2.03/5.3.02/5.3.03 适配表；cubism-editor-computer-use 的 5.4 alpha 编辑 API 样例 |
| 2. AI 驱动（口型/面捕/LLM 桌宠） | ✅ | Agent-desktop-pet（agent 状态→表情）、AAAAGENT、web-vtuber（面捕）；「音频驱动口型」本轮**零命中**（见下） |
| 3. 运行时集成（Unity/UE/Godot/Web/Py） | ✅ | ayagami / ayagami-gd / manosaba-live2d / Godot-Live2D / UnityLive2DExtractor-Unofficial |
| 4. 替代栈（Inochi2D/3D/单图→模型） | ✅ | inox2d / inochi-viewer / inochi2d-toolkit / ayatsuri_2d / illust2psd |
| 5. moc3 解析/逆向/转换 | ✅ | ayagami（读 moc3）、live2drust、UnityLive2DExtractor-Unofficial、GFLMotionConverter、bang-dream-old-moc |
| 6. PSD 分层/自动切图/自动绑定 | ✅ | illust2psd（自动切图+分层 PSD）、cormy-live2d（源文件范本）、whale-maid-svg-layers（矢量重绘分层） |
| 7. 商用授权/许可证清单 | 🔶 部分 | AAAAGENT（非商用）、Turboism/EULA、ayagami（双许可+黑盒逆向法务姿态）各带一段许可信息，但**没有独立的「许可证清单仓库」命中** |

**真空子方向：**
- **音频驱动口型（Audio→LipSync）专项**：本轮 GitHub 搜索**零独立命中**。原因推断：这条路多被并入「LLM 语音助手/桌宠」整体项目里（如 HoloCore、open-llm-vtuber 系），单独成库的少；且已收录的 open-llm-vtuber 已覆盖「语音→口型」主干，新独立库尚未涌现。
- **HuggingFace / Gitee 新制作工具**：**零命中**。HF 上的 Live2D 资源是被塞进 LLM 数据集（如 `NopePrime/Open-LLM-Dataset` 内含 `shizuku.moc3` 及配套 `*3.json`），**没有独立的 Live2D 模型/绑定数据集**；Gitee 侧结果全是多年前的看板娘 widget（xiazeyu/live2d-widget 系）与教程镜像，无新制作工具。原因推断：Live2D 制作工具心智集中在 GitHub + 官方生态，HF/Gitee 不是这条线的活跃地。

---

## 九、本路去重报告（gh 路）

### A. 命中去重基线而剔除的候选（列出 owner/repo + 命中基线）
1. `tsunehimatoi/psd2live` —— 命中 `_dedupe_gh.txt` 与 `index.html`（第三十一辑卡片「PSD 直接出 Cubism 工程」）
2. `hacxy/l2d-widget` —— 命中基线（index [1178]）
3. `lvhaojie456/image-to-live2d`、`flowingduskpro/jpg-to-live2d-workflow` —— 命中 `csdn-social-summary-v30.md` 剔除记录 + index [rpm34c15w]
4. `KurisuMakise004/renderkit` —— 命中 `_dedupe_gh.txt`
5. `mw2wbyys6t-sudo/live2d-auto-pipeline` —— 命中基线（index [1264]）
6. `openl2d/moc3ingbird`、`hana-ame/moc3-json-viewer` —— 命中基线（moc3 查错工具）
7. `nijigenerate/nijigenerate`、`zeikar/iki`、`codewayco/Inkinesis` —— 命中 index（第三十一辑开源替代栈卡片 [1261]/[1262]）
8. `DasterProkio/awesome-ai-companion` —— 命中 index [1275]
9. `umamoorg/umamo` —— 命中 index（第三十三辑「真在读 .cmo3」卡片）
10. `pakholeung37/gd_cubism`、`mizunagikb/gd_cubism` —— 命中 index [1276] / dedupe
11. `erodozer/open-vt` —— 命中 index [1188]
12. `nana7chi/CubismExternalEditMCP`、`sayaka-aiart/cubism-api-bridge` —— 命中 dedupe（MCP/桥接）
13. `canyueY/pyqt-live2d-bridge`、`funlin724/emote-to-cubism`、`fifteen42/live2d-from-art`、`Wzhang3912/image2live2d` —— 均命中 dedupe

### B. 疑似同源但不确定（提请后续复核）
- **`daoming07280/live2d-auto-pipeline` ↔ `mw2wbyys6t-sudo/live2d-auto-pipeline`**：**同名不同 owner**，描述都指向「See-through + psd2live 全自动流水线」。`mw2wbyys6t-sudo` 版已被第三十辑/三十一辑收录；`daoming07280` 版未收录。二者**极可能同一作者的账号迁移/重命名**（`daoming07280` 还挂了 `whale-maid-svg-layers` 这件同流水线的素材）。本次**只单列了 `whale-maid-svg-layers`（因为它承载「矢量重绘分层」这一独立做法）**，`daoming07280/live2d-auto-pipeline` 判为同源**不单列**。
- **`empty-sekai/nnnotes-standalone` ↔ `MetaSekaiLab/nnnotes`**：后者 ★15、MIT、活跃；前者 ★0、描述几乎逐字相同。疑为「standalone 独立版/衍生」。本次**只单列 `MetaSekaiLab/nnnotes`**。
- **`pakholeung37` 单人多仓簇**：`manosaba-live2d`、`ayagami-gd`、`gd_cubism`、`cubism-editor-computer-use` 同属一人，均在 2026-09-16 前后建/推。**同源（同作者）无疑，但各是独立工具，故分别保留了 `manosaba-live2d` 与 `cubism-editor-computer-use`**（`gd_cubism` 已被基线收录，`ayagami-gd` 归于 Ayagami 官方组织条目下说明）。
- **`AkagawaTsurunaki/ZerolanPlayground`**：与作者同名的「Zerolan」系列可能是同一人的多个项目；本次只取 AR 这一个，其余未追踪。

### C. 判断为「有价值但证据不足/过时」而主动放弃的候选
- `hugujiugan/Live2D_Cubism_5.2.03`（★0）：描述直白写着「Live2D破解/patch」——**属于盗版分发，主动排除，不收录**。
- `tcy2002/mediapipe-live2d`（★1，pushed 2023-03）：面捕+Liv2D 方向确有价值，但代码停在 2023、无 license，**时效性不达标，放弃**。

---

> 立条 **27 条**（§一–§六 正文完整条目：12 + 9 + 6 = 27），另 §七 边缘登记 5 条（未计入）。数量略超 25 上限，原因：本轮新爆出「Cubism Editor 官方 External API（22033 端口）被第三方围建工具」这一整簇（Turboism / cubism-editor-computer-use / NanaBetterCubism / cubihub），是**真空补位**且确有 4 个独立项目，故保留成簇。
>
> 全部 ★ / 许可证 / 语言 / 推送日均由 `gh api repos/<owner>/<repo>` 实取，命令见各条「证据」字段。**本机 `git clone`/`curl` 均被代理挡死**（`curl` 实测 `CONNECT tunnel failed, response 502`），故 HuggingFace / Gitee 两处**仅能靠 WebSearch 网页级核实**，已在 §八 标注为「零命中」。

