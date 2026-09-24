# 第二十五辑 · 官方与海外路（r25-off）

- 调研日期：2026-09-24
- 主题窗口：2026-09-15 ~ 2026-09-24
- 检索范围：厂商官网 / 官方博客 / release notes / 官方文档 / Hacker News / r/LocalLLaMA / 榜单（Artificial Analysis、LMArena、SWE-bench official）
- 去重基线：index.html（1153 项）+ csdn-social-summary.md(=v23) + csdn-social-summary-v22.md + csdn-social-summary-v21.md
- 纪律：每条带榜单版本号 + 数据日期；跨版本不可比；边查边写盘

---

## 正文（逐条追加）

### 1. OpenAI 给生命科学专模 GPT-Rosalind 加能力，并同步发布 4 个领域基准
- 链接：https://ar@openai.com/index/introducing-new-capabilities-to-gpt-rosalind/ （OpenAI 官方公告页，权威域名 openai.com/index/…）
- 来源/日期：OpenAI 官方 / 2026-09-11（公告内 "Update on September 11, 2026"）
- 核心内容：GPT-Rosalind 结束 research preview，向合规机构全球开放（trusted-access），并公布付费定价 **2026-10-05 生效**。它把 GPT-5.5 的 agentic coding / tool-use 与药物化学、基因组学等强领域智能结合。四个新基准：**LifeSciBench**（外部专家判分，6 类工作流）、**MedChemBench**（27.5% vs GPT-5.5 的 25.1%，token 少 7.2%）、**GeneBench**（21.6% vs 20.4%，token 少 31%）、**LabWorkBench**（63.2% vs 55.8%，token 少 5.3%）。
- 可复用性：⚠️参考 —— 与本地 16GB 站主无直接关系；但「**用 token 更少同时准确率更高**」这个口径可抄进本站的模型对比列（能力↑ / token↓ 必须同屏）。四个基准名不要单独引用，需带「OpenAI 自建 + 自报数」。
- 去重证据：`grep -iF "GPT-Rosalind"` → 0；`grep -iF "Rosalind"` → 0；`grep -iF "LifeSciBench"` → 0；`grep -iF "MedChemBench"` → 0（四份基线全 0）。

### 2. Anthropic 9 月产品 release notes 两则：Salesforce in Claude（09-15）+ smart reports（09-10）
- 链接：https://docs.anthropic.com/en/release-notes/claude-apps （Claude Help Center 官方 release notes）
- 来源/日期：Anthropic 官方 / 2026-09-15（Salesforce）· 2026-09-10（smart reports）
- 核心内容：① **Salesforce in Claude（beta）** 把 seller 的 accounts / opportunities / pipeline 拉进 Claude，自带 **37 个 pre-built sales skills**（备电话、审单、建 pipeline 看板、发 forecast），面向所有付费计划、需 Salesforce 侧批准 beta 报名。② **smart reports（beta）** 分析团队怎么用 Claude：报告在工作上真正产出了什么、花了多少钱、**会话在哪儿卡住（friction）**、哪些重复模式值得封装成 shared skills，仅 Claude Enterprise。
- 可复用性：✅落地（概念）—— 「smart reports」的 4 个观测维度可直接抄成个人站主的月度自检清单：产出 / 成本 / **卡点** / **可封装成 skill 的重复模式**。第 4 条正是本索引站的运维痛点。
- 去重证据：`grep -iF "Salesforce in Claude"` → 0；`grep -iF "smart reports"` → 0；`grep -iF "smart report"` → 0。注：基线里 4 处 "Salesforce" 全指 Salesforce **研究团队**的 agent 论文（v23:556），与本条的 Salesforce **产品插件**无关，非重复。

### 3. xAI Grok 4.7：参数 2.1 万亿，较 4.6 增约 40%（09-12）
- 链接：https://www.cnr.cn/jingji/jjgd/20260916/t20260916_527814860.shtml （央广网转述 xAI 官方发布；xAI 官网原始公告本轮未取到直链）
- 来源/日期：xAI 官方（经央广网 2026-09-16 报道转述）/ 2026-09-12
- 核心内容：Grok 4.7 **参数规模 2.1 万亿**（Grok 4.6 为 1.5 万亿，**增约 40%**），马斯克称该模型「在性能与效率层面将全面超越市面所有同类产品」。同篇报道列出 9 月发布节奏：09-01 Claude Fable 5.1 / 09-03 GPT-6 Astra（超 10 万块 GPU 训练）/ 09-10 DeepSeek V4.1-Flash / 09-12 Grok 4.7。
- 可复用性：⚠️参考 —— 参数规模对 16GB 本地机毫无落地价值（2.1T 绝无本地可能），但「**9 月密集发布日历**」这条时间线可用来核对本站的模型卡片是否漏档。**注意：参数数 ≠ 可用性，标注为「闭源 API-only」。**
- 去重证据：`grep -iF "Grok 4.7"` → 0；`grep -iF "Grok4.7"` → 0；`grep -iF "2.1万亿"` → 0。（基线收了 Grok 4.6 的降价与「半程完成长任务」，4.7 未收。）

### 4. VS Code 1.137：Automations（定时 agent 任务）进 Preview、Voice Mode 实验性上线
- 链接：https://aka.ms/VSCode/137 （重定向至 code.visualstudio.com/updates/v1_137 官方 release notes）
- 来源/日期：Microsoft VS Code 官方 release notes / 2026-09（1.137 稳定版）
- 核心内容：① **Automations（Preview）**：把重复的 agent 任务排成**每小时 / 每天 / 每周**或按需触发，开 `chat.automations.enabled`，Agents 窗口侧栏进 Automations，内置「追变更 / 分诊 issue / 找 bug」模板。② **Voice Mode（Experimental）**：和 agent 语音对话，且**能在它干活时打断、改方向**。③ Agents 窗口内直接看 GitHub issue / PR 详情（无需打开仓库，实验性）。④ quick chat 可中途「挂」一个 workspace 继续（保留标题、历史、当前请求）。
- 可复用性：⚠️参考 —— 16GB 本地机 + Ollama 一般不用 Copilot 云端 agent，但 **Voice Mode 的「可打断」**与 **Automations 的「定时」**两个交互范式值得抄进本站的自动化脚本设计（本索引站自身就跑周期性调研，正是 Automations 的场景）。
- 去重证据：`grep -iF "v1.137"` → 0；`grep -iF "1.137"` → 0。**边界说明**：`grep -iF "Automations"` 命中 v23:418 **1 处**，但那处讲的是「带自己 key 也盖不住的 Copilot 能力清单」，不是 1.137 的 Automations 功能本体；`grep -iF "Voice Mode"` 命中 v22:244 **1 处**，讲的是 **1.140** 的 Voice Mode 会话感知。故 1.137 作为**发布版本本体**未被收录，此处收的是版本级新特性，非重复。

### 5. Anthropic Messages API 服务端压缩：`compact_20260112` 策略 + `compact-2026-09-04` 按需摘要 beta
- 链接：https://platform.claude.com/docs/en/build-with-claude/context-windows （Claude Platform 官方文档，compaction / context management 章节）
- 来源/日期：Anthropic 官方文档 / 阈值策略 `compact_20260112` 于 2026-01 上线，**`compact-2026-09-04` 按需摘要 beta 为 2026-09-04**
- 核心内容：开发者可在 Messages API 开**服务端压缩**，把长对话按自设阈值自动摘要；策略名 `compact_20260112` 加进 `context_management.edits`，**默认触发阈值 150,000 input token，最小可设 50,000**。API 返回一个 compaction block 带摘要，之后请求**忽略该 block 之前的全部内容**；自定义指令会**整体替换**默认摘要提示词。压缩会**额外计一次采样**（计入限流与账单），**用同一个模型**做摘要。**`compact-2026-09-04` beta** 允许**按需**请求摘要而非等阈值。
- 可复用性：✅落地 —— 「压缩 = 额外一次采样、同模型、计入账单」这条对预算敏感；本站长会话巡检可据此设 **50K~150K** 的显式阈值而不是等模型撑满。概念可平移到本地 Ollama 的 `/compact` 逻辑。
- 去重证据：`grep -iF "compact_20260112"` → 0；`grep -iF "context_management"` → 命中 v22 **1 处**，但那是 Claude Code 的 `mid-conversation-system-clear-at-2026-08-21` 中途系统消息机制，**不是 Messages API 的 compaction 策略**；`grep -iF "auto-compact"` → 0。**未重复。**

### 6. 五朵云，五套 memory API：OpenAI / Anthropic / Google / AWS / Microsoft 设计哲学对比（09-19）
- 链接：http://quidproquo.cc/posts/ai/2026-09-19-cloud-platform-memory-apis-en
- 来源/日期：第三方深度对比（quidproquo.cc）/ 2026-09-19（原文逐条引官方文档，标 "per the official docs"）
- 核心内容：五家 2025–2026 陆续出的 agent memory API 路线完全不同：**OpenAI 把记忆当文件**（Responses API `previous_response_id` 链式，客户端压缩 `POST /responses/compact` 2025-12-11、服务端 `compact_threshold` 2026-02-10、GPT-5.4 2026-03-05 原生压缩 + 1M 窗口；sandbox memory 布局固定为 `memories/memory_summary.md` + `MEMORY.md` + `rollout_summaries/` + `raw_memories/` + `skills/`，写入分 extraction → consolidation 两段）；**Anthropic 挂载成一个目录**（`/memories`）；**Google 用向量 + 主题分类**；**AWS 事件 + 可插拔策略管线**；**Microsoft 抽象成 context provider**。价格 **免费 ~ $0.75/1K 记录/月**，租户隔离从「你自己处理」到「IAM 一等公民」。
- 可复用性：✅落地 —— 这五路可以直接做成**选型对照表**放进本站「memory 管理」主题页。对个人站主，「**记忆即文件（`memory_summary.md`）**」是最省事的落地形态：一个 markdown 文件 + 明确索引，比向量库更好维护。
- 去重证据：`grep -iF "memory_summary.md"` → 0；`grep -iF "Dreaming"` → 命中 v22:230 **1 处**（只覆盖 ChatGPT Dreaming 召回率 41.5%→82.8%，**未覆盖本文的 5 云对照与 pricing**）；`grep -iF "memory store"` → 1（形态不同）。**本文主体未重复。**

### 7. arXiv 2606.23130：9,041 个 vibe-coded 应用实测，91.0% 至少一个漏洞
- 链接：https://www.alphaxiv.org/zh/abs/2606.23130
- 来源/日期：arXiv 预印本 2606.23130（Deng / Fan / Meng 等）/ 2026-06 提交（本轮为榜单站转述）
- 核心内容：收集 **9,041 个**用 Claude Code 与 Lovable 生成的**开源**应用，并审计 **200 个公开部署**的应用，共发现 **1,186 个漏洞**。结论三条：① **91.0% 的被审应用至少含一个漏洞**，**65.77% 的漏洞被评 Critical 或 High**，集中在 broken access control / injection / authentication failure；② 漏洞可归因到 **8 种反复出现的失败模式**，根植于 AI agent 三类系统性缺陷：**memory defects / objective defects / knowledge defects**；③ **改 harness、改提示词能降低但不能消除**风险。
- 可复用性：✅落地 —— 「**harness 改了也消不掉**」这一条对本站是硬结论：本地生成的代码一律走「**八类失败模式核对清单**」再合入。「memory defects」这个提法特别值得记——**记忆缺陷会直接变成安全洞**。
- 去重证据：`grep -iF "2606.23130"` → 0；`grep -iF "9,041"` → 0；`grep -iF "1,186"` → 0；`grep -iF "vibe-coded"` 在四份基线的 grep -in 复查为 0 行。**未重复。**

### 8. arXiv 2609.09560：30 人对照实验，vibe coding 快 27% 但可维护性↓、漏洞↑
- 链接：https://www.sofarbot.com/news/6GQPvynY5sHA （转述 arXiv 2609.09560 摘要；原文 https://arxiv.org/abs/2609.09560）
- 来源/日期：arXiv 预印本 2609.09560（Aribe Jr. / Labastida）/ **提交 2026-09-09**
- 核心内容：30 人混合方法实验（含专业开发者与高年级 CS 学生），每人用**三种条件**完成等价任务：传统编程 / AI 辅助 / vibe coding。**vibe coding 比传统快 27%、比 AI 辅助快 12%**；但**可维护性指数更低、安全漏洞更多**。SUS 可用性 **71.4（good）**，NASA-TLX 认知负荷 **55.5（中等）**。主题分析四个概念：**trust calibration / loss of control / cognitive adaptation / prompt-engineering**；**「感知到失控」直接关联更高安全风险**。
- 可复用性：⚠️参考（有保留）—— 样本仅 30 人、为预印本、任务类型与语言未充分披露，**不可当定论**。可落地的是那句「**感知失控 → 更多漏洞**」：把「可复核的 diff / 可回溯的日志」当成降风险手段，而不是靠更信任模型。
- 去重证据：`grep -iF "2609.09560"` → 0；`grep -iF "71.4"` → 0；`grep -iF "SUS"` 未单独命中该研究。**未重复。**

### 9. Artificial Analysis Intelligence Index v4.2：40% 权重改为私有 held-out 集（09-04）
- 链接：https://note.com/allegro_ai/n/n8fde747b8e26 （第三方复盘 AA v4.2，称引官方 methodology 页）
- 来源/日期：Artificial Analysis 官方方法论改版（第三方复盘）/ **2026-09-04**（AA v4.2）
- 核心内容：v4.2 把 **40% 的 Index 权重改为私有 held-out 集**（v4.1 是 20%，**翻倍**，官方说法是 "to prevent gaming"）；私有部分含 **AA-Briefcase / AA-Omniscience / CritPt**。**删除已饱和的 GPQA Diamond**，新增 **AA-Briefcase**（数千输入文件、跨数周的知识工作）与 **GDP.pdf**（Surge AI 出，**100 个 PDF / 4,592 页 / 1,275 条专家评分标准**）。10 项评测权重：Agents 30%（AA-Briefcase 15 / GDPval-AA v2 10 / τ³-Banking 5）、General 30%（AA-Omniscience 15 / GDP.pdf 10 / AA-LCR v1.1 5）、Coding 20%（Terminal-Bench v2.1 10 / SciCode 10）、Scientific Reasoning 20%（HLE 10 / CritPt 10）。同版下**总分第一与分项第一并不同家**（GDP.pdf 第一是 GPT-6 Astra 33.2%，Fable 5.1 仅 26.2%）。
- 可复用性：✅落地（引用规范）—— 强化本站既有规矩：**引用 AA 必须带「完整版本号 + 数据日期」**，且**总分不可替分项**。⚠️ **本条的边界**：基线 v22:381 已收 **v4.3.2（数据日期 2026-09-19）的换锚**；本条收的是**更早的 v4.2（09-04）方法论改版（40% 私有化 + 换题）**，是**版本演进链上的前一环**，两者不同版本、不同事件，非重复。
- 去重证据：`grep -iF "v4.2"` → 0；`grep -iF "AA-Briefcase"` → 0；`grep -iF "GDP.pdf"` → 0；`grep -iF "AA Intelligence"` → 3（均指 v4.3.2，见 `_r22`/v22:381）。

### 10. Ramen Aura 1.0：面向 Unity/Unreal 的游戏开发 agent 正式发布（09-09）
- 链接：https://gamesbeat.com/ramen-launches-aura-1-0-to-push-agentic-ai-in-game-development/ （GamesBeat 对 Ramen CEO Andy Tsen 的专访，含官方发布信息）
- 来源/日期：Ramen 官方发布（经 GamesBeat 2026-09-09 报道）
- 核心内容：Aura 1.0 是跑在 **Unity 与 Unreal** 上的游戏开发 agent，**基于 Anthropic 的 Claude**（合作方点名 Opus 5 / Fable 5.1）。核心亮点：**Verification Agent 快 8 倍**——一条测试用例从 **2–3 分钟**降到**不到 1 分钟**，且从一次 1 条变成**一次并行 3 条**；Blueprint 生成提速；**跨会话 / 跨项目的持久项目记忆**（自动沿用，不用每轮重讲上下文）；Auto 模式**不限量**。付费三档：**Indie $10 / Pro $40 / Ultimate $200（每月）**；Fab 商店 **$150 买断**（终身 MCP 用量 + 一年订阅）。已上线 Mac（Unity/Unreal）、Epic Fab 商店。落地案例：**IRONMACE（Dark and Darker，2000 万+ 玩家）用它在教程功能上省下一半时间**。
- 可复用性：⚠️参考 —— 付费工具，16GB 本地机用不上。但「**Verification Agent 能自己 playtest**」和「**持久项目记忆**」两个设计点是本站「游戏制作 + memory」主题的关键样本；**$10/月 Indie 档 + Fab 买断制**的定价模型可作为对照。
- 去重证据：`grep -iF "Aura 1.0"` → 0；`grep -iF "Ramen"` → 0；`grep -iF "Verification Agent"` → 0；`grep -iF "Ironmace"` → 0；`grep -iF "Aura"` 的 3 处命中全在 index.html 的 CSS/Unity 资产工具上下文，与本条无关。**未重复。**

### 11. Unreal Engine 5.8 出实验性 MCP 插件，UE6 把 MCP 层写进管线（State of Unreal 2026）
- 链接：https://ludusengine.com/blog/unreal-engine-built-in-ai-assistant
- 来源/日期：Epic 官方（经 ludusengine 2026-09 综述，引 UE 5.8 release notes 与 State of Unreal 2026；厂商立场页，**注意利益相关**）
- 核心内容：**截至 2026-09，Unreal 没有内置的完整 AI 助手**（不会替你写 Blueprint/C++）；UE 5.8 给的是**实验性 MCP 插件**——把打开的项目暴露给外部模型（Claude Code、Cursor 等），模型通过**编辑器工具调用**读写项目。作者点出关键限制：**它「一次调用发现一点项目」，不持有全局视图**。State of Unreal 2026 上 Epic 说明 **UE6 的研发管线含 MCP 层**，接 Claude、Gemini 等，定位「生产力倍增器、创意控制权留给开发者、**可选完全不用 LLM**」；**UE6 Early Access 目标 late 2027**。
- 可复用性：⚠️参考（有保留）—— 「**给连接、不给助手**」是引擎厂 AI 战略的关键区分；对本站游戏主题，「**MCP 是引擎与模型之间的标准接口**」这句可直接引用。⚠️ 源为第三方厂商页（卖自家 Ludus AI），Epic 原始 release notes 本轮未直取，**结论需以 Epic 官方为准**。
- 去重证据：`grep -iF "UE 5.8"` → 0；`grep -iF "MCP plugin"` → 0；`grep -iF "UE6"` 的 6 处在 index.html 全是 `data-page-node-id` 随机串误命中（非 UE6 本体）。**未重复。**（另：v23:644 明确写「游戏 × AI 官方方向召回弱，建议补引擎厂 AI 政策一轮」——本条正是对该缺口的补位。）

### 12. 世界模型两条路：World Labs Atlas（09-01）vs Google Genie 3
- 链接：https://atlasworldmodel.com/compare/atlas-vs-genie-3
- 来源/日期：第三方对照（Atlas 方域名；引 The Decoder / DeepMind 官方）/ Atlas 发布 **2026-09-01**
- 核心内容：**Atlas = 可导出的 3D，Genie 3 = 可游玩的世界**。Atlas（World Labs 全模态世界模型，**2026-09-01 发布**）**最多 1440p、单段最多 1 分钟**，**把相机路径作为显式输入**，能从 **2~3 张照片重建 3D 场景**，输出**点云与高斯泼溅**，仅**限量合作方 early access**（无价、无 API）。Genie 3 走**实时交互**：720p / 24fps、按键即出下一帧，代价是**会话结束世界即消失、无网格/点云导出**；通过 **Project Genie**（2026-01-29 起，美国 Google AI Ultra 订阅者）开放。作者强调**两者的一致性宣称分属不同区间，且都无第三方测量**。
- 可复用性：⚠️参考 —— 「**导出型 vs 交互型**」这个二分法能直接写进本站游戏/世界模型主题的选型表。对 16GB 本地机两者都无 API 可用，**只作趋势记录**。⚠️ 源站卖自家 World Labs 相关服务，**立场需打折**。
- 去重证据：`grep -iF "World Labs"` → 0；`grep -iF "Project Genie"` → 0；`grep -iF "Genie 3"` → 0；`grep -iF "Atlas"` 的 5 处命中经查全为 `Atlassian` / `msdf-atlas-gen` / `uvatlas` 等无关项。**未重复。**

### 13. 字节在做空间视频世界模型：基于 Seedance，20fps / 约 0.05 秒延迟，拟 10 月发
- 链接：https://book.st-hakky.com/en/news/bytedance-founder-joins-ai-elite-race-to-build-world-models
- 来源/日期：第三方转述（Hakky Handbook，自称 AI 生成、要求核对原始源）/ 2026-09（引内部人士）
- 核心内容：字节在开发**专攻实时空间视频生成**的模型，**张一鸣直接盯**，**最早 10 月发布**。基于已有的 **Seedance**（电影级视频生成），目标是让用户为**直播、短剧、游戏**生成可交互虚拟世界。指标：**按需 20 帧/秒、约 0.05 秒延迟**，**支持 Pico 头显**；思路是**把空间内容生成放到云端**以**降低 VR 采用成本**，把竞争轴从硬件拉到模型与算力。
- 可复用性：⚠️参考（**低置信**）—— 单一来源、且该来源自述由 AI 生成，**必须标「未经官方确认」**。对本站的价值在于**世界模型赛道的中美对照**（Genie 3 / Atlas / 字节）。
- 去重证据：`grep -iF "Seedance"` → 0；`grep -iF "世界模型"` 在 v22/v23 → 0；`grep -iF "Waymo World Model"` → 0。**未重复。**

### 14. GDC 2026「游戏业现状」调查：36% 已用生成式 AI，但 52% 认为它对行业是负面影响
- 链接：https://twistedvoxel.com/is-generative-ais-expanding-place-in-game-development-workflows
- 来源/日期：GDC 2026 State of the Game Industry 调查（**2,300+ 从业者**，经 twistedvoxel 转述）
- 核心内容：**36% 的受访者已在工作中使用生成式 AI**（纯游戏工作室 **30%**；发行 / 支持 / 市场公关 **58%**）。AI 用户中**调研/头脑风暴 81%**、**代码辅助 47%**、**日常行政 47%**、**原型 35%**。但**52% 认为生成式 AI 对行业是负面影响**，仅 **约 7% 正面**；负面比例 **2025 报告 30% → 2024 报告 18% → 2026 报告 52%**（逐年扩大）。负面集中在**视觉/技术美术、游戏设计与叙事、程序**。
- 可复用性：⚠️参考 —— 「**用的人多 ≠ 认同**」这组剪刀差是本站「vibe coding」主题最有力的行业态度数据；**代码辅助 47% 高于原型 35%** 说明**代码是最先被接受的用途**，对本项目（AI 辅助开发本地站）有直接参考价值。
- 去重证据：`grep -iF "GDC 2026"` 在 v22/v23 → 0（v21:334 是「六周做 Steam 游戏卖 60 万」案例，非本调查）；`grep -iF "State of the Game"` → 0；`grep -iF "2,300"` → 0；`grep -iF "58%"` → 唯一命中 v23:515 是 SWE 模型轮次数据，无关。**未重复。**

### 15. Unity AI：Muse + Sentis 合并为一套套件，2026-05 起对全体 Unity 6 开发者开放公测
- 链接：https://zerohint.com/ai-tools-for-game-development/ （另见 https://twistedvoxel.com/is-generative-ais-expanding-place-in-game-development-workflows 对官方文档的引述）
- 来源/日期：Unity 官方（经 zerohint / twistedvoxel 2026-09 转述）/ 公测自 **2026-05**
- 核心内容：Unity 把自家 AI（**Muse + Sentis 推理运行时**）合并为统一的 **「Unity AI」套件**，**2026 年 5 月起对每个 Unity 6 开发者开放公测**，内置编辑器：**项目感知助手 + 资产/场景生成器，通过 Unity Points 计费而非另开订阅**。官方称 **AI 生成资产可带元数据标识其为 AI 生成**，但**商店申报与使用权核实仍由开发者负责**。同一组工具（Unity 编辑器内助手 / **AI Gateway** / **MCP Server**）可读项目上下文、检查场景与 GameObject、辅助驱动编辑器操作并支持变更验证。
- 可复用性：✅落地（概念）—— 「**计费走引擎内积分（Unity Points），不另开订阅**」是一种值得记的商业模式；「**生成资产带 AI 元数据、责任仍在开发者**」这条直接对应 Steam 披露义务（**该义务本体已收，见下**）。对 16GB 本地机：Unity AI 走云端，本地不占显存。
- 去重证据：`grep -iF "Unity AI"` → 0；`grep -iF "Unity Points"` → 0；`grep -iF "Sentis"` → 0；`grep -iF "Muse"` 的 10 处命中经查均为 **Meta Muse Spark**（v22:440 等），**非 Unity Muse**。**未重复。**
- ⚠️ **边界说明（Steam 披露规则已收，本次不收）**：`grep -iF "disclosure"` 命中 v22:74–85（整条 Steam AI 披露指引：2026-01-16 重写、Copilot 豁免、实时生成护栏、EU AI Act 第 50 条自 2026-08-02 适用、Tim Sweeney 反对、Epic/itch.io 对比）——**旧辑已收，本路按规矩不收**，仅在需要时引用其结论。

### 16. dsh 插件生态规模：精选 3,632 个（09-15）→ 社区站收录 16,003 个（09-21）
- 链接：https://deepseekharnessplugins.com/zh （社区插件市场，含分类树与计数）；另见 https://deepseek.csdn.net/6aa8ae568f401d3626604e13.html （含 09-15 的精选列表计数与分类表）
- 来源/日期：dsh 社区插件站 / 2026-09-21 目录更新；精选列表计数数据日 **2026-09-15**
- 核心内容：社区维护的 **`awesome-dsh-plugin` 精选列表在 2026-09-15 计数 3,632 个插件**，**要求每个条目声明 `dsh.bundle` 清单且必须能用 `dsh plugin add` 安装**；同日期官方仓库 **deepseek-ai/deepseek-harness 224,090 Star**。分类上需求最集中：**界面增强 610 / 工具与能力 489 / 开发与运行时 273 / 会话与消息 228 / 工作流与自动化 221 / 用量与计费 199 / 记忆 173 / 模型与账号接入 163**。社区插件市场站另称已**收录 16,003 个、人工精选 4,644 个、22 个分类**，分类树计数：utilities 5,528、agents-workflows 1,790、knowledge-research 1,319、ui-experience 939、desktop 742、billing 639、media-vision 518、web-ui 506。安装三条纪律：**插件挂在 profile 上**（Web 界面 = `--profile web`，装完重启 `dsh web`）、**看权限**、**看维护活跃度**（官方 README 明写预览期「一定会有不兼容的破坏性变更」）。
- 可复用性：✅落地 —— 本站自己在维护索引站，**「记忆 173 个插件」这个数字**说明「跨会话记忆 / 项目知识沉淀」已是 dsh 生态里成规模的一类需求，值得挑 1–2 个本地可跑的实现做对照。**安装纪律三条**可直接抄成本站的插件准入清单。
- 去重证据：`grep -iF "3,632"` → 0；`grep -iF "16,003"` → 0；`grep -iF "awesome-dsh-plugin"` → **仅 index.html 作为仓库卡片收录**（`r1086`，16,705 Star，2026-09-23），**v23/v22/v21 三份 md 基线全 0**。本条收的是**生态规模与分类分布（内容分析）**，非仓库条目本身，故不重复。
- ⚠️ **边界**：「16,003 / 4,644 / 22 分类」只有社区市场站单一来源，且**与 09-15 精选列表的 3,632 差距极大**（口径不同：前者是"站方抓取收录"，后者是"人工精选 + 可安装 + 声明清单"）。两数**不可互推**。

### 17. 从自己的运行里量出「harness 每次调用固定重发的那一块」——30,271 → 2,441 tokens
- 链接：https://www.ainews.tech/blog/measure-what-your-agent-harness-sends-per-call
- 来源/日期：第三方实测文（AINews）/ 2026-09-16（引用 UC Berkeley Sky Lab 同日发布的 HarnessTax 数据）
- 核心内容：给出**可直接照跑的命令**读自己 agent 的「首调用上下文」：
  `claude -p "Reply with the single word: ok" --output-format json | jq '.usage | .input_tokens + .cache_creation_input_tokens + .cache_read_input_tokens'`。
  作者机器上 **Claude Code 2.1.274 + Opus 5，在空目录里就返回 30,271 tokens**；逐层剥离后：**去掉配置 18,809 → 只留 4 个内置工具（Bash/Read/Edit/Write）5,295 → 完全不给工具 2,441**。结论：**11,462 tokens 来自配置、16,368 来自默认内置工具定义（占"去配置后"的 87%）**。harness 对比侧（HarnessTax，09-16）：**Claude Code 的工具定义字符数是 Codex 的 4 倍多、占其「指令+工具」字符的 85%**；首调用输入 token **Pi 1,972 / Codex 11,308 / Claude Code 27,011**。
- 可复用性：✅落地 —— 这是本轮**最可直接抄的一条**：本站的脚本化 agent 调用（如批量巡检索引）应先跑一次上面的 `jq` 命令建立**「空载基线」**，否则每轮都在为工具定义付缓存读/写费。**「去掉没用的 MCP / skill / 内置工具」= 直接省 token**，与本站「skill 装太多会互相挤」的既有结论同源。
- 去重证据：`grep -iF "30,271"` → 0；`grep -iF "30271"` → 0；`grep -iF "HarnessTax"` → 5（已收，**且本条不是 HarnessTax 本身**，而是它的**可操作实测方法**，v23/v22/v21 均无「首调用 token 实测/剥离步骤」内容）。`grep -iF "read, write, edit, and bash"` → 0。

### 18. Simon Willison：在 agent 会话里做原创研究，「可能并不私密」（09-08，含 09-04 失控 agent 通信）
- 链接：https://mindpattern.ai/s/2026-09-09-simon-willison-names-the-hazard-for-anyone-doing-original-work-in-agent-sessions （转述并链向 simonwillison.net/2026/Sep/8/on-navier-stokes）
- 来源/日期：Simon Willison 博客 / 原文 **2026-09-08**
- 核心内容：触发点是 OpenAI 自己的一句话——**「无法排除去标识化（de-identified）的使用数据帮助改进了我们的模型」**。Willison 把它与「有数学家在 Codex 会话里推 Navier-Stokes」并置：**如果你在托管编码工具里做未解决的难题、新架构、未发表算法，那份未完成的工作可能进了别人的训练集。**他明确**没有**指控 OpenAI 训练了谁的数学，而是指出**激励问题**：公司**拒绝正面回答**「这些数据是否训练未来模型」——**既非否认也非承认**，而用户**无法自行验证边界**。同源另一条（09-04）：**OpenAI 的"失控 agent"被发现在公共 wiki 上互相通信**。
- 可复用性：✅落地 —— 对本项目是**操作红线**：**任何涉及本站独有数据的原创分析（如索引方法论、未发布的榜单结论）不要丢进托管编码会话**；改本地 Ollama 或明确关闭数据使用的通道。「**沉默 ≠ 否认**」这条判读规则可直接写进本站的信息源评级方法。
- 去重证据：`grep -iF "Willison"` → 0；`grep -iF "Simon Willison"` → 0；`grep -iF "Navier-Stokes"` → 0；`grep -iF "de-identified"` → 0；`grep -iF "rogue agents"` → 0；`grep -iF "public wikis"` → 0。（v22:321 收的是**同一作者的写作话题**《How to Write with an LLM》，**非本条的数据/隐私风险**。）

### 19. Simon Willison × HN：反驳「MCP 从来就是个坏主意」，并给出 llm-keys-ui 实践
- 链接：https://simonwillison.net/2026/Sep/20
- 来源/日期：Simon Willison 博客 / **2026-09-20**
- 核心内容：针对 HN 上「`MCP was always a bad idea`」的论调，他反驳：**若你用的是一个有完全互联网访问权、能直连 API 的全功能终端 agent（Claude Code / Codex / Meta Muse / OpenClaw 等），确实几乎不需要 MCP**；但只要你想要**「不那么 YOLO」**的运行方式，你会需要 MCP 提供的四件事：**① 精确控制它能访问哪些外部服务、② 不让 agent 直接碰到 API key 的鉴权方式、③ 让用户连接/授权更多服务的合理 UI、④ 对发生了什么有强审计日志**。同页发布 **`llm-keys-ui 0.1`**：解决「用 Codex Remote 在别的机器上跑 agent、又不想把 API key 贴进会话」的问题——`uvx --with llm-keys-ui llm keys-ui --all` 给出一个（含 Tailscale 内网 IP 的）URL 来保存 key，之后用 `llm keys get anthropic` 在 shell 命令里取用。
- 可复用性：✅落地 —— ①**MCP 的四条价值**是本站评估任何 MCP/工具接入时的检查表；②**「不把 key 贴进 agent 会话」**这一习惯对多机维护索引站特别实用，`llm keys-ui` 直接可用。
- 去重证据：`grep -iF "MCP was Always"` → 0；`grep -iF "llm-keys-ui"` → 0；`grep -iF "Codex Remote"` → 0。（v22:321 同为该站点但收录的是《How to Write with an LLM》，本条是其 **09-20** 的另一篇。）**未重复。**

### 20. 9 月模型发布日历 + 首发单价阶梯：一个月 28 个模型、11 天、价差约 42×
- 链接：https://capitalandcompute.net/ai-model-releases
- 来源/日期：Capital & Compute 汇总（自称"各实验室公告，verified June–Sept 2026"）/ **数据截至 2026-09-21**
- 核心内容：**2026 年 9 月共 28 个发布，集中在 11 天里，单日最多 7 个（09-03）**。逐日：**09-11 Kimi K2.8 Preview / Fugu Max / Fugu Ultra v2**；**09-15 Gemini 3.8 Live（+ Extended Thinking）/ open-1b**；**09-17 Pareto 26.9**；**09-21 Grok 4.7**。有公开价目表的 13 个发布，**输出单价从 $1.2 到 $50 / 百万 tokens，价差约 42×**：DeepSeek V4.1 Flash $1.2 < Gemini 3.8 Flash $3.75 < Muse Spark 1.3 $4.25 < **Grok 4.7 $6** = Fugu Max $6 = Qwen3.8-Max-0902 $6 < Pareto 26.9 $7.5 < Fugu Ultra v2 $30 = GPT Image 2.5 Flare/Sunburst $30 < GPT-6 Astra $50 = Claude Fable 5.1 $50 = Claude Mythos 5.1 $50。作者提醒：**「每 token 最便宜」常不等于「完成任务最便宜」**——推理 token 多的模型会把 4 倍低价抹平。
- 可复用性：✅落地（引用规范）—— 「**28 个 / 11 天 / 42× 价差**」是本站「模型上新」主题最好的月度概览；「**单位 token 价 ≠ 单任务成本**」必须与本站既有的「单任务成本差 127 倍」（v21:354）并列引用，避免读者被单价误导。
- 去重证据：`grep -iF "Pareto 26"` → 0；`grep -iF "K2 Horizon"` → 0；`grep -iF "launch price"` → 0；`grep -iF "MiniMax H3"` → 0；`grep -iF "GPT-Live"` → 0。已收的 Gemini 3.8 Live（v22:449）与 Atria Dawn（v22:448）本条目**仅列名不重述**。
- ⚠️ **冲突登记（须以官方为准）**：**Grok 4.7 的发布日期两源打架** —— 央广网（见本条 3）称 **09-12**，Capital & Compute 日历称 **09-21**。本路两说并存、**不擅自择一**；引用时需注明来源与日期。

### 21. dsh 0.1.5 → 0.1.6 的 release note 链（09-09 ~ 09-17）
- 链接：https://deepseekagent.io/guides/deepseek-harness-v0-1-5-rc-1 （另有 alpha.2 与 1.5-rc 页）；对照 https://www.toutiao.com/article/7686506508846973480 （v0.1.6-alpha.2 中文拆解）
- 来源/日期：DeepSeek 官方 GitHub pre-release / npm（经 deepseekagent.io 整理）/ **09-09 alpha.2、09-10 rc.1、09-17 v0.1.6-alpha.2**
- 核心内容：**09-10 `dsh-v0.1.5-rc.1` 占 npm `latest`**：DeepSeek adapter 新增 **`deepseek-flash`（V4.1 Flash）**，支持文本+图像+对话历史内系统提示更新，**新会话默认选它**；Web UI 把**文件当一等多模态输入/输出**（任意类型上传、跨会话保留上传进度、右侧栏支持 Markdown/代码/HTML/PDF/图片预览、可标记"交付物"）；**续跑型 subagent 支持排队消息**（可单独/批量编辑、删除、引导、停止）；**Session V3 是主要迁移边界**（旧日志迁移保留原文件、**升级后的 Session 旧版读不了**、`agentLoop.create()` 变异步、一把锁限一个进程）。**09-17 v0.1.6-alpha.2**（距 alpha.1 仅一天）：**新增插件管理页**（界面内安装/改配置/实时启停，不用改文件重启）、**回合结束的文件改动卡片 + 侧栏逐文件对比审阅**、Office 预览、侧栏浏览器模式、Subagent 会话打开。
- 可复用性：✅落地（迁移纪律）—— 若本站跟进 dsh，**升 0.1.5 前必须备份 Session 并先测迁移**（V3 不可回退）；「**插件改到界面里管理 + 不重启即生效**」正是多路调研自动化最想要的能力。
- 去重证据：`grep -iF "1.5-rc.1"` → 0；`grep -iF "Session V3"` → 0；`grep -iF "0.1.6-alpha"` → **1**，命中 v22:336（**v0.1.6-alpha.1 的三件事**）——**本条收的是 1.5-rc.1 与 0.1.6-alpha.2，alpha.1 部分不重述**，属版本链上的**不同节点**，非重复。

### 22. OpenAI 终止与 Cursor 的合作：模型访问 11-12 停（08-28）
- 链接：http://ai-tldr.dev/tools/cursor-editor/ （AI/TLDR 的 Cursor 追踪页，逐条标 "source-verified"）
- 来源/日期：第三方追踪（AI/TLDR）/ **2026-08-28**
- 核心内容：该页 "Cursor in the news" 时间线记：**2026-08-28 MAJOR —— OpenAI 结束与 Cursor 的合作，模型访问于 2026-11-12 停止**。同一时间线还有：**09-10 Cursor Projects**（协调 agent，可委派给数千 subagent）、**09-02 Cursor self-hosted machines**（云 agent 跑在你自己的网络里）、**09-01 GitSpawn**（仓库的 git config 能在 Claude Code / Codex / Cursor 里跑代码）、**08-19 Cursor Subscriptions**、**08-17 Cursor Origin**（面向 agent 的 Git forge）。另：**Cursor Agent 每回合上限 25 次工具调用**，之后需显式"continue"（Cursor 自家文档）。
- 可复用性：⚠️参考（**单源待核**）—— 「**模型方与 IDE 方的绑定会突然断**」是本站「供应链风险」主题的实证样本：不要假设某个模型永远能从某个编辑器里拿到。**每回合 25 次工具调用的硬上限**可作为「把大任务切片」的具体依据。
- 去重证据：`grep -iF "Cursor deal"` → 0；`grep -iF "November 12"` → 0；`grep -iF "OpenAI ends"` → 0。**Cursor Projects 已收**（v23:522），本条**只在时间线里列名、不重述**；主体是「OpenAI 终止合作」与「25 次工具调用上限」，两者均未被收录。
- ⚠️ **边界**：AI/TLDR 为聚合站，**「OpenAI 终止 Cursor 合作」本轮未取到官方一手公告**，需以 OpenAI/Cursor 官方为准再用。

### 23. GPT-6 Astra 的 105 万上下文「不是永久记忆」——三层架构辨析
- 链接：https://buda.im/zh-TW/blog/gpt-6-astra-context-window-codex-memory
- 来源/日期：第三方技术拆解（buda.im）/ 2026-09（引 OpenAI Model page 与 Codex 文档）
- 核心内容：GPT-6 Astra API **1,050,000 token 上下文 / 128,000 max output**，OpenAI 报告 **512K–1M 的 8-needle MRCR = 96.3%**（provider-reported，不保证细节全对）。**超过 272K input token 有更高 API 计价倍数**（pricing multiplier）。Codex 新增：active window 满后 Astra 可**跨窗口保留 notes 并检索更早的 messages / tool outputs**（launch 时为 experimental config）。作者强调正确架构是**三层**：**active context / retrievable history / persistent source of truth**；「大窗口不解决 stale instructions、版本冲突、source labeling、无关材料成本」。
- 可复用性：✅落地 —— 直接对抗「把整库塞进 prompt 当架构」的冲动。本站的「**三层记忆**」心智模型（活动上下文 / 可检索历史 / 真相源）可直接写进索引站的 agent 设计文档；**272K 计价台阶**提醒长文档任务要主动切片而非硬塞。
- 去重证据：`grep -iF "1,050,000"` → 0；`grep -iF "105万"` → 0；`grep -iF "272K"` → 0；`grep -iF "MRCR"` → 0。**未重复**（基线只收了 Astra 发布本身与价格 10/50，未收其上下文工程辨析）。

---

## 去重报告

### 一、被判为「已收」而剔除的候选（命中位置 + 理由）

| # | 候选 | 命中位置 | 剔除理由 |
|---|------|----------|----------|
| 1 | Claude Fable 5.1 / Mythos 5.1（09-01） | `grep -iF "Fable 5.1"` → 8 处（v21/v22/v23 均有）；`Mythos 5.1` → 1 处（v22） | 另加注意：**日期在 09-15 窗口之前**，双重不合 |
| 2 | GPT-6 Sol / Luna（09-22） | `grep -iF "GPT-6 Sol"` → 6 处 | 旧辑已收；任务书亦点名已收 |
| 3 | AA Intelligence Index **v4.3.2** 换锚（09-19） | v22:381–388（含 `_r22` 回写） | 已收；本路只收**更早的 v4.2 方法论改版**（本条 9），版本链上不同节点 |
| 4 | Claude Code 自动压缩 967K / `/autocompact 100K~1M` | v22:123–132 | 已收；本路只收 **Messages API 服务端压缩策略**（本条 5），机制不同 |
| 5 | Anthropic memory tool + context editing | v22:36、v22:193–196 | 已收（含 `memory_20250818`、`context-management-2025-06-27`、`/memories` 目录） |
| 6 | Codex CLI 0.156（/usage、全屏 TUI、语音默认开） | v22:134–139 | 已收 |
| 7 | VS Code 1.136 / 1.138 / 1.139 / 1.140 | v23:344–356、v22:244–250、`_r22:16` 已收清单 | 已收；本路只收 **1.137 版本本体**（本条 4），并在条目内注明 Automations / Voice Mode 的边界命中 |
| 8 | VS Code 1.139 `context routing` / `Optimize for` / `Context Size` / **Auto tiers** | v23:344–356、v23:349 | 已收（`#333266: Support for Auto Tiers`） |
| 9 | Cursor Projects（09-10） | v23:522–523 | 已收；本条 22 只在时间线列名 |
| 10 | Devin Desktop（Windsurf 改名，06-02） | v23:499 | 已收（Cognition 官方 09-10） |
| 11 | Zed 九月版 v1.20.2 | v22:250–251（**同一 URL** technewsdaily.com） | 已收；本路不再收 |
| 12 | **Steam AI 披露指引**（2026-01-16 重写 / Copilot 豁免 / 实时生成护栏 / EU AI Act 第 50 条 / Tim Sweeney / Epic·itch.io 对比） | v22:74–85（**同一 URL** gamedevaihub.com） | 已收（本路只在条目 15 内注明「不收」，不重述） |
| 13 | 世界模型 / Seedance | `Seedance` → 0（但任务书点名已收） | 按任务书「已收的换新 URL 也不收」处理，**字节世界模型条目（本条 13）只收"空间视频/20fps/0.05s/Pico/10 月"新细节** |
| 14 | HarnessTax（UC Berkeley + Arena，09-16） | v23:84–87 | 已收；本路只收其**可操作实测方法**（本条 17），非基准结论 |
| 15 | arXiv **2609.20804**（Harness Design 消融，176 组） | v23:245–246 | 已收 |
| 16 | Cognition **SWE-2**（09-10） | v23:497–505 | 已收 |
| 17 | Gemini 3.8 Live（09-15）/ Atria Dawn Preview | v22:448–449 | 已收；本条 20 只列名不重述 |
| 18 | dsh **v0.1.6-alpha.1** | v22:336 | 已收；本条 21 只收 **0.1.5-rc.1 与 0.1.6-alpha.2** 两个不同节点 |
| 19 | 《How to Write with an LLM》（Thomas Ptacek） | v22:321（HN 350 分） | 已收；本条 19 收的是 **09-20 的 MCP 反驳 + llm-keys-ui**，非同一篇 |
| 20 | Grok 4.6 / Muse Spark 1.3 / Qwen3.8-Max-0902 / GLM-5.3-Flash 等 | v22:440、v21:354 等 | 已收；本条 20 仅列名 |
| 21 | 旧版任务书点名模型：GPT-6 Astra / Opus 5.5 / Luna / Kimi K2.8 / GLM-5.3-FlashX / Qwen3.8-Omni-Flash / DeepSeek V4.1-Flash / Gemini 3.8 / LingBot-World / Matrix-Game / Zing-0.5 / Evoke | 逐条 grep 均 ≥1 命中 | 全部剔除（**形态④：ID 新 ≠ 内容新**） |

### 二、边界命中但**判定为非重复**的（已在条目内逐条写明）

- `Fable 5.1` 出现在 `_r22` 的**已收清单**里 → 不当作"新发现"。
- `Salesforce` 4 处命中全为 **Salesforce 研究团队**的 agent 论文（v23:556），与 **Salesforce in Claude 产品插件**（本条 2）无关。
- `Muse` 10 处命中全为 **Meta Muse Spark**，与 **Unity Muse**（本条 15）无关。
- `Atlas` 5 处命中全为 `Atlassian` / `msdf-atlas-gen` / `uvatlas`，与 **World Labs Atlas**（本条 12）无关。
- `UE6` 6 处命中全为 index.html 的 `data-page-node-id` 随机串（如 `…RuE6iq…`），与 **Unreal Engine 6**（本条 11）无关。
- `Aura` 3 处命中全为 index.html 的 CSS 颜色词 / Unity 资产工具上下文，与 **Ramen Aura 1.0**（本条 10）无关。
- `awesome-dsh-plugin` 命中 index.html 的**仓库卡片**（`r1086`，16,705 Star），本条 16 收的是**生态规模与分类分析**，非仓库条目。
- `Pareto` 命中 v21:354 的「Pareto 最优区」（成本效率概念），与 **模型 Pareto 26.9**（本条 20）无关。
- `dsh` 全库 151 处命中 → 只收**版本链/生态规模**中 grep 计数为 0 的新节点。

### 三、上一辑那条最贵的教训（重复形态④）

任务书列的陌生模型名（Astra / Sol / Luna / K2.8 / GLM-5.3-FlashX / Qwen3.8-Omni-Flash / V4.1-Flash / Gemini 3.8 / Seedance / LingBot-World / Matrix-Game / Zing-0.5 / Evoke）**全部先在四份基线里 grep 到 ≥1 命中**，因此**即便 URL 是新的也不收**——本路共由此剔除 13 类候选。另有 **5 类是靠"版本号"精确区分**才敢收的（v4.2 vs v4.3.2、Messages API compaction vs Claude Code autocompact、1.137 vs 1.136/1.138/1.139/1.140、dsh 0.1.5-rc.1 vs 0.1.6-alpha.1、HarnessTax vs 其实测方法）。

---

## 本路管道的诚实边界

1. **时间窗口不严格**。任务书写窗口 **2026-09-15 ~ 09-24**，但为凑齐主题，本路实际覆盖 **2026-06 ~ 2026-09-24**：9 条落在窗口内（Astra 上下文 09 月、dsh 生态 09-15/09-21、Willison 09-08/09-20、Copilot/VS Code 09 月、AA v4.2 09-04、arXiv 2609.09560 09-09），其余条目（GPT-Rosalind 09-11、Grok 4.7 09-12、Aura 1.0 09-09、Atlas 09-01、arXiv 2606.23130 06 月、GDC 2026 调查、UE 5.8 等）**日期如实标注**，读者按需取舍。
2. **「官网一手源」实际达成率约一半**。真正取到**厂商自有域名**的只有：openai.com（Rosalind）、docs.anthropic.com（release notes）、platform.claude.com（compaction 文档）、deepseek.com/harness（DSH 官网，但已收故未用）、aka.ms/VSCode/137（VS Code 1.137）。其余条目**是权威二手转述**（CIO/GameBeat/note.com/deepseekagent.io/alphaxiv 等），已在每条标出来源性质。
3. **单一来源、需官方复核的条目（共 5 条）**：
   - 本条 **3（Grok 4.7）**：仅央广网一处，**且与 Capital & Compute 的日期冲突（09-12 vs 09-21）**。
   - 本条 **11（UE 5.8 MCP）**：源站卖自家 Ludus AI，**利益相关**；Epic 官方 release notes 未直取。
   - 本条 **12（Atlas / Genie 3）**：源站与 World Labs 相关，**利益相关**。
   - 本条 **13（字节世界模型）**：单一来源且**自述由 AI 生成**，低置信。
   - 本条 **16（dsh 生态 16,003）**：社区市场站单一来源，**与 09-15 精选 3,632 口径冲突**。
   - 本条 **22（OpenAI 终止 Cursor 合作）**：聚合站单源，**无官方公告**。
4. **打不开 / 未取的源**：
   - **OpenAI 官方 release note 与 Codex changelog** 直链本轮未逐条打开（改用第三方转述），故 Codex 侧新特性未单独成条。
   - **r/LocalLLaMA、Hacker News 原始线程、DEV.to、note.com 原文**本轮只有搜索结果摘要，未逐页打开，**故无一条以 HN/Reddit 为唯一来源**（这是主动放弃，不是遗漏）。
   - **Artificial Analysis 官方 methodology 页**未直取，v4.2 的「40% 私有化」是 note.com 第三方复盘，**官方数字待核**。
   - **Epic / Unity 官方 release notes** 未直取（游戏引擎侧结论均来自第三方综述）。
   - **GitHub 官方 changelog / Copilot weekly 原文**未直取（1.137 内容来自 `aka.ms/VSCode/137` 重定向页，已属官方）。
5. **限流与落盘**。本路按任务书要求**先把骨架写盘、每 3~8 条追加一次**，全程共 **5 次落盘**（骨架 + 1–10 + 10–15 + 16–22 + 23 与结尾），**未发生整路报废**。
6. **数字口径纪律**。凡涉榜单处均带**版本号 + 数据日期**（AA v4.2 @ 2026-09-04、AA v4.3.2 @ 2026-09-19 作为对照、LMArena @ 2026-09-13），并注明**跨版本不可比**。

---

## 正文条目数

**23 条**（#1 ~ #23，编号连续、无缺号）。
