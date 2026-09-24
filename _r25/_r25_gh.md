# 第二十五辑 · GitHub 路候选（r25-gh，2026-09-24）

> 数据来源：`gh api repos/<owner>/<repo>` 实测（2026-09-24，UTC）；星标一律实测，不照抄网页。
> 查重范围：`index.html`、`csdn-social-summary.md`(=v23 副本)、`csdn-social-summary-v23.md`、`csdn-social-summary-v22.md`、`csdn-social-summary-v21.md`，必要时回溯 v1~v20。
> 收录标准：优先 `pushed_at` 落在 2026-09 的项目。
> 适用画像：16GB Windows + 本地 Ollama + 维护索引站的个人开发者。

---

## 一、AI 开发与使用（agent harness / 多 agent 编排 / vibe coding 工具链 / spec-kit）

### 1. ruvnet/metaharness
- 链接：https://github.com/ruvnet/metaharness
- 实测（gh api，2026-09-24）：★672 / license: MIT / 语言 TypeScript / pushed_at 2026-09-22T08:24:30Z / forks 85
- 一句话：不是再造一个 harness，而是「脚手架元 harness」——用一条命令生成属于你自己的、带 npx CLI + MCP server + memory + 学习回路 + 见证签名的专用 agent harness。
- 可复用性：⚠️参考 —— 它一上来要 Node/npx 生态，16GB 机器上能跑，但生成物很重（web 服务 + 签名发布链）；值得读的是它把「记忆 / 学习回路 / 发布可信度」拆成可插拔层的目录结构，而不是直接采用整套。
- 去重证据：`grep -iF "ruvnet/metaharness"` 在 index.html / csdn-social-summary.md / v23 / v22 / v21 → 0 命中

### 2. stacklok/mecatl
- 链接：https://github.com/stacklok/mecatl
- 实测（gh api，2026-09-24）：★168 / license: Apache-2.0 / 语言 Go / pushed_at 2026-09-24T10:08:56Z / forks 17
- 一句话：Stacklok（做 MCP 安全网关那家）出的开源 agent harness，同一套 provider 无关循环可本地跑、远程跑或上 K8s，自带持久状态、权限和 gRPC/HTTP-SSE 接口。
- 可复用性：⚠️参考 —— 单二进制 Go 很轻，本地跑不吃内存，适合我们这种小机器；但它的价值主张是「云原生生产负载」，个人索引站用不上 K8s 那部分，只借鉴它的权限模型与 SSE 接口设计即可（注意 open issues 已 275 条，偏活跃但也偏生）。
- 去重证据：`grep -iF "stacklok/mecatl"` → 0 命中

### 3. martymcenroe/AssemblyZero
- 链接：https://github.com/martymcenroe/AssemblyZero
- 实测（gh api，2026-09-24）：★112 / license: NOASSERTION（GitHub 未识别，仓库自有授权） / 语言 Python / pushed_at 2026-09-24T06:08:09Z / forks 2
- 一句话：参数化的多 agent 编排框架，同一套流水线按参数同时驱动 Claude Code 与 Gemini，做「规格→实现→自检」的装配线。
- 可复用性：⚠️参考 —— 编排思想（参数化角色分工）可借，但许可证状态未明（NOASSERTION）+ open issues 625 条，说明项目处于高度自我迭代期；本地 Ollama 用户要先确认它是否支持 OpenAI 兼容端点。
- 去重证据：`grep -iF "martymcenroe/AssemblyZero"` → 0 命中

## 二、上下文管理（裁剪 / 压缩 / 缓存保活 / 指针化 / 预算扫描 / token 计量）

### 4. Paritok-official/paritok-4b-v1
- 链接：https://github.com/Paritok-official/paritok-4b-v1
- 实测（gh api，2026-09-24）：★1455 / license: Apache-2.0 / 语言 Python / pushed_at 2026-09-20T17:28:05Z / forks 140
- 一句话：非破坏性上下文压缩网关，用自家开源「代码原生 4B 模型」在请求进模型前压缩历史，宣称第一轮省 25%、长会话省到 85%+，对 Claude Code/Cursor/Codex/任意 BASE_URL agent 都是 drop-in。
- 可复用性：⚠️参考 —— 「4B 模型」这层对 16GB + 本地 Ollama 是负担（和主模型抢显存），不能照搬；但它是**照 BASE_URL 挂载、零客户端改动**的范例，最值得我们抄的是「网关侧压缩 + fail-closed」这套接口，而不是它的模型。
- 去重证据：`grep -iF "Paritok-official/paritok-4b-v1"` → 0 命中

### 5. mlhher/late-cli
- 链接：https://github.com/mlhher/late-cli
- 实测（gh api，2026-09-24）：★432 / license: NOASSERTION / 语言 Go / pushed_at 2026-09-22T19:15:32Z / forks 45
- 一句话：高性能长任务 agent CLI，宣称把「20 万 token 的工作量塞进 64k 上下文窗口」，靠经验性研究驱动上下文调度而非单纯截断。
- 可复用性：⚠️参考 —— 单 Go 二进制、本地跑很轻，契合小机器；但许可证未声明（NOASSERTION），且「把大活塞小窗」的具体机制需读源码验证，先当方法论参考、不直接并入索引站。
- 去重证据：`grep -iF "mlhher/late-cli"` → 0 命中

### 6. ranxianglei/billion-context
- 链接：https://github.com/ranxianglei/billion-context
- 实测（gh api，2026-09-24）：★267 / license: MIT / 语言 TypeScript / pushed_at 2026-09-24T10:12:27Z / forks 30
- 一句话：中文作者写的上下文压缩插件，专治小窗口——「100K 上下文足矣」，宣称省 5 倍 token，支持数月级、数十亿 token 的单会话。
- 可复用性：✅落地 —— 直接冲「小上下文窗口 + 省 token + 超长会话」而来，与 16GB 机器上跑小参数本地模型的痛点完全重合；MIT、TypeScript、中文文档，是本节最贴合我们画像的一条。
- 去重证据：`grep -iF "ranxianglei/billion-context"` → 0 命中

### 7. fitchmultz/pi-posthorse
- 链接：https://github.com/fitchmultz/pi-posthorse
- 实测（gh api，2026-09-24）：★248 / license: MIT / 语言 TypeScript / pushed_at 2026-09-24T01:14:11Z / forks 7
- 一句话：给 Pi coding agent 的 fork 提供「原生不摘要」的上下文窗口滚动：上下文满了就开新窗口，靠 rollover 工具 + 持久笔记 + 历史回捞保持连续性。
- 可复用性：⚠️参考 —— 它反对「摘要压缩丢信息」，走「无损换窗 + 笔记锚定」路线，这个取舍值得写进我们的上下文策略；但绑定 Pi 的 fitchmultz fork，不可直接移植到 Ollama 链路。
- 去重证据：`grep -iF "fitchmultz/pi-posthorse"` → 0 命中

### 8. snchimata/tokenfold
- 链接：https://github.com/snchimata/tokenfold
- 实测（gh api，2026-09-24）：★205 / license: Apache-2.0 / 语言 Rust / pushed_at 2026-09-21T03:02:46Z / forks 35
- 一句话：provider 中立的私有上下文压缩器，可逆压缩 schema 与日志，全程在你自己边界内、零第三方调用。
- 可复用性：✅落地 —— 「零第三方调用 + 可逆压缩」正好满足我们「数据不出本机」的硬约束；Rust 单二进制轻量，适合放在本地 Ollama 前置做日志/schema 瘦身；Apache-2.0 商用无忧。
- 去重证据：`grep -iF "snchimata/tokenfold"` → 0 命中

### 9. Siddhant-K-code/distill
- 链接：https://github.com/Siddhant-K-code/distill
- 实测（gh api，2026-09-24）：★181 / license: MIT / 语言 Go / pushed_at 2026-09-24T08:34:56Z / forks 17
- 一句话：给 LLM agent 的「上下文智能层」——持久记忆 + 写入时去重 + 敏感度打标 + 冲突检测 + 分层衰减，约 12ms，**不调用任何 LLM**。
- 可复用性：✅落地 —— 纯确定性、不烧模型算力、Go 单二进制，16GB 机器零压力；「写入时去重 + 分层衰减」正是索引站长期上下文治理最缺的一环，MIT 可直接借鉴实现。
- 去重证据：`grep -iF "Siddhant-K-code/distill"` → 0 命中

## 三、Memory 管理（长期记忆 / handoff / 记忆整合 dreaming / 失败记忆 / 健康检查）

### 10. akitaonrails/ai-memory
- 链接：https://github.com/akitaonrails/ai-memory
- 实测（gh api，2026-09-24）：★8256 / license: MIT / 语言 Rust / pushed_at 2026-09-23T22:37:36Z / forks 562
- 一句话：给各种 agent coding CLI 做长期记忆，并提供**跨厂商 handoff**（把上下文从 A 家 agent 交接到 B 家）。本项目 ★ 最高的一条。
- 可复用性：✅落地 —— Rust 单二进制、MIT、活跃；「跨 vendored agent 交接」正对我们要在 DSH / Claude / 本地模型之间搬上下文的现实需求，是本节最值得先跑通的一条。
- 去重证据：`grep -iF "akitaonrails/ai-memory"` → 0 命中

### 11. Lyellr88/marm-memory
- 链接：https://github.com/Lyellr88/marm-memory
- 实测（gh api，2026-09-24）：★402 / license: Apache-2.0 / 语言 Python / pushed_at 2026-09-24T10:10:27Z / forks 84
- 一句话：local-first 的「三合一」AI 记忆层 + MCP server，把会话历史、代码库索引、概念图谱融合进本地 SQLite，零云、隐私优先，支持多 agent swarm。
- 可复用性：✅落地 —— 「全部落到本地 SQLite、零云」与 16GB + Ollama 完全对齐，MCP 接口可被多个客户端复用；Python 依赖需留意，但比引入向量数据库轻得多。
- 去重证据：`grep -iF "Lyellr88/marm-memory"` → 0 命中

### 12. awrshift/agent-memory-kit
- 链接：https://github.com/awrshift/agent-memory-kit
- 实测（gh api，2026-09-24）：★34 / license: MIT / 语言 Python / pushed_at 2026-09-24T09:26:46Z / forks 7
- 一句话：把 agent 记忆做成你文件夹里的**纯文本文件**，且必须「agent 提议、你批准」才写入，每行带日期；支持会话 handoff，并在你点头后升级为知识与规则。
- 可复用性：✅落地 —— 「记忆即纯文本 + 人在环批准」最契合维护索引站的个人（可 grep、可 git diff、不会被黑盒记忆污染）；MIT，实现思路可直接照搬到我们的工作区。
- 去重证据：`grep -iF "awrshift/agent-memory-kit"` → 0 命中

### 13. JusticeUA/agent-handoff-memory
- 链接：https://github.com/JusticeUA/agent-handoff-memory
- 实测（gh api，2026-09-24）：★0 / license: MIT / 语言 TypeScript / pushed_at 2026-08-18T10:20:28Z / forks 0
- 一句话：MCP 记忆服务器，给多个 agent 一份**带版本号的共享记忆**，并用 handoff packet「钉死」下个会话应从哪一版记录开始，底层 SQLite、零原生依赖。
- 可复用性：⚠️参考 —— 0★ 且 8 月推送，不是「最近更新」的强候选；但「handoff 时钉版本号」是防上下文漂移的好点子，可作为设计参考而非落地方案。
- 去重证据：`grep -iF "JusticeUA/agent-handoff-memory"` → 0 命中

## 四、DeepSeek Harness (dsh) 及其插件生态

### 14. dsh-market/dsh-market
- 链接：https://github.com/dsh-market/dsh-market
- 实测（gh api，2026-09-24）：★4476 / license: MIT / 语言 TypeScript / pushed_at 2026-09-24T10:12:47Z / forks 224
- 一句话：直接嵌在 DSH 里的可视化插件市场，浏览、搜索、一键安装；是本轮 dsh 生态里 ★ 最高的官方形态目录。
- 可复用性：⚠️参考 —— 我们不是 DSH 插件作者，装它意义有限；但它是观察「dsh 生态哪些插件真有量」的最佳观测点，可当选型雷达用。
- 去重证据：`grep -iF "dsh-market/dsh-market"` → 0 命中

### 15. sjh9714/dsh-win32
- 链接：https://github.com/sjh9714/dsh-win32
- 实测（gh api，2026-09-24）：★68 / license: MIT / 语言 TypeScript / pushed_at 2026-09-24T10:13:14Z / forks 3
- 一句话：在**原生 Windows**（无需 WSL）上修复并诊断 DeepSeek Harness：官方 PowerShell、Workspace 写入、快捷方式与旧预设修复。
- 可复用性：✅落地 —— 我们就是 Windows 工作区，「不用 WSL 跑 DSH」直击痛点；MIT、TypeScript、★ 虽不高但方向极准，值得优先试。
- 去重证据：`grep -iF "sjh9714/dsh-win32"` → 0 命中

### 16. slow-stack/mneme
- 链接：https://github.com/slow-stack/mneme
- 实测（gh api，2026-09-24）：★121 / license: MIT / 语言 JavaScript / pushed_at 2026-09-24T10:12:05Z / forks 18
- 一句话：DSH 的跨会话记忆插件，「会做梦的记忆」——离线私密，睡眠时自动整合（autoDream），并在记忆面板里可视化。
- 可复用性：✅落地 —— 同时命中「dsh 插件」与「记忆整合 dreaming」两个重点主题，离线私密契合本地路线；MIT、JS，接入成本低。
- 去重证据：`grep -iF "slow-stack/mneme"` → 0 命中

### 17. whyihaveyou/dsh-suite
- 链接：https://github.com/whyihaveyou/dsh-suite
- 实测（gh api，2026-09-24）：★56 / license: MIT / 语言 HTML / pushed_at 2026-09-24T10:05:48Z / forks 13
- 一句话：DSH 插件「活目录」——每小时刷新、每日做兼容实测，内置插件商店与脚手架，比静态榜单更接近实测口径。
- 可复用性：⚠️参考 —— 作为选型/兼容性参考价值高（尤其「每日兼容实测」这一条），但不解决我们自己的上下文或游戏制作问题。
- 去重证据：`grep -iF "whyihaveyou/dsh-suite"` → 0 命中

## 五、VSCode / 编辑器扩展

### 18. ollama/ollama-vscode
- 链接：https://github.com/ollama/ollama-vscode
- 实测（gh api，2026-09-24）：★52 / license: MIT / 语言 TypeScript / pushed_at 2026-09-14T19:30:39Z / forks 23
- 一句话：Ollama 官方的 VS Code 扩展，把本机 Ollama 模型直接接进编辑器对话。
- 可复用性：✅落地 —— 官方出品 + 直连本地 Ollama，与「16GB + 本地模型」的画像零摩擦；MIT、TypeScript，装上即用，是本节最该先装的一条（注意 open issues 28 条，功能尚在补齐）。
- 去重证据：`grep -iF "ollama/ollama-vscode"` → 0 命中

### 19. agent-sh/agnix
- 链接：https://github.com/agent-sh/agnix
- 实测（gh api，2026-09-24）：★423 / license: Apache-2.0 / 语言 Rust / pushed_at 2026-09-20T21:24:48Z / forks 31
- 一句话：AI 编程助手的「缺失的 linter + LSP」——校验 CLAUDE.md、AGENTS.md、SKILL.md、hooks、MCP 配置，覆盖主流 IDE 插件并支持自动修复。
- 可复用性：✅落地 —— 我们天天写 agent 指令文件（house rules / skills），一个确定性的规范校验器能防「配置写错导致 agent 行为漂移」；Rust 单二进制、Apache-2.0，轻量直接上。
- 去重证据：`grep -iF "agent-sh/agnix"` → 0 命中

### 20. cdervis/Pendant
- 链接：https://github.com/cdervis/Pendant
- 实测（gh api，2026-09-24）：★181 / license: 未声明 / 语言 未识别（无主语言标记） / pushed_at 2026-09-20T20:48:29Z / forks 4
- 一句话：把 Pi coding agent 搬进 VS Code 的扩展。
- 可复用性：⚠️参考 —— 只解决「Pi 用户在 VS Code 里的体验」，与我们本地 Ollama 链路无直接关系；且无许可证声明、无主语言，工程成熟度存疑，仅登记备查。
- 去重证据：`grep -iF "cdervis/Pendant"` → 0 命中

## 六、游戏制作及拓展（引擎 AI 集成 / 游戏 agent / 自动试玩 / AI NPC / 素材管线）

### 21. nobodywho-ooo/nobodywho
- 链接：https://github.com/nobodywho-ooo/nobodywho
- 实测（gh api，2026-09-24）：★1346 / license: EUPL-1.2 / 语言 Rust / pushed_at 2026-09-24T10:00:48Z / forks 86
- 一句话：面向游戏/任意设备的**本地 LLM 推理引擎**，让游戏里直接跑本地模型，实现真正的离线 AI NPC。
- 可复用性：✅落地 —— Rust 引擎、目标就是「任何设备本地跑 LLM」，与 16GB + Ollama 的本地推理诉求同源；可评估它能否挂我们已有的 GGUF 权重给游戏 NPC 用（EUPL-1.2 属弱著佐权，二次分发需注意）。
- 去重证据：`grep -iF "nobodywho-ooo/nobodywho"` → 0 命中

### 22. CharTyr/STS2-Agent
- 链接：https://github.com/CharTyr/STS2-Agent
- 实测（gh api，2026-09-24）：★327 / license: NOASSERTION / 语言 C# / pushed_at 2026-09-24T07:31:07Z / forks 46
- 一句话：《杀戮尖塔 2》MOD：把游戏状态与操作暴露成本地 HTTP API 并包装成 MCP Server，供任意支持 MCP 的 AI 客户端调用——即「让 agent 直接玩商业游戏」。
- 可复用性：⚠️参考 —— 它是「已上市商业游戏 + MOD + MCP」的范式样本（自动试玩/游戏 agent 的极佳教学案例），但依赖该游戏本体与 MOD 环境，不是通用引擎工具。
- 去重证据：`grep -iF "CharTyr/STS2-Agent"` → 0 命中

### 23. tettethu/VibeGame
- 链接：https://github.com/tettethu/VibeGame
- 实测（gh api，2026-09-24）：★250 / license: Apache-2.0 / 语言 Python / pushed_at 2026-09-23T13:34:21Z / forks 15
- 一句话：自称「AI 原生游戏引擎」的开源自演化多 agent 框架，用自然语言直接生成可玩的 2D 网页游戏并随时改，基于 Claude Code 与 Codex。
- 可复用性：⚠️参考 —— 「自然语言→可玩游戏」的管线值得研究（尤其对我们做游戏生产流水线索引）；但基于 Claude Code/Codex，需确认能否把模型后端换成本地 Ollama 再谈落地。
- 去重证据：`grep -iF "tettethu/VibeGame"` → 0 命中

### 24. GAlbanese09/spritebrew
- 链接：https://github.com/GAlbanese09/spritebrew
- 实测（gh api，2026-09-24）：★56 / license: AGPL-3.0 / 语言 TypeScript / pushed_at 2026-09-24T02:30:42Z / forks 6
- 一句话：AI 像素美术素材管线：上传或生成角色 → 做动画 → 导出 Unity/Godot/GameMaker/RPG Maker 可直接用的 sprite sheet。
- 可复用性：⚠️参考 —— 直击「素材管线」这个本节最缺的环节，导出口径覆盖四大引擎很实用；但 AGPL-3.0 对二次分发/服务化有传染性，个人自用无碍、要商用需谨慎。
- 去重证据：`grep -iF "GAlbanese09/spritebrew"` → 0 命中

### 25. IvanMurzak/Unreal-MCP
- 链接：https://github.com/IvanMurzak/Unreal-MCP
- 实测（gh api，2026-09-24）：★39 / license: Apache-2.0 / 语言 C++ / pushed_at 2026-09-24T03:06:33Z / forks 5
- 一句话：Unreal Engine 的 AI Game Developer 插件（C++ 编辑器插件 + .NET bridge + unreal-cli），把 UE 编辑器接到 AI agent（走 ai-game.dev 或本地 MCP server）。
- 可复用性：⚠️参考 —— 补齐了「UE 引擎 AI 集成」这一节空缺，且明确支持「本地 MCP server」；但 UE 本身对 16GB 机器偏重，只作方案参考、不建议在本机全量跑。
- 去重证据：`grep -iF "IvanMurzak/Unreal-MCP"` → 0 命中

## 七、vibe coding 安全（无认证扫描 / slopsquatting / 披露合规）

### 26. benavlabs/vibe-check
- 链接：https://github.com/benavlabs/vibe-check
- 实测（gh api，2026-09-24）：★112 / license: MIT / 语言 Python / pushed_at 2026-09-18T23:45:08Z / forks 11
- 一句话：给 vibe coded 应用的安全清单：一份 AI rules 文件 + 自动审计 + 人工核对步骤，三条腿一起上。
- 可复用性：✅落地 —— 「AI rules 文件 + 自动审计」正是我们这种「让 agent 写代码但自己兜底」的场景所需；MIT、Python，可直接抄规则集到自己的 agent 指令里。
- 去重证据：`grep -iF "benavlabs/vibe-check"` → 0 命中

### 27. HQ1995/vibe-security-radar
- 链接：https://github.com/HQ1995/vibe-security-radar
- 实测（gh api，2026-09-24）：★110 / license: MIT / 语言 Python / pushed_at 2026-09-12T20:55:48Z / forks 9
- 一句话：持续追踪「由 AI 写的代码所引入的漏洞」的雷达，把 AI 编码带来的真实安全事件做成可追踪清单。
- 可复用性：✅落地 —— 是「披露合规 / 风险情报」这一细分最对口的项目，可当作我们 vibe coding 安全主题的情报源；MIT、Python，轻量。
- 去重证据：`grep -iF "HQ1995/vibe-security-radar"` → 0 命中

### 28. LeiLiLab/susvibes
- 链接：https://github.com/LeiLiLab/susvibes
- 实测（gh api，2026-09-24）：★52 / license: MIT / 语言 Python / pushed_at 2026-09-17T21:48:29Z / forks 8
- 一句话：ICML 2026 论文配套基准「Is Vibe Coding Safe?」——在真实任务上给「agent 生成代码的安全性」打分。
- 可复用性：⚠️参考 —— 学术基准而非工具，不能直接扫我们的代码；但它是目前少见的「可复核数字」的安全证据来源，适合做索引站的安全议题引用锚点。
- 去重证据：`grep -iF "LeiLiLab/susvibes"` → 0 命中

---

## 本路去重报告

查重口径：对每个候选先跑
`grep -iFn "<owner>/<repo>" index.html csdn-social-summary.md csdn-social-summary-v23.md csdn-social-summary-v22.md csdn-social-summary-v21.md`，
命中即剔；另对裸项目名 / 上游名做补查（见末行）。共检索约 120 个候选，命中去重 12 个，收录 28 条。

| 剔除对象 | 重复形态 | 命中位置（文件:行） |
|---|---|---|
| `Context-Engine-AI/Context-Engine` | ①换名/往辑已收 | csdn-social-summary-v21.md:205（20 辑已列 ★403/MIT/Python） |
| `YerbaPage/Awesome-Agent-Context-Compression` | ④ID 新≠内容新（卡片+脚注双写） | index.html:11451（卡片）、index.html:15981（脚注 [1122]） |
| `NPGameDev/godot-mcp-toolkit` | ①同项目族已收 | index.html:11059 区段文本「`NPGameDev/godot-mcp-toolkit`（44★，编辑器内插件）」 |
| `mksglu/context-mode` | ④ID 新≠内容新 | index.html:11126（卡片）、index.html:16205（脚注 [1104]） |
| `ojuschugh1/sqz` | ④ID 新≠内容新 | index.html:11763（卡片）、index.html:15614（脚注 [1140]） |
| `ooples/token-optimizer-mcp` | ②旧闻（上一辑候选池） | csdn-social-summary-v22.md:591 |
| `PawanOsman/OpenCursor` | ④ID 新≠内容新 | index.html:11627（卡片）、index.html:15606（脚注 [1132]） |
| `hi-godot/godot-ai` | ④ID 新≠内容新 | index.html:11050（卡片） |
| `CoplayDev/unity-mcp` | ④ID 新≠内容新 | index.html:1063（卡片） |
| `hatayama/unity-cli-loop` | ④ID 新≠内容新 | index.html:11291（卡片）、index.html:16114（脚注 [1113]） |
| `Donchitos/Claude-Code-Game-Studios` | ④ID 新≠内容新 | index.html:651（卡片） |
| `youichi-uda/godot-mcp-pro` | ②旧闻（上一辑已述） | csdn-social-summary-v21.md:341 |

补充说明（非重复、因口径剔除，如实登记）：
- `brennhill/sloppy-joe`（★32）：功能对口，但 `pushed_at=2026-04-17`，不满足「最近实质更新」，剔。
- `Armur-Ai/vibescan`（★83）：`pushed_at=2026-03-28`，同上，剔。
- `editor-code-assistant/eca`、`specstoryai/getspecstory`、`arabold/docs-mcp-server`、`objectstack-ai/objectstack`：查重 0 命中，但与「16GB Windows + Ollama + 索引站」画像关联度弱于已收录条目，列为下辑备选池。
- 已知 6 种重复形态里，本路主要命中 ①②④ 三种；未发现 ③转载 / ⑤SEO 镜像 / ⑥同日双发内容农场形态（GitHub 路口径下这三类通常出现在 cn/official 路）。
- 裸名/上游名补查：`ollama-vscode`（index.html:0 / summary:0）、`aigengame/godot-agent` 与 `juffson/godot-agent`（0 命中）均已确认非重复。

### 本路边界（诚实交代）
1. **未找到**独立成条的「失败记忆 / memory health check」专项项目——只检索到 `shantanubokey/failure-memory-engine`（★0，2026-04 推送，太旧太冷），故该子题在第三节并入「分层衰减/冲突检测」（Siddhant-K-code/distill）与「证据门控整合」（Namiuti/evidence-gated-memory-consolidation，★1，未单独成条）。
2. **Gitee / HuggingFace 未产出**：本轮 `gh` 无法检索 Gitee，HuggingFace 侧仅旁证到 `huggingface/pi-llama`（模型 provider 扩展）。Gitee 路需另配工具，本路已放弃，不计入 28 条。
3. **Unity / Unreal 的「自动试玩」**：只找到 `CharTyr/STS2-Agent` 这一「商业游戏 + MOD + MCP」样本；主流引擎侧的 `CoplayDev/unity-mcp`、`hatayama/unity-cli-loop`、`youichi-uda/godot-mcp-pro`、`hi-godot/godot-ai` 均已被历史辑收录，故「自动试玩」实质性新增有限。
4. 星标读数一律取 `gh api` 实测（2026-09-24），未采信任何网页/二手报道；`dsh-market`（★4476）与 `akitaonrails/ai-memory`（★8256）为放大后的活跃星标，非历史峰值。
