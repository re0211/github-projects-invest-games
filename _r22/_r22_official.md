# 第二十二辑 · 官方与海外路（厂商官网 / Official Docs / 海外社区 / 榜单与指标 / 游戏厂 AI 政策）

> 子 agent：r22-official · 日期 2026-09-24（周四）
> 骨架已落盘（房规 #47：边做边落盘，防限流全丢）。每查到 3~5 条追加一次。
> 去重基线：`index.html`(1128) + `csdn-social-summary.md` + `csdn-social-summary-v19/v20/v21.md` + `_r21/_r21_official.md`

## 本路覆盖来源
- 厂商官网 / release notes：Anthropic · OpenAI · Google DeepMind · DeepSeek(DSH) · Qwen · GLM · Kimi · Doubao · MiniMax · xAI · Meta · Mistral
- 编辑器与平台：VS Code · GitHub Copilot · Cursor · JetBrains · Windsurf · Zed
- 海外社区：Hacker News · r/LocalLLaMA · r/ChatGPTCoding · DEV.to · note.com · Zenn
- 榜单与指标：Artificial Analysis · LMArena · OpenRouter · SWE-bench · Epoch AI · The AI Changelog
- 游戏引擎厂：Unity · Unreal · Godot（AI 生成内容政策）

## 已知已收（不再重复，除非有后续进展）
见 `_r21/_r21_official.md` §八 全表。要点：Claude Opus 5.5 / GPT-6 Sol·Astra / DeepSeek V4.1 Flash /
Kimi K3 Bedrock / Gemini 3.8 Live / VS Code 1.136·1.138·1.139 / Copilot 09-18 周报 / Claude
on-demand compaction / Claude Code 2.1.266~270 / Cursor 3.21.4 / JetBrains Copilot 1.18.0 /
Godot 禁 AI 贡献 / CESA 85.8% / TGS 2026 / AA v4.3 快照 / Meshy 7.1。

---

## 一、模型测评与上新（厂商官网 / release notes）

### 1. Qwen-Image-2.1 悄悄把许可证从 Apache-2.0 收成"仅非商业"（阿里通义 / Qwen）
https://muhammad-ahmed.com/blog/ai-brief-an-alpha-channel-and-a-licence · 2026-09-20（模型卡 09-20 09:41 UTC 公开）
**是什么**：Qwen-Image 1.0 是 **Apache-2.0**，可商用、无需协商；**2.1 换成了 Qwen Research License，授权"for non-commercial purposes only"**，把"非商业"定义为研究或评估，**并且限制延伸到了"用它的输出训练出来的模型"**。想要升级的团队面对的不是版本升级而是**和杭州通义实验室谈授权**。模型本身：总参数 **16.22B**（Qwen3-VL 文本编码器 8.77B + 扩散 transformer 7.12B + 自编码器 0.34B），**33.1 GB** 权重、无门禁；**发布帖里一个基准数字都没有**，独立评测者手工测 **7/15 通过**（上一版 4/15）；RTX 4090 上 int8 约 **5 秒**出 1MP 图，Q8 运行时占 **15,645 MB**。
**对我们的影响**：Qwen-Image-2.1 本体上一辑已收（v19 记的是它在 Arena 图像榜开源第一），**这一条是新信息 = 许可证收窄，且收窄时没公告**。对我们是**选型红线**：Ren'Py 项目将来若用生成图做立绘/背景，**"可商用"必须写进选型表并留原文链接**，不能只看"开源"两个字 —— 这正是 M-0019 式"同一个词（开源）不同口径"。
**可复用性**：**参考（反面）** —— 本地生成模型一律按"许可证 + 是否可商用 + 输出能否再训练"三列登记；Qwen-Image-2.1 标"不可商用"。

### 2. Anthropic 首次公开"前沿实验室内部 AI 研发进度"指标：Claude 已主导自家约 26% 的研发（Anthropic 官方）
https://www.claudenews.com.br/en-US/edicoes/147-2026-09-20 · 2026-09-17
**是什么**：Anthropic 发布**三项透明度指标**（AI 承担的研发占比 / Agent 监督质量 / 算力分配）：①**Claude 现在"主导"约 26% 的 Anthropic AI 研发**（2 月还不到 1%），**90% 以上任务的协作等级达到"AI 协作"及以上**；②**约 30,000 个研究 agent 并发运行**，**在线监控器只拦下 0.002% 的 agent 决策**；③**约 6% 的研发算力用于安全工作**（在"AI 驱动的 AI 研发"子集里是 12%）。
**对我们的影响**：**这是"agent 当主力"最大尺度的一次自证**，但也顺手给了一个**风险刻度**：0.002% 的拦截率意味着 **50 万次决策才拦 10 次** —— 这个数字既可以读成"可靠"，也可以读成"拦得极少"。对我们维护索引站/写闸门脚本的直接含义：**agent 产出越多，"复核"越不能省**（对应 r21 那条 Dan Luu 的"肉代理"）。
**可复用性**：**参考** —— 我们的多路调研可以照这个格式记三个数：**本辑 agent 产出条目数 / 人工复核改掉的条数 / 被去重闸门拦掉的条数**。

### 3. Anthropic 开"生命科学验证计划"：受审机构把"实时安全拦截"换成"离线用量监控"（Anthropic 官方）
https://www.claudenews.com.br/en-US/edicoes/147-2026-09-20 · 2026-09-17
**是什么**：**beta 项目，和美国政府共同开发**：经过验证的生命科学机构（药物发现、研究生物学、临床开发、制造）可获得 **Standard 或 High-risk Use 授权**，**解锁默认被屏蔽的模型能力**；代价是**把实时安全拦截改成离线用量监控**。先开放 Team/Enterprise，个人 Pro/Max 之后。
**对我们的影响**：**"默认拦死 + 白名单放行 + 事后审计"这套结构，正在成为官方标准动作** —— 这是一条结构性的情报：**闸门不是"加得越多越安全"，而是"默认关、按需开、开完留痕"**。我们现在的白名单式 skill 管理就是这个形状，可以更有底气地坚持"默认不动闸门，需要时显式开"。
**可复用性**：**参考** —— 记入"闸门设计范式"资料，与 Forest 的"默认拒绝"互相印证。

### 3b. Cactus Needle 3：8~29MB 的"只做工具调用"模型，厂商说打平 DeepSeek V4 Flash、独立测试只有 32%（Cactus Compute 开源）
https://byteiota.com/cactus-needle-3-8mb-on-device-ai-without-the-api-bill · 2026-09-17（MIT / Apache-2.0，HF + GitHub + PyPI）
**是什么**：Cactus 开源 **Needle 3**，一个**专做工具调用 / 结构化抽取 / 向量**的端侧基础模型，**整个模型是单个 8~29MB 二进制**，**29M~121M 参数**，架构是 **Laddered Simple Attention Network**（用 Monarch Hadamard MLP 换掉稠密 FFN，**大部分参数放在不耗算力的"engram"n-gram 表里 —— 121M 参数却按 ~50M 的量算，100 MFLOPs/token vs 296**）；**权重压到约 2 bit（CQ2）**；**2~20 每一层都是可独立部署的子网络**；**输出被"从 schema 编译出的 byte-level 语法"约束，保证 JSON 一定可解析**；**每轮返回一个 JSON（函数调用 + 简短推理 + 校准置信度）**，**没有工具匹配就返回空列表而不是瞎猜**。性能：**Mobile Actions（961 条手机指令，精确匹配）上 121M 版 2-bit 得 86.0**，**超过 LFM2.5 1.2B（82.4）、Qwen3.5 0.8B（76.0）、Apple 3B 端侧模型（57.6）**，**接近云端 DeepSeek V4 Flash 的 88.4**；Raspberry Pi 5 上 **400~4,000 token/s**。**关键的反面**：**"打平 DeepSeek V4 Flash"是"微调后的 4 层切片"在 DroidCall 上、而 DroidCall 只有 200 行**；**一位开发者的独立测试把 Needle 3 测成 32.2%（FunctionGemma 90.9%）、精确参数 20.4%（vs 85.2%）**；Cactus 的 Henry Ndubuaku 也直说**"它是任务专用的，上生产前通常需要微调"**；HN 还记录了一个失败：**"我的车撞了"触发了音乐播放**；**工具超过约 10 个就退化**。
**对我们的影响**：①**"小模型不该做成小号聊天机器人，而该做成一个专用组件"** —— 这正好是我们 16GB 本机的方向：**路由/抽取用 8~29MB 的专用模型，判断/写作才用大模型**；②**它每轮带"置信度"并支持"执行 / 请用户确认 / 拒绝"三路分发**，是我们闸门"分级放行"的一个现成形态；③**厂商基准 vs 独立测试 86.0 vs 32.2 的巨大落差**，又一次印证 r21 定的规矩：**厂商数字要打折，必须带测试集版本与是否微调**。
**可复用性**：**参考（观察）** —— 本地 agent 的"轻量路由层"候选；但**独立测试未复现前不落地**，只登记为"端侧工具调用"观察项。

### 3c. Aikido 开源 Altar 1：基于智谱 GLM 5.3 微调的"安全模型"，主打漏洞检测与安全代码评审（Aikido 官方）
https://www.explainx.ai/blog/aikido-altar-1-open-security-model-2026 · 2026-09-23
**是什么**：Aikido 发布**开放权重安全模型 Altar 1**，从**智谱 AI 的 GLM 5.3 微调**而来，目标是**漏洞检测与安全向代码评审**。定位很明确：**让组织把代码与安全敏感产物留在自己可控的基础设施里本地跑**，而不必把源码送去外部 API。同一天的行业简报把它和"AnyJev（Nokia 把开放 LLM 变成决策模型）"并列，作为**"开放权重生态从'发模型'转向'发领域专用、可部署的系统'"**的证据。
**对我们的影响**：**"安全评审本地化"对我们这种把代码/闸门脚本当核心资产的项目是对的方向** —— 我们已有 `skills-security-check` 一类检查，**用本地模型跑安全初筛**比把脚本发到云端更合适。不过要按 r21 定的规矩办：**安全模型的价值在"漏报率"而不在"看起来专业"**，落地前必须**自己造一批已知有洞/无洞的样本去测**（这正是我们 check 脚本的既有做法）。
**可复用性**：**参考（候选）** —— 记为"本地安全初筛模型"的候选，**必须自测漏报后再考虑**。



## 二、上下文与 agent（context editing / compaction / agent 运行时）

### 4. Claude API：会话中途换工具集，不再让 prompt cache 全失效（Anthropic 官方文档）
https://wpnews.pro/news/claude-api-change-tools-mid-session-without-cache-miss · 2026-07~09 陆续上线（beta `mid-conversation-tool-changes-2026-07-01`）
**是什么**：prompt cache 按**固定前缀顺序 `tools → system → messages`** 做哈希，`tools` 在**第 0 位** —— 以前动一下工具数组（加一个、删一个、换顺序），**整段对话的缓存全废**，长会话就得为已经付过钱的上下文再付一次全价。官方的新做法：**`tools` 数组一次声明完、之后永不动**，改用 `role:"system"` 消息里的 **`tool_addition` / `tool_removal` 内容块**控制"此刻模型能看到哪些工具"；引用一个不在 `tools` 里的工具名会返回 **400**，`error.details.error_code: tool_reference_unresolved`。另有 **`defer_loading: true`**：把大工具注册表**先藏起来**，显式 surface 时才让模型看见，省上下文、也减少"工具太多模型挑花眼"。
**对我们的影响**：**这是"上下文是会花钱的资产"这条原则的官方版本** —— 以前"换工具"和"保缓存"不可兼得（要么全开工具、要么开新会话），现在可以**声明一次、按需揭示**。对我们的直接启发：**给本地 agent 配工具时，与其"一次给全"，不如"声明全 + 按阶段揭示"**，尤其 `defer_loading` 对应我们"skill 太多、每次全塞进系统提示"的问题。
**可复用性**：**落地** —— 我们若自建 harness/skill 编排，按"工具声明与可见性分离"设计；`defer_loading` 记为"按需加载 skill"的官方同构。

### 5. Claude API 的中途系统消息与"逐轮提醒"：`clear_at` 让一条指令只活一轮（Anthropic 官方文档）
https://skills.pub/en/skills/anthropics-skills-claude-api-2 · 2026-07~09（beta `mid-conversation-system-clear-at-2026-08-21` / `mid-conversation-output-config-2026-07-01`）
**是什么**：①**中途系统消息**：把 `{"role":"system","content":"..."}` 追加进 `messages` 数组（**不是顶层 `system` 字段**），就能在会话中途下一条 operator 指令而**不破坏缓存前缀**；限定 **Opus 5 / Opus 4.8 / Fable 5 / Fable 5.1 / Mythos 5 / Mythos 5.1** 可用（**Sonnet 5 不行**），**无 beta header**，位置有硬约束（必须跟在 user 消息之后、要么在最后、要么后面跟一条 assistant，**不能是 messages[0]**）。②**逐轮提醒**：给这条消息 `clear_at: "next_user_message"`，它**只渲染一轮**，之后留在 transcript 里但已被清空 —— 文档特别警告**"永远不要删掉更早的副本"**（在 Fable 5.1 上删副本会连带作废其后的 thinking block）。③**中途改 effort**：`output_config:{effort:...}` 配空 `content:[]` 可**从该点起改推理档位且不重置缓存**。
**对我们的影响**：**"临时指令只活一轮"是一个很实用的上下文卫生工具** —— 我们的场景是"这一轮必须用某种格式/必须读某个文件"，以前只能写进长期系统提示（每轮都在烧 token）。同时那条警告**又是一次"别动历史"**：官方明文说删早期消息会让之后的 thinking 失效 —— 与 r21 的 compaction 签名块是同一个教训：**压缩/清理的产物动不得，历史不是随便能改的**。
**可复用性**：**落地（概念）** —— 我们的 agent 编排可以引入"TURN 级指令"概念：只对当前轮生效的约束单独放，不污染长期提示。

### 6. DeepSeek Harness v0.1.6-alpha.1：headless 可续会话、SSH 远程工作区、PTC 移出主进程（DeepSeek 官方 release note）
https://yage.ai/share/ai-news-weekly-boundaries-en-20260920.html · 2026-09-15（v0.1.7-rc.1 = 09-17）
**是什么**：DSH 把三件事一次性改掉 —— ①**headless 会话续期**：外部脚本以前每次调用都拿到一个随机 session ID、跑完即退，cron/CI 无法把后续命令喂回上文，社区只能靠 `dsh-resume-headless` 这类补丁；新版本正式加了"**adopt-only**"的会话沿用标志：**可以指定旧 session ID 续跑、用 stdin 继续喂任务、用 NDJSON 把运行事件实时回吐给监控脚本**；找不到 session ID / 工作目录不符 / 被别的进程锁住时**快速失败，而不是悄悄开一个空白新会话**（避免流水线攒下无主状态）。②**SSH 远程工作区**：**协调器、API key、本地会话记录留在本机**，**所有文件读写/代码检查/命令执行全走 SSH 到远程 POSIX 服务器**，远程预装一个 **SHA-256 校验**的 helper 代执行；**SSH 掉线立即报错，不自动重连重放**。③**PTC（Programmatic Tool Calling，模型写 TypeScript 脚本批量调本地工具）从主进程内置 worker thread 移出**，改在**干净隔离子进程**里跑模型生成的代码。**v0.1.7-rc.1（09-17）**追加侧栏终端/网页/子代理/提交计划、插件管理页、会话 pin/归档。
**对我们的影响**：**三条都是我们环境的正面消息**：①"**续不上就快速失败，绝不悄悄开新会话**"正是我们坚持的"错不起的步骤确定性化"，而且它治的就是我们"后台 agent 跑完就找不到"的老毛病；②**SSH 远程工作区 = "本机留 key、远端干活"**，对"16GB Windows 本机不够跑重活、但不想把 key 丢到云上"是一个可抄的分工；③**"模型写的代码必须在隔离进程里跑"** 给我们的 check 脚本提供了一个更硬的边界（我们目前是靠"只读 + 白名单"）。
**可复用性**：**落地（观察）** —— DSH 是我们的核心工具，记下这三条行为变化；"adopt-only 续会话"与"远端执行不自动重放"两条直接进我们的 agent 编排规范。

### 7. OpenAI 把 Codex 的 agent harness 做成 API：Agents API 公测（OpenAI 官方）
https://www.analyticsinsight.net/amp/story/artificial-intelligence/how-ai-is-changing-code-editors-in-2026 · 2026-09-10（公测）
**是什么**：**Agents API 公测**，开发者可以**直接调用 Codex 的 agent harness**（长会话、工具、子代理、文件、代码、可切换算力环境）。同文给了一组可核对的采用数字：**Codex 在 2026-02 发布前的一个月里被超过 100 万名开发者使用**；**Cursor 的 cloud agents 现在产出其内部已合并 PR 的 60% 以上**。
**对我们的影响**：**"harness 被单独当产品卖"是这一辑反复出现的主题**（DSH、Codex harness、Claude Code 的 mods）—— 官方开始承认 **"调度层"和"模型层"是可分离的两件事**。对我们意味着：**换模型不一定换工作流**，反过来**工作流/harness 的选择开始独立于模型选择**。这条同时也是给我们自己"多路调研如何调度子 agent"的一个参照系。
**可复用性**：**参考** —— 不必接（要云 key），但"harness 与模型解耦"这个判断写进我们的选型原则。



## 三、Memory 管理

### 8. 五朵云的"让 agent 记住事"五种设计：Anthropic 全 client-side、Google 全托管（quidproquo 综述，逐条引官方文档）
http://quidproquo.cc/posts/ai/2026-09-19-cloud-platform-memory-apis-en · 2026-09-19
**是什么**：把 OpenAI / Anthropic / Google / AWS / Microsoft 五家的记忆 API 摆在一张表上，**最值得抄的是 Anthropic 那一路的具体参数**：①**context editing**（beta `context-management-2025-06-27`）两个清除器 —— **`clear_tool_uses_20250919`（触发阈值 100k token、保留最近 3 条、可用 `exclude_tools` 排除）**与 `clear_thinking_20251015`，服务端执行并回报 `applied_edits`；**和 memory tool 一起用时，Claude 会先收到"先存进记忆再清"的系统提示**。②**memory tool** 是 **client-side 工具定义**（`{"type":"memory_20250818"}`）：Claude 对 `/memories` 目录发 view/create/str_replace/insert/delete/rename，**由你的程序执行，Anthropic 不碰你的存储**；自动注入的指令是"**做任何事前先看记忆目录，并假设随时会被中断**"；**存储 / 租户隔离 / TTL 全是应用的责任**，文档明说要防**路径穿越**。③**Managed Agents memory stores**（beta `agent-memory-2026-07-22`）：**workspace 级文本文件集合，建会话时用 `resources[]` 挂载（每会话最多 8 个）到 `/mnt/memory/...`**，权限 `read_write` / `read_only`；**每个 store ≤4,096 字符指令、单条 ≤100 kB、单 store ≤2,000 条**；**版本不可变、保留 30 天、可 redact 但不可 restore**；跨 agent 共享靠**同一 store 用不同权限多次挂载**。对照组：**Google Vertex AI Memory Bank** 是反过来"平台替你抽取分类检索"（内置 `USER_PERSONAL_INFO` / `USER_PREFERENCES` / `KEY_CONVERSATION_DETAILS` 三类主题）。
**对我们的影响**：**这是一张"记忆分层怎么切"的现成参数表**。对我们最有用的三条：①**"清上下文之前先把要点写进文件"**（Anthropic 把它做成了系统级提示）—— 正是我们"长会话压缩前先存原文"的官方版；②**memory tool 的"假设随时会被中断"** 与我们的分阶段落盘同源；③**"存储、隔离、TTL 都是应用责任"** 提醒我们：**记忆不是平台功能，是要自己维护的文件约定**。
**可复用性**：**落地** —— 我们的 `mistakes/` + 日志索引就是这个模型的手工版；把"触发阈值 / 保留最近 N 条 / 排除清单"这三个旋钮记下来，将来若做自动清理照此设计。

### 9. Claude Code 官方上下文文档：压缩之后"什么能活下来"有明确清单（Anthropic 官方文档，09-19 阅读）
https://vucense.com/ai-intelligence/ai-infrastructure/claude-code-turboquant-context-optimization · 文档读取日 2026-09-19
**是什么**：把 Claude Code 的上下文规则逐条摊开：①**窗口**：Fable 5.1 / Fable 5 / Sonnet 5 / Opus 4.6+ / Sonnet 4.6 列 **1M**，默认在**约 967K** 触发自动压缩；可用 **`CLAUDE_CODE_DISABLE_1M_CONTEXT=1`** 强行钉在 200K；**`/autocompact 500k`** 可把自动压缩点设在 **100K~1M** 之间。②**启动时加载**：系统提示 + 你的 CLAUDE.md + **auto memory 的前 200 行或 25KB** + MCP 工具名 + skill 的一行描述（**MCP 工具 schema 默认延迟加载**）。③**压缩后谁活下来**（最关键）：**项目根 CLAUDE.md 与不带 `paths:` 的规则会从磁盘重读**；带 `paths:` 的规则和子目录 CLAUDE.md **只在你下次读到匹配文件时才回来**；**Claude 会重读最多 5 个它读过/改过的文件（新的优先）**；**超过 5,000 token 的文件只以路径引用回来、不带内容**；**被调用的 skill 会重新注入，单个封顶 5,000 token、总计 25,000**。④官方建议 **单个 CLAUDE.md 控制在 200 行以内**（越长越吃上下文、依从性越差），**import 不能绕过**（导入文件同样在启动时加载）。
**对我们的影响**：**这是"什么该写进长期提示、什么该按需加载"的官方裁决书** —— 一条必须全局长驻的规则就放**项目根 CLAUDE.md**，其余按 `paths:` 拆出去按需加载；这正是我们"骨架/规则分层"的对标。另外两条立刻可用：**"大文件压缩后只留路径"** 说明**别指望压缩记住文件内容**（要它记住就写进 md）；**"skill 重注入有 5,000/25,000 token 上限"** 直接解释了"skill 装太多会互相挤"。
**可复用性**：**落地** —— 把"≥5,000 token 的文件压缩后只剩路径""CLAUDE.md ≤200 行""autocompact 阈值"三条写进我们的 agent 使用规范。

### 10. AWS 重做 Bedrock AgentCore 运行时：内存"用完就还"，冷启动钉在 ~2 秒（AWS 官方）
https://www.unite.ai/aws-reworks-bedrock-agentcore-runtime-for-elastic-memory-fast-cold-starts · 2026-09-18（`platformVersion: V2`）
**是什么**：AgentCore 的托管算力层改版：**每个会话从小内存档起步、按需分页加载，agent 一释放缓冲/缓存过期平台就把内存收回去**（老版是**从分配到会话结束一直占着高水位**，长时/突发 agent 要为自己没在用的内存付整天的钱）。**冷启动**：AWS 用**空 echo agent** 在 us-west-2 调 us-east-1（含跨区往返）测 **每种 agent 5,000 次冷调用 × 5 种镜像大小**，**新版 P75 冷启动约 2 秒、从 200MB 到 2GB 镜像都一样**，老版随镜像从 **约 5.4 秒涨到近 30 秒**；echo agent 自身代码 P75 只跑 **约 34 ms**，**几乎所有时间都是平台启动**。机制是"**容器起一次 → 拍快照 → 之后都从快照恢复**"，快照会**剥掉缓存与临时内存**，所以镜像变大快照也不涨。计费改成"**按实际用到的内存**"。
**对我们的影响**：**"冷启动几乎全是平台时间、跟镜像大小无关"是一句很好的性能常识**（调试时别怪自己的代码）；而"**内存从'一直占着'改成'按用付费'**"与我们 16GB 本机的处境同构 —— **我们本地的 Ollama 也是"模型一加载就占住显存/内存"**，真正省的做法是**用完卸载 / 只加载当前任务需要的模型**，而不是常驻。**可复用性**：**参考** —— 只作性能模型参照，我们不用 Bedrock。

### 11. 两篇 preprint 指出"记忆信任缺口"：agent 过度相信过期事实、记忆后端默认不执行"撤销"（AI Agent Store 周报）
https://aiagentstore.ai/ai-agent-news/topic/human-agent-trust/2025-04-08 · 周报覆盖 2026-09-22 当周
**是什么**：两篇预印本量化了 agent 记忆的系统性失败：①**《The Memory Trust Gap》**：带持久记忆的 agent **会过度采信过期事实**（在 Qwen3 多个尺寸上测），**不会优先采用权威证据**；②**《Revoked but Still Authoritative》**：**流行记忆后端默认不执行"撤销"** —— **被撤销的记录仍常被检索出来，并能触发不安全动作**。给出的缓解是**在 agent 与记忆之间加守卫层、把撤销强制放在检索时执行**。同一周报里还有厂商动作：**UiPath 九月版加 AI Trust Layer 开关（Context Grounding + "LLM as Judge" 护栏）**，另有项目做**签名"trust receipts"**与更细的 agent trace/span 元数据。
**对我们的影响**：**"记忆是缓存不是真理源"** —— 这条对我们直接成立：我们的索引/日志里的旧条目**如果与现状冲突，必须以可核实的当前文件为准**。落地动作很清楚：**记忆条目要有 TTL 或"复核日期"，撤回必须真的删/标废，而不是"我下次不查它了"**。这与我们"每条索引都带日期 + 原文可追溯"的做法是同一条原则的更硬版本。
**可复用性**：**落地** —— 给 `mistakes/` 与索引条目加"最后复核日期 + 是否作废"两个字段（作废不是删行，是显式标废并保留原因）。



## 四、IDE 与 Copilot 类 changelog（VS Code / Copilot / Cursor / JetBrains / Windsurf / Zed）

### 12. Claude Code v2.1.281：`"attribution": false` 一键去掉 AI 署名，Auto 模式分类器扩到只读命令（Anthropic 官方 release notes）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-23（v2.1.281；前一日 v2.1.280 = 09-22）
**是什么**：①**`"attribution": false`** 写进 `settings.json`，**所有 commit 与 PR 上的 AI 署名文案全部去掉**，全组织一次生效 —— **但旧版 CLI 看到这个布尔值会直接跳过整个配置文件**，混用版本时要保留旧的 object 格式。②**`CLAUDE_CODE_AUTO_MODE_SERVER` 扩到直连 Anthropic API**（设 1 显式开、0 回退到**会计入用量的本地分类器**）；**在服务端分类器下，连只读/沙箱命令也要过审、被标就拦**。③**新增 `/insights` 建议**：估算你**最近会话里有多少权限提示本来可以被 Auto 模式自动处理**。④危险 `rm` 的确认框改成**等 2 分钟才拒绝**（无人值守会话不再卡死，`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` 关掉）。⑤自托管 runner 的**系统提示改走私有文件**（`--system-prompt-file`），**修掉"提示太大导致执行失败"**。⑥`claude plugin validate` 现在也校验 MCP（提前报出 `.mcp.json` 里会被静默丢弃的条目、未声明的 `${user_config.*}`、不安全 URL）。共计 **180+ 项改动**。
**对我们的影响**：①**`attribution:false` 是"要不要在产物里暴露 AI 参与"的官方开关** —— 与 r21 的 Godot 禁 AI 贡献、Steam AI 披露（本辑第 22 条）构成同一个辩论的三方立场；我们的索引站条目要不要标"AI 生成"也因此多了一个对照；②**"只读命令也要过分类器"** 是**收紧**而非放松 —— 提醒我们"只读 = 安全"这个假设在官方那里已经不成立，我们自己的白名单也不能拿"只读"当免检理由；③**`/insights` 先估算再改配置** 这个"先用数据再决定"的做法可以直接抄（我们改闸门配置前也该先统计）。
**可复用性**：**参考+落地** —— ④⑤两条直接抄（长等待超时、大提示走文件）；①②作为政策立场登记。

### 13. Claude Code 的 AGENTS.md 与遥测开关被绑在一起：关掉遥测会静默不读 AGENTS.md（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-23 发现
**是什么**：有人发现**关掉用量数据上报后，Claude Code 会连带不再读取项目的指令文件 AGENTS.md，且没有任何警告** —— 因为**本地文件读取这个功能与"从服务器取数据"共用同一个开关**，关掉遥测会把一个**不相关的本地功能**一起关掉。
**对我们的影响**：**"关一个开关，静默关掉另一个不相关功能"是我们最该防的一类坑**（它不报错、只是行为变了）。对我们直接相关：我们的房规/AGENTS 类文件如果哪天"没生效"，排查方向要包括**"是不是某个网络/遥测开关把它顺手关了"**。**可复用性**：**落地（排查清单）** —— 记一条：**"规则文件没被读到"先查遥测/隐私开关，再查文件名与路径**。

### 14. Codex CLI 0.156：全屏 TUI、语音默认开、`/usage` 用量看板、worktree 默认开（OpenAI 官方 changelog）
https://help.openai.com/en/articles/11428266-codex-changelog · 2026-09-18~19（0.156.0 / 0.156.1；0.155.0 = 09-17）
**是什么**：**0.156** 新增 **`/tui` 全屏界面**（transcript 搜索、鼠标选择、右键复制）、**语音会话默认开启**（F8 切换、Linux/Windows 打包音频运行时）、**`/usage` 分析看板**（账号用量、token 总量、插件与 skill 活动）、**worktree 默认开启**、六套新主题 + 在回复里渲染 Mermaid 图与公式、**`/daemon` 更新本地后台服务（`--no-daemon` 绕过）**。**0.155（09-17）**先加了**实验性 `/voice`**、**状态行实时显示推理摘要**、**agent 概览的任务隐藏/归档/删除**、**Touch ID 验证 MCP 请求**（支持的 Mac）、**可配置的 daemon 更新计划**、**Amazon Bedrock 支持用命令取 AWS 凭证（带缓存与过期刷新）**；并修了一条关键的：**"compaction 在回合开始前失败时，已接受的 prompt 现在会被保存"**。**0.154** 引入 **GPT-6 Astra 进模型选择器**与**实验性 worktree**。
**对我们的影响**：①**`/usage` 把"token 总量 + 插件/skill 活动"做成看板** —— 正是我们"成本要看总账不看单价"（r21 第 8/18 条）的工具化；②**"compaction 失败别把用户输入丢了"** 是我们长会话最怕的静默数据丢失，官方修了这条值得记；③**worktree 从实验转默认**说明"隔离检出"已成主流工作方式 —— 我们做多路调研时**用隔离目录而不是同一个工作树**是对的方向。
**可复用性**：**落地（习惯）** —— 若用 Codex CLI，先开 `/usage` 建成本基线；worktree 隔离写进我们的多 agent 规范。

### 15. Zed 九月版（v1.20.2）：表格数据预览、JetBrains 键位、DeepSeek V4 低推理档（Zed 官方 release）
https://technewsdaily.com/news/zed-delivers-september-updates-for-multiplayer-workflows · 2026-09-17（v1.20.2）
**是什么**：Zed 九月更新：**CSV/TSV/PSV/SSV 表格预览**（可排序、按值筛选行）、Markdown 表格列宽、**Git blame / stash 动作**、**JetBrains 键位改进**（alt-left/right 的 CamelHump 子词导航）、**为 DeepSeek V4 Flash / V4 Pro 增加低推理档（low reasoning effort）**。性能对照（同文给出，v1.3.6 口径）：**冷启动 0.4~0.6 秒 vs VS Code 1.3 秒；空闲内存 180~222 MB vs 650~3,549 MB；输入延迟 2ms vs 12~25ms**。Zed 用自研 **GPUI**（macOS 走 Metal、Windows 走 DirectX）原生渲染，**支持自带 key（Anthropic/OpenAI/Google/本地 Ollama）**。
**对我们的影响**：**"为某个模型单独加低推理档"是编辑器开始真正理解 token 成本** —— 对我们 16GB 本机 + 本地模型路线，**"同一模型可调推理档"比"再换一个模型"更省**。另外那时**"自带 key + 指向本地 Ollama"** 再次出现（r21 第 5 条 Cursor 也有），说明**"编辑器当本地模型前端"在变成标配**。**可复用性**：**参考** —— 记入"IDE 是否能接本地 Ollama"的选型对比表（我们关心的是**能不能不装 Electron**）。

### 16. VS Code 1.140 Insiders：Agents 窗口继续加厚（自定义聊天背景、Voice Mode 会报并行会话状态）（Microsoft 官方）
https://code.visualstudio.com/updates/v1_140 · 2026-09-21（Insiders）
**是什么**：1.140 Insiders 目前主要两条：**支持在不选文件夹的情况下、对"可用的远程 agent host"起一个 chat**；以及 Agents 窗口的**自定义聊天背景**（可按深/浅色主题分别设图案或图片，新增 `chat.agentSessions.preferredDarkBackgroundImageLayout` / `...LightBackgroundImageLayout` 两个设置，替代旧的 `backgroundImageLayout`）与 **Voice Mode 的会话感知（实验）**：**能在 Voice Mode 里找到最近的 agent 会话、按标签切换、并回报每个会话的状态**。1.139 侧的另一条（releasebot 记录）：**Agents 窗口修复多任务/嵌套后台 agent 的可见性 —— 任务一启动就显示所用模型、父子任务卡片不再自动折叠、切会话/重启不丢进度**。
**对我们的影响**：**"后台 agent 任务可见化"（模型名提前显示、幽灵子任务保留卡片、会话状态不丢）直接对应我们"后台 agent 跑起来就看不见进度"的痛** —— 这是官方的 UI 级答案；**Voice Mode 能报每个会话状态**则说明"用语音指挥多个并行会话"开始被当真。我们对"背景图"不感兴趣，但**"任务生命周期全程可见 + 模型名提前知道"这两条可以作为我们自己日志面板的设计参考**。**可复用性**：**参考** —— 记入"多 agent 可见性"设计参考；不必升级。

### 17. Cursor 开始卖"自托管机器"：把源码、构建产物、密钥、工具执行都留在企业自己网内（Cursor 官方方向）
https://www.analyticsinsight.net/amp/story/artificial-intelligence/how-ai-is-changing-code-editors-in-2026 · 2026-09（Cursor 自托管机器）
**是什么**：Cursor 九月加入**自托管机器（self-hosted machines）**：企业可以把**源码、构建产物、密钥与工具执行全部留在自己网络内的机器上**；同时可把 cloud agents 接到 **AWS / Cloudflare / Modal / Vercel** 等基础设施。官方口径还有两个数字：**Cursor 的 cloud agents 现在产出其内部已合并 PR 的 60% 以上**；Projects 的 coordinator 能把大任务**拆给成千上万个子 agent**、**项目上下文能保留数月**。
**对我们的影响**：**"agent 的算力边界"正式成了产品卖点** —— 从"用谁的模型"转向"**agent 在哪台机器上跑、能碰到什么**"。对我们这种**本机跑、数据不出门**的用法是一个正向信号（大厂在往"可控执行环境"做）；也提醒我们：**我们真正的资产不是模型，是"哪些文件允许被碰"的边界**（与 DSH 的 SSH 远程工作区是同一类设计）。**可复用性**：**参考** —— 记入"agent 执行边界"资料；`60% 内部 PR 由 cloud agent 产出`这个数字可作"agent 成熟度"标尺。



## 五、vibe coding 官方政策与工具

### 18. HN 当日第一名的"翻车实验"：OpenJev 拿 521 分，热评前十条**全都在骂它的落地页**（HN / Lobsters 日报）
https://daily.steinslab.io/en/posts/vol-98-2026-09-19 · 2026-09-19
**是什么**：当日 HN 提供了一个干净的对照：**OpenJev 冲到第一（521 分）**，但**点进评论区，前十条热评没有一条在讨论产品本身做什么，全在拆它的落地页**。最高赞写的是："**一次性的 vibe-coded 站点永远是视觉灾难：无穷的填充文案、遍地陈词滥调、对可用性零关心。**" 第二条把比喻升级：当前的 AI 产出像"**一个焦虑的学生写的学期论文 —— 该被编辑得聚焦清晰的地方，反而被反向编辑，拼命塞进多余细节，默认读者没得选只能读下去。**" 同一天 Lobsters 把 McSweeney 的讽刺文《We Must Create the Shit Machine》推到 89 分 —— **"形式完整却毫无内容"的产出已经多到成为可被嘲讽的独立文体**。日报把根因写得很直接：**"这是一件成品"与"到底是谁做的"已经完全脱钩。**
**对我们的影响**：**这是我们维护"索引站"最该照的一面镜子** —— 索引站就是"给人读的产出"，**填充文案、陈词滥调、零可用性**正是它最容易得的病。对照我们自己的标准（每条要有 URL + 日期 + 数字 + 可复用性判断），**这份"热评清单"实际上是一份负面验收单**：如果我们的条目去掉数字之后仍然成立，那它多半就是"焦虑学期论文"。
**可复用性**：**落地（验收）** —— 把"**去掉具体数字后这条还成立吗？**"加进我们的条目自检；"形式完整 ≠ 内容有用"写进攻略。

### 19. "token 便宜到不值得计量"：成本降到不再是瓶颈，瓶颈变成"够不够得着质量标准"（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-24
**是什么**：一篇《Tokens too cheap to meter》的论点：随着 AI 使用成本持续下降，**"烧了多少 token"不再是关键，"能不能达到你要的质量线"才是**；AI 也在从"独立产品"往"基础算力设施"移动。同文的两个具体判断：**顶级模型的 token 单价不一定降，但"模型 + GPU + 推理软件"的综合改进意味着"完成同一个任务的成本"一直在降**；**Opus 5.5 的推理档位成本/性能权衡指向同一个结论 —— 按"够到你要的质量"去调档，而不是按"省 token"去调档**。
**对我们的影响**：**这是一条"选型纪律"的提醒**：我们过去按"便宜"比价（单价 vs 总账），但**当 token 便宜到一定阈值以下，继续优化它的边际收益低于"把质量线提上去"**。对我们这种个人维护索引站的场景，可操作版本是：**本地/便宜模型负责"量"（初筛、抽取），贵的模型只在"质量线"上出手**；**别再为省一点 token 牺牲条目质量**。
**可复用性**：**落地（预算原则）** —— 把"按质量线选档位、不按 token 选档位"写进我们的模型使用规范。

### 20. Stripe 内部 AI 平台 Kai：4,000+ 个各自为政的 agent 催生一个"统一层"，83% 员工每周在用（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-24
**是什么**：Stripe 做了内部 AI 平台 **Kai**（售前客户调研、财务分析、合规审查），**宣布时已被 83% 的员工每周使用**。它**是从一团乱里长出来的**：**此前用各种工具堆了 4,000+ 个 agent，反复重复相似的 prompt，产生质量与维护灾难** —— Kai 是大组织**收束"内部 agent 泛滥"**的案例。
**对我们的影响**：**"agent 繁殖失控"是任何 agent 用户的必然阶段** —— 我们有几十个 skill / check 脚本 / 各路调研 agent，**重复点已经是"相似 prompt 反复重写"**。Stripe 的解法不是"更努力地管住每个 agent"，而是**做一个统一的上层（Kai）**。对我们的直接启发：**索引站 / `_tools/` 应该承担"Kai 那一层"的角色**（统一入口 + 复用的 prompt/检查），而不是继续让每个流程各写一份。
**可复用性**：**参考（架构）** —— "先有一层统一入口，再谈管住单个 agent"；`83% 员工周用`与`4,000+ agent`两个数字可作规模参照。

### 21. 「我不能一直这样下去」：全公司把 AI 输出叠在 AI 输出上，开发者每天指挥 AI 12~13 小时（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-23
**是什么**：一位**入职大公司两周**的开发者记述：所在环境里 **Claude Code 生成一切 —— 规格、代码、测试、产品需求、工单、报告**；**领导层不断催速度，问"写代码都不是瓶颈了为什么还这么慢"**，而**开发者每天要指挥 AI 12~13 小时，正在被榨干**。日报把它和 09-20 那句"**别把需要真正思考的写作交给 AI**"并置：前者是个人层面的建议，这篇是**当整个组织把 AI 输出叠在 AI 输出上、不做验证时，人会发生什么**。
**对我们的影响**：**这条是对"agent 越多越好"的反向校准**，也和我们上一辑记的 Dan Luu"肉代理"是一体两面：**省下来的时间如果没有变成"更高的交付标准"，省下来的是赤字不是红利**。对我们个人维护者尤其真实：**唯一不能外包的环节是"判断"**（什么该收、什么该弃、哪条是重复）—— 本辑三路调研的"人工去重 + 交叉区"就是这条的实践。
**可复用性**：**参考（红线）** —— 记一条纪律：**每轮调研必须有"人工复核改掉/剔除"的记录**，否则就是"AI 叠 AI"。

## 六、游戏制作 / 引擎厂 AI 政策与工具

### 22. Steam AI 披露半年数据：**每 3 款新游有 1 款标了 AI**，9 月上半月逼近一半（SteamData.AI 统计 / 游戏站解读）
http://gamedevaihub.com/steam-ai-disclosure-guide · 数据窗口 2026-01-01~09-15（第三方 SteamData.AI 统计）
**是什么**：第三方站 **SteamData.AI** 统计 **2026-01-01 至 09-15 Steam 发售的 25,899 款新游**：**带 AI 披露标识的 8,651 款 = 33.4%**（每 3 款 1 款）；**斜率**：年初 28.7% → 8 月 43.7% → **9 月前 15 天 48.5%**。这批游戏的**定价中位数 4.99 美元，84.9% 低于 10 美元，20 美元以上仅 3.4%，免费占 10.4%** —— **AI 披露与"低价小体量独立游戏"高度绑定**。另一组常被引用的商业数字：**AI 披露游戏约占新发行三分之一，但估计销量只占 10%~27%**。规则侧：**Valve 2026-01-16 重写披露指引 —— 只有"玩家能看见/听见的内容"（美术、音频、叙事文本、本地化、宣传素材）必须申报，"幕后用代码助手"豁免（GitHub Copilot 明确豁免）；实时生成内容仍必须披露且要说明护栏；实时生成的 Adult Only 性内容绝对禁止**。
**对我们的影响**：**这是"AI 参与游戏制作"目前最大的一份实测底数**，而且它给的是一条**冷静的结论**：**标签不等于质量**（好评率中位数仍 87.5%，见中文侧样本），真正被压的是"铺量的曝光"。对我们的 Ren'Py 项目：①**如果用到 AI 生成的美术/配音/文案，Steam 上要申报，且宣传图（capsule）也算**；②**代码助手豁免**这一条让我们可以放心用 AI 写脚本/闸门，但**不能用它来省掉"素材来源可追溯"**（与 r21 CESA"IP 是头号顾虑"一致）。
**可复用性**：**落地（合规）** —— Ren'Py 项目建一张"素材来源表"：素材名 / 生成工具 / 提示词 / 日期 / 是否需 Steam 披露；**代码助手不填**。

### 23. Steam 是唯一"强制 AI 披露"的大店；EU AI Act 第 50 条已在 2026-08-02 生效，中国 2025-09-01 起"双标注"（VGTimes 综述）
http://www.vgtimes.com/articles/168308-ai-in-games-backlash-boycotts.html · 综述于 2026-09
**是什么**：把"AI 与游戏"的**平台规则 vs 法律**分开摊：**平台侧** —— **Steam 是唯一有详细强制披露规则的大店**；**Epic Games Store 由开发者自定、itch.io 只对"售卖的素材"要求、PlayStation/Xbox/Nintendo/Apple 均无专门 AI 标签**；Google Play 只要求"能按用户提示生成内容"的应用提供举报途径。**Tim Sweeney 公开反对 Valve 的做法**，先说"商店应放弃 AI 披露要求"（理由是 AI 很快会被用在几乎所有游戏里），后称该标签是**"公开的污名"**、会招来想害这款游戏的 AI 反对者；曾参与 Counter-Strike 的艺术家 **Ayi Sánchez** 反驳：**AI 披露就像食品包装的成分表**，消费者该知道里面有什么。**法律侧**：**EU AI Act 第 50 条（透明度）自 2026-08-02 适用** —— **玩家在与 AI 控制的角色交互时必须被告知**，AI 生成素材**要带可被自动识别合成来源的技术标记**，但**不要求给传统叙事游戏的每张 AI 贴图/每句 AI 台词贴可见标签**；**违规罚款最高 1,500 万欧元或全球年营收 3%**。**中国**：**2025-09-01 起 AI 生成内容"双标注"（元数据隐藏记录 + 可能误导用户的可见警示）**，对"运行中动态生成的游戏内容"同样适用。**加州**：**2025-01-01 起**，演员的声音/肖像**不能凭含糊合同条款做数字复刻**，必须事先写明具体用途、且须由律师或工会代表。
**对我们的影响**：**"店里不标 ≠ 法律不管"是本条最该记住的一句** —— **发售地避开 Steam 也躲不开 EU/中国的法律**。对我们是两条硬约束：①**若叙事里有"AI 控制的对话角色"，按 EU 第 50 条要告知玩家**（Ren'Py 里加一个声明即可，成本极低）；②**AI 生成的立绘/配音要留"可被识别合成来源"的技术标记**，这直接影响我们"怎么存生成素材"（**别把元数据洗掉**）。
**可复用性**：**落地（合规清单）** —— Ren'Py 项目：发行页 AI 披露段 + 游戏内 AI 角色告知 + 生成素材保留工具/日期元数据。

### 24. Unity 7 对生成式 AI 的官方立场：**"选择权在开发团队，不在平台"**（Unity 官方活动 Unite Seoul）
https://vongola.org/article/unity-7-revealed-zero-rebuilding-smarter-ai-and-open-ecosystem-everything-you-need-to-know · 2026-07-21（Unite Seoul 公布）
**是什么**：Unity 7 定位**Unity 6 的直接延续、主打"零重建"**（不破坏既有项目/代码/技能）。AI 上官方**刻意保守**：Unity 7 会**与开发者现有 AI 工具协同**、用 AI 辅助图形优化、集成广告侧的 Unity Vector，但**不把生成式 AI 设为使用 Unity 7 的必要条件**。**Adam Smith 的原话**："**游戏创作确实在变，创作团队与 Coding Agent 越来越常并肩工作，Unity 7 确实是为这样的世界打造的。但『为这样的世界打造』并不代表『必须使用这些技术』。**" 以及："**如果你的工作室已经决定不让 AI 介入创作，你们并不会因此被排除在这次更新之外……选择权永远属于开发团队，而不是平台。**" 开放架构下 **Coding Agent 可直接接入并验证 Build，制作人可用浏览器查场景而不必开 Editor**；Unity 还提供**可免费使用的 MCP**。对照：**Epic 公布 Unreal Engine 6 时积极强调 AI 对游戏开发的影响**，规划 **2027 年底**抢鲜体验 —— 两家在"版本升级策略 + AI 态度"上明显分叉。
**对我们的影响**：①**"为 AI 时代打造"与"强制用 AI"是两件事** —— 这句话对我们做 Ren'Py 视觉小说的立场是很好的背书：**我们的房规允许 AI 参与，但闸门必须留人的裁决**，与 Unity 的措辞同构；②**"Coding Agent 可不打开编辑器就验证 Build"** 是"AI 在环但不接管创作"的一种具体分工，值得留意 Ren'Py 侧有没有等价的 lint/build 无头校验（我们其实已有 `lint` + 断言式冒烟测试，方向一致）。
**可复用性**：**参考** —— 记入"引擎厂 AI 立场"对比表（目前三档：Epic 积极 / Unity 中立可选 / Godot 明确拒收 AI 贡献）。



## 七、海外社区一手材料（HN / r/LocalLLaMA / DEV / note.com / Zenn）

### 25. 约 950 个 Claude agent 花 21 小时、2.1 亿 token，找出一个新的酶系统 ART（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-24
**是什么**：通过在庞大 DNA 数据库里**把"已知酶附近的重复序列与附属蛋白"连起来**，agent 找到了一个**此前未被表征的酶系统 ART**（带类 CRISPR 重复序列）。**约 950 个 Claude agent 花了 21 小时、2.1 亿 token，扫描超过 20 万个逆转录酶**。日报把它和 09-19 的"生物分子模型加速"、09-21 的"RSA-896 分解"并列：**这是 Claude 用大规模并行 agent 跑把"科学探索阶段"本身自动化的又一例**。
**对我们的影响**：**"大规模并行 agent + 结构化检索"能做成真事**，但也给了一个**成本刻度**：**950 个 agent × 21 小时 = 2.1 亿 token**。对我们个人维护索引站的直接含义：**这种规模不是我们该抄的部分**，该抄的是**"把已知的东西当作锚，在它周围找未知"这个检索策略**（我们的去重也是"拿已知关键词当锚，在语料里找还没收的"）。
**可复用性**：**参考（策略）** —— 引用"锚点 + 邻域检索"的检索范式，**不抄规模**。

### 26. GPT-6 Astra 在真实丰田卡罗拉上开完一整条赛道：第一次 49%，第二次 5 分 22 秒跑完（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-24
**是什么**：**DrivingBench** 把**真实丰田卡罗拉的摄像头画面与车辆状态**喂给一个通用模型，让它**通过工具调用控制转向与加速**。**GPT-6 Astra 第一次跑完 49% 的赛道，第二次在 5 分 22 秒内跑完全程**。日报称这是"通用模型把工具调用从写代码延伸到实时物理控制"的一个醒目演示。
**对我们的影响**：**"工具调用 = 通用接口"在向物理世界外推**，但**更该注意的是它第一次只跑 49%** —— **一次成功演示不等于可靠**，与我们"厂商基准要打折""评审要看循环能不能跑完"是同一条纪律。对我们没有直接落地价值，**登记为"工具调用能力边界"的信号**。
**可复用性**：**不采用（登记）** —— 与我们 Ren'Py / 索引站无关，仅作能力边界参照。

### 27. Amazon 用"服务条款"封掉 Meta 的 Muse agent 在自己站点购物（GeekNews / Claude 日志）
https://claude-news.today/en/briefings/briefing-2026-09-24 · 2026-09-24
**是什么**：**Amazon 屏蔽了 Meta 的 Muse 在 Amazon.com 上购物**，并通知用户：**未经授权的 AI agent 继续访问违反其账号服务条款**。背景：此前**禁止 Perplexity 的 Comet 进站的法院命令被上诉推翻**，所以 Amazon**不再主张"agent 是非法入侵"，改用"违反服务条款"来正当地拦**。
**对我们的影响**：**"agent 能不能替你操作别人的站点"没有技术定论，只有条款定论** —— 这是"agent 时代"正在形成的新边界，企业用**ToS 而不是技术**来划界。对我们**调试自动化抓取/访问**时有直接提醒：**先看目标站的服务条款，别默认"技术上做得到就合法"**（我们是手工调研，风险低，但这条原则值得记）。
**可复用性**：**参考（边界）** —— 记入"agent 行为的合法性边界"资料。

### 28. HN 350 分《How to Write with an LLM》：热评比正文更狠 —— "LLM 写出的段落对读者不算'写作'，算'输出'"（HN / Daring Fireball 一脉）
https://daily.steinslab.io/en/posts/vol-98-2026-09-19 · 2026-09-19（HN 350 分 / 238 评论）
**是什么**：当日 HN 上《How to Write with an LLM》拿到 **350 分 / 238 评论**；**评论区比正文更直白**：有评论专门挑出文中一句 **"LLM 写出的段落对多数读者不会登记为'写作'，而是登记为'输出'"**，并给出反建议 —— **"如果你是写给人类看的，就不要用 LLM。"** 同一批条目里还有"GitHub wiki 是反模式"（**文档应放进和代码同版本的 `/docs`，而不是 wiki**，理由：**版本可追溯、克隆仓库即带上文档**）。
**对我们的影响**：①**"写给人类看的东西别交给 LLM"** 与我们索引站的原则直接相关：**条目的'判断'部分（对我们的影响、可复用性）必须是人写的**，AI 只该负责"找来源、抄数字"；②**"文档与代码同仓、可版本追溯"** 正是我们 `_r22/` 与 index 的做法（**不要去建一个 wiki**）—— 这条给了我们做法的外部背书。
**可复用性**：**落地（纪律）** —— 索引站条目：**事实（URL/日期/数字）可由 AI 抽取，判断/取舍必须人写**。

### 29. 华为云在 HC 2026 首秀 "CMS 记忆存储"：面向 agent 的 PB 级记忆，宣称 95% 缓存命中（华为云，全联接大会 2026）
https://dy.163.com/article/L745JHSO0514R9OJ.html · 2026-09-18（华为全联接大会 2026）
**是什么**：华为云**首次实物展出 CMS 记忆存储方案**，给智能体"增强记忆"：**盘级存储架构 + 灵衢互联总线（UB）让 NPU 直通 AI 语义存储模组（ASU）**，宣称构建 **PB 级记忆空间**（**优于同类 1 倍**）、**TB 级读取**（**优于业界 50%**），并用**分布式内存池化 + 分层联动**做到 **95% 记忆缓存命中**。这是华为云 **"高效 Token + 增强记忆 + 通智一体化调度 + 安全自治" Agentic Infra 新范式**的落地件。
**对我们的影响**：**"记忆被当成基础设施（PB 级、带缓存命中率）"是这辑 Memory 主题最硬件的版本** —— 和我们看的前四条（API 层）是同一个问题的另一层。但我们**用不上 PB 级**，真正可抄的只有一个**指标定义**：**记忆系统的关键 KPI 是"命中率"和"读取延迟"**，而不是"存了多少"。**⚠️ 一手源说明**：本条只取到**网易对环球网稿的转载**，未找到华为云官网原文（见 §十），数字均为**厂商自述**。
**可复用性**：**参考（指标）** —— 只借"命中率"这个 KPI 定义；**方案本身不采用**（云、PB 级，与我们单机场景无关）。

## 八、榜单与指标（AA / LMArena / OpenRouter / SWE-bench / Epoch AI）

### 30. ⚠️ Artificial Analysis Intelligence Index v4.3.2 换锚：**把 Elo 基准钉在 DeepSeek V4.1 Flash = 1600**，145 个分数变动、128 个下降（AA 官方 changelog，第三方复盘）
https://muhammad-ahmed.com/blog/ai-brief-an-alpha-channel-and-a-licence · 2026-09-19（v4.3.2）
**是什么**：AA 在 **09-19** 发布 **Intelligence Index v4.3.2**，**只有一条 changelog、没有配套文章**，做了两件事：①**把 GDPval-AA 评估的 Elo 刻度锚定在"DeepSeek V4.1 Flash = 1600"** —— 此前（6 月）锚点是**人类专家表现 = 1000**，**现在人类参照点已从方法论章节消失**；②用 **Crowd-BT**（带逐标注者可靠性项的 Bradley-Terry 变体）**重拟合 GDPval-AA 与 AA-Briefcase**。**量化影响**（第三方对比两天的存档榜单得出，非 AA 公布）：**两天都带 GDPval-AA 评分的 233 个模型里，平均 Elo 掉 60.7、中位数掉 59.1（177 降 / 4 升 / 52 个本来就被钳在地板）**；**指数层面 145 个分数变化、128 个下降**；**只看 129 个"实测"模型平均变化 −0.36、其中 126 个下降**；**56 个模型的显示（取整）分数变了，含 GPT-6 Astra（extra-high effort）从 53 变 52**。**公式公开可算**：贡献值 = `clamp((E−500)/2000)`、占 **10% 权重**，所以 **1 个指数点 = 200 Elo**；锚点自身只降了 32（说明不是整体平移，而是**下半区被压缩**，被钉在地板的模型从 52 增到 74）；**15 个模型从"实测"降级为"估计"，反向为零**。**榜首差距**：09-07 记的 **Claude Fable 5.1 领先 GPT-6 Astra 0.56 点**（当时都显示 53），09-19 该值仍精确为 **0.5597**，**现在是 0.6813** —— **差距扩大 0.12 点，且没有任何新评测结果参与**。
**对我们的影响**：**这是"跑分必须带指数版本号"这条规矩的极端案例，也是最强的一次证明**：**换一次拟合方法，就能让榜首差距凭空变化 0.12 点**（AA-Briefcase 占 15% 权重、逐模型值不公开，所以连归因都做不到）。对我们直接可用的推论：①**引用任何 AA 分数必须同时写"v4.3.2 + 数据日期"**，否则跨版本不可比；②**"厂商/榜单的进步有时来自方法而非能力"** —— 我们读"某模型又涨了 X 分"时，**先问一句"这周换没换指数版本"**；③**把"锚点从一个模型改成另一个模型"这件事本身存疑**（人类基准消失了）—— 这正是 M-0019"同一个数、不同口径"的最高级形态。
**可复用性**：**落地（引用规范）** —— 强制写"AA Intelligence Index **v4.3.2**，数据版本 **2026-09-19**"，并注明"不可与 v4.3.1 及更早横向比"。



---

## 九、本路去重报告

**比对基线**：`index.html`（1128 项）+ `csdn-social-summary.md` + `csdn-social-summary-v15.md` ~ `v21.md`（逐份 grep）+ `_r21/_r21_official.md` 的已收表。命中即弃。

**因精确命中而剔除（含原因）**
1. **Claude Opus 5.5**（09-22，$4/$20、Index v4.3.2 最高分）：`Opus 5.5` 在 v16/v18/v19 命中，`_r21 §八` 已明确剔除 → 不收（只在第 12 条 v2.1.280 里作为"默认模型切换"的背景被提及）。
2. **GPT-6 Sol / Luna**（09-22 降价 50%）：`GPT-6 Luna` 在 v16 命中、`_r21` 已剔 → 不收。
3. **GPT-6 Astra**（09-03）：v10~v20 大量命中 → 不收（仅在 AA v4.3.2 里作为"显示分 53→52"的例子出现）。
4. **Grok 4.7**（09-21，新基座 / $2.73 每任务）：`Grok 4.7` 在 `_r21 §八` 已作为"每任务成本"条目收过 → 不收。
5. **Claude Projects 重构（多线程 coordinator）**（09-17）：`_r21 §八` 第 8 条明列"Projects 重构 已在 _r20 收" → 不收。
6. **Claude Cowork 与 Chat 合并 / Claude Docs + Slides**（09-16）：`Claude Docs` 在 v13(#24)/v17 命中，**已由 cn 路收录** → 不收。
7. **Claude Managed Agents Memory Stores**：`_r21 §一` 第 4 条已收 → 不收（本路只在第 8 条的"五云对照"里作为**证据数字**引用其参数上限）。
8. **Claude Code 2.1.266~2.1.270 / 2.1.277（AGENTS.md）**：`2.1.277` 在 v17 命中且已收；`_r21 §一` 第 2 条已收 2.1.266~270 → 不收。**本路只收 2.1.281（及 v2.1.280 默认模型切换、2.1.278 服务端分类器）**，均为新版本。
9. **DSH v0.1.5 / MiMoCode**：DSH 历代版本归 **gh 路**（仓库/release 本体）；**cn 路收"源码解析帖"**。本路的 DSH 条目是 **v0.1.6-alpha.1 的 release-note 行为变化（机制视角）**，与 gh 的"仓库本体"、cn 的"源码帖"**实体不同**（见交叉区）。
10. **Qwen3.8-Omni-Flash / GLM-5.3-FlashX / Kimi K3 Bedrock**：`Omni-Flash` 在 v7(#26)/v11 命中，`Kimi K3` 在 v7/v17 命中 → 全不收。
11. **小米 MiMo-V2.6（Pro/Flash/Pro-UltraSpeed）**：`MiMo-V2.6` 在 v18/v19 命中（v20 明列剔除）→ **不收**（本节原拟收其 MIT/RL 直播/$3.5M 新细节，按"同一件事不换媒体重报"规则放弃）。
12. **中国电信 Xing4.0-29B-A4B**：v10(#15) 已收 → 不收。
13. **Meta Muse Glimmer**：作为 AA"最低单任务成本 $0.06"在 v20/`_r21 §四` 出现过；本次拿到的"30B / Apache-2.0 / 4-bit <20GB / DFlash 3.1×"属**另一层细节**，但模型发布于 **2026-08-10**、且家族已被提过 → **存疑不收**（列入 §十）。
14. **Bend 2 与"先例检查四问"（DEV.to / HN 603+323 分）**：`先例` 在 v20 §十 命中（**"学名 / 行内人在用什么 / 为什么现成的不合用 / 能建在上面的最小版本"**四问，58 行 / 442 行 AI 证明 / SPARK 全都在 v20 收过）→ **不收**（本辑 DEV.to 那篇是同一事件的重述）。
15. **Zed 作为"平台名"**：`Zed` 在 v19 只作为 17 个受支持平台之一被列名 → **允许收其九月具体 changelog**（第 15 条属新增量，非重复）。
16. **Amazon 封 Meta Muse / GPT-6 Astra 开真车 / 950 agents 找酶**：均为 **GeekNews 当日简报**（09-24），四份基线 **0 命中** → 收。

**因重复形态而合并/降级的**
- **Qwen-Image-2.1**：本**体**已在 v19 收（Arena 图像榜开源第一）；**本条只保留"许可证从 Apache-2.0 收成仅非商业"这个新事实**，并显式标注"模型本体已收"。
- **Claude API 的"中途改请求不脏缓存"**：拆成第 4 条（tool_addition/removal + defer_loading）与第 5 条（中途系统消息 + clear_at + 中途改 effort），因**两条对应不同的 beta header 与不同的使用场景**，不合并。
- **AA v4.3.2** 的报道在 felloai / theairankings / muhammad-ahmed 三处出现，数字以 **muhammad-ahmed 的逐项复盘**为准（唯一给出 145/128/60.7 等具体计数与公式的），并**明确标注"第三方复盘、非 AA 公布"**。

**主动不收（主题不符 / 无稳定信息量）**：Zhenwu V900 等芯片条目；纯融资条目；Windsurf 收购史与 Zed vs Windsurf 的选型软文（无官方一手 changelog）；Slack Code / Sponsored Agents（与我们的索引站/Ren'Py 无落地关系）。

---

## 十、未取到一手源清单

| 条目 | 缺失的一手源 | 现有可互证来源 |
|---|---|---|
| 第 3b 条 Needle 3 | 未取到 **Cactus 官方 blog / GitHub README 原文**（只读到 4 篇二手评测，其中含**独立测试 32.2%** 这个反证） | byteiota / mindstudio / agihunt / aimadetools 四篇互证，数字一致 |
| 第 29 条 华为云 CMS | **未找到华为云官网原文**，只有网易对环球网稿的转载 | 网易转载（单源）· 已在条目内标注 ⚠️ |
| 第 30 条 AA v4.3.2 | **AA 官方只有一条 changelog、无配套文章**；145/128/60.7 等计数是**第三方对比存档榜单得出** | muhammad-ahmed 复盘 + felloai + theairankings 三处 |
| 第 24 条 Unity 7 | **未取到 Unity 官方 blog 原文**（Unite Seoul 的中文转述 + 第三方汇总） | vongola / japanese-specialist 两处互证 |
| 第 8 条 五云记忆 API | 未逐条打开 **Anthropic / Google 官方 docs 原页**（beta header、触发阈值等数字来自综述转引） | quidproquo（英/中两版）+ skills.pub 的官方 docs 摘录 |
| 第 7 条 Codex Agents API | 未取到 **OpenAI 官方 blog 原文**（09-10 公测） | analyticsinsight 综述 |
| 第 11 条 Memory Trust Gap | 未打开 **两篇 arXiv 预印本原文**（论文号未知） | aiagentstore 周报（单源） |
| DSH 英文侧（cn 路提示） | `beri.net/learning/deepseek-harness-docs`、`developersdigest.tech/.../deepseek-harness-dsh-first-look` 两篇**读到了但未收**（前者含 `~218k stars / CVE-2026-82533 CVSS 9.4` 等数字） | 归本路但未取到细则，**登记为下一辑待办** |

---

## 十一、搜索覆盖表

| # | 主题 / 关键词 | 搜索工具 | 结果 | 是否产出条目 |
|---|---|---|---|---|
| 1 | Anthropic Claude Code changelog | WebSearch + WebFetch | 有 | ✅ 12/13 |
| 2 | OpenAI Codex changelog | WebSearch | 有 | ✅ 14/7 |
| 3 | DeepSeek Harness (DSH) release notes | WebSearch + WebFetch | 有 | ✅ 6 |
| 4 | VS Code release notes 1.14x | WebSearch | 有 | ✅ 16 |
| 5 | Anthropic memory tool / context editing | WebSearch | 有（4 篇） | ✅ 4/5/8/9 |
| 6 | Google Gemini / DeepMind release | WebSearch | 有（3.8 Live，**已在 `_r21` 收**） | ❌ 全剔 |
| 7 | agent memory news | WebSearch | 有 | ✅ 10/11/29 |
| 8 | Qwen3.8-Omni-Flash | WebSearch | 有（**v7 已收**） | ❌ 剔 |
| 9 | Steam / Ren'Py AI disclosure | WebSearch | 有 | ✅ 22/23 |
| 10 | Unreal / Unity AI policy | WebSearch | 有 | ✅ 24 |
| 11 | Windsurf / Zed editor | WebSearch | 有（Zed 一手较好，Windsurf 只有软文） | ✅ 15（Windsurf 不收） |
| 12 | Hacker News vibe coding | WebSearch | 有 | ✅ 18/21/28 |
| 13 | 新模型（open weights, d3） | WebSearch | 有（多与 v18/v19 重复） | ✅ 3b/3c（MiMo/Xing/Omni 全剔） |
| 14 | Cactus Needle 3 | WebSearch | 有（4 篇） | ✅ 3b |
| 15 | Artificial Analysis index update | WebSearch + WebFetch | 有 | ✅ 30 |
| 16 | r/LocalLLaMA 本地模型 | WebSearch | 有 | ✅ 3b（Cactus）· 另见 §八剔 |
| 17 | Codex / Claude Code 2.1.281（WebFetch 原文） | WebFetch | 有 | ✅ 12/13 |
| 18 | DSH v0.1.6（WebFetch 原文） | WebFetch | 有 | ✅ 6 |
| 19 | 游戏引擎 / UE6 | WebSearch | 仅二手 | ✅ 24（UE6 归 `_r21` 已议） |
| 20 | Epoch AI / OpenRouter / LMArena | 未单独检索 | — | ❌ **本轮未查**（`_r21 §四`刚收过 OpenRouter 周用量，本轮无新窗口数据） |

**未覆盖/欠覆盖的自查**：①**X / xAI 官网**未直接抓（Grok 4.7 已在 `_r21` 收，无新增）；②**Meta / Mistral 官方**本轮无新东西（Muse Spark 1.3 与 Muse Glimmer 已收，见 §九第 13 条）；③**Epoch AI / SWE-bench 官方**本轮未单独查（无新版本发布迹象）；④**字节豆包 / MiniMax / Kimi 官网**本轮未单独查（无新发布迹象，且 cn 路已覆盖国产模型侧）。

---

## 十二、对我们的意义汇总（16GB Win / Ollama / Ren'Py / 静态索引站 / Python 脚本）

**本路 32 条，收敛成四句可直接用的话：**

1. **"记忆"这件事，官方给出的是一条分层纪律：清之前先落盘、存储/隔离/TTL 全归你自己、撤销必须真的执行。** Anthropic 的 context editing 在清之前会系统级提示"**先存进记忆**"（第 8 条），memory tool 明说"**存储、租户隔离、TTL 全是应用责任**"且要防路径穿越，Claude Code 压缩后**只有项目根 CLAUDE.md 与不带 paths 的规则会重读，>5,000 token 的文件只剩路径**（第 9 条），而两篇 preprint 指出**被撤销的记忆默认仍会被检索出来并触发动作**（第 11 条）。→ 落在我们身上：`mistakes/` 与索引**加"最后复核日期 + 是否作废"两个字段，作废要显式标废而不是删行**；长会话压缩前**先存原文**。

2. **"上下文是会花钱的资产"，所以官方都在做"声明一次、按需揭示"，而不是"一次给全"。** Claude API 用 `tool_addition/removal` + `defer_loading` 做到**换工具不脏缓存**（第 4 条），用 `clear_at` 让一条指令**只活一轮**（第 5 条）；Claude Code 侧 skill 重注入**有 5,000/25,000 token 上限**（第 9 条）；DSH 把**模型生成的代码移出主进程到隔离子进程**（第 6 条）。→ 落在我们身上：**别把"想让它记住的"塞进系统提示**（写进 md），**"只在某一轮生效的约束"单独放**；自建编排时按"工具声明与可见性分离"设计。

3. **"便宜"与"更强"都要带版本号和口径读 —— 这一辑 AA 换锚是最强的证据。** AA **把 Elo 锚点从"人类专家 1000"换成"DeepSeek V4.1 Flash = 1600"**，一次**145 个分数变动、128 个下降**，**榜首差距在没有新评测的情况下扩大 0.12 点**（第 30 条）；Needle 3 厂商说打平 DeepSeek V4 Flash，**独立测试只有 32.2%**（第 3b 条）；"tokens too cheap to meter"说**成本已不该是选型主轴**（第 19 条）。→ 落在我们身上：**引用分数必须写"v4.3.2 + 日期"**；**厂商数字必须找独立复现**；**选型按质量线选档，不按省 token 选档**。

4. **"AI 参与创作"的边界正在从"技术问题"变成"条款与法规问题"，我们站在需要留痕的一侧。** Steam 数据说**每 3 款新游 1 款标了 AI、9 月上半月 48.5%**（第 22 条），但"标签 ≠ 质量"；**EU AI Act 第 50 条已在 2026-08-02 生效、中国 2025-09-01 起双标注**，"店里不标 ≠ 法律不管"（第 23 条）；Unity 官方立场是"**选择权在开发团队**"（第 24 条），而 Anthropic 给了 `attribution:false` 这个"去掉署名"的开关（第 12 条）；HN 热评则说"**写给人类看的东西别交给 LLM**"（第 28 条）。→ 落在我们身上：**Ren'Py 项目建"素材来源表"（代码助手不填，生成素材要填且保留元数据）**；**索引站条目的"判断"部分必须人写**。

**给本机环境（16GB Windows / Ollama）的三条具体动作：**
- **本地模型的下一步观察项：Cactus Needle 3 式的"专用小组件"**（8~29MB 只做工具调用/抽取，第 3b 条）—— 比"再找一个更小的聊天模型"更合 16GB 本机；**但独立测试未复现前不落地**。
- **长会话/长任务的两个官方补丁值得照抄**：危险 `rm` 确认框**等 2 分钟**、自托管 runner 的**大系统提示改走私有文件**（第 12 条）—— 都是"别让大提示把流程卡死"。
- **一律给引用加两个钉子**：**版本号 + 数据日期**（AA 第 30 条、Needle 3 第 3b 条、DSH 第 6 条的版本号）。这是本辑成本最低、收益最高的一条纪律。

---

## 十三、统计

- **条目数：32 条**（编号 1~30，其中 3b/3c 为第 3 条之后的追加，共 32 个条目），全部带**发布日期 + 完整 URL + 至少一个具体数字**。
- **分节**：模型测评与上新 **6**（1、2、3、3b、3c + 本体说明）· 上下文与 agent **4**（4~7）· Memory 管理 **4**（8~11）· IDE / Copilot 类 **6**（12~17）· vibe coding **4**（18~21）· 游戏 / AI 政策 **3**（22~24）· 海外社区 **5**（25~29）· 榜单与指标 **1**（30）。
- **带指数版本号标注的榜单引用：1 处**（第 30 条，明确写"**AA Intelligence Index v4.3.2，数据版本 2026-09-19**"，并声明**不可与 v4.3.1 及更早横向比**）。
- **区分"厂商基准 / 独立复现"的条目：2 处**（第 3b 条 Needle 3 的 86.0 vs 32.2；第 30 条 AA 换锚的"厂商未公布、第三方复盘"）。
- **明确标注 beta / preview / GA 的条目：4 处**（第 4 条 beta `mid-conversation-tool-changes-2026-07-01`；第 5 条 beta `...clear-at-2026-08-21`；第 8 条 `context-management-2025-06-27` 与 `agent-memory-2026-07-22`；第 3 条 Life Sciences beta）。
- **时效**：绝大多数为 **2026-09-15 ~ 2026-09-24**；三条更早（第 24 条 Unity 7 = 2026-07-21、第 3b 条 Needle 3 = 09-17、第 29 条华为 = 09-18），均已标注原日期。
- **文件落盘**：`D:\34498\Documents\github-projects-invest-games\_r22\_r22_official.md`，UTF-8，**分 7 批增量写入**（骨架 → §一 → §二 → §三 → §四 → §五/§六 → §七/§八 → §九~§十三）。


