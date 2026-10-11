# 第三十三辑 · GitHub 路 · Live2D 制作专题（滚动去重后）

> 落盘：`_r33/_r33_gh.md`｜调研时间 2026-10-11
> 去重基线：`_r33/_dedupe_gh.txt`（1274 owner/repo）+ `_r33/_dedupe_urls.txt`（1418 URL）+ `index.html`（1301 项）
> 取数方式：**全部 `gh api repos/{o}/{r}` 实取**（stars / license / language / updated_at / pushed_at / created_at / archived），
> 目录结构走 `gh api repos/{o}/{r}/git/trees/HEAD?recursive=1`；**本机 `git clone` 不通，仅 `gh api` 可用**。
> 可复用性基准 = **16GB Windows + 本地 Ollama + 维护静态索引站的个人开发者**。
> 三档：**落地**（今天能装能用）/ **参考**（值得读源码或当模板，不直接当依赖）/ **不采用**（登记备查）。

---

## §0 本辑口径与发现分布

本辑可复用性判定基准不变，且**继续沿用上一辑立的「三问」**（主指标是美术手作网格还是部署用 auto-mesh？与 baseline 是否同协议？眨眼等关键参数在自动分层上成没成？）——凡声称「全自动出可部署模型」的，逐条对三问。

发现分布（正文 **33 条**，编号 1–33）+ 边缘登记 **13 行（含约 20 个仓库）**：

| 方向 | 正文条数 | 编号 | 备注 |
|---|---|---|---|
| 1 替代栈 / 开源渲染器 | 6 | 1–6 | 仍以「封装官方 Core」为主，纯自研解析依旧稀少 |
| 2 模型制作自动化 | 5 | 7–11 | 单图→模型这条线**没有新增可信工具**，新增的是「分层 PSD→绑定」 |
| 3 AI Agent 桌宠 / 虚拟形象 | 11 | 12–22 | 本辑最富矿，且出现「大脑/身体分离」成体系的做法 |
| 4 Cubism Editor 自动化 | 2 | 23–24 | 与上辑 `CubismExternalEditMCP` 同源，Novelty 低 |
| 5 运行时集成 | 5 | 25–29 | OBS / 直播 / VTube Studio 客户端层 |
| 6 AI 开发与使用 | 4 | 30–33 | DSH 插件生态；索引站维护者可直接吃到的部分 |
| 7 边缘登记（表） | 13 行 | — | 研究 / 停更 / 玩具 |

**三条最硬的发现**（详见各节）：
1. `ExpiredPopsicle/SnekStudio` ★418 —— 用 **Godot** 写的开源 VTuber 软件，**生产环境已跑 3 年**，是本辑唯一「非 Electron、非 Unity」的重型直播软件主干。
2. `kiyotakali/Miru` ★175 —— 把「本地优先 + 长期记忆 + 桌宠 + 多端同步」四件事做成**一条自托管产品线**，且 Windows/macOS/Android 全出安装包。
3. `LivXue/dsh-plugin-shop` ★1009 —— DeepSeek Harness 插件市场，**本机环境（DSH）自身生态**里唯一千星级基础设施。

---

## §一 方向一：替代栈 / 开源渲染器（不依赖 Cubism Editor 的实现）

> 本方向本辑的现实结论：**「开源替代」仍分两极**——一极是老实封装官方 `Live2DCubismCore`（拿到的是渲染，不是编辑器），另一极是自研解析 `.moc3`（能跑但生态小）。**没有一条能同时替代 Editor 的绑骨与导出。**

### 1. `Veykril/cubism-rs` ★47 · Apache-2.0 · Rust · 停更
- URL：https://github.com/Veykril/cubism-rs
- 实取：★47｜Apache-2.0｜Rust｜updated 2026-09-09｜**pushed 2020-01-16**｜created 2018-06-15｜archived=False
- 是什么：把 Live2D Cubism **Native Core 包成 Rust crate**，仓库切成 `cubism-core-sys`（FFI）+ `cubism-core`（安全封装）+ `cubism-core-wgpu-renderer` + `cubism-core-piston2d-renderer`，目录 65 项，附 `haru.rs` / `ver4.rs` 示例。
- 可复用性：**参考**。理由：**六年没推过代码**（pushed 2020-01-16），Core 已迭代到 5.x，ABI 大概率对不上；但它是「Rust + wgpu 渲染 Cubism Core」这一套的最小完整参考，读结构有用。
- ⚠️ 注意：`updated_at` 是 2026 说明**还有人在 star**，不代表代码还活着——**别把 updated 当 pushed 用**。

### 2. `jz315/live2d-cubism-core-sys` ★1 · MIT · Rust · 新
- URL：https://github.com/jz315/live2d-cubism-core-sys
- 实取：★1｜MIT｜Rust｜updated 2026-04-05｜pushed 2026-04-04｜created 2026-04-04｜archived=False
- 是什么：到 **Cubism SDK Native Core (v5)** 的**裸 Rust FFI 绑定**（只做 `-sys`，不含安全封装、不含渲染器）。
- 可复用性：**参考**。理由：本辑里唯一明确标注 **v5** 的 Rust Core 绑定，比 `cubism-rs` 的版本更贴当下；但 1★、单人、无渲染层，只能当「自己写 Rust 渲染器」的起点。

### 3. `MahouTechnologies/moc3-rs` ★6 · Apache-2.0 · Rust
- URL：https://github.com/MahouTechnologies/moc3-rs
- 实取：★6｜Apache-2.0｜Rust｜updated 2026-08-15｜pushed 2026-08-15｜created 2023-09-14｜archived=False
- 是什么：**纯 Rust 的 `.moc3` 读取库**（不依赖官方 Core，直接解析二进制）。
- 可复用性：**参考**。理由：与上两条（封装官方 Core）是**相反的路线**——自己解 `.moc3`。这条路才是「绕开 Cubism 授权」的正解方向，但 6★、无渲染器、无 CLI，离可用还远。

### 4. `Heonys/live2d-web` ★2 · MIT · TypeScript · **本方向最值得读**
- URL：https://github.com/Heonys/live2d-web
- 实取：★2｜MIT｜TypeScript｜updated 2026-09-01｜pushed 2026-09-01｜created 2026-07-29｜archived=False｜**目录 670 项**
- 是什么：官方的**非官方 Web 运行时**——「An unofficial Live2D Cubism runtime for JavaScript and React. **Direct WebGL2 rendering without PixiJS**」。自带 **Framework 5-r.5 adapter**，支持 Cubism 3/4/5，含 motions/sequences/fades/weighted idle/expressions/指针交互、**单 canvas 多模型共享 WebGL 上下文**、wLipSync 口型、MediaPipe 面捕（实验）、devtools 面板。
- 目录证据：`apps/integration-lab`（含 e2e / soak 测试帧，`frames/live2d.html`、`pixi.html`、`overlay.html`）、`AGENTS.md`、`CLAUDE.md`、三语 README。
- 可复用性：**参考（强）**。理由：**它正面回答了「不用 Pixi 能不能渲染 Cubism 3/4/5」——能**，而且直接抄了 Framework 5-r.5 适配层；`AGENTS.md`+`CLAUDE.md`+soak 测试说明它是按「给 agent 接手」的方式写的。**不采用为依赖**的原因：2★、发布不足 3 个月、**Core 与模型一律不打包**（需自备 Core 与授权模型）。
- ⚠️ 与既收录的 `guansss/pixi-live2d-display` / `Panzer-Jack/easy-live2d` 的关系：后两者**都要求 PixiJS**，本条是**其替代**而非重复。

### 5. `Moebytes/live2d-renderer` ★19 · MIT · TypeScript
- URL：https://github.com/Moebytes/live2d-renderer
- 实取：★19｜MIT｜TypeScript｜updated 2026-06-14｜**pushed 2025-10-07**｜created 2025-01-25｜archived=False
- 是什么：一个 **Web 端 Live2D 模型渲染器**。
- 可复用性：**参考**。理由：19★ 且架构干净，可作为「轻量 web viewer」模板；但 **pushed 2025-10**，近一年未动，Cubism 5 适配情况未知。

### 6. `shinkuan/Waifuland` ★81 · **无许可证** · C++ · Linux/Wayland
- URL：https://github.com/shinkuan/Waifuland
- 实取：★81｜**NONE（未声明许可）**｜C++｜updated 2026-10-08｜pushed 2026-04-14｜created 2026-04-11｜archived=False｜目录 50 项
- 是什么：**Linux 桌面 Live2D 查看器**，用 `wlr-layer-shell` 把角色渲染成**透明 Wayland 覆盖窗**。目录里是标准 Cubism Native 示例骨架（`LAppLive2DManager.cpp`、`LAppModel.cpp`、`LAppWayland.cpp`、`LAppWaylandRegion.cpp`、`MouseActionManager.cpp`）。
- 可复用性：**参考（本机不采用）**。理由：它是「把官方 Native 示例改成 Wayland 覆盖窗」的完整范例；但①**平台是 Linux/Wayland**，对 16GB Windows 用户无直接价值；②**未声明许可**，不宜进任何发布物。价值在**抄它的窗口穿透 + 区域命中**思路。

---

## §二 方向二：模型制作自动化

> 本方向本辑的硬结论：**「单图 → 可部署模型」这条线本辑零新增可信工具**（上一辑已收录的 `psd2live` ★612 / `Bunraku` ★37 / `image2live2d` 等仍是主干）。
> 真正的新增量在**「分层 PSD → 自动绑定 → 可直接驱动」**这一层，且**全部自建运行时、不产 `.moc3`**——这是绕开 Cubism Core ABI 那道墙的务实选择。

### 7. `lTwTlol/Auto-live2D-beta` ★28 · MIT · HTML/Python · **本方向最推荐实测**
- URL：https://github.com/lTwTlol/Auto-live2D-beta
- 实取：★28｜MIT｜HTML（+Python 桌面壳）｜updated 2026-10-08｜pushed 2026-08-30｜created 2026-08-20｜archived=False｜目录 17 项
- 是什么：**把分层 PSD 拖进浏览器即自动绑定并动起来**（网格切分 / 变形 / 物理全自动），**客户端本地处理、免安装**。基于 `852wa/Anime2.5DRig` 二次开发。桌面版走 WebView2（Win11 预装），支持 **OpenSeeFace**（头/眨眼/口型/虹膜，读 `127.0.0.1:11573` UDP）。
- 关键实现（README 逐条核到）：直接吃 **see-through 输出的 PSD**（`mouth`→`mouth_open` 自动改名）；**缺闭眼/闭口差分时自动生成通用差分**（按锚点缩放、颜色匹配睫毛/口部，仓库自带 `eye_close.psd`/`mouth_close.psd`）；低透明度噪点连通域滤波；**眼/眉/睫毛/闭眼左右自动分离**（按连通域重心）；锚点自动检测；**发丝按轮廓峰值检测（每层≤6 束）**；按图层深度做**伪 3D 转头**（视差+剪切）；发丝双弹簧物理（根硬梢柔）+ 胸晃 + 呼吸。
- 目录证据：`lib/rigger.js`、`lib/genericparts.js`、`lib/ag-psd.min.js`、`main.py`、`osf.py`、`run.bat`、`sample.psd`。
- 可复用性：**落地（浏览器版）/ 参考（桌面版）**。理由：`index.html` 双击即用、无依赖、MIT；**三问里第①问（网格来源）答得坦白——它是自动网格、并明说不是 Cubism/ moc3 导出器**；第③问（眨眼）用「自动生成差分 + 交叉淡入淡出 + 瞳孔模板裁剪」正面接住了。**不采用为生产依赖**：因它驱动的**不是 `.moc3` 而是自家 2.5D 运行时**，跨平台/跨软件不通用。

### 8. `Fenglin-Maple/AutoLive2d` ★19 · Apache-2.0 · TypeScript · 低显存适配
- URL：https://github.com/Fenglin-Maple/AutoLive2d
- 实取：★19｜Apache-2.0｜TypeScript｜updated 2026-10-10｜pushed 2026-07-24｜created 2026-07-24｜archived=False｜**目录 499 项**
- 是什么：**面向二次元分层 PSD 的开源 Live2D 风格编辑器与运行时**（React+TS+WebGL/Canvas + Electron 壳）。**不依赖 Cubism/Inochi2D 格式**，把规范化 PSD 转成可编辑、可面捕、可换材质、可导出成品包的 2D 角色。**仓库内置经「低显存与 Windows 适配」的 see-through 源码**，可从单张图拆 PSD 再自动绑定。
- 核心算法（README）：可模板化**分层网格投影**；PSD 图层保留透明材质并赋予脸/眼珠/嘴/前发/后发/身体/手臂/`obj` 语义；部件生成三角网格可编顶点/形态键/支点/父级；**伪 Z 只参与几何投影、不抢 draw z 的覆盖顺序**；头模代理把顶点投到以双眼中点为中心的前后椭圆壳；头发/衣服/附件用「根固定、末端加权」惯性飘动。
- 目录证据：`docs/screenshot-to-live2d-workflow.md`、`docs/rig-validation-checklist.md`（**固定验收清单**）、`docs/cubism-5.4-alpha1-external-api.zh-CN.md`、`AGENTS.md`、`public/samples/u3..u6`（带 `input.psd` + `attachments.json` 样例）。
- 可复用性：**参考（强）**。理由：**三问里唯一自己写「验收清单」的项目**（`rig-validation-checklist.md` 明确「改算法必须回归」），这份清单本身对任何自动绑骨项目都可复用；「低显存 + Windows 适配 + 内置 see-through」正对本机画像。**不采用为依赖**：19★、单人、**自研运行时非标准格式**、无 release 二进制。

### 9. `goldimpact/Eviler` ★12 · NOASSERTION · Python · 逆向
- URL：https://github.com/goldimpact/Eviler
- 实取：★12｜NOASSERTION（自定义/不明）｜Python｜updated 2026-04-15｜**pushed 2025-03-29**｜created 2025-03-23｜archived=False
- 是什么：**从 `.moc3` 里把 PSD 抠出来**的工具，README 强调「IT IS NOT USING ANY CODE FROM LIVE2D」（不依赖官方代码，纯逆向）。
- 可复用性：**参考（谨慎）**。理由：本辑里唯一「反着来」的工具——别人做图→模型，它做模型→图，**用于 reclaim 已购模型的源分层**；但①pushed 2025-03、②**许可不明**、③涉及逆向授权边界，**仅登记**。

### 10. `kiraio-moe/Revolt2D.Model3` ★1 · **无许可证** · C#
- URL：https://github.com/kiraio-moe/Revolt2D.Model3
- 实取：★1｜NONE｜C#｜updated 2026-01-25｜**pushed 2024-10-11**｜created 2024-10-10｜archived=False
- 是什么：`model3.json`（Live2D 模型设置文件）的**托管 (De)Serializer**。
- 可复用性：**不采用**。理由：功能极窄（只读写 model3.json）、1★、**无许可**、pushed 停在 2024-10。登记价值：说明「model3.json 的 C# 读写」这个生态位已有人填，C# 栈若需要可参考其数据模型定义（同类的 `vtubing/model3` ★0 是 Rust/TS 版）。

### 11. `xiaoxingyuemiao/Live2D-Param` ★2 · **无许可证** · .NET · 仅二进制
- URL：https://github.com/xiaoxingyuemiao/Live2D-Param
- 实取：★2｜NONE｜（WinForms/.NET）｜updated 2026-09-30｜pushed 2026-09-30｜created 2026-09-30｜archived=False｜**目录仅 2 项（LICENSE + README）**
- 是什么：给 **Live2D Cubism Editor 5.4 版**做**辅助建模**的 Windows 小程序，**硬性要求 Editor ≥ 5.4 alpha1**，通过 Releases 分发安装包（`Live2D-Param-v0.0.1-alpha.1-Setup.exe`）。
- 可复用性：**参考**。理由：它是「**直接挂在 Editor 5.4 上的外部辅助工具**」的一个样本，证明 **5.4 的 External API 已经被第三方用起来**（与 §四 的 MCP 呼应）；但**仓库不含源码**（仅 LICENSE+README），**许可未声明**，只能装 release 试用，**不能作为依赖**。

---

## §三 方向三：AI Agent 桌宠 / 虚拟形象（本辑最富矿）

> 本方向出现了一个**成体系的新范式：大脑/身体分离**——桌宠不自带 LLM 人格，而是作为「渲染层 + 传感器」挂在你**已有的 agent 会话**上（`zziying/ai-live2d-body` 把这套讲得最清楚）。这直接命中「维护索引站的个人开发者」的真实用法：**给已有的 ta 装身体，而不是换一个新 AI。**

### 12. `kiyotakali/Miru` ★175 · Apache-2.0 · Python · **本方向最成熟**
- URL：https://github.com/kiyotakali/Miru
- 实取：★175｜Apache-2.0｜Python｜updated 2026-10-09｜pushed 2026-09-23｜created 2026-07-03｜archived=False｜**目录 566 项**
- 是什么：**「真的记得你、且完全跑在你自己的机器上」的 AI 伴侣**——自称 Desktop pet · long-term memory · proactive companionship · **multi-device sync**，后端 self-hosted，模型**任意 OpenAI 兼容**。**三端都出安装包**：`Miru-macOS.dmg` / `Miru-Windows-x64-Setup.exe` / `Miru-Android.apk`。
- 目录证据：`admin_api.py` / `admin_stats.py` / `_memory_demo.html` / `_screen_pipeline.html` / `_page/`（官网+演示视频）/ `.miru-runtime-source-ref`。
- 可复用性：**落地→参考**。理由：**本辑唯一「长期记忆 + 多端同步 + 三平台安装包」齐全的自托管伴侣**，Windows exe 直接可装，是「主干 vs 玩具」的分界线样本；Apache-2.0 干净。**参考为主**：Python 后端 + 566 项目录，二次改造成本不低；「Windows 版」的 Live2D 具体用哪套栈需自行核。

### 13. `qiyueblues-design/zhuomianling`（桌面灵）★27 · MIT · TypeScript · **Windows 落地首选**
- URL：https://github.com/qiyueblues-design/zhuomianling
- 实取：★27｜MIT｜TypeScript｜updated 2026-10-01｜pushed 2026-08-26｜created 2026-07-09｜archived=False｜**目录 573 项**
- 是什么：**开源、可自定义、本地优先的 Live2D 桌宠软件框架**（Electron 43 + React 18 + TS5 + Vite6，**当前主平台 Windows**）。用户导入自己的 Live2D 模型，配置桌宠资料、人设、事件台词、AI 聊天、可选的视觉与语音能力。**明确不内置受版权限制的模型/声音/AI Key**。
- 目录证据：`docs/adr/0001-记忆权威账本.md`、`docs/adr/0002-本地中文记忆检索.md`；`docs/help/features/` 含 memory-book / mood / persona / expression / preset-voice；`config/examples/` 含 `ai.example.json`、`gpt-sovits.example.yaml`、`speech.example.json`、`tts.example.json`。
- 可复用性：**落地**。理由：**MIT + Windows + local-first + 框架化（模型由用户自备）**= 本机画像的正面命中；`ADR 0001/0002` 把「记忆权威账本 / 本地中文记忆检索」写成了架构决策，说明记忆层是想清楚了的；GPT-SoVITS 走**配置文件**接入而非写死。⚠️ 27★、发布 3 个月，**先当框架读、别当稳定产品用**。

### 14. `ochiru520/Mio` ★49 · MIT · Python · **Windows 本地优先 Agent**
- URL：https://github.com/ochiru520/Mio
- 实取：★49｜MIT｜Python｜updated 2026-10-11｜pushed 2026-09-19｜created 2026-08-20｜archived=False
- 是什么：**Windows 本地优先的个人 AI Agent**——对话、记忆、日记、语音、QQ、**Live2D**、屏幕感知一体的桌面 agent。
- 可复用性：**参考**。理由：与 §13 同赛道（Windows 桌面 agent + Live2D + 本地记忆），差异在 Mio 更偏「个人信息管理（日记/QQ）」、桌面灵更偏「可配置桌宠框架」。49★、MIT、月内活跃，可作交叉对照。

### 15. `yuri-os/YuriOS` ★34 · Apache-2.0 · Python · 「你拥有模型/记忆/角色」
- URL：https://github.com/yuri-os/YuriOS
- 实取：★34｜Apache-2.0｜Python｜updated 2026-10-11｜pushed 2026-10-10｜created 2026-07-14｜archived=False
- 是什么：**本地友好的 agentic AI 伴侣运行时**——「always-on brain with **self-editing memory**. You own the model, the memory, and the character.」
- 可复用性：**参考**。理由：本方向里**口径最清楚的一款**（模型/记忆/角色三权归用户），Apache-2.0、日更；「self-editing memory」的具体鲁棒性待验，**别被 slogan 带走**。

### 16. `hhjk21/Firefly-Companion-AI-` ★27 · MIT · Python · 功能面最全的单体
- URL：https://github.com/hhjk21/Firefly-Companion-AI-
- 实取：★27｜MIT｜Python｜updated 2026-10-10｜pushed 2026-08-05｜created 2026-08-04｜archived=False
- 是什么：基于《崩坏：星穹铁道》「流萤」的桌面 Live2D AI 伴侣（Win/macOS/Linux）。卖点是**双窗口解耦 + 鼠标穿透**、流式对话、**本地 ONNX 语义记忆**、双引擎主动关怀、**GPT-SoVITS 原声 TTS**、Agent 任务执行、**MCP 工具链 + Skill 插件体系**，并分「日常模式 / 萨姆战术模式（显示思维链 + CPU 占用）」。
- 可复用性：**参考（工程结构值得抄，素材不可用）**。理由：**双窗口解耦 + 鼠标穿透**是 Live2D 桌宠的通用难点，它把方案写清楚了；Local ONNX 记忆 + GPT-SoVITS 正好对上 16GB + 本地 Ollama 的画像。⚠️ **角色素材版权归米哈游**，README 自述「仅个人学习交流、禁商用」，**绝不可进任何发布物**。

### 17. `ice-only/localai-rag-live2d` ★21 · MIT · Python · 「本地数据不上云」
- URL：https://github.com/ice-only/localai-rag-live2d
- 实取：★21｜MIT｜Python｜updated 2026-08-06｜pushed 2026-07-30｜created 2026-07-30｜archived=False
- 是什么：本地 AI 聊天（localaiAgentWithRAG），**本地数据不上传云端**，可自行导入记忆文件、修改角色形象、记忆对话、**记忆库支持导入或对话后自动记录**。
- 可复用性：**参考**。理由：直接把「本地 RAG + 长期记忆 + Live2D 形象」打包，MIT、体量小、上手快；**若你已有 Ollama，这是本方向上改造成本最低的一份骨架之一**。pushed 2026-07 略旧。

### 18. `goodko/xiaozhi-ios` ★128 · MIT · C++/SwiftUI · 移动端
- URL：https://github.com/goodko/xiaozhi-ios
- 实取：★128｜MIT｜C++（+SwiftUI）｜updated 2026-09-11｜pushed 2026-08-10｜created 2026-08-10｜archived=False
- 是什么：基于 SwiftUI 的「小智」AI 助手 **iOS 客户端**，集成 **Live2D 虚拟形象**、实时语音对话、**MCP 工具调用**与多模态交互（视觉/地图/小红书/抖音/本地音乐）。
- 可复用性：**参考**。理由：本辑**唯一像样的 iOS 端**（128★、MIT），可作「把 Live2D 形象塞进移动 App + 接 MCP」的参考；对 Windows 桌面开发者价值有限，但对「跨端索引站」的移动入口有启发。

### 19. `DCDingCong/desktopbuddy` ★2 · MIT · TypeScript · Windows + Ollama
- URL：https://github.com/DCDingCong/desktopbuddy
- 实取：★2｜MIT｜TypeScript｜updated 2026-09-12｜pushed 2026-06-12｜created 2026-05-12｜archived=False
- 是什么：**Windows 优先的 AI 桌面伴侣宠物**：Live2D + 物理引擎 + **Ollama 支持** + 一键主题生成。
- 可复用性：**参考**。理由：**唯一一条把「Ollama」写进一句话描述**的桌宠，方向完全对画像；但 2★、pushed 2026-06，**当作「一个人用 Ollama 起桌宠」的最小样板**看，别当依赖。

### 20. `zziying/ai-live2d-body` ★46 · **无许可证** · 文档（非代码）· **范式定义**
- URL：https://github.com/zziying/ai-live2d-body
- 实取：★46｜NONE｜（无语言标记）｜updated 2026-10-04｜pushed 2026-09-05｜created 2026-07-06｜archived=False｜**目录仅 2 项（README.md + human-guide.md）**
- 是什么：一篇**架构思路文档**（不是教程也不是代码），核心命题是「**大脑和身体分离**」：市面框架（airi / Open-LLM-VTuber）会给你**一个新的 AI**（人格来自框架自己的 prompt、记忆存框架自己的库）；本篇主张桌宠**没有大脑**，只做三件事——① 显示 ta 的状态（输出端）② 把你的触摸传回 ta 的 session（输入端）③ 给 ta 一套身体 API（主动端）。配套代码版是 `zziying/ai-live2d-body-starter` ★17。
- 可复用性：**参考（作为设计文档）**。理由：**本辑唯一明确回答「为什么不用现成框架」的一份**，正对「已经有 ta 的 agent CLI 用户」；⚠️ **无许可证**、且只有两份 md，**别当作可依赖的项目**；价值在被 downstream 引用当设计纲领。同类的还有 `Ariakage/live2d-agent-kit`（已在库）。

### 21. `ExpiredPopsicle/SnekStudio` ★418 · GPL-3.0 · GDScript · **非 Live2D，但巨型对照**（3D VTuber）
- URL：https://github.com/ExpiredPopsicle/SnekStudio
- 实取：★418｜GPL-3.0｜GDScript｜updated 2026-10-11｜pushed 2026-09-27｜created 2024-09-23｜archived=False｜**目录 730 项**
- 是什么：**用 Godot 4.7.x 写的开源 VTuber 软件**（自称 Super ~~Secret~~ Public Alpha），作者自述「**自 2022 年起就在生产直播里用它**」。仅支持 **VRM 0.x（VRM 1.x 会有严重问题）**，用 MediaPipe 做摄像头面捕，Win/Linux 有二进制 release，跨平台目标（x86/AMD64/ARM）。
- 目录证据：`Core/`（AudioInput / AvatarColliders / CameraBoom…）、`Build/build_inside_docker.bsh`（**Docker 内构建**）、`.github/workflows/{build,nightly,check_update}.yml`（**三平台 CI + 夜构建**）。
- 可复用性：**参考**。理由：**它是「3D 路线」的重型对照**（Live2D 用户常忽略的分支）——如果想走「VRM + 面捕」而非「Live2D 绑骨」，这是本辑唯一「生产跑了 3 年 + 三平台 CI」的存在；Godot 栈比 Electron 轻、无商业授权。**但它不是 Live2D**：只吃 VRM 0.x，与 `.moc3` 不互通。

### 22. `bearman141/ds-whale-pet` ★2 · NOASSERTION · Electron + Cubism 4
- URL：https://github.com/bearman141/ds-whale-pet
- 实取：★2｜NOASSERTION｜JavaScript｜updated 2026-09-27｜pushed 2026-09-27｜created 2026-09-25｜archived=False
- 是什么：**DS 鲸鱼娘 Live2D 桌面宠物**（Electron + Cubism 4），跟着键鼠做反应。
- 可复用性：**不采用（登记）**。理由：与已收录的 `dsh-whale-girl-live2d`、`dsh-pet-live2d` 同属「DSH/DS 主题鲸鱼娘桌宠」家庭，**建仓 2 天、2★、许可不明**，属同题复刻；登记以免下轮重复撞。

---

## §四 方向四：Cubism Editor 自动化

> 本方向本辑**几乎没有新增量**：主干仍是上一辑的 `nana7chi/CubismExternalEditMCP`（★34，Editor 5.4 alpha1 External API 的 MCP）。
> 新增两条都极小，且一条是**空仓库**。**结论：这条线已被上一辑吃满，本辑只做定点补收。**

### 23. `madosuki/live2dManager` ★1 · NOASSERTION · TypeScript
- URL：https://github.com/madosuki/live2dManager
- 实取：★1｜NOASSERTION｜TypeScript｜updated 2026-09-15｜pushed 2026-09-15｜created 2023-10-03｜archived=False｜目录 25 项
- 是什么：**Live2D Cubism SDK for Web 的非官方库**（`live2dManager.ts` / `live2dModel.ts` / `live2dViewer.ts` / `touchmanager.ts` / `lappwavfilehandler.ts`），以 git submodule 引官方 `CubismSdkForWeb`，配 Vite + oxlint/oxfmt + Nix flake。
- 可复用性：**参考**。理由：**它在做的是「上一辑 `easy-live2d` / `pixi-live2d-display` 同类的事——把官方 Web SDK 包一层」**，不是 Editor 自动化；1★ 但工程配置（Nix + lint 全家桶）比一般个人件规范，可读作「如何把 CubismSdkForWeb 当 submodule 管理」的样板。

### 24. `UFOnian/.physics3.json-Editor` ★1 · **无许可证** · HTML
- URL：https://github.com/UFOnian/.physics3.json-Editor
- 实取：★1｜NONE｜HTML｜updated 2026-07-28｜**pushed 2026-03-01**｜created 2025-12-20｜archived=False
- 是什么：**Cubism Editor「Physics」系统的 `.physics3.json` 编辑器**（针对官方的物理设定文件）。
- 可复用性：**不采用（登记）**。理由：解决了「手改 `.physics3.json` 很痛苦」这个真实痛点，但 1★、无许可、pushed 2026-03、纯前端小工具；**登记以免下轮当新发现重复捡**。

---

## §五 方向五：运行时集成（OBS / 直播 / VTube Studio）

### 25. `menglimi/astrbot_plugin_live_stream_companion` ★58 · MIT · Python · **一条链路打通直播**
- URL：https://github.com/menglimi/astrbot_plugin_live_stream_companion
- 实取：★58｜MIT｜Python｜updated 2026-10-11｜pushed 2026-10-11｜created 2026-06-09｜archived=False｜目录 78 项
- 是什么：面向 **AstrBot** 的直播陪伴插件——把**B 站弹幕读取 + LLM 自动回应 + VTube Studio 表情动作 + TTS 嘴型联动 + OBS 字幕层**组织进**同一条直播链路**。目录含自带 `blivedm/`（B 站弹幕库）与 `l2d_mixin.py`（Live2D 演出混入）。
- 可复用性：**参考（落地）**。理由：**本辑「直播集成」里唯一把 B 站弹幕→LLM→VTube Studio→OBS 全链打通且日更的项目**，MIT、Python、58★；`clients/open_live.py` + `l2d_mixin.py` 的拆分方式可直接借。⚠️ 依赖 AstrBot 生态；VTube Studio 需付费买模型。

### 26. `a1928370421/Obs-Live2D-Plugin` ★68 · GPL-2.0 · C++ · **已停更 6 年**
- URL：https://github.com/a1928370421/Obs-Live2D-Plugin
- 实取：★68｜GPL-2.0｜C++｜updated 2026-09-12｜**pushed 2020-06-02**｜created 2020-05-28｜archived=False｜**目录 2148 项**
- 是什么：「把萌萌的看板娘放到 OBS 上」的 **OBS 插件**，**整仓内置 `CubismSdk/Core` 的完整多平台 dll**（android arm64/armeabi-v7a/x86、linux x86_64、UWP、experimental/rpi 的 `libLive2DCubismCore.so`）。
- 可复用性：**不采用（重要警示）**。理由：**`pushed_at = 2020-06-02`，整整 6 年没动过代码**（`updated_at` 2026 只是有人 star）；OBS 早已改版到 OBS 28+/插件 API 大改，**大概率装不上**。**它是本辑最好的「updated ≠ pushed」反面教材**——若只看 updated 会误判为在维护。

### 27. `HanetakaChou/Brioche-Puppet` ★14 · LGPL-3.0 · C++ · 跨平台
- URL：https://github.com/HanetakaChou/Brioche-Puppet
- 实取：★14｜LGPL-3.0｜C++｜updated 2026-09-16｜pushed 2026-07-21｜created 2025-02-06｜archived=False｜目录 79 项
- 是什么：**免费开源的 VTuber 软件**（C++），带三平台 CI 构建（`build-linux` 含 `Android.mk`/`Application.mk`/`Linux.mk`；`build-macos` 含 `.xcodeproj` + AppIcon；Windows workflow）。
- 可复用性：**参考**。理由：**纯 C++ + LGPL-3.0 + 真三平台构建脚本**本方向少见，可作「原生 VTuber 软件工程骨架」参考；14★、无二进制 release，成熟度待验。

### 28. `Agash/VTubeStudio.Client` ★1 · MIT · C# · .NET 10
- URL：https://github.com/Agash/VTubeStudio.Client
- 实取：★1｜MIT｜C#｜updated 2026-10-05｜pushed 2026-10-05｜created 2026-05-20｜archived=False
- 是什么：**VTube Studio WebSocket API 的现代 .NET 10 / C# 14 客户端库**，AOT 友好、System.Text.Json 源生成、全强类型。同作者另有 `Agash/Veadotube.Client`（.NET 客户端）。
- 可复用性：**参考**。理由：若要用 C# 驱动 VTube Studio（发烫/表情/换装），这是**目前唯一标注 .NET 10 + AOT 的强类型客户端**；1★ 但 API 面清楚。⚠️ 1★、发布 5 个月，未在大项目验证。

### 29. `donskyblock/VTUBEStudio-Linux` ★0 · AGPL-3.0 · Rust · 原生 Linux 客户端
- URL：https://github.com/donskyblock/VTUBEStudio-Linux
- 实取：★0｜AGPL-3.0｜Rust｜updated 2026-10-01｜pushed 2026-10-01｜created 2026-10-01｜archived=False
- 是什么：**用 Rust 原生写的 Linux 版 VTube Studio 客户端**（作者注：port 自其旧 git server）。同生态还有 `rikkichy/vts-opendeck`（Rust，OpenDeck 热键/换模）。
- 可复用性：**不采用（登记）**。理由：0★、建仓当日、单人；**但它揭示了一个需求**——Linux 上 VTube Studio 无原生客户端，正被 Rust 补位。登记以免下轮重复。

---

## §六 方向六：AI 开发与使用（索引站维护者 + 16GB Windows + Ollama 能吃到什么）

> 本方向口径：**只收「维护一个 2.3 MB 静态索引站的个人开发者」真能用上的**，不收泛 agent 论文/清单。
> 因本机运行在 **DeepSeek Harness (DSH)** 上，DSH 插件生态被单独列为可直接吃的部分。

### 30. `LivXue/dsh-plugin-shop` ★1009 · Apache-2.0 · TypeScript · **本机生态基础设施**
- URL：https://github.com/LivXue/dsh-plugin-shop
- 实取：★1009｜Apache-2.0｜TypeScript｜updated 2026-10-11｜pushed 2026-10-11｜created 2026-08-25｜archived=False
- 是什么：**DSH（DeepSeek Harness）插件市场**——自称「最全面的 DSH 插件市场，每日刷新、全网取材、发布前审核」。
- 可复用性：**落地**。理由：**本机就跑在 DSH 上，这是唯一千星级、且直接决定「你能装到什么插件」的入口**；Apache-2.0、日更。**第一次把 `dsh plugin add …` 的发现层做成了基础设施**。⚠️ 第三方市场，「发布前审核」为由作者自述，安装仍应逐条看源码。

### 31. `liguobao/ds-harness-remote` ★309 · **无许可证** · TypeScript
- URL：https://github.com/liguobao/ds-harness-remote
- 实取：★309｜NONE（未声明）｜TypeScript｜updated 2026-10-11｜pushed 2026-10-11｜created 2026-08-14｜archived=False
- 是什么：基于 DSH 插件机制的**多端远程访问方案**——通过**端到端加密、P2P 优先**的网络，从 PC / Android / Web 随时访问并操作远程 Harness 与 CodeX。
- 可复用性：**参考**。理由：**「在手机上操控本机 DSH」这件事对本机维护索引站有实际价值**（出门也能让 agent 改 index.html）；309★、日更。⚠️ **未声明许可 + 涉及远程访问/加密网络，安全面大**，仅作思路参考。

### 32. `petabridge/memorizer` ★215 · MIT · C# · Agent 记忆 MCP
- URL：https://github.com/petabridge/memorizer
- 实取：★215｜MIT｜C#｜updated 2026-10-09｜pushed 2026-10-09｜created 2025-07-15｜archived=False
- 是什么：**向量检索驱动的 agent 记忆 MCP server**（.NET/Akka 系）。
- 可复用性：**参考（不采用）**。理由：本方向里**质量与活跃度最靠前**的记忆 MCP，MIT、日更；但**栈是 .NET**，与「Windows + Ollama + Python/TS 索引站」不同路，且向量检索会引入额外模型/依赖。**登记为主**：说明「agent 记忆」已从概念进入工程化竞品期（同题还有 `mtrnix/metronix-memory` ★107、`ipiton/agent-memory-mcp` ★42 等）。

### 33. `kennethlaw325/awesome-llm-knowledge-systems` ★93 · MIT · 清单
- URL：https://github.com/kennethlaw325/awesome-llm-knowledge-systems
- 实取：★93｜MIT｜HTML｜updated 2026-10-05｜pushed 2026-09-15｜created 2026-04-06｜archived=False
- 是什么：一份「2026 年 LLM 知识工程」**地图式清单**，把 RAG、Context Engineering、Harness Engineering、Skill Systems、Agent Memory、MCP、Progressive Disclosure 串成一张统一图谱。
- 可复用性：**参考**。理由：**这是给「选题」用的，不是给「用」用的**——可直接当作下几轮的方向盘（避免再零散搜）。⚠️ 是清单不是代码。

> 方向六另有两枚**极小但直接相关 DSH 插件**（登记，未单列正文）：`P02-1010751281/dsh-project-context` ★1 · MIT（项目级持久化上下文：session 归档+机械索引、记忆整合 CONTEXT.md/MEMORY.md、低频 skill 自学习、自动 handoff）、`lcy0121/dsh-plugin-compat-check` ★0 · MIT（装 DSH 插件前先判断「在你这一版上到底能不能用」）。**后者正对「第三方插件踩版本坑」这个痛点**，但 0★、建仓 2026-10-06。

---

## §七 方向七：边缘登记（有意思但谈不上实用）

| 项目 | 实取数字 | 是什么 / 为何只登记 |
|---|---|---|
| `wan-h/awesome-digital-human-live2d` | ★2425 · MIT · TypeScript · U 2026-10-10 · **P 2026-05-18** · C 2024-05-15 | 名字像清单、**实为一整套数字人应用**：Docker 快速部署、**低于 2核2G** 即可跑、接 Dify/FastGPT/Coze、ASR/LLM/TTS/Agent 模块化、**Live2D 模型+控制方式扩展**、PC+移动 web。**为何只登记**：pushed 2026-05 已 5 个月未动，且「低配数字人」这条路与「Live2D 绑骨」主线不同；**但 2425★ 体量极大，建议下轮正面评一次**（本辑时间不够，不假装已核实） |
| `LitStronger/live2d-moc3` | ★92 · **无许可** · JavaScript · U 2026-10-08 · **P 2021-02-05** · C 2020-08-20 | 加载新版 moc3 游戏角色模型（碧蓝航线），带用例。**pushed 停在 2021**、许可不明 → 玩具级 |
| `HCLonely/Live2dV3` | ★61 · MIT · JavaScript · U 2026-08-29 · **P 2020-04-18** · **archived=True** | 网页加 moc3 的看板娘。**官方已 archive**，仅作历史参考 |
| `QiE2035/moc3-reader-re` | ★17 · **无许可** · Java · U 2026-06-07 · **P 2022-07-21** · **archived=True** | 逆向 moc3 的读取器。已 archive、许可不明 → 纯研究 |
| `Chaoray/AzurLane-Live2D-Viewer` | ★28 · **无许可** · JavaScript · U 2026-09-22 · **P 2024-05-26** | 碧蓝航线 Live2D 模型查看器。pushed 2024、许可不明 |
| `adrianiainlam/mouse-tracker-for-cubism` | ★15 · MIT · C++ · U 2026-04-02 · P 2026-04-02 · C 2020-10-02 | 用鼠标位置 + 麦克风生成 Cubism 参数（与已收录的 `facial-landmarks-for-cubism` ★75 同作者同系列） |
| `TianMengLucky/BongoCat-X` | ★9 · AGPL-3.0 · C · U 2026-10-11 · P 2026-10-10 · C 2026-09-19 | C × SDL3 × OpenGL 跨平台桌宠（**BongoCat 的 X 分支 fork**）。**轻量、非 Live2D**，但「C+SDL3 做桌宠」是低占用路线样本 |
| `hoardodile/plugin-2d-skel` | ★1 · MIT · TypeScript · U 2026-09-29 · P 2026-09-20 · C 2026-08-31 | **Live2DViewerEX 数据格式**支持：Live2D/Spine/DragonBones 动画查看器。小但生态位独特 |
| `niizam/obs-spine-player` | ★1 · **无许可** · JavaScript · U 2026-10-07 · P 2026-10-07 · C 2026-09-01 | OBS 插件：播放 Spine 3.7/4.0/4.1，带**音频驱动 yap 模式**、表情与热键。**Spine 路线**（非 Live2D），1★ |
| `darkin-blade/live2d_SDK_WebGL` | ★1 · **无许可** · JavaScript · U 2023-10-23 · **P 2019-09-25** · C 2019-06-12 | 官方 SDK WebGL 改版，支持无限个 live2d canvas。**早已停更** |
| `B612plant/dsh-plugin-live2d-stage` ★1 / `MQGXG/dsh-plugin-live2d-pet` ★0 / `fromatlantis/dsh-plugin-live2d` ★0 | 均为 JavaScript；U/P 2026-08~10 | **DSH 的 Live2D 桌宠插件三连**（另有已收录的 `dsh-pet-live2d` ★38、`dsh-whale-girl-live2d` ★28）。**同题供给已饱和**，登记以免下轮重复收 |
| `wxyz404/sprout-pngtuber` ★0 · **无许可** · TypeScript · U/P 2026-10-10 · C 2026-10-04 | 及 `zwh988/pngtuber-studio` ★0 · **无许可** · Python · U/P 2026-10-10 · C 2026-10-10 | 离线 Windows PNGtuber studio：摄像头面捕 + 分层 PNG rig + 透明 OBS 输出。**PNGtuber 是 Live2D 的穷亲戚**，单独成簇（本辑不展开） |
| `misaalya/kana-hermes` ★2 · MIT · TS · P 2026-09-26｜`celestial-sora/vivian` ★1 · **无许可** · TS · P 2026-10-07｜`kongweiguang/xiaoya` ★1 · MIT · TS · P 2026-10-09｜`haixu8396-png/aileen-desktop` ★5 · NOASSERTION · JS · P 2026-10-06｜`efficiencyx/JunOS` ★5 · Apache-2.0 · JS · P 2026-10-09｜`yuanqubeiding/tamias` ★2 · Apache-2.0 · Py · P 2026-09-18｜`agentworks-lab/MoeAgent` ★1 · Apache-2.0 · TS · P 2026-09-22｜`Sunname123456/Firefly-DeskPetPanel` ★1 · GPL-3.0 · Py · P 2026-09-03｜`lrplrplrp/dsh-live2d` ★2 · MIT · JS · P 2026-09-12｜`aalizelau/Digital-human-live2d` ★13 · **无许可** · TS · **P 2025-03-02** | 详见汇总 | **十款「Live2D + agent 桌宠」小件**（0–13★，2026-08 后建仓）。共同点：都是单人、单体、快建快更；**同质化严重**。本辑只登记不逐条展开——下轮若再搜此方向，**先用「已在 `_r33_gh.md` §七」过滤** |

---

## §八 去重报告（本辑剔除清单）

**方法**：对每个候选执行 `grep -iF "owner/repo" _r33/_dedupe_gh.txt` 与 `grep -iF "owner/repo" index.html`，**两者任一命中即弃**；并对六种重复形态（换名 / 旧闻换日期 / 转载 / ID 新≠内容新 / SEO 镜像站 / 同日双发账号农场）单独标注。

**A. 命中去重基线（`_dedupe_gh.txt` 或 `index.html`），本辑剔除**：

| 剔除项 | 命中位置 | 备注 |
|---|---|---|
| `umamoorg/umamo` ★151 · GPL-3.0 · Kotlin | GH + IDX（index 节点 [1207]） | 已收录（上一轮），非本辑新增 |
| `tsunehimatoi/psd2live` ★612 · GPL-3.0 | GH + IDX（[1168]） | 已收录 |
| `SakuraMotion/PurismCore` ★40 · MIT · C | GH + IDX（[1201]） | 已收录 |
| `Arcelyth/live-ascii` ★234 · MIT · Rust | GH + IDX（[1224]） | 已收录 |
| `Yoru-KenomoVT/ayatsuri_2d` ★2 · GPL-3.0 · Rust | GH + IDX（[1286]） | 已收录 |
| `KurisuMakise004/renderkit` ★29 | GH + IDX（[1242]） | 已收录 |
| `SparcAI-Inc/Bunraku` ★37 | GH + IDX（[1248]） | 已收录 |
| `nanlingyin/soullink-emotion-sdk` ★144 · Apache-2.0 | GH + IDX（[1223]） | 已收录 |
| `nana7chi/CubismExternalEditMCP` ★34 · MIT | GH + IDX（[1175]） | 已收录（本辑 §四 口径基线） |
| `OpenL2D/moc3ingbird` ★98 | GH + IDX | 已收录 |
| `aethiopicuschan/cubism-go` ★32 | GH + IDX | 已收录 |
| `RevStudio/Rev2D` ★7 | GH + IDX | 已收录 |
| `Hera-Berg/open-avatar-creator` ★0 | GH + IDX | 已收录（建仓前即被登记） |
| `lvhaojie456/image-to-live2d` ★2 | IDX | 已收录 |
| `A8Chann/dsh-pet-live2d` ★38 | IDX | 已收录 |
| `flowingduskpro/jpg-to-live2d-workflow` ★4 | IDX | 已收录 |
| `joyparkray/agent-avatar` ★1 | IDX | 已收录 |

**B. 六种重复形态的现场样本（本辑实撞）**：
1. **`obsidian-knowledge-mcp` 命名农场**：`GooDongWoo / AndersNS / Utkarshsharma30 / nekottyo / SooonChang / WilsonWukz / TheOutcastVirus` **七个不同 owner 用完全同名仓库**——典型 **SEO 镜像站/账号农场**形态。**本辑全部不收**。
2. **`pngtubermaker/*`**：同一「组织」下 `pngtuber-converter`、`pngtuber-obs-player` 等**同日批量发布**、0★、同模板描述 → **同日双发账号农场**形态，不收。
3. **`windblown-directionalantenna594/*`**：同名描述出现在 `2d-vtuber-vtube-studio-setup-toolkit` 与 `<user>.github.io` 两仓 → **镜像站**形态，不收。
4. **ID 新 ≠ 内容新**：§五.26 的 `a1928370421/Obs-Live2D-Plugin`（`updated_at` 2026-09 但 `pushed_at` **2020-06**）、§七的 `LitStronger/live2d-moc3`（updated 2026-10 但 pushed **2021-02**）——**两例都靠 `pushed_at` 识破**。
5. **Fork / 旧 owner 名**：`TianMengLucky/BongoCat-X` 自述 fork 自 `vladelaina/BongoCat`（X 分支），已在 §七 标注为 fork；`DennyWanye/simple_harness` 自述 fork 自 `DeskPet`。对全部候选按 `owner/repo` 全名与旧名分别 `grep -iF`，**除上述两条自述 fork 外无其他命中**。

**C. 已剔除但需留意的「擦边」项**：`wan-h/awesome-digital-human-live2d`（★2425）**不在**去重基线内、本辑新收，但**未及深评**，已列入 §七 并建议下轮正面评。

---

## §九 负结论（哪个方向零命中，下轮别再单独投入）

1. **「单图/提示词 → 可部署 `.moc3`」本辑零新增可信工具**。搜到的 `image-to-live2d`、`jpg-to-live2d-workflow`、`Auto-live2D-beta`、`AutoLive2d` **全部是「到自研运行时」或「到 PSD 绑定」为止，无一产出可部署 `.moc3`**。→ **下轮别再单独搜「one image to live2d / moc3 export」。**
2. **「纯自研 `.moc3` 解析器」仍然稀缺且玩具化**：命中仅 `MahouTechnologies/moc3-rs`(★6)、`vtubing/moc3`(★10)、`jz315/live2d-cubism-core-sys`(★1)，且后两者本质是「读」不是「渲」。→ **这条路要么早已被 `ayagami`(上辑) 占住，要么无人做，别指望新仓。**
3. **「Cubism Editor 自动化」本辑近零新增**：除 `madosuki/live2dManager`(★1，其实是 Web SDK 封装) 与 `.physics3.json-Editor`(★1) 外无物；`nana7chi/CubismEditorClientJS` **是空仓库**（`gh api .../git/trees` 返回 409 "Git Repository is empty"）。→ **这条线上一辑已被 `CubismExternalEditMCP` ★34 吃满。**
4. **「VTube Studio 官方/半官方插件」零命中**：搜 `vtuber studio plugin` 仅得 0★ 孤件；官方 `DenchiSoft/VTubeStudio`(★1313) 是 **API 文档仓**不是插件市场。→ **VTS 插件生态在 GitHub 上基本是空白，别再投。**
5. **「音频驱动口型 / 独立 lip-sync」** 延续上辑：本辑仍**无独立命中**（都是整包在桌宠里，如 `menglimi` 的 `l2d_mixin.py`）。→ **维持上辑负结论。**

---

## §十 备注 / 下轮待办

1. **`updated_at ≠ pushed_at` 必须成文规则**：本辑至少两处（§五.26、§七）靠 `pushed_at` 才识破「假活」。**建议索引卡固定同时打印两个日期**。
2. **DSH 插件生态已成形**（`dsh-plugin-shop` ★1009 / `ds-harness-remote` ★309 / `dsh-plugin-registry` ★4 …）：这是**本机所跑运行时自身**的生态，下轮可单独一辑，别混在 Live2D 里。
3. **`wan-h/awesome-digital-human-live2d` ★2425 未及深评**——本辑最大的漏网，下轮正面评一次（重点核：它到底是不是「Dify 生态壳 + Live2D 前端」）。
4. **`Fenglin-Maple/AutoLive2d` 的 `rig-validation-checklist.md` 可直接抄**成索引站自己的「自动绑骨验收清单」。
5. 本辑**未做**：`git clone` 实测（本机不通）、runtime 跑通验证、许可证逐文件核对。**所有可复用性判定基于 README + 目录树 + gh api 元数据，不含运行实测**——已在各条写明。
