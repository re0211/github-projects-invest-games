# 第二十二辑 · GitHub 路（仓库与工具链本体）

> 调研日期 2026-09-24 · 责任：r22-gh · 用户画像：Windows 本机 16GB RAM + 本地 Ollama + 远程上财 Ollama 桥，做 Ren'Py 视觉小说 / AI agent 工具调研 / 索引站维护
> 全部条目均以 `gh api repos/{owner}/{repo}` 核实 stars/license/language/updated_at。

## 一、游戏 / Ren'Py 与 AI 集成

### GameStringer（rouges78/GameStringer）★119
https://github.com/rouges78/GameStringer · 语言 TypeScript · license NOASSERTION · updated 2026-09-23
**是什么**：桌面程序，自动识别单机游戏的引擎、抽取文本、用本地或云端 AI 翻译、再把译文补丁打回游戏。支持 20+ 引擎、20+ AI 提供方、11 种界面语言。
**为什么值得看**：和 Ren'Py 视觉小说本地化直接对口；"识别引擎 → 抽文本 → 翻译 → 回填"这条流水线本身就是可抄的架构，且支持本地模型（可接你自己的 Ollama，不上云）。
**可复用性**：落地 —— 16GB 本机跑本地翻译模型 + 该工具的回填逻辑，可替代手工改 .rpy 文本。注意它是 source-available，不是标准 OSI 许可，商用前需看条款。

### tav2（Drhushi/dsh-plugin-tav2）★22
https://github.com/Drhushi/dsh-plugin-tav2 · 语言 TypeScript · license MIT · updated 2026-09-18
**是什么**：DeepSeek Harness 插件，把游戏本地化做成"跟 AI 对话完成全流程"。内部是引擎适配器架构，首发适配 Ren'Py。
**为什么值得看**：这是本轮唯一"DSH 插件 + Ren'Py"交叉的活跃项目，且引擎适配器写法给了你扩展自己引擎的思路；你本来就在用 dsh，装上试成本极低。
**可复用性**：参考 —— 架构（引擎适配器 + 对话式编排）值得抄，作为成品还要看它 Ren'Py 文本抽取的完整度；星数少、单人维护，别当生产依赖。

### RenPy ChatGPT Example（Taiko3615/RenPyChatGPTExample）★38
https://github.com/Taiko3615/RenPyChatGPTExample · 语言 Ren'Py · license GPL-3.0 · updated 2026-09-19
**是什么**：一个小而完整的示例，演示怎么在 Ren'Py 里放一个 ChatGPT 插件，让游戏内对话调用大模型。
**为什么值得看**：代码量小、结构清楚，是把"LLM 接进 Ren'Py 运行时"讲明白的最短路径；换成 Ollama 的 /v1/chat/completions 即可本地化。
**可复用性**：参考 —— 拿它当 Ren'Py 侧 HTTP 调用的模板，自己重写许可干净的实现（GPL-3.0 会传染，别直接抄进闭源商业作）。

### Godot MCP Native（yurineko73/Godot-MCP-Native）★801
https://github.com/yurineko73/Godot-MCP-Native · 语言 GDScript · license MIT · updated 2026-09-23
**是什么**：用 Godot 原生 HTTP 实现的 MCP Server 插件，不装任何依赖、开箱即用，让 AI 工具直接操作 Godot 编辑器（场景/脚本/节点等常见操作）。
**为什么值得看**：虽然你在做 Ren'Py，但这是"引擎内嵌 MCP"这个模式目前最干净的实现——零依赖、纯原生。做 Ren'Py 侧类似桥接时，它的"不引入外部运行时"取舍很值得学。
**可复用性**：参考 —— 引擎内嵌 MCP 的样板；不直接用于 Ren'Py（Ren'Py 用 Python，需换实现）。

> 备选（本轮未占名额，已核实数据，留待下轮）：`tomyud1/godot-mcp` ★434 · GDScript · MIT · 2026-09-21（与 Godot-MCP-Native 同为 Godot MCP 实现，本次只取原生化那一个）。

## 二、Agent harness / 框架

### Omnigent（omnigent-ai/omnigent）★10197
https://github.com/omnigent-ai/omnigent · 语言 Python · license Apache-2.0 · updated 2026-09-24
**是什么**：开源 agent 框架兼"元 harness"：把 Claude Code、Codex、Cursor、Pi 和自定义 agent 编排到一起，换 harness 不用重写代码，可加策略与沙箱、跨设备实时协作。
**为什么值得看**：你同时在用 dsh / Claude Code / 各种 CLI，这种"harness 之上的统一调度层"正是痛点；Apache-2.0 干净，README 里的 adapter 接口设计可借鉴。
**可复用性**：参考 —— 概念可抄；真跑起来对单机 16GB 偏重，建议先读架构再决定是否引入。

### Gentle-AI（Gentleman-Programming/gentle-ai）★7209
https://github.com/Gentleman-Programming/gentle-ai · 语言 Go · license MIT · updated 2026-09-24
**是什么**：一个 Go 二进制，用来"配置你已有的 AI 编码 agent"（Claude Code、Cursor、OpenCode、Codex、Pi 等）：勾选持久记忆、skills、MCP server、persona、审查策略等。
**为什么值得看**：不想被单一 agent 绑定时的中间层；和 engram 同一作者（Gentleman-Programming），两者常配套用。对维护多套配置的个人开发者省事。
**可复用性**：落地 —— Go 单二进制，Windows 可直接跑；用来统一你本机多个 agent 的记忆/skills 配置。

### zot（patriceckhart/zot）★344
https://github.com/patriceckhart/zot · 语言 Go · license MIT · updated 2026-09-24
**是什么**：又一个编码 agent harness，主打轻量、纯 Go。
**为什么值得看**：轻量 Go 实现读起来快，适合当"自己搓一个 harness"的参考底本；比 Omnigent 那种大框架更贴近个人开发者的可维护规模。
**可复用性**：参考 —— 作为自建 harness 的骨架参考。

## 三、上下文管理与压缩

### Headroom（headroomlabs-ai/headroom）★73669
https://github.com/headroomlabs-ai/headroom · 语言 Python · license Apache-2.0 · updated 2026-09-24
**是什么**：在工具输出、日志、文件、RAG 片段进入 LLM 之前先压缩它们。官方数据：编码 agent 省约 20% token，JSON 省 60~95%，答案不变。提供库、代理、MCP server 三种形态。
**为什么值得看**：本轮上下文主题里体量与活跃度最高的一条；"压缩后再喂模型"这个位置比"改 prompt"更通用，且 Apache-2.0。对本地小上下文模型（你 16GB 跑 7B 级）收益尤其明显。
**可复用性**：落地 —— 直接作为 MCP server 或本地代理接进 dsh/Claude Code，先拿 JSON/日志场景试收益。

### Paritok 4B（Paritok-official/paritok-4b-v1）★1454
https://github.com/Paritok-official/paritok-4b-v1 · 语言 Python · license Apache-2.0 · updated 2026-09-23
**是什么**：非破坏性的"压缩网关"，用自己的开源 code-native 4B 模型做上下文压缩，号称首轮省 25%、长会话省 85%+，同样窗口能塞约 3 倍轮次。对 Claude Code、Cursor、Codex、OpenHands 等即插即用。
**为什么值得看**：它把一个 4B 压缩模型开源出来，等于给了"压缩质量 vs 本地算力"的可选档位；4B 在 16GB 机器上跑得动，这点对你很关键。
**可复用性**：参考偏落地 —— 网关接法是 drop-in；但要评估本机同时跑压缩模型 + 主力模型的显存/内存余量。

### sqz（ojuschugh1/sqz）★629
https://github.com/ojuschugh1/sqz · 语言 Rust · license NOASSERTION · updated 2026-09-24
**是什么**：Rust 写的上下文压缩器，在工具输出进入模型前压缩，把重复内容去重成 13-token 的引用；Claude Code、Cursor、Codex、Zed 及任意 MCP 客户端可用，**零 LLM 调用**。
**为什么值得看**："零 LLM 调用"是关键——不额外占你的本地算力、不引入延迟，纯确定性去重。适合作为 Headroom 之外的低成本选项。
**可复用性**：落地 —— Rust 单二进制，本地零开销；适合先上它看省多少再决定要不要上模型压缩。

### distill（Siddhant-K-code/distill）★181
https://github.com/Siddhant-K-code/distill · 语言 Go · license MIT · updated 2026-09-24
**是什么**：LLM agent 的上下文智能层：持久记忆 + 写入去重 + 敏感度打标 + 冲突检测 + 分层衰减，约 12ms，**不调用 LLM**。
**为什么值得看**：把"记忆生命周期管理"（衰减、冲突、去重）做进写入路径，这个设计比单纯做摘要更接近真实需求；MIT、Go、快。
**可复用性**：参考 —— 它的写入去重/衰减策略可直接借用到你索引站的知识条目去重流程。

### token-optimizer-mcp（ooples/token-optimizer-mcp）★536（备选，未占正式名额）
https://github.com/ooples/token-optimizer-mcp · 语言 JavaScript · license MIT · updated 2026-09-23
**是什么**：测量各 AI 编码 agent 的 token 节省量、优化上下文，并在 16 个 CLI 客户端之间共享一个本地知识图谱。
**为什么值得看**：卖点为"可测量"——能给手里几套 agent 各自省了多少 token 出数，选型有依据。
**可复用性**：参考 —— 度量思路最值得抄；本轮因与第三节其余压缩工具职能重叠，降为备选留档。

## 四、Memory 层（记忆服务器 / 存储格式 / 整合）

### engram（Gentleman-Programming/engram）★6786
https://github.com/Gentleman-Programming/engram · 语言 Go · license MIT · updated 2026-09-24
**是什么**：面向 AI 编码 agent 的持久记忆系统，AGPL/agent 无关的 Go 二进制，内含 SQLite + FTS5、MCP server、HTTP API、CLI 与 TUI。
**为什么值得看**：单二进制 + SQLite 这个组合在 16GB Windows 上几乎零负担，agent 无绑定；和同作者的 gentle-ai 是配套生态。本轮 memory 主题里工程完成度最高的一条。
**可复用性**：落地 —— Go 二进制直接跑，先接 dsh，看跨会话召回是否真的有用。

### Nocturne Memory（Dataojitori/nocturne_memory）★1371
https://github.com/Dataojitori/nocturne_memory · 语言 Python · license MIT · updated 2026-09-24
**是什么**：轻量、可回滚、可视化的 MCP 长期记忆服务器，用"图状结构化记忆"替代向量 RAG，号称任何模型/会话/工具都能持久；是 OpenClaw 的 drop-in 替代。
**为什么值得看**："可回滚 + 可视化"是记忆系统常缺的两块——记忆被污染时能退回上一个状态，这对长期跑的 agent 很重要。
**可复用性**：落地 —— Python + MCP，本地起服务即可；向量 RAG 的替代路线值得试。

### okf-agent-memory（okf-memory/okf-agent-memory）★722
https://github.com/okf-memory/okf-agent-memory · 语言 Go · license MIT · updated 2026-09-23
**是什么**：Git 原生的 agent 持久记忆，实现 Google OKF v0.2 规范；纯 Go，内嵌 MCP server，内存内 BM25 搜索亚 300µs，渐进式披露，宣称省 80% 上下文膨胀，零外部数据库。
**为什么值得看**："Git 原生"意味着记忆可 diff、可版本化、可同步——正好贴合你维护索引站的习惯；纯 Go 无依赖，Windows 友好。
**可复用性**：落地 —— 记忆即文件、进 Git，和你现有 repo 工作流天然兼容。

### aoci-code（aoci-spec/aoci-code）★550
https://github.com/aoci-spec/aoci-code · 语言 Go · license NOASSERTION · updated 2026-09-24
**是什么**：一个持久、Git 版本化的"代码库 + 数据库 schema 地图"，agent 动手前先读它；本地优先的 MCP server + CLI（Go），给 Claude Code、Codex、Cursor、opencode 提供长期上下文与代码智能。
**为什么值得看**：和 okf-agent-memory 是"记忆存什么"的两种答案：一个存事实、一个存代码知识地图。你维护索引站时，"agent 先读地图再动手"这个约束很实用。
**可复用性**：参考 —— 代码知识地图的构建思路可复用；license 非标准，商用留意。

### atomicmemory（atomicstrata/atomicmemory）★431（备选，未占正式名额）
https://github.com/atomicstrata/atomicmemory · 语言 TypeScript · license NOASSERTION · updated 2026-09-23
**是什么**：可移植的语义记忆：核心引擎 + TS SDK + 框架适配器 + MCP server + CLI + 宿主插件。
**为什么值得看**：定位"可移植"、不锁单一 agent；TS 生态集成面广。
**可复用性**：参考 —— license 非标准，谨慎；报名原因仅是留档。

## 五、VS Code 扩展 / vibe coding 工具与安全扫描

### OpenCursor（PawanOsman/OpenCursor）★6024
https://github.com/PawanOsman/OpenCursor · 语言 TypeScript · license 未标注/需核 · updated 2026-09-24
**是什么**：开源版"类 Cursor"的 VS Code 扩展：agent 式对话、多 provider（含 OpenAI、Ollama、llama.cpp）、语义搜索、MCP 支持。
**为什么值得看**：明确支持 Ollama / llama.cpp 本地后端——正是你的技术栈；6k 星、活跃，是"VS Code 里用本地模型做编码 agent"目前最直接的开源选项。
**可复用性**：落地 —— 装上直连本机 Ollama，替代部分 Cursor 场景，省订阅。

### SpecStory（specstoryai/getspecstory）★1339
https://github.com/specstoryai/getspecstory · 语言 Go · license Apache-2.0 · updated 2026-09-24
**是什么**：本地优先的扩展，收集你在各 AI IDE / 终端 agent 里的对话历史，用 Lore 把历史加工成可复用 skills，也可同步到云端。
**为什么值得看**："把历史对话沉淀成可复用资产"这件事，正是你索引站方法论的技术化版本；本地优先 + Apache-2.0，隐私友好。
**可复用性**：落地 —— 用来把散落在各 agent 里的会话变成可检索素材，反哺索引站。

### vibescan（Armur-Ai/vibescan）★82
https://github.com/Armur-Ai/vibescan · 语言 Go · license 未标注/需核 · updated 2026-09-23
**是什么**：针对 AI 生成（"vibe-coded"）代码的安全扫描器：跑 SAST、DAST 和沙箱化漏洞利用模拟，覆盖 15+ 语言、30+ 工具，带 AI 修复建议和 PR 审查集成。
**为什么值得看**：vibe coding 的最大风险就是安全债；这个把"扫描 + 复现利用 + 修复建议"串起来，比单纯 lint 高一层，Go 单文件易跑。
**可复用性**：参考 —— 本地跑一遍自己 agent 生成的代码；license 待确认。

### Vibeship Scanner（vibeforge1111/vibeship-scanner）★129
https://github.com/vibeforge1111/vibeship-scanner · 语言 Python · license 未标注/需核 · updated 2026-09-21
**是什么**：免费的 vibe coding 漏洞扫描器，2000+ 规则集，并给一段可复制的"Master AI Fix Prompt"用来让 AI 修漏洞。
**为什么值得看**：规则多、Python 易改；"扫出问题 → 直接给 AI 一个修复 prompt"这个闭环对个人开发者很实用。
**可复用性**：参考 —— 规则集和修复 prompt 模板可借鉴；单人项目，别当唯一防线。

### oh-my-agent（first-fluke/oh-my-agent）★1324
https://github.com/first-fluke/oh-my-agent · 语言 TypeScript · license MIT · updated 2026-09-23
**是什么**：给 AI 编码 agent 做"机械式验证"：skills 包或整套 harness（stop-hook 门禁、产物校验、独立评审员）。
**为什么值得看**：它针对的是 agent"谎报完成"的顽疾——用 stop-hook 门禁和独立 judge 卡住产出。你的 dsh 工作流可直接套用"完成前先过校验"的模式。
**可复用性**：落地 —— skills 包形态即插即用；MIT。

## 六、DSH（DeepSeek harness）生态

### dsh-vision-router（ysr666/dsh-vision-router）★1116
https://github.com/ysr666/dsh-vision-router · 语言 JavaScript · license MIT · updated 2026-09-24
**是什么**：给"纯文本"的 DSH agent 装上眼睛：内置免 key 的视觉链，外加像素级视觉工具（问答、grounding、裁剪、像素 diff、取色、OCR、SVG 描摹、抠图、截图）。一条命令装，无需 Python。
**为什么值得看**：DSH 生态本轮最热插件之一；免 key + 无需 Python，对你 Windows 环境极友好。"图片轮次当成普通工具调用轮"这个设计很巧。
**可复用性**：落地 —— 直接装进 dsh，拿来做截图 OCR / UI 比对。

### DSH-X（yyh-001/DSH-X）★419
https://github.com/yyh-001/DSH-X · 语言 JavaScript · license MIT · updated 2026-09-24
**是什么**：DSH 的轻量启动器：选一个版本，在系统浏览器里启动 dsh web，并管理插件（Windows / macOS）。
**为什么值得看**：你既然在用 dsh，版本切换 + 插件管理是日常刚需；这类工具能显著降低维护摩擦。
**可复用性**：落地 —— Windows 本机直接用。

### billion-context-dsh（Tyan66666/billion-context-dsh）★107
https://github.com/Tyan66666/billion-context-dsh · 语言 TypeScript · license MIT · updated 2026-09-24
**是什么**：给 DSH 做"模型驱动的上下文管理"（Active Context Pruning / ACP）——由模型决定何时压缩什么；从 billion-context-pi 移植，acp-kernel 原样复用；后端 CompactionEngine，带 compress/decompress/search_context/acp_status 工具。
**为什么值得看**：这是 DSH 生态里唯一把"上下文压缩"做成一等公民的插件，和第三节的通用压缩工具形成"DSH 内建 vs 外挂"对照。
**可复用性**：落地 —— 装进 dsh 试；作者单人，注意后续维护。

### dsh-commandcode-provider（Mars-Sea/dsh-commandcode-provider）★319
https://github.com/Mars-Sea/dsh-commandcode-provider · 语言 TypeScript · license MIT · updated 2026-09-24
**是什么**：DSH 的 Command Code provider 插件：接入 Command Code 模型、实时模型目录、按套餐选模型、推理力度、图像输入、联网搜索、多账号。
**为什么值得看**：DSH 接第三方模型网关的样板；"按套餐感知选模型 + 多账号"是实用细节。
**可复用性**：参考 —— 想给 dsh 接自建/远程（如你上财桥）provider 时，它的插件结构可直接照搬。

## 七、模型本地推理与评测工具

### ollama-benchmark（aidatatools/ollama-benchmark）★390
https://github.com/aidatatools/ollama-benchmark · 语言 Python · license MIT · updated 2026-09-21
**是什么**：通过 Ollama 测本地 LLM 吞吐（tokens/s 等）的基准工具。
**为什么值得看**：你本机 16GB + Ollama，正需要量化"这台机器跑得动哪个模型、多快"。工具轻、直接给数。
**可复用性**：落地 —— 跑一遍建你的本地模型性能基线表。

### Claw-Eval（claw-eval/claw-eval）★774
https://github.com/claw-eval/claw-eval · 语言 Python · license MIT · updated 2026-09-23
**是什么**：把 LLM 当 agent 来评测的 harness，所有任务经人工核验。
**为什么值得看**：agent 能力评测的"任务经人工核验"这点难得，结果可信度高于自动生成的题库；MIT。
**可复用性**：参考 —— 评测方法论可借鉴；若要跑需自备模型与算力。

### ClawProBench（suyoumo/ClawProBench）★824
https://github.com/suyoumo/ClawProBench · 语言 Rust · license Apache-2.0 · updated 2026-09-24
**是什么**：在 OpenClaw 运行时评测 LLM agent 的 live-first 基准 harness，确定性打分 + 多次试验可靠性。
**为什么值得看**："确定性打分 + 重复试验"直击 agent 评测的方差问题；Rust 实现跑得快。适合想严肃比较不同 harness/模型的人。
**可复用性**：参考 —— 评测设计值得读，落地需 OpenClaw 运行时。

### little-coder（itayinbarr/little-coder）★2618
https://github.com/itayinbarr/little-coder · 语言 TypeScript · license Apache-2.0 · updated 2026-09-24
**是什么**：为"更小的 LLM"专门优化的 harness。
**为什么值得看**：本轮最贴合你硬件条件的一条——它整套设计前提就是小模型。如果你想让本地 7B/4B 级模型当好编码助手，这是对口的路线。
**可复用性**：落地/参考 —— Apache-2.0，可试；也能读它"如何迁就小模型"的设计来改自己的 harness。

## 八、未核实 / 待核

- **PawanOsman/OpenCursor、Armur-Ai/vibescan、vibeforge1111/vibeship-scanner**：`gh api` 返回的 license 为 null 或非标准 SPDX。**星数/语言/时间已核实，license 未核实**，引用时勿写具体许可证名。
- **MCPJam/inspector（★2222，TypeScript，NOASSERTION，2026-09-24）**：MCP server 的对话/检查/调试平台。数据已核实，但本轮未找到它与你现有索引的差异点，**暂不列正式条目**，留待下轮。
- 搜索 "npc dialogue llm game"、"visual novel ai agent"（带 pushed 过滤）本轮**返回空**，故视觉小说"NPC 对话"方向本轮无新增（不臆造）。

## 附一、本路去重报告

对每条候选跑 `grep -icF "owner/repo" index.html csdn-social-summary.md csdn-social-summary-v21.md csdn-social-summary-v20.md`，命中即弃：

| 候选 | 命中 | 处置与理由 |
|---|---|---|
| coddy-project/coddy-agent | 6 | **弃**。已在 `index.html`（并注明旧 owner `EvilFreelancer/coddy-agent` 已查过）+ summary v20 有表格条目。 |
| Context-Engine-AI/Context-Engine | 1 | **弃**。已在 `csdn-social-summary.md:205`（403★/MIT/Python）成条。 |
| mtrnix/metronix-memory | 2 | **弃**。已在 `csdn-social-summary.md:138~139` 成条（101★/Apache-2.0）。 |
| godot-mcp（Coding-Solo / beckettlab / nguyenchiencong 三个） | 24 | **弃重复项**，仅取本轮新增的 yurineko73/Godot-MCP-Native；tomyud1/godot-mcp 核实后降为备选。 |
| SillyTavern | 3 | **弃**，已在基线。 |
| text-generation-webui | 2 | **弃**，已在基线。 |
| jan | 10 | **弃**，已在基线。 |
| open-webui | 2 | **弃**，已在基线。 |

**假命中记录**：`godot-mcp-toolkit` 在 `index.html` 有 1 次 `-F` 命中，逐字看上下文是 CSS/文案行（`data-page-node-id`/`可拓展性`），**属假命中**，该仓库实为可收录项（本轮未占用名额，留待下轮）。

## 附二、搜索覆盖表

| 站点 | 关键词 | 命中情况（有效候选 / 原始） |
|---|---|---|
| GitHub API `search/repositories` | `renpy ai OR llm OR agent` | 大量 SEO 垃圾仓（0★）；有效 1（RenPy 相关多为翻译工具） |
| GitHub | `renpy plugin stars:>20` | 4（含 dsh-plugin-tav2、RenPy-AutoScriptPlugin、RenPyChatGPTExample、renpy-encyclopaedia） |
| GitHub | `renpy ai stars:>15 pushed:>2026-06-01` | 2（GameStringer、dsh-plugin-tav2） |
| GitHub | `godot ai plugin stars:>30` | 6 有效（Godot-MCP-Native、tomyud1/godot-mcp、godot-mcp-toolkit、AI4U 等） |
| GitHub | `agent memory server mcp stars:>100` | 15+ 有效（engram、nocturne_memory、okf-agent-memory 等） |
| GitHub | `agent context compression stars:>50` | 10+ 有效（headroom、paritok、sqz、distill） |
| GitHub | `vibe coding security scanner stars:>50` | 3（vibescan、vibeship-scanner、Vibecode-Cleaner） |
| GitHub | `vscode extension ai coding agent stars:>200 pushed:>2026-08-01` | 1（OpenCursor）；另 `vscode extension stars:>1000` 得 SpecStory |
| GitHub | `deepseek harness stars:>10` + `dsh plugin` | 20+ 有效（DSH-X、dsh-vision-router、dsh-desktop、billion-context-dsh 等） |
| GitHub | `llm evaluation harness stars:>300 pushed:>2026-07-01` | 4（Claw-Eval、ClawProBench、llm-space、Hypha） |
| GitHub | `ollama benchmark stars:>100 pushed:>2026-06-01` | 3（ollama-benchmark、little-coder 等） |
| GitHub | `npc dialogue llm game stars:>30` / `visual novel ai agent stars:>20` | **0（空）** —— 该主题本轮无新增 |
| 核实口径 | `gh api repos/{owner}/{repo}` | 正式 28 条 + 备选 2 条（tomyud1/godot-mcp、ooples/token-optimizer-mcp）全部取到真实 stars/license/language/updated_at |

*（本文件为逐段增量写盘，最后更新 2026-09-24）*
