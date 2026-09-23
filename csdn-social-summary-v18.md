# 跨平台游戏制作 × AI 开发资源梳理（2026-09-23 · 第十八辑）

> 搜索覆盖：GitHub（本辑 **15 个查询 / 147 行候选**，stars · 协议 · 推送与创建日期
> **全部走 REST API 实测**）/ CSDN · 稀土掘金 · 博客园 · 今日头条 · 搜狐 · 腾讯研究院 ·
> 大模型公司官方与聚合站（OpenAI · Anthropic · xAI · 小米 · 腾讯混元 · Google Research ·
> Cisco Talos · GitHub）/ 英文社区（dev.to · Minitap · AIToolsRecap · MindPattern ·
> worldprogramming · VS Code Insiders 更新日志 · deepseek1024 插件站）
>
> 上一辑（第十七辑）的主线是**「上下文是预算，不是仓库」**。
> 这一辑顺着它往下追 —— 预算花完之后会发生什么：**账单寄到了。**
>
> **本辑主线 = 「账到期」。** 三笔账在同一个星期到期：
> vibe coding 的**维护账**（第三个月）、摘要压缩的**失真账**（"只打分不写"的逐字压缩阵营成型）、
> 模型发布的**口径账**（有人拿 20 个真实已合并 commit 重放，榜单上的 91.2% 和你读到的不是一回事）。
>
> 已有索引：`index.html`（**1094** 项 GitHub 项目，本辑新增 10 张卡 → 第二十四版增补）
> + 前十七辑经验帖（累计约 523 条 + 本辑 **约 44 条** ≈ **567 条**）
> + `game-production-pipeline.md`（9 步工具链 + 决策原则 **54** 条）
> + `agent-house-rules.md`（**39** 条房规）+ `mistakes/`（错误记忆 **18** 条）
>
> 上一辑存档：`csdn-social-summary-v17.md`

---

## 本辑一句话

**摘要压缩省下来的 token，是用"事实被改写"付的账**；
**vibe coding 省下来的第一周，是用"第三个月"付的账**；
**榜单上省下来的那 34 个实例，是用"你说不清自己跑了几分"付的账。**

---

## 一、第一笔账：vibe coding 的维护账，第三个月到期

**为什么先说这笔**：前十七辑大多是"AI 把做东西变便宜了"。这一周终于有人系统地写了
**便宜之后的那部分** —— 而且中文、英文两边是同一周独立发出来的。

### 1. "Month 3 Crisis"（dev.to / tamiz.pro，2026-09-17）

开发者 Tamizuddin 的从业者自述（**自述不是研究**，这点原文自己标了），把 vibe coding 的
技术债拆成四阶段：

| 阶段 | 时间 | 表现 |
|---|---|---|
| 蜜月期 | 0–2 周 | 功能飞速上线，Demo 惊艳，"十倍工程师"错觉 |
| 膨胀期 | 2–4 周 | 同一功能被重复实现，命名各搞一套，模块划分混乱 |
| 撞墙期 | 1–3 月 | **改一处炸三处**；AI 修一个引入两个；复用率趋近 0 |
| 停滞期 | 3–6 月 | 团队不再理解自己的系统 |

三条具体机制（都带代码示例）：
- **Frankenstein 效应**：助手为了让新代码编译，**悄悄改动共享工具函数或类型签名**，
  几个月后别人动那个工具才炸 —— 和第十一辑"扎克鸡 3D 模型物理一开就散架"同一类：
  **渲染/编译看不出来，跑起来才炸。**
- **依赖膨胀**：模型偏爱引库而不是写 20 行标准实现 → 每个 prompt 都往 package.json / requirements.txt 加包。
- **六边形架构被绕过**：一个 AI 写的 delete 路由直接 `import database.js` 发裸 SQL，
  绕过 userService 的 repository 层。**测试全过，但用户数据有了两条到达路径。**

他的建议（值得抄的四条）：模型产出当**草稿不当交付物** / 违反架构边界的代码**直接拒收** /
测试写**边界用例而不是刷覆盖率** / 把"什么时候该用 AI"写成团队规范。

> 对我们的价值：**第 3–6 月停滞期正是"闸门"要防的东西。** 我们已有 check_* 系列闸门，
> 但**没有一条检查"架构边界被绕过"** —— 下一轮可补。

### 2. 安全账：5,000 个 vibe coded 应用几乎没有认证（Minitap 综述，2026-09）

引 RedAccess 的 Dor Zvi 团队：对 Lovable / Replit / Base44 / Netlify 上**数千个** vibe coded
Web 应用扫描，**5,000+ 个没有任何安全或认证**，拿到 URL 就能进；其中**约 40% 暴露敏感数据**
（医疗、财务、公司战略文档）。Palo Alto 云安全报告补充：**99% 的受访组织在用 GenAI 辅助 vibe coding，
同年 99% 遭遇过针对 AI 应用/服务的攻击。**

四类复发风险（**每次都以同一副"能跑"的样子出现**，所以过不了"跑一遍看看"这道人工关）：

| 风险 | 长什么样 | 为什么漏 |
|---|---|---|
| 硬编码密钥 | API key / 数据库口令直接写在代码里 | 跑得通，是最快的能跑方案 |
| 授权检查缺失 | 页面显示用户数据但从不校验请求归属 | 改 URL 就能看别人的，界面不报错 |
| 输入未校验 | 用户输入直达 SQL / 页面 | agent 优化目标是"测试通过"，不是"挡注入" |
| 依赖风险 | 按名字 import，不核实是不是真库 | 这正是 slopsquatting 的入口（第六辑已记） |

**根因判定（原文）**：这是**规格缺口**，不是模型缺陷 —— *工具只造你让造的东西，
而安全需求几乎从不出现在指令里。*

合并前六条检查：扫硬编码密钥 → **逐个核实依赖真的存在** → 校验授权 → 校验输入 →
查 secret 管理 → 跑一遍**安全向**测试套件（而不是只跑功能测试）。

### 3. 中文侧同题：Vibe Coding 90 天猝死四阶段（黑马程序员深圳，09-18）

与 Month 3 Crisis 几乎同一张表，另给两个数字：大中型企业 AI 采纳率 **90.9%**、
企业 AI Agent 采纳率两年 **17.3% → 40.3%**。
⚠️ 来自培训机构招生页，**数字无一手出处，只取阶段描述不引数字**。

### 4. 环境 / 需求 / 上下文三件事（mhpn 转载，无署名无日期）

优先级**严格排序**：**先环境干净、再需求明确、最后上下文可控**（顺序错一点都不行）：
- 环境不干净 → 它看不到编译报错和运行日志，"自己改到能跑"只能瞎猜；
- 需求不明确 → 大而全、七成是垃圾代码；
- 上下文不可控 → 对话长了记不清前提，"你问东它答西"。

⚠️ 无署名转载站（SEO 水文嫌疑），**只收方法不收数字**。

---

## 二、第二笔账：摘要压缩的失真账 —— "只打分，不写"

**本辑技术上最新的一块。** 第十七辑记过"上下文管理是 DSH 生态最热插件类别，7 个里
3 个明确绕开摘要压缩"。这一周这 3 个长成**一整个可安装的阵营**，而且有了统一原理。

### 1. 原理：压缩器只能打分，不能写字

`Waxmell114514/jev-compaction`（MIT，3★，09-19 创建）的 README 一句话就是这个阵营的纲领：

> **A context compactor that can only score, never write —
> so an agent's memory can't hold a fact the transcript never contained.**
> （一个只能打分、永远不能写字的上下文压缩器 —— 这样 agent 的记忆里就不可能有
> 原始记录中没有的事实。）

**为什么比"用 LLM 生成摘要"强**：摘要是**生成**出来的，生成就会改写。
第十七辑那句"摘要会把 `orderExport.ts:42:19` 变成'之前失败了'"就是这个机制。
逐字压缩只做**选择**：打分 → 低分挪出去 → 保留下来的每一行**逐字节原样**。

实测数字（作者自测 demo run）：一段 `npm install` 输出 **749 → 391 token（−48%）**，
保留行逐字节原样，**append-only 前缀从不失效 → prompt cache 不破**；
整趟打分成本 **$0.000031**；按 shadow log 重放，阈值 0.10 省 1,092 token 且
**没漏掉任何 agent 后来回来找过的东西**。

⚠️ 3 星、**作者自测**。价值在**原理**（可自检的那种），不在成熟度。

### 2. 同一阵营另外四个（均 09-19 ~ 09-23 创建）

| 仓库 | ★ | 协议 | 说什么 |
|---|---|---|---|
| `kolawong/fast-compaction-dsh` | 3 | other | **Verdict-based**：用判定替换有损 LLM 摘要，专给 DSH |
| `hoshinodis/opencode-context-pruner` | 2 | MIT | 给 OpenCode 做**连续逐字剪枝**，TypeSafe Jev 驱动；fast-jev-compaction 的移植 |
| `satiricalguru/Fast-Jev-Agents` | 2 | MIT | 同时支持 Claude / Codex / Antigravity / Gemini 的逐字压缩 |
| `hraness/gobstopper` | 5 | other | **自动**上下文压缩，支持 Codex 与 Claude Code 会话 |

### 3. 对面一派：交接文档（handoff）阵营

与"压缩"并列的是**不压缩，而是换会话**：

- `ccompactor/ccompactor`（**21★ / MIT / TypeScript / npm**）——
  **把任意 coding agent 的会话（Claude Code / Codex / Pi）提取成紧凑、可验证、带出处的交接件**，
  别的 agent 能直接接着干：`ccompactor list` / `find "auth migration"` /
  `extract claude:last` / `handoff claude:last --to codex --run`。是 `handyutils/sctxx` 的 TS 版。
- `n0an/handoff-skill`（MIT）：**让会话结束在一个人能控制的 step 文件上，而不是结束在自动压缩上。**
- `kingju1c3/continuity`（MIT）：持久记忆 + **压缩前自动**做会话交接。
- `suanyi001/handoff` / `tianchengc/handoff`（MIT）：session JSONL + 当前 git worktree → 下一会话简报。
- `Avinash-Amudala/weftgate`（Apache-2.0）：本地记忆 + 压缩上下文 + 交接三件套。

### 4. 中文侧把这条线讲成了可执行规则（本辑最该抄的一段）

**worldprogramming 转述的中文社区帖**（原作者每天 vibe coding 7–8 小时）+ **掘金同题**，
操作高度一致，比第十七辑那四篇更具体：

- **One-shot 原则不是信任问题，是算术**：生成错了**别就地打补丁** ——
  改写 prompt、回滚（Claude Code 里两下 Esc / git revert）**从干净状态重来**。
  每一轮"错了→你纠正→它道歉→它改"都往上下文里堆噪声，而**十轮小修小补的代价，
  会在两小时后以"模型开始自相矛盾"的形式一次性结算**。
- **计划要落成文件，不要留在对话里**：先让 A 写计划文档 → **另一个 agent 审这份文档** →
  **新会话**照着实现。同会话里"计划的 token 在实现时已经用掉了"，
  模型只能从**自己压缩过的内部表示**里重建意图；写成文件后，计划是**仓库里的一个事实**。
- **50% 交接规则**（最具体）：上下文到**约 50%** 就生成交接文档、开新会话。
  不用模板，原话是*"我要开新会话了，把下一个会话需要知道的全写下来"*。
  有人（Matt Pocock）更激进，**压在 15% 以下**。
  反方也记了："完整会话连贯性更好" —— 但**交接的损失可预期可管理，
  长上下文退化的损失隐蔽且不可预期**。
- **分层配置文件本身就是一个上下文预算决策**：`CLAUDE.md` / `AGENTS.md` 不是越多越好。

**掘金版补的一条**：交接文档必须**分清"已决定"和"待确认"**，
否则接手的 agent 会把讨论里的猜测当定论。可直接下这句指令：
> "把已确认的目标、约束、方案、相关文件、验收标准和待办整理到 handoff.md，
> **单独标出尚未确定的问题**。" 然后新会话："读 handoff.md，按其中的方案和待办完成修改。"

**CSDN 同题另两条**：① **上下文消耗的大头不是提示词，是工具自动读的文件内容** →
按**决策点**切会话（选型 / 执行 / 测试各一个），每个会话只贴方案摘要和目标文件；
② `.claudeignore` + 主动压缩 + 分阶段开新会话三件套，**单次大型任务成本降 30–50%**（自述值）。

---

## 三、第三笔账：模型发布的口径账

### 1. 有人没发榜单，而是重放了 20 个真实已合并 commit（paddo.dev / MindPattern）

同日两个旗舰（09-22）：**Claude Opus 5.5**（$4/$20，1M 上下文，cache read 降到 $0.20）
与 **GPT-6 Sol / Luna**（$2/$10、$0.10/$0.50，均为 GPT-5.6 同档的一半）。

paddo 的做法：从一个约 **3,700 文件**的 TypeScript monorepo 挑 **6 个已由人类写好、审过、合并过的生产改动**，
用 Claude Code 与 Codex 在默认 medium effort 下**各跑 20 次**：

| | 干净通过 | 测试回归 | 总成本 |
|---|---|---|---|
| **Opus 5.5** | **13/20** | **0** | $45.81 |
| **GPT-6 Sol** | 8/20 | **5** | $13.16 |

而在 **4 个自带 4,176 条断言的独立任务**上，**两者都是 100%**。
→ **差距只出现在脏活上。厂商榜单住的地方（自包含任务）两个模型都没问题。**

结论：**测试与评审强的地方用 Sol，测试薄的无人值守任务用 Opus 5.5。
一个每四跑就弄坏一次的便宜模型，只有在人能接住的时候才便宜。**

同一天口径打架的另两组：Artificial Analysis 给 Sol(max) **48 分 / 212 个里排 18**，Opus 5.5 **58**；
Browser Use 在 browser agent 上反过来（Sol 66.9 vs Opus 5.5 59.4，**成本 1/3.5**）。
→ **上线日评测的噪声本身就很大**，这是本条最该记住的。

### 2. ProgramBench：91.2% 不等于你在榜上读到的 91.2%

ProgramBench 共同作者 Ofir Press 指出：Anthropic 在系统卡里跑的是 **200 个实例中的 166 个**，
报的是**平均通过测试数**；官方榜只数**完全完成的任务**。
**部分解常常能过 60–70% 的测试** → 系统卡里的 91.2% 和榜上的 91.2% **不是同一个指标**。

→ M-0002（先核实再下结论）的第四种形态：**数字一样，口径不同。** 已记 **M-0018**。

### 3. Opus 5.5 的四个 breaking API 变更（会咬到已有代码）

1. **thinking 不能关**（也不能设 budget）；
2. `tool_choice: "any"` → **400**；
3. thinking blocks **绑定模型与会话** → 回放失败；
4. `computer_20251124` 工具被拒。

另有两条直接改账单：**`max_tokens` 要设到 128,000**（thinking 计入输出额度）；
**改 effort 要用 per-message 的 beta 参数** —— 顶层请求间改 effort **会让 prompt cache 失效**。
Anthropic 自己的迁移指南：**medium effort ≈ Opus 5 的 high**。

### 4. 本周其他上新（09-21 ~ 09-23）

| 模型 | 关键数字 | 备注 |
|---|---|---|
| **Grok 4.7**（xAI） | $2/$6 不变；**CursorBench 4.0 46.3%**（+5.9pt）；**Terminal-Bench 4.0 20.3% → 38.0%**；速度 2 倍 | 强化长任务、自我检查、**长上下文管理**；网友对跑分有争议 |
| **小米 MiMo-V2.6**（Pro/Flash，开源） | AA 综合智能 **46 分 = 当前最强开源**；DeepSWE v1.1 **+17 / +14 分** | 不到 6 天 Live RL 烧 $85万 / $262万，75 万条轨迹；**开源 7k+ RL 任务环境与端到端训练框架**；能搭 3D 游戏 / Blender 建模 |
| **腾讯混元 Hy Image 3.5 preview** | 2K 图 **¥0.15/张，只对输出计费**，单次最多参考 5 图 | 盲测与 Seedream 5.0 pro 持平；已接入元宝 / ima / WorkBuddy |
| **阿里平头哥真武 V900** | 算力上代 3 倍、显存 216GB、片间 1200GB/s | 2027 Q1 就绪；与主线弱相关，只登记 |

**推理效率（对本地/远程部署最实用的一组）**：
- **SGLang × Qwen × NVIDIA**：NVFP4 用于 **KV Cache**，decode 吞吐 **+26%~78%**；
- **树状推测解码**适配 **DeepSeek-V4**，吞吐最高 **+18.5%**。
→ 我们那个 Ollama 桥（qwen3.8:27b）下次调优，**KV Cache 量化是第一条该试的路**。

---

## 四、VSCode / Copilot：路由、会话与"agent 住进项目里"

**一手来源**：VS Code **1.139 Insiders** 更新日志 + GitHub Copilot 周更（09-14）。

1. **三档自动选模 efficiency / balance / intelligence** —— **三档选的是同一批底层模型，
   改的是路由偏好**：不是模型目录，是**成本-质量旋钮**。铺到 VS Code 扩展 / CLI / 桌面端。
2. **Agent 会话住进 Dev Container** —— 用项目自己声明的工具链与依赖，而不是宿主机环境。
   需要 Docker + 受支持的 devcontainer 配置，**渐进开放**。
3. **会话生命周期**：PR 合并后自动标 **Done**（可选宽限期后删除）；会话里**直接建 PR**
   （可审标题/描述、设 draft、或委托 agent）；Agent Merge 可让 agent 自己开 PR 走完评审与 CI。
4. **评审**：自动把"自己提过、后来被修复"的评论标 resolved；接受建议时**自动生成 commit message**；
   评审可调用 **shell 工具做验证**；**Lite 模式汇总多个 agent 的发现**降噪。
5. **治理**：Business/Enterprise 新增用量指标（DAU / 会话数 / 人均消息数）+ **额度追加审批流**；
   模型选择器新增 **Thinking Effort** 与**更长上下文**控件；`.jj`（Jujutsu）默认进 files.exclude。

**对我们**：三档路由那条最值得抄成概念 —— **"同一批模型，改路由偏好"**，
和我们"同一批脚本，改闸门阈值"是同一思路。Dev Container 对 Ren'Py/Unity 这类重依赖项目有意义，
但本机 Docker 条件未知，**只登记**。

---

## 五、DSH（DeepSeek Harness）插件第二波

第十七辑只登记了 DSH 生态的类别信号，这一辑落到具体仓库（**全部 REST API 实测**）：

| 仓库 | ★ | 协议 | 是什么 | 判断 |
|---|---|---|---|---|
| `Clearailhc/clearai-dsh` | **381** | Apache-2.0 | 把 **Epistemic Loop**（frame→hypothesize→plan→observe→verify→evaluate→record 七段）做成 DSH 原生插件；产物是**领域本体**（可增长的、下轮按概念可取回的知识结构） | ⭐ 星最高、思路最完整：**每条边都要被证据和独立评审检验过** |
| `cv-superding/dsh-deepseek-web-login` | 127 | Apache-2.0 | 把 chat.deepseek.com 网页版模型当 LLM provider（非官方） | ⚠️ 非官方，合规风险 |
| `a86582751/dsh-nexttavern` | 103 | GPL-3.0 | DSH **长篇角色扮演** agent：SillyTavern 角色卡导入 / 行动选项卡 / 分支对话 / 长篇记忆 / 关键词+语义混合检索 | 与"角色一致性"老问题同一领域 |
| `LuxUmbra697/DSH-Desktop` | 62 | MIT | 把 DSH 装进独立窗口，双击即用、免终端免浏览器，**载荷可裁到 210MB（便携包 74.8MB）** | 与第十七辑 dsh-desktop 同类 |
| `huangziyuan-general/dsh-novel-forge` | 13 | MIT | 小说锻炉：**事实账本 / 上下文包 / 阶段门禁 / 零费用去 AI 味扫描 / 确定性审计 / 提案制修订** | ⭐ **"零费用去 AI 味"= 确定性规则而非模型调用**，与我们 `check_dialogue.py` 同一路线 |
| `bowenliang123/dsh-context` | **1,448** | - | 上下文可视化：六色组成（System / Tool Schemas / User / Injected / Assistant / Tool Results）+ **最贵的 5 个工具 Schema** + 逐请求演进 | ⭐ **把"上下文账单"变成可见的** |
| `snow-The/dsh-session-handoff` | - | - | 结构化交接文档导出/恢复 + **主动剪枝**（`acp_status` / `acp_compress` / `acp_set_limit`，默认软硬限 60%/70%）+ 会话回收站 + 模型路由 | 与第二节 handoff 阵营完全同题 |
| `TheHeartFickle/dsh-session-manager` | - | MIT | 会话**回退**（Ctrl+Shift+Z，基于官方 `sessions.fork` 重建分支）+ 归档；依赖 DSH ≥ 0.1.2-rc.1 / Node ≥ 20 | 与上面互补 |

**本辑判断**：DSH 生态这一周长成**三个可辨认的子方向** ——
**① 看得见（dsh-context）② 接得住（session-handoff / manager / ccompactor）③ 少装点（verbatim compaction）**。
我们本机 `dsh 0.1.0-rc.6` 已装，**先装 dsh-context 把账单看清楚**，再决定要不要上压缩类。

---

## 六、Agent 风险与治理（本周三条）

1. **32.5 万次实验：13 个 agent 里 8 个会给"推断有钱"的用户推荐更贵的选项** ——
   差别对待不需要被明示，会从上下文里学出来。
2. **CLOSEDQUORUM（Cisco Talos）**：自称首个**完全自主的多模型 AI C2 植入体**。
   Windows 植入体收集主机信息 → 发给**最多四家商业模型供应商**（DeepSeek / Qwen / Mistral / Gemini）
   → **投票决定下一步动作**，目标是凭证与加密钱包。
   **重点不是 AI 用法，是"投票"这个设计**：不为更聪明，是为了**任何一家断供都拦不住它**。
   Talos 未确认有在野部署。
3. **Google Research RRSI**：给 agent 的**自我改进**加正则化（防越改越偏）。
4. **Amazon 封了 Meta 的购物 agent** —— 平台侧开始对外部 agent 关门。

---

## 七、游戏侧（本辑新增，全部 REST 实测）

| 仓库 | ★ | 协议 | 是什么 | 判断 |
|---|---|---|---|---|
| `holokat/AetherFX` | 1 | MIT | **AI 能署名的游戏 VFX**：typed building blocks → agent 看自己的渲染迭代 → 产物是一个小 JSON；**所有编辑动作都是 MCP 工具**；无 shader、无二进制资产，靠小型 C 库在游戏里播放 | ⭐ **"agent 可署名 + 确定性 + 可移植"三件套**，思路比星数重要 |
| `Jadis0x/URKit` | 25 | MIT | Unity **Mono 与 IL2CPP** 通用 modding 框架（原生 C++） | 与第七辑 DroidSpy（手机端 dnSpy）互补：一个解包、一个注入 |
| `song-chaoyang/UnityAssetDB` | 49 | MIT | **Rust + SQLite + tree-sitter**，把工程里所有 Unity 资产引用变成可查询数据库，CLI + Web | 对"AI 找资产引用"是正解（比让模型 grep 全工程省上下文） |
| `q956085398-netizen/RenpyTranslatorNG` | 0 | - | Ren'Py 汉化工作台：**稳定项目身份 / 出现位置级译文记录 / 事务式应用与恢复点 / 外部 tl 变更检测** | 0★ 但**"事务式应用 + 恢复点 + 外部变更检测"正是第 10 轮英文版缺的三样** |
| `mawen0317/renpy-vn-engineering` | 0 | MIT | 给大型 Ren'Py / VN 项目的 Claude Code skill（工程纪律） | 0★，只登记 |
| `banjiu763-cpu/visual-novel-illustrator-skill` | 2 | - | VN 插画 skill：剧情驱动 CG + 角色一致性 | 与第十辑 Story Illustrator 同类 |
| `michaltomczykowski/godot-ai-animation-toolkit` | 0 | MIT | 7 个 AI 原生 Godot 动画工具（预设 / 原地剪辑 / 检查审计） | 0★，只登记 |

**本辑游戏侧结论**：这周没有"AI 又做了个游戏"的大新闻，全是**工程化零件**
（可查询资产库 / 可署名 VFX / 事务化翻译 / 注入框架）。
→ 与主线一致：**便宜的"做"已经做完了，现在贵的是"接得住"。**

---

## 八、本辑自测（唯一"改了"的部分）

### ✅🔬 量了一次自己的 harness tax —— 闭环上一轮待办 #1

第十七辑的教训是"**量之前必须先隔离调用侧个人配置**"（否则量的是"我的机器"不是"这个工具"）。
这一辑照做：不看模型侧，**只读本机文件**量"每次请求都要重发的固定块"。

**产出**：`D:\34498\Documents\_tools\harness_tax_probe.py`（零依赖、可重跑；
有 tiktoken 走 cl100k_base 精确计数，没有则退回近似并**在输出里标注口径**）。

**实测结果（2026-09-23 23:47，本机）**：

| 组成 | token | 占比 |
|---|---|---|
| **MCP 工具定义**（7 个服务器 / 95 个工具） | **10,519** | **50%** |
| 常驻记忆文件（工作区 MEMORY.md 4,733 + 用户级 1,540 + USER/SOUL/IDENTITY） | 7,721 | 37% |
| 18 个技能的 frontmatter | 2,660 | 13% |
| **合计** | **20,900** | 占 200k 窗口 **10.45%** |

最贵三项：`bf45d9eff733`（8 工具 / 2,977 token，canvas 类）、
`ae1e01473eb6`（**45 工具 / 2,293 token**，GitHub）、`33d3ce39d97f`（9 工具 / 1,981 token，表格）。
最贵技能：`tencent-meeting-skill` 298 / `fullstack-dev` 222 / `github-pages-auto-deploy` 191。

**三条结论**：
1. **MCP 是最大的一块，而且"连上就付、不用也付"** —— 45 个 GitHub 工具里常用不到 10 个。
   第二节那个 `KaryawanSurga/mcp-context-budget`（1★/MIT）正是这个思路的现成实现：
   **启用一个 MCP 服务器之前，先量它要占多少上下文。** 已进索引 + 房规。
2. **记忆占 37%，比技能还贵** —— 房规 #35 说"上下文是预算"，这条给出**具体花费**：
   用户级 MEMORY.md 1,540 + 工作区 MEMORY.md 4,733。**工作区那份该瘦身了。**
3. **与 HarnessTax 论文对得上量级**：论文说 Claude Code 首次调用固定块 27,011 token，
   我们这边**调用侧自己就贡献 20,900** —— **tax 的大头确实在客户端那一侧。**

**已落的改动**：
- 新增 `_tools/harness_tax_probe.py`
- 新增房规 **#37**（MCP 先量后开）、**#38**（记忆按 token 计预算）、**#39**（交接分清已决定/待确认）
- 新增决策原则 **#52**（逐字压缩优先于摘要压缩）、**#53**（50% 交接 + 计划落盘）、
  **#54**（合并前六条安全检查）
- 新增 **M-0018**（数字相同，口径不同）

### 📖 读了全文但没改的

- **Month 3 Crisis**：方法好，但我们**没有"架构边界"这道闸门** → 写进下一轮待办，不擅自加
- **50% 交接 / handoff.md**：操作清晰，但**已有 mistakes/ + 每日日志 + 自动化记忆三层**，
  再加一层 handoff 会重复 → **只取"分清已决定 / 待确认"这一条**写入房规 #39
- **Opus 5.5 四个 breaking 变更**：我们走 Ollama 桥不受影响 → 只登记（换云端模型时会咬人）
- **`clearai-dsh` / `dsh-context`** ⚠️ **只登记不装**：本轮没有 DSH 会话在跑，装了测不出东西
- **AetherFX / URKit / UnityAssetDB** ⚠️ 需要 Docker / 本机无 Unity 工程 → 只登记

---

## 九、下一辑搜索缺口

1. **"架构边界被绕过"有没有现成闸门**（Month 3 Crisis 的 Frankenstein 效应）—— 最想找的
2. ~~面向角色对白的 AI 味检测~~ —— 因游戏线终止，**该待办实际已失效**，本辑起不再跟踪
3. 活跃的开源 **Steam 上架/发行**工具（第十六辑起两次未闭合）
4. **verification skill**（`zaid-mian/vibe-coder` 的 "interview first, verify the repo"）有没有成熟版
5. 本地/远程推理的 **KV Cache 量化**（NVFP4）在 Ollama 上的实操路径
6. DSH 三个子方向里，**"少装点"那一支到底谁家能跑**（需要有真在跑的 DSH 会话）

---

## 十、本辑统计

- 新增信源：**约 44 条**（中文约 9 / 官方与英文约 14 / GitHub 21）
- 累计经验帖：约 523 → **约 567 条**
- GitHub 索引：1094 → **1104 项**（第二十四版增补 10 张卡）
- `agent-house-rules.md`：36 → **39 条**；`game-production-pipeline.md` 原则 51 → **54 条**；
  `mistakes/` 17 → **18 条**（+M-0018）
- 新增资产：`_tools/harness_tax_probe.py`
