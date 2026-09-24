# 第二十一辑 · 官方与海外路（厂商官网 / 海外社区 / 榜单与价格 / 游戏引擎厂）

> 子 agent：r21-official · 日期 2026-09-24
> 骨架已落盘（房规 #47：边做边落盘，防限流全丢）。每查到 3~5 条追加一次。
> 去重基线：`index.html`(1120) + `csdn-social-summary.md` + `csdn-social-summary-v2..v20.md`（18 份存档）

## 本路覆盖来源
- 厂商官网 / release notes：Anthropic · OpenAI · Google DeepMind · DeepSeek · Moonshot · 智谱 · 阿里通义 · Meta
- 编辑器与平台：VS Code · GitHub Copilot · JetBrains · Cursor · Windsurf · Zed
- 海外社区：Hacker News · r/LocalLLaMA · r/ChatGPTCoding · DEV.to · note.com · Lobsters
- 榜单与价格：Artificial Analysis（带 index 版本号）· LMArena · SWE-bench 官方 · MLPerf · OpenRouter
- 游戏引擎厂：Unity · Unreal · Godot

## 已知已收（不再重复，除非有后续进展）
Claude Dreaming · Memory Stores · Projects 重构 · Claude smart reports · AA Intelligence Index v4.3 ·
MLPerf Inference v6.1 · Unity Claude Code/Codex 插件 · Unity AI Assistant · VS Code 1.136 Agent Host ·
GitHub Copilot 周报(09-18) · DeepSeek 09-10 撤回涨价 · Grok 4.7 每任务成本 · Bend 2 先例检查 ·
5,000 行未测 AI PR · kihaya 上下文预算算法 · 4090 + Qwen3.8-27B 显存倒推

---

## 一、厂商官网 / Release Notes

### 1. Anthropic Messages API 新增「按需对话压缩」——摘要块签名不可改（beta）
- URL：https://platform.claude.com/docs/en/release-notes/api · 分析：https://gloss.run/post/the-summary-comes-back-signed-and-you-cant-edit-it · https://modeldex.dev/news/claude-api-adds-on-demand-context-compaction-to-the-messages-api
- 日期：**2026-09-14**（beta header `compact-2026-09-04`）
- 是什么：Messages API 多了一种压缩方式。**旧的（threshold）压缩**由 API 按阈值自动触发 —— 默认 `input_tokens` 到 **150,000**（下限 50,000 才允许设置）就在请求中途摘要一次，摘要块**排在**被摘要消息之后，且请求要等摘要写完。**新的（on-demand）**改成一个顶层参数 `compaction: {"type":"summarize"}`：API 不生成回复，只回一个**带签名的 `compaction` block**（`stop_reason: "compaction"`），后续请求把它**放在最前、替换**掉它覆盖的那些消息（把旧消息留在它前面会 400）。
- 关键数字 / 边界：①摘要**能后台生成**，对话继续跑完整历史，落定后再替换；②最近若干轮可以**逐字保留**在摘要之后（preserved thinking 模型上，这些保留轮的 thinking 仍然有效）；③重新压时 `instructions` 最长 **16,384 字符**；④**只支持 Claude API**，明确**不支持 Bedrock / Google Cloud**；⑤覆盖 **11 个模型**（Fable 5.1 / Mythos 5.1 到 Opus 4.6 / Sonnet 4.6）；⑥**不能和 `context_management` 同请求**；⑦顶层 usage 显示 input/output 为 0，真实消耗在 **`usage.iterations`** 里（成本统计要看这里）。
- ⚠️ 坑（分析文章逐条列出）：**摘要你能读但不能改**，块被改动/错位/重复会报 400；**摘要失败仍然返回 200**、忘带块也照常跑（静默失败）；被摘要范围内的**中途 system message 与工具变更随之失效**（"What they declared stops applying"）；图片、文档、抓取的 URL 也没了。要补回丢失的约束，只能在块后**重述**，或"用更好的 instructions 再压一次"——而再压一次是**旧摘要 + 之后内容**，第一轮丢的细节**永久丢失**。
- 对我们的意义：**官方把"什么时候压"的裁决权交给了调用方，但把"压坏了怎么办"的补救权收走了。** ①这与房规「错不起的步骤确定性化」同源 —— 之前社区工具（`dsh-argp` 的"LLM 只提议、守卫裁决"、`jev-compaction` 的"压缩器只能打分不能写"）是**自己造闸门**，现在是官方 API 原生形态；②对我们最实用的一条：**原始消息必须自己留底**（签名块只是历史的一个压缩替身，丢了东西回不来）；③成本核对要读 `usage.iterations`，别再只看顶层 token —— 否则会误判"这次压缩不要钱"。
- 去重核查：`compact-2026` / `compaction on demand` / `按需压缩` 四份基线 **0 命中**（v18/v17/v15 的 `compaction` 命中全是**社区压缩工具** `jev-compaction` / `fast-compaction-dsh` / `opencode-context-pruner`，与官方 API 语义无关）。

### 2. Claude Code 2.1.266→2.1.270：插件也能跑评测、输出上限被钉死、只读 git 权限回归收回
- URL：https://www.gradually.ai/en/changelogs/claude-code/ · https://howtoclaude.dev/claude-code-2-1-270-arrives-with-a-quiet-but-essential-bash-permission-fix · https://myaiguide.co/news/builders-weekly-20260911
- 日期：**2.1.269 = 2026-09-11，2.1.270 = 2026-09-12**（2.1.266~2.1.268 在 09-10 前后）
- 是什么（挑对我们有用的）：
  - **`claude plugin eval`**（2.1.269）：对一个 plugin 跑它的评测套件，拿到**可复现的评分结果（JSON + HTML 报告）**。
  - **`/output-style [name]`**：切换输出风格，Remote Control / 云端 / headless 会话都支持。
  - **`bashEditDiffEnabled`**：Bash 工具改文件时，结果里**附上它改动了哪些文件的 diff**。
  - **`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`（1–256）**：提高 Workflow 工具单次运行的**并发 agent 上限**。
  - **输出/工具结果封顶**：bash 与 task 输出截到 **128K 字符**；保存的工具结果上限 **1 GB**；新增 **`--plugin-dir`** 加载多目录；新增 **`/skill-doctor`** 审计没用上的 skill。
  - **修 prompt cache**：截图截到输出上限后自动续写的那一轮，**部分缓存失效**已修；中断后 resume 导致早期上下文重发、拖累缓存命中的问题也修了。
  - **2.1.270 只有一条**：收回 2.1.269 引入的回归 —— 会话跑久了 `git status/log/diff/branch` 这类**只读命令会突然弹权限**。装上即生效、无需配置，之前为绕开它把 git 加进 allowlist 的可以撤掉。
  - 另一处细节（2.1.269）：**compaction 之后告诉 Claude 的 git status 现在取"当前"而不是会话开始时的**。
- 对我们的意义：①**`plugin eval` 是"给 skill 也配测试"的官方形态** —— 我们有一堆 `check_*.py` 和 `skills-security-check`，但 skill 本身没有"评分制"的 eval suite，这是可补的一环；②"bash 输出截 128K 字符 + 工具结果上限 1GB"是**官方帮我们钉的天花板**，正好印证我们"工具输出会爆上下文"的顾虑；③`/skill-doctor`（审计没用的 skill）= 我们该做的"skills 体检"。
- 去重核查：`2.1.270` / `skill-doctor` 四份基线 **0 命中**。

### 3. Claude Cowork / Desktop changelog：修「Prompt is too long」卡死 + Windows 够不到文件的真因
- URL：https://claude.com/docs/cowork/changelog
- 日期：**v1.52386.6 = 2026-09-13；Windows 修复说明 = 2026-09-14**
- 是什么：①**捆绑的 Claude Code CLI 更新到 2.1.270**（与第 2 条同源）；②修掉 **"会话 prompt 极大时永久卡在 'Prompt is too long' 错误"**（此前是死锁，只能放弃会话）；③修"某模型对你可用却被提示受限、运行中的会话静默切回组织默认模型"；④**Windows**：9 月 8 日的一个 Windows 更新导致 Cowork 工作区够不到本地文件，9-14 微软发更新修复 —— **Win11 24H2 / 25H2 上是 `KB5129195`**，装完重启即可，**不需要更新 Claude Desktop**。
- 对我们的意义：**长会话是真的会撞死的**（不是理论）—— 官方直到 09-13 才把"大 prompt 永久卡死"修掉，这给我们"分阶段、控上下文"又多一条外部证据；另外**"够不到文件"的排查方向应是系统更新而不是应用本身**（Windows 用户常踩的错层归因）。
- 去重核查：`Prompt is too long` 四份基线 **0 命中**（v17 收的是"Cowork 与 Chat 合并成同一界面 + Docs/Slides/Design"，是**另一件事**；本条是 Cowork 的运行时 changelog）。

### 4. Claude Managed Agents：权限判定加了「auto 模式」，还能把终端挂到正在跑的会话上
- URL：https://modeldex.dev/news/claude-api-adds-on-demand-context-compaction-to-the-messages-api（与第 1 条同批发布）
- 日期：**2026-09-10**
- 是什么：①**权限 auto 模式** —— 服务端**自己评估**每一次 agent / MCP 工具调用，决定**执行 / 拒绝 / 暂停等审批**，评估结果通过 **`agent.tool_use` 与 `agent.mcp_tool_use` 事件**回报；②`ant beta:sessions connect` 把终端**接到一个正在运行的 Managed Agents 会话**上，可实时观看、发消息、批准或拒绝被暂停的工具调用，`--web` 还能把 Console 的会话查看器**在本地起一个**。
- 对我们的意义：**"审批变成可观测事件"** 是这一条的核心 —— 我们的闸门是"改闸门/记忆/发行必须人核"，但审批结果**不留结构化记录**；官方把它做成事件流（谁拦了什么、为什么拦）。"挂终端旁听"对应我们"后台 agent 不持久、看不到进度"的困境，是产品化答案。
- 去重核查：`Managed Agents` / `tool_use` / `sessions connect` 四份基线 **0 命中**（v20 收的是 Managed Agents 的 **Memory Stores**，是另一条能力）。

## 二、编辑器与平台（VS Code / Copilot / JetBrains / Cursor / Windsurf / Zed）

### 5. Cursor 3.21.4：Canvas、知识库 API、MCP 后台管理，以及一条「本地 Ollama」路径
- URL：https://techdevnotes.com/releases/cursor-ide/20260916-200507Z-2d581b499828 · Cursor CLI：https://techdevnotes.com/releases/cursor-cli/2026.09.15-d2fe57e
- 日期：**IDE 3.21.4 = 2026-09-16（latest 通道，stable 仍是 3.20.21）；CLI = 2026-09-15**
- 是什么：①**Canvas**（`cursor.com/canvas`）产品内画布，支持 agent 驱动的**读写**；②**知识库 API**（增 / 列 / 改）；③**MCP 管理**：组织级 MCP 工具的发现与 list/call/preview；④**agent host 接管会话存储**（可选 migrate-on-open）；⑤**`local models` 里出现「Glass 走本地 Ollama」的路径（flag-gated）**；⑥git 分支命名与 commit message 生成；⑦web fetch / web search / 图像生成走 AI 服务端。CLI 侧则**删掉**了内置 `shell_command` 工具、`/bug` `/checkpoint` `/cost` 三条 slash 命令与 `providers` 配置键。
- 对我们意义：①**Cursor 开始出现"本地 Ollama"入口**（即使还是 flag）—— 对 16GB Windows / 本地模型路线是一个**大厂在往本地走**的信号；②**CLI 把 `/cost` 删了**说明成本追踪正被收进 IDE 侧，命令行用户要自己另找口径；③"组织级 MCP 后台统一发现/调用"与我们的"官方 skills 集中维护"是同一思路。
- 去重核查：`Cursor Origin` / `3.21.4` 四份基线 **0 命中**（v19 收的是 Cursor 的 Cloud Agents/Projects 早期形态，本条是 **3.21.4 的具体 changelog**）。

### 6. GitHub Copilot：六个模型 10-19 集体退役 + code review 转 GA（findings 分三类）
- URL：https://webairadar.com/en/news/github-is-retiring-six-copilot-models-and-has-rebuilt-the-code-review-overview （引 GitHub 官方 changelog，2026-09-18）
- 日期：**公告 2026-09-18，生效 2026-10-19**
- 是什么：①**六模型退役，各自有替代**，覆盖 chat / inline / ask / agent / 补全**全部入口**：`Gemini 3.7 Flash → Gemini 3.8 Flash`；`GPT-5.5 → GPT-5.6 Sol`；`GPT-5.4 → GPT-5.6 Sol`；`GPT-5.4 mini` 与 `GPT-5 mini → GPT-5.6 Luna`；`Grok 4.5 → Grok 4.6`。Enterprise/Business 默认自动启用替代模型，**除非管理员关过全局默认**；菜单选模型的用户零成本，**风险在"写死模型名的地方"（workflow 文件、脚本、团队共享配置）**。②**code review GA**：概览评论把发现分**三类** —— Open（未处理，新提交引入的标 new）、Resolved since last review（已验证修复）、**Previously missed（先前漏掉、后一轮才找到，完整列出）**；**每条 finding 带短标题**；Copilot 自己关闭的评论记录原因（**Won't Fix / Incorrect**）。
- 对我们意义：①**"写死的模型名会过期"** —— 我们 AGENTS.md §十的"版本钉子"应顺带记**退役日期**，否则钉子是钉住了、但钉的是个要下线的名字；②**`Previously missed` 这一分类值得抄**：把"复查时新发现的问题"和"原评论"区分开，我们的 `mistakes/` 复查也该标"这是第几轮才发现的"。
- 去重核查：`GPT-5.4` / `Gemini 3.7` / `Grok 4.5` / `October 19` / `retir` 四份基线 **0 命中**（v19/v20 收的是 **09-18 周报**与 **code review Lite ensemble**，模型退役映射与本条 GA 细节是新的）。

### 7. JetBrains 版 Copilot 1.18.0：低风险工具调用「自动批准」+ 可重编辑上一条消息
- URL：https://plugins.jetbrains.com/plugin/17718-github-copilot
- 日期：**2026-09-18（版本 1.18.0-261）**
- 是什么：①**Assisted Approvals（Public Preview）**：agent 会话中**自动批准低风险工具调用**，高风险动作继续弹确认；②**重编辑上一条用户消息**：**回滚该消息之后的对话与文件改动**，再发替换版；③内置 **GitHub MCP server 默认开启**（可单独关，不动手工配置的 MCP）；④支持**组织/企业级 skills 与自定义指令**；⑤**Codex agent 支持 Plan mode**（先审/改/批计划再实现）；⑥MCP 服务器**按工具持久化控制**；⑦修 Inline Chat 忽略 Thinking Effort / Context Window 设置。
- 对我们意义：①**"低风险自动批、高风险继续问"** 正是我们分层（改 md 随便 / 改闸门必须自验）的**工业版参数化形态**，可以直接照抄成一个"动作风险白名单"；②**"重编辑消息并回滚文件改动"** 是我们没有的能力（我们只能开新会话重来），值得留意是否有等价本地方案。
- 去重核查：`Assisted Approvals` / `1.18.0` 四份基线 **0 命中**。

## 三、海外社区一手材料（HN / Reddit / DEV / note.com / Lobsters）

### 8. ★ 「肉代理」是条死路：Dan Luu 长文 + Yegge 关停 Gas Town + Databricks 换 Astra 反涨 60%
- URL：https://danluu.com/ai-coding/ · 综述与引文：https://prismix.dev/news/3c123bff8ba1 · https://thecontext.dev/en/briefing/2026-09-19
- 日期：**Dan Luu 文 2026-09-15 前后；HN 讨论 2026-09-19（167 up，145 评论）**
- 是什么：①**Dan Luu** 把"从不验证输出、只把 agent 循环起来"的做法叫 **meat proxy（人当肉代理）**，论证它对**雇员**是死路："它现在勉强能用、而且模型越强看着越便宜，但等到模型好到能这样交付软件的那天，公司直接把 LLM 循环起来、把你裁掉就行 —— 这套方法论**没有任何一个时刻对雇员是成立的**"。支撑证据：**Gary Bernhardt 观察到评审把 agent 的 diff 砍到原大小的 25%**；Luu 自己去看那些宣称"编程已经解决"的意见领袖的项目，**"要么跑不起来、要么跑得很糟"**；ChatGPT 给一个新手 Dominion 玩家的建议"对一半错一半"。建议：**监督你的 agent、离群情况自己处理、把模型省下的时间花在抬高自己的交付标准上**。②**Steve Yegge 关停了 Gas Town**（09-15）——tokenmaxxing 最响的旗手，承认每月花几千美元订阅、**却几乎只做出来 Gas Town 这一个东西**；Luu 说他找不到这些"超级 vibe 编排器"有用，是因为**可靠性**（能不能把任务跑完）。③**Databricks 把 ~3,500 名工程师切到 GPT-6 Astra，编码开销反涨约 60%** —— 尽管多个榜单上 Astra 因 token 效率更高、**每任务成本**比 Sol 低，**但它并不是在所有地方都便宜**。
- 对我们的意义：**这是本路最该抄进制度的一条，它一次踩中我们两个已知的坑**：①**"单价便宜 ≠ 总花费便宜"** —— Databricks 的 +60% 正是 M-0019 说的"同一个数、不同口径"在**成本**上的版本（榜单按每任务算、真金白银按总账单算）；②**"谁在替谁省钱"** —— 我们把 AI 用在维护索引站/写检查脚本上，如果省下的时间没有变成"更高的交付标准"，那省下来的就是**被裁的理由**而不是红利（Luu 原话的转写）。可直接落地的一条：**agent 的 diff 必须过人类评审**，Bernhardt 的"砍到 25%"可以当**评审有效性的基线数字**（如果我们的评审平均砍不到什么，说明评审是走过场）。
- 去重核查：`Dan Luu` / `Yegge` / `Gas Town` / `Databricks` / `Bernhardt` / `meat proxy` 四份基线 **0 命中**。

### 9. 176 组编码 agent 配置的实证研究：上下文管理主要只是"防溢出"
- URL：https://snapbyte.dev/llm-news （HN 条目，183 分，2026-09-18）
- 日期：**2026-09-18**
- 是什么：一篇在 **SWE-Bench Verified 与 Terminal-Bench 2.1** 上跑 **176 种编码 agent 配置**的研究，结论三条：①**上下文管理的作用主要是"防止上下文溢出"**，其中**规则化删减（rule-based elision）> LLM 摘要**，后者最省 token；②**规划（planning）提升弱模型的准确率，但对强模型主要只是"降成本"**；③**预定义工具帮到"bash 用不好"的模型**；而**会 bash 的模型用更低成本的 bash-only 接口也表现良好**。
- 我们的意义：**直接反驳了一个流行的过度期待** —— 上下文管理不是"让模型更聪明"，是**兜住不让它掉下去**；这解释了为什么我们 kihaya 式的"重读工作树当前内容 + 骨架化淘汰"管用（它防的是溢出）。第 ③ 条对我们尤其关键：**我们环境里模型"会不会 bash"决定该不该给它一堆工具** —— 会 bash 就少给工具（省上下文、省成本），不会才要预定义工具补齐。
- 去重核查：`176`/`SWE-Bench Verified` 组合四份基线 **0 命中**（v12 曾出现 `harness` 一词但非此项研究）。

### 10. lossless-memory（Show HN）：**永不总结**的记忆 —— 时间轴优先于向量
- URL：https://thecontext.dev/en/briefing/2026-09-22 （Show HN，62 up / 27 评论，项目 aru-labs）
- 日期：**2026-09-22**
- 是什么：给"单用户、单机 AI 助手"做的**无损长期记忆**，唯一原则就是**永不摘要**。①原始对话按天追加进 **JSONL**，每条七字段（时间戳、说话人、角色、类型、**逐字原文**、模型、会话）；②检索用 **SQLite FTS5 精确检索**，`sqlite-vec` **只作为兜底**，且必须**先用时间表达缩小范围**才启用；③**时间短语排在语义相似度前面**；④每轮注入一份独立的**话题标记索引（LLL）**，**这样即使发生上下文压缩，模型也知道对话进行到哪了**。作者说从 2026-07 起**单用户天天在跑**。
- 我们的意义：**"永不总结 + 时间轴优先"是我们 `mistakes/` 与日志索引的一个现成对照物**。①我们的索引是**人写关键词 + grep**，本质就是这个思路的手工版 —— 这条给了它一个**有人长期在跑的背书**；②"**用时间表达先缩小范围，再上向量**"是一个很便宜的性能技巧，适合我们的日志检索；③**LLL 那一条最值钱**：它在"压缩之后"给模型补一张"我聊到哪了"的索引 —— **正是我们长会话压缩后最大的痛点**（第二十辑 caveman/压缩那条的反面答案）。
- 去重核查：`lossless-memory` / `aru-labs` / `LLL` 四份基线 **0 命中**。

### 11. Foremerge：并行 agent 的「意图冲突」协议 —— 冲突检测不调模型
- URL：https://thecontext.dev/en/briefing/2026-09-22 （Show HN，43 up / 13 评论）
- 日期：**2026-09-22**（v0.5.0，Apache-2.0）
- 是什么：**文字不会冲突，意图会**。Git 管合并文本，这一层**盖在 Git 之上**管意图冲突，三步：①一个 agent 开工**前**把它**要改什么**写进项目 `.git` 目录里的**共享 SQLite**；②其它 agent 开工前**读同一张表**；③两份计划撞车时，它**点名两个 agent、解释冲突在哪、建议拆分**。它**只比意图、从不锁文件**，警告是**建议性**的，且**冲突检测是确定性算法、不涉及任何模型**。
- 我们的意义：**"确定性"这三个字是这条的价值观** —— 和第 9 条（上下文管理只是防溢出）、房规"错不起的步骤确定性化"完全同调。我们目前是**串行**多路调研，一旦并行（这轮就是 3 路子 agent），**我们没有任何机制知道"两路在查同一件事"** —— 这正是上几辑"两路 429 中断/产出重复"的根因。可抄的最小版本：**开工前把"我要查什么"写进一个共享文件，收工前先读它**。
- 去重核查：`Foremerge` / `Intent` 四份基线 **0 命中**。

### 12. jevals：8 个 eval 一次请求、0.33 秒、$0.00006 —— 用判定模型替掉 LLM 裁判
- URL：https://thecontext.dev/en/briefing/2026-09-22 （Show HN，42 up / 3 评论，Openlayer 开源）
- 日期：**2026-09-22**
- 是什么：把 agent eval / guardrail 里的 **LLM judge 换成 Jev 式判定模型**，一次 trace 的**所有 eval 合并成一个请求**：README 的例子是 **8 个 eval、1,388 token、0.33 秒、$0.00006**。**Jev 定价 $0.042 / 百万输入 token**，经 Vercel 网关测得 **p50 延迟 244 ms**；仓库里引的 LangChain 对比显示 **GPT / Claude 裁判的分数方差是 Jev 的 92~913 倍**。后端可以是 TypeSafe / Vercel API，也可以是**本地的 Kev 与 Laya**。
- 我们的意义：**这解释了我们为什么"只在关键闸门上跑检查"** —— 用 LLM 当裁判**又贵又抖**（方差 92~913 倍正是"同一段代码两次判不同"）。而这条给的路是：**判定用便宜、确定性高的专门模型，且一次请求评完所有项**。对我们的直接启发：我们的 `check_*.py` 是**规则判定**（已经是这个方向），但"**把 N 个检查合并成一次调用**"的工程手法可以抄来降低编排开销。
- 去重核查：`jevals` / `Openlayer` / `Jev` 四份基线 **0 命中**。

### 13. Devin Code Scans：Agentic MapReduce —— Dioxus 编译从 58.6s 砍到 21s
- URL：https://thecontext.dev/en/briefing/2026-09-19 （HN，26 up，Cognition 官方）
- 日期：**2026-09-19**
- 是什么：Devin 的 `/scan`：给一个**宽泛目标**（"改善 SEO""降低维护成本""让编译更快"），Devin 调研仓库，返回**按优先级排序、有证据支撑的发现清单**，对你选中的项开 PR。底层是**四阶段 Agentic MapReduce**：**Plan**（研究仓库、定义规则）→ **Shard**（把匹配的代码切成批）→ **Map**（并行 agent 各查一批）→ **Reduce**（去重并排优先级）。官方例子：**Dioxus 的 clean debug build 58.6s → 21.0s（-64%）**；对 devin.ai / cognition.com 的 SEO 扫描出 **44 条发现**，Ahrefs 健康分 **87 → 92**；某 Philips 团队报告试验期 **96% PR 合并率、省下 700+ 工程小时**。
- 我们的意义：**"四阶段 MapReduce"就是我们应该给多路子调研/多文件检查套的骨架**（我们现在是"想到哪查到哪"）。而且它的入口设计极其实用：**不问"你要什么精确结果"，只给一个宽泛目标，让 agent 自己定义规则并给证据** —— 这和我们的"体检脚本"正好互补（我们的是确定性、它的是探索性）。**可抄的一句**：每个发现都要**带证据**（Dioxus 那个数字就是证据）。
- 去重核查：`Code Scans` / `MapReduce` 四份基线 **0 命中**。

### 14. 675B 模型幻觉调用「不存在的工具」的频率，和小 90 倍的模型一模一样
- URL：https://genaisecretsauce.com/genai-secret-sauce-daily-digest-2026-09-18
- 日期：**2026-09-18 期**
- 是什么：一项跨十个模型的研究找到 **322 起 agent 调用根本不存在工具**的案例，并给出一句判词：**"一个 6750 亿参数的模型幻觉出假工具调用的频率，和比它小 90 倍的模型一样 —— 更大不等于更安全。"**
- 我们的意义：**"参数不是安全"** 对我们 16GB 本地小模型是**反直觉的好消息**：我们一直在担心"小模型会不会更爱瞎编工具名"，数据说**这个失败模式基本与大模型同频**，所以**不该用"换个更大的模型"来解决**，而该用**闸门**（校验工具名是否存在）来解决 —— 正是我们 `check_*.py` 的思路。
- 去重核查：`fake tool calls` / `675` 组合四份基线 **0 命中**。

### 15. 「确定性不需要纯函数」：把散落各处的确定性碎片回收起来
- URL：https://thecontext.dev/en/briefing/2026-09-22 （HN 55 up / 17 评论，outdata.net）
- 日期：**2026-09-22**
- 是什么：借 Gary Bernhardt 2012 年的 **Functional Core, Imperative Shell**，作者主张：**真正让核心可测的是"确定性"本身，纯函数只是通向确定性的一条路**；**状态机同样确定**（同样的转移序列得到同样的状态），用命令式代码写也不改变这一点。对既有代码库，他推荐做 **"确定性的碎片化回收"（defragmentation of determinism）**：不追求一个干净的核心，而是**把散落在各文件/类/函数里的确定性片段收集起来**，难测代码的表面积就会缩小。
- 我们的意义：**这是给我们"闸门为什么可行"补的一句理论支撑**。我们的检查脚本大多是**命令式**的，却因为**输入→输出确定**而可靠；"碎片化回收"更是直接描述我们的现状 —— 我们不可能重写成纯函数核心，但可以**盘点现有脚本里哪些已经是确定的、把它们聚成一层**（这正好是 `_tools/` 该做的事）。
- 去重核查：`Bernhardt` / `defragmentation` 四份基线 **0 命中**。

### 16. note.com 的一页本地 LLM 全景（2026-09）：Ollama 月活约 890 万、85% 财富 500 在用
- URL：https://note.com/shali_note/n/n71e55d423ac1?hl=en
- 日期：**2026-09（页面标注"截至 2026 年 9 月"）**
- 是什么：一篇日文作者写的"本地 LLM 生态 7 个关键玩家"概览。①**Ollama 月活约 890 万开发者，已被 85% 的财富 500 公司采用**（数据标注截至 2026-07）；②一句话概括当前格局：**中国的 Qwen / DeepSeek / GLM / Kimi 势头在涨，美国的 Llama 与 gpt-oss 停住，只有 Gemma 4 例外地跟得上**；③选型三条判据：**许可证**（是否完全开放如 Apache-2.0，还是有条件）、**你的机器规格**（按 VRAM/RAM 决定能跑多大）、**用途**（通用聊天 / 偏编码 / 日语强化）；④本地方案两条代表路线：**Ollama 是 CLI/API 派**（开发者与程序集成），**LM Studio 是 GUI 派**（不想写程序就从它开始）；⑤日语场景另提 **ELYZA-Llama-3-JP-8B** 与 **Swallow**。
- 对我们的意义：①**"85% 财富 500 用 Ollama"是本地路线最好用的一句背书** —— 当我们为"16GB Windows + 本地 Ollama"的可行性辩护时，可以直接引这个采用面；②**"美国两强停住、中国阵营在涨、Gemma 4 例外"** 正对应我们上一辑"省钱默认改用 GLM 5.3 Flash / DeepSeek 谷时价"的选型结论，**这是第三方视角的互证**；③作者给的**三条判据（许可证 / 机器规格 / 用途）**可以直接当我们本地模型选型表的表头。
- 去重核查：`8.9 million` / `Fortune 500` / `Ollama 月活` 四份基线 **0 命中**（`Ollama` 命中很多，但都是作为**工具**出现，**没有一条收过它的采用规模数据**）。

### 17. 扩散式语言模型在悄悄成熟：训练 1.61×、生成 7.59×，且能用一半数据"改造"现成 Qwen
- URL：https://genaisecretsauce.com/genai-secret-sauce-daily-digest-2026-09-18
- 日期：**2026-09-18 期**（引 arXiv 论文）
- 是什么：现在多数对话模型是**从左到右逐词写**；**扩散模型一次refine 多个词**，可能更快。本周三项进展削掉了它过去"不实用"的理由：①**Block Parallelism**：新的分布式训练工作在**超长输入**上报告**训练快 1.61×、生成快 7.59×**；②**dQwen3.5**：用**大约一半的训练数据**把**标准 Qwen 模型转成扩散模型**；③（另一篇 Zarya 我们第二十辑已收）。文中把 DeepSeek 09-12 那个不寻常架构也归为同一股潮流。
- 对我们的意义：**这是"下一批本地模型可能更快"的方向信号** —— 对 16GB Windows 尤其相关：扩散式生成**不按 token 串行**，理论上更适合**算力/带宽受限**的机器（用更少的步骤出更多字）。**但必须是"信号"而不是"现在可换"**：本地运行时（llama.cpp / Ollama）目前对扩散 LLM 的支持尚未成主流，所以答案是**登记为观察项**，不要现在就把它写进选型。可直接抄的**方法**反而是第 ② 条：**"用一半数据把既有模型改造成新架构"** 这个思路，成本远低于从头训 —— 值得留意有没有人做成脚本。
- 去重核查：`dQwen` / `Block Parallelism` 四份基线 **0 命中**（`Zarya` 在 v12 已收，本条**不再重复它**）。

---

## 四、榜单与价格（AA / LMArena / SWE-bench / MLPerf / OpenRouter）

### 18. ⚠️ Artificial Analysis 分数必须带版本号：数据版本 2026-09-22，头部仍是 v4.3 口径
- URL：https://www.datalearner.com/en/leaderboards/external/aa-quality-index （引 Artificial Analysis）· 周报：https://stock.hexun.com/2026-09-23/225049679.html
- 日期：**榜单数据版本 2026-09-22**；周报 **2026-09-23**
- 是什么：DataLearnerAI 镜像显示 AA Intelligence Index **数据版本 2026年09月22日**，覆盖 **270 个模型**，Top：**Claude Fable 5.1 (max with fallback) 53 / GPT-6 Astra (max) 53 / Claude Opus 5 (max) 51 / Muse Spark 1.3 (max) 48 / GPT-5.6 Sol (max) 47**。券商周报（截至 2026-09-21）另给**单任务成本**：最高 **Claude Fable 5.1 (max with fallback) $7.63**，最低 **Muse Glimmer (high) $0.06**；**单任务耗时**：最低 Gemini 3.5 Flash-Lite 0.7 分钟，最高 Qwen3.8 Max(0902) 34.9 分钟；**能力-成本 Pareto 最优区覆盖 GLM-5.3-Flash**；**OpenRouter 上周（09-14~09-20）总调用 128.9T token（环比 +1.7%）、API 调用 53.9 亿次（环比 -2.8%）**，token 用量第一是 **DeepSeek V4.1 Flash 15.8T（份额 12.2%，环比 +219.3%）**。
- ⚠️ 口径提醒（本路必须写死的一条）：**AA 的当前版本口径仍是 v4.3（换过 Terminal-Bench 4.0 / AutomationBench-AA / mini-SWE-agent harness，见第二十辑）**；上面这些分数是 **v4.3 口径下的 2026-09-22 快照**，**不能和 v4.3 以前的分数横向比**。引用时必须写"**AA Intelligence Index v4.3，数据版本 2026-09-22**"。
- 我们的意义：①**这是我们选型表的权威入口，但必须带版本号 + 数据日期两个钉子**；②**单任务成本 $7.63 与 $0.06 相差 127 倍**，同一个榜单上的"第一名"和"最便宜"完全不是一回事；③**OpenRouter 的 token 用量榜是我们观察"世界在用什么"的最短路径**（DeepSeek V4.1 Flash 环比 +219% —— 与我们那周"DeepSeek 撤回涨价 + 上新"的条目互相印证）。
- 去重核查：`AA Intelligence Index v4.3` 在 v20 **已收"改版"事件本身**；本条**新内容 = 数据版本 2026-09-22 的快照 + OpenRouter 周用量 + 单任务成本区间 + Pareto 区**，且**明确标注 v4.3 口径**（这是对第二十辑"必须带版本号"要求的执行）。

---

## 五、游戏引擎厂官方（Unity / Unreal / Godot）

### 19. ★ CESA 官方调查：85.8% 日本游戏开发者已在用生成式 AI —— 但"人不放行就不出"
- URL：https://www.waredata.com/85-8-of-japanese-game-developers-now-use-generative-ai · 中文/数据细项：https://bitcomme.com/85-8-of-japanese-game-developers-use-generative-ai-for-work-cesas-first-survey · https://www.toy-people.com/?p=114565
- 日期：**2026-09-17 发布（TGS 2026 首日，CESA《游戏产业报告 2026 预览版》）**
- 是什么：CESA **首次**自己做生成式 AI 专项调查。**开发者侧**（今年 5–8 月，**1,349 份有效回答**）：**63.0% 日常使用 + 22.8% 偶尔使用 = 85.8%**；另有 8.6% 在试用/评估、4.8% **从未用过**、0.7% 用过就不用了。样本覆盖策划/导演/工程/美术/音效/QA/高管，**不是一个部门的偏好**。**企业侧**（220 家会员中 **48 家**回应）最期待的效果：**效率与生产力 38 家 > 缩短开发周期 30 > 降低开发运营成本 29 > 多语言与全球化 24 > 新表现与新点子 22 > 内容与服务品质 21 > 解决人手不足 20**。**最普遍的管理方式：由人"确认、修改、审核"**；其次是限定可用工具范围、避免直接用生成物。**第一大顾虑：著作权 / 知识产权**。执行董事 **Tsutomu Masuda（增田努）** 的措辞值得记：接受新技术潜力的同时，要**在权利保护**与**以人为本提升开发质量**之间取得平衡。
- ⚠️ 口径提醒：**去年那个 51% 是"企业级"口径，今年 85.8% 是"开发者个人"口径，两者不能直接比**（CESA 自己也没做成一对照）—— 又是一个 M-0019 式的"同一个东西不同口径"。
- 对我们的意义：**这是"独立开发者 + AI"路线目前最大样本量的行业背书**（1349 人，且覆盖反派角色——QA 和高管）。最该抄的是那条**共识性的管理方式**：**限定工具范围 + 人审 + 不用原样产出** —— 这三条恰好就是我们的三层约束（`skills` 白名单 / 闸门 / 人工核发）。另外"**IP 是头号顾虑**"提醒我们：Ren'Py 项目的素材来源要**留可追溯记录**（生成工具、提示词、日期），否则将来难自证。
- 去重核查：`85.8%` / `日本游戏` / `Tokyo Game Show` / `CESA` 四份基线 **0 命中**（v20 §四收的是"外媒：AI 加剧游戏供给过剩"的 Steam 底数，**与 CESA 调查是两件事**）。

### 20. TGS 2026 首设「AI 技术馆」：Meshy 7.1 把一个月的手工 3D 流程压到约 3 分钟
- URL：https://app.cinevva.com/news/2026-09-20-tokyo-game-show-2026-ai-pavilion
- 日期：**TGS 2026 = 2026-09-17~21（最后一天因 25 号台风取消）；Meshy 7.1 于展会前一周发布**
- 是什么：TGS 30 周年，**1,138 家参展商（日本 540 / 海外 598）、3,999 个展位、53 个国家地区**（创纪录）。今年**首设「AI 技术馆」**，14 家公司入驻（Adobe、腾讯云、Meshy AI、Studio51、Heroz、ZEAL 等）。最抢眼的 demo 是 **Meshy**：访客输入角色描述 → 生成 2D 概念 → 转 3D 模型，**展台称过去约一个月的手工流程现在约 3 分钟**。跑的是 **Meshy 7.1**（比 8 月的 Meshy 7 窄）：新增 **Ultra 4K 模式，几何按 4096³ 而非 2048³ 生成，简化前原始网格最高 8,000 万三角面**。厂商自己的 **Detail Richness** 基准（衡量单个渲染像素内仍有精细法线变化、即"表面细节保留度"）：**7.1 = 23.1%**，对比 **Hi3D 3.0 21.9% / Rodin 2.5 21.1% / Tripo 3.1 17.3% / Hunyuan3D 3.1 14.7%**。两个实际限制：**Ultra 4K 只吃单张图**；**下载任何 7.1 结果都要付费方案**。另：**Nexon Games** 带来 RX Studio 的可玩 build《Fareidolia》，有"和角色说话、直呼同伴名字"的语音功能。
- 对我们的意义：①**3D 资产是这轮 AI 渗透最快的一格**（我们 Ren'Py 做视觉小说，主要吃 **2D 立绘/背景** —— Meshy 这类 3D 工具对我们**暂时用不上**，但这说明"资产生成"这条线的成熟度已经超过"AI 直接做玩法"）；②**厂商基准要打折看**（Detail Richness 是 Meshy 为这次发布量身定的指标）；③"**单图输入 + 付费才可下载**"是典型的**试得动、用不起**结构 —— 与我们对本地工具"可否离线、可否免费长期用"的要求正好相反。
- 去重核查：`Tokyo Game Show` 四份基线 **0 命中**（`Meshy` 仅在 v11 作为"3D 生成工具之一"被泛提，**本次是 7.1 的具体版本与数字**）。

### 21. ★ Godot 官方收紧贡献政策：不接受 AI 生成代码、AI agent 提交、AI 写的沟通
- URL：https://app.cinevva.com/news/2026-07-14-godot-bans-ai-contributions （引 Godot Foundation 政策原文 2026-06-30）· 综述：https://www.yomimono.id/tag/godot-engine · 治理背景：https://www.remio.ai/zh/post/acm-open-source-ai-report-warns-faster-coding-is-overloading-human-review-zh
- 日期：**政策 2026-06-30 发布 / 07-01 前后公开**（本路在 2026-09 的引擎综述里再次确认仍生效）
- 是什么：**Godot 贡献给引擎的代码必须是人写的**；AI 只许用于**琐碎工作**（代码补全、正则、查找替换）；**任何用 AI 参与作者身份的情况都要在 PR 讨论里声明**。**同一条规则覆盖沟通**：issue 描述、PR 说明、提案**必须由人写，不能模型生成**；机器翻译可以（前提是原文是人写的）。**自主 agent 与 vibe-coded 提交一直是自动封禁的理由**，现在写进政策。理由不是意识形态而是**责任**：贡献不是一次性交易 —— **写代码的人要理解到能在评审里为它辩护、在它坏掉时修它、几年后还答得上问题**；原文一句很硬：**"我们无法信任重度使用 AI 的人，理解自己的代码到能修它的程度。"**（"We can't trust heavy users of AI to understand their code enough to fix it."）另一条：**合并 PR ≤3 个的贡献者，不经维护者同意不得开新功能或大重构**。背景数字：3 月时 Rémi Verschelde 说 AI slop PR 让维护者**精疲力竭**，**开放 PR 队列 4,681**；政策落地时**已超 5,000**。相关政策生态：**curl 2026-02 终止付费漏洞赏金**（AI 假报告暴增），**2026-07 暂停接收外部漏洞报告一个月**；**GitHub 2026-06 对贡献者加"同时开启 PR 数上限"并**把 Copilot 类 agent 纳入限制；一项 2026 研究称 **78% 项目允许 AI 辅助，其中 74% 强制人类在回路、51% 强制披露 AI 使用**。
- 对我们的意义：**这是本路立场最"反"我们日常做法的一条，必须记下来当反方论据。** ①它和**第二十辑的 "Bend 2 / 先例检查"**是同一根神经：**构建变便宜、评审没变便宜**；②**"沟通也必须人写"**这一条对我们尤其刺：如果我们把 AI 生成的说明直接当成索引站的条目文案，就是在**制造 godot 明确拒绝的那种东西**；③可立刻落地的一条：**我们的 `mistakes/` 和索引站条目都应带"是否 AI 生成、经谁复核"的标记**（这正是"51% 强制披露"的同构要求）。
- 去重核查：`Godot Foundation` / `自主智能体` / `Tidelift` 四份基线 **0 命中**（v11 收的是 **UE 5.8 MCP 插件**与 **Unity 官方插件**，方向相反；本项目是**引擎基金会反向拒绝 AI 贡献**）。

### 22. Godot 官方在 CEDEC 2026：首次 GodotCon 落地日本，CRI Middleware 宣布支持
- URL：https://www.yomimono.id/tag/godot-engine
- 日期：**2026-09-10/11（CEDEC 2026，横滨）**
- 是什么：Godot Foundation 执行董事 **Emilio Coppola** 在 CEDEC 2026 谈基金会的角色与**今年 12 月首次在日本办 GodotCon** 的计划；他说日本企业问得最多的是**"迁移到 Godot 需要对内部做哪些改动"**；同日 **CRI Middleware 宣布支持 Godot 引擎**。落地形态被明确为"**支持公司生态**"而不是基金会直接支持。
- 对我们的意义：**"引擎迁移的真实成本是内部组织改动，不是引擎功能"** —— 这句话对我们有直接用处：我们做 Ren'Py 视觉小说，**换引擎/换工具的真正代价是"我们的房规、闸门、脚本要重写"**，而在引擎选型讨论里这部分几乎从不被算进去。另外"CRI 支持"说明**日本市场的中间件生态在补齐** —— 对一个以日本视觉小说为参照的项目，这是一个环境信号。
- 去重核查：`GodotCon` / `CRI Middleware` / `CEDEC` 四份基线 **0 命中**。

### 23. W4 Games 拿 1,800 万美元 B 轮，腾讯领投（Godot 商业化 + 亚洲）
- URL：https://www.yomimono.id/tag/godot-engine
- 日期：**2026-08-28**
- 是什么：由 **Godot 项目负责人创办**的爱尔兰公司 **W4 Games** 完成 **1,800 万美元 B 轮**，**腾讯领投**；资金用于**国际团队扩编 50%** 与**做企业产品**；W4 与腾讯另签**多年战略合作**支持 Godot 在亚洲的增长。（另一条相关：W4 的 Q&A 澄清**"一键出主机版"需要大量额外工作**，不是真的一个按钮。）
- 对我们的意义：**"开源免费引擎"背后有资本在推动商业化** —— 这对我们是**双面信号**：好处是工具与中间件会变多（第 20 条），风险是**"免费"的部分可能逐步转移进企业产品**。做法上：我们的 Ren'Py 管线**尽量只用社区资产与纯文本**，把"依赖某家公司"的面积压到最小。
- 去重核查：`W4 Games` / `腾讯领投` 四份基线 **0 命中**。

### 24. Godot 在 GMTK Game Jam 2026 首次超越 Unity（47% vs 34%）
- URL：https://www.yomimono.id/tag/godot-engine
- 日期：**2026-08-07**
- 是什么：**GMTK Game Jam 2026（共 10,777 份提交）里，Godot 占统计到的 10,511 款游戏的 47%，Unity 34%，GameMaker 5%，Unreal 3%** —— **Godot 首次领跑该活动**。2022 年还是 Unity 61% 对 Godot 16%，2025 年已接近持平。**但 GDC 行业调查仍显示商业开发中 Unity / Unreal 遥遥领先 —— 这个领先只局限在 jam 里**。
- 对我们的意义：**"jam 领先 ≠ 商业领先"** 是一句很干净的辨别法：**一个工具的流行度要看口径**（谁在用、用来干什么）。对我们直接有用的是：**Godot 是"个人/小团队 + AI 快速出原型"这一格的主场** —— 如果将来要把 Ren'Py 项目往"可玩 3D 或更复杂交互"推，**Godot + 现有 MCP 生态**是比 Unity 更轻的第一站。
- 去重核查：`GMTK` 四份基线 **0 命中**。

---

## 六、对我们的意义汇总（16GB Win / Ollama / Ren'Py / 静态索引站 / Python 脚本）

**这一路 24 条，收敛成四句可以直接用的话：**

1. **"压缩"这件事，官方也承认要么可控、要么别做。** Anthropic 把压缩做成**你按按钮、结果签名不可改**（第 1 条），社区则做**永不总结**（第 10 条）和**守卫裁决**（第十九/二十辑）。三条路指向同一句：**原始记录必须自己留底，压缩产物是替身不是本体**。→ 落在我们身上：`mistakes/` 与日志**永不原地覆盖，只追加**；长会话压缩前**先存档原文**。

2. **"便宜"要看总账，不看单价；"更强"要看循环能不能跑完，不看选择题分。** Databricks 换 Astra **实际多花 60%**（第 8 条），AA 榜上单任务成本 **$0.06 到 $7.63 差 127 倍**（第 18 条）；而 176 组配置的实证说**上下文管理只是防溢出、规划对强模型只是省钱**（第 9 条），675B 模型**幻觉工具调用和小 90 倍的模型一样多**（第 14 条）。→ 落在我们身上：**选型表要按"跑完一个真实任务"的数字排，不按单价排**；**"更大模型"不是安全解，闸门才是**。

3. **确定性的东西要外移成闸门，而且要能合并、要能解释。** jevals 把 8 个 eval 合并成一次请求、方差只有 LLM 裁判的 1/92~1/913（第 12 条），Foremerge 的**冲突检测不调模型**（第 11 条），"确定性 ≠ 纯函数、碎片化回收"（第 15 条）。→ 落在我们身上：`_tools/` 该做的是**把散落的规则判定聚成一层**，并把多次检查**合并成一次编排**（省的是编排开销，不是判定力度）。

4. **"构建变便宜、评审没变便宜"是本辑最大的行业张力，我们站在被质疑的那一侧。** Godot 直接**不收 AI 生成代码与 AI 写的沟通**（第 21 条），CESA 1349 人调查里最普遍的管理方式就是**人确认/修改/审核 + 限定工具 + 不用原样产出**（第 19 条），而 Dan Luu 说"肉代理"对雇员是死路、评审要把 diff 砍到 25%（第 8 条）。→ 落在我们身上：**索引站/`mistakes/` 的每条要能标"是否 AI 生成、谁复核过"**（对应"51% 强制披露"）；**AI 写的闸门脚本必须自己复算一遍**（这是第二十辑踩过的坑）。

**给本机环境（16GB Windows / Ollama）的三条具体动作：**
- **选型表加一列"退役/下线日期"**（第 6 条的六模型退役映射说明写死的模型名一定会过期）。
- **本地模型的下一步观察项登记"扩散式语言模型"**（第 17 条），**现在不换**；同时把 **Ollama 采用规模数据**收进选型表的"可行性"列（第 16 条）。
- **长会话的死锁风险是真的**（第 3 条 "Prompt is too long" 官方直到 09-13 才修）—— 坚持分会话、分阶段写落盘。

---

## 七、下一辑待办

1. **追第 1 条的后续**：Anthropic on-demand compaction 是否会扩到 Bedrock/Google Cloud；有无第三方做**摘要保真度**的对照测试（目前官方只给了机制，没有保真度数据）。
2. **追第 19 条（Godot 禁 AI 贡献）的演化**：其他引擎/基金会是否跟进；我们自己的索引站要不要加"AI 生成披露"字段（与房规去重报告同源）。
3. **把第 11 条（Foremerge）做成最小原型**：多路子 agent 开工前先写"我要查什么"到共享文件，收工前先读它 —— 直接治我们"两路重复/两路 429"的老毛病。
4. **给本地模型加一条"扩散式生成"的观察位**（第 17 条），并留意用"半个数据集改造架构"（dQwen3.5）是否有人做成脚本。
5. **核一次 AA 的指数版本**：下一辑引用 AA 分数时，**必须写清 v4.x + 数据版本日期**（第 18 条已把这条钉死）；若 AA 升到 v5，要专门标注"不可与 v4.3 横向比"。

---

## 八、本路去重报告

**比对基线**：`index.html`（1120 项）+ `csdn-social-summary.md`（第二十一辑骨架）+ `csdn-social-summary-v2.md` ~ `v20.md`（**18 份存档全比**）+ **`_r20/_r20_official.md`**（第二十辑官方路的完整产出，本路额外加比这一份以免与上一辑撞车）。

**因精确命中而剔除（含原因）**
1. **Claude Opus 5.5**（09-22，$4/$20、1M 上下文、四个 breaking API 变更）：`Opus 5.5` 在 **v16 / v18 / v19** 命中多处，**v20 也已剔过一次** → 不收。
2. **GPT-6 Sol / Luna**（09-22）、**GPT-6 Astra**（09-03）：`GPT-6 Sol` / `GPT-6 Astra` 在 v10~v20 大量命中；**v20 已明确剔除** → 不收。
3. **DeepSeek V4.1 Flash**（09-10，552B MoE / CED / 谷时半价）：`V4.1 Flash` / `V4.1-Flash` 在 v6/v12/v13/v16/v17/v19/v20 命中，**v20 §四已收（含撤回涨价 + 谷时价）** → 不收（仅在第 18 条的 OpenRouter 用量数据里作为**用量结果**被引用）。
4. **Kimi K3 on Amazon Bedrock**（09-18，2.8T 参数 / 1M 上下文 / $3-$15）：`Kimi K3` 在 v7（Bedrock 条目）、v10、v12、v17（明列"不重复登记"）、v19 命中 → 不收。
5. **Gemini 3.8 Live / Live Extended Thinking**（09-15，语音智能体、82.6 分语音指数）：`Gemini 3.8 Live` 在 v7、v16、v17（明列已收）、v3/v6/v9 命中 → 不收。
6. **VS Code 1.136（Agent Host）/ 1.138 / 1.139**：`1.136` 在 `_r20_official.md` §七已收、`1.138` 在 v19 已收且 **v20 明列剔除** → 不收。
7. **GitHub Copilot 周报（09-14 周）** 与 **Copilot code review Lite ensemble（09-11）**：`_r20_official.md` §七第 19 条、v19 已收 → 不收（本条只保留 **09-18 的六模型退役映射 + code review GA 的三分类**，属新信息）。
8. **Claude Dreaming / Memory Stores / Projects 重构 / smart reports / Memory topics / Salesforce 插件**：`_r20_official.md` §一**全部已收** → 不收。
9. **Unity 官方 Claude Code / Codex 插件**（09-10 / 09-16，31 项技能）：`_r20_official.md` §五第 14 条已收（含 Claude Code 09-10、Codex 09-16 两个日期）→ 不收（**注意：本路搜索到的搜狐/今日头条二传稿也与之一致，属重复形态③多站改写**）。
10. **UE 5.8 官方实验性 MCP 插件 / UE6 的 MCP 路线（Claude·Gemini·Codex）**：`UE 5.8` 在 v7、v11（已收）、v13 命中；**UE6 的 MCP 路线是 State of Unreal 2026（2026-06）的内容，且已在 v11 一并讨论** → 不收。（本路确认**截至 2026-09 Unreal 仍无第一方内置 AI 助手**，此为增补结论，不单独立项。）
11. **Claude Code 2.1.277 支持 AGENTS.md**（09-18，HN 309 分）：`2.1.277` 在 v17 命中且**已收** → 不收。
12. **Godot MCP Omni**（资产库 #5470，1820 操作 / 59 域 / 自适应工具暴露）：`Godot MCP` / `Godot Omni` 在 v6、v7（判重说明）、v10、v11、v16 命中，**v6 已收 v5.0.5** → 不收（本路所见 5.0.24 只是版本前进，无新机制）。
13. **MLPerf Inference v6.1 / AA 改版 v4.3 事件本身 / The AI Changelog / Grok 4.7 每任务成本 / NInfer 4-bit KV / 4090+Qwen3.8-27B 显存倒推 / kihaya 上下文预算 / 半百万 token 索引 / 失败记忆 > 成功记忆 / Bend 2 先例检查 / 5,000 行未测 PR / SER·PQC**：均在 `_r20_official.md` **逐条已收**（本路全部命中）→ 不收。
14. **Zarya（扩散模型混合架构）**：`Zarya` 在 v12 命中 → 第 17 条**只留 Block Parallelism 与 dQwen3.5，不再重复 Zarya**。
15. **Cursor Cloud Agents / Projects（coordinator agents）**：`Cursor Origin` 与 `coordinator` 命中 v19 / v7 的 Cursor 早期形态讨论 → 第 5 条**只收 3.21.4 的具体 changelog 与 CLI 2026.09.15 的删除清单**。

**因重复形态而合并/降级的**
- **CESA 85.8%** 的中、日、英、葡四语报道（waredata / toy-people / bitcomme / anmtv / cinevva）为**同一事件的 multi-site 改写**（形态③）→ 只保留 waredata 与 bitcomme 两处可互证的细项，**数字以 CESA 官方新闻稿口径为准**（1,349 份开发者回答）。
- **TGS 2026** 的各站报道 → 只保留 cinevva 一处（含 AI 技术馆 + Meshy 7.1 数字）。
- **Anthropic on-demand compaction** 的 5 篇分析（releasebot / modeldex / gloss / clauding / ainewsbank）为**同一 release note 的多方解读** → 数字与坑以 **gloss.run 的逐条坑清单** 与 **modeldex 引 platform.claude 的原文**为准。

**因主题不相关/无稳定信息量而主动不收**：纯融资与芯片条目（Terafab、十万卡等）；匿名免费预览模型（Union Alpha 等）；纯营销的"AI 手游/独立游戏变天"标题稿。

**本路未能确认的**：`Dan Luu` 原文的精确发布日期（HN 讨论 09-19，danluu.com/ai-coding/ 页面未标日）；`Unreal 官方的 UE6 MCP` 只有 State of Unreal 2026 二手转述，**未找到 Epic 官方 release note 原文**（已在第 10 条剔除说明中标注）。

---

## 九、统计

- **条目数：24 条**（编号 1~24，全部给出**发布日期 + 完整 URL**）
- 分节：厂商官网 / Release Notes **4** 条（1~4）· 编辑器与平台 **3** 条（5~7）· 海外社区 **10** 条（8~17）· 榜单与价格 **1** 条（18）· 游戏引擎厂官方 **6** 条（19~24）
- **带指数版本号标注的榜单引用：1 处**（第 18 条，明确写"**AA Intelligence Index v4.3，数据版本 2026-09-22**"，并声明**不可与 v4.3 以前横向比**）
- **区分「单价 / 每任务成本 / 实际总花费」的条目：2 处**（第 8 条 Databricks +60% 实际账单 vs 榜单每任务；第 18 条 $0.06~$7.63 单任务成本区间）
- **明确标注 GA / beta / preview 的条目：5 处**（第 1 条 beta header `compact-2026-09-04`；第 4 条 auto 模式；第 5 条 flag-gated 的本地 Ollama 路径；第 7 条 Assisted Approvals = Public Preview；第 6 条 code review = GA）
- **时效**：绝大多数为 **2026-09-10 ~ 2026-09-22**；两条例外为机制性强的更早事件（第 19 条 Godot 政策 2026-06-30、第 23 条 W4 Games 2026-08-28），均已标注原日期。
- **本路新增（相对 v20 官方路）**：全部 24 条在 `index.html` + 18 份存档 + `_r20_official.md` 中**关键词 `grep -iF` 零命中或经上下文判定为新增量**；**剔除/降级 15 组**（详见 §八）。
- **文件落盘**：本文件 `D:\34498\Documents\github-projects-invest-games\_r21\_r21_official.md`，UTF-8，**分 4 批增量写入**（骨架 → 第 1 批 1~7 → 第 2 批 8~18 → 第 3 批 19~24 + 汇总）。
