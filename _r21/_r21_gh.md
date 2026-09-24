# 第 21 轮 GitHub 调研（GitHub 路）

> 核查时间：2026-09-24（仓库元数据来自 GitHub API 实测 `stargazers_count / license.spdx_id / language / pushed_at / created_at`）
> 去重基线：`index.html`（1120 项）、`csdn-social-summary.md`、`csdn-social-summary-v20.md`、`csdn-social-summary-v19.md`；并比对 `_r20/_r20_gh.md`。
> 受众基准：16GB RAM Windows、本地 Ollama、维护静态索引站、用 Ren'Py 做过视觉小说、习惯 Python 写检查脚本。
> 进度（房规 #47：边做边落盘）：**已完成，25 条**（游戏 6 / 上下文 4 / VS Code 1 / vibe coding 2 / DSH 5 / memory 3 / 模型评测 4），末附本路去重报告。

## 一、游戏制作与拓展（引擎 AI 集成 / agent CLI / 素材管线 / 发行打包）

### 1. `youichi-uda/godot-mcp-pro`

- URL：https://github.com/youichi-uda/godot-mcp-pro
- 元数据：**607 stars**｜**未声明（GitHub API `license=NOASSERTION`）**｜**GDScript**｜最近更新 **2026-09-23T22:28:57Z**｜创建 **2026-02-24T08:12:34Z**
- 是什么：Godot 4 的 MCP server + 编辑器插件，号称 175 个工具；架构为 `AI 客户端 ← stdio/MCP → Node.js server ← WebSocket:6505 → Godot 编辑器插件`，走编辑器 API / UndoRedo / 场景树，是"实时而非轮询文件"的路线。
- **可复用性：不采用。** 公开仓库只放了免费的 Godot addon，真正连 AI 的 `server/` 目录是**一次性付费包**（Buymeacoffee / itch.io），克隆下来看不到 `server/` 属正常；且许可为 NOASSERTION（非标准/未明确），加上它是 GDScript + Node 双栈，与 Ren'Py 无关。可参考的只有"WebSocket 常驻 + 编辑器 UndoRedo 可回退"这条交互设计。
- 去重核查：`grep -ilF "youichi-uda/godot-mcp-pro" index.html csdn-social-summary.md csdn-social-summary-v19.md csdn-social-summary-v20.md _r20/_r20_gh.md` **0 命中**；裸名 `godot-mcp-pro` 亦 0 命中。

### 2. `IvanMurzak/GameDev-MCP-Server`

- URL：https://github.com/IvanMurzak/GameDev-MCP-Server
- 元数据：**13 stars**｜**Apache-2.0**｜**C#**｜最近更新 **2026-09-24T02:22:53Z**｜创建 **2026-06-11T10:56:32Z**
- 是什么：Unity-MCP / Godot-MCP / Unreal-MCP 三个引擎插件**共用的引擎无关 MCP 宿主**（NuGet 包 + Docker 镜像），链路是 `MCP 客户端 ⇄ gamedev-mcp-server ⇄(SignalR)⇄ 引擎插件`，仓库内无引擎专属代码，工具/资源由接入的引擎插件动态提供。
- **可复用性：参考。** 机制上"一个 server 二进制服务多个引擎、能力由插件侧动态注入"值得借鉴到多 harness 共用一套工具面；但实现是 .NET/C# + SignalR + Docker，对 16GB Windows 的 Ren'Py 场景过重，且需另装对应引擎插件（Unity/Godot/Unreal），与 Ren'Py 不通用。
- 去重核查：完整路径 5 份基线 **0 命中**；裸名 `GameDev-MCP-Server` 0 命中；未与索引中已有的 `AI-Game-Dev-Server`（云端计费代理）混淆。

### 3. `nguyenchiencong/godot-mcp-cli`

- URL：https://github.com/nguyenchiencong/godot-mcp-cli
- 元数据：**12 stars**｜**MIT**｜**GDScript**｜最近更新 **2026-09-23T10:31:06Z**｜创建 **2025-11-02T05:34:06Z**
- 是什么：把 Godot 交互做成 **CLI** 而非直接 MCP，理由是"只有工具输出进上下文，省 token"；覆盖场景/节点/脚本/着色器编辑、运行时场景快照、表达式求值、断点与单步调试、输入模拟、把场景渲染成 PNG 给视觉模型看、生成 `project_guide.md` / `AGENTS.md`。
- **可复用性：参考。** `npm install -g godot-mcp-cli` 是标准包管理器安装，Windows 可用 npm；"CLI 优先、MCP 次之，为了压上下文"这条取舍对本机 16GB + 小模型特别适用，可直接搬到 Ren'Py 的 lint/build/screenshot 工具链（Godot 侧代码本身不可复用）。
- 去重核查：完整路径 **0 命中**；裸名 `godot-mcp-cli` 0 命中。

### 4. `estebanrfp/defold-ai`

- URL：https://github.com/estebanrfp/defold-ai
- 元数据：**4 stars**｜**未声明（`license=NOASSERTION`）**｜**Lua**｜最近更新 **2026-05-27T00:38:11Z**｜创建 **2026-05-26T17:07:06Z**
- 是什么：Defold 版 MCP 桥：Python FastMCP server + Defold 编辑器脚本（`.editor_script`），走 Defold 内置 HTTP server，无需 WebSocket；能建 collection、生成 game object、加组件、改脚本、配渲染管线、装材质/相机/粒子预设、构建并运行，约 35 个工具。
- **可复用性：参考。** 需 Defold 1.10+ 与 Python 3.10+ `uv`（README 只给 Unix `curl` 安装），未点名支持 Windows；但"编辑器自带 HTTP server 直接当桥、脚本落 `~/.defold_ai_url` 让 server 自动发现端口"这个免桥接思路可套到 Ren'Py；明确写着灵感来自 `godot-ai`，是为非 Godot 引擎补齐同类能力的案例。
- 去重核查：完整路径 **0 命中**；裸名 `defold-ai` 0 命中；其上游参考 `hi-godot/godot-ai` 已在 `index.html`，但不构成对本仓库的命中。

### 5. `Lolner95/godotter`

- URL：https://github.com/Lolner95/godotter
- 元数据：**31 stars**｜**MIT**｜**GDScript**｜最近更新 **2026-05-20T17:21:48Z**｜创建 **2026-05-12T05:14:57Z**
- 是什么：Godot 4 编辑器内的 AI 副驾停靠面板 + 小型本地 Python server，定位"给 Godot 的 Cursor"：可计划、解释、可视化，并在**明确授权后**带 plan/diff/历史护栏地改项目文件；支持 Gemini / OpenAI / Claude 三类 provider。
- **可复用性：参考。** "先出计划 → 展示 diff → 用户批准才落盘"的护栏流程与 Ren'Py 脚本改动场景高度契合，值得抄设计；但运行必须填云端 API key（Gemini/OpenAI/Claude），README 未提供 Ollama 本地路径，对离线/本地优先的 16GB 机器是硬门槛。
- 去重核查：完整路径 **0 命中**；裸名 `godotter` 0 命中。

### 6. `cats2333/bevy_ai_editor`

- URL：https://github.com/cats2333/bevy_ai_editor
- 元数据：**12 stars**｜**未声明（`license=null`）**｜**Rust**｜最近更新 **2026-02-12T17:07:46Z**｜创建 **2026-01-22T20:25:23Z**
- 是什么：Bevy 的 AI 原生编辑器 Axiom：用自然语言（如"建 5x5 道路网格""这里放片森林"）批量生成场景，经 **BRP（Bevy Remote Protocol）** HTTP 连到正在运行的 Bevy 游戏，支持 `.glb`/贴图热上传不重启，内置 egui 界面与道路工程专门逻辑。
- **可复用性：不采用。** 依赖 Gemini API key（`GEMINI_API_KEY`），`license=null` 意味着只能读不能把代码抄进项目；Rust + Bevy + BRP 与 Ren'Py 完全不搭。仅"连到运行中的游戏、热上传素材、批量命令建场景"这条实时闭环值得记录。
- 去重核查：完整路径 **0 命中**；裸名 `bevy_ai_editor` / 标题 `Axiom` 0 命中（注意 `_r20_gh.md` 收录的是另一个 Bevy 项目 `KyosukeIshizu1008/berryscode`，非同一仓库）。

## 二、AI 开发与使用（agent harness / 上下文压缩 / 子智能体 / tool 设计）

### 7. `Context-Engine-AI/Context-Engine`

- URL：https://github.com/Context-Engine-AI/Context-Engine
- 元数据：**403 stars**｜**MIT**｜**Python**｜最近更新 **2026-07-08T23:51:56Z**｜创建 **2025-10-08T22:34:56Z**
- 是什么：给 AI 编码助手用的"语义代码检索 + 记忆 + 符号图谱"套件，以 30+ 个 MCP 工具 + 配套 Agent Skills 形式分发给 Claude Code / Cursor / Codex；topics 明确带 `ollama-api`、`qdrant`、`refrag`，定位是给长会话做上下文压缩与检索。
- **可复用性：参考。** MIT + Python 友好，且 topics 里有 Qdrant 与 Ollama API，理论上可自托管接本地向量库；但 README 首屏引导的是"到 dev.context-engine.ai 领免费账号"，技能安装路径主要围绕 Claude Code 插件市场，对 16GB Windows 自托管要先确认后端是否完全本地。先借它的"检索 + 符号图谱 + 记忆三合一"分层，不宜直接替换现有工具链。
- 去重核查：完整路径 **0 命中**；裸名 `context-engine` 在基线的 `index.html` 中有同名近似词，逐条看上下文为其它项目卡片，本仓库全名 0 命中，非重复。

### 8. `YerbaPage/Awesome-Agent-Context-Compression`

- URL：https://github.com/YerbaPage/Awesome-Agent-Context-Compression
- 元数据：**90 stars**｜**MIT**｜**无主语言（纯 Markdown）**｜最近更新 **2026-08-26T06:10:30Z**｜创建 **2026-04-30T14:18:29Z**
- 是什么：长程 Agent **上下文压缩**的综述 + 论文清单（EMNLP 2026 主会收录），按观测压缩、轨迹压缩、计划/推理压缩、记忆状态压缩、表示层压缩分类，覆盖编码/网页/研究 Agent 与多智能体。
- **可复用性：参考。** 不含可运行代码，价值在"失败模式 + 评测方法"的分类学，正好用来给索引站维护中的会话压缩策略选型、以及判断某插件（如 DSH 压缩类）属于哪一类；纯文档，零运行成本。
- 去重核查：完整路径 **0 命中**；裸名 `Agent-Context-Compression` 0 命中；与 `_r20_gh.md` 中收录的 `yoza10635/dsh-argp`（具体一个压缩插件）不是同一物。

### 9. `Prompthon-IO/agent-systems-handbook`

- URL：https://github.com/Prompthon-IO/agent-systems-handbook
- 元数据：**316 stars**｜**未声明（`license=NOASSERTION`）**｜**MDX**｜最近更新 **2026-09-24T03:12:47Z**｜创建 **2026-04-20T13:28:26Z**
- 是什么：生产级 Agent 系统手册，覆盖工作流、工具、记忆系统、上下文工程、MCP/A2A 互操作、评测、可观测性与多智能体架构，配站点 labs.prompthon.io；topics 含 `context-engineering`、`agent-memory`、`multi-agent-systems`。
- **可复用性：参考。** 是读本不是工具，无安装成本；可用来对照自建 DSH/Codex 工作流是否缺"评测/可观测"环节；`license=NOASSERTION` 意味着正文可读但复用文字/图需谨慎。
- 去重核查：完整路径 **0 命中**；裸名 `agent-systems-handbook` 0 命中。

### 10. `aldegad/skill-hook-authoring`
- URL：https://github.com/aldegad/skill-hook-authoring
- 元数据：**12 stars**｜**未声明（`license=null`）**｜**JavaScript**｜最近更新 **2026-09-18T09:13:19Z**｜创建 **2026-05-18T07:09:23Z**
- 是什么：跨 Agent 运行时的 skill/hook/plugin **单一事实源**方法论：一份包根、符号链接安装、单一注册清单、显式废弃/改名流程、机器校验的"引擎 × 目录"一致性规则；`docs/official-sources.json` 把 68 个官方 vendor 页按"运行时 × 问题"建索引，答案一律实时回官方页取、从不镜像。
- **可复用性：参考。** 直击"同一个 skill 在 DSH / Codex / Claude Code 间漂移"的痛点，对维护多 harness 工具链的人最有用；但 `license=null`，只能读思路不能抄代码，vendor 事实查询清单也需按自己使用的 harness 重做。
- 去重核查：完整路径 **0 命中**；裸名 `skill-hook-authoring` 0 命中。

## 三、VS Code 相关（AI 编码扩展 / agent 工作台 / DSH）

### 11. `warm3snow/vscode-ollama`

- URL：https://github.com/warm3snow/vscode-ollama
- 元数据：**67 stars**｜**MIT**｜**TypeScript**｜最近更新 **2026-09-01T12:20:39Z**｜创建 **2025-02-16T16:11:52Z**
- 是什么：把 Ollama 直接接进 VS Code 的扩展（上架 VS Marketplace）：本地模型聊天、可视化思维过程、保留历史，并带一个自主编码 agent，拥有 `read / write / edit / grep / find / ls / bash` 工具读写工作区，危险操作先确认；还有 `codebase-search / plan / implement / review` 内置子智能体，可串行或并行分派。
- **可复用性：落地。** 与目标场景几乎重合：本地 Ollama、VS Code、无需云端 key、MIT、TypeScript 扩展走 Marketplace 直装；最适合给"renpy 脚本 + 索引站 Python 检查脚本"配一个能读工作区、能跑 bash 的本地子智能体组。注意并行子智能体会同时压 16GB 内存，宜限制并行度、只启用 plan/implement 两个。
- 去重核查：`grep -ilF "warm3snow/vscode-ollama"` 对 5 份基线 **0 命中**；裸名 `vscode-ollama` 0 命中。

## 四、vibe coding（安全 / 验证 / 规格 / 护栏）

### 12. `pranava0x0/vibe-coding-security`

- URL：https://github.com/pranava0x0/vibe-coding-security
- 元数据：**4 stars**｜**未声明（`license=null`）**｜**Python**｜最近更新 **2026-09-23T15:27:16Z**｜创建 **2026-05-16T18:01:50Z**
- 是什么：持续更新的"vibe coding 供应链攻击事件索引"：`ALERTS.md` 一页可扫的最新告警、`advisories/` 每条含"我是否受影响"自查、`playbooks/` 凭证轮换与影响面评估、`prevention/` 攻击面图谱（npm 加固、GitHub Actions 加固、MCP 卫生、沙箱）、`sources/` 关注清单；记录了 Shai-Hulud 两代 npm 蠕虫等真实事件。
- **可复用性：落地。** 纯文档 + Python 组织，零依赖、无 key、离线可读，最新全量扫描日期 2026-09-23；最适合用来给自己定的"允许 agent 自动 `pip/npm install`"这条红线做威胁建模与加固清单。`license=null` 表示内容可读、代码/文本别直接搬进项目。
- 去重核查：完整路径 **0 命中**；裸名 `vibe-coding-security` 0 命中（注意基线里可能出现的 `vibe` 类短词假命中已用上下文排除）。

### 13. `boxed-dev/vibe-coding-security`

- URL：https://github.com/boxed-dev/vibe-coding-security
- 元数据：**15 stars**｜**未声明（`license=null`）**｜**无主语言**｜最近更新 **2026-08-09T13:48:36Z**｜创建 **2026-05-01T22:48:32Z**
- 是什么：上线前 **69 项安全检查清单**，按 Auth / Secrets / API / 数据库 / 前端 / AI-LLM / agent 工具 / 部署分组，每条对标真实事故模式（Lovable RLS CVE-2025-48757、Moltbook 泄露 150 万 token、2026-04 Lovable 平台事故），并引用 Escape.tech 对 5600 个 AI 生成应用的扫描结论（2038 个严重漏洞、400+ 泄露密钥）。
- **可复用性：参考。** 清单本身可读可用且没有运行依赖，但仓库只是清单，完整工具包（50 个审计 skill、15 份 `.cursorrules`、MCP 配置）是 **$10 付费**；`license=null`。适合当作"索引站上线前"的人工 checklist，落地检查仍要自己写脚本（Bandit / 依赖审计 / 密钥扫描）。
- 去重核查：完整路径 **0 命中**；与第 12 条是**两个不同 owner 的同名仓库**，内容形态不同（本条是静态清单、第 12 条是事件索引），不属换名重复。

## 五、DeepSeek Harness（DSH）（外壳 / 插件 / VSIX / 压缩参数）

### 14. `helloHupc/dsh-plugin-hub`

- URL：https://github.com/helloHupc/dsh-plugin-hub
- 元数据：**13 stars**｜**MIT**｜**HTML**｜最近更新 **2026-09-24T05:44:21Z**｜创建 **2026-08-15T19:36:41Z**
- 是什么：DSH 插件聚合索引站，合并 6 个数据源（GitHub `dsh-plugin` topic、`dshworks/awesome-dsh-plugins`、`kejixiaoliang/awesome-dsh-plugins`、`ZASENJC/dsh-plugins-store`、`awesome-dsh-plugin/awesome-dsh-plugin`、`0xsline/awesome-deepseek-harness`），实测去重后 **~3700+ 条**、未分类率 ~8%，每小时刷新；线上 dsh-plugin-hub.hupc.site。
- **可复用性：落地。** `python3 scripts/aggregate.py` 一键跑 ETL，`--offline` 用缓存调试，再 `python3 -m http.server` 本地预览——纯 Python + 静态页，与"维护静态索引站 + 习惯写 Python 检查脚本"的画像完全对齐，可直接抄它的多源去重/分类/每小时刷新流水线。需联网抓 GitHub API。
- 去重核查：完整路径 **0 命中**；裸名 `dsh-plugin-hub` 0 命中。

### 15. `TecFancy/dsh-auth-gate`

- URL：https://github.com/TecFancy/dsh-auth-gate
- 元数据：**15 stars**｜**MIT**｜**TypeScript**｜最近更新 **2026-09-24T05:42:26Z**｜创建 **2026-08-14T09:19:00Z**
- 是什么：给公开部署的 DSH Web 实例加"登录门"：密码或共享 token 登录、可选 TOTP 双因子，挡住未授权者访问你的 agent、会话与 LLM 凭证；npm 包发行，带 CLI、配置 skill 与 CI（Linux/Windows）。作者声明会**持续跟到 dsh 官方自带认证**为止。
- **可复用性：落地。** `npm install dsh-auth-gate`，README 明确覆盖 Windows CI，MIT；若把索引站的 DSH 暴露到局域网/公网，这是成本最低的一道门。属"官方缺位期的补丁"，升级 dsh 时要跟着升。
- 去重核查：完整路径 **0 命中**；裸名 `dsh-auth-gate` 0 命中。

### 16. `AI-Scarlett/DSH-Store`

- URL：https://github.com/AI-Scarlett/DSH-Store
- 元数据：**2 stars**｜**MIT**｜**JavaScript**｜最近更新 **2026-09-24T05:45:51Z**｜创建 **2026-08-16T04:17:02Z**
- 是什么：第三方 DSH 插件商城 + 带护栏的生命周期管理器，直接跑在 DSH 设置页内（标准 Bundle + Host Plugin + Client Bundle），不改 DSH 源码、不替换官方 `@deepseek-ai/*` 包；上架走公开 issue，Catalog 固定到完整 commit 才生成修复命令。
- **可复用性：参考。** 是"DHS 插件怎么安全装/更新/回滚"的参考实现，`registry/catalog.json` 的准入规则与"固定 commit 才出命令"的做法可借鉴到自建插件流程；但要 DSH `0.1.0-rc.7`~`0.1.5-rc.1` 特定版本 + Node `^22.19.0 || >=24`，且只有 2★，先观察再依赖。README 提醒 `ERR_PNPM_GIT_DEP_PREPARE_NOT_ALLOWED` 时**别**放开整个 Profile 的 `prepare` 权限。
- 去重核查：完整路径 **0 命中**；裸名 `DSH-Store` 0 命中。

### 17. `RYun601/dsh-launcher`

- URL：https://github.com/RYun601/dsh-launcher
- 元数据：**3 stars**｜**MIT**｜**PowerShell**｜最近更新 **2026-09-24T05:43:43Z**｜创建 **2026-08-13T14:34:59Z**
- 是什么：**Windows 专用**的 DSH Web 启动/管理工具：cmd/PowerShell 输入 `deepseek` 即可前台或后台启动（`deepseek -b`）、服务就绪后自动开带认证的浏览器、`--status` / `--stop`、一键注册命令、可指定浏览器重开；首次启动会用 npm 在 `%USERPROFILE%\dsh-launch\runtime` 准备 DSH 本体。
- **可复用性：落地。** PowerShell + Windows 10/11 原生，Node `^22.19.0 || >=24.0.0` 与上游一致，安装时统一检查 Node 版本；对"每天在 Windows 上开 dsh web 维护索引站"是最贴合的一个壳，MIT 可读改。
- 去重核查：完整路径 **0 命中**；裸名 `dsh-launcher` 0 命中（注意与 `_r20_gh.md` 的 `dsh-argp`、`deepseek-harness-for-vscode` 非同一仓库）。

### 18. `MingYU-kalo/dsh-https-fix`

- URL：https://github.com/MingYU-kalo/dsh-https-fix
- 元数据：**2 stars**｜**MIT**｜**JavaScript**｜最近更新 **2026-09-24T05:42:08Z**｜创建 **2026-08-21T19:58:44Z**
- 是什么：让 dsh Web GUI 能从外网访问：自带 HTTPS 反向代理、受信域名注册、Web 账密登录、证书管理（自签 / 自有 / 无域名用 IP）。作者自述"主要服务本人"，更新节奏不定期。
- **可复用性：不采用。** 三个高危点写在自己的 README 里：① 它给 dsh 安装目录的 `@deepseek-ai/dsh-client-connection/lib/client.js` 打**运行时热补丁**，dsh 一升级就被覆盖、装错版本会让 dsh **直接起不来**；② 必须先处理插件再升级 dsh，顺序反了就是事故；③ 默认账密 `admin/admin`，而 dsh 里的 agent 能在本机执行命令。风险远大于收益，只作"反面案例 + 证书/反代组合"的查阅。
- 去重核查：完整路径 **0 命中**；裸名 `dsh-https-fix` 0 命中。

## 六、memory 管理（长期记忆 / 记忆验证 / RAG / embedding 记忆层）

### 19. `wcatz/ghost`

- URL：https://github.com/wcatz/ghost
- 元数据：**2 stars**｜**Apache-2.0**｜**Go**｜最近更新 **2026-09-24T05:32:42Z**｜创建 **2026-03-14T10:59:06Z**
- 是什么：本地优先的 MCP 记忆 server，给 Claude Code / opencode / Cursor / Codex / Goose 等客户端共用**一份 SQLite 记忆**：存记忆、任务与决策，用 SQLite FTS5 + 可选本地 embedding 检索；Ollama 是**可选**（不装也能全文检索）；consolidation / resolution / supersession 默认 dry-run，可撤销可关闭。
- **可复用性：落地。** `go install github.com/wcatz/ghost/cmd/ghost@latest` + `ghost mcp init`；显式点名 "Ollama 可选 + 不装也能用 FTS5" 的优雅降级，对 16GB 机器最友好；单文件 SQLite 可自己审阅，"一个项目约定在一个客户端学到、下一个客户端能用"正好对应多 harness 维护索引站。需 Go 1.26+。
- 去重核查：完整路径 **0 命中**；裸名 `ghost` 是高频短词，已用 `grep -o ".\{60\}ghost.\{60\}"` 看上下文确认基线中的出现均为无关项目；全名 `wcatz/ghost` 0 命中。

### 20. `mtrnix/metronix-memory`

- URL：https://github.com/mtrnix/metronix-memory
- 元数据：**101 stars**｜**Apache-2.0**｜**Python**｜最近更新 **2026-09-23T22:02:04Z**｜创建 **2026-02-11T06:52:00Z**
- 是什么：自托管的 Agent 记忆基础设施：MCP 记忆 server + 持久化事实/偏好（按 workspace 与 agent 隔离）+ 混合检索（dense + SPLADE 稀疏 + Neo4j 图谱上下文，带来源引用）+ 可选的外部答案生成与 OpenWebUI；Docker Compose 栈自带本地模型，也可开放 REST / OpenAI-compatible 接口。
- **可复用性：参考。** 优点是"全自托管 + 带本地模型 + OpenAI-compatible 出口"；代价是硬门槛写明 **Docker ≥6GB RAM（建议 8GB）+ ~15GB 磁盘**，且要跑 Neo4j + 向量 + 稀疏三套组件——16GB Windows 同时开本地 Ollama 会很吃紧。建议只在需要"图谱式长期记忆"时按需起，别与 7B 以上本地模型常驻共存。
- 去重核查：完整路径 **0 命中**；裸名 `metronix-memory` / `metronix` 0 命中。

### 21. `jsflax/Engram`

- URL：https://github.com/jsflax/Engram
- 元数据：**6 stars**｜**未声明（`license=NOASSERTION`）**｜**Swift**｜最近更新 **2026-09-24T05:30:05Z**｜创建 **2026-02-13T18:36:25Z**
- 是什么：本地 MCP server，给编码 agent 跨会话的持久语义记忆；`curl … install.sh | bash` 下预编译二进制并自动配好 Claude Code，检测到 Codex 与 Python 3.11+ 时再注册 Codex 的 MCP 与 session learner。学习过程有一整套节流：同时只跑一个 learner、10 分钟上限、每批 ≤12 次记忆调用 / ≤5 次写入、成功区间 checkpoint、失败保留游标并退避 5 分钟。
- **可复用性：不采用（仅可借鉴节流设计）。** 主语言是 **Swift**，预编译二进制 + `install.sh` 面向 macOS 路线，对 Windows 基本不可用；`license=NOASSERTION` 也不宜抄代码。真正值得抄的是"learner 节流 + checkpoint + 失败退避 + 写回执由独立 MCP gateway 校验"这套防失控机制。
- 去重核查：完整路径 **0 命中**；裸名 `Engram` 0 命中。

## 七、模型测评与上新相关开源工具（评测 harness / 榜单复现）

### 22. `AmigaMeow/llm-leaderboard-data`

- URL：https://github.com/AmigaMeow/llm-leaderboard-data
- 元数据：**4 stars**｜**MIT**｜**Python**｜最近更新 **2026-09-24T04:15:11Z**｜创建 **2026-09-20T00:22:53Z**
- 是什么：**每日自动更新**的大模型排行榜数据仓库（GitHub Action），聚合 LMArena 人类盲测偏好 + OpenRouter 定价：收录 77 个模型（46 有 Arena 分、66 有定价、21 个开源权重、覆盖 20 家厂商），出综合榜 / 按预算选型榜 / 价格榜 / 长上下文榜；同步镜像到 Hugging Face dataset `AmigaMeow/llm-leaderboard` 可直接 `load_dataset()`。
- **可复用性：落地。** 中文 + MIT + Python，数据即文件（不用跑推理），HF 端可直接读；对"模型上新/选型"流程最省事——把榜单当数据源做 diff，比抓网页稳。注意 README 自述 **Arena 分取自 2026-09-13 LMArena 快照，上游此后未发新快照**，定价则每日抓取，看榜时要分清哪个字段是陈旧的。
- 去重核查：完整路径 **0 命中**；裸名 `llm-leaderboard-data` 0 命中。

### 23. `kmvaidya/llm-arena-vram-calc`

- URL：https://github.com/kmvaidya/llm-arena-vram-calc
- 元数据：**2 stars**｜**MIT**｜**Python**｜最近更新 **2026-09-23T10:37:27Z**｜创建 **2026-02-25T16:10:49Z**
- 是什么：把 Arena.ai 开源模型榜与**参数量 + 各精度显存估算**交叉起来，回答"我的显卡实际能跑哪个最强的模型"；给 222 个模型补参数量（已解析 171 个，77%），按 BF16 / FP8 等精度出"每张单卡能跑的最好模型"，并把 **25% 服务开销（KV cache + 激活 + 框架）** 计入。
- **可复用性：落地。** MIT + Python，纯数据加工无推理，正好回答 16GB 机器的核心问题"这个模型本机跑不跑得动"；但它的目标档位偏 H100/B200 等大卡表，用之前要自己加一档 12~16GB 消费卡（RTX 3060 12G / 4070 级），并且 README 自己标了"AA 数据可能陈旧（RSC 抓取失败用缓存）"，数字要复核。
- 去重核查：完整路径 **0 命中**；裸名 `llm-arena-vram-calc` 0 命中。

### 24. `notwitcheer/llm-bench-rig`

- URL：https://github.com/notwitcheer/llm-bench-rig
- 元数据：**40 stars**｜**未声明（`license=null`）**｜**Python**｜最近更新 **2026-09-20T09:22:37Z**｜创建 **2026-05-27T19:03:15Z**
- 是什么：GGUF + safetensors 的双引擎（llama.cpp / vLLM）评测流水线：速度侧跑 `llama-bench`（-p 128…16384 六档上下文 + tg128）与 served 流式的 TTFT / 体感 tok/s 分位；质量侧自写生成式评测器跑 MMLU / ARC-C / HellaSwag / GSM8K / HumanEval；`board_ci.py` 出 Wilson 95% 误差棒；每次运行写 provenance（llama-server build、chat template hash、gguf sha256）供回溯；带 FastAPI+SSE 实时仪表盘与排队管理器。
- **可复用性：参考。** 对"本地 Ollama/llama.cpp 选型 + 可复现地出数"很对口，`board_ci.py` 的"误差棒让相邻名次可视为平手"这条方法论尤其值得抄；但 README 明写目标是 **RTX 5090/Blackwell 级 CUDA 卡**，16GB 机器只能降配跑；且 `license=null`（只能读思路，别把代码抄进项目），另注意它**不依赖 lm-evaluation-harness**、分数是生成式判定，会和 loglikelihood 口径差几分。
- 去重核查：完整路径 **0 命中**；裸名 `llm-bench-rig` 0 命中；与已收录在 `index.html` 的 `EleutherAI/lm-evaluation-harness`（14068★）不是同一仓库，且本条明确自述不依赖后者。

### 25. `yrougy/llm-quant-bench`

- URL：https://github.com/yrougy/llm-quant-bench
- 元数据：**10 stars**｜**未声明（`license=null`）**｜**HTML**｜最近更新 **2026-09-16T18:44:22Z**｜创建 **2026-04-27T19:03:00Z**
- 是什么：专门量化"**GGUF 量化档位到底损失多少精度**"的基准：同一硬件、同一 harness、同一 prompt，只变量化级别，回答"从 Q6_K 降到 IQ2_XXS 掉多少分"；跑 BigCodeBench（单元测试）、MUSR（多选题）、BFCL 函数调用（AST 匹配，固定 1000 样本 seed 42），全部经 `inspect_ai` + llama.cpp，**无 LLM judge、完全确定性**。
- **可复用性：落地。** 这是本辑里对"16GB Windows + 本地 Ollama 该选哪个量化"最直接有用的一个：硬件就是 **2×RTX 3060 12G / GTX 1070 8G**（消费级）、用 llama.cpp `llama-server`、KV cache q4_0、上下文 16384–32768，与目标机器量级一致，方法论和评测集可直接复现。注意 `license=null`（别抄代码）、GPQA 因太慢已被作者暂缓，别指望全绿。
- 去重核查：完整路径 **0 命中**；裸名 `llm-quant-bench` 0 命中。

## 本路去重报告

### 精确命中基线后剔除（完整仓库名 grep，5 份基线：`index.html` / `csdn-social-summary.md` / `v19` / `v20` / `_r20/_r20_gh.md`）

- `banjtheman/renpy_mcp_server`（61★，TypeScript）：命中 `index.html`，索引已有项目卡片，弃。
- `Muanchen2/renpy-mcp`（22★，Python，CJK 字体自动配置）：命中 `index.html` 与 `csdn-social-summary-v20.md`，弃。
- `EleutherAI/lm-evaluation-harness`（14068★，MIT）：命中 `index.html`，弃（本辑收录的 `llm-bench-rig` / `llm-quant-bench` 是另两个独立评测实现）。
- `IvanMurzak/Godot-MCP`、`IvanMurzak/Unity-MCP`、`IvanMurzak/Unreal-MCP`：均属索引已高密度覆盖的引擎 MCP 系列，本轮只收其**共用的引擎无关宿主** `GameDev-MCP-Server`（该全名 0 命中）。

### 同主题但主动不收（控制数量 / 质量不足 / 高度重叠）

- `hybridindie/godot-mcp`（23★）、`bebabinlarsson-blip/Godot-MCP`（19★）、`nguyenchiencong/godot-mcp-cli` 之外的多个 godot-mcp 变体（`nordicnode/`、`anthonypaddison/`、`Sarmkadan/` 等，0–1★）：Godot MCP 赛道已过密，只保留"CLI 省 token"这条有区分度的 `godot-mcp-cli`。
- `beamable/bevy-ai-forge`（4★）：是 Bevy 示例工程而非通用工具，与 `cats2333/bevy_ai_editor` 重叠，弃。
- `Zagos/RPG-Maker-AI-Toolkit`（1★）：RPG Maker MZ MCP，星数太低、未见采用面，弃。
- `STAR-LAB-AI-Agent/agent-context-compression`、`SuperHelix77/HelixContext`、`saitarrun/Agentic_context_compression_framework`、`176336109/awesome-agent-context-compression`（均 0★）：上下文压缩主题下大量 0★ 同日新仓，与已收的 EMNLP 综述 `Awesome-Agent-Context-Compression` 高度重叠，弃。
- 一批 0–1★ 的 `llm-eval-harness` 同名仓库（`zaif-c/`、`aaddii09/`、`Mallika23/`、`Victor-David-Medina/`、`pxlcrtiv/pocket-eval`、`adityashah841/` 等）：多数是个人练习/课程作业模板，评测集与方法论不完整，风险是"看着像工具其实是空壳"，弃；只留下硬件与目标机同量级的 `llm-quant-bench` 与有 provenance/误差棒的 `llm-bench-rig`。
- DSH 生态 0★ 插件（`jypjypjypjyp/dsh-music-studio`、`BOWLUNA/dsh-multi-instance`、`AkinoHaruka/companion-memory`、`RockinPaul/dsh_railway_template` 等）：DSH 插件赛道每轮都刷出大量 0★ 新仓，只收有明确功能边界、MIT 且 Windows 可用的 `dsh-auth-gate` / `dsh-launcher` / `dsh-plugin-hub` / `DSH-Store`。
- `Physicolor/dsh-widgets`（5★，MIT）：功能真实、Windows 可用，但纯属 DSH 右侧栏美化/组件，对"索引站 + Ren'Py"工作流增益有限，为控数量弃。
- `GoogleCloudPlatform/db-context-enrichment`（39★，Apache-2.0）：是给 GCP AlloyDB / Cloud SQL / Spanner 的 Gemini 数据代理做 ContextSet 的 agent，**必须绑 GCP + Gemini 云服务**，与"本地 Ollama / 离线优先"约束直接冲突，弃。
- `treylom/ThisCodex`（18★，MIT）：Codex CLI + Claude Code 多智能体 Discord bot × Obsidian vault 的跨运行时 skill 包，质量够且与多 harness 场景相关，但强依赖 Discord + Obsidian 且与本地 Ollama 工作流不接，为守 25 条上限本轮弃，可下辑再看。
- `towano/memoro`（0★）、`maxswritessomecode/installornot`（0★）、`ShenSeanChen` 系列之外的 0★ 记忆/审计仓：星数与采用面不足，弃。

### 换名、同名、上游与派生核查

- 第 12 条 `pranava0x0/vibe-coding-security` 与第 13 条 `boxed-dev/vibe-coding-security` 是**不同 owner 的同名仓库**，README 自述站点标题即 "Vibe Coding · Security Issue Tracking"，两者均为 0 命中基线，内容形态不同（事件索引 vs 静态清单），不属换名重复。
- 第 4 条 `estebanrfp/defold-ai` 的 README 自述灵感来自 `hi-godot/godot-ai`；`godot-ai` 已在 `index.html`，但对 `defold-ai` 全名与裸名 `defold-ai` 的 grep 均 0 命中，且它是 Defold 引擎的独立移植，不是同名复刻。
- 第 25 条 `yrougy/llm-quant-bench` 依赖 `inspect_ai` / `llama.cpp` 上游项目，但自身为独立评测工程，全名 0 命中，不计为上游重复。
- 第 19 条裸名 `ghost` 属高频短词，已用 `grep -o ".\{60\}ghost.\{60\}"` 抽查基线上下文，命中均为无关项目卡片；`wcatz/ghost` 全名 0 命中，非假命中误判。

### 核实方式与限制

- 25 条全部由 `gh api repos/{owner}/{repo}` 实测返回 `stargazers_count / license.spdx_id / language / pushed_at / created_at`，且 `fork=false`、`archived=false`；未用搜索结果摘要代替真实性核验。
- 许可证风险清单（**只能读、不能把代码/文本抄进项目**）共 10 条：`license=null` 6 条 —— 第 6（bevy_ai_editor）、10（skill-hook-authoring）、12（pranava0x0/vibe-coding-security）、13（boxed-dev/vibe-coding-security）、24（llm-bench-rig）、25（llm-quant-bench）；`NOASSERTION`（非标准/未明确）4 条 —— 第 1（godot-mcp-pro）、4（defold-ai）、9（agent-systems-handbook）、21（Engram）。
- 可安全抄用代码（MIT / Apache-2.0）共 15 条：第 2、3、5、7、8、11、14、15、16、17、18、19、20、22、23。
- 去重基线完备性：`csdn-social-summary.md` 现为第二十一辑骨架（v2–v20 已存档），本路比对时同时扫了 `v19`、`v20` 与 `_r20/_r20_gh.md`，避免"上一辑刚收过"的重复。
