# 第三十五辑 · gh 路调研产出（Live2D 制作相关新增/重大更新）

> 检索窗口：`pushed:>2026-09-01`（实际检索日 2026-10-11）
> 去重基线：`_r35/_dedupe_gh.txt`（1317 条已收 owner/repo）+ `csdn-social-summary.md` / `-v34.md` / `-v33.md`
> 可复用性基准：16GB 内存 Windows、跑本地 Ollama、维护静态索引站的个人开发者（非企业、无 GPU 集群）
> 所有 ★ / 许可证 / 语言 / 日期均走 `gh api repos/<r>` 实取；关键条目已用 `gh api .../git/trees` 复核文件树

---

## 一、格式解析 / 渲染（绕开或半绕开 Cubism 官方 SDK）

### 1. `HELPMEEADICE/Neocari`（★0 · **GPL-3.0** · Rust）
纯 Rust 的 **Cubism V2 模型加载 + 渲染**实现（自称 Mocari 的 Rust 派生）。仓库自带完整 Haru 模型资产（`.moc3` / `.model3.json` / `.physics3.json` / `.pose3.json` / `.exp3.json` / `.motion3.json` 六件套齐全），并配 CI。
- 价值：**它把「一份 Cubism V2 模型到底由哪些文件组成」摆成了可编译的样本**，`assets/models/Haru` 是读格式的现成对照物。
- URL：https://github.com/HELPMEEADICE/Neocari ｜ `pushed_at` 2026-09-27 ｜ `updated_at` 2026-09-27
- **⚠️ 参考**：刚起（0 star、单次推送），GPL-3.0 传染；但作为「Cubism V2 文件结构教材」值得拉下来读 tree。

### 2. `rydanee/live2drust`（★0 · 无许可证 · Rust）
用一个 `.moc3` 查看器最小验证 **Rust + wgpu 渲染 Live2D** 的路径。源码含 `physics.rs` / `expressions.rs` / `animations.rs` / `live2d.wgsl`。
- ⚠️ **关键事实**：它链的是官方核心库 `src/libs/libLive2DCubismCore.a` + `Live2DCubismCore.h`，**不是格式重写**（别把它误当「绕开官方」）。
- URL：https://github.com/rydanee/live2drust ｜ `pushed_at` 2026-09-23 ｜ `updated_at` 2026-09-23
- **❌ 不采用**（当依赖）：**无 LICENSE**、无 README、单文件级实验；仅作「wgpu 接官方 core 的接线参考」。

### 3. `sdegfd/embedded-live2d`（★0 · **MIT** · C）
**嵌入式 Live2D 引擎 + 编辑器**（PainterEngine 系）：自建 `l2d.h / l2d_model.h / l2d_instance.h` 等抽象，且已带 **ESP-IDF / ESP32-P4 移植** 与 host benchmark。
- 价值：这是本辑**最不寻常的一条** —— 把 Live2D 往 MCU 上搬，MIT 许可、有 CI。对「想在奇怪设备上跑 Live2D」的人是唯一现成起点。
- URL：https://github.com/sdegfd/embedded-live2d ｜ `pushed_at` 2026-10-02 ｜ `updated_at` 2026-10-03
- **⚠️ 参考**：PC 上用不上，但 MIT + 结构清晰，可读其内存/光栅化设计。

### 4. `hoardodile/plugin-2d-skel`（★1 · **MIT** · TypeScript）
**Live2DViewerEX 数据格式支持**，并统一了 Live2D / Spine / DragonBones 三类 2D 骨骼动画查看器。
- 价值：Live2DViewerEX 的私有打包格式在开源侧几乎没有解析实现，这是一个稀缺案例。
- URL：https://github.com/hoardodile/plugin-2d-skel ｜ `pushed_at` 2026-09-20 ｜ `updated_at` 2026-09-29
- **⚠️ 参考**：star 低，但格式覆盖面独特。

### 5. `Hana-ame/moc3-json-viewer`（★0 · 无许可证 · HTML）
**纯 Canvas2D、零依赖**的 moc3 JSON 查看器，上传即看、不存模型数据。
- 价值：单文件、零依赖，适合塞进静态站做「模型结构预览」。
- URL：https://github.com/Hana-ame/moc3-json-viewer ｜ `pushed_at` 2026-09-25 ｜ `updated_at` 2026-09-25
- **⚠️ 参考**：**无 LICENSE**（自用可，商用先问）；体量极小。

### 6. `Hana-ame/live2d-viewer`（★0 · 无许可证 · TypeScript）
浏览器内渲染 Cubism 模型，**不打包任何模型数据（用户上传式）**。
- 价值：与上条同作者，一是「看结构」一是「看渲染」，凑成一对自托管查看器。
- URL：https://github.com/Hana-ame/live2d-viewer ｜ `pushed_at` 2026-09-19 ｜ `updated_at` 2026-09-19
- **⚠️ 参考**：无 LICENSE；同一作者的轻量对照件。

### 7. `davidleonstr/live2dqt`（★1 · **MIT** · Python）
把 Live2D 模型做成**透明、置顶的桌面浮层**，或**嵌进 Qt 窗口**。
- 价值：PyQt/PySide 桌宠人最关心的「窗口穿透 + 置顶」在这里有现成写法；MIT。
- URL：https://github.com/davidleonstr/live2dqt ｜ `pushed_at` 2026-09-29 ｜ `updated_at` 2026-09-29
- **⚠️ 参考**：Python 栈、与本地 Ollama 路线同源，可直接抄窗口策略。

### 8. `rayriffy/CubismMetal`（★0 · 无许可证 · Swift）
**专门为 Metal API 调优**的高性能 Live2D 查看器（macOS/iOS）。
- URL：https://github.com/rayriffy/CubismMetal ｜ `pushed_at` 2026-09-16 ｜ `updated_at` 2026-09-16
- **❌ 不采用**：Apple 专属、无 LICENSE；Windows 个人开发者用不到，仅登记。

### 9. `4163/pixijs-live2d-spine-viewer`（★2 · **MIT** · JavaScript）
独立网页渲染器，用 PixiJS 经 WebGL 同时显示 **Live2D（Cubism 2/3）与 Spine 2.x**。
- 价值：**「一个 viewer 吃两种 2D 骨骼格式」的双格式抽象**值得学（和桌宠多形态诉求同构）。
- URL：https://github.com/4163/pixijs-live2d-spine-viewer ｜ `pushed_at` 2026-09-30 ｜ `updated_at` 2026-09-30
- **⚠️ 参考**：MIT；注意其「含 Girls' Frontline 参考模型」——资产不要随站分发。

### 10. `RealNath/wuwa-live2d-viewer`（★5 · 无许可证 · HTML）
一份**把鸣潮（wuwa）的 Spine/Live2D 动画导出成图片/视频**的实操指南。
- URL：https://github.com/RealNath/wuwa-live2d-viewer ｜ `pushed_at` 2026-09-11 ｜ `updated_at` 2026-09-19
- **❌ 不采用**：本质是「抽游戏资产」教程，**版权灰区**，仅登记不进索引。

---

## 二、自动绑定流水线（PSD → rig → 动画）

### 11. ⭐ `shinshin86/still2rig-psd`（★130 · **MIT** · JavaScript）—— 本辑绑定侧最高星
**一张静态动漫角色图 → 一张「经过 QA 的结构化 PSD」**：走 Codex + 用户授权的 Google Colab GPU 会话，并**内置动作预览（motion preview）**。
- 关键分岔：多数「拆层」项目只给 PSD 就结束，**它多做了一步「QA 自检 + 动起来预演」** —— 拆得对不对，靠预览说话。
- URL：https://github.com/shinshin86/still2rig-psd ｜ `pushed_at` 2026-09-29 ｜ `updated_at` 2026-10-09
- **✅ 落地**：MIT、130 star、作者另有 `mesh-avatar-studio`（★599，已收）；唯一门槛是 Colab GPU 那步（本地 16GB 可降级跑）。

### 12. ⭐ `sayaka-aiart/StandRig`（★82 · **Apache-2.0** · TypeScript）—— 本辑绑定侧最「另类」
**「AI 可编辑的 2D 建模与回放」**：吃「已分好层的 PSD」，提供**独立本地服务 + 可嵌入 runtime**，并通过 **MCP** 让 AI 直接改模型。
- 价值：把「绑定」这件事从 GUI 拖拽变成 **MCP 工具调用**，正对上「让 agent 参与制作」的主线。
- URL：https://github.com/sayaka-aiart/StandRig ｜ `pushed_at` 2026-09-13 ｜ `updated_at` 2026-10-07
- **✅ 落地**：Apache-2.0、82 star、TypeScript 本地服务形态，个人机可跑。

### 13. `naiyouj/live2d-ai-generator`（★0 · 无许可证 · Python）
**AI 图 → 可动 Live2D 模型的全本地 5 段流水线**（生成 / 拆层 / 绑定 / 预览）+ 动画编辑器。
- 关键实现：它以 `patches/` 形式**覆盖在 `image2live2d`（★43，已收）与 See-through 之上**，并带 `pytest`（含 `test_neck_zorder.py`）。
- URL：https://github.com/naiyouj/live2d-ai-generator ｜ `pushed_at` 2026-09-20 ｜ `updated_at` 2026-09-20
- **⚠️ 参考**：**无 LICENSE**、依赖上游 `image2live2d`；但「patch + test」的组织方式比一堆脚本干净。

### 14. `bluewakame/live2d-psd-generator`（★1 · **MIT** · Python）
**从一张正面立绘生成 Live2D 用的「分好层的 PSD」，被遮挡的部分用 AI 补全**。
- 价值：日语项目，正对「藏层补全」这个绑定前最费手的痛点；MIT。
- URL：https://github.com/bluewakame/live2d-psd-generator ｜ `pushed_at` 2026-09-15 ｜ `updated_at` 2026-09-21
- **⚠️ 参考**：star 低，实现单一，但补全思路可抄。

### 15. `lvhaojie456/image-to-live2d`（★2 · **MIT** · Python）
**一张立绘或一句提示 → 一版首轮 Live2D 模型（moc3 + Cubism 工程）**：AI 规划 → See-through 拆层 → 度量表情 → psd2live 绑定 → **Cubism Core 校验**。
- 关键分岔：**它把「用官方 Core 校验产物」写进了流水线**（同辑中「可验证断言」主题的延续）。
- URL：https://github.com/lvhaojie456/image-to-live2d ｜ `pushed_at` 2026-09-22 ｜ `updated_at` 2026-09-29
- **⚠️ 参考**：MIT，但体量小、依赖 psd2live（已收）；作流程模板看。

### 16. `flowingduskpro/jpg-to-live2d-workflow`（★4 · **MIT** · Python）
**单张 JPG → 可驱动 Live2D → VTube Studio** 的完整链路：See-Through 拆层 → 分层 PSD → psd2live 自动绑定 → moc3。**附 8GB 显存上的实测性能与精度结论**。
- 价值：**给了「消费级显卡能不能跑」的一手数字** —— 对 16GB/无独显集群的个人开发者最实用。
- URL：https://github.com/flowingduskpro/jpg-to-live2d-workflow ｜ `pushed_at` 2026-09-14 ｜ `updated_at` 2026-10-07
- **✅ 落地**：MIT，文档即产品，直接照抄参数。

### 17. `Sheeber-2024/live2d-pipeline`（★1 · 无许可证 · Python）
**单张插画 → 可用 Live2D 模型**：串起 See-through 拆层与 psd2live 自动绑定，打包成 **Web 服务 + 浏览器预览 + 跨平台部署（macOS/Windows/Linux）+ 本地 GPU 方案**。
- URL：https://github.com/Sheeber-2024/live2d-pipeline ｜ `pushed_at` 2026-09-28 ｜ `updated_at` 2026-10-08
- **⚠️ 参考**：Web 化封装完整，但**无 LICENSE**；与 13/15/16 同源思路，选其一读即可。

### 18. `lilyco-42/happy-sugar-life-live2d`（★0 · 无许可证 · Python）
**AI 拆层 + Stretchy Studio 绑定/动画**，并公开**完整流水线文档、脚本、以及「踩坑日志 v9」**。
- 价值：**踩坑日志本身**比脚本值钱 —— 记录到 v9，说明作者真跑过很多轮。
- URL：https://github.com/lilyco-42/happy-sugar-life-live2d ｜ `pushed_at` 2026-10-10 ｜ `updated_at` 2026-10-10
- **⚠️ 参考**：无 LICENSE；当「经验帖」读，不当代码依赖。

### 19. `0ran/puppet-part-splitter`（★4 · 无许可证 · JavaScript）
**纯客户端**的素材分割器：Live2D / Spine / **Wallpaper Engine** 三类，把插画/PSD 拆成部件层并**自动打包成透明精灵图**；全本地、不上传。
- URL：https://github.com/0ran/puppet-part-splitter ｜ `pushed_at` 2026-09-06 ｜ `updated_at` 2026-09-30
- **⚠️ 参考**：前端即可用，无 LICENSE；「本地不上传」正合隐私偏好。

### 20. `satoxpochi/PSLayerLRSplitter`（★1 · **MIT** · JavaScript）
**Photoshop 脚本**：把带 LR（左右）后缀的图层夹**拆成独立的左/右部件** —— Live2D 分部件工序里的高频机械动作。
- URL：https://github.com/satoxpochi/PSLayerLRSplitter ｜ `pushed_at` 2026-09-13 ｜ `updated_at` 2026-09-13
- **⚠️ 参考**：MIT、极小，但解决的是真痛点（省手工）。

### 21. `Zosuya/ParaRig`（★0 · **GPL-3.0** · Python）
**Blender 插件**：自动生成可拖拽的滑杆 rig + Drivers，把滑杆映射到 Shape Key / 自定义属性 / 骨骼位置 —— 即**用 Blender 原生能力仿 Live2D Cubism 的参数面板**。
- 价值：对齐「绕开 Cubism 官方」主线 —— 在 Blender 里复刻参数-驱动范式。
- URL：https://github.com/Zosuya/ParaRig ｜ `pushed_at` 2026-09-16 ｜ `updated_at` 2026-09-16
- **⚠️ 参考**：GPL-3.0 传染；GIF/文档齐全，可读设计。

### 22. `xez65/bang-dream-old-moc-game-import-workflow`（★0 · 无许可证 · 文档）
**BanG Dream 老式 MOC 模型 → MOC3 + Unity 引擎**的「可复核工作流」文档。
- 价值：老 MOC→MOC3 的迁移路径在开源侧稀缺。
- URL：https://github.com/xez65/bang-dream-old-moc-game-import-workflow ｜ `pushed_at` 2026-10-07 ｜ `updated_at` 2026-10-07
- **⚠️ 参考**：纯文档、无 LICENSE；游戏资产相关，作方法参考。

### 23. `henceketh/inochi2d-autorig-claude`（★0 · 无许可证 · Python）
用 Claude 自动绑定 **Inochi2D**（非 Cubism），并在 README 里**明确断言「Cubism 根本无法自动绑定」**，给出替代路径：生成「绑定配方（图层改名 / 参数表 / deformer 计划 / keyform 清单）」交人执行。
- 价值：**「把硬限制写成文档」** 是本辑可验证断言的典型；作者把「能自动化到哪一步」划得很清。
- URL：https://github.com/henceketh/inochi2d-autorig-claude ｜ `pushed_at` 2026-10-05 ｜ `updated_at` 2026-10-05
- **⚠️ 参考**：无 LICENSE；主要价值是那条被明说的边界结论。

---

## 三、AI 资产生成 / 拆层（ComfyUI 生态）

### 24. `Bellpepperknuthamsun280/ComfyUI-See-through`（★0 · 无许可证 · 节点）
**ComfyUI 节点**：把动漫插画转成**带深度顺序的分层 2.5D PSD**，供 Live2D 工作流使用（See-through 的 ComfyUI 化）。
- ⚠️ 注意：基线里**已有同名 `ComfyUI-See-through`**（此前收录），本条是**后起的同功能副本**，详见去重报告。
- URL：https://github.com/Bellpepperknuthamsun280/ComfyUI-See-through ｜ `pushed_at` 2026-10-11 ｜ `updated_at` 2026-10-11
- **⚠️ 参考**：功能方向对，但按去重规则**不进索引**（同功能已收）。

---

## 四、引擎集成（Godot / 桌面 / 壁纸）

### 25. `KCN2/simple-live-2d`（★0 · 无许可证 · GDScript）
**Godot 4 的 CharacterMorph2D：无网格（meshless）的实时 2D 角色形变**工具。
- 价值：Godot 上「透明窗 + 轻量形变」的另一条路，与已收的 `gd_cubism`（batched + mask atlas）互补。
- URL：https://github.com/KCN2/simple-live-2d ｜ `pushed_at` 2026-10-10 ｜ `updated_at` 2026-10-10
- **⚠️ 参考**：无 LICENSE、极新；概念先行。

### 26. `mimi0123/live2d_game`（★0 · **GPL-3.0** · GDScript）
**Godot 4.7 的 Live2D 互动 demo**：SoftTouch 软体触摸 + 节奏模块。
- URL：https://github.com/mimi0123/live2d_game ｜ `pushed_at` 2026-09-13 ｜ `updated_at` 2026-09-13
- **⚠️ 参考**：GPL-3.0；「触感交互」的点子可借鉴。

### 27. `loliRuriruri/HoloDori`（★0 · 无许可证 · Rust）
**HoloDori Live2D Manager**：导入 / 构建 / 预览 Live2D 模型（含动作、表情、物理），并可把模型**作为桌宠或 Windows 壁纸**运行。
- 价值：**「制作工具 + 运行时 + 壁纸」三合一**的少见组合；Rust 栈。
- URL：https://github.com/loliRuriruri/HoloDori ｜ `pushed_at` 2026-10-01 ｜ `updated_at` 2026-10-01
- **⚠️ 参考**：无 LICENSE、单次推送；当产品形态参考。

---

## 五、桌宠 / 数字人「身体」侧（agent 状态联动）

### 28. `zeikar/charivo`（★23 · **MIT** · TypeScript）
**模块化 TypeScript 框架**：把「Live2D 角色 × LLM / TTS / STT / 实时语音」组装成互动数字人。
- 价值：与已收的 `zeikar/iki`（同作者的开放 2D 木偶引擎）**同源生态**；MIT、23 star，是「身体侧」里工程化程度较高的一条。
- URL：https://github.com/zeikar/charivo ｜ `pushed_at` 2026-10-06 ｜ `updated_at` 2026-10-09
- **✅ 落地**：MIT、TS、模块化，与静态站/本地服务都好接。

### 29. `FanyinLiu/Nexus`（★20 · **MIT** · TypeScript）
**本地优先桌面 AI 伙伴**：Live2D 或 Portrait Puppet 角色常驻桌面，文字/语音对话 + 长期记忆。Electron + React + TS，**当前稳定版 v0.4.7**。
- URL：https://github.com/FanyinLiu/Nexus ｜ `pushed_at` 2026-10-03 ｜ `updated_at` 2026-10-10
- **✅ 落地**：MIT、有版本号说明在真迭代；「Live2D *或* Portrait Puppet」双渲染分支值得看。

### 30. `JeffreyChen-s-Utils/Imervue`（★5 · **MIT** · Python）
**GPU 加速图像工作站**（PySide6 + OpenGL）：浏览整理图库、非破坏性调整、绘制、**绑定 2D 木偶**，并以**无边框桌面浮层**运行；带插件系统 + **MCP server**。
- 价值：本辑**唯一「绑定 + 桌面运行时 + MCP」三合一**的 MIT 工具，把制作端和身体端缝在一起。
- URL：https://github.com/JeffreyChen-s-Utils/Imervue ｜ `pushed_at` 2026-10-10 ｜ `updated_at` 2026-10-08
- **✅ 落地**：MIT、Python + OpenGL，本机可跑；`updated_at` 早于 `pushed_at` 提示元数据未顺手更新（不碍事）。

### 31. `sslbs09/suzuran-pet`（★17 · 许可证 NOASSERTION · JavaScript）
Q 版狐狸医师桌面宠物：深浅双主题、任意 OpenAI 兼容 API、**本地语音克隆（中/日）**、**Spine / Live2D / GIF 多形态**。
- 价值：**「多形态同一角色」** 的落地范例（Spine+L2D+GIF 三种呈现共存）。
- URL：https://github.com/sslbs09/suzuran-pet ｜ `pushed_at` 2026-10-11 ｜ `updated_at` 2026-10-09
- **⚠️ 参考**：许可证为 NOASSERTION（非标准），商用先问；功能面很全。

### 32. `CocoRoF/Geny`（★11 · **Apache-2.0** · Python）
**自托管 AI agent，「有脸、有声音、有记忆」**：web / 桌面（头像浮层）/ 手机三端，跑在**一条 21 阶段流水线**上。
- 价值：把「数字人 = 长流水线」讲得最系统的项目之一；Apache-2.0。
- URL：https://github.com/CocoRoF/Geny ｜ `pushed_at` 2026-10-01 ｜ `updated_at` 2026-10-01
- **⚠️ 参考**：21 阶段意味着依赖偏重，16GB 机要挑段跑；架构值得抄。

### 33. `mefist-asuka/Deepseek-standard-mode`（★4 · 无许可证）
**基于 BongoCat 的「Deepseek 蓝色大肥鱼」Live2D 标准模式模型开源工程，含全套源文件与贴图**。
- 价值：Live2D **制作源文件（图层/贴图）**在开源侧极罕见 —— 这是「可直接拆开学的成品 rig」。
- URL：https://github.com/mefist-asuka/Deepseek-standard-mode ｜ `pushed_at` 2026-09-28 ｜ `updated_at` 2026-10-09
- **⚠️ 参考**：**无 LICENSE**（源文件版权谨慎）；但作为「看得见图层结构的样本」很值。

### 34. `VeiQiuLab/DesktopPet`（★0 · **MIT** · Rust）
**轻量 Windows Live2D 桌宠**：直接走 **Rust + Win32 + D3D11 + DirectComposition** 原生渲染 —— 不背 Electron/Tauri 的壳。
- 价值：对想「桌宠只占几十 MB 内存」的人，这是最省资源的窗口方案示范。
- URL：https://github.com/VeiQiuLab/DesktopPet ｜ `pushed_at` 2026-09-19 ｜ `updated_at` 2026-09-19
- **⚠️ 参考**：MIT，但极新、star 0；当「原生合成窗口」技术样本。

### 35. `zrmCode/DSchatpet`（★0 · **GPL-3.0** · Python）
把 **DS 鲸鱼娘 Live2D 模型做成桌面宠物**：透明置顶、可对话（**任意 OpenAI 兼容接口**，含 ollama）、自选表情、本地养成记忆。Windows / PySide6。
- URL：https://github.com/zrmCode/DSchatpet ｜ `pushed_at` 2026-10-02 ｜ `updated_at` 2026-10-02
- **⚠️ 参考**：**与本地 Ollama 完全同源**、GPL-3.0；窗口与显隐逻辑可直接抄。

### 36. `chengyuZou/EmaAgent`（★3 · **MIT** · TypeScript）
**桌面优先的 AI 伙伴 agent**：Tauri + React + Fastify，带 **Live2D 舞台**、本地 SQLite 记忆、独立 **Narrative RAG**。
- URL：https://github.com/chengyuZou/EmaAgent ｜ `pushed_at` 2026-10-11 ｜ `updated_at` 2026-10-11
- **⚠️ 参考**：MIT、当日仍在推；「叙事型 RAG」是差异化点。

### 37. `ReSerendipity/SpiritPal`（★0 · **Apache-2.0** · TypeScript）
**桌边友**：Tauri v2 + React 19 + **Pixi.js 8 Live2D**，情感陪伴 + 轻交互 + 本地记忆召回。
- URL：https://github.com/ReSerendipity/SpiritPal ｜ `pushed_at` 2026-10-11 ｜ `updated_at` 2026-10-11
- **⚠️ 参考**：Apache-2.0、技术栈新（Pixi 8 + Tauri 2）；刚起。

### 38. `xuwancheng62-lab/CodexPetLive2D`（★0 · **MIT** · TypeScript）
**macOS 上的 Codex Live2D 桌宠原型**：把「编码 agent 状态」映射到角色。
- URL：https://github.com/xuwancheng62-lab/CodexPetLive2D ｜ `pushed_at` 2026-09-26 ｜ `updated_at` 2026-09-26
- **⚠️ 参考**：MIT、macOS 侧样本（Windows 用不上，但状态映射接口可参考）。

### 39. `xShiroeNguyenx/desktop-companion`（★1 · 非标准许可证 · JavaScript）
**独立 Windows Live2D 桌宠**，内置 **AI 翻译 / 快捷回复 / 任务保存**，可覆盖任意应用（Teams、浏览器、Word…）工作。
- 价值：**「桌宠当系统级小助手」** 而非纯挂件；跨应用覆盖是它的差异点。
- URL：https://github.com/xShiroeNguyenx/desktop-companion ｜ `pushed_at` 2026-09-15 ｜ `updated_at` 2026-09-15
- **⚠️ 参考**：许可证 NOASSERTION；功能点独特。

### 40. `nanhudev/AgentPet`（★1 · 无许可证 · Python）
**只读的桌面伙伴**：观察你的本地编码 agent（**WorkBuddy 优先**），把真实工作可视化成一只 2D 宠物 + 停靠工作台。
- 价值：**「read-only、不联网」** 是它的隐私卖点，与本机环境高度相关。
- URL：https://github.com/nanhudev/AgentPet ｜ `pushed_at` 2026-09-16 ｜ `updated_at` 2026-10-02
- **⚠️ 参考**：无 LICENSE；WorkBuddy 联动这条线值得记一笔。

### 41. `12sncaksh/AIssistant`（★2 · **MIT** · Python）
**Windows 桌面 AI 助手兼 Live2D 桌宠**：PyQt6 + 结构化工具调用的 LLM 聊天 + **MCP 支持** + 语音唤醒/输入/输出 + 系统工具。
- URL：https://github.com/12sncaksh/AIssistant ｜ `pushed_at` 2026-10-08 ｜ `updated_at` 2026-10-09
- **⚠️ 参考**：MIT、Python；与 35/40 同属「PySide/PyQt 桌宠 + agent」。

### 42. `haixu8396-png/aileen-desktop`（★5 · 非标准许可证 · JavaScript）
**AILEEN**：Windows 桌面 AI 助手/agent，Live2D 角色 + 多 provider LLM + 长期记忆 + 本地知识库 + 工具调用 + 电脑控制。**声明受 Neuro-sama 启发、致敬 moeru-ai/Airi**，多语言（英/日/简中）。
- URL：https://github.com/haixu8396-png/aileen-desktop ｜ `pushed_at` 2026-10-06 ｜ `updated_at` 2026-10-06
- **⚠️ 参考**：许可证 NOASSERTION；「多 provider + 电脑控制」组合较重，16GB 机需裁剪。

### 43. `Nya-Nya-Hoshino/minto-desktop-assistant`（★5 · **Apache-2.0** · Python）
**日语向的 Live2D 桌面 AI 助手**（日本語で話す）。
- URL：https://github.com/Nya-Nya-Hoshino/minto-desktop-assistant ｜ `pushed_at` 2026-10-10 ｜ `updated_at` 2026-10-10
- **⚠️ 参考**：Apache-2.0；日语场景，中文用户参考价值中等。

### 44. `Rivulet138/yuizaki`（★2 · **MIT** · Python）
本地 Windows/Linux AI 桌宠 Agent：对话、语音、视觉、记忆，**Live2D / VRM 双形态**。
- URL：https://github.com/Rivulet138/yuizaki ｜ `pushed_at` 2026-10-07 ｜ `updated_at` 2026-10-07
- **⚠️ 参考**：MIT；L2D/VRM 双形态与 31 同型。

### 45. `zovoeh830/jingjing-pet`（★2 · 无许可证）
**Android Live2D 桌宠**：WebView + `pixi-live2d-display`，**无 Gradle 构建**，并做 agent 状态联动。
- 价值：**「Android + 无 Gradle」** 是很稀的组合，且复用现成 web Live2D 播放器。
- URL：https://github.com/zovoeh830/jingjing-pet ｜ `pushed_at` 2026-09-27 ｜ `updated_at` 2026-10-06
- **⚠️ 参考**：无 LICENSE；移动端样本。

### 46. `ycwycw2020/GPT_Dragon_girl_transformation`（★4 · 无许可证 · JavaScript）
中文版「live2d codex GPT6 龙娘形象工作站助手」。
- URL：https://github.com/ycwycw2020/GPT_Dragon_girl_transformation ｜ `pushed_at` 2026-10-08 ｜ `updated_at` 2026-10-10
- **⚠️ 参考**：无 LICENSE、描述模糊；仅登记。

### 47. `meokisama/moe2d`（★3 · 非标准许可证 · TypeScript）
**可嵌入网页的 Live2D 角色**（「住在你的网页上」）。
- URL：https://github.com/meokisama/moe2d ｜ `pushed_at` 2026-10-03 ｜ `updated_at` 2026-10-07
- **⚠️ 参考**：许可证 NOASSERTION；适合静态站挂看板娘这条线。

### 48. `empty-sekai/ournotes-player`（★3 · **AGPL-3.0** · JavaScript）
**BanG Dream! Our Notes 的浏览器播放器**：谱面、剧情、**Live2D 模型**（WebGL2 web components）。
- URL：https://github.com/empty-sekai/ournotes-player ｜ `pushed_at` 2026-10-10 ｜ `updated_at` 2026-10-10
- **⚠️ 参考**：**AGPL-3.0 强传染**；且涉游戏资产，只读技术实现。

### 49. `zhuangnan829-lang/interactive-live2d-digital-human`（★0 · 无许可证 · TypeScript）
**Docker 部署的交互式 Live2D 数字人**：中文 TTS + 音频驱动口型 + 表情，并附**验收证据**。
- 价值：「带验收证据」这一条少见（本辑可验证断言主题的又一例）。
- URL：https://github.com/zhuangnan829-lang/interactive-live2d-digital-human ｜ `pushed_at` 2026-10-09 ｜ `updated_at` 2026-10-09
- **⚠️ 参考**：无 LICENSE、极新；Docker 一键起，试错成本低。

---

## 六、边缘登记（相关但价值/窗口不足，不进索引）

| 仓库 | ★ | 许可 | 语言 | pushed | 一句话 & 为何仅登记 |
|---|---|---|---|---|---|
| `sqqtc/bdon-live2d-zh` | 1 | AGPL-3.0 | JS | 2026-10-08 | 汉化 yatta.moe Live2D 工具页的油猴脚本；**纯翻译**，非制作工具 |
| `MrKLLM/azurlane-assetbundle-toolkit` | 4 | 无 | Python | 2026-10-07 | 碧蓝航线 AssetBundle 解包 + Live2D 还原；**游戏资产灰区** |
| `FireTable/project-xiaochun` | 4 | MIT | TS | 2026-10-11 | 纯浏览器 VTuber（WebLLM Qwen3 + EMAGE + Edge-TTS），但走 **VRM 非 Live2D** |
| `JiGuang283/VRMify` | 10 | GPL-3.0 | Python | 2026-10-11 | MMD/PMX → VRM 转换器（无 Blender/Unity）；**VRM 侧**，与 Live2D 仅相邻 |
| `3Asterism/dsh-whale-girl-live2d-custom` | 4 | — | — | 2026-09-30 | `Andersen216/dsh-whale-girl-live2d` 的**二次开发版**，本体已在前辑 |
| `zhuangnan829-lang/...`（见 §五.49） | 0 | 无 | TS | 2026-10-09 | 保留在正文（Docker 数字人 + 验收证据） |
| `Rayriffy/CubismMetal`、`rydanee/live2drust` | 0 | 无 | Swift/Rust | 09 月 | 已在正文，标注为「不采用/参考」 |
| 其余 DSH 插件系（`john-walks-slow/dsh-live2d-voice`、`xieluyang912/dsh-live2d-widget`、`B612plant/dsh-plugin-live2d-stage`、`deanzhang2026-max/dsh-lived-pet`、`nanshan118/KAFKA-Agent` 等） | 0–1 | 杂 | 杂 | 09–10 月 | **DSH 插件生态同质化严重**，建议**下轮成辑**统一处理，本辑不逐个收录 |

---

## 七、本路去重报告

### 7.1 直接命中基线（`_r35/_dedupe_gh.txt`，36 条，整条剔除）
第一批 58 个候选中命中 36 个，**命中率 62%** —— 说明前几辑已把 Live2D 主流项目基本收干：
`tsunehimatoi/psd2live`、`umamoorg/umamo`、`Hera-Berg/open-avatar-creator`、`shinshin86/mesh-avatar-studio`、`codewayco/Inkinesis`、`zeikar/iki`、`RevStudio/Rev2D`、`Kota-Ohno/seethrough-live2d-pipeline`、`Wzhang3912/image2live2d`、`Ariakage/live2d-agent-kit`、`fifteen42/live2d-from-art`、`mw2wbyys6t-sudo/live2d-auto-pipeline`、`yanjingzhaisun/inochi2d-toolkit`、`aethiopicuschan/cubism-go`、`Yoru-KenomoVT/ayatsuri_2d`、`Inochi2D/inox2d`、`nijigenerate/nijigenerate`、`Inochi2D/inochi2d`、`Inochi2D/inochi-viewer`、`madosuki/live2dManager`、`Untitled-Story/untitled-pixi-live2d-engine`、`omniwaifu/pixi-live2d5`、`Panzer-Jack/easy-live2d`、`EasyLive2D/live2d-py`、`marukun712/kokoro`、`Jelosus2/BD2-L2D-Viewer`、`pakholeung37/gd_cubism`、`pakholeung37/manosaba-live2d`、`NekoUnix/A.R.I.A`、`nanlingyin/soullink-emotion-sdk`、`turboism/Turboism`、`sena-nana/NanaBetterCubism`、`KurisuMakise004/renderkit`、`funlin724/emote-to-cubism`、`DasterProkio/awesome-ai-companion`。

### 7.2 后批次新增命中
- `J621111/live2d-automation`（★77，Live2D Automation MCP Server）→ **已在基线**，弃；
- `lk2168/vtuber-pipeline`（★2，插画→VTS，See-through/psd2live 对接层）→ **已在基线**，弃；
- `daoming07280/live2d-auto-pipeline` → 命中 `v33` 经验帖 + 基线，弃；
- 桌宠线大批命中：`cqzaaa/AgentPet`(★262)、`kiyotakali/Miru`(★175)、`momori777/Artemis`(★382)、`meet447/Meuxe`(★78)、`Andersen216/dsh-whale-girl-live2d`(★28)、`shicheng5589-oss/Agent-desktop-pet`(★20)、`Lsc-91-69/dsh-live2d-avatar`（v34 §三.4 已收）等，**一律剔除**。

### 7.3 重复形态识别（六类）
- **同名不同 owner（镜像/SEO 站）**：
  - `Rickettsiayorkshirefog4963/still2rig-psd` 是 `shinshin86/still2rig-psd` 的**同描述复制仓**（描述逐字一致）→ **不收复制件，只收本体**；
  - `untrained-devilray248/ComfyUI-See-through` 与基线中**已有的 `ComfyUI-See-through`** 同功能 → 弃；
  - `Bellpepperknuthamsun280/ComfyUI-See-through` 同为该功能的**后起副本** → 正文 §三.24 已注明「不进索引」。
- **换名/衍生**：`3Asterism/dsh-whale-girl-live2d-custom` = `Andersen216/dsh-whale-girl-live2d` 的定制版，本体已收 → 仅登记。
- **fork**：`TianMengLucky/BongoCat-X` 自述 fork 自 `vladelaina/BongoCat`；`MistFloat/Airi-Forge` 为 AIRI fork → 均按 fork 规则不收（除非本体未收）。
- **旧闻换日期 / ID 新≠内容新**：本批 ★0 的 DSH 插件大量「一天建成、描述雷同」，判为同质刷榜 → 统一压进边缘登记，不成辑不收。

### 7.4 结论
- 本路共复核候选 **≈132 个**，**剔除重复 ≈74 个**，命中重复的主要来源是「前辑已收 + 同名镜像/fork + DSH 插件同质化」。
- 新增 **49 条正文条目**（§一–§五：编号 1–49，其中 §三.24 为同功能副本仅作说明）+ **1 组边缘登记**；
- 最有价值 3 条：**① `shinshin86/still2rig-psd`（★130，唯一「拆层 + QA + 动起来预演」闭环）**、**② `sayaka-aiart/StandRig`（★82，把绑定变成 MCP 工具调用）**、**③ `HELPMEEADICE/Neocari`（纯 Rust Cubism V2 加载/渲染 + 自带完整模型六件套，读格式的现成教材）**。
