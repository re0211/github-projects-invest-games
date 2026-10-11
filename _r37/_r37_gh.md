# 第三十七辑 · gh 路（2026-10-11）

## 一、本路一句话

**「Cubism 之外」的那条线本辑第一次凑齐了三个正交方向 —— 反向解析（moc3→PSD/cmo3）、非官方宿主（macOS/Rust 原生、Zellij/终端、Godot）、以及把桌宠当 agent 状态灯的那批 MCP/插件；而正向「PSD→自动绑定」这一格本轮无新增（上两辑的 psd2live / CLI-Anything 都已进索引）。**

> 说明：本路 32 条正文。★ / 许可证 / 语言 / pushed_at **全部走 `gh api repos/<r>` 实取，取数日期 2026-10-11**。
> 本机对未缓存路径会 404 假阴性（见 §五），所有 404 项均已注明并尽量走第二通道。

---

## 二、正文条目

### A. agent × Live2D（本辑独立成节）

#### 1. kongweiguang/xiaoya（★1 · MIT · TypeScript）
**「会听会说会行动」的中文数字人助手**：实时语音对话 + 自然打断 + Live2D 神态/口型同步 + 本地语音处理 + MCP 工具扩展。
- 关键机制：把「Live2D 神态 + 口型」与「agent 执行任务」放在同一条实时链里（LiveKit 实时语音 + Live2D 口型驱动 + MCP 工具调用），喊出的口号是「让 AI 从回答问题走向完成任务」。
- 可复用性：**⚠️ 参考**。立意（Live2D 当 agent 的「脸 + 状态」）正是本辑主线，但仓库刚建、★1，别当依赖；可抄它的「神态 ⇄ 工具调用」状态映射。
- 证据：`gh api repos/kongweiguang/xiaoya` → ★1 / MIT / TypeScript / pushed 2026-10-11T10:33:20Z（取数 2026-10-11）。
- URL：https://github.com/kongweiguang/xiaoya

#### 2. Rosa134/daidai-live2d-pet（★12 · MIT · JavaScript）
**开箱即用的 Electron Live2D 桌宠，内置 Codex/Claude Code 状态气泡**：监听 Codex / Claude Code 会话状态，在角色头顶弹中文气泡，并按「思考 / 运行工具 / 回复 / 完成」切换模型动作。
- 关键机制：双模式共存 —— ① 工作提醒模式（agent 状态 → Live2D 动作 + 中文气泡）；② 角色陪伴模式（OpenAI 兼容文本接口 + 火山引擎 TTS + RMS 口型同步 + 随机肢体动作）。技术栈 Electron 透明窗 + 系统托盘 + 后台管理。
- 可复用性：**✅ 落地**。正好命中「DSH/Claude Code 插件 → Live2D 桌宠」这条接口，MIT 可自由改；对同时开多个 agent 跑长任务的人是真痛点。
- 证据：`gh api repos/Rosa134/daidai-live2d-pet` → ★12 / MIT / JavaScript / pushed 2026-07-25T17:58:21Z（取数 2026-10-11）。
- URL：https://github.com/Rosa134/daidai-live2d-pet

#### 3. hacxy/dsh-live2d（★0 · MIT · TypeScript）
**DSH 插件版 Live2D 桌宠**：基于 `lrplrplrp/live2d` 改造，移除对话框/小游戏/外部 API，新增 DSH 状态驱动、拖拽/缩放/画布调整、眼睛跟随、实时推送，深度集成 DSH 设置页。
- 关键机制：`window.ModuleLoader + ctx.slots + webServer SSE` 挂载；PIXI.js 7 + pixi-live2d-display（含 `model.focus` 视线跟随）。第三方沙箱评级 L5 运行时通过（dsh 0.1.2-alpha.1，2026-09-06 捕获）。
- 可复用性：**⚠️ 参考**。是「DSH 插件协议 → Live2D」的一个可运行样本；但母本 `lrplrplrp/live2d` 最后推送 2025-03，长期维护存疑。
- 证据：`gh api repos/hacxy/dsh-live2d` → ★0 / MIT / TypeScript / pushed 2026-08-18T08:07:21Z（取数 2026-10-11）。
- URL：https://github.com/hacxy/dsh-live2d

#### 4. f25h-233/live2dpet（★7 · GPL-3.0 · Python）
**「基于 Claude Code 开发」的 Live2D 桌宠**：Python + PySide6 无边框透明桌宠，多厂商 LLM（OpenAI/DeepSeek/Ollama）流式对话 + 情感标签 + GPT-SoVITS 语音 + mss 截屏多模态主动搭话 + psutil 系统监控吐槽。
- 关键机制/数字：**四进程 ZeroMQ IPC 分离（前端渲染 / LLM 推理 / TTS / 系统监控）**，Pydantic 定义消息协议，带健康检查/自动重连/流式广播；含完整 pytest 覆盖与 Windows 托盘。
- 可复用性：**⚠️ 参考**。架构（多进程 IPC 把渲染和推理解耦）值得抄；⚠️ GPL-3.0 传染，做产品先想清楚。
- 证据：`gh api repos/f25h-233/live2dpet` → ★7 / GPL-3.0 / Python / pushed 2026-08-28T18:17:43Z（取数 2026-10-11）。
- URL：https://github.com/f25h-233/live2dpet

#### 5. lrplrplrp/live2d（★0 · MIT · JavaScript）
DSH Live2D 插件的**母本仓库**（hacxy/dsh-live2d 的上游）。
- 可复用性：**❌ 不采用**。最后推送 2025-03-29，比多数下游还旧；只作谱系定位。
- 证据：`gh api repos/lrplrplrp/live2d` → ★0 / MIT / JavaScript / pushed 2025-03-29T15:08:39Z（取数 2026-10-11）。
- URL：https://github.com/lrplrplrp/live2d

#### 6. HH1st/hoho-avatar（★3 · MIT · TypeScript）
**「说话 + 音频驱动」头像的 source-first 工具包**：SDK 化的 `createAvatar()`，同一 API 下可选 Canvas 或 Three.js 渲染器；Live2D 走独立的 runtime port（隔离 Cubism/Pixi 实现）。
- 关键机制/数字：CHANGELOG 可查 —— 麦克风采集从 ScriptProcessorNode 迁到 **AudioWorklet（20ms 单声道 PCM 批）**；嘴型状态机 + 眨眼 + 动画调度共用一套 `MotionController`；Live2D 样例在 GitHub Pages 用**校验和验证的官方素材 + 同源 URL + 生产浏览器冒烟测试**上线。
- 可复用性：**⚠️ 参考**。它给出「Live2D 与 3D(Three.js) 共用一套渲染器契约」的工程范式，适合要做「2D/3D 混装」的宿主时借鉴。
- 证据：`gh api repos/HH1st/hoho-avatar` → ★3 / MIT / TypeScript / pushed 2026-09-11T05:15:09Z（取数 2026-10-11）。
- URL：https://github.com/HH1st/hoho-avatar

---

### B. 桌宠宿主

#### 7. liwenka1/bongo-cat-next（★151 · MIT · TypeScript）
**Tauri 2 + Next.js 15 的现代 Live2D 猫咪桌宠**（BongoCat 系最有维护的那一支）。
- 关键机制：pixi-live2d-display 渲染 + `rdev` 跨平台设备事件监听（键盘响应）；透明窗、镜像、点击穿透、多模型切换、托盘、全局热键、多窗口（主窗 + 设置窗）、中英 i18n；后端 Rust。
- 可复用性：**✅ 落地**。结构清晰（hooks 拆成 `_useCore/_useModelLoader/_useMotionPlayer/_useMouseEvents`），是研究 Tauri 多窗口 + Live2D 的好样本。
- 证据：`gh api repos/liwenka1/bongo-cat-next` → ★151 / MIT / TypeScript / pushed 2026-08-16T13:27:50Z（取数 2026-10-11）。⚠️ 同名的 `cherrol/bongo-cat-next` 为 **fork(true)**，parent 即本仓 → 只收本体。
- URL：https://github.com/liwenka1/bongo-cat-next

#### 8. CatStack-pixe/MochiPaw（★49 · NOASSERTION · TypeScript）
**Tauri 桌宠 + 输入反应 + 番茄钟/统计**：Live2D 行为直接绑键盘/鼠标/手柄输入，带托盘、开机自启、快捷键、更新。
- 关键机制：MIT 的 BongoCat 衍生部分 **+ PolyForm Noncommercial 增补 + 第三方素材**混许可；README 明确**商用需 CatStack / InfinityXCat 书面许可**。
- 可复用性：**⚠️ 参考**。功能面完整（含便携版 Windows zip 打包路径），但 **❌ 商用不行**，且混许可做成产品前必须逐项过一遍。
- 证据：`gh api repos/CatStack-pixe/MochiPaw` → ★49 / NOASSERTION / TypeScript / pushed 2026-10-05T07:55:57Z（取数 2026-10-11）。
- URL：https://github.com/CatStack-pixe/MochiPaw

#### 9. guipie/pingyou（★1 · MIT · Vue）
**屏友：Tauri 2 + Vue 3 + Rust 的「3D + Live2D 双引擎」桌宠**。
- 关键机制：同一窗口挂 `live2dCanvas` 与 `model3dCanvas` 两个 canvas，按模型 `engine` 字段切显隐 —— **Live2D 用 easy-live2d，3D 用 three.js**；键鼠/手柄动作同步继承 BongoCat（动态读 `resources/left-keys`、`right-keys`）；接 OpenAI 兼容接口 + 本地 Ollama。
- 可复用性：**⚠️ 参考**。★1 太新，但「一套窗口双引擎」的切换写法是稀缺参考。
- 证据：`gh api repos/guipie/pingyou` → ★1 / MIT / Vue / pushed 2026-09-18T10:02:13Z（取数 2026-10-11）。
- URL：https://github.com/guipie/pingyou

#### 10. NewComer00/Chobits（★3 · MIT · Rust）
**住在 Zellij 终端里、由 LLM 驱动的跨平台 Live2D 终端桌宠**。
- 关键机制：把 Live2D 渲染搬进终端复用器 Zellij 的窗格，而不是桌面透明窗 —— 对「以终端为主战场」的人，这是唯一形态。
- 可复用性：**⚠️ 参考**。Rust 实现 + 终端宿主这条路径独一份，抄「在非 GUI 宿主里跑 moc3」的想法。
- 证据：`gh api repos/NewComer00/Chobits` → ★3 / MIT / Rust / pushed 2026-06-30T06:07:26Z（取数 2026-10-11）。
- URL：https://github.com/NewComer00/Chobits

#### 11. SymphonyIceAttack/mac-avatar-layer（★4 · 无许可证文件 · Rust）
**Rust-first 的 macOS 原生 Live2D avatar host 原型**。
- 关键机制：目标是「用 macOS 原生层托 Live2D」，与 Win 侧的 Tauri/Electron 路线正交。
- 可复用性：**❌ 不采用**（对本机 Windows 无效 + 无 LICENSE）。登记价值在于「平台原生宿主」这条支线在 macOS 也有人做。
- 证据：`gh api repos/SymphonyIceAttack/mac-avatar-layer` → ★4 / license=none / Rust / pushed 2026-05-26T01:35:30Z（取数 2026-10-11）。
- URL：https://github.com/SymphonyIceAttack/mac-avatar-layer

#### 12. TamKungZ/VLiva（★10 · NOASSERTION · C++）
**VLiva —— 给 Linux 用的 VTuber 宿主**，直接跑 Live2D 制作的模型（描述自注「Closed-source」指模型来源非本项目代码）。
- 关键机制：C++ 原生；走 Live2D Cubism Native SDK，对标「Linux 上没有 VTube Studio」的空白。
- 可复用性：**⚠️ 参考**。Linux 宿主这条线对「只用 Windows」的基准不是刚需，但可看它如何在没有 VTS 的平台上接追踪数据。
- 证据：`gh api repos/TamKungZ/VLiva` → ★10 / NOASSERTION / C++ / pushed 2026-09-23T03:45:04Z（取数 2026-10-11）。
- URL：https://github.com/TamKungZ/VLiva

#### 13. NekoHome-Studio/mea-pet-public（★44 · MIT · Python）
**MeaPet 梅尔桌宠**：Python + PyQt5，Live2D 与 PNG 差分**双渲染引擎一键切换**，集成 AI 对话（Ollama/DeepSeek/MiMo）+ 日语 TTS（VITS/GPT-SoVITS）+ 记忆养成 + 屏幕观察三层决策吐槽。
- 关键机制/数字：主打立绘量 —— **180+ 张立绘、18 种表情、5 套服装、2 种朝向**；渲染层 Live2D 走 WebGL 硬件加速、PNG 差分走逐帧绘制；启动脚本自动装依赖（走清华镜像）。
- 可复用性：**⚠️ 参考**。早期项目（作者自称不完善），但「Live2D / PNG 差分可热切」的双引擎思路对低配机是实用退路。
- 证据：`gh api repos/NekoHome-Studio/mea-pet-public` → ★44 / MIT / Python / pushed 2026-10-05T05:20:55Z（取数 2026-10-11）。
- URL：https://github.com/NekoHome-Studio/mea-pet-public

#### 14. fswolf/luna-local-agent（★4 · MIT · Python）
**全本地、可「看见思维」的 AI 语音伴侣**：Whisper 语音进、Kokoro 语音出，带记忆、工具、插件、moods，并有推理与逐 token 置信度的实时可视化，跑在 LM Studio / llama.cpp 上。
- 关键机制：把「interpretability 视图」和 Live2D 形象并置 —— 角色不只是脸，还外显内部状态。
- 可复用性：**⚠️ 参考**。契合「本地 Ollama/LM Studio」路线，抄它的「状态外显」设计而非代码。
- 证据：`gh api repos/fswolf/luna-local-agent` → ★4 / MIT / Python / pushed 2026-10-11T11:26:43Z（取数 2026-10-11）。
- URL：https://github.com/fswolf/luna-local-agent

#### 15. isHarryh/Ark-Pets（★1124 · GPL-3.0 · Java）
**明日方舟主题桌宠（ArkPets），本辑唯一千星级通用桌宠框架**。
- 关键机制/数字：**平面重力场物理**（干员会被丢出去、能站在窗口边缘）+ 透明模式点击穿透 + 开机自启；实测**运行内存约 50–80MB**，模型库持续更新；仅 Windows（Mac/Linux 开发中）。
- 可复用性：**⚠️ 参考**。GPL-3.0 传染；但「低内存 + 物理交互」的实现值得作为桌宠体感基准。
- 证据：`gh api repos/isHarryh/Ark-Pets` → ★1124 / GPL-3.0 / Java / pushed 2026-09-26T07:13:35Z（取数 2026-10-11）。
- URL：https://github.com/isHarryh/Ark-Pets

#### 16. zhuang-HE/live2d-ai-pet（★1 · 无许可证文件 · JavaScript）
**PIXI.js + Live2D + Ollama 的浏览器/桌面 AI 伙伴**：Cubism 2/3 模型，6 情绪状态机（idle/speaking/thinking/happy/shy/surprised）、Web Speech STT/TTS、WebSocket 流式打字机、5 分钟无操作自动搭话。
- 可复用性：**❌ 不采用**（★1 + 无 LICENSE）。仅作「Ollama + Live2D 最小闭环」的登记参考。
- 证据：`gh api repos/zhuang-HE/live2d-ai-pet` → ★1 / license=none / JavaScript / pushed 2026-05-14T13:56:30Z（取数 2026-10-11）。
- URL：https://github.com/zhuang-HE/live2d-ai-pet

---

### C. 格式 / 渲染 / 逆向轮子

#### 17. Ludentes/py-moc3（★4 · MIT · Python）
**纯 Python 的 .moc3 二进制读写库**（PyPI `py-moc3`，零依赖，仅 stdlib）。
- 关键机制/数字：**能读能写，read→write 做到字节级 round-trip**（`moc3 verify` 自检）。格式拆解写得极清楚 —— 64B 头（magic "MOC3" + 版本 + 端序）+ **640B 段偏移表（160 × uint32）** + 从第 1984 字节起的 ~100 个 64B 对齐的 typed array（struct-of-arrays）。支持版本 **V3.00(1) / V3.03(2) / V4.00(3) / V4.02(4) / V5.00(5)** 读写。
- 可复用性：**✅ 落地**。这是本辑对「个人维护索引站」最有用的一条 —— 批量扫模型、读参数范围、改 texture index，全部命令行化、零 SDK、零依赖；直接 `pip install py-moc3`。
- 证据：`gh api repos/Ludentes/py-moc3` → ★4 / MIT / Python / pushed 2026-04-08T01:00:42Z（取数 2026-10-11）；PyPI 0.1.0，每周下载约 131–145。
- URL：https://github.com/Ludentes/py-moc3 · https://pypi.org/project/py-moc3/

#### 18. alksdesu/live2d-tools（★4 · 无许可证文件 · C++）
**Live2D Cubism 模型转换工具箱：.moc3 → Photoshop PSD，或还原为可编辑的 .cmo3 工程**（原名 live2d2psd）。
- 关键机制：PSD 导出把**每个 drawable（art mesh）单独渲染成一层**并保留原 Part 分组层级与命名；cmo3 生成则从 moc3 二进制里**恢复全部几何/变形器/参数/物理**（CAFF 容器 + XML 序列化）。自带模型查看器（可开 .model3.json / .moc3，支持拖拽、变形器系统、参数面板、Pose 切换）。
- 可复用性：**⚠️ 参考**。这是**逆向方向**（运行时 → 工程），用于「源码工程丢了、只剩运行时文件」的抢救；⚠️ 无 LICENSE 文件，先别商用。
- 证据：`gh api repos/alksdesu/live2d-tools` → ★4 / license=none / C++ / pushed 2026-07-13T14:10:17Z（取数 2026-10-11）。⚠️ 网页直取别名 `alksdesu/live2d2psd` 本轮 `gh api` 返回 404（假阴性，非不存在）。
- URL：https://github.com/alksdesu/live2d-tools

#### 19. Eatgrapes/Live2D-JavaBinding（★16 · MIT · Java）
**Live2D Cubism SDK 的原生 Java 绑定（JNI）**。
- 关键机制：Java API 与本地二进制**解耦分发**（native JAR 自包含）；**双后端运行时切换** `makeGL()` / `makeVulkan(...)`；功能含模型/物理/Pose 加载、表情切换、带优先级与回调的动作播放、参数读写、拖拽与命中检测、OpenGL/Vulkan 两条渲染路径。
- 可复用性：**⚠️ 参考**。对本机（Ollama + 索引站）不是刚需；价值在证明「Cubism Native 能被非 C# 生态干净封装」，以及 Vulkan 后端这一稀缺口。
- 证据：`gh api repos/Eatgrapes/Live2D-JavaBinding` → ★16 / MIT / Java / pushed 2026-06-27T09:18:37Z（取数 2026-10-11）。
- URL：https://github.com/Eatgrapes/Live2D-JavaBinding

#### 20. Lendic42/LumaStage（★1 · NOASSERTION · TypeScript）
**开源 VTuber studio：Windows/macOS 桌面端 + 局域网 iPhone Face ID 追踪**，目标是与 VTube Studio 模型文件**互操作**。
- 关键机制/数字：仓库内 **compatibility.md 是一张硬核验收矩阵** —— 逐行标了 Cubism 3/4/5 模型发现、VTS sidecar 的 parameter mapping / 表情热键 / 场景热键 / 插件 API 的「Full / Compatible subset / Best effort / Planned」，并在官方 Haru 样例与 NITORUDRAW 模型上实测过（打包运行时、localhost:8001 插件通道）。**明确声明不复制 VTS 代码、不解密受保护模型、不绕过作者限制**；Cubism Core 属专有，需用户自行按 Live2D 条款安装。
- 可复用性：**⚠️ 参考**。**它不是拿来跑的（★1、GPL-3.0-only），是拿来抄「兼容性验收清单」的** —— 想做 Live2D 宿主时，把这张表当自查表。
- 证据：`gh api repos/Lendic42/LumaStage` → ★1 / NOASSERTION（实际 GPL-3.0-only）/ TypeScript / pushed 2026-07-18T18:19:15Z（取数 2026-10-11）。
- URL：https://github.com/Lendic42/LumaStage

#### 21. Inochi2D/inochi-session（★407 · BSD-2-Clause · D）
**Inochi2D 官方的直播/串流应用** —— 即「完全开源 2D 木偶」这条替代路线的配套宿主。
- 关键机制：用自己的 INP 绑定格式（模型需在 Inochi Creator 里做），**授权全开、无运行时费用**；Linux 原生一等公民。Linux 社区实测「webcam-only 追踪与 VTube Studio 免费档在同等硬件上相当」。
- 可复用性：**⚠️ 参考**。⚠️ **最后推送 2025-11-08（约 11 个月未动）**；对「Live2D 许可有顾虑、想全开源」的场景是唯一退路，但别指望活跃维护。
- 证据：`gh api repos/Inochi2D/inochi-session` → ★407 / BSD-2-Clause / D / pushed 2025-11-08T18:18:23Z（取数 2026-10-11）。
- URL：https://github.com/Inochi2D/inochi-session

#### 22. DenchiSoft/VTubeStudio（★1313 · MIT · C#）
**VTube Studio 的 API 开发页**（本仓是 API 文档 + 示例插件，不是 VTS 本体）。
- 关键机制：定义了整个 Live2D VTuber 生态的「事实标准接口」—— 模型加载/表情/动作/物理覆盖/参数注入/事件订阅；上面第 20 条 LumaStage 的兼容矩阵正是对着这套 API 写的。
- 可复用性：**⚠️ 参考**。当「接口规范」用，别当实现用。
- 证据：`gh api repos/DenchiSoft/VTubeStudio` → ★1313 / MIT / C# / pushed 2026-09-28T23:12:53Z（取数 2026-10-11）。
- URL：https://github.com/DenchiSoft/VTubeStudio

---

### D. AI 辅助制作链条

> **本格本轮结论：正向「PSD → 自动绑定 → moc3」无新增。** 上两辑已收的 `tsunehimatoi/psd2live`（★447，本辑复核仍在榜）、`HKUDS/CLI-Anything`（42 命令 CLI）、`J621111/live2d-automation`（MCP 生图→rig）均已进索引（见 §四）。本辑只在**下游/反向**这一侧有增量。

#### 23. sandboxdream/AI-Vtuber（★107 · MIT · 无语言 · Python）
**AI 虚拟主播框架的「本体」仓库**（多平台直播 + Live2D/UE/虚拟人驱动）。
- 关键机制：ChatterBot/LLM 驱动 + TTS + SD 画图，直播多平台。⚠️ 最后推送 2023-03-16，已三年未动。
- 可复用性：**❌ 不采用**。收它只为**谱系定位**：热门 fork `Ikaros-521/AI-Vtuber`（★4464，`fork:true`，parent 即本仓）—— 按 fork 规则，**本体未收的 fork 收本体**（两者此前都未进索引）。真要用请用已长期停更判断后的 fork，谨慎。
- 证据：`gh api repos/sandboxdream/AI-Vtuber` → ★107 / MIT / pushed 2023-03-16（取数 2026-10-11）；`gh api repos/Ikaros-521/AI-Vtuber` → ★4464 / GPL-3.0 / fork:true / parent sandboxdream/AI-Vtuber / pushed 2025-07-29。
- URL：https://github.com/sandboxdream/AI-Vtuber

#### 24. haneoka-gakuen/vega（★0 · MPL-2.0 · TypeScript）
**插件化视觉小说引擎（web + native）**，Live2D 立绘由 `vega-plugin-cubism`（已进索引）承担。
- 关键机制：内核极薄、一切从插件来 —— 同族还有 `vega-plugin-composite`（把 Live2D/图片/GIF/视频拼成分层角色）、`altair-plugin-models`（分层角色可视化编辑器）。
- 可复用性：**⚠️ 参考**。整族 ★0 且 2026-10-11 同日推送，像一次性密集上线；价值在观察「Live2D 立绘被拆成可插拔模块」的引擎侧设计。
- 证据：`gh api repos/haneoka-gakuen/vega` → ★0 / MPL-2.0 / TypeScript / pushed 2026-10-11T09:47:15Z（取数 2026-10-11）。
- URL：https://github.com/haneoka-gakuen/vega

#### 25. Voine/ChatWaifu_Mobile（★1430 · MIT · C++）
**移动版「二次元 AI 老婆」聊天器**（Android，Compose + Live2D + sherpa 唇同步 + VITS + ChatGPT）。
- 关键机制：把 Live2D 形象 + 本地 TTS(逐字口型) + LLM 塞进手机端；★1430 且 2026-09-18 仍在推。
- 可复用性：**⚠️ 参考**。移动端不是本机基准的战场，但其「Compose 里挂 Live2D + 唇同步」的做法对做宿主有旁证价值。
- 证据：`gh api repos/Voine/ChatWaifu_Mobile` → ★1430 / MIT / C++ / pushed 2026-09-18T02:00:36Z（取数 2026-10-11）。
- URL：https://github.com/Voine/ChatWaifu_Mobile

---

### E. 生态 / 引擎 / 上新（2026-09 之后新建或重大更新）

#### 26. timi-liuliang/echo（★991 · MIT · C++）
**跨平台 2D/3D 游戏引擎（Qt + Lua + Vulkan）**，内置 live2d / spine / gltf2 / PBR 等模块。
- 关键机制：把 Live2D 作为引擎级 2D 角色方案之一，与 spine 并列；Sep 2026 仍在推。
- 可复用性：**⚠️ 参考**。★991 的引擎级参考，看它「Live2D 与 Spine 如何在同一渲染管线里共存」。
- 证据：`gh api repos/timi-liuliang/echo` → ★991 / MIT / C++ / pushed 2026-09-16T16:36:28Z（取数 2026-10-11）。
- URL：https://github.com/timi-liuliang/echo

#### 27. imuncle/live2d（★1156 · 无许可证文件 · JavaScript）
**Live2D 模型收集 + 展示，可直接用于静态网站**。
- 可复用性：**⚠️ 参考**（模型素材来源；⚠️ 无 LICENSE，注意模型版权）。
- 证据：`gh api repos/imuncle/live2d` → ★1156 / license=none / JavaScript / pushed 2026-01-28T13:10:23Z（取数 2026-10-11）。
- URL：https://github.com/imuncle/live2d

#### 28. Eikanya/Live2d-model（★3439 · 无许可证文件 · "Wolfram Language"）
**最大的 Live2D 模型合集类仓库**（被 Open-LLM-VTuber 等官方文档列为模型来源之一）。
- 可复用性：**⚠️ 参考**（取模型测试用；版权归原作者，不可商用分发）。
- 证据：`gh api repos/Eikanya/Live2d-model` → ★3439 / license=none / 2026-10-03 推送（取数 2026-10-11）。
- URL：https://github.com/Eikanya/Live2d-model

#### 29. IsaacBell/awesome-vtuber（★0 · CC0-1.0）
**VTuber 生产全栈资源清单**：从 Live2D rigging 到追踪、推流、硬件、AI 语音。
- 可复用性：**⚠️ 参考**。CC0，可自由摘；★0 但结构完整（含 2D 追踪、3D 替代、Avatar 制作与绑定、资产市场、AI 语音工具）。
- 证据：`gh api repos/IsaacBell/awesome-vtuber` → ★0 / CC0-1.0 / pushed 2026-09-30T02:40:42Z（取数 2026-10-11）。
- URL：https://github.com/IsaacBell/awesome-vtuber

#### 30. RifkyA911/mirunova-live（★0 · 无许可证文件 · Svelte）
**下一代 Web Live2D & 3D Avatar 视觉追踪器，100% 客户端**（Bun + SvelteKit + MediaPipe）。
- 可复用性：**❌ 不采用**（★0 + 无 LICENSE）。登记：浏览器端「Live2D/3D + 面捕」这条线又添一个 2026-10-11 当日仓库。
- 证据：`gh api repos/RifkyA911/mirunova-live` → ★0 / license=none / Svelte / pushed 2026-10-11T12:08:39Z（取数 2026-10-11）。
- URL：https://github.com/RifkyA911/mirunova-live

#### 31. An-d-u/ENE（★1 · 无许可证文件 · Python）
**住在屏幕上的 AI 桌面伴侣**：记忆上下文 + 笔记 + 情绪 + 语音 + 日历工作流（Live2D 形象）。
- 可复用性：**❌ 不采用**（★1 + 无 LICENSE + 当日新建）。
- 证据：`gh api repos/An-d-u/ENE` → ★1 / license=none / Python / pushed 2026-10-11T10:17:57Z（取数 2026-10-11）。
- URL：https://github.com/An-d-u/ENE

#### 32. qqzhangyanhua/ai-desktop-pet（★0 · 无许可证文件 · TypeScript）
**Tauri 2 + React 19 + PixiJS/oh-my-live2d + LangGraph + MCP 的「多 Agent 协作桌宠」**（天气查询 / AI 对话 / SQLite）。
- 可复用性：**❌ 不采用**（★0、无 LICENSE、2026-01 后未动）。登记：技术栈堆得很全（Vercel AI SDK + LangChain/LangGraph + tauri-plugin-sql），可看「桌宠当 agent 编排前端」的形态。
- 证据：`gh api repos/qqzhangyanhua/ai-desktop-pet` → ★0 / license=none / TypeScript / pushed 2026-01-04T02:49:13Z（取数 2026-10-11）。
- URL：https://github.com/qqzhangyanhua/ai-desktop-pet

---

## 三、边缘登记（一行一条，不进正文）

- `lmy414/live2d-to-agent` —— MCP 控制的 Live2D 桌宠（Electron + WebSocket :9228 + Python PySide6/OpenGL 双适配）；**本轮 `gh api` 与网页直取均未命中（404/空页），★/许可证未知**，仅凭 LobeHub / Glama MCP 目录页与 himcp.cn 页面确认存在。URL https://github.com/lmy414/live2d-to-agent
- `haneoka-gakuen/vega-plugin-composite`（★0 · MPL-2.0 · TS，2026-10-11）—— 把 Live2D/图片/GIF/视频拼成分层角色（vega 同族）。
- `haneoka-gakuen/altair-plugin-models`（★0 · MPL-2.0 · TS，2026-10-11）—— Altair 的分层角色可视化编辑器。
- `Meph1sto666/ArKomp`（★0 · 无 license · Rust，2026-05-06）—— 把 Live2D 渲染成桌面 overlay。
- `HaoranPei-casia/BossKey-BongoCat-Desktop-Pet`（★1 · MIT · Rust，2026-07-31）—— Boss-Key + BongoCat 桌宠 + 工作区切换。
- `qqzhangyanhua/ai-desktop-pet` 之外的 `zz` 类小体量已单列，见正文 E 组。
- `Navi-Studio/Virtual-Human-for-Chatting`（★707 · NOASSERTION · C#，2023-11-13）—— 基于 Unity 的 Live2D 虚拟人聊天（停更 2 年+）。
- `zenghongtu/PPet`（★2034 · MIT · TS，2024-06-18）—— Electron 桌面萌妹（停更）。
- `galnetwen/Live2D`（★1100 级 · JS，2020-09-21）—— 老牌 Web Live2D 展示，停更。
- `hacxy/l2d-widget`（★639 · MIT · TS，2026-08-12）—— `oh-my-live2d` 重命名后的**本体**（`ATQQ/oh-my-live2d` 是其 fork，见 §四）。
- `Project-N-E-K-O/N.E.K.O`（★3046 · Apache-2.0 · Python，2026-10-11 仍在推）—— 已在 v34 正文，仅作本轮活跃度复核。

---

## 四、去重报告（剔除了谁、为什么）

**全部命中 `_r37/_dedupe_gh.txt`（已是 index.html 卡片，1337 条基线）→ 剔除：**
- `zeikar/iki`（"open Live2D alternative that AI can build"，★15，含 Claude Code/Codex 插件）—— **已是卡**，本轮不再收。
- `moeru-ai/airi`（★50.3k）、`myths-labs/prometheus-avatar`、`RevStudio/Rev2D`（★352）、`AyagamiDev/ayagami`（★352，且 `ayagamidev/ayagami-gd` 在 urls 里被提及）、`Eatgrapes/Mocari`（★47）、`Eatgrapes/Mocari` 同名 `mocari` 亦在 backtick 列表 —— 全为卡。
- `tsunehimatoi/psd2live`（★447 · GPL-3.0 · Kotlin）—— **已是卡**（本辑复核：★447，pushed 2026-09-08~23）。**正因它是卡，本路 D 组「AI 正向绑定」才没有新增。**
- `HKUDS/CLI-Anything`（42 命令 Live2D CLI）—— 已是卡；其镜像 `q-qp-p/HKUDS-CLI-Anything` 为同内容副本 → 不收。
- `j621111/live2d-automation`（MCP 单图→rig）—— 已是卡。
- `OpenWebGAL/WebGAL`（★1.4 万级）—— 已是卡；`Yanggum/WebGAL` 为 **fork(true)，parent=OpenWebGAL/WebGAL** → 按 fork 规则不收。
- `hacxy/l2d-widget`（★639）—— 已是卡；`ATQQ/oh-my-live2d` 为 **fork(true)，parent=hacxy/l2d-widget** → 不收（仅登记本体，见 §三）。
- `MizunagiKB/gd_cubism` —— 已是卡（backtick + gh 双命中）；`VulpxVenandi25/TrueGDCubism` 为 **fork(true)，parent=MizunagiKB/gd_cubism** → 不收。
- `Perfare/UnityLive2DExtractor` —— 已是卡；`aelurum/UnityLive2DExtractor`（★58）为 **fork(true)，parent=Perfare/UnityLive2DExtractor** → 不收。
- `EasyLive2D/live2d-py`（★576）—— 已是卡；`chugf/live2d-py`、`jiangdianzhang/live2d-py` 均为 fork → 不收。
- `haneoka-gakuen/vega-plugin-cubism` —— 已是卡（故本路只收其母仓 vega）。
- `DasterProkio/awesome-ai-companion`（★920）、`waifuai/waifu-companion`、`Inochi2D/inochi2d`、`emilianavt/OpenSeeFace`、`morettt/my-neuro`、`elevenyellow/handcrafted-persona-engine`、`Playa-Cyrene/Cyrene-Agent`、`x380kkm/live2dpet`（★?，含 VOICEICONX 那条）—— 全为卡，剔除。

**命中 `_r37/_dedupe_backtick.txt`（卡内正文反引号提及型，62 条基线）→ 视同已提及，不收：**
- `eatgrapes/mocari`、`revstudio/rev2d`、`mizunagikb/gd_cubism`、`rig-c/core`、`852wa/anime2.5drig`、`flowingduskpro/jpg-to-live2d-workflow`、`lvhaojie456/image-to-live2d`、`mw2wbyys6t-sudo/live2d-auto-pipeline`、`stevenjoezhang/live2d-widget`、`1098542053/spive2d-web`、`a8chann/dsh-pet-live2d`、`andersen216/dsh-whale-girl-live2d`、`ankesu/dsh-live2d-pet`、`ariakage/live2d-agent-kit`、`cyanfish-x/dsh-live2d-pets`、`lsc-91-69/dsh-live2d-avatar`、`zziying/ai-live2d-body-starter`、`asfdfdfd/renpy-live2d`、`dihuangdebitebi/renpy_rt_tool`、`patches/psd2live-agent-kit.patch`（路径）。
  —— 这批里 `eatgrapes/mocari`（纯 Rust 运行时）与 `revstudio/rev2d` 其实很有价值，但它们已在 index.html 正文出现过，**本路不再重复收**，仅在此标注「已被提及」。
- urls 基线命中：`github.com/ayagamidev/ayagami`、`github.com/ayagamidev/ayagami-gd`、`github.com/7l-ui/whalegirl-pet/...` → 均视为已覆盖。

**同名疑点（逐条查过，不预设同源/不同源）：**
- `liwenka1/bongo-cat-next` vs `cherrol/bongo-cat-next`：**同源**，`cherrol` 那条 `fork:true`、parent 即 `liwenka1` → **只收本体**。
- `suan-11/MeaPet` vs `NekoHome-Studio/mea-pet-public`：**同一项目换 owner**（前者 `gh api` 404，后者 ★44 命中且描述匹配「梅尔桌宠」）→ 收后者的真实路径。
- `alksdesu/live2d2psd` vs `alksdesu/live2d-tools`：**同一仓库更名**（前者 404，后者 ★4 且目录与 live2d2psd 内容一致）→ 收 `live2d-tools`。
- `haxy/dsh-live2d` vs `hacxy/dsh-live2d`：**不同名不同源**，`haxy` 是拼写错误（404），真实 owner 为 `hacxy`。

---

## 五、负结论（一律写「本轮未命中」，不写「不存在」）

1. **moc3 渲染 runtime 的纯 Rust 实现**：本辑 API 多次指向 `Eatgrapes/Mocari`（★47）与 `AyagamiDev/ayagami`（★352）—— 二者**均已是索引卡**，本轮**无新增第三方 Rust 运行时命中**。
2. **PSD → 自动绑定的正向工具**：本轮**未命中**任何未收/non-card 的新仓库（psd2live / CLI-Anything / live2d-automation 全为卡）。
3. ⚠️ **404 假阴性清单（本机代理对未缓存路径 404，不代表不存在）**：`lmy414/live2d-to-agent`、`suan-11/MeaPet`、`alksdesu/live2d2psd`（已分别换第二通道或更正 owner 核实）。**绝不据此写「死链/不存在」。**
4. **DSH 插件 → Live2D 这条线**：v34 已独立成节并收了 13 条正文；本轮只新增 `hacxy/dsh-live2d` + 母本 `lrplrplrp/live2d`，其余 `dsh-*-live2d*` 族均在 backtick 基线中（已提及）。
5. **Live2D 桌宠的「显存/帧率」硬指标**：本轮**未在 GitHub 仓库 README 中命中可复现的显存/帧率 benchmark**；只有中文二手文章给出「运行内存 50–150MB、GPU 负载高/中档差 20–30%」这类区间（来源非仓库，未采信为卡片证据）。

