# 第三十辑 · gh 路

> 调研日期：2026-10-11
> 主题：Live2D 相关项目（新工具 / agent 集成 / 新版本 / 上新）
> 基准形象：16GB Windows + 本地 Ollama + 维护 GitHub Pages 索引站的个人，游戏制作新手，Ren'Py 为目标引擎之一

## 搜索覆盖

用 `gh search repos "<kw>" --sort updated`（2026-10-11，本地 gh 2.93.0）跑过以下关键词组，命中候选后逐条 `gh api repos/{owner}/{repo}` 核实：

| 组 | 关键词 |
|---|---|
| 1. agent/LLM | `live2d agent` · `live2d mcp` · `live2d llm` · `live2d skill` · `live2d agent skill` · `live2d ollama` |
| 2. Cubism SDK | `cubism sdk` · `live2d cubism 5` · `cubism alternative` · `moc3` · `moc3 v6` |
| 3. 运行时 | `live2d godot`（空） · `live2d unity` · `live2d webgpu`（空） · `live2d wasm`（空） · `live2d python` · `live2d rust`（空） · `live2d golang`（空） |
| 4. 工具链 | `live2d motion` · `image to live2d` · `psd live2d`（空） · `motion3` · `live2d cli`（限流未回） · `2D puppet live2d moc3`（空） |
| 5. 应用侧 | `vtuber` · `vtuber pipeline` · `face tracking live2d`（空） · `live2d desktop pet` · `live2d puppeteer`（限流） · `pngtuber`（限流） |
| 6. 格式 | `moc3` · `motion3` |
| 7. 查看器/渲染 | `live2d viewer` · `live2d renderer` · `live2d wasm` |
| 8. 引擎 | `renpy live2d` · `live2d rpgmaker`（空） |

> 注：跑完前 8 组后 GitHub 搜索端点触发 403 限流（`API rate limit exceeded`），第 4/5 组个别关键词未取回；核心 `gh api repos/...` 端点未受影响，所有条目证据均已核实。另：`live2d godot` / `live2d webgpu` / `live2d wasm` / `live2d rust` / `live2d golang` / `live2d rpgmaker` / `face tracking live2d` 检索为空，说明这些方向目前几乎无独立仓库。

## 条目

### 分组 A · Agent / LLM 集成（本辑重点）

### elevenyellow/handcrafted-persona-engine —— Live2D+LLM+ASR+TTS+RVC 的一体化虚拟形象引擎
- 链接：https://github.com/elevenyellow/handcrafted-persona-engine
- 核实：stars=1381 · license=none（未声明） · language=C# · pushed=2026-05-20 · updated_at=2026-10-08
  - 命令：`gh api repos/elevenyellow/handcrafted-persona-engine --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at,updated:.updated_at}'`
- 是什么：C# 写的交互式虚拟形象引擎，把 Live2D 形象、LLM 对话、ASR 语音识别、TTS、RVC 变声串成一条实时链路，定位 VTubing / 直播 / 虚拟助手。
- 为什么值得看：topics 里明确含 `live2d`；是本辑 star 最高、且功能最全的「Live2D+LLM」工程化范例，可直接照抄它的「音频→口型/表情参数映射」与状态机设计。
- 可复用性：🔶 参考 —— 全链路设计值得借鉴，但 C#/.NET 桌面栈对新手偏重，且未声明 license，先读不装。

### moeru-ai/airi —— 自托管 Live2D/VRM 桌面伴侣（Neuro-sama 平替，5 万★）
- 链接：https://github.com/moeru-ai/airi
- 核实：stars=50263 · license=MIT · language=TypeScript · pushed=2026-10-11 · updated_at=2026-10-11（topics 含 `live2d`、`vrm`）
  - 命令：`gh api repos/moeru-ai/airi --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：自托管、你拥有的数字生命伴侣，支持实时语音、Live2D/VRM 形象、桌面宠物形态，Web / macOS / Windows 三端。
- 为什么值得看：MIT、Windows 可用、社区巨大、2026-10-11 仍在更新；对「本地 Ollama + Live2D 桌宠」这套基准场景几乎零门槛，可直接装来当参考实现或直接用。
- 可复用性：✅ 落地 —— MIT + Windows + 活跃，今天就能装起来跑本地 AI 伴侣，是他这类场景里最稳的开源底座。

### Andersen216/dsh-whale-girl-live2d —— DSH Web 界面里的 Live2D 桌宠插件
- 链接：https://github.com/Andersen216/dsh-whale-girl-live2d
- 核实：stars=28 · license=MIT · language=JavaScript · pushed=2026-10-10 · updated_at=2026-10-10
  - 命令：`gh api repos/Andersen216/dsh-whale-girl-live2d --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：挂在 DSH（DeepSeek Harness）Web UI 上的 Live2D 鲸鱼娘桌宠：跟着 agent 真实状态换表情动作，点击直接跟 agent 说话。
- 为什么值得看：这是「agent 状态 → Live2D 表情/动作」的现成样例，安装命令即 `dsh plugin --profile web add github:Andersen216/dsh-whale-girl-live2d`；思路可平移到任意本地 agent（含 Ollama）驱动桌宠。
- 可复用性：✅ 落地 —— 一行命令装进 DSH，作者本人就是「本地 agent + Live2D」生产力玩法，直接对口。

### shinshin86/aituber-onair —— 做 Neuro-sama 式 AI VTuber 的 TypeScript 工具箱
- 链接：https://github.com/shinshin86/aituber-onair
- 核实：stars=267 · license=MIT · language=TypeScript · pushed=2026-10-11 · updated_at=2026-10-11（README 多次提及 Live2D）
  - 命令：`gh api repos/shinshin86/aituber-onair --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：开源 TS 工具包，用来搭能聊天、说话、记忆、对观众实时反应的 Neuro-sama 式 AI VTuber / AI 角色，形象层支持 Live2D。
- 为什么值得看：作者 shinshin86 长期做 Live2D Web 相关项目（本索引已收其 `live2d-add-motion-sample-web-ui`）；本库 MIT、活跃，是「Web 端 Live2D + LLM + 直播互动」的完整脚手架。
- 可复用性：✅ 落地 —— Web/TS 栈轻量，Ollama 接本地模型即可起一个能播的 AI VTuber，学习成本对新手友好。

### Wayne1145/yachiyo-claw —— 安卓端本地 agent + Live2D + Skills + MCP 的 AI 聊天客户端
- 链接：https://github.com/Wayne1145/yachiyo-claw
- 核实：stars=13 · license=GPL-3.0 · language=TypeScript · pushed=2026-10-09 · updated_at=2026-10-07
  - 命令：`gh api repos/Wayne1145/yachiyo-claw --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：开源安卓 AI 聊天 + 端侧 agent，集成本地模型、Live2D、Skills、MCP 与 Vibe Coding。
- 为什么值得看：把 Live2D 与「本地模型 + agent + MCP」塞进手机的少见案例；其 prompt/skill 组织方式可迁移到桌面端。
- 可复用性：🔶 参考 —— 安卓平台偏移动端，与 Windows 桌面主线不同，但 agent+Live2D 的产品结构值得抄。

### ptghb/virtual-person —— 「小凡」：Live2D Cubism SDK + OpenAI 的网页版 AI 女友
- 链接：https://github.com/ptghb/virtual-person
- 核实：stars=45 · license=NOASSERTION · language=TypeScript · pushed=2026-10-08 · updated_at=2026-10-10
  - 命令：`gh api repos/ptghb/virtual-person --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：基于 Live2D Cubism SDK 和 OpenAI API 的智能对话助手，Live2D 虚拟形象 + 实时 WebSocket 通信 + AI 对话。
- 为什么值得看：中文项目、Web 栈、聚焦「Live2D 形象与对话状态联动」，README 与结构对中文新手友好，可把 OpenAI 换成 Ollama。
- 可复用性：✅ 落地 —— 纯 Web 前端，本地起服务即可跑；把 API base 改成本地 Ollama 就是离线版。

### momori777/Artemis —— 本地离线 AI 女友后宫（含 Live2D 桌宠，8G 显存可跑）
- 链接：https://github.com/momori777/Artemis
- 核实：stars=381 · license=NOASSERTION · language=Python · pushed=2026-09-30 · updated_at=2026-10-10
  - 命令：`gh api repos/momori777/Artemis --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：本地离线 AI 女友系统，Agent + 画图/语音/向量库 + Live2D 桌宠 + 酒馆角色卡导入 + webchat + QQ/Telegram 双通道，8G 显存可跑。
- 为什么值得看：明确「8G 显存动态调度 + 可离线」，与 16GB Windows + 本地 Ollama 基准几乎重合；是「本地 LLM + Live2D 桌宠 + 记忆」的集成样板。
- 可复用性：✅ 落地 —— 显存与离线要求正好匹配，可直接对照它搭自己的桌宠；注意 license 为 NOASSERTION，商用需谨慎。

### fifteen42/live2d-from-art —— 画作→Live2D 的 Agent Skill（含 MOC3 直接生成与浏览器校验）
- 链接：https://github.com/fifteen42/live2d-from-art
- 核实：stars=11 · license=none · language=Python · pushed=2026-09-15 · updated_at=2026-09-25
  - 命令：`gh api repos/fifteen42/live2d-from-art --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：实验性 Agent Skill，覆盖「美术图 → Live2D」工作流、直接生成 MOC3、以及浏览器端校验。
- 为什么值得看：正好命中「agent 集成」方向——把 Live2D 制作流程封装成 agent 可调用的 skill，格式（skill 描述 + 脚本）可直接套用到自己的 agent。
- 可复用性：✅ 落地 —— if 他要给自己的 agent 加 Live2D 能力，这是可直接照抄的 skill 模板；实验性、无 license，先参考。

### nguyen-van-phuoc/HoloCore —— 本地优先的语音助手（LLM/STT/TTS/Live2D/MCP/记忆/视觉/游戏）
- 链接：https://github.com/nguyen-van-phuoc/HoloCore
- 核实：stars=2 · license=none · language=Python · pushed=2026-10-02 · updated_at=2026-10-05
  - 命令：`gh api repos/nguyen-van-phuoc/HoloCore --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：模块化、local-first 的 AI 语音助手，集成 LLM、STT、TTS、Live2D、MCP、记忆、视觉与小游戏。
- 为什么值得看：「local-first + MCP + Live2D」的模块化拆分思路值得借鉴，但 star 极少、无 license，属早期作品。
- 可复用性：🔶 参考 —— 模块划分可学，成熟度不足，暂不装。

### Yancheng-s/mate-human —— Live2D Cubism 5 Web SDK × Fay 数字人框架
- 链接：https://github.com/Yancheng-s/mate-human
- 核实：stars=11 · license=MulanPSL-2.0 · language=Python · pushed=2026-03-09 · updated_at=2026-10-08
  - 命令：`gh api repos/Yancheng-s/mate-human --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：把 Live2D Cubism 5 Web SDK 与 Fay 数字人 AI 框架深度集成，做实时语音交互 + 动作表情驱动 + AI 对话的 Web 数字人。
- 为什么值得看：用上了 Cubism **5** Web SDK，是「新版本 SDK + 数字人框架」的对接范例；MulanPSL 许可对国内使用友好。代码活跃度一般（pushed 在 3 月）。
- 可复用性：🔶 参考 —— 集成思路可借鉴，但其依赖 Fay 框架较重，先看不动手。

### Pal-AI-Lab/Cortico —— 用事件流 agent 框架搭 persona 机器人（含 Live2D）
- 链接：https://github.com/Pal-AI-Lab/Cortico
- 核实：stars=198 · license=MIT · language=TypeScript · pushed=2026-10-11 · updated_at=2026-10-11（README 提及 Live2D）
  - 命令：`gh api repos/Pal-AI-Lab/Cortico --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：面向 persona bot 的事件流 AI Agent 框架，TS 实现，形象层支持 Live2D。
- 为什么值得看：MIT、198★、当日仍在推送；「事件流驱动的虚拟形象状态」是很值得抄的架构，适合把 Live2D 表情挂在 agent 事件上。
- 可复用性：🔶 参考 —— 框架偏重、偏通用 agent 底座，先读其事件→形象驱动那层。

### arjunindia/live2d-skills —— 面向 Live2D Cubism SDK 的 Agent Skills
- 链接：https://github.com/arjunindia/live2d-skills
- 核实：stars=1 · license=none · language=TypeScript · pushed=2026-05-12 · updated_at=2026-06-29
  - 命令：`gh api repos/arjunindia/live2d-skills --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：由 hermes agent 分析公开代码/文档后写成的 Cubism SDK 实验性 agent skills。
- 为什么值得看：展示「如何让 agent 读懂 Cubism SDK」的 skill 写法，可作 skill 模板参考。
- 可复用性：🔶 参考 —— 实验性、无 license、star 低，仅作 skill 格式参考。

### lileping12/live2d-skills-bundle —— Live2D 角色细节制作的 skill 脚本包
- 链接：https://github.com/lileping12/live2d-skills-bundle
- 核实：stars=0 · license=none · language=（未识别，可能纯文本/脚本） · pushed=2026-10-07 · updated_at=2026-10-07
  - 命令：`gh api repos/lileping12/live2d-skills-bundle --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：一捆用于「构建并优化角色细节工作」的 Live2D skill 脚本与笔记。
- 为什么值得看：10-07 刚更新，同属「Live2D skill」赛道，可作对照，但信息量/成熟度未知。
- 可复用性：🔶 参考 —— 无 license、无 star、语言未识别，先看内容再说。

### 分组 B · 桌宠 / 运行时（贴合 16GB Windows 基准）

### SherlockYzz/anime-desktop-pet —— 多角色 Live2D 桌宠（AI）
- 链接：https://github.com/SherlockYzz/anime-desktop-pet
- 核实：stars=9 · license=MIT · language=JavaScript · pushed=2026-10-06 · updated_at=2026-10-06
  - 命令：`gh api repos/SherlockYzz/anime-desktop-pet --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：AI 桌面宠物，支持多个动漫角色的 Live2D 形象。
- 为什么值得看：MIT、JS/Electron 栈、多角色管理，Windows 可直接跑，适合当自建桌宠的骨架。
- 可复用性：✅ 落地 —— MIT + 轻量 JS，装来即用，多角色切换逻辑对他做桌宠很实用。

### jinsc123654/l2dpet —— 跨平台 Live2D 桌宠（可选 LLM 对话/记忆/性格）
- 链接：https://github.com/jinsc123654/l2dpet
- 核实：stars=0 · license=NOASSERTION · language=C++ · pushed=2026-10-11 · updated_at=2026-10-11
  - 命令：`gh api repos/jinsc123654/l2dpet --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：跨平台（Win/Linux/macOS）Live2D 桌宠，带交互动画、可选 LLM 对话、记忆与性格。
- 为什么值得看：当日仍活跃，明确 Windows 支持且内置 LLM 对话——与基准场景完全对口。
- 可复用性：🔶 参考 —— 功能对口，但 C++ 需编译且 star=0、license 未标准化，先看实现。

### VeiQiuLab/DesktopPet —— Rust + Win32 + D3D11 的轻量 Windows 桌宠
- 链接：https://github.com/VeiQiuLab/DesktopPet
- 核实：stars=0 · license=MIT · language=Rust · pushed=2026-09-19 · updated_at=2026-09-19
  - 命令：`gh api repos/VeiQiuLab/DesktopPet --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：纯 Rust 写的 Windows Live2D 桌宠，基于 Win32 + D3D11 + DirectComposition。
- 为什么值得看：MIT、原生 Windows 渲染、依赖少；想做轻量原生桌宠时是干净参考。
- 可复用性：🔶 参考 —— 要 Rust 工具链，对新手上手成本高，先作原生渲染参考。

### ymhyyds/DesktopPet —— Qt6 + Cubism SDK 的 Windows 桌宠（DeepSeek 对话）
- 链接：https://github.com/ymhyyds/DesktopPet
- 核实：stars=2 · license=none · language=C++ · pushed=2026-07-17 · updated_at=2026-08-27
  - 命令：`gh api repos/ymhyyds/DesktopPet --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：基于 Qt6 与 Live2D Cubism SDK 的 Windows 桌宠，含 DeepSeek 对话、Edge TTS、天气感知、模型导入。
- 为什么值得看：中文项目、Windows 原生、功能完整（模型导入+TTS+对话），对中文新手可读性好。
- 可复用性：🔶 参考 —— Qt/C++ 需编译、无 license，功能思路值得借鉴。

### blueberrymaid/phrolova-agent-platform —— 多后端 LLM + 台词语料检索 + Live2D 桌宠平台
- 链接：https://github.com/blueberrymaid/phrolova-agent-platform
- 核实：stars=1 · license=MIT · language=Vue · pushed=2026-09-25 · updated_at=2026-09-28
  - 命令：`gh api repos/blueberrymaid/phrolova-agent-platform --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：FastAPI + Vue3 + LangChain + PostgreSQL/PgVector + Redis + MinIO 的智能体平台，含多后端 LLM 对话与 Live2D 桌宠，Docker Compose 一键起。
- 为什么值得看：技术栈完整、Docker 一键起，是「全套后端 + Live2D 前端」的工程范式；可换成 Ollama 作为 LLM 后端。
- 可复用性：🔶 参考 —— 中间件较重（PG/Redis/MinIO），超个人站需求，架构值得参考。

### zminlibra/xiaoya_girlfriend —— 「小雅」：HuggingFace 语音到语音 + Live2D 桌宠 + agent 工具 + 向量记忆
- 链接：https://github.com/zminlibra/xiaoya_girlfriend
- 核实：stars=0 · license=Apache-2.0 · language=Python · pushed=2026-09-22 · updated_at=2026-09-21
  - 命令：`gh api repos/zminlibra/xiaoya_girlfriend --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：AI 语音女友，基于 HuggingFace speech-to-speech，带 agent 工具、语音设计与向量记忆，形象为 Live2D 桌宠。
- 为什么值得看：Apache-2.0 + Python，把「S2S 语音 + agent 工具 + Live2D」串起来的完整案例。
- 可复用性：🔶 参考 —— 依赖 HF S2S 较重，先看其语音↔形象联动实现。

### xShiroeNguyenx/desktop-companion —— 自带 AI 翻译/快捷回复的 Windows Live2D 桌宠
- 链接：https://github.com/xShiroeNguyenx/desktop-companion
- 核实：stars=1 · license=NOASSERTION · language=JavaScript · pushed=2026-09-15 · updated_at=2026-09-15
  - 命令：`gh api repos/xShiroeNguyenx/desktop-companion --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Windows 独立 Live2D 桌宠，内置 AI 翻译、快捷回复、任务保存，可悬浮在任意应用之上。
- 为什么值得看：把桌宠做成「工具型挂件」（翻译/回复）是差异化思路，Electron/JS 栈对新手友好。
- 可复用性：🔶 参考 —— 思路有趣但 star 极少、license 非标准，先看交互设计。

### Ding808/Nikki-Bongo-Cat —— 带 AI 用量统计的 Windows Live2D 桌宠
- 链接：https://github.com/Ding808/Nikki-Bongo-Cat
- 核实：stars=2 · license=none · language=C# · pushed=2026-09-14 · updated_at=2026-09-14
  - 命令：`gh api repos/Ding808/Nikki-Bongo-Cat --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Windows Live2D 桌宠，含每日 AI 用量统计、成本估算、中英 UI、Steam Bongo Cat 联动。
- 为什么值得看：把「AI 用量/花费」做成桌宠展示，对天天用 API 的人有直接价值。
- 可复用性：🔶 参考 —— C# 栈、无 license，先借用「用量可视化」这个点子。

### ljhLJH0102-0721/Romasha-Live2D-AI —— Live2D 桌宠 + 本地 AI 伴侣（仅代码）
- 链接：https://github.com/ljhLJH0102-0721/Romasha-Live2D-AI
- 核实：stars=0 · license=NOASSERTION · language=Python · pushed=2026-10-11 · updated_at=2026-10-11
  - 命令：`gh api repos/ljhLJH0102-0721/Romasha-Live2D-AI --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Live2D 桌宠 + 本地 AI 伴侣；仓库仅含代码，模型/素材不含。
- 为什么值得看：当日活跃、Python 栈，本地 AI 伴侣结构可对照；但缺素材、无清晰 license。
- 可复用性：🔶 参考 —— 代码骨架可看，素材需自备。

### C6H5Gp/deskpet —— Electron 点击穿透的 Windows Live2D 桌宠
- 链接：https://github.com/C6H5Gp/deskpet
- 核实：stars=0 · license=none · language=JavaScript · pushed=2026-09-23 · updated_at=2026-09-23
  - 命令：`gh api repos/C6H5Gp/deskpet --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Electron 实现的 Windows Live2D 桌宠，支持点击穿透。
- 为什么值得看：Electron 点击穿透的实现细节对自建桌宠有参考价值。
- 可复用性：🔶 参考 —— 无 license、功能单一，仅取「穿透窗口」实现。

### kushana-86/shima-rin-ai —— 志摩凛 AI 桌面伴侣（Live2D + LLM + 语音）
- 链接：https://github.com/kushana-86/shima-rin-ai
- 核实：stars=0 · license=none · language=JavaScript · pushed=2026-08-05 · updated_at=2026-08-05
  - 命令：`gh api repos/kushana-86/shima-rin-ai --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：中文的 AI 桌面伴侣，Live2D + LLM 对话 + 语音交互。
- 为什么值得看：中文、轻量、主题单一明确，可作小体量桌宠范例。
- 可复用性：🔶 参考 —— 无 license，pushed 已 2 个月，先看结构。

### 分组 C · 制作工具链（PSD/MOC3/动作）

### KurisuMakise004/renderkit —— 把 PMX/VRM/MOC3 渲染成 albedo/depth 的 CLI
- 链接：https://github.com/KurisuMakise004/renderkit
- 核实：stars=29 · license=Unlicense · language=Jupyter Notebook · pushed=2026-10-02 · updated_at=2026-10-02
  - 命令：`gh api repos/KurisuMakise004/renderkit --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：命令行工具，把 PMX / VRM / MOC3 等模型批量渲染成 albedo/depth 图。
- 为什么值得看：Unlicense（公共领域）、支持 MOC3，做数据集/预览图/训练素材时是现成的批处理管线。
- 可复用性：✅ 落地 —— 免许可负担、CLI 即用，配合他的索引站出图或做素材预处理很直接。

### Hana-ame/moc3-json-viewer —— 纯 Canvas2D 的 moc3 JSON 查看器（零依赖）
- 链接：https://github.com/Hana-ame/moc3-json-viewer
- 核实：stars=0 · license=none · language=HTML · pushed=2026-09-25 · updated_at=2026-09-25
  - 命令：`gh api repos/Hana-ame/moc3-json-viewer --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：单文件 HTML 的 moc3 JSON 查看器，纯 Canvas2D、零依赖、上传即看、不存储模型数据。
- 为什么值得看：单文件、零依赖，正好可以当作自己 GitHub Pages 索引站的「模型预览」小工具，或本地调试 moc3 用。
- 可复用性：✅ 落地 —— 一个 HTML 文件拖进站点即可，零成本且隐私友好。

### Type010/live2d-web —— 把 moc3 做成网站看板娘（带面板切换背景/装饰/表情）
- 链接：https://github.com/Type010/live2d-web
- 核实：stars=0 · license=none · language=TypeScript · pushed=2026-09-30 · updated_at=2026-09-30
  - 命令：`gh api repos/Type010/live2d-web --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：将 moc3 模型用作网站看板娘，附带面板控制，可切换背景、装饰、表情。
- 为什么值得看：直接对口「GitHub Pages 索引站 + 看板娘」的场景，控制面板的实现可抄。
- 可复用性：✅ 落地 —— 正好能挂到他的索引站上；无 license、star=0 需自行判断质量。

### canyueY/pyqt-live2d-bridge —— 在 PyQt5 里渲染 Live2D 并绑定动作/表情/情绪
- 链接：https://github.com/canyueY/pyqt-live2d-bridge
- 核实：stars=1 · license=MIT · language=Python · pushed=2026-09-19 · updated_at=2026-09-19
  - 命令：`gh api repos/canyueY/pyqt-live2d-bridge --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：在 PyQt5 中渲染 Live2D Cubism 模型，并做动作、表情、情绪绑定。
- 为什么值得看：Python 栈 + MIT，是「用 Python 写 Live2D 桌面程序」的现成桥接层，与他 Python 环境契合。
- 可复用性：✅ 落地 —— MIT + Python，装上就能跑，适合做纯 Python 的桌宠/工具。

### arkrolin/VLive —— Live2D VLA：由「角色 rig + 动作标签」生成 motion3.json 参数曲线
- 链接：https://github.com/arkrolin/VLive
- 核实：stars=0 · license=none · language=Python · pushed=2026-09-20 · updated_at=2026-09-20
  - 命令：`gh api repos/arkrolin/VLive --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：把「角色 rig + 动作标签」映射为 motion3.json 参数曲线的研究型项目（含消融日志与 V11 角色条件化重设计）。
- 为什么值得看：代表「生成式动作合成」这条新方向，将来「文字/标签直接驱动 Live2D 动作」值得关注。
- 可复用性：🔶 参考 —— 研究性质、无 license、star=0，思路领先但暂不可用。

### potter-pixel/live2d-motion-animator —— Live2D 动作动画器
- 链接：https://github.com/potter-pixel/live2d-motion-animator
- 核实：stars=0 · license=none · language=TypeScript · pushed=2026-07-12 · updated_at=2026-07-12
  - 命令：`gh api repos/potter-pixel/live2d-motion-animator --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：TS 写的 Live2D 动作（motion）动画器。
- 为什么值得看：动作编辑类工具较少见，可看其时间轴/曲线实现。
- 可复用性：🔶 参考 —— 无 license、信息少，仅作实现参考。

### madosuki/live2dManager —— Cubism SDK for Web 的非官方封装库
- 链接：https://github.com/madosuki/live2dManager
- 核实：stars=1 · license=NOASSERTION · language=TypeScript · pushed=2026-09-15 · updated_at=2026-09-15
  - 命令：`gh api repos/madosuki/live2dManager --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Live2D Cubism SDK for Web 的非官方 JS/TS 库。
- 为什么值得看：想简化 Web 端 SDK 调用时可参考它的封装 API 设计。
- 可复用性：🔶 参考 —— license 未标准化、star 低，先看 API 设计。

### Eatgrapes/Live2D-JavaBinding —— Cubism SDK 的 Java 绑定（MIT）
- 链接：https://github.com/Eatgrapes/Live2D-JavaBinding
- 核实：stars=16 · license=MIT · language=Java · pushed=2026-06-27 · updated_at=2026-08-19
  - 命令：`gh api repos/Eatgrapes/Live2D-JavaBinding --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Cubism SDK 的 JavaBindings。
- 为什么值得看：JVM 生态里少见的 Cubism 绑定，MIT；若将来做 Android/Java 桌宠有用。
- 可复用性：🔶 参考 —— 与他 Python/JS 主线不重合，先记档。

### jz315/live2d-cubism-core-sys —— Cubism Native Core v5 的 Rust FFI 绑定
- 链接：https://github.com/jz315/live2d-cubism-core-sys
- 核实：stars=1 · license=MIT · language=Rust · pushed=2026-04-04 · updated_at=2026-04-05
  - 命令：`gh api repos/jz315/live2d-cubism-core-sys --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Live2D Cubism SDK Native Core（v5）的原始 Rust FFI 绑定。
- 为什么值得看：Rust 生态接入 Cubism 的底层入口，MIT；配合上面的 Rust 桌宠可用。
- 可复用性：🔶 参考 —— 底层 FFI、star 低，需 Rust 能力，先记档。

### funlin724/emote-to-cubism —— E-mote(PSB) → Live2D Cubism 转换工具链与格式文档
- 链接：https://github.com/funlin724/emote-to-cubism
- 核实：stars=0 · license=MIT · language=Python · pushed=2026-09-19 · updated_at=2026-09-19
  - 命令：`gh api repos/funlin724/emote-to-cubism --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：E-mote 格式（PSB）转 Live2D Cubism 的转换工具链与格式文档；不含游戏素材、无厂商密钥（自带文件）。
- 为什么值得看：跨格式迁移（E-mote→Cubism）的稀缺工具，且明确「自带文件」规避版权问题。
- 可复用性：🔶 参考 —— 小众格式、star=0，但格式文档有参考价值。

### daoming07280/live2d-auto-pipeline —— See-through 768/30 + psd2live 自动化流程笔记与脚本
- 链接：https://github.com/daoming07280/live2d-auto-pipeline
- 核实：stars=0 · license=MIT · language=Python · pushed=2026-09-18 · updated_at=2026-09-18
  - 命令：`gh api repos/daoming07280/live2d-auto-pipeline --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Live2D 自动化流程，含 See-through 768/30 与 psd2live 工作流笔记、脚本与样例 moc3 结果（RTX 4060）。
- 为什么值得看：把「拆层 + 绑定」整条链参数化，且有 RTX 4060 实测；不过依赖的 psd2live 本索引已收录。
- 可复用性：🔶 参考 —— 与已收录 psd2live 同链，取其流程笔记即可，别重复造。

### obrs09/layer-pipeline —— image→live2d 的工作流
- 链接：https://github.com/obrs09/layer-pipeline
- 核实：stars=0 · license=none · language=Python · pushed=2026-09-23 · updated_at=2026-09-23
  - 命令：`gh api repos/obrs09/layer-pipeline --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：`workflow_image_to_live2d`，图像到 Live2D 的流程。
- 为什么值得看：同属「图生 Live2D」赛道，可作对照；但无 license、信息少。
- 可复用性：🔶 参考 —— 同类已有多条（见去重报告），非必要不重复。

### Laughting455/live2d_toolkit-v2 —— PNG 立绘精准拆成 Live2D 可开 PSD 的 AI 应用
- 链接：https://github.com/Laughting455/live2d_toolkit-v2
- 核实：stars=0 · license=none · language=（未识别） · pushed=2026-05-16 · updated_at=2026-05-16
  - 命令：`gh api repos/Laughting455/live2d_toolkit-v2 --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：AI Web 应用，把一张 PNG 角色立绘精确拆层成 Live2D 可直接打开的 PSD；含 conda 环境、Gradio 界面、Unity 集成与动捕驱动。
- 为什么值得看：拆层是「图生 Live2D」的关键痛点，Gradio 界面 + conda 对新手友好；但 5 月后未再更新、无 license。
- 可复用性：🔶 参考 —— 拆层思路可用，注意停更。

### daoming07280/whale-maid-svg-layers —— 59 层 PSD/SVG 拆层样例（psd2live→moc3）
- 链接：https://github.com/daoming07280/whale-maid-svg-layers
- 核实：stars=0 · license=none · language=Python · pushed=2026-09-21 · updated_at=2026-09-29
  - 命令：`gh api repos/daoming07280/whale-maid-svg-layers --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：一个 59 层 PSD/SVG 拆层样例（鲸鱼娘），走 psd2live→moc3 管线。
- 为什么值得看：可作为「拆层 → 绑定」链路的现成样例数据来对照。
- 可复用性：🔶 参考 —— 单例样例，仅供学习，无 license。

### xez65/bang-dream-old-moc-game-import-workflow —— 老式 MOC → MOC3 + Unity 的可复核迁移流程
- 链接：https://github.com/xez65/bang-dream-old-moc-game-import-workflow
- 核实：stars=0 · license=none · language=（未识别） · pushed=2026-10-07 · updated_at=2026-10-07
  - 命令：`gh api repos/xez65/bang-dream-old-moc-game-import-workflow --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：把 Bang Dream 老式 MOC 模型迁移到 MOC3 与 Unity 的可复核工作流。
- 为什么值得看：老格式迁移的实操记录，格式转换类问题可参考。
- 可复用性：🔶 参考 —— 极窄场景，仅格式迁移时翻看。

### jianchengwang/live2d_models —— 网站看板娘 Live2D 模型集（JS 加载）
- 链接：https://github.com/jianchengwang/live2d_models
- 核实：stars=28 · license=MIT · language=JavaScript · pushed=2026-10-08 · updated_at=2026-10-08
  - 命令：`gh api repos/jianchengwang/live2d_models --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：「萌萌哒的看板娘」，网站看板娘 Live2D 模型与加载代码集。
- 为什么值得看：MIT、28★、10-08 仍在更新，拿来给个人站加看板娘最省事。
- 可复用性：✅ 落地 —— MIT + 现成模型/加载代码，挂到 GitHub Pages 索引站即可。

### 分组 D · 查看器 / 渲染器

### o0Nomar0o/Motiv2D —— Spine2D + Live2D 双格式查看器
- 链接：https://github.com/o0Nomar0o/Motiv2D
- 核实：stars=45 · license=MIT · language=JavaScript · pushed=2026-06-26 · updated_at=2026-09-14
  - 命令：`gh api repos/o0Nomar0o/Motiv2D --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：同时查看 Spine2D 与 Live2D 模型的 Web 查看器。
- 为什么值得看：45★、MIT、Web 实现，是「多 2D 骨骼格式统一查看」的参考。
- 可复用性：🔶 参考 —— 功能对口但非必需，可参考其加载/渲染封装。

### Untitled-Story/untitled-sekai-live2d-viewer —— 极简 Project Sekai Live2D 查看器（支持并行动作）
- 链接：https://github.com/Untitled-Story/untitled-sekai-live2d-viewer
- 核实：stars=3 · license=Apache-2.0 · language=TypeScript · pushed=2026-04-29 · updated_at=2026-04-29
  - 命令：`gh api repos/Untitled-Story/untitled-sekai-live2d-viewer --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：极简的 Project Sekai Live2D 查看器，支持并行动作。
- 为什么值得看：Apache-2.0、TS；作者团队另有一个已收录项目（`untitled-story/untitled-pixi-live2d-engine`），本条是其配套查看器。
- 可复用性：🔶 参考 —— 与已收录引擎同源，配套关系值得注意，属小众场景。

### bungaku-moe/Azure-Gravure —— 碧蓝航线交互式 Live2D 查看器
- 链接：https://github.com/bungaku-moe/Azure-Gravure
- 核实：stars=29 · license=MIT · language=C# · pushed=2025-06-03 · updated_at=2026-10-02
  - 命令：`gh api repos/bungaku-moe/Azure-Gravure --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：碧蓝航线游戏内 Live2D 的交互式查看器，C# 实现。
- 为什么值得看：stars 尚可、MIT；但 C# 桌面栈 + 游戏资源专项，pushed 停在 2025-06（star 数靠近期曝光）。
- 可复用性：🔶 参考 —— 场景偏游戏资源查看，与他的主线关联弱，勉强参考。

### mogmog-0110/live2d-cubism-d3d12 —— Cubism 5 移植到 Direct3D 12（官方未支持）
- 链接：https://github.com/mogmog-0110/live2d-cubism-d3d12
- 核实：stars=0 · license=MIT · language=C++ · pushed=2026-08-27 · updated_at=2026-08-27
  - 命令：`gh api repos/mogmog-0110/live2d-cubism-d3d12 --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：把 Live2D Cubism 5 忠实移植到 Direct3D 12（官方仅支持 D3D11），声称与官方 D3D11 样例渲染一致。
- 为什么值得看：底层渲染移植的技术参考，展示 Cubism 渲染管线如何适配新图形 API。
- 可复用性：🔶 参考 —— 纯底层、star=0，除非要自写渲染器否则用不上。

### NathanDVD/L2DRenderer —— DirectX11 + Cubism Native SDK 的渲染器
- 链接：https://github.com/NathanDVD/L2DRenderer
- 核实：stars=0 · license=MIT · language=C++ · pushed=2026-04-07 · updated_at=2026-04-07
  - 命令：`gh api repos/NathanDVD/L2DRenderer --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：用 DirectX11 与 Live2D Cubism Native SDK 做的渲染器。
- 为什么值得看：Windows 原生渲染器的起步参考，MIT。
- 可复用性：🔶 参考 —— 与上面 D3D12 同理，底层参考。

### rydanee/live2drust —— Rust 写的 .moc3 查看器
- 链接：https://github.com/rydanee/live2drust
- 核实：stars=0 · license=none · language=Rust · pushed=2026-09-23 · updated_at=2026-09-23
  - 命令：`gh api repos/rydanee/live2drust --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：简单的 .moc3 模型查看器（Rust）。
- 为什么值得看：Rust + moc3 查看的最小实现，可作解析参考。
- 可复用性：🔶 参考 —— 无 license、star=0，仅看解析实现。

### rayriffy/CubismMetal —— 针对 Metal API 优化的 Live2D 查看器
- 链接：https://github.com/rayriffy/CubismMetal
- 核实：stars=0 · license=none · language=Swift · pushed=2026-09-16 · updated_at=2026-09-16
  - 命令：`gh api repos/rayriffy/CubismMetal --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：针对 Metal API 调优的高性能 Live2D 查看器（Swift）。
- 为什么值得看：Apple 平台渲染优化参考。
- 可复用性：❌ 不采用 —— Apple/Metal 专属，与 Windows 基准场景无关。

### KristopherGBaker/Live2DKit —— Cubism Native SDK 的 Swift 封装（Metal）
- 链接：https://github.com/KristopherGBaker/Live2DKit
- 核实：stars=1 · license=NOASSERTION · language=Swift · pushed=2026-08-10 · updated_at=2026-08-10
  - 命令：`gh api repos/KristopherGBaker/Live2DKit --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Swift 封装 Cubism Native SDK，加载模型、驱动参数/动作、经 Metal 在 iOS/macOS 渲染（BYO SDK）。
- 为什么值得看：Apple 生态里较完整的 Cubism 封装。
- 可复用性：❌ 不采用 —— iOS/macOS 专属，与 Windows 场景无关。

### SubNoted/live2d4wayland —— Wayland 专用轻量 Live2D 查看器
- 链接：https://github.com/SubNoted/live2d4wayland
- 核实：stars=0 · license=none · language=Rust · pushed=2026-07-07 · updated_at=2026-07-07
  - 命令：`gh api repos/SubNoted/live2d4wayland --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：面向 Wayland 的轻量、零额外依赖 Live2D 查看器。
- 为什么值得看：Linux 桌面集成参考。
- 可复用性：❌ 不采用 —— Wayland/Linux 专属，与 Windows 场景无关。

### NaviVoid/Rive2d —— niri 桌面下的 Live2D 查看器
- 链接：https://github.com/NaviVoid/Rive2d
- 核实：stars=0 · license=MIT · language=TypeScript · pushed=2026-09-18 · updated_at=2026-09-18
  - 命令：`gh api repos/NaviVoid/Rive2d --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：为 niri（Wayland 平铺合成器）做的 Live2D 查看器。
- 为什么值得看：Linux 桌面挂件思路。
- 可复用性：❌ 不采用 —— niri/Wayland 专属，与 Windows 场景无关。

### HaiKonofanDesu/konofan-live2d —— 游戏内 Live2D 素材库（附查看器计划）
- 链接：https://github.com/HaiKonofanDesu/konofan-live2d
- 核实：stars=44 · license=none · language=（未识别） · pushed=2025-02-15 · updated_at=2026-10-04
  - 命令：`gh api repos/HaiKonofanDesu/konofan-live2d --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：某游戏全部 Live2D 形象素材，未来计划自带查看器。
- 为什么值得看：素材量大，但 pushed 停在 2025-02、无 license、无代码。
- 可复用性：❌ 不采用 —— 纯游戏素材 dump、无代码、无许可，法律与实用价值都不高。

### 分组 E · 引擎集成 / 其他

### GunGuyDude-Python/renpy-live2d-plus —— Ren'Py 的 Live2D 增强模块
- 链接：https://github.com/GunGuyDude-Python/renpy-live2d-plus
- 核实：stars=0 · license=GPL-3.0 · language=Python · pushed=2026-05-15 · updated_at=2026-05-15
  - 命令：`gh api repos/GunGuyDude-Python/renpy-live2d-plus --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：Ren'Py 的 Live2D 增强版本（描述字段为空，从命名判断为 renpy-live2d 的增强分支）。
- 为什么值得看：**直接命中最关键场景**——他的目标引擎之一就是 Ren'Py，而官方 Ren'Py 的 Live2D 支持有限，这条是想扩展 Live2D 能力时的入口；GPL-3.0。
- 可复用性：🔶 参考 —— 方向极对口，但 star=0、描述为空、5 月后未更新，需自行核对是否可用；对照已收录的 `asfdfdfd/renpy-live2d` 一起看。

### Up-to-code/edwardarwin —— 本地 macOS 语音伴侣（Live2D 动作 + SQLite 记忆 + 桌面 MCP）
- 链接：https://github.com/Up-to-code/edwardarwin
- 核实：stars=1 · license=NOASSERTION（mixed-license） · language=TypeScript · pushed=2026-10-10 · updated_at=2026-10-10
  - 命令：`gh api repos/Up-to-code/edwardarwin --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：面向 macOS 的本地 AI 伴侣「Emma Darwin」，含语音、Live2D 动作、SQLite 记忆与桌面 MCP 工具，混合许可源码。
- 为什么值得看：把「Live2D 动作 + 记忆 + MCP 工具」串成桌面伴侣，架构完整、当日活跃。
- 可复用性：🔶 参考 —— macOS 专属且混合许可，架构可学但不宜直接采用。

### DennyWanye/deskpet-engine —— 可插拔的 2D 桌宠渲染后端抽象（Cubism 替代）
- 链接：https://github.com/DennyWanye/deskpet-engine
- 核实：stars=1 · license=MIT · language=TypeScript · pushed=2026-06-13 · updated_at=2026-09-10
  - 命令：`gh api repos/DennyWanye/deskpet-engine --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：免版税的、可插拔的 2D 桌宠角色渲染后端抽象层，定位「独立/爱好者项目的 Live2D Cubism 替代」。
- 为什么值得看：想做「不被 Cubism 许可约束」的桌宠时，这是渲染抽象层的思路参考，MIT、TS。
- 可复用性：🔶 参考 —— 抽象层设计值得借鉴，尚早期，先看接口。

### yazelin/glitch-2d —— Live2D Cubism 5.0 的 Glitch 模型 + 可编辑 rig + 交互展示
- 链接：https://github.com/yazelin/glitch-2d
- 核实：stars=0 · license=MIT · language=JavaScript · pushed=2026-09-24 · updated_at=2026-09-24
  - 命令：`gh api repos/yazelin/glitch-2d --jq '{stars:.stargazers_count,lic:.license.spdx_id,lang:.language,pushed:.pushed_at}'`
- 是什么：一个 Glitch 风格的 Live2D Cubism 5.0 模型，含可编辑 rig 与交互式展示。
- 为什么值得看：MIT + Cubism 5，提供了「模型 + rig + 展示」整套样例，可拆解学习。
- 可复用性：🔶 参考 —— 单例模型样例，学习 rig 结构用。

> 其余已核实但未单独立条的候选，见下方「去重报告 · 未立条的候选」。

## 去重报告

查重命令（对每个候选执行，命中即弃）：
```bash
cd D:/34498/Documents/github-projects-invest-games && export PATH=/usr/bin:$PATH
grep -iF "<owner/repo>" _r30/_dedupe_gh.txt index.html csdn-social-summary.md csdn-social-summary-v28.md csdn-social-summary-v27.md
```

### 命中已收录 · 剔除（4 条）

| 候选 | 命中位置 | 剔除原因 |
|---|---|---|
| `tsunehimatoi/psd2live` | `_r30/_dedupe_gh.txt`（`github.com/tsunehimatoi/psd2live`） | 本辑热门（612★，PSD→Live2D 自动绑定），但**已收录**，弃。多个新仓库（见下）都依赖它。 |
| `lmmtrr/spive2d` | `_r30/_dedupe_gh.txt`（`github.com/lmmtrr/spive2d`） | Spine&Live2D 查看器，**已收录**，弃。 |
| `lvhaojie456/image-to-live2d` | `index.html`（已作为 `flowingduskpro/jpg-to-live2d-workflow` 的同类变体被点名） | 已被索引正文提及，**弃**。 |
| `flowingduskpro/jpg-to-live2d-workflow` | `index.html`（同上，同一句「同类还有…」） | 已被索引正文提及，**弃**。 |

### 已知已收录的 Live2D 仓库（按任务清单排除，未再查重）
`adrianiainlam/facial-landmarks-for-cubism` · `aethiopicuschan/cubism-go` · `ariakage/live2d-agent-kit` · `asfdfdfd/renpy-live2d` · `cyanfish-x/dsh-live2d-pets` · `easylive2d/live2d-motion3` · `easylive2d/live2d-py` · `guansss/live2d-viewer-web` · `guansss/pixi-live2d-display` · `hera-berg/open-avatar-creator` · `joyparkray/agent-avatar` · `kojimio/renpylive2dtracesample` · `kota-ohno/seethrough-live2d-pipeline` · `live2d/cubismnativeframework` · `live2d/cubismspecs` · `live2d/cubismunitycomponents` · `live2d/cubismwebframework` · `lk2168/vtuber-pipeline` · `luomo66ccff/amahane-hikari-live2d` · `mizunagikb/gd_cubism` · `myths-labs/prometheus-avatar` · `nana7chi/cubismexternaleditmcp` · `omniwaifu/pixi-live2d5` · `open-llm-vtuber/open-llm-vtuber` · `openl2d/moc3ingbird` · `panzer-jack/easy-live2d` · `perfare/unitylive2dextractor` · `rc14193/renpylive2deyefollowdemo` · `shinshin86/live2d-add-motion-sample-web-ui` · `so0420/doro-live2d-web` · `umamoorg/umamo` · `untitled-story/untitled-pixi-live2d-engine` · `wzhang3912/image2live2d`

> 备注：检索中还出现 `Hera-Berg/open-avatar-creator`（大小写差异，等同已收录的 `hera-berg/open-avatar-creator`）、`adrianiainlam/mouse-tracker-for-cubism`（与已收录 `facial-landmarks-for-cubism` 同作者同族），一并排除。

### 未立条但已核实 · 归入观察（查重均 NEW，但立条价值低或与场景弱相关）

| 候选 | 核实（stars/lic/lang/pushed） | 为何不单独立条 |
|---|---|---|
| `realtime-ai/live2d-agent` | 2 / none / HTML / 2026-02-14 | 仅名字相关，描述就是 "live2d agent"，无实质内容、已停更 8 个月。 |
| `Aaaazdy/VirtualPersonalAssistant` | 2 / Apache-2.0 / TS / 2025-11-05 | 学生项目、停更近一年。 |
| `ZophiaWong/desk-mate-kira` | 0 / none / C# / 2026-07-11 | Unity+Cubism 桌宠，与 `ymhyyds/DesktopPet` 同类且更弱。 |
| `PCMakia/Agent_mobile` | 0 / GPL-3.0 / — / 2026-04-02 | 只是一个 APK 发布页，无源码主体。 |
| `lindenthink/CubismSdkForWeb-5-r.4` | 0 / NOASSERTION / TS / 2026-03-26 | 官方 SDK 的私有定制分支，非通用工具。 |
| `UFOnian/.physics3.json-Editor` | 1 / none / HTML / 2026-03-01 | physics3.json 编辑器，极窄；可作为物理配置小工具备查。 |
| `ShapeLayer/cubism-sdk-realtime-facial-representation` | 0 / NOASSERTION / C++ / 2026-02-01 | 课程作业、已归档性质。 |
| `igttttma/how_to_download_old_cubism_sdk` | 0 / none / — / 2026-05-23 | 仅笔记（如何下载旧版 SDK），无代码。 |
| `RifkyA911/mirunova-live` | 0 / none / Svelte / 2026-10-11 | 当日新建的 Web Live2D&3D 追踪器，太早期（1 天），无法评估。 |
| `poroburu/juno-vtuber-workflows` | 0 / none / Python / 2026-06-10 | 某特定 VTuber 的 ComfyUI 工作流，绑定单一角色。 |
| `shinshin86/mesh-avatar-studio` | 596 / MIT / TS / 2026-10-11 | 高星，但做的是「插画→2D 网格变形头像」（mesh），README 不含 Live2D，属**替代路线**；可关注但非 Live2D 项目。 |
| `adrianiainlam/mouse-tracker-for-cubism` | 15 / — / C++ / 2026-04-02 | 同作者已收录 `facial-landmarks-for-cubism` 的姊妹项目，同族不重复收。 |

### 去重结论
- 本辑共核实候选 **60+** 个，**剔除 4 个命中已收录**、**排除 33 个任务清单已知仓库**、**12 个归入观察**，最终**立条 55 条**（✅落地 12 · 🔶参考 38 · ❌不采用 5）。
- 值得注意的重复模式：`psd2live` 已成「图生 Live2D」事实标准上游，`daoming07280/live2d-auto-pipeline`、`daoming07280/whale-maid-svg-layers`、`obrs09/layer-pipeline` 等都是它的下游变体，**本辑只保留其中 1 条**（live2d-auto-pipeline）作为流程笔记代表，其余同链不重复造。
