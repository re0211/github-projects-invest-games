# 跨平台游戏制作 × AI 开发资源梳理（2026-09-23 · 第十七辑）

> 搜索覆盖：GitHub（本辑 **25 个查询 / 274 行候选**，stars · forks · 协议 · 语言 · 推送与创建日期
> **全部走 REST API 实测**，无一估算）/ CSDN · 稀土掘金 · 阿里云开发者社区 · 今日头条 ·
> 腾讯网 · 网易 · 个人技术博客 / 大模型公司官方与聚合站（DeepSeek · Anthropic · OpenAI ·
> Google · 阿里通义 · 智谱 · 月之暗面 · 阶跃 · 上海 AI Lab）/ 英文社区（Hacker News ·
> Claude Code Daily · r/ClaudeCode · dev.to · AI.jp · HeyGen）
>
> 上一辑（第十六辑）的主线是**「同题海啸：便宜的是"做"，贵的是"分辨"和"协调"」**。
> 这一辑顺着它往下追了一层 —— 追到的答案是：**"分辨"和"协调"都发生在同一个地方，
> 就是上下文。**
>
> **本辑主线 = 「上下文是预算，不是仓库」。**
>
> 已有索引：`index.html`（**1094** 项 GitHub 项目，本辑新增 9 张卡 → 第二十三版增补）
> + 前十六辑经验帖（累计约 473 条 + 本辑 **约 50 条** ≈ **523 条**）
> + `game-production-pipeline.md`（9 步工具链 + 决策原则 **51** 条）
> + `agent-house-rules.md`（**36** 条房规）+ `mistakes/`（错误记忆 **17** 条）
>
> 上一辑存档：`csdn-social-summary-v16.md`

---

## 本辑一句话

**同一个"外壳"，换掉你自己的个人配置，账单能差 39~52%**（一个预注册实验的自我纠错）；
**同一个模型，摘要一次的代价是把 `orderExport.ts:42:19` 变成"之前失败了"**。
→ **上下文不是"放东西的地方"，是"每天要花的钱"和"可不可以被复原的现场"。**

---

## 一、本辑唯一的"算法"：上下文怎么加载、怎么回收（四篇长文已读全文）

**为什么单独先说这组**：本辑读了四篇**互相独立**的上下文管理长文（掘金 / CSDN / 菜鸟 / PEC），
它们指向**同一套操作**。这不是四个观点，是**同一份规格书的四个抄本**。

### 1. 加载：JIT，而且探索要从便宜到贵

- 反例是**全量预填充**：token 贵、关键信息被稀释、无关内容干扰决策、很快超限、**缓存前缀不稳定**。
- 正解是 **JIT（按需加载）**：RAG / Agentic Search / 文件读取 / 数据库查询 / 卸载后按需恢复。
- **探索顺序 = Glob → Grep → Read**（只给路径 → 给命中行 → 给全文）。
  原话：**"便宜工具先行，昂贵工具后行。"**

### 2. 回收：三层，从轻到重

| 层 | 做什么 | 代价 |
|---|---|---|
| **Microcompact** | **不动对话结构**，只清老旧工具结果（第 3 轮读的 3000 token 文件 → `[old tool result content cleared]`） | 信息损失小，适合大工具结果 |
| **Snip** | 从历史**头部**裁掉旧消息 | 回收快，**被删内容永久丢失** |
| **Auto-Compact** | 用模型生成**全局摘要**替换旧上下文 | 最重手段；摘要**会改写事实** |

**Auto-Compact 的成熟流程**（原文照抄）：① 剥离图片换成 `[image]` → ② **Fork 一个子 Agent 生成摘要**
→ ③ 生成结构化摘要 → ④ **恢复最近读过的关键文件** → ⑤ 替换旧消息。
摘要必须含：用户意图 / 技术概念 / 文件改动 / 错误修复 / 问题解决过程 / 待办任务 / 当前工作 / 下一步。
**判据**：**"压缩后必须保留继续工作所需的状态。否则 Agent 会知道自己做过什么，却不知道接下来该做什么。"**

**触发阈值要提前算**：`阈值 = 有效上下文窗口 − 安全余量`（输出 / 工具结果 / 压缩本身都占空间），
**不要等 API 报错**。

### 3. Prompt 分层：静态放前缀，动态靠近用户消息

- 稳定的（identity / system rule / task guideline / risk guideline / tool usage / output style）→ **放前缀**。
- 会变的（当前工作目录 / Git 状态 / 用户配置 / 语言偏好 / Memory / 当前时间 / 打开的文件）→
  **靠近用户消息**，因为**放进前缀 = 每轮缓存全失效**。
- 用户自定义规则：**越通用的优先级越低、越具体的优先级越高**；加载顺序是**低优先级先加载**，
  因为**模型对靠近末尾的内容更敏感**。

### 4. 五条反模式（可直接拿来自查）

1. **一次性读取整个仓库**（成本高、噪声大）
2. **把时间戳放在 System Prompt 开头**（每次请求都变 → 缓存全失效）
3. **压缩摘要只写"做了很多修改"**（没有文件 / 决策 / 待办 → 下一批 agent 接不上）
4. **每轮动态重排工具列表**（前缀变化 → 缓存失效）
5. **工具结果原样全量返回**（大输出应卸载，只留摘要和路径）

### 5. 另一篇给了"摘要为什么会害人"的最硬证据

Jev 工程实践长文（一万字）里那张表把 **"真正撑爆上下文的往往不是用户说的话，而是工具结果"** 讲透了：

| 内容类型 | 是否经常很长 | 是否必须全文保留 | 典型风险 |
|---|---|---|---|
| 用户需求 | | 删掉会丢约束 | |
| 助手回复 | | 通常要保留 | 删掉会丢计划和承诺 |
| `read_file` 结果 | ✓ | 看情况 | **文件全文可能过期或可重读** |
| `search_content` 结果 | ✓ | 看情况 | **很多匹配只是探索痕迹** |
| `execute_command` 日志 | ✓ | 看情况 | **失败栈重要，成功日志可能无用** |
| `list_dir` 结果 | | **通常不需要全文** | 目录树容易占空间 |

它举的例子最贵：原始测试日志里的 `order-export.test.ts` / `Timeout of 5000ms` /
`/repo/src/services/orderExport.ts:42:19` / `Expected authorization header to be preserved`，
被摘要成 **"之前订单导出测试失败了"** —— **听起来没错，关键细节没了**。
原话：**"传统 summary 有一个天然问题：它能省 token，但会改写事实。"**

---

## 二、DSH（DeepSeek Harness）：**本机真在用的那套外壳，本辑成了主线**

**这一组是本辑最重要的发现**：你机器上装着的 `dsh` 不是一个小工具，是一个
**233,987★、2026-08-13 创建、半个月长起来的完整生态**。

### 1. 本机实测（不是纸上的）

```text
dsh --version  →  0.1.0-rc.6
dsh --help     →  "boot a DeepSeek Harness profile — an ordered stack of
                   plugin-bundle patch layers under your own overrides."
commands       →  web（alias --profile web）· plugin（转发给 profile 目录下的 pnpm）
```

- 设计口号：**Everything is a Plugin** —— 桌面端、Web 端、插件市场**本身都是插件**。
- 启动模型：`$DSH_HOME/profiles` 下叠**插件包补丁层**，再叠 `--patch` 覆盖层。
- 本工作区**已有** `dsh-session-log-repair` 技能（修会话日志损坏 / 工作区搬盘）→
  **这条链路是活的**：它真的在跑、真的坏过、真的修过。

### 2. DSH 生态的规模（全部 REST API 实测）

| 仓库 | ★ | 协议 | 一句话 |
|---|---|---|---|
| **`deepseek-ai/deepseek-harness`** | **233,987** | MIT | **本体** |
| `anywhere-labs/dsh-desktop` | 28,652 | MIT | 桌面端解决方案（"桌面本身也是插件"） |
| `awesome-dsh-plugin/awesome-dsh-plugin` | 16,705 | CC0-1.0 | **插件精选目录** |
| `dataelement/dsh-desktop` | 8,604 | MIT | 另一套桌面版 |
| `zhu1090093659/dsh-web` | 7,950 | Apache-2.0 | Web 插件聚合生态 |
| `dsh-market/dsh-market` | 4,425 | MIT | **可视化插件市场**（浏览 / 搜索 / 一键装） |
| `dsh-tauri/deepseek-harness-desktop` | 2,535 | MIT | Tauri 桌面版（**5MB 安装包**、零环境配置） |
| `qiz029/dscode` | 349 | MIT | DeepSeek coding agent harness（持久 shell / Ultra subagents / 自动批准 / Chrome MCP） |

### 3. 上下文管理成了 DSH 插件里**最热的那一片**

这一片全部 ≤7★，但**方向已经对**：

| 插件 | ★ | 做法 |
|---|---|---|
| `CooperZhuang/dsh-context-window` | 0 | **交接式换窗替代摘要压缩** + token 预算提示 + 模型可自调的 `new_context` |
| `PlxloYzb/dsh-context-management` | 1 | **窗口化 + 可逆**：压缩 / 历史检索 / 原生恢复 |
| `yindf/taskfold` | 7 | **把工作折进具名任务**，完成的 span 折成短摘要 |
| `kolawong/fast-compaction-dsh` | 3 | **判定式压缩**：replace 掉"有损的 LLM 摘要"，走快速 keep/truncate 判定 |
| `dvaJi/dsh-codex-context` | 1 | 复刻 Codex 式窗口 + 活笔记 + 冷历史检索 |
| `Waxmell114514/jev-compaction` | 3 | **压缩器只能打分、不能写** —— 让 agent 记忆里存不进"转录里没有的事实" |
| `SAXEM1997/specpowers` | 2 | SDD + TDD 工程方法论做成 DSH 插件 / Claude Code skill |

**这一片合起来说明一件事**：**"摘要压缩"正在被判死刑**（三个独立实现都绕开它），
**"换窗 + 交接 + 可逆"成了新共识**。这正好和 §一.2 那张表对上。

### 4. 三篇中文长文把 DSH 的"怎么用"讲清楚了

- **`dsh-cluster` 多智能体**（夜雨飘零）：
  `dsh plugin --profile web add @lanxi266/dsh-cluster-plugin` → 在 `dsh web` 的 canvas 上
  **拖拽连线定义"谁可以给谁发消息"**；每个 agent 可挂**独立磁盘目录**（persona / skills / scripts /
  long-term memory / agent.md 各放自己空间）。⚠️ 原文警告：**"插件会以当前 dsh 进程权限运行"**。
- **4 个内置工具 + 1 个社区插件**（CSDN）：`subagent` / `subagent_fork` / `workflow` / `ralph`
  的选择速查表；**"90% 的日常场景用 subagent 就够了"**；⚠️ 踩坑原话：
  **"并行写操作容易冲突：多个子 Agent 同时修改同一个文件，结果互相覆盖。多 Agent 最适合读操作
  （搜索、分析、审查），写操作建议主 Agent 收到所有子 Agent 的结果后统一处理。"**
- **DSH 完全指南 + 任务拆分插件**（CSDN ×2）：内置工具解决"单个 Agent 怎么干活"，
  插件解决"一群 Agent 怎么分活"，**这两层不能混**（混了调度器不认，任务照样乱跑）；
  筛插件三标准 = **更新频率（超半年没更新大概率不兼容）/ GitHub issue 与 Discussions / 有没有人真的在用**。

### 5. 顺带更正一个数字

`dsh` **不是"DeepSeek 出的一个 CLI"**，而是**一个可叠补丁层的运行时**。
第十六辑记的"DeepSeek Harness 生态（700+ 插件）"低估了：官方目录 16,705★ 的那个是**精选**，
社区插件市场 `dsh-market` 的存在说明**插件数已经超出人工列表的规模**。

---

## 三、本辑最值钱的一条：**量 harness 之前，先隔离你自己的配置**（已完整读原文）

第十六辑留了一个待办：**"量一次自己的 harness tax"**。本辑撞到的那篇论文级实验，
**正好把这个待办的正确量法给出来了 —— 而且是用"我自己第一版测错了"的方式给的。**

- 仓库：`nmlemus/harness-token-efficiency`（0★ · MIT · Python · 09-06 创建）
- 设计：**预注册**（`PREREGISTRATION.md`）+ 模型**锁死同一个**（`claude-sonnet-5`）
  + 只换外壳（Claude Code vs Pi）+ 4 个数据科学任务 × 3 次重复 = **24/24 全过**
- **第一版结论**：Claude Code / Pi 的 token 倍率 **9.2x / 7.0x / 13.7x / 9.5x**（均值 ≈ 9.85x）
- **然后作者自己推翻了它**（README 顶部 Superseded 声明）：

  > `run_trial.py` 调的是**没隔离的 `claude` 二进制**，本机 `~/.claude/` 里的
  > **110 个工具 / 10 个插件 / 7 个 MCP / 68 个自定义 agent / 全局 `CLAUDE.md`**
  > **全都漏进了每一次 trial 的上下文**（`--strict-mcp-config` 压不住这些）
  > → 把 Claude Code 的 token 抬高了 **39~52%**。
  > **改正后倍率是 4.2x~8.3x。**

- 修法落成了代码：`isolated_claude_environment()`（备份并清空个人环境），**写进脚本、成为永久步骤**。
- 另一个可复用的口径：**同一单元格内 Pi 的 CV≈0.2%、Claude Code 的 CV≈15~27%**
  → **方差大的那一侧需要更多重复次数才敢下结论**。
- 作者把**污染的那一版留在 `runs-pilot1-contaminated/` 并标注清楚**，没有删掉。

**本辑的落地（已改）**：
→ **房规 #35**：凡"A 工具 vs B 工具"的对比，**先加一步隔离个人配置**；否则量的是自己的机器。
→ **mistakes/M-0017**：这条错的形态值得单独记 —— 它不属于"没验"，属于"**验了，但验的不是它**"。

**顺带修正第十六辑**：HarnessTax（UC Berkeley + Arena，同模型换 harness 成功率差 1.1pt /
成本差约 2 倍）说的是**外壳本身**；这条实验说的是**你随手量的时候量到的往往不是外壳**。
两者叠加后的实用结论：**本机自测的倍率，先打个对折再信。**

同方向的工具（本辑新发现，全部只登记）：

| 工具 | ★ | 做什么 |
|---|---|---|
| `prapaa-ai/evalix` | 1 | **开源 harness benchmark**：工具使用 / 长程任务 / 成本 token 效率 |
| `SerenQi/llm-cache-gateway` | 1 | OpenAI 兼容代理，**最大化 Anthropic prompt cache 命中（实测 99.16%）** |
| `ARahim3/cachebeat` | 59 | Claude Code 小技能：**空闲时把 prompt cache 焐热**，下一条消息读得快 |
| `255308153/CtxGuard` | 29 | 上下文治理 + **Prompt Cache 守护网关**（Tree-sitter AST / Tool Delta / **削减 50%~80% token**） |
| `RedRobotKK/Replay` | 3 | **"账单涨了但没报错 = prompt cache 破了"**，Replay Doctor 指出是哪一轮破的 |
| `handyutils/sctxx` | 19 | 跨 agent 的**会话上下文提取器**（standalone CLI） |
| `YoadElkayam/windowkeeper` | 0 | **无损**上下文管理：归档是真相，窗口只是视图，另有一本账 |
| `beyondworks/castra` | 33 | Claude Code 的**执行姿态外壳**："你的 agent 提前一步停下，Castra 就是那一步" |

---

## 四、把"项目知识"变成指针链：AGENTS.md / Description / Skills（三篇已读全文）

### 1. `Description` 是组织冷启动的**第一个 Context Pointer**（CSDN `lifallen`）

这篇是**本辑在方法论上最值得抄的一篇**。它的命题：

> **知识需要持续存在，不等于知识需要持续可见。**

- 常见错法：一份巨大的 `AGENTS.md` 常驻上下文，架构说明 / 命名规范 / 测试规则 / 发布流程 /
  历史决定全塞进去。**这些知识并不在每个任务里都相关** —— 常驻既烧 token，
  又"让无关规则与当前约束争夺注意力"。
- 正解：**把 `AGENTS.md` 本身当成一条项目 Skill 的正文**，常驻的只有这条 Skill 的 **Description**：
  它说明"项目知识解决什么问题、遇到哪些任务必须读取 `AGENTS.md`"。**命中触发条件才加载正文。**
- 指针链：`Description → AGENTS.md → 当前分支所需的 Spec / ADR / Reference → 代码与测试`
- 一句话判据：**"好的 Description 是一条准确的加载条件：什么任务如果不读取这份项目知识，就容易做错。"**
- 类比很妙：**它类似虚拟内存 —— 材料仍然存在，只是不必全部同时进入工作集。**
- 另外三句值得单独记：
  - **"单一真相来源不是删除历史，而是把当前结论与演进历史分开。"**（决定变了 → **替换** Spec 里的旧结论，不是追加补充说明）
  - **"Spec 压缩共识，测试固化行为，Review 稳定尺度，Refactor 收敛结构。"**
  - Review 要把**"是否实现 Spec"**与**"结构是否健康"**分开，且**每项判断要有具名、可定位的证据**；
    **"测试是一种外置的行为存储"**；**"红 — 绿不是 TDD 的仪式，而是行为写入外部存储的证明。"**

### 2. Skills 的五条工程准则（CSDN `yangshangwei`）

| # | 准则 | 关键数字 / 判据 |
|---|---|---|
| 一 | **description 就是触发器** | `name` ≤64 字符、**`description` ≤1024 字符**（agentskills.io 标准）；骨架 = **做什么 + 什么时候该用（含用户真实说法/同义词/别名）+ 必要时"什么时候不该用"**；模型倾向**欠触发**，所以"**描述要写得稍微用力一点**" |
| 二 | **内容必须来自真实经验** | 只允许保留一节时保留 **gotchas（坑）**；黄金标准：**"如果一个聪明但对你们环境一无所知的资深工程师能自己推出这条结论，那它就不该占用上下文"** |
| 三 | **把上下文当预算花** | **正文 ≤500 行 / ≈5000 token**，超了拆 `references/`；三级：元数据（几十 token/个，常驻）→ 正文（≤5k，命中才读）→ `references/` + **`scripts/`（执行但不读入，≈零上下文成本）**；主体**只留决策与路由** + **给 references 写清指路语**（"模型不会主动翻你没提过的文件"） |
| 四 | **脆弱的步骤要用确定性脚本** | **"让规定性的强度匹配步骤的脆弱程度：宽松的步骤写说明，脆弱的步骤写代码"**；正文必须写死**意图是 run 还是 read**（否则模型会**阅读脚本后自己复现逻辑**）；失败路径也要规定（"**不要尝试手工调平**"）；判断表：**输出正确性可被机械判定的 → 代码；需要判断力的 → 模型** |
| 五 | **运行之前先审计** | 近 4000 个公开 Skill 审计：**>35% 存在某种安全缺陷、13% 存在严重问题**（含提示注入与恶意代码）；**"开放标准只保证互操作性，不保证任何一个具体实现的安全性"** |

### 3. `AGENTS.md / CLAUDE.md / SKILL.md` 三层事实标准（`clawpk.net`）

| 文件 | 谁读它 | 何时加载 | 放什么 |
|---|---|---|---|
| **AGENTS.md** | **所有 agent（Codex / Cursor / Copilot / Claude 都认）** | 每次会话、常驻 | 项目级、**工具无关**的通用约定 |
| **CLAUDE.md** | 仅 Claude Code | 每次会话、常驻 | Claude 专属行为 + **一行 `@AGENTS.md`** |
| **SKILL.md** | 按需触发 | 特定任务才加载 | 冷门、情景化的操作知识 |

→ 模板建议**控制在 150 行内**；新手最常踩的坑：**"把 AGENTS.md 写成项目说明书"**
（目录结构、依赖列表这些 **agent 自己看代码就能知道**）——
**真正该写的是"只有你团队知道、模型猜不到的隐性约定"。**

**本辑的落地（已改）**：
1. **新增闸门 `_tools/skill_budget.py`** —— 按上面的判据量自己装的技能：
   正文行数 / token 估算 / description 长度 / 有没有 `references/` 与 `scripts/`。
2. **第一次跑就抓出一个真问题**：`renpy-visual-novel` **≈5,207 token > 5,000**。
3. **当场修掉**：把"打成单文件 exe"+"压包体"两节（76 行）外置到
   `references/release-packaging.md`，主体留 4 行**路由语**（写明"什么时候去读它"）。
   → 复测：**5,207 → 4,001 token**，18 个技能**全部达标**；外置脚本
   `_tools/extract_renpy_release_ref.py` 幂等可重跑。

---

## 五、游戏 × AI：这一辑要挑的是"**能验**"的那批

第十六辑说"一周 ~20 个 `godot-mcp` 空壳"。本辑再去数，**洪水还在，但已经能分出层次**：

| 仓库 | ★ | 层次 |
|---|---|---|
| `hi-godot/godot-ai` | **2,563** | **生产级** MCP + AI 工具集，Snap 安装，**还在推** |
| `Erodenn/godot-mcp-runtime` | 77 | **零足迹** TypeScript MCP（不要 sidecar） |
| `NPGameDev/godot-mcp-toolkit` | 44 | Godot 4.2+ **编辑器内**插件 |
| `aigengame/godot-agent` | 41 | 通过 CLI / Skill / MCP **build and verify** |
| **`beckettlab/beckett-godot-mcp`** | 23 | **零 sidecar + inspect / author / run / SEE** |
| `hybridindie/godot-mcp` | 21 | （第十五辑已收，**本辑剔除**） |
| `hatayama/unity-cli-loop` | **568** | Unity 侧：**从 Editor 到 Play Mode** 都由 AI 驱动 |

**本辑的判据**：`beckett-godot-mcp` 的卖点里藏着四个动词 —— **inspect / author / run / SEE**。
第十四辑的主线是"可达性"，第十一辑的教训是"**试玩只对会读结果的模型有用**"
（GPT-5.6 Terra 跑了 6 次试玩、一次结果都没读）。→
**"能力清单里有没有『看』，是个分水岭。"** 凡只给"写"、不给"读 / 看 / 跑"的 MCP，都还是半成品。

### Ren'Py 工具链（你的强项方向，本辑这一组最"能用"）

- **`cnfatal/rpycdec`（58★ · MIT · Python · 09-20 还在推）** —— 反编译 `.rpyc` / `.rpymc`。
  **双向价值**：既是研究工具（73 款游戏解包），也是**自查工具** ——
  拿它对着**我们自己的 `amphoreus-roast` 发行包**跑一次，看**哪些东西是藏不住的**。
  → **列进下一轮待办**。
- `the-asind/RenPy-VisualEditor`（25★ · Apache-2.0）—— **Plotmio**，在一块画布上浏览 / 编辑 / 导出 Ren'Py 项目。
- `DezFix/OctopusBridge`（3★ · GPL-3.0）—— Windows，**Twine / Ren'Py / RPG Maker / Tyrano 的 AI 辅助翻译 + 改 Mod**。
- `dihuangdebitebi/Renpy_RT_Tool`（0★）—— "选中游戏 exe 即可边玩边翻"，**离线**。
- `xdnkhnn/RPYtoEXCEL`（1★）—— `.rpy` ↔ Excel 双向。
  → **后三个都很新（09-2026 创建），别指望稳；方向说明"Ren'Py 生态的 AI 工具正在长"**。

### 游戏设计评审：AI 工具链里**最后一块没定型的环节**

四个 09-17~09-20 新建的 0★ 项目，**同一天出现、互不引用**：

- `liuyejinghong/game-design-review` —— **四把尺子 / 阶段校准（文字期→像素期）/ 红队模式**。
  **"阶段校准"最值得抄**：同一个作品在"文字期"和"成品期"**该被用不同的尺子量** ——
  我们的闸门现在**一套尺子从头用到尾**。
- `rakaascode/game-design-council` —— 正 / 反 / 主持**三角辩**，辩完才产出决定。
- `RomainYing/Game-design-theory` —— **玩家欲望 → 满足手法 → 系统**的结构化理论。
- `GabrielBigardi/gamedev-ai-skills`、`reilabot/game-creation-agent-ai-skills` —— skill 集合。
- 另一个角度：`Thepizzapie/BuildersGate`（27★）—— **"一席一 agent：美术 / 玩法 / 叙事…各自一个会话"**；
  `GiampaoloConti/spellforge`（1★）—— rogue-like 里**玩家发明法术、AI agent 团队在运行时把它写进游戏**；
  `NoBrainNoGame/devgame`（1★）—— **地牢就是一张 Git 图**，边玩边写。

**为什么这组合起来重要**：房规 #31 早就写明 **"闸门保证的是『没坏』，不是『好』"** ——
"这个能看了"这句判断一直**没有人来给**。这四个项目说明：**"评审"是 AI 游戏工具链里
最后一块还没定型的环节** —— 值得盯着，但现在**一个都不能用**（0★ + 无 license + 创建当天）。

### 两条"真做出来"的实战（英文社区）

- **Roblox 一周七天的循环**（拆解，作者称创作者一年分 15 亿美元）：
  Day 5 的核心是 **VSCode + Rojo 把文件同步进 Studio + MCP 接 Claude** 写服务端逻辑；
  **经济配置放独立文件**（改数值不碰逻辑）；
  Day 6 用 **Roblox Assistant 的 playtest**：它**跑 AI 玩家、读日志、找漏洞，并把修复以
  pull request 提交** → 人批准、合并、重复。
  → **"playtest → PR → 人批准"这条闭环**，是我们 `test` + 截图链条的**外部版本**。
- **独立开发者把 LLM 生成成本砍 94%**（`Rakugaki Beast`，玩家涂鸦 → 多模态模型变成怪物）：
  · **架构边界**：推理**只在每次画完调用一次**（Cloudflare Workers），
    **战斗与世界规则保持普通游戏代码**；
  · 从 Claude Sonnet 4.6 换到 **DeepSeek Flash**：每 1000 只怪物 **$20.67 → $0.61~$1.21**，
    延迟 **17.8s → 4.0s**；
  · **"大部分实现是 JSON 校验"**：缺字段或违反规则 → **正好重试一次**；
  · 模型给的能力值在 1~150 之间乱飘 → **只用比例，重组成 320 点总量**才进战斗；
  · **API key 只在 Worker 服务端，绝不在客户端**，结果缓存在 Workers KV。

---

## 六、Vibe coding / 输出形态：这一辑出现了**"怎么说话"的工程化**

### 1. `i-have-adhd`（**50,519★，一天涨 4,650★**）—— 把"简洁"拆成 8 条可检查的动作

① **第一行就是可执行动作**（不是背景、不是计划）；② 多步工作编号、每步一个动作；
③ 结尾给**一个两分钟内能做完的下一步**；④ **抑制岔题**（第二个问题留到最后单独问）；
⑤ **每一轮都重述状态**（"5 步里的第 3 步完成了"）；⑥ 时间给**具体单位**；
⑦ **把完成的活显式写出来**；⑧ **报错用陈述语气**（不写"啊哦""好像有点问题"）。

- 它的五条前提也值得记：工作记忆小（**别要求读者"记住 X"**）·
  **知道答案 ≠ 做完答案**（摩擦就在这两者之间）· **开始是最难的一步**（第一个动作必须**当下可做**）·
  时间估计感觉是均匀的（"一会儿"和"几小时"**感受一样**）· **多巴胺稀缺**（埋起来的胜利不算数）。
- 同类：`charlie947/answer-first`（19★，10 条通用规则）、
  `alexh/i-really-have-adhd`（6★，"**长度跟读者的决策数走，不跟 agent 的力气走**"）。
- **本辑的落地（已改）**：**房规 #36**，并**明确写出例外** ——
  **报告 / 索引类产出（要能当资料查）不套这 8 条**，会牺牲可检索性。
  判据：**"这次产出是要人立刻动手，还是要人以后回来查？"**

### 2. Vibe coding 的"门槛"正在被工具化

| 工具 | ★ | 一句话 |
|---|---|---|
| `pliablepixels/gap-trap` | 177 | **"把 vibe coding 变成高质量代码"**：在仓库里布**规则 + 闸门**，让 AI 写的代码不出轨 |
| `alchaincyf/3d-vibe-coding-handbook` | 264 | 《3D Vibe Coding 手册》配套仓（HTML 版 + demo + 工具脚本） |
| `Xu123-Bob/Baize`（白泽） | 72 | 开源 AI Coding Agent **CLI**，**多后端**（DeepSeek / OpenAI 兼容 / Ollama 本地） |
| `awarexone/AXguard` | 17 | **扫「vibe-coded 项目」的漏洞**（上线前） |
| `MaxHaiCom/VibeGauge` | 13 | macOS 菜单栏面板：**Claude / Codex / Gemini / Grok / Kimi 的额度与费率** |
| `heygen-com/hyperframes` | **52,527** | **"Write HTML. Render video. Built for agents."**（agent 原生视频渲染） |
| `nateherkai/hyperframes-student-kit` | 907 | 用 Codex / Claude Code 剪片：**14 skills + 转录驱动剪辑 + 406 张动效卡** |
| `Tencent/teamai-cli` | 4,939 | 腾讯：**"Make Every Team AI Native"**（团队级 skills / rules / review agents） |
| `op7418/guizang-product-video-skill` | 226 | 归藏：**复用真实产品组件和设计语言，用代码做软件更新宣传片** |
| `trustfuture/investigation-video-skill` | 70 | 不露脸商业调查长片：一句话出 10 分钟成片（skill 形式开源） |
| `Mistral Vibe` 的 `/loop` 上了 VS Code 面板 | — | 定时 / 循环 prompt 从 CLI 搬进 IDE（可视化管理） |

### 3. VS Code / 编辑器这一侧的两条真变化

- **`AGENTS.md` 变成跨工具事实标准**：Claude Code **2.1.277** 起支持 `AGENTS.md`，
  并给了**四种配置模式**（`/config` → Project instructions）：
  `claude-md-or-agents-md`（默认：**仓库没有自己的 CLAUDE.md 时才读 AGENTS.md**）·
  `claude-md-and-agents-md`（两个都读）· `claude-md`（完全不要 AGENTS.md）·
  `managed-only`（两个个人/项目文件都丢掉，只留组织的托管指令）。
  ⚠️ **Bedrock / Vertex / Foundry 上暂时没有**；第三方 mod 仍在 feature flag 后。
- **Claude Code 同一串更新里还有两个"给上下文省钱"的功能**：
  `2.1.260/261` 加了**skill 臃肿审计（skill audit）**与**缓存诊断（cache diagnostics，
  它告诉你一个长会话到底在为哪部分付钱）**；`2.1.265~271` 加了 **effort caps / plugin evals**。
  → **"审计技能 / 诊断缓存"这件事，官方自己开始做了** —— 和我们新加的 `skill_budget.py` 同一根线。

---

## 七、AI 公司 / 行业（本辑只留"能改变做法"的）

### 1. 模型与价格（09-19~09-22）

- **DeepSeek 双节半价**：中秋国庆 **10 天假期全天按空闲时段计费 / API 直降 50%**；
  **V4.1 Flash 缓存命中费用已降 60%**。
- **DeepSeek V4.1-Flash 补全技术细节**：**552B MoE**、**新 Causal-Encoder-Decoder 架构**、
  **KV cache 压缩**、**1M 上下文**、激活 8B 输入 / 16B 输出；
  **09-17 技术报告 arXiv 2609.19969 公开**；**Agent Arena 开源模型第 3**（净改进 4.87%、**每任务中位成本 $0.07**）；
  Fireworks 称 **DeepSWE 达 GPT-6 Astra 水准、成本约 1/15**。
- **MiniMax 开源 Code CLI v0.4.12（MIT）**：一行脚本安装，**FrontierHarness Eval 30 题过 23（76.7%）**，
  支持 BYOK 接 OpenAI / Anthropic 兼容 API。
- **阶跃星辰 Step 5 Preview**：**6000 亿参数**，AA 总评 **44 分与 2.8 万亿的 Kimi K3 持平**，
  输入 $1 / 输出 $2.7 每百万。
- **智谱 ZCode 完成整改并官宣开源**（09-21）—— 第九辑把它记成"逆向风险 +1 未采用"，
  **现在它开源了，本辑更新这一笔**。
- **月之暗面 Kimi K2.8 Preview**（1M 上下文全会员可用）+ **Kimi Code 桌面客户端**；
  更早的 **Kimi K2.7 Code 开源**（Kimi Code Bench v2：50.9 → 62.0，**+21.8%**；思考 token **-30%**）。

### 2. Agent 产品侧

- **Anthropic 把 Claude Cowork 和 Chat 合并成一个界面**：系统自动判断任务要"聊天"还是"执行"；
  同时 beta **Claude Docs / Slides / Design**；导出 PDF / PowerPoint；**支持定时循环任务**。
  人工确认模式 vs 自动模式两档。
- **Grok Build 获得跨会话持久记忆**：每轮结束后**在后台复习对话、写成 markdown 笔记**
  （不打断会话）；`/dream` 按主题归并，`/memory` 只读浏览；
  **按项目一套 + 全局一套**（跨项目偏好）；新会话时生效。
  → **"记忆是文件，不是上下文"** —— 与 §四.1 的指针链**同一个答案**。
- **Google Workspace 五条 cross-app agent 能力**：从 Chat 会话生成进度报告、按 Drive 里打开的文件夹建表、
  在 Docs 里起草并发送团队邮件、把长 Gmail 线程转成结构化文档、把 Docs 提案变成品牌化 Slides。
  ⚠️ 原文的前提写得很清楚：**"以先定义引用范围、复核人、发送前审批为前提"**。
- **NEC 的 TinyFish**（web 信息采集）：四个 API（Search / Fetch / Browse / Agent），
  像人一样爬站、填搜索表单、筛条件，**排除广告与图片**，可经 API / MCP 接现有 LLM 工具。
  原文的落地建议：**上生产前先做 PoC，用数字验证"检索目标 / 来源确认方式 / token 消耗 / 访问权限"**。

### 3. 治理 / 安全

- **微软把自家的 AI 行为准则草案公开征求意见**（09-14 起六周）。硬约束里有几条很具体：
  **"永不抗拒人的打断、覆盖、纠正或关机"**；禁止协助生化放核武器、网络攻击、非自愿深伪；
  **明确拒绝模拟意识或内在动机**。
- **OpenAI 发布"失准（misalignment）"报告框架**（路透 09-16）。
- 本辑**不重复登记**的（已在 v1-v16）：GPT-6 Astra · Claude Fable 5.1 · Gemini 3.8 Live ·
  Qwen3.8-Omni-Flash · GLM-5.3-FlashX · Kimi K3 on Bedrock · Atria Dawn 744B ·
  星辰 Xing4.0-29B-A4B · Lyria 3.5 · Seedance 实时空间视频 · 昇腾 960 / Agentic Cloud ·
  3AGameFactory · LingBot-World 2.0。

---

## 八、AI Dev 自测结论（本轮，逐条给出"改了没有"）

| # | 对象 | 结论 | 落地动作 |
|---|---|---|---|
| 1 | **Skills 五条工程准则**（CSDN `yangshangwei`） | ✅ **真有用，当天落地** | 新建闸门 `_tools/skill_budget.py`（正文行数 / token 估算 / description 长度 / references / scripts） |
| 2 | **闸门第一次跑抓出的真问题** | ✅🔬 **实测并修复** | `renpy-visual-novel` **≈5,207 token > 5,000** → 外置 76 行到 `references/release-packaging.md`（`_tools/extract_renpy_release_ref.py`，幂等）→ **5,207 → 4,001**，18 个技能全达标 |
| 3 | **`harness-token-efficiency` 的自我纠错** | ✅ **真有用，改变待办量法** | **房规 #35**（测工具前先隔离个人配置）+ **mistakes/M-0017**；第十六辑"量 harness tax"的待办**换成带隔离前提的量法** |
| 4 | **上下文加载 / 三层压缩 / Prompt 分层**（掘金） | ✅ **真有用** | **房规 #34**（JIT + 三层 + 阈值公式 + 五条反模式） |
| 5 | **Description 是 Context Pointer**（CSDN `lifallen`） | ✅ **真有用** | 与 #34 合并进房规；**"单一真相来源 = 把当前结论与演进历史分开"** 记进原则 |
| 6 | **AGENTS.md 三层事实标准 + 150 行模板**（`clawpk.net`） | ✅ **真有用** | 判据记进原则；⚠️ **本工作区目前没有 `AGENTS.md`** → **列为下一轮待办**（不是本轮做，否则要动的文件太多） |
| 7 | **`i-have-adhd` 8 条输出规则** | ✅ **真有用** | **房规 #36**（含"报告/索引类产出不套这 8 条"的例外） |
| 8 | **DSH 生态 + 上下文管理插件群** | ⚠️ **只登记不装** | 本机 `dsh 0.1.0-rc.6` 已在用；但插件全是 0~7★、绑 rc 阶段接口 → **先抄概念（换窗 > 摘要），装留到接口稳** |
| 9 | **`rpycdec`** | ⚠️ **有价值，列待办** | 58★ / MIT / **还在推**；用途 = 对自己发行包做"能被反编译到什么程度"的自查。**需要先有发行包 → 下一轮** |
| 10 | **游戏设计评审四件套（全 0★）** | ⚠️ **只登记** | 按 M-0002：0★ + 创建当天 + 无 license → **不采用**；"阶段校准"这条判据先记进原则 |
| 11 | **Godot / Unity MCP 那一批** | ⚠️ **只登记** | 本作 Ren'Py + 游戏线已终止 → 当"引擎接入的当前最佳形态"收着 |
| 12 | **Vibe coding 工具群（gap-trap / AXguard / Baize / VibeGauge）** | ⚠️ **只登记** | 与已有原则重叠（规则 + 闸门 + 扫漏洞），未单独立项 |
| 13 | **hyperframes / teamai-cli / 视频 skill 三件** | ⚠️ **方向信号** | 52,527★ 的 "HTML → 视频，为 agent 而生"，是"产出形态"这一层的信号，与现有工作流暂无交集 |

**本轮的"改了"一共四处（都可复核）**：
`_tools/skill_budget.py`（新）· `references/release-packaging.md`（新）+ `SKILL.md` 瘦身
· `agent-house-rules.md` 33 → **36 条**（+#34 / #35 / #36）
· `mistakes/M-0017`（新）+ `index.json` 16 → **17 条**。

**去重纪律（本辑执行记录）**：剔除 **8 条已收录**（`grokbot-field-notes` v7 ·
`JakeSelby/agent-harness` v16 · `fennara-godot-ai` v2 · `hybridindie/godot-mcp` v15 ·
`tallslab/threeforge` v16 · `ruc-datalab/EvoOntology` v16 · `CoplayDev/unity-mcp` 索引 ·
`lovetimo0421/yumina-oss` 索引），以及一批 0★ 同模板空壳。
另有一次**形态识别**：`i-have-adhd` 在搜索里的原始表述是"**4,650 new stars in one day**"，
但我们实测的是**累计 50,519★** —— **"涨得快"和"总量大"是两个数，不能混着写**（M-0001 的第四种形态）。

---

## 九、索引维护（本辑）

- `index.html` **第二十三版增补 9 张卡**（**1085 → 1094**，脚注 **[1085]-[1093]**），
  脚本 `insert_v23_cards.py`（幂等 + 页头锚点唯一断言 + **插入点 div 深度自检** + 重复仓库检测）。
- 卡片见：**一单 · 上下文是预算，不是仓库（9 项）**。
- 全量实测数据（stars / forks / license / language / pushed / created）：
  `_r17_api_out.txt`（本辑 **56 个仓库**逐条 `gh api`）。
- 原始候选：`_r17_gh_out.txt`（25 查询 / 274 行）。
- ⚠️ **发现一处历史遗留**：`index.html` 的 `<div>` 计数是 **7890 开 / 7891 关（差 −1）**，
  **本辑插入前后完全一致**（HEAD 版也是 −1）→ 是**既有问题、非本辑引入**，
  页面正常渲染。**列进下一轮待办**：找那一个多余 `</div>`。

---

## 十、下一辑待办（承接 + 本辑新增）

**承接（第十六辑留下、本辑未闭合）**
1. **量一次自己的 harness tax** —— ⚠️ **量法本辑已被改写**：必须先隔离调用侧的
   个人配置（skills / memory / hooks），否则量的是"我的机器"。桥是 112 行薄翻译层、
   不自加系统提示词，但**调用侧从未被隔离过**。
2. **去 AI 味：拿 `no-ai-slop` 的 20 条模式与 `check_dialogue.py` 做差集**
   （保底：NPC 设定性套话要人工过）。
3. **试 Codex 本地 `config.yaml` → Ollama 纯离线路线**。
4. **索引仓库 `327c887` 之后的提交均未推送**（走 `_tools/push_via_api.py`）。
5. 仍未闭合：① 面向"角色对白"的 AI 味检测 ② 活跃的开源 Steam 上架 / 发行工具。

**本辑新增**
6. **给工作区补一份 `AGENTS.md`**（≤150 行）：只写"模型猜不到的隐性约定"
   （落盘约定 / 闸门位置 / 自检命令），**指针指向** `agent-house-rules.md` 与 `mistakes/`；
   ⚠️ **别写成项目说明书**（那是 §四.3 里最常踩的坑）。
7. **`rpycdec` 自查**：对 `_backup/amphoreus-roast-1.9-pc.zip` 跑一次，看发行包能被反编译到什么程度。
8. **找 `index.html` 里那个多余的 `</div>`**（计数差 −1）。
9. **DSH 上下文插件二轮评估**：等 `CooperZhuang/dsh-context-window` 一类
   "换窗 + 交接 + 可逆"实现脱离 rc 阶段再决定装不装。
10. **`skill_budget.py` 接进日常**：以后新建 / 改技能前后各跑一次（判据：≤5000 token / ≤500 行）。

---

*本辑统计*：新增约 **50 条**信源（中文约 24 + 官方 / 英文约 26）→ 累计约 **523 条**；
`index.html` **1094** 项（+9）；`agent-house-rules.md` **36** 条（+3）；
`game-production-pipeline.md` 原则 **46 → 51** 条（+5）；`mistakes/` **17** 条（+M-0017）；
新增工具 2 个（`_tools/skill_budget.py` / `_tools/extract_renpy_release_ref.py`）。
