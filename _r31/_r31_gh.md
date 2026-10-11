# R31 GitHub 增量调研 — Live2D 制作 / 立绘 / Cubism / moc3 / motion3 / 桌宠 / VTuber / agent 虚拟形象

- 轮次：第 31 轮（上一轮 R30 约 20 分钟前，已收录 1257 项）
- 基线：`_r31/_dedupe_gh.txt`（1230 条）+ 二次对 `index.html` 现取链接（1347 条唯一 repo 链接）双重查重
- 时间窗：`pushed:>2026-09-25` 与 `created:>2026-09-01` 各跑一遍
- 说明：新发现稀薄属正常；本轮只收「gh api 实测元数据 + 主题强相关」的条目，噪声/同名一律否决

---

### 1. Inochi2D/inochi2d  ·  ★1811 · BSD-2-Clause · D · 推送 2026-10-03
- URL: https://github.com/Inochi2D/inochi2d
- 是什么：开源 2D 木偶（puppet）动画 SDK，即 Inochi2D 运行时。目标就是做 Live2D Cubism 的开源替代：把分层立绘绑定成可实时驱动、可做表情/物理的 2D 角色，用于 VTubing、游戏与实时应用。
- 关键数字/事实：⭐1811 · BSD-2-Clause · 创建 2020-10-08 · 未归档 · 语言 D · homepage https://inochi2d.com
- 判定：✅采纳 —— 许可证明确、有完整代码、不买 Cubism Editor 就能干活的唯一成熟开源路线（index 只收了它的编辑器 inochi-creator，SDK 本体此前未收）。

### 2. nijigenerate/nijigenerate  ·  ★314 · BSD-2-Clause · D · 推送 2026-10-10
- URL: https://github.com/nijigenerate/nijigenerate
- 是什么：面向 nijilive 木偶格式（派生自 Inochi2D v0.8）的开源编辑器，用来给模型绑骨/绑定，供游戏或 VTubing 等实时应用使用。可理解为 Inochi2D 生态里的「绑定编辑器」。
- 关键数字/事实：⭐314 · BSD-2-Clause · 创建 2024-06-02 · 未归档 · 语言 D
- 判定：✅采纳 —— 与 inochi2d 配套的绑定工具，许可证清晰、活跃，替代 Cubism Editor 的合理选择。

### 3. shinshin86/mesh-avatar-studio  ·  ★597 · MIT · TypeScript · 推送 2026-10-11
- URL: https://github.com/shinshin86/mesh-avatar-studio
- 是什么：把「一张插画」变成可动画的 2D 网格（mesh）虚拟形象——配合一个编码 agent + 本地编辑器完成绑定与驱动，主打「一条命令/一个 agent 流程」出可动立绘。
- 关键数字/事实：⭐597 · MIT · 创建 2026-10-04（极新）· 未归档 · 语言 TypeScript · 近 7 天仍高频推送
- 判定：✅采纳 —— MIT、有代码、agent 驱动的工作流与本机场景高度吻合；建仓仅几天即 597★，值得优先试。

### 4. CheshireMew/PuppetLoom  ·  ★245 · AGPL-3.0 · TypeScript · 推送 2026-10-05
- URL: https://github.com/CheshireMew/PuppetLoom
- 是什么：把分层角色 PSD 变成「可自动制作、可验证、可继续校准」的 2D 动态角色；Electron 桌面应用 + CLI + Codex skill。topics：live2d / psd / character-rigging / vtuber / electron / windows。README 有中/英/日三语。
- 关键数字/事实：⭐245 · AGPL-3.0 · 创建 2026-08-14 · 未归档 · 语言 TypeScript · 仓库约 19 MB · topics 含 live2d, psd, codex-skill, windows
- 判定：✅采纳 —— 描述虽为空但 README 级已核实清楚：PSD→绑定的自动化工具链，明确标注 Windows/Codex，与本机场景直接相关（AGPL 需注意分发条款）。

### 5. zeikar/iki  ·  ★15 · MIT · TypeScript · 推送 2026-10-10
- URL: https://github.com/zeikar/iki
- 是什么：面向 Web 的开放 Live2D 替代 2D 木偶引擎，带开放 `.iki` 格式、AI 自动绑骨器，并捆绑一个 Claude Code 插件，主打「AI 能直接构建」。
- 关键数字/事实：⭐15 · MIT · 创建 2026-06-04 · 未归档 · 语言 TypeScript · homepage https://zeikar.dev/iki/
- 判定：✅采纳 —— MIT + 开源格式 + AI 自动绑定 + agent 插件，正是「不买 Cubism 也能干活」路线里少见的 Web 侧实现。

### 6. Yoru-KenomoVT/ayatsuri_2d  ·  ★2 · GPL-3.0 · Rust · 推送 2026-09-13
- URL: https://github.com/Yoru-KenomoVT/ayatsuri_2d
- 是什么：实时 2D 木偶动画与绑定的跨平台开源工具，自称 Live2D Cubism 的开放替代，声称对 moc3 格式 v3–v6 做端到端支持。
- 关键数字/事实：⭐2 · GPL-3.0 · 创建 2026-09-08 · 未归档 · 语言 Rust · 仅 README 级核实
- 判定：✅采纳 —— 许可证明确、紧扣 moc3，主题命中度极高；但目前仅 2★、建仓数天，能力需实跑验证（谨慎采纳）。

### 7. codewayco/Inkinesis  ·  ★6 · Apache-2.0 · TypeScript · 推送 2026-10-05
- URL: https://github.com/codewayco/Inkinesis
- 是什么：把插画转成可移植的 2D 角色绑定（rig）；输入文本或图片，输出 Inochi2D 与 Live2D 两种 rig，并针对官方运行时做校验。
- 关键数字/事实：⭐6 · Apache-2.0 · 创建 2026-09-25 · 未归档 · 语言 TypeScript
- 判定：✅采纳 —— Apache-2.0、双格式输出、以官方运行时做验证，是「一张图 → 可用模型」流水线里较规范的一环。

### 8. marukun712/kokoro  ·  ★42 · MIT · TypeScript · 推送 2026-10-06
- URL: https://github.com/marukun712/kokoro
- 是什么：「面向工程师的 2D 角色网格变形库」——提供 2D 角色网格变形能力，可作立绘驱动/变形的底层组件。
- 关键数字/事实：⭐42 · MIT · 创建 2026-04-02 · 未归档 · 语言 TypeScript
- 判定：✅采纳 —— MIT、纯库、与立绘变形场景相关，适合作为自建桌宠/看板娘的渲染底座。

### 9. mw2wbyys6t-sudo/live2d-auto-pipeline  ·  ★10 · Apache-2.0 · Python · 推送 2026-10-10
- URL: https://github.com/mw2wbyys6t-sudo/live2d-auto-pipeline
- 是什么：Live2D 全流程自动化项目，目标是从素材全自动生成「可部署运行」的 Live2D 模型，覆盖拆分/绑定/导出各环节。
- 关键数字/事实：⭐10 · Apache-2.0 · 创建 2026-05-14 · 未归档 · 语言 Python
- 判定：✅采纳 —— Apache-2.0、Python、主题正中「自动化制作」，与 See-through + psd2live 思路同源，值得对照。

### 10. sayaka-aiart/cubism-api-bridge  ·  ★11 · MIT · TypeScript · 推送 2026-09-12
- URL: https://github.com/sayaka-aiart/cubism-api-bridge
- 是什么：Cubism Editor External API 的非官方 TypeScript/Python 桥接与本地 HTTP 服务，附 StandRig 集成——即用脚本/agent 去驱动 Cubism Editor 自动化。
- 关键数字/事实：⭐11 · MIT · 创建 2026-09-10 · 未归档 · 语言 TypeScript · 自述 Experimental
- 判定：✅采纳 —— MIT、直击「用 agent 自动化 Cubism Editor」痛点；注意其自评为实验性。

### 11. Jelosus2/BD2-L2D-Viewer  ·  ★540 · MIT · Vue · 推送 2026-10-08
- URL: https://github.com/Jelosus2/BD2-L2D-Viewer
- 是什么：面向《Brown Dust 2》的 Web 端 Live2D 与 Spine 动画交互查看器，纯浏览器渲染。
- 关键数字/事实：⭐540 · MIT · 创建 2025-06-28 · 未归档 · 语言 Vue · homepage https://jelosus2.github.io/BD2-L2D-Viewer/
- 判定：✅采纳 —— MIT、高星、稳定更新，是 Web 侧 Live2D+Spine 渲染的实用参考/组件来源。

### 12. StudioRaming/warudo-agent-bridge  ·  ★9 · MIT · C# · 推送 2026-10-10
- URL: https://github.com/StudioRaming/warudo-agent-bridge
- 是什么：MCP server + CLI，让 AI agent（Claude、Codex 及任意 MCP 客户端）能「看到并驱动」运行中的 WARUDO：场景、资产、角色姿势与 IK、表情、蓝图、相机与截图。
- 关键数字/事实：⭐9 · MIT · 创建 2026-09-28 · 未归档 · 语言 C# · 已发 npm 包 @studioraming/warudo-agent-bridge
- 判定：✅采纳 —— MIT、现成 MCP 工具集，是「agent 直接操控虚拟形象/场景」的少见工程化产物。

### 13. morettt/my-neuro  ·  ★1389 · MIT · JavaScript · 推送 2026-10-05
- URL: https://github.com/morettt/my-neuro
- 是什么：自制 AI 桌面伴侣——可定制角色与语音对话，1 秒内响应，含长期记忆、视觉识别、声音克隆与 LLM 训练，兼容多种 Live2D 定制。
- 关键数字/事实：⭐1389 · MIT · 创建 2024-12-30 · 未归档 · 语言 JavaScript
- 判定：✅采纳 —— MIT、高星、成熟，是桌宠/伴侣赛道最值得对照的基线项目之一。

### 14. Playa-Cyrene/Cyrene-Agent  ·  ★696 · MIT · TypeScript · 推送 2026-10-09
- URL: https://github.com/Playa-Cyrene/Cyrene-Agent
- 是什么：开源桌面 AI 智能体，基于「昔涟」形象，属于带虚拟形象的桌面 agent 方向。
- 关键数字/事实：⭐696 · MIT · 创建 2026-07-06 · 未归档 · 语言 TypeScript · homepage https://playaagentcyrene.online/
- 判定：✅采纳 —— MIT、高星，与 agent 桌宠场景强相关。

### 15. Xinrea/JPet  ·  ★105 · MIT · C++ · 推送 2026-10-09
- URL: https://github.com/Xinrea/JPet
- 是什么：Live2D 桌面宠物（C++ 实现），老项目持续维护。
- 关键数字/事实：⭐105 · MIT · 创建 2020-03-07 · 未归档 · 语言 C++ · homepage https://pet.vjoi.cn
- 判定：✅采纳 —— MIT、原生实现、长期维护，适合做低占用 Windows 桌宠的参考。

### 16. MacchaPafe/D_sakiko  ·  ★96 · GPL-3.0 · Python · 推送 2026-10-08
- URL: https://github.com/MacchaPafe/D_sakiko
- 是什么：Live2D + AI Agent + GPT-SoVITS 组合的桌面 AI 数字角色。
- 关键数字/事实：⭐96 · GPL-3.0 · 创建 2025-05-26 · 未归档 · 语言 Python · homepage https://www.dsakiko.org
- 判定：✅采纳 —— 许可证明确、语音+形象链路完整，与本地 TTS+Live2D 场景吻合（GPL 注意分发）。

### 17. moonrailgun/vtubeleaf  ·  ★13 · MIT · TypeScript · 推送 2026-10-10
- URL: https://github.com/moonrailgun/vtubeleaf
- 是什么：用于会议场景的本地 Live2D 虚拟形象面捕/跟踪，基于 Tauri + MediaPipe。
- 关键数字/事实：⭐13 · MIT · 创建 2026-09-07 · 未归档 · 语言 TypeScript · homepage vtubeleaf.moonrailgun.com
- 判定：✅采纳 —— MIT、Tauri 本地应用、MediaPipe 面捕，与本机场景贴合。

### 18. NekoUnix/A.R.I.A  ·  ★10 · MIT · Rust · 推送 2026-10-05
- URL: https://github.com/NekoUnix/A.R.I.A
- 是什么：跨平台 Avatar Studio（Alpha，Rust）：支持 Live2D、PNG/GIF、VRM 及实验性 GLB，共享跟踪、弹性骨骼、灯光、可视化动作与多形象 OBS 输出。
- 关键数字/事实：⭐10 · MIT · 创建 2026-09-11 · 未归档 · 语言 Rust
- 判定：✅采纳 —— MIT、Rust 一站式形象工作室，OBS 多形象输出对直播/桌宠很实用（Alpha）。

### 19. JiGuang283/VRMify  ·  ★7 · GPL-3.0 · Python · 推送 2026-10-11
- URL: https://github.com/JiGuang283/VRMify
- 是什么：带 GUI 的 PMX/MMD → VRM 转换器：把 MMD、FBX、unitypackage、XPS、PSK 模型转成 VRM 1.0/0.x（MToon、SpringBone、表情），供 VSeeFace、UniVRM、VTuber 应用使用；纯 Python，无需 Blender/Unity。
- 关键数字/事实：⭐7 · GPL-3.0 · 创建 2026-10-08 · 未归档 · 语言 Python · 有 Release 产物
- 判定：✅采纳 —— GPL、纯 Python 免 Blender/Unity、直接产出 VRM，与本地 VTuber 资产链相关。

### 20. luckui/HiyoriAI  ·  ★93 · MIT · TypeScript · 推送 2026-10-10
- URL: https://github.com/luckui/HiyoriAI
- 是什么：带 Live2D 角色的桌面 AI 助手，接入现代 LLM。
- 关键数字/事实：⭐93 · MIT · 创建 2026-03-16 · 未归档 · 语言 TypeScript
- 判定：✅采纳 —— MIT、主题正中「桌面 AI 助手 + Live2D 角色」。

### 21. yuri-os/YuriOS  ·  ★33 · Apache-2.0 · Python · 推送 2026-10-10
- URL: https://github.com/yuri-os/YuriOS
- 是什么：面向 agentic AI 伴侣的开源、本地友好运行时——常驻「大脑」+ 可自编辑记忆；模型、记忆、角色都归用户所有。
- 关键数字/事实：⭐33 · Apache-2.0 · 创建 2026-07-14 · 未归档 · 语言 Python · homepage https://yurios.org/
- 判定：✅采纳 —— Apache-2.0、本地优先、可自选形象，属 agent 虚拟形象基础设施。

### 22. Xinhaihai-Xinhaihai/Table_pet_xinhaihai  ·  ★5 · MIT · C# · 推送 2026-10-07
- URL: https://github.com/Xinhaihai-Xinhaihai/Table_pet_xinhaihai
- 是什么：Windows 桌面宠物，支持矢量/PNG/GIF/Live2D 多种形态。
- 关键数字/事实：⭐5 · MIT · 创建 2026-09-17 · 未归档 · 语言 C#
- 判定：✅采纳 —— MIT、Windows 原生、多形态桌宠，轻量可参考。

### 23. J621111/live2d-automation  ·  ★77 · 许可证未标注 · Python · 推送 2026-09-27
- URL: https://github.com/J621111/live2d-automation
- 是什么：Live2D 自动化 MCP Server——从单张角色图生成中间态 Live2D 包，提供图像分析、人脸提取、图层生成、绑骨、物理、动作、导出等 MCP 工具；导出为 mock `.moc3` 并带校验契约。
- 关键数字/事实：⭐77 · 无 license（gh 返回 NO）· 创建 2026-02-21 · 未归档 · 语言 Python · 仓库约 467 KB
- 判定：🔶观察 —— 方向极对（MCP + 单图→模型），但目前是 mock 导出且有并发/TTL 等实验性约束；无明确许可证，暂不入库。

### 24. cqzaaa/AgentPet  ·  ★262 · 许可证未标注 · TypeScript · 推送 2026-10-10
- URL: https://github.com/cqzaaa/AgentPet
- 是什么：基于 Electron + React 的桌面智能 AI 助手，带 Live2D 动态外观与自主决策 Agent 引擎，支持 SSH 远程、Computer Use、工具箱与 MCP，并基于 ACP 支持多 Agent 本地/远程调度。
- 关键数字/事实：⭐262 · 无 license · 创建 2026-06-15 · 未归档 · 语言 TypeScript
- 判定：🔶观察 —— 功能与主题高度契合且高星，但许可证缺失，需补许可后再采纳。

### 25. AOrbitron/Eridanus  ·  ★206 · 许可证不明(NOASSERTION) · Python · 推送 2026-10-10
- URL: https://github.com/AOrbitron/Eridanus
- 是什么：基于 OneBot 协议的多功能 bot 兼开发框架，以 LLM function calling 为核心；支持「不接 QQ 的纯 Live2D 桌宠模式」。
- 关键数字/事实：⭐206 · NOASSERTION · 创建 2024-07-23 · 未归档 · 语言 Python · homepage https://eridanus.netlify.app
- 判定：🔶观察 —— 高星且含纯 Live2D 桌宠模式，但许可证不明确，暂观察。

### 26. phoiex/AAAAGENT  ·  ★142 · 非商业(NOASSERTION) · TypeScript · 推送 2026-10-10
- URL: https://github.com/phoiex/AAAAGENT
- 是什么：带语音、情绪记忆、微信及 Codex / DeepSeek Harness 的 Live2D 伴侣；macOS 优先，Windows 开发中；非商业、需署名。
- 关键数字/事实：⭐142 · NOASSERTION（非商业+署名）· 创建 2026-09-17 · 未归档 · 语言 TypeScript
- 判定：🔶观察 —— 主题契合、与 DSH/Codex 打通，但非商业许可 + Windows 尚在开发，暂观察。

### 27. vcamapp/app  ·  ★278 · MIT · Swift · 推送 2026-10-10
- URL: https://github.com/vcamapp/app
- 是什么：VTuber Camera——macOS 应用，通过 CoreMedia I/O 的虚拟摄像头输出你的虚拟形象。
- 关键数字/事实：⭐278 · MIT · 创建 2022-02-08 · 未归档 · 语言 Swift · homepage https://vcamapp.com/en
- 判定：🔶观察 —— 许可证清晰、质量高，但仅 macOS（本机为 Windows 场景），暂观察。

### 28. pakholeung37/gd_cubism  ·  ★0 · 许可证不明(NOASSERTION) · C++ · 推送 2026-09-16
- URL: https://github.com/pakholeung37/gd_cubism
- 是什么：Godot 的 Cubism 集成，带批渲染与屏幕空间遮罩图集。
- 关键数字/事实：⭐0 · NOASSERTION · 创建 2026-09-16 · 未归档 · 语言 C++
- 判定：🔶观察 —— Godot + Cubism 正是本机目标场景，但 0★、许可证不明、建仓不足月，仅 README 级核实。

### 29. DasterProkio/awesome-ai-companion  ·  ★914 · CC0-1.0 · HTML · 推送 2026-10-10
- URL: https://github.com/DasterProkio/awesome-ai-companion
- 是什么：AI 伴侣 / 桌宠 / 长期记忆 / 主动对话方向的 awesome 项目大全（人机恋开源项目合集）。
- 关键数字/事实：⭐914 · CC0-1.0 · 创建 2026-07-03 · 未归档 · 语言 HTML
- 判定：🔶观察 —— 非代码而是索引清单，但 CC0、覆盖广，可作为后续轮次的选题来源。

### 30. Hera-Berg/open-avatar-studio  ·  ★0 · 许可证未标注 · TypeScript · 推送 2026-09-24
- URL: https://github.com/Hera-Berg/open-avatar-studio
- 是什么：免费的 Live2D Studio 开源替代，用开放的社区驱动模型格式渲染与动画 2D 模型。
- 关键数字/事实：⭐0 · 无 license · 创建 2026-09-10 · 未归档 · 语言 TypeScript · 仅 README 级核实
- 判定：🔶观察 —— 方向正中主题，但 0★ + 无许可证，暂观察（同作者另有 open-avatar-creator，已在基线中被剔）。

### 31. shicheng5589-oss/Codex-desktop-pet  ·  ★20 · 许可证不明(NOASSERTION) · Python · 推送 2026-09-25
- URL: https://github.com/shicheng5589-oss/Codex-desktop-pet
- 是什么：跟随 Codex 状态实时变化的 Live2D 桌面宠物（Windows）。
- 关键数字/事实：⭐20 · NOASSERTION · 创建 2026-09-25 · 未归档 · 语言 Python · topics 含 live2d, desktop-pet, codex, webview2, windows
- 判定：🔶观察 —— 与 Codex agent 状态联动、明确 Windows，但许可证不明确，暂观察。

### 32. mtxcjnb/Arknight_Wallpaper  ·  ★3 · GPL-3.0 · JavaScript · 推送 2026-10-09
- URL: https://github.com/mtxcjnb/Arknight_Wallpaper
- 是什么：基于 Electron 的 Ubuntu 明日方舟 Live2D 动态壁纸播放器（AKLive2D 非官方第三方客户端）。
- 关键数字/事实：⭐3 · GPL-3.0 · 创建 2026-09-20 · 未归档 · 语言 JavaScript
- 判定：✅采纳 —— 许可证明确、Live2D 动态壁纸/播放器场景相关；注意其目标平台标注为 Ubuntu。

### 33. haneoka-gakuen/bangdream-live2d  ·  ★4 · 许可证未标注 · Python · 推送 2026-10-11
- URL: https://github.com/haneoka-gakuen/bangdream-live2d
- 是什么：《BanG Dream! 少女乐团派对》角色的 Live2D 模型集合。
- 关键数字/事实：⭐4 · 无 license · 创建 2025-05-10 · 未归档 · 语言 Python
- 判定：❌否决 —— 纯游戏模型资产搬运，非工具/非可复用技术，且许可证不明、版权风险高。

### 34. aruveletton-rgb/arknights_live2d  ·  ★4 · 许可证未标注 · TypeScript · 推送 2026-10-08
- URL: https://github.com/aruveletton-rgb/arknights_live2d
- 是什么：明日方舟风格 Live2D 桌宠项目的「说明与提问窗口」（自述不存放项目代码）。
- 关键数字/事实：⭐4 · 无 license · 创建 2026-07-06 · 未归档 · 语言 TypeScript
- 判定：❌否决 —— 自述不含代码，无实质产出，许可证不明。

### 35. rydanee/live2drust  ·  ★0 · 许可证未标注 · Rust · 推送 2026-09-23
- URL: https://github.com/rydanee/live2drust
- 是什么：一个简单的 `.moc3` 模型查看器（Rust），自称后续会扩展。
- 关键数字/事实：⭐0 · 无 license · 创建 2026-09-10 · 未归档 · 语言 Rust · 仅 README 级核实
- 判定：❌否决 —— 0★ + 无许可证 + 功能停留在「简单查看器」。

### 36. danirukun/opensekai  ·  ★0 · 许可证未标注 · TypeScript · 推送 2026-10-10
- URL: https://github.com/danirukun/opensekai
- 是什么：OpenSekai——开源可定制的 VTubing 3D 引擎，用 WebGPU + Tauri v2。
- 关键数字/事实：⭐0 · 无 license · 创建 2026-10-04 · 未归档 · 语言 TypeScript
- 判定：❌否决 —— 0★、无许可证、建仓数天，无实质可用产出。

### 37. Hana-ame/live2d-viewer  ·  ★0 · 许可证未标注 · TypeScript · 推送 2026-09-19
- URL: https://github.com/Hana-ame/live2d-viewer
- 是什么：Live2D 模型查看器，浏览器内渲染 Cubism 模型，不打包模型数据（用户上传式）。
- 关键数字/事实：⭐0 · 无 license · 创建 2026-09-18 · 未归档 · 语言 TypeScript
- 判定：❌否决 —— 0★、无许可证，功能与既有 viewer 重复、无增量。

---

## 已收录（剔除）

以下命中基线 `_r31/_dedupe_gh.txt` 或 `index.html`，本轮剔除、不入库：

- moeru-ai/airi（★50263）
- tsunehimatoi/psd2live（★612）
- umamoorg/umamo（★151）
- stevenjoezhang/live2d-widget（★10980）— ⚠️ 在 index.html 内，但 **不在 dedupe 基线**（基线漏收，故二次用 index.html 兜底）
- A8Chann/dsh-pet-live2d（★38）— 同样在 index.html 内、dedupe 基线漏收
- Andersen216/dsh-whale-girl-live2d（★28）
- RevStudio/Rev2D（★7）
- Hera-Berg/open-avatar-creator
- Pal-AI-Lab/Cortico（★198）
- shinshin86/aituber-onair（★267）
- shinshin86/live2d-add-motion-sample-web-ui（★195）
- KurisuMakise004/renderkit（★29）
- ptghb/virtual-person（★45）
- myths-labs/prometheus-avatar（★17）— 命中基线 dedupe 与 index.html（首轮查重时误拼为 myth-labs 漏检，已修正剔除）
- jianchengwang/live2d_models（★28）
- luomo66ccff/Amahane-Hikari-Live2D（★113）
- Ariakage/live2d-agent-kit（★26）
- fifteen42/live2d-from-art（★11）
- canyueY/pyqt-live2d-bridge（★1）
- Hana-ame/moc3-json-viewer
- funlin724/emote-to-cubism
- lvhaojie456/image-to-live2d（★2）
- flowingduskpro/jpg-to-live2d-workflow（★4）
- 7l-ui/whalegirl-pet
- momori777/Artemis（★381）
- SherlockYzz/anime-desktop-pet（★9）

## 负结论

- **`live2d+renpy` 两个时间窗均为 0 结果** —— Ren'Py 侧已无新料，下轮不必再投。
- **`motion3` 几乎全是同名噪声**（"motion 3d" / 物理课作业 / 隐私政策），唯一沾边的是 `arkrolin/VLive`（用 Live2D 生成 motion3.json 参数曲线，0★无许可证），无可用产出。
- **`cubism` 关键词被大量同名噪声污染**：立体主义画派（cubismo-sintetico/Cubismo）、图书馆座位管理（Cubismart）、设计系统等，务必带 `live2d` 或 `moc3` 限定。
- **`vtube` / `vtuber` 关键词信息量极低**：绝大多数是 VTuber 索引站、粉丝页、播放量追踪、日程工具，跟「制作/moc3/桌宠」无关；直接搜这两个词性价比差，建议改用 `live2d` + 场景词组合。
- **`in:readme live2d` 命中 1487 条但噪声率 ~95%**（博客、awesome 列表、AI 百宝箱等误命中，"live2d" 仅在 README 提一句）；`in:name live2d`（117 条）质量明显更高，后续优先用 in:name。
- **DSH（DeepSeek Harness）桌宠是当前最密集的增量簇**：dsh-whale-girl-live2d / dsh-pet-live2d / dsh-live2d-avatar / dsh-pet / dsh-live2d-widget 等大量同源插件，其中多条已收录；后续可专门按 `dsh` + `live2d` 收口，但注意重复率极高。
- **0★ 且描述为空的一批（kateli326-web/cubism、leo1133/live2d、OOOLLLA/moc3、rezabusiness/live2d 等）为占位/垃圾仓**，不投入。

## 搜索覆盖

时间窗 `pushed:>2026-09-25`（S）与 `created:>2026-09-01`（C）各跑一遍：

- 主关键词：`live2d`（S/C）、`cubism`（S/C）、`moc3`（S/C）、`motion3`（S/C）
- 组合：`live2d+cubism`（S/C）、`live2d+godot`（S/C）、`live2d+unity`（S/C）、`live2d+web`（S/C）、`psd+live2d`（S/C）、`live2d+mcp`（S/C）、`live2d+agent`（S/C）、`live2d+desktop+pet`（S/C）、`live2d+renpy`（S/C）、`live2d+alternative`（S/C）、`cubism+sdk`（S/C）
- 宽词：`vtube`（S/C）、`vtuber`（S/C）、`vtuber+live2d`（S）
- 限定符：`live2d+in:name`（S/C）、`live2d+in:readme`（S）
- 旁系：`inochi2d`（S）
- 单仓库核实：`gh api repos/<owner>/<repo>`（约 90 次），并对 PuppetLoom/live2d-automation 读取 README/topics
- 查重：对全部候选同时 grep `_r31/_dedupe_gh.txt` 与 `index.html`
