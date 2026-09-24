# 第二十三辑 GitHub 路候选（2026-09-24）

> 查重范围：`index.html`、`csdn-social-summary.md`、`csdn-social-summary-v1.md` 至 `csdn-social-summary-v22.md`；以下条目均以 `owner/repo` 小写名精确检索，未命中才保留。

### 1. Compresr-ai/Context-Gateway
- 链接：https://github.com/Compresr-ai/Context-Gateway
- ★：642（数据日期 2026-09-24）
- 一句话：放在编码 Agent 与模型 API 之间的 Go 代理，在历史真正超窗前后台预压缩，到触发点直接换入已算好的摘要。
- 为什么值得收（可扩展性 / 实用性，说人话）：它针对的是“压缩时停下来等摘要”这一处真实延迟，不绑 Claude Code、Cursor 等具体前端；仓库还有 Dockerfile、测试与发布工作流，适合拿来研究透明代理式上下文治理。
- 许可证 / 语言：Apache-2.0 / Go
- 核实情况：已核实仓库 API、README、源码目录与 GitHub Actions；README 给出安装脚本和 `context-gateway` 启动命令，但未执行远程安装脚本。

### 2. big0lives/codex-task-pointer
- 链接：https://github.com/big0lives/codex-task-pointer
- ★：234（数据日期 2026-09-24）
- 一句话：用“目标 + 下一步”的小型任务指针和 Codex hooks，让长任务跨自动压缩后重新锚定主线。
- 为什么值得收（可扩展性 / 实用性，说人话）：不是再造完整记忆库，而是用 CAS、防重复键、原子写入和压缩后重注入解决最常见的“做过又做、目标漂移”；Windows 安装器支持 `-WhatIf`、备份和回滚，适合本工作区直接借鉴。
- 许可证 / 语言：MIT / PowerShell
- 核实情况：已核实仓库 API 与 14KB README，安装前置检查、smoke、回滚路径均写明；只登记未实测，原因是安装会改用户 Codex hooks，未在本机代用户执行。

### 3. sdwolf4103/opencode-working-memory
- 链接：https://github.com/sdwolf4103/opencode-working-memory
- ★：193（数据日期 2026-09-24）
- 一句话：把 OpenCode 自带 compaction 顺手用于记忆抽取，分开维护跨会话 workspace memory 与当前会话 hot state，不额外调用模型。
- 为什么值得收（可扩展性 / 实用性，说人话）：默认只给长期记忆约 900 token / 28 条，并让热状态只在 epoch 边界刷新以保护前缀缓存；还带本地 `/memory` 查看、凭据脱敏、去重和衰减，能直接参考“记得少但记得准”的设计。
- 许可证 / 语言：MIT / TypeScript
- 核实情况：已核实仓库 API、README；`npm view opencode-working-memory` 返回可安装版本 1.6.9，未接入真实 OpenCode 会话做长期效果测试。

### 4. disler/self-compact-pi-agent
- 链接：https://github.com/disler/self-compact-pi-agent
- ★：53（数据日期 2026-09-24）
- 一句话：让 Pi Agent 看见自己的上下文用量，在软提醒、警告、硬截止三道阈值间主动写 `note_to_self` 并触发压缩。
- 为什么值得收（可扩展性 / 实用性，说人话）：硬截止后只允许调用 `self_compact`，并把 Agent 自己写的交接条原样带回新上下文，既有“预算表”也有强制动作；仓库还提供无 API 成本的脚本化端到端测试，适合验证自主长跑 Agent。
- 许可证 / 语言：MIT / HTML（核心扩展为 TypeScript）
- 核实情况：已核实仓库 API、13KB README、阈值和测试说明；只登记未实测，原因是本机未安装其要求的 Pi v0.85.1、Node 24 与 `just` 组合环境。

### 5. GlitterKill/sdl-mcp
- 链接：https://github.com/GlitterKill/sdl-mcp
- ★：488（数据日期 2026-09-24）
- 一句话：把代码仓库索引为符号图和紧凑“卡片”，再按任务切片、预算取回，而不是让 Agent 一上来读整文件。
- 为什么值得收（可扩展性 / 实用性，说人话）：符号搜索、图切片、delta pack、按需源码窗口和可选开发记忆组成了一条渐进披露链；MCP 同时支持 stdio/HTTP，适合大型仓库压缩检索面。
- 许可证 / 语言：未声明（GitHub API 为 NOASSERTION） / TypeScript
- 核实情况：已核实仓库 API、README；`npm view sdl-mcp` 返回可安装版本 0.13.7，未实际对本仓建立索引。

### 6. nguyenvuthientrang/cliffcompaction
- 链接：https://github.com/nguyenvuthientrang/cliffcompaction
- ★：34（数据日期 2026-09-24）
- 一句话：透明 API 代理在请求越过 token 阈值时，把旧历史替换成“开头原文 + 单条摘要 + 最近若干轮”。
- 为什么值得收（可扩展性 / 实用性，说人话）：Agent 无需改代码就能接入，能用 `--shadow` 只观察不改写，也能在超阈值后严格拒绝；按原始前缀链哈希匹配，适合比较代理层压缩与客户端原生压缩的得失。
- 许可证 / 语言：MIT / Python
- 核实情况：已核实仓库 API、README；`python -m pip index versions cliffcompaction` 返回 0.1.0，证明包已发布，未启动代理实测。

### 7. MarceloCaporale/codex-agent-mem
- 链接：https://github.com/MarceloCaporale/codex-agent-mem
- ★：38（数据日期 2026-09-24）
- 一句话：本地 SQLite + FTS5 的 MCP 记忆层，把目标、约束、未完事项和快照压成有预算的 context pack，按需给 Codex、Claude Code、Gemini CLI 等取回。
- 为什么值得收（可扩展性 / 实用性，说人话）：强调 pull-based、来源可追溯、只读模式、pack hash 未变短路和确定性收尾检查；README 公开多客户端验证矩阵及受控 fixture，而不是只报一句“节省 95%”。
- 许可证 / 语言：Apache-2.0 / Python
- 核实情况：已核实仓库 API 与 30KB README；PyPI 查询未找到同名包，因此不把 README 的运行说明当成“可直接 pip 安装”，只登记未实测。

### 8. ZKiteLM/pi-trace-viewer
- 链接：https://github.com/ZKiteLM/pi-trace-viewer
- ★：14（数据日期 2026-09-24）
- 一句话：给 Pi 会话做本地实时显微镜，展示分支、工具调用、压缩切点、摘要输入及真正发给模型供应商的 payload。
- 为什么值得收（可扩展性 / 实用性，说人话）：它不改 Pi 原生 session JSONL，只把观察数据写到项目内 `.pi-traces`；能把“Pi 认为的上下文”与“供应商实际收到的请求”并排看，是定位压缩丢信息和缓存失效的稀缺工具。
- 许可证 / 语言：MIT / JavaScript
- 核实情况：已核实仓库 API、README和 GitHub Release；`npm view pi-trace-viewer` 返回 0.1.0，与仓库最新 release 一致，未接真实 Pi 会话。

### 9. codecoradev/uteke
- 链接：https://github.com/codecoradev/uteke
- ★：266（数据日期 2026-09-24）
- 一句话：单 Rust 二进制的本地 Agent 记忆引擎，用 ONNX 嵌入与混合检索在 CPU 上完成存储、召回和 MCP 服务。
- 为什么值得收（可扩展性 / 实用性，说人话）：不依赖云端 LLM、Python 或外部向量库，支持带作者归属的多 Agent room、时间回溯与 Docker；仓库还提交 LongMemEval-S 复现实验，适合 16GB Windows + Ollama 的本地优先路线。
- 许可证 / 语言：Apache-2.0 / Rust
- 核实情况：已核实仓库 API、21KB README和 releases（最新公开 release 为 v0.18.1）；本机无 Cargo，未验证 README 的 `cargo install uteke-cli`，且 README 已写 v0.18.2 基准、release 尚为 v0.18.1，采用时应锁版本复核。

### 10. RamaAditya49/titen
- 链接：https://github.com/RamaAditya49/titen
- ★：16（数据日期 2026-09-24）
- 一句话：不用 API key、LLM 或默认向量服务的 Agent 记忆服务，兼容 MCP reference memory 的工具名，并给每条记忆保留来源、权限与反证。
- 为什么值得收（可扩展性 / 实用性，说人话）：它把检索内容明确标为不可信上下文，支持审计 JSON/JSONL/Mem0 导出，并公开“库从单实例扩大到近两万会话后 recall@1 明显下降”的负结果，比只展示最好分数更可信。
- 许可证 / 语言：Apache-2.0 / TypeScript
- 核实情况：已核实仓库 API、43KB README与 release；`npm view titen-memory` 返回 0.10.0，可用 `npx titen-memory mcp`，未连接 MCP 客户端实测。

### 11. OnlyTerp/prompt-cache-skills
- 链接：https://github.com/OnlyTerp/prompt-cache-skills
- ★：114（数据日期 2026-09-24）
- 一句话：逐个审计编码 Agent harness 的请求组装方式，并提供可移植技能来修复缓存断点、动态时间戳和缺失 cache key。
- 为什么值得收（可扩展性 / 实用性，说人话）：它区分“已证实工作、需要修、闭源无法验证”，还指出 Claude Desktop/Codex CLI 等无需乱补；对 Aider、Cline、Continue、OpenCode 的修复能直接映射到“稳定前缀放前、动态块放后”的房规。
- 许可证 / 语言：未声明（GitHub API 为 NOASSERTION） / Python
- 核实情况：已核实仓库 API、15KB README和 CI；README 标注 13 份已完成审计及 6 个待办 stub，未运行其会产生真实模型费用的双请求缓存探针。

### 12. Just-Agent/make-agents-cheaper
- 链接：https://github.com/Just-Agent/make-agents-cheaper
- ★：23（数据日期 2026-09-24）
- 一句话：用 Rust CLI 审计 Codex 的提示层、工具 schema 与缓存断点，对比普通配置和 cache-friendly 配置的实际账单输入。
- 为什么值得收（可扩展性 / 实用性，说人话）：核心立场不是“删上下文”，而是让重复前缀逐字稳定并维持同会话路由；它同时保留质量门和分段统计，可避免只追缓存命中率却把任务做差。
- 许可证 / 语言：MIT / Rust
- 核实情况：已核实仓库 API 与 28KB README；本机没有 Cargo，无法验证安装，仓库也没有公开 GitHub release，因此只登记未实测。

### 13. lllq-123/claude-code-cache-keepalive
- 链接：https://github.com/lllq-123/claude-code-cache-keepalive
- ★：12（数据日期 2026-09-24）
- 一句话：一份带实测读数的 Claude Code 长会话缓存保活手册，说明哪些操作会让 cache read 归零，以及如何在 TTL 前低成本续命。
- 为什么值得收（可扩展性 / 实用性，说人话）：最有用的是提醒“看 usage 时间序列，不看单点”，并记录改 skill 文件后延迟爆缓存、`/compact` 重建前缀、headless resume 的计数陷阱；适合直接补充提示缓存观测规则。
- 许可证 / 语言：MIT / 文档型仓库（GitHub 未识别主语言）
- 核实情况：已核实仓库 API 与 20KB README；只登记未实测，因为验证需要真实 Claude Code 会话和计费 usage，且 README 明确提示版本升级后必须重测。

### 14. dean0x/skim
- 链接：https://github.com/dean0x/skim
- ★：30（数据日期 2026-09-24）
- 一句话：用 AST 理解代码结构，并压缩测试、构建、git diff 与命令输出的 Rust 上下文优化器。
- 为什么值得收（可扩展性 / 实用性，说人话）：支持 18 种语言、token budget cascading、AST-aware diff 和 Agent hook 命令改写；README 同时坦白管道与并发 sidecar 仍有两个洞，适合“先安全降噪、字节敏感命令强制透传”的实践。
- 许可证 / 语言：MIT / Rust
- 核实情况：已核实仓库 API、29KB README、CI 和 v2.10.0 release；`npm view rskim` 同样返回 2.10.0，证明 npm 路径可安装，未在本仓启用自动命令重写。

### 15. codeus-morbid/contextmaxxer
- 链接：https://github.com/codeus-morbid/contextmaxxer
- ★：5（数据日期 2026-09-24）
- 一句话：本地 Go MCP 检索器用小型编码器、符号关系与明确 token budget 返回带行号的代码证据。
- 为什么值得收（可扩展性 / 实用性，说人话）：它把首次检索、展开单个结果和继续分页拆成三个工具，避免一次塞满；还用 SWE-Explore 的公开问题做了可复核对照，并明确承认基础上下文可能盖过检索省下的 token。
- 许可证 / 语言：MIT / Go
- 核实情况：已核实仓库 API、23KB README、CI 与 v0.1.1 release；README 有 Windows 等平台安装说明，但未下载约 161M 参数模型并跑本仓 warmup。

### 16. WeiYe6/dsh-session-handoff
- 链接：https://github.com/WeiYe6/dsh-session-handoff
- ★：4（数据日期 2026-09-24）
- 一句话：`/handoff` 让 LLM 总结 DSH 当前会话，创建同工作区的新 session + agent，注入交接文档后自动打开。
- 为什么值得收（可扩展性 / 实用性，说人话）：原会话不改、模型路由与工作区继承、使用 DSH 公开服务且不改 core；22 个测试覆盖 host/client 逻辑，是研究 DSH 跨会话延续的最小样本。
- 许可证 / 语言：MIT / JavaScript
- 核实情况：已核实仓库 API、README 与 CI；npm 公共注册表未找到包，README 要求本地 `npm pack` 后以 tgz 加到 web profile，因此只登记未实测。

### 17. liangmianya/dsh-synapse
- 链接：https://github.com/liangmianya/dsh-synapse
- ★：419（数据日期 2026-09-24）
- 一句话：把同一工作区的 DSH 会话、追问与 fork 投影成可拖拽缩放的地图，并保持原生 session log 为唯一事实源。
- 为什么值得收（可扩展性 / 实用性，说人话）：地图只保存布局，删 `$DSH_HOME/synapse/` 不伤会话；从画布切回对话仍是同一个 DSH session，很适合从“线性聊天”升级为可视化分支导航而不另造历史库。
- 许可证 / 语言：MIT / JavaScript
- 核实情况：已核实仓库 API、README、主分支测试与发布工作流；`npm view dsh-synapse` 返回 0.4.1，未在本机 DSH web profile 安装。

### 18. AdamPlatin123/dsh-plugin-radar
- 链接：https://github.com/AdamPlatin123/dsh-plugin-radar
- ★：1467（数据日期 2026-09-24）
- 一句话：持续发现 DSH 插件、检查包结构，再用隔离运行环境做兼容性实测并每 15 分钟输出快照的生态雷达。
- 为什么值得收（可扩展性 / 实用性，说人话）：它不是又一份手工 awesome 清单，而是把候选发现、克隆验证、runtime test、可追溯状态与 JSON 下游接口连成流水线；README 当日快照标注 1345 个确认插件、13556 次测试，能降低“README 写了但装不上”的筛选成本。
- 许可证 / 语言：MIT / Python
- 核实情况：已核实仓库 API、36KB README及 2026-09-24 当日自动快照说明；只登记未复跑其 Kubernetes 验证管线，具体插件仍应按测试日期复核。

### 19. tintinweb/vscode-pi-model-chat-provider
- 链接：https://github.com/tintinweb/vscode-pi-model-chat-provider
- ★：16（数据日期 2026-09-24）
- 一句话：把 Pi coding agent 的模型注册进 VS Code `vscode.lm.*` 模型选择器，供 Copilot Chat 和其他扩展复用。
- 为什么值得收（可扩展性 / 实用性，说人话）：它利用 VS Code 标准 Language Model Chat Provider 接口，而不是给每个扩展单独写接入；会话池会跨轮复用并清理空闲实例，适合观察 Copilot 界面与自定义模型后端的解耦方式。
- 许可证 / 语言：MIT / TypeScript
- 核实情况：已核实仓库 API、README和 v0.2.1 release；README 给出 VS Marketplace 安装及本地 `npm run compile`，未在 VS Code 实机加载。

### 20. PIsberg/vibetags
- 链接：https://github.com/PIsberg/vibetags
- ★：23（数据日期 2026-09-24）
- 一句话：用 Java 源码注解生成 Claude、Cursor、Copilot 等多平台 Agent 护栏文件，并在编译或 CI 中检测规则漂移。
- 为什么值得收（可扩展性 / 实用性，说人话）：规则跟着类和方法移动，安全类护栏常驻、普通细节按路径作用域加载，避免一个巨型 AGENTS.md 永久占上下文；`@AILocked` 还能让 GitHub Action 阻止 Agent 改动关键代码。
- 许可证 / 语言：MIT / Java
- 核实情况：已核实仓库 API、64KB README、v1.3.6 release及完整 CI/CodeQL/fuzz/发布工作流；未新建 Java 消费项目验证注解处理器。

### 21. roboco-io/vibe-ready-cli
- 链接：https://github.com/roboco-io/vibe-ready-cli
- ★：3（数据日期 2026-09-24）
- 一句话：让 Claude Agent SDK 或 Codex CLI 只读巡检仓库，从文档、测试、CI、提交习惯等 7 类指标评估“适不适合交给编码 Agent”。
- 为什么值得收（可扩展性 / 实用性，说人话）：不只输出总分，还把 must-have、nice-to-have、optional 分层，并预提取提交日志证据；适合在大规模 vibe coding 前先找出缺测试、缺规范、缺小步提交这些基础问题。
- 许可证 / 语言：MIT / TypeScript
- 核实情况：已核实仓库 API、README、CI 与 v0.6.0 release；`npm view vibe-ready` 返回 0.6.0，未让其调用本机 Claude/Codex 做付费扫描。

### 22. EricSun0218/OpenGameAgent
- 链接：https://github.com/EricSun0218/OpenGameAgent
- ★：50（数据日期 2026-09-24）
- 一句话：面向游戏内 NPC 的 C# Agent runtime，用结构化上下文、ReAct 工具循环、持久计划和游戏侧授权动作连接 Unity、Godot、Unreal 或 .NET 服务。
- 为什么值得收（可扩展性 / 实用性，说人话）：它明确“不是游戏生成器”，模型不能直接改游戏状态，所有 mutation 都经游戏自有工具校验；支持本地 OpenAI-compatible 端点、记忆扩展和多 NPC 调度，适合做可控 AI NPC 的中间层。
- 许可证 / 语言：MIT / C#
- 核实情况：已核实仓库 API、26KB README、CI 和 OpenUPM 发布工作流；公开 release 为 v0.3.0-alpha.2，而 README 主分支已写到 alpha.4，属于 pre-1.0，未接入引擎实测。

### 23. praydog/re-engine-mcp
- 链接：https://github.com/praydog/re-engine-mcp
- ★：34（数据日期 2026-09-24）
- 一句话：借 REFramework.NET 把运行中的 Resident Evil、Monster Hunter、DMC 等 RE Engine 游戏对象、日志与热重载暴露为 MCP 工具。
- 为什么值得收（可扩展性 / 实用性，说人话）：Agent 不只读资源文件，而能在活游戏里查对象图、读写字段、调方法、编译插件、看错误再修；50+ 工具和同一套跨游戏核心 explorer，使“AI 辅助 Modding”形成真实闭环。
- 许可证 / 语言：MIT / C#
- 核实情况：已核实仓库 API、18KB README与 CI；没有公开 GitHub release，且依赖 REFramework nightly、对应 C# API 与 .NET 10，故只登记未实测。

### 24. lebek/modmixer
- 链接：https://github.com/lebek/modmixer
- ★：21（数据日期 2026-09-24）
- 一句话：面向 RimWorld 的桌面 AI Mod 工作台，可在对话中改 XML/C#、管理素材、启动游戏、盯日志并辅助发布到 Steam Workshop。
- 为什么值得收（可扩展性 / 实用性，说人话）：它把“写 Mod—启动游戏—玩家验收—看报错—修复—上架”串成一条用户能理解的流程，价值在发行闭环而不是单次生成代码；README 也明确最后的玩法测试必须由人完成。
- 许可证 / 语言：MIT / TypeScript
- 核实情况：已核实仓库 API、README、CI 和 v0.10.5 release；安装入口为项目官网构建包，未在本机安装，也未连接 RimWorld 与模型账号。

### 25. alex-jordan547/renforge-mcp
- 链接：https://github.com/alex-jordan547/renforge-mcp
- ★：10（数据日期 2026-09-24）
- 一句话：Ren'Py 的 MCP + CLI + Web 控制台，可检查项目、启动游戏、看截图/场景树、点击运行界面并把可编辑布局保存回源码。
- 为什么值得收（可扩展性 / 实用性，说人话）：和只生成 `.rpy` 的方案不同，它补齐“运行—观察—操作—验证—停机”回路；每个工具显式传 `project_path`，还能管理翻译统计，对独立视觉小说制作更落地。
- 许可证 / 语言：MIT / Python
- 核实情况：已核实仓库 API、README、CI/live-editor 测试与 v0.7.2 release；`python -m pip index versions renforge` 返回 0.7.2 等版本，未启动 Ren'Py 项目实测。

### 26. DJ-Huang/PCG-AI
- 链接：https://github.com/DJ-Huang/PCG-AI
- ★：9（数据日期 2026-09-24）
- 一句话：用可编辑 `.pcg` 图作为程序化资产真相源，让人或 MCP Agent 共同搭节点、校验、cook、截图并导出游戏资产。
- 为什么值得收（可扩展性 / 实用性，说人话）：Web 编辑器和 Unity 集成已可用，同一图保留参数、seed 与几何步骤，生成后还能量化和重做；它把 AI 生成从“一次性网格”变成可复现资产管线。
- 许可证 / 语言：Apache-2.0 / C++
- 核实情况：已核实仓库 API、14KB README、源码体量与现有 workflow；README 明确 Unreal/Godot/Blender/Three.js 仍是计划项，只按“Web + Unity 当前可用”登记，未本机构建 340MB 仓库。

### 27. MRCalderon3D/everything-game-dev-code
- 链接：https://github.com/MRCalderon3D/everything-game-dev-code
- ★：86（数据日期 2026-09-24）
- 一句话：覆盖 Unity、Unreal、Godot 与 Web 的 AI 游戏开发脚手架，把角色 Agent、命令、技能、规则、MCP 配置和质量门放进同一工程结构。
- 为什么值得收（可扩展性 / 实用性，说人话）：支持多种编码 harness，但用 engine profile 隔离各引擎规则；带 doctor、pre-commit 结构校验、13 个一次生成的 HTML 游戏样例及从 GDD 到 release 的命令，便于检查“全工作室”方案是否真有闭环。
- 许可证 / 语言：MIT / JavaScript
- 核实情况：已核实仓库 API、README、源码目录与 CI；未执行其安装脚本，也未复跑样例游戏，只登记结构与可复核资产。

### 28. buyun00/Seed-GameDev-Harness
- 链接：https://github.com/buyun00/Seed-GameDev-Harness
- ★：17（数据日期 2026-09-24）
- 一句话：面向 Unity/Godot/Unreal/Cocos 的 Claude Code 插件，按任务类型、领域和复杂度动态组装原生 Agent Team，并跨 session 维护项目记忆。
- 为什么值得收（可扩展性 / 实用性，说人话）：不自建编排进程，而是复用 Claude Code 的 Team/Task/SendMessage；同时提供 Constitution、Auto Memory、Project Knowledge 三层记忆和 Web 编辑器，是“游戏专用 harness + context 管理”的交叉样本。
- 许可证 / 语言：未声明（GitHub API 无 license） / TypeScript
- 核实情况：已核实仓库 API、16KB README、源码目录与 release；README 说明安装后无需 `npm install`，但会写 Claude 配置并启用实验性 Agent Teams，未在本机代用户安装。

### 29. Purewhiter/mobilegym
- 链接：https://github.com/Purewhiter/mobilegym
- ★：799（数据日期 2026-09-24）
- 一句话：在浏览器里并行模拟手机应用，用结构化状态和代码级 judge 对 GUI Agent 做可验证评测与在线强化学习。
- 为什么值得收（可扩展性 / 实用性，说人话）：包含 28 个应用、416 个参数化任务模板，单实例约 400MB RAM / 50MB 磁盘，README 报告 256 并发任务约 6 分钟；新 app、task、agent、judge 都走模块清单扩展，比不可复现的真机点击榜单更适合作回归测试。
- 许可证 / 语言：Apache-2.0 / Python
- 核实情况：已核实仓库 API、33KB README、数据 release 与 EMNLP 2026 Main 接收说明；未下载约 1.9GB companion dataset、未复跑排行榜，性能数字仅按仓库公开口径登记。

### 30. sleeepeer/PIArena
- 链接：https://github.com/sleeepeer/PIArena
- ★：52（数据日期 2026-09-24）
- 一句话：统一运行提示注入攻击与防御评测的 ACL 2026 工具箱，并把 AgentDojo、AgentDyn、InjecAgent 接到同一实验入口。
- 为什么值得收（可扩展性 / 实用性，说人话）：可以自定义攻击、防御和数据集，又能在 workspace、slack、travel、shopping、github 等 Agent 场景中比较防护效果；对工具调用 Agent 做上线前安全回归比单看普通问答 benchmark 更实际。
- 许可证 / 语言：MIT / Python
- 核实情况：已核实仓库 API、README、源码/数据/runner 目录与 GitHub Pages workflow；未下载模型和数据集跑完整评测，只登记可复现实验入口。

## 自查

- 共保留 30 条；每条都以 `owner/repo` 小写名在 `index.html` 与 `csdn-social-summary*.md` 精确查重，均未命中。
- 已剔除 25 条重复，明细：`ccompactor/ccompactor`、`Clearailhc/clearai-dsh`、`Muanchen2/renpy-mcp`、`fracturedring/renpy-mcp`、`tigerless-labs/agent-memory`、`FunplayAI/funplay-unity-mcp`、`hi-godot/godot-ai`、`255308153/CtxGuard`、`handyutils/sctxx`、`DezFix/OctopusBridge`、`Drhushi/dsh-plugin-tav2`、`solis-team/XRepoTest`、`gamedev-skills/awesome-gamedev-agent-skills`、`Donchitos/Claude-Code-Game-Studios`、`Coding-Solo/godot-mcp`、`CoplayDev/unity-mcp`、`IvanMurzak/Unity-MCP`、`Natfii/UnrealClaude`、`CoderGamester/mcp-unity`、`tomyud1/godot-mcp`、`Erodenn/godot-mcp-runtime`、`hatayama/unity-cli-loop`、`IvanMurzak/Godot-MCP`、`rouges78/GameStringer`、`fennaraOfficial/fennara-godot-ai`。
- 0★ 空壳、README 只有一句和纯 fork 未纳入；最低星条目为 3★，但已有完整 README、源码结构、CI/release 或可查询安装包。
- 可顺手核实的安装渠道已查：npm（`opencode-working-memory`、`sdl-mcp`、`titen-memory`、`pi-trace-viewer`、`dsh-synapse`、`vibe-ready`、`rskim`）、PyPI（`cliffcompaction`、`renforge`）；`codex-agent-mem` 在 PyPI 无同名包，已明确降级为“只登记未实测”。
