# 第 20 轮 GitHub / Hugging Face 新项目调研（GitHub 路）

> 核查时间：2026-09-24（仓库元数据来自 GitHub API；`updated_at` 以 UTC 记录）  
> 去重基线：`index.html`、`csdn-social-summary.md`、`csdn-social-summary-v18.md`。  
> 筛选原则：非 fork、非归档、非 0★ 空壳；逐项执行仓库全名的大小写不敏感精确 grep，并额外搜索裸项目名及已发现的旧 owner / 上游名，排查换名重复。

## 一、游戏制作与扩展

### 1. `KyosukeIshizu1008/berryscode`

- URL：https://github.com/KyosukeIshizu1008/berryscode
- 元数据：**145 stars**｜**MIT**｜**Rust**｜最近更新 **2026-09-14T00:01:46Z**
- 是什么：专为 Bevy 构建的原生 IDE，集成场景编辑、ECS Inspector、System Graph、测试运行器，以及可接 Ollama 的本地 AI 助手，解决“通用代码编辑器看不懂游戏引擎状态”的问题。
- **可拓展性：参考。** 编辑器内“场景状态 + ECS + 本地模型”的交互范式值得借鉴，但主体是 Bevy/Rust，不可直接接入 Ren'Py；README 推荐的 Llama 3.3 未给 16GB 友好的量化配置，实用时应换更小 Ollama 模型。
- 去重核查：`grep -iF "KyosukeIshizu1008/berryscode" index.html csdn-social-summary.md csdn-social-summary-v18.md` **0 命中**；裸名 `berryscode` **0 命中**。

### 2. `chrisgliddon/bevy-skills`

- URL：https://github.com/chrisgliddon/bevy-skills
- 元数据：**15 stars**｜**MIT**｜**Python**｜最近更新 **2026-09-21T22:42:53Z**
- 是什么：面向 Bevy 0.19 的可移植 Agent Skills，覆盖 ECS、资源、物理、音频、存档、测试、性能与迁移，并用配套测试仓库编译校验 Rust 示例。
- **可拓展性：参考。** 引擎知识拆成小技能、每段示例都编译验证的做法可迁移到 Ren'Py 技能库和索引维护流程；技能正文则是 Bevy 专用。
- 去重核查：`grep -iF "chrisgliddon/bevy-skills" ...` **0 命中**；裸名 `bevy-skills` **0 命中**。

### 3. `ukanwat/selfstarter`

- URL：https://github.com/ukanwat/selfstarter
- 元数据：**386 stars**｜**MIT**｜**Shell**｜最近更新 **2026-09-23T14:58:26Z**
- 是什么：把“明确 brief + 预算 + 完成条件”交给编码 Agent，让它跨多个会话自行规划、记录状态并运行；仓库附有 Agent 独立驱动 Unreal Engine 5 制作开放世界城市的可复现实验。
- **可拓展性：不采用。** 跨会话 brief、状态报告和无人工提示的验收规则很有研究价值，但当前样例绑定 UE5/MCP，仓库体积约 405 MB，16GB Windows 做 Ren'Py 小游戏没必要承担这套运行负担。
- 去重核查：`grep -iF "ukanwat/selfstarter" ...` **0 命中**；裸名 `selfstarter` **0 命中**。

### 4. `indiesoftby/defold-agent-config`

- URL：https://github.com/indiesoftby/defold-agent-config
- 元数据：**95 stars**｜**未声明（GitHub API `license=null`）**｜**Python**｜最近更新 **2026-09-18T02:21:42Z**
- 是什么：Defold 的 `AGENTS.md` 与技能配置样板，可把依赖源码/API 下载到只读 `.deps/`，支持 Claude Code、Copilot、Windsurf、Trae、CodeBuddy，并明确建议单任务会话与 65% 上下文上限。
- **可拓展性：参考。** Python 3.11、Windows 和通用 Agent 目录结构都容易复用；可借鉴“依赖文档 JIT 拉取 + 只读上下文 + 会话水位线”，但技能内容需改写为 Ren'Py/Python。
- 去重核查：`grep -iF "indiesoftby/defold-agent-config" ...` **0 命中**；裸名 `defold-agent-config` 与标题 `Defold AI Agent Configuration` 均 **0 命中**。

### 5. `striderZA/OpenCodeGameStudios`

- URL：https://github.com/striderZA/OpenCodeGameStudios
- 元数据：**88 stars**｜**MIT**｜**JavaScript**｜最近更新 **2026-09-15T19:47:41Z**
- 是什么：面向 OpenCode / Pi 的模块化游戏制作 Agent 工作室，含 52 个角色、22 个可选模块、158 项测试及 Godot/Unity/Unreal/Bevy 等引擎包，解决大而全提示词无法按项目按需装载的问题。
- **可拓展性：参考。** `core + design + qa + engine-*` 的按需安装方式适合改造成 Ren'Py 小团队工作流；但 52 Agent 对 16GB 本地模型过重，应只抽取策划、叙事、实现、QA 四类最小闭环。
- 去重核查：`grep -iF "striderZA/OpenCodeGameStudios" ...` **0 命中**；裸名与标题 `OpenCode Game Studios` 均 **0 命中**。

### 6. `alex-jordan547/renforge-mcp`

- URL：https://github.com/alex-jordan547/renforge-mcp
- 元数据：**10 stars**｜**MIT**｜**Python**｜最近更新 **2026-09-13T15:35:49Z**
- 是什么：直接服务 Ren'Py 的 MCP server、CLI 与 Web dashboard，可检查、驱动、调试运行中的视觉小说，轮询事件、抓帧供模型查看，并提供 Live Editor。
- **可拓展性：落地。** 与目标场景直接匹配；Python 3.11 + `uv/uvx` 即可，README 称可复用已发现或缓存的 Ren'Py SDK，且有 Windows PATH 指南，16GB 机器可先用 slim MCP/CLI 版本接现有 Agent。
- 去重核查：`grep -iF "alex-jordan547/renforge-mcp" ...` **0 命中**；裸名 `renforge-mcp` 与标题 `RenForge` 均 **0 命中**。

### 7. `hatayama/unity-cli-loop`

- URL：https://github.com/hatayama/unity-cli-loop
- 元数据：**568 stars**｜**MIT**｜**C#**｜最近更新 **2026-09-23T15:17:38Z**
- 是什么：让 Agent 从 CLI 驱动 Unity 2022.3+ 的编译、测试、日志、场景编辑、截图、输入回放、断点与热更新，形成从编辑到 Play Mode 的闭环。
- **可拓展性：参考。** Unity 包本身不适合 Ren'Py，但“最少工具覆盖编译—运行—截图—交互—验证”的闸门设计可直接映射成 Ren'Py launch/lint/screenshot/smoke 技能；Windows Git Bash/PowerShell 均有安装路径。
- 去重核查：`grep -iF "hatayama/unity-cli-loop" ...` **0 命中**；裸名与标题 `Unity CLI Loop` 均 **0 命中**。

### 8. `godot-fun/gai`

- URL：https://github.com/godot-fun/gai
- 元数据：**170 stars**｜**MIT**｜**GDScript**｜最近更新 **2026-09-23T15:46:21Z**
- 是什么：Godot 的 Agent CLI/GUI、跨 Harness 技能集合与轻量游戏框架，提供音频、图片、视频、分镜批处理及单元/集成测试等制作和发行辅助能力。
- **可拓展性：参考。** 媒体批处理技能、不可覆盖源文件约束、测试约定适合移植到 Ren'Py 素材管线；`zfoo/` 框架和 GDScript 代码不能直接复用。
- 去重核查：`grep -iF "godot-fun/gai" ...` **0 命中**；完整仓库名已覆盖裸名检查，三个基线文件均无结果。

## 二、Agent Harness、上下文与长期记忆

### 9. `coddy-project/coddy-agent`

- URL：https://github.com/coddy-project/coddy-agent
- 元数据：**154 stars**｜**MIT**｜**Go**｜最近更新 **2026-09-23T16:10:09Z**
- 是什么：单一静态 Go 二进制 Agent Harness，统一 TUI、ACP、Web/API、定时任务和多节点入口，内置技能、子 Agent、MCP、后台任务、上下文压缩、长期记忆和项目可信门。
- **可拓展性：落地。** 发布 Windows 二进制且支持 Ollama/llama.cpp/OpenAI-compatible；16GB 机器可选小模型，把索引站更新设成定时任务、把 Ren'Py lint/build 设为技能，同时用项目可信门阻止仓库自带 hook/MCP 自动执行。
- 去重核查：`grep -iF "coddy-project/coddy-agent" ...` **0 命中**；README 残留旧 badge owner `EvilFreelancer/coddy-agent`，对该旧路径追加 grep 亦 **0 命中**，不是换名重复收录。

### 10. `rossoctl/context-guru`

- URL：https://github.com/rossoctl/context-guru
- 元数据：**56 stars**｜**Apache-2.0**｜**Go**｜最近更新 **2026-09-23T15:47:53Z**
- 是什么：Provider-agnostic 上下文工程代理/代理层，通过少携带上下文、检索对话轨迹、压缩与摘要来降低 token、延迟和成本，并提供状态与统计观察面。
- **可拓展性：参考。** “上下文预算可观测 + 预设裁剪策略”的方法适合长期索引维护；现成安装路径偏 Claude Code 插件/组织代理，对本地 Ollama 与现用 Harness 需要额外适配，先借设计不直接替换工具链。
- 去重核查：`grep -iF "rossoctl/context-guru" ...` **0 命中**；裸名 `context-guru` **0 命中**。

### 11. `dcellison/kai`

- URL：https://github.com/dcellison/kai
- 元数据：**36 stars**｜**Apache-2.0**｜**Python**｜最近更新 **2026-09-23T16:30:45Z**
- 是什么：本机常驻的持久编码 Agent 工作台，以 SQLite append-only event log 保存会话/任务/记忆，支持多用户隔离、定时任务、GitHub 自动化和 Claude/Codex/Goose/OpenCode/Pi 等后端。
- **可拓展性：参考。** 可经 Goose/OpenCode 等后端接 Ollama，持久项目记忆与定时刷新索引很契合；但它是常驻多服务工作台，个人 16GB 机器应先只启用一个后端和一个 Agent，避免与本地模型争内存。
- 去重核查：`grep -iF "dcellison/kai" ...` **0 命中**；裸名检查亦无对应项目卡片。

### 12. `unbound-force/dewey`

- URL：https://github.com/unbound-force/dewey
- 元数据：**3 stars**｜**MIT**｜**Go**｜最近更新 **2026-09-23T16:29:47Z**
- 是什么：面向 Logseq/Obsidian 与代码库的知识图谱 MCP，支持 Markdown 读写、全文/语义检索、决策跟踪、GitHub/网页/源码索引和 Ollama 本地向量化。
- **可拓展性：落地。** 本地 Markdown + SQLite/Ollama 很适合把 1112 项索引、调研笔记和项目决策做可检索记忆；Windows 可 `go install`（需 Go 1.25+），16GB 足以运行 Go 服务与小型嵌入模型。
- 去重核查：`grep -iF "unbound-force/dewey" ...` 与裸名 `dewey` 均 **0 命中**；README 声明它是 `graphthulhu` 的 hard fork，但加入 SQLite、Ollama、多源索引和信任分级，且上游名 `graphthulhu` 在三份基线也 **0 命中**，不是已收录项目的纯复刻。

### 13. `mnemoverse/mcp-memory-server`

- URL：https://github.com/mnemoverse/mcp-memory-server
- 元数据：**25 stars**｜**MIT**｜**TypeScript**｜最近更新 **2026-09-23T16:30:58Z**
- 是什么：跨 Claude Code、Cursor、VS Code、ChatGPT 的持久记忆 MCP；用户可反馈某条召回“有帮助/误导”，系统据结果更新排序，并用共享房间支持多 Agent 协作。
- **可拓展性：不采用。** “错误记忆负反馈”是值得吸收的设计，但开源仓库只是客户端/MCP server，核心记忆引擎默认托管，自托管仅 Enterprise，和本地 Ollama/本地资料优先约束冲突。
- 去重核查：`grep -iF "mnemoverse/mcp-memory-server" ...` **0 命中**；裸名及标题 `Mnemoverse Memory` 均 **0 命中**。

### 14. `gary23w/nl-veil`

- URL：https://github.com/gary23w/nl-veil
- 元数据：**204 stars**｜**MIT**｜**Zig**｜最近更新 **2026-09-23T16:03:59Z**
- 是什么：Windows/macOS/Linux 桌面编码 Agent，可并行分派专家、保留跨会话项目记忆，并选择内置模型、Ollama 或 OpenAI-compatible endpoint。
- **可拓展性：落地。** Windows 原生应用和 Ollama 路径吻合，适合把“检索项目—改脚本—跑测试—记住命令”拆给多个 Agent；内置 12B 模型可能挤占 16GB，宜改用已装的小量化 Ollama 模型，并限制并行度。
- 去重核查：`grep -iF "gary23w/nl-veil" ...` **0 命中**；裸名 `nl-veil` 与标题 `the veil` 均 **0 命中**。

### 15. `ShenSeanChen/waku-agent`

- URL：https://github.com/ShenSeanChen/waku-agent
- 元数据：**1825 stars**｜**MIT**｜**Python**｜最近更新 **2026-09-23T13:35:21Z**
- 是什么：刻意保持可读、可改的本地优先 Agent 教学/生产骨架，把 loop、语义/情节/程序性记忆、检索门、确定性测试、LLM-as-judge 和发布闸门放在一个 Python 项目中。
- **可拓展性：落地。** 记忆是单个本地 SQLite，`pip install waku-agent` 即可运行；非常适合作为 Ren'Py/索引维护 Agent 的透明骨架，但官方列出的 provider 偏云端，若接 Ollama 应先验证 OpenAI-compatible adapter 或补一个很薄的 adapter。
- 去重核查：`grep -iF "ShenSeanChen/waku-agent" ...` **0 命中**；裸名 `waku-agent` 与 `Waku` **0 命中**。

## 三、VS Code / DeepSeek Harness / 上下文编排

### 16. `skymecode/deepseek-harness-for-vscode`

- URL：https://github.com/skymecode/deepseek-harness-for-vscode
- 元数据：**148 stars**｜**MIT**｜**TypeScript**｜最近更新 **2026-09-22T17:08:21Z**
- 是什么：把 DeepSeek Harness 做成原生 VS Code 工作台，内置经过兼容测试的 runtime，支持会话持久化/分叉/归档/导入导出、文件上下文卡、模型与推理控制和插件中心。
- **可拓展性：落地。** 有平台 VSIX、简体中文、Windows 历史目录说明，无需另装 DSH；可直接用于 Ren'Py 脚本与索引站，但共享会话日志时必须遵守 V4 格式和单写者锁，先备份再切换官方 CLI/扩展。
- 去重核查：`grep -iF "skymecode/deepseek-harness-for-vscode" ...` **0 命中**；裸名 `deepseek-harness-for-vscode` **0 命中**。

### 17. `NERDSORG/Mutsumi`

- URL：https://github.com/NERDSORG/Mutsumi
- 元数据：**20 stars**｜**Apache-2.0**｜**TypeScript**｜最近更新 **2026-09-17T23:59:21Z**
- 是什么：强调人在回路、上下文全控制和可审计性的 VS Code 多 Agent 扩展；以 notebook 保存纯文本会话，支持父子 Agent、上下文预览、文件版本/hash 跟踪与过期引用裁剪。
- **可拓展性：参考。** “工具结果预执行成 ghost block、未变文件只引用历史、变更后再注入”的 JIT 上下文方案很适合大型 `index.html`，但扩展仍较新，先借上下文装配逻辑，不宜立刻替换成熟编辑器工作流。
- 去重核查：`grep -iF "NERDSORG/Mutsumi" ...` **0 命中**；裸名 `Mutsumi` 和 README 旧 badge owner `MalachiteN/Mutsumi` 均 **0 命中**。

### 18. `yoza10635/dsh-argp`

- URL：https://github.com/yoza10635/dsh-argp
- 元数据：**9 stars**｜**MIT**｜**TypeScript**｜最近更新 **2026-09-23T16:39:10Z**
- 是什么：DSH 双阶段上下文压缩插件：LLM 只提出逐原子压缩，确定性守卫负责裁决；再用 0-LLM 引用图剪枝，并从 append-only 日志按摘要或原文精确召回。
- **可拓展性：落地。** 默认 npm 安装只启用 Stage-2 的 0-LLM 图剪，对 16GB 本地机成本最低；需要更强压缩时才启 Stage-1，并可走本地 llama.cpp。用于长时间维护索引前应先在副本会话验证其已公开的窗口截断盲区和 tombstone 两跳限制。
- 去重核查：`grep -iF "yoza10635/dsh-argp" ...` **0 命中**；裸名 `dsh-argp` 同样 **0 命中**。

## 四、vibe coding 安全与模型评测

### 19. `goklab/guardvibe`

- URL：https://github.com/goklab/guardvibe
- 元数据：**5 stars**｜**Apache-2.0**｜**TypeScript**｜最近更新 **2026-09-22T19:07:38Z**
- 是什么：面向 AI/vibe-coded Web 项目的本地确定性安全层，提供 472 条规则、39 个 MCP 工具、跨文件污点/鉴权覆盖分析、提示词前置加固及每日 CVE 情报更新。
- **可拓展性：落地。** `npx guardvibe` 无账号、无 API key、全本地，适合维护索引站时检查密钥、依赖、XSS、鉴权与 MCP 配置；它聚焦 Next.js/Supabase 等 Web 栈，不能替代 Ren'Py/Python 的 Bandit、依赖与发行检查。
- 去重核查：`grep -iF "goklab/guardvibe" ...` **0 命中**；裸名 `guardvibe` 与标题 `GuardVibe` 均 **0 命中**。

### 20. `Blackwellboy/model-serving-minefield`

- URL：https://github.com/Blackwellboy/model-serving-minefield
- 元数据：**134 stars**｜**未声明（GitHub API `license=null`）**｜**Python**｜最近更新 **2026-09-23T16:17:42Z**
- 是什么：按症状整理模型部署与评测“地雷”的证据库，覆盖 chat template、tool parser、reasoning 字段、量化 kernel、CUDA、KV/统一内存、版本漂移，并给出可复现检查与负结果。
- **可拓展性：参考。** 仓库有 Ollama 专页和只读诊断 CLI/MCP，可用来判断“模型能力差”是否其实是服务链配置错；它不直接制作游戏，且未声明许可证，适合查证和引用结论，不宜复制代码进入项目。
- 去重核查：`grep -iF "Blackwellboy/model-serving-minefield" ...` **0 命中**；裸名与标题 `Model Serving Minefield` 均 **0 命中**。

## 本路去重报告

### 精确命中后剔除

- `gamedev-skills/awesome-gamedev-agent-skills`：`index.html` 已有项目卡片。
- `wellingfeng/UltraGameStudio`：`index.html` 已有项目卡片。
- `IvanMurzak/Godot-MCP`、`CoplayDev/unity-mcp`、`hi-godot/godot-ai`：三者均被 `index.html` 命中；属于 Godot/Unity MCP 高频项目，不重复收入。

### 高频主题但主动不收

- `IvanMurzak/Unity-MCP`、`hybridindie/godot-mcp`：虽然本轮完整路径 grep 未命中，但属于索引已高密度覆盖的 `unity-mcp` / `godot-mcp` 同类实现，本轮不再堆叠。
- `DotHarness/dotcraft-unity`（24★）：真实且完整，但与更成熟的 `hatayama/unity-cli-loop` 在 Unity Agent 自动化上高度重叠，为保持 20 项上限而剔除。
- `ShinyDataTech/fast-laya-compaction`、`falling-ts/dsh-force-compact`、`john-walks-slow/dsh-clear-mind`、`LXBWOW/dsh-context-curator`：均未精确命中，但分别涉及已高频出现的 Laya/Jev/DSH 压缩叙事，且当前只有 1–10★；只保留机制更清楚、有确定性守卫与召回测试的 `dsh-argp`。
- `michaltomczykowski/godot-ai-animation-toolkit`、`halilogia/Godot-AI-Sidebar`、`built-by-rafi/universal-cloud-3d-asset-mcp`、`KAFKA2306/unity-mcp`、`codingriver/upilot`：0–1★ 或尚未形成可验证采用面，按要求剔除空壳/早期项目。
- `Labored-nontricyclicdrug743/vibecheck`、`Mansi-2024/VibeCheck`、`protectvibe14/protectvibe`、`SabahatGhauri/vibesafe` 等：同主题描述高度模板化，多为 0–1★，疑似 SEO/课程样板，不收。
- `mnemoverse/mcp-memory-server` 虽最终列入，但明确标为“不采用”：开源范围仅 MCP 客户端，核心服务默认托管；保留它只为“有帮助/误导反馈驱动记忆重排”这一不同于普通向量检索的新机制。

### 换名、上游与派生核查

- `coddy-project/coddy-agent` README badge 中出现旧 owner `EvilFreelancer/coddy-agent`；旧路径在三份基线均 0 命中，因此不是换名后重复收入。
- `NERDSORG/Mutsumi` README badge 中出现旧 owner `MalachiteN/Mutsumi`；旧路径同样 0 命中。
- `unbound-force/dewey` 明示为 `graphthulhu` 的 hard fork；三份基线未收录上游，且 Dewey 增加 SQLite、Ollama、多源索引、时间知识编译与信任分级，不按“无实质变化的 fork 复刻”处理。
- 最终 20 项均由 `gh api repos/{owner}/{repo}` 成功返回，`fork=false`、`archived=false`，并完成完整仓库名 grep；未用搜索结果摘要代替真实性核验。
