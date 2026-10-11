# 第三十八辑 · gh 路（2026-10-11）

> 本路只覆盖 GitHub / Gitee / HuggingFace 上的 Live2D 相关仓库与项目。CSDN/官网/论坛由其他子 agent 覆盖，本路不重复。
> 取数方式：GitHub 走 `gh api repos/<r>`（取数日 2026-10-11）；Gitee 走 `gitee.com/api/v5/repos/<r>`；HF 走 WebSearch/WebFetch。限流或 404 已标注。
> 去重基线：index.html（1386 卡，实为 r37 合并前快照）+ csdn-social-summary(.md/-v36/-v34) + **r37 已收 32 条**（上一辑刚收，视同已覆盖，避免撞车）。
> 去重操作：每条候选先 `grep -rF "owner/repo"` 比对四份基线，再比对 r37 清单，命中即弃。

## 一、搜索覆盖

- **GitHub**：`gh search repos` 多维度（live2d 按 stars/updated、moc3、cubism、vtuber、rig、web）共扫描 ~124 个不重复仓库；对疑似新仓逐一 `gh api` 取数。
- **Gitee**：WebSearch「Gitee Live2D 开源」→ 命中 5 条，逐条 `gitee.com/api/v5` 取数；剔除已收录仓库的 Gitee 镜像（BANDORI-PET-REV、Open-LLM-VTuber）。
- **HuggingFace**：WebSearch「HuggingFace Live2D」→ 命中的多为 GitHub 镜像/引用；唯一原生 HF 资产为 Muapi 的 Flux LoRA 模型（已登记）。

## 二、本路一句话主线

**本辑 gh 路的新增集中在「Live2D 宿主/查看器的二次繁荣」与「AI 桌宠的同质化海」两端**：一方面冒出一批可落地的查看器/插件/引擎（hime-display、Live2D-Viewer、vue-live2d、UnrealLive2D、Kokoro-Engine、ComfyUI-Live2DViewer、OneClick2D），另一方面是大量★0–★400 的「本地 LLM + Live2D 桌宠」克隆（openclaw、Lumi_Nox、warashi、petto、Xue_CyberNeko、Xuansi、SpiritPal、DoroPet）；**正向「PSD→自动绑定→moc3」与纯 Rust 运行时依旧无新增**（r37 的 psd2live / moc3-rs 等已卡）。Gitee 侧只有 DoroPet_V3 一个像样的新原生项目。

---

## 三、GitHub 候选（工具 / 查看器 / 插件 / 引擎 / 模型）

### 1. ezshine/AwesomeLive2D（★411 · 无许可证文件 · 2023-12-19）
**Live2D 模型 / 资源 awesome 清单**（"Awesome live2d models repository"）。
- 可复用性：**② 参考**。作为模型与资源索引对维护索引站的人有用；⚠️ 最后推送 2023-12（约 3 年未动）、无 LICENSE，仅作资源导航，别当实现。
- 证据：`gh api repos/ezshine/AwesomeLive2D` → ★411 / license=none / pushed 2023-12-19（取数 2026-10-11）。
- URL：https://github.com/ezshine/AwesomeLive2D

### 2. TSKI433/hime-display（★254 · GPL-3.0 · JavaScript · 2026-03-30）
**通用桌面模型查看器**：一套 UI 同时显示 **Live2D / Spine / MMD / VRoid** 四种模型格式。
- 关键机制：跨格式统一查看器，省去为每种格式装一个软件；桌面端运行。
- 可复用性：**② 参考**。多格式聚合查看的思路对做模型素材库预览有用；GPL-3.0 传染，做产品留意。
- 证据：`gh api repos/TSKI433/hime-display` → ★254 / GPL-3.0 / JavaScript / pushed 2026-03-30（取数 2026-10-11）。
- URL：https://github.com/TSKI433/hime-display

### 3. LIlGG/plugin-live2d（★251 · MIT · TypeScript · 2026-09-29）
**Halo 博客平台的 Live2D 看板娘插件**（"为你的网站领养一只可爱的看板娘"）。
- 关键机制：面向 Halo 生态的即插即用看板娘，2026-09 仍在推，维护活跃。
- 可复用性：**② 参考**。若你的站点/索引站基于 Halo，可直接用；否则当作"博客挂 Live2D"的最小插件样本抄。
- 证据：`gh api repos/LIlGG/plugin-live2d` → ★251 / MIT / TypeScript / pushed 2026-09-29（取数 2026-10-11）。
- URL：https://github.com/LIlGG/plugin-live2d

### 4. amorist/platelet（★226 · GPL-3.0 · JavaScript · 2026-10-05）
**经典「血小板」Live2D 网页看板娘**（描述 "けっしょうばん"，2018 建仓但 2026-10 仍在推）。
- 可复用性：**② 参考**。知名度高的萌系网页 widget，GPL-3.0；适合做"网站挂看板娘"的现成实现参考（注意医学梗版权）。
- 证据：`gh api repos/amorist/platelet` → ★226 / GPL-3.0 / JavaScript / pushed 2026-10-05（取数 2026-10-11）。
- URL：https://github.com/amorist/platelet

### 5. iCharlesZ/vscode-live2d-models（★169 · 无许可证文件 · 2026-03-25）
**VSCode 看板娘模型库**（"VSCode看板娘模型库"，收集可挂到 VSCode Live2D 插件的模型）。
- 可复用性：**② 参考**。模型资源集合（非工具），无 LICENSE，取模型测试用；版权归原作者。
- 证据：`gh api repos/iCharlesZ/vscode-live2d-models` → ★169 / license=none / pushed 2026-03-25（取数 2026-10-11）。
- URL：https://github.com/iCharlesZ/vscode-live2d-models

### 6. LSTM-Kirigaya/Live2dRender（★183 · Apache-2.0 · TypeScript · 2025-07-07）
**Web 端新版 Live2D 渲染器**（"render for new version of live2d in Web"）。
- 可复用性：**② 参考**。Apache-2.0、面向新版 Cubism 的 Web 渲染封装，可作为自己搭网页查看器/桌宠的渲染底座；⚠️ 最后推送 2025-07，非最新。
- 证据：`gh api repos/LSTM-Kirigaya/Live2dRender` → ★183 / Apache-2.0 / TypeScript / pushed 2025-07-07（取数 2026-10-11）。
- URL：https://github.com/LSTM-Kirigaya/Live2dRender

### 7. evgo2017/vue-live2d（★166 · MIT · Vue · 2026-01-27）
**Vue 组件：给网站博客加一只 Live2D 看板娘**（"为你的网站博客增加看板"）。
- 可复用性：**② 参考**。MIT、Vue 生态现成组件，适合 Vue/Nuxt 站点直接挂；2026-01 仍在推。
- 证据：`gh api repos/evgo2017/vue-live2d` → ★166 / MIT / Vue / pushed 2026-01-27（取数 2026-10-11）。
- URL：https://github.com/evgo2017/vue-live2d

### 8. Arisego/UnrealLive2D（★153 · MIT · C++ · 2025-02-26）
**UE4/Unreal 引擎的 Live2D 模型插件**（"UE4 plugin for live2d model"）。
- 可复用性：**② 参考**。Unreal 路线里少见的 Live2D 桥接，MIT 可改；⚠️ 最后推送 2025-02，Cubism SDK 版本可能偏旧，接入前先核 SDK 兼容性。
- 证据：`gh api repos/Arisego/UnrealLive2D` → ★153 / MIT / C++ / pushed 2025-02-26（取数 2026-10-11）。
- URL：https://github.com/Arisego/UnrealLive2D

### 9. redchenk/yachiyo-live2d-studio（★25 · MIT · JavaScript · 2026-10-11）
**Live2D 工作室**（yachiyo-live2d-studio，2026-10-11 当天推送，MIT）。
- 可复用性：**② 参考**。刚建即 MIT、当天活跃，定位"studio"值得盯；当前无描述，先登记，待 README 补全再评落地性。
- 证据：`gh api repos/redchenk/yachiyo-live2d-studio` → ★25 / MIT / JavaScript / pushed 2026-10-11（取数 2026-10-11）。
- URL：https://github.com/redchenk/yachiyo-live2d-studio

### 10. ImDuck42/Live2D-Viewer（★14 · MIT · JavaScript · 2026-06-17）
**功能完整的浏览器端 Live2D 查看器**：原生 JS + PIXI.js 6.5.10 + pixi-live2d-display，支持 Cubism 2.1(.moc) 与 3/4(.moc3)。
- 关键机制/数字：**四种模型载入方式** —— URL 直链 / 预设下拉 / **GitHub 仓库浏览器（输入 owner+repo 直接浏览并导入模型）** / 本地 ZIP 拖拽上传（JSZip 全客户端解压）；模块化重构到 v5.1（js/ 目录）。
- 可复用性：**① 落地**。开箱即用的网页查看器，MIT，可本地 `python -m http.server` 起、也可 GitHub Pages 部署；对"在索引站里嵌一个 Live2D 预览器"是直接可改的样本。
- 证据：`gh api repos/ImDuck42/Live2D-Viewer` → ★14 / MIT / JavaScript / pushed 2026-06-17（取数 2026-10-11）。
- URL：https://github.com/ImDuck42/Live2D-Viewer · https://imduck42.github.io/Live2D-Viewer

### 11. sweetcornna/OneClick2D（★0 · 无许可证文件 · Python · 2026-08-08）
**「先合规、重隐私」的二次元插画→可编辑 2D 形象草稿工具箱 + 开放规范**：把获授权的插画转成可检视、可编辑的 2D avatar 草稿。
- 关键机制：导出**自研 `.oc2d` 工程 + 分层 PSD**，**明确不做 Cubism `.moc3`**（绕开 Live2D 许可）；强调 rights-cleared、隐私优先、开放规范。早期项目。
- 可复用性：**② 参考**。思路稀缺——它走"不碰 Cubism 授权"的替代格式，对版权敏感场景有参考价值；⚠️ ★0、无 LICENSE、非 moc3，不能当 Live2D 绑定工具用。
- 证据：`gh api repos/sweetcornna/OneClick2D` → ★0 / license=none / Python / pushed 2026-08-08（取数 2026-10-11）。
- URL：https://github.com/sweetcornna/OneClick2D

---

## 四、AI 开发/使用相关（[AI] 标记）

> 主 agent 请逐条读、核实、实测是否有用。本组均为「LLM/本地模型 + Live2D 形象」类项目。

### [AI] 1. andyhuo520/openclaw-assistant-mvp（★408 · 无许可证文件 · JavaScript · 2026-02-13）
**Electron 版 AI 语音助手 + Live2D 角色动画**：实时语音识别 + TTS，Live2D 角色随对话做表情/口型。
- 可复用性：**② 参考**。Electron+Live2D+语音闭环的最小 MVP 样本；⚠️ 无 LICENSE，商用先问作者。
- 证据：`gh api repos/andyhuo520/openclaw-assistant-mvp` → ★408 / license=none / JavaScript / pushed 2026-02-13（取数 2026-10-11）。注：索引里另有一个同名 "OpenClaw"（MCP 长期记忆服务器），**非同一仓库**。
- URL：https://github.com/andyhuo520/openclaw-assistant-mvp

### [AI] 2. MIO-456/Lumi_Nox（★239 · MIT · Python · 2026-08-14）
**「两个 AI VTuber 同台直播」的实时引擎与编排**（"Two AI VTubers co-hosting one live show — the realtime engine & orchestration. Open-core, battle-tested by a daily stream."）。
- 关键机制：多 AI 角色同一直播间的**编排/调度**开源核（open-core），号称已被日更直播实战检验。
- 可复用性：**② 参考**。多 Agent 同台 VTuber 的编排思路稀缺且 MIT，适合做"多数字人联动"参考；open-core 意味着核心外可能有闭源部分。
- 证据：`gh api repos/MIO-456/Lumi_Nox` → ★239 / MIT / Python / pushed 2026-08-14（取数 2026-10-11）。
- URL：https://github.com/MIO-456/Lumi_Nox

### [AI] 3. YuriCrystal/ai-avatar-bot（★203 · NOASSERTION · JavaScript · 2026-07-18）
**Live2D / VRM 语音 AI 形象**：口型同步 + 知识库 + 运营后台 + 支持分析，**一行嵌入网站**。
- 可复用性：**② 参考**。站外嵌入型 AI avatar 的完整前端样本；⚠️ 许可证标 NOASSERTION（含糊），先别商用。
- 证据：`gh api repos/YuriCrystal/ai-avatar-bot` → ★203 / NOASSERTION / JavaScript / pushed 2026-07-18（取数 2026-10-11）。
- URL：https://github.com/YuriCrystal/ai-avatar-bot

### [AI] 4. inni918/warashi（★119 · NOASSERTION · Python · 2026-08-18）
**Warashi —— 免费开源桌面 AI 伴侣**：Live2D 形象 + 语音对话 + 长期记忆 + 主动搭话（"proactive conversation"）。
- 可复用性：**② 参考**。本地 Ollama 路线契合（Python + 长期记忆 + 主动对话）；⚠️ NOASSERTION 许可证。
- 证据：`gh api repos/inni918/warashi` → ★119 / NOASSERTION / Python / pushed 2026-08-18（取数 2026-10-11）。
- URL：https://github.com/inni918/warashi

### [AI] 5. funnycups/petto（★119 · GPL-3.0 · Dart · 2025-12-05）
**智能 Live2D 桌面助手**（petto，Flutter/Dart 实现，跨平台）。
- 可复用性：**② 参考**。Flutter 路线里少见的 Live2D 桌宠；GPL-3.0 传染。
- 证据：`gh api repos/funnycups/petto` → ★119 / GPL-3.0 / Dart / pushed 2025-12-05（取数 2026-10-11）。
- URL：https://github.com/funnycups/petto

### [AI] 6. Nav-Joe/Xue_CyberNeko（★7 · MIT · TypeScript · 2026-10-11）
**「A Live2D AI Neko」**：把 Live2D 形象接 AI 对话的轻量项目，2026-10-11 当天建仓、MIT。
- 可复用性：**② 参考**。小而新的 AI+Live2D 样本，MIT；刚建，待观察。
- 证据：`gh api repos/Nav-Joe/Xue_CyberNeko` → ★7 / MIT / TypeScript / pushed 2026-10-11（取数 2026-10-11）。
- URL：https://github.com/Nav-Joe/Xue_CyberNeko

### [AI] 7. DesktopPetXuansi/Xuansi（★1 · Apache-2.0 · Python · 2026-10-11）
**玄司 Xuansi：Windows 本地 AI 桌宠** —— 屏幕理解 + 语音对话 + 长期记忆 + Live2D，纯本地（契合 16GB + 本地 Ollama 基准）。
- 可复用性：**② 参考**。Apache-2.0、本地优先的定位正中基准需求；★1 太新，但协议友好，值得盯。
- 证据：`gh api repos/DesktopPetXuansi/Xuansi` → ★1 / Apache-2.0 / Python / pushed 2026-10-11（取数 2026-10-11）。
- URL：https://github.com/DesktopPetXuansi/Xuansi

### [AI] 8. ReSerendipity/SpiritPal（★0 · Apache-2.0 · TypeScript · 2026-10-11）
**桌边友 · 跨平台 AI 桌面宠物**：Tauri v2（Rust + React 19）+ **Pixi.js 8 Live2D** + 本地记忆召回。
- 关键机制：Tauri v2 + React 19 + Pixi.js 8 这一最新组合；情感陪伴 + 轻交互 + 温和生产力协助；Apache-2.0。
- 可复用性：**② 参考**。技术栈最新（Pixi.js 8 而非旧的 pixi-live2d-display），是"2026 新写法"的稀缺样本；★0 但协议好。
- 证据：`gh api repos/ReSerendipity/SpiritPal` → ★0 / Apache-2.0 / TypeScript / pushed 2026-10-11（取数 2026-10-11）。
- URL：https://github.com/ReSerendipity/SpiritPal

### [AI] 9. HELPMEEADICE/BANDORI-PET-REV（★465 · GPL-3.0 · Python · 2026-10-06）
**BandoriPet —— 基于 Live2D Cubism SDK + PySide6 的开源桌面宠物**：支持 **51+ 位 BanG Dream! 角色、305+ 套服装**。
- 关键机制/数字：**自研 LuaJIT 渲染核心**（基于 Live2D-v2-Lua），性能较原 live2d-py **提升 6 倍+（30fps → 180fps+）**，支持头部追踪/拖拽/点击互动；LLM 角色扮演 + 好感度记忆（中日英 + 动作标签）；Qwen3TTS 口型同步 + 本地 faster-whisper ASR；Fluent Design 设置面板 + 多语言 i18n。
- 可复用性：**② 参考**。模型量（50+/300+）与自研渲染核是硬指标，对桌宠体感研究价值高；⚠️ GPL-3.0 传染、且依赖官方 Cubism SDK（须自按 Live2D 条款装）。
- 证据：`gh api repos/HELPMEEADICE/BANDORI-PET-REV` → ★465 / GPL-3.0 / Python / pushed 2026-10-06（取数 2026-10-11）。Gitee 另有 `boomer001/BANDORI-PET-REV` 仅是它的镜像（剔除，见 §六）。
- URL：https://github.com/HELPMEEADICE/BANDORI-PET-REV

### [AI] 10. waterfeet/DoroPet_V3（★7 · Apache-2.0 · Python · 2026-07-23）【Gitee 原生】
**DoroPet —— 智能桌面伴侣**：集 **Live2D 桌宠 + AI 对话 + 语音交互 + 养成系统 + Galgame 叙事 + 音乐播放器**于一体的桌面应用（Gitee 原生，非 GitHub 镜像）。
- 关键机制/数字：PyQt5 + PyQt-Fluent-Widgets GUI；Live2D 走 **live2d-py + OpenGL v3**；AI 接 OpenAI 兼容多厂商（含 Ollama）；语音 sherpa-onnx + edge-tts；SQLite 存记忆；唤醒词"Hey Doro" + 四大养成属性 + Galgame 多结局。版本 v3.6.8，约 2026-07 活跃。
- 可复用性：**② 参考**。Gitee 侧少见的功能完整 Live2D AI 桌宠，Apache-2.0 友好；⚠️ ★7 偏小、Gitee 生态、且 README 自述 MIT 与仓库 LICENSE 文件（Apache-2.0）不一致，以 LICENSE 文件 Apache-2.0 为准。
- 证据：`gitee.com/api/v5/repos/waterfeet/DoroPet_V3` → ★7 / Apache-2.0 / Python / created 2026-02-10 / updated 2026-07-23（取数 2026-10-11，核实方式：Gitee API + 页面）。
- URL：https://gitee.com/waterfeet/DoroPet_V3

### [AI] 11. chyinan/Kokoro-Engine（★156 · MIT · Rust · 2026-09-24）
**跨平台虚拟角色沉浸式交互引擎**（"Cross-platform virtual character immersive interaction engine"，Rust 实现）。
- 可复用性：**② 参考**。Rust + 跨平台 + 虚拟角色交互引擎，定位接近轻量版 VTuber/数字人运行时；MIT、2026-09 活跃。需 README 确认是否直接吃 Live2D .moc3（描述未明示格式）。
- 证据：`gh api repos/chyinan/Kokoro-Engine` → ★156 / MIT / Rust / pushed 2026-09-24（取数 2026-10-11）。
- URL：https://github.com/chyinan/Kokoro-Engine

### [AI] 12. aurel-g/ComfyUI-Live2DViewer（★0 · MIT · JavaScript · 2024-12-21）
**ComfyUI 节点：在 ComfyUI 里查看 Live2D 模型**（把模型放进 `web/vtuber` 目录即可在节点预览）。
- 关键机制：把 Live2D 预览嵌进 ComfyUI 工作流 —— 对应「AI 绘画 → Live2D 流水线」的**最后一环可视化**。
- 可复用性：**② 参考**。ComfyUI 生态里罕见的 Live2D 查看节点，MIT；⚠️ ★0、**仅一次初始提交（2024-12 建仓即停）**，多年未动，做产品前可能要自己续维护。
- 证据：`gh api repos/aurel-g/ComfyUI-Live2DViewer` → ★0 / MIT / JavaScript / created&pushed 2024-12-21（取数 2026-10-11）。
- URL：https://github.com/aurel-g/ComfyUI-Live2DViewer

### [AI] 13. Muapi/flux-live2d-virtual-avatar-quick-creation-live2d-vroid【HuggingFace 模型】
**Flux LoRA：「LIVE2D 万能模型」** —— 训练词含 `live2d, guijiaoxiansheng(骨架先生), separate hand/feet/head, full body`，用于**用 AI 生图快速产出 Live2D 风格虚拟形象**（vroid Base / Flux.1 D）。
- 关键机制/数字：Base model **Flux.1 D**；调用走 **MUAPI 付费 API**（`api.muapi.ai`，需 API Key），非本地权重。
- 可复用性：**③ 不采用（对本机基准）**。属「AI 绘画 → Live2D 风格」上游生成的一环，但**闭源付费 API、非本地、不可离线**；对 16GB + 本地 Ollama 路线无直接用，仅作「AI→Live2D 流水线」生态登记。
- 证据：HuggingFace 模型卡（WebSearch/WebFetch 核实，2026-10-11）；非 GitHub 仓，`gh api` 404。星级/下载量未在模型卡公开取数。
- URL：https://huggingface.co/Muapi/flux-live2d-virtual-avatar-quick-creation-live2d-vroid

---

## 五、边缘登记（一行一条，不进正文）

- `jiang-yuang3310689646/desk-pet`（Gitee · ★0 · MIT · 2026-09-03）—— 佳怡桌宠：Electron + DeepSeek AI 的 Live2D 桌宠（含 `Live2DPet.ts`/`AIClient.ts`/Vite 结构）。★0 刚建，登记待观察。URL https://gitee.com/jiang-yuang3310689646/desk-pet
- `airisu-dev/experiment-rn-live2d`（★0 · MIT · TS · 2026-10-11）—— React Native 跑 Live2D 的实验，MIT。移动端非本机基准，实验性质。URL https://github.com/airisu-dev/experiment-rn-live2d
- `cyanXsterling/Czechia2030-AI-Live2D-Interaction`（★1 · 无许可证 · 2026-10-11）—— "AI + Live2D 人机交互尝试"，当天新建、无 LICENSE。URL https://github.com/cyanXsterling/Czechia2030-AI-Live2D-Interaction
- `cuiyuanlie2020-stack/dsh-pet-think-voice`（★0 · NOASSERTION · JS · 2026-10-11）—— DSH 思考朗读桌宠：把模型 reasoning 念出来（Live2D + Edge TTS），极细分 DSH 插件。URL https://github.com/cuiyuanlie2020-stack/dsh-pet-think-voice
- `zlovantuzu/moc3-uv-editor`（★0 · 无许可证 · HTML · 2026-08-17）—— moc3 UV 编辑器，★0 无 LICENSE。URL https://github.com/zlovantuzu/moc3-uv-editor
- `LeafiDev/Catism-Live2D`（★0 · 无许可证 · HTML · 2026-09-10）—— 把 scratch SVG 转成 Cubism 用 PSD（需 Inkscape），★0 无 LICENSE。URL https://github.com/LeafiDev/Catism-Live2D
- `respectZ/blue-archive-viewer`（★201 · 无许可证 · Rust · 2026-07-21）—— Blue Archive 资源查看器（Rust），★201 但不确证渲染 Live2D、无 LICENSE，故不进正文。URL https://github.com/respectZ/blue-archive-viewer

### 负结论（一律写「本轮未命中/未核实」，不写「不存在」）
1. **正向「PSD→自动绑定→moc3」新仓库**：本轮 `gh search` + 去重后**未命中**任何未收录的新仓（r37 的 `tsunehimatoi/psd2live`、已卡的 `HKUDS/CLI-Anything`、`j621111/live2d-automation` 仍为唯一来源）。
2. **纯 Rust moc3 运行时新仓**：`MahouTechnologies/moc3-rs`、`SakuraMotion/PurismCore`、`rydanee/live2drust` 等均在 index/r37 已卡，本轮**无新增**。
3. **404 假阴性（本机代理对未缓存路径可能 404，不代表不存在）**：`go-xiaoyu/Live2D`、`SDFA-BOOP/PetForge-...`（超长名含点）、`Muapi/flux-live2d-...`（HF 非 GitHub）。**绝不据此写「死链/不存在」**；HF 模型已用 WebSearch 核实存在。
4. **Gitee 镜像剔除**：`boomer001/BANDORI-PET-REV`、`RexHuang936/Open-LLM-VTuber` 分别是 GitHub `HELPMEEADICE/BANDORI-PET-REV` 与 `Open-LLM-VTuber/Open-LLM-VTuber`（★14041，r37 已卡）的 Gitee 镜像，不重复收。

---

## 六、去重报告

**本路候选总数**：GitHub 扫描 ~124 不重复仓库 + Gitee 5 条 + HF 若干 → 经 `grep -rF` 比对四份基线 + r37 清单，最终 **KEEP 26 个**候选（全部 `grep` 命中 0），其中 24 条进正文、2 条进边缘。

**剔除数**：约 **98+** 条（含已卡/已 r37 收/镜像/破解/素材库/404/非 Live2D 核心）。

**剔除清单（owner/repo + 原因）：**

*A. index.html / r37 已收，命中即弃（节选代表性）：*
- `Eikanya/Live2d-model`、`Voine/ChatWaifu_Mobile`、`imuncle/live2d`、`xiazeyu/live2d-widget.js`、`xiazeyu/live2d-widget-models`、`fghrsh/live2d_demo`、`fghrsh/live2d_api`、`JoeyBling/hexo-theme-yilia-plus`、`Navi-Studio/Virtual-Human-for-Chatting`、`xb2016/poster-girl-l2d-2233`、`mmmmmm44/VTuber-Python-Unity`、`vignetteapp/vignette`、`huihut/Facemoji`、`yeemachine/kalidoface-2d`、`summerscar/live2dDemo`、`52cik/bilibili-haruna` 等 —— 这类老牌/高星 Live2D 仓库在 r37 或 index 已卡（index 为 r37 合并前快照，故 `Eikanya`/`Voine` 等在 index grep 为 0，但 r37 已收，视同已覆盖）。
- r37 已收 32 条（kongweiguang/xiaoya、Rosa134/daidai-live2d-pet、liwenka1/bongo-cat-next、NekoHome-Studio/mea-pet-public、Ludentes/py-moc3、tsunehimatoi/psd2live、Open-LLM-VTuber 等）全部剔除。
- 已知已卡（r37 去重报告列名）：`zeikar/iki`、`moeru-ai/airi`、`RevStudio/Rev2D`、`AyagamiDev/ayagami`、`Eatgrapes/Mocari`、`HKUDS/CLI-Anything`、`j621111/live2d-automation`、`hacxy/l2d-widget`、`MizunagiKB/gd_cubism`、`Perfare/UnityLive2DExtractor`、`EasyLive2D/live2d-py`、`DasterProkio/awesome-ai-companion`、`waifuai/waifu-companion`、`morettt/my-neuro`、`elevenyellow/handcrafted-persona-engine`、`Playa-Cyrene/Cyrene-Agent` 等。

*B. moc3/cubism 搜索命中但已卡（index/r37）：*`renderkit`、`moc3-rs`、`SakuraMotion/PurismCore`、`Wzhang3912/image2live2d`、`fifteen42/live2d-from-art`、`jianchengwang/live2d_models`、`moc3-json-viewer`、`live2drust`、`pyqt-live2d-bridge`、`emote-to-cubism`、`ayatsuri_2d`、`whalegirl-pet`、`ZerolanPlayground` —— 均在索引已卡。

*C. 非 Live2D 核心 / 误命中：*`P1kaj1uu/ChattyPlay-Agent`（★949，描述实为视频解析+AI 聚合工具，gh search 误命中，非 Live2D 仓库）、`rotejin/MotionPNGTuber`（PNGTuber，非 Live2D）、`respectZ/blue-archive-viewer`（资源查看器，非确证 Live2D，边缘登记）。

*D. 破解 / 内容政策排除：*`hugujiugan/Live2D_Cubism_5.2.03`（描述"Live2D破解/Live2D_Cubism patch"，破解库，按内容政策不收录）。

*E. 素材库 / 非工具（剔除出正文）：*`4xura/AxuraDesign`（个人设计素材库）、`lilyco-42/lyco-ip`（原创角色 IP 素材库）—— 非可运行项目。

*F. 404 / 无法核实：*`go-xiaoyu/Live2D`（404）、`SDFA-BOOP/PetForge-A-modular-AI-desktop-pet-framework-with-voice-memory-and-Live2D`（404，超长仓名）。

*G. Gitee / 其他平台镜像：*`boomer001/BANDORI-PET-REV`（= HELPMEEADICE/BANDORI-PET-REV 镜像）、`RexHuang936/Open-LLM-VTuber`（= Open-LLM-VTuber 已卡镜像）。

**未撞 429**：`gh api` 全程未触发速率限制（gh 已登录 re0211，额度充足）；Gitee 走 `api/v5` 公开接口亦正常。
