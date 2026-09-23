# 跨平台游戏制作 × AI 开发资源梳理（2026-09-23 · 第十九辑）

> 搜索覆盖：GitHub（本辑 **15 个查询 / 153 行候选 → 32 个仓库 `gh api` 逐条实测**，
> stars · forks · 协议 · 语言 · 推送与创建日期**无一估算**）/ CSDN · 稀土掘金 · 今日头条 ·
> 腾讯云开发者社区 · 博客园 / 官方与聚合站（GitHub Changelog · VS Code Insiders Release Notes ·
> Google · Microsoft · Amazon · Anthropic · OpenAI · xAI · 阿里 · Yandex）/ 英文社区
> （Hacker News · quidproquo 日报 · MindPattern · agihunt · sift · malpass · datapipesoft ·
> AIToolTier · worldprogramming · agentpatterns）
>
> 上一辑（第十八辑）的主线是**「账到期」** —— 三笔账在同一个星期到期：vibe coding 的维护账、
> 摘要压缩的失真账、模型发布的口径账。**本辑顺着「失真账」往下追一层。**
>
> **本辑主线 = 「省下来的 vs 赔进去的」。**
> 上下文省钱的技术在这一周已经成熟到**可以量产**（`context-mode` 33.12 万次 npm 安装、
> 98% 削减、17 个平台）。但同一周有**三份互相独立的材料**在说同一件事：
> **省错了地方，赔的比省的多。**
> ① `context-mode` 自己删掉了它最出名的功能（22 处简洁提示注入，因为损害基准）；
> ② arXiv 2609.26629 实测 LLM 生成的角色**表面千差万别、行为高度同质**；
> ③ 我们**自己跑了一遍**：三条新指标，只有一条抓到东西。
>
> 已有索引：`index.html`（**1104** 项 → 本辑 **第二十五版增补 8 张卡 → 1112**）
> + 前十八辑经验帖（累计约 567 条 + 本辑 **约 38 条** ≈ **605 条**）
> + `game-production-pipeline.md`（决策原则 **54** 条）
> + `agent-house-rules.md`（**39** 条房规 → 本辑 **+2 → 41**）+ `mistakes/`（**18** 条）
>
> 上一辑存档：`csdn-social-summary-v18.md`

---

## 本辑一句话

**工具输出可以往死里压，模型的说话方式和行为分布不能压。**
压前者是纯赚（98% 削减，且用指针不是截断）；压后者 —— `context-mode` 试过，
**Moonshot AI 在 kimi-k2.5 上的报告让它把 22 处注入全删了**。

---

## 一、本辑第一部分：一个项目的自我推翻（已读仓库正文与 issue）

### 1. `mksglu/context-mode` —— 23,982★ / 1,729 forks / NOASSERTION / TypeScript

**它做了什么**：在 **MCP 协议层**装一道拦截层。工具（Bash / Read / curl）的原始输出先进沙箱，
超过 `LARGE_OUTPUT_THRESHOLD = 100KB` 的**不截断** —— 写进 SQLite **FTS5** 全文索引，
只给模型回一个**指针**，要用再 `ctx_search` 取片段。11 个 `ctx_*` MCP 工具，
**17 个平台**（Claude Code / Codex / Cursor / Copilot CLI / agy / Qwen Code / Kimi Code / Zed …），
npm 安装量 **331,200+**。

**为什么"不截断"是关键**：截断会丢尾巴（日志最后的报错往往就在尾巴上）；
**外部化 + 指针**不丢任何东西，只是不进上下文。这是和"摘要压缩"完全不同的两条路。

**⚠️ 本辑最值钱的一段（#482）**：早期版本会在前后注入 **"Terse like caveman（像穴居人一样简洁）"**
这类简洁提示。**Moonshot AI 在 kimi-k2.5 上的报告显示：激进的简洁提示会损害编码/推理基准。**
作者因此**全量移除了 22 处注入点**，Pillar 4 改成 **"No prose-style enforcement"** ——
只压缩工具输出，**绝不干预最终答案的文风**。全量测试 **2,645 passed / 0 failed**。

→ **这条直接修正我们第十七辑的房规 #36**（`i-have-adhd` 八条）：
八条针对的是**给人读的产出**，不是**给模型的系统提示**。两者混用会赔。
**已写成房规 #40。**

**其他可抄的机制**：
- `PreToolUse` **强制路由**：不让裸工具把输出直接倒进上下文（Claude 系用 deny/ask/modify，
  agy 1.0.6+ 实测能真强制）；
- **dispatcher fail-open**：hook 脚本缺失时 `exit 0` —— 因为 Copilot CLI 会把 exit-1 的
  PreToolUse 当成 Deny，直接把整个 agent 砖化；
- **别把根 `.mcp.json` 当真相**（已 gitignore + 从 npm tarball 移除）—— 会造成"新鲜安装损坏"的回归。

参考链接：https://github.com/mksglu/context-mode

### 2. 同一周的三个"省钱"项目，走的是同一条路：把确定性部分从模型手里拿走

| 项目 | 星 / 协议 | 它拿走了什么 | 官方数字 |
|---|---|---|---|
| **alibaba/open-code-review** | 40,091★ / Apache-2.0 / Go | 选文件、打包、规则匹配交给工程逻辑，只留动态判断给 agent | 同底座模型下 precision/F1 显著更高，**token 约 1/9** |
| **cloudflare/security-audit-skill** | 20,680★ / MIT / JS | 六阶段流程写死；**发现者永不验证自己**；判断标准写进流程不写进提示词 | 自测：**跑一次只找到反复跑能找到的约一半** |
| **addyosmani/agent-skills** | 98,643★ / 10,365 forks / MIT | 把"每次都要重讲的能力"打包成 skill | 星数是这批里最高的 |

三者同一天（09-19）被同一份日报发现，作者分别是阿里、Cloudflare、微软 ——
**都不是新框架，都是给已经在跑的通用 agent 加护栏。**

**最该抄的一条**：**"一次只能找到一半"是验证侧最诚实的自述。**
我们有六道 `check_*.py` 闸门 + `mistakes/`，**但从来没量过自己的召回率。**
（对照第十三辑"验证侧"、房规 #31"闸门保证没坏，不保证好"）

链接：
- https://github.com/alibaba/open-code-review
- https://github.com/cloudflare/security-audit-skill
- https://github.com/addyosmani/agent-skills

---

## 二、第二部分：赔进去的那一半（本辑唯一"改了"的实测）

### 1. arXiv 2609.26629 · PersonaWeaver（2026-09-22）

**它测出了什么**：LLM 做**程序化角色生成**时（给游戏 / 模拟世界批量造人），
两条现有路线 —— 直接生成、或从 persona 库里检索后改编 —— **都产出行为同质化的人群**：
角色**压倒性认同正面道德规范**、回答问题时**用"助手式"的反应**。
作者的解法是把**世界构建**与**行为规格**解耦，另建手工整理的立场库与反应库。
实测覆盖 10 个场景 × 3 个 LLM：**道德与互动反应的分布都更宽，人际语言、回应长度、情绪也更分化。**

**为什么这条打中我们**：第十八辑的待办写的是
「拿 `no-ai-slop` 的 20 条模式与 `check_dialogue.py` 做差集」。
**PersonaWeaver 给的不是 20 条模式，是一个更深的层**：
我们那六条（脚注 / 旁白套话 / 填充词 / 朗读 / 口癖 / 平均句长分化）
**全在表层形式，一条都没看"反应分布"。**

论文：https://arxiv.org/abs/2609.26629

### 2. 🔬 我们自己做了一遍差集（不是抄，是实测）

从 `_backup/amphoreus-roast-v1.9-ch11-src.zip` 里取出 `tools/check_dialogue.py` 与 `game/*.rpy`，
**先复跑旧闸门确认基线**（11 角色 / 144 句：**C1~C6 全过**，最长/最短平均句长 2.50），
再按 PersonaWeaver 的三个维度写探针跑一遍 → 存为
**`_tools/dialogue_homogeneity_probe.py`**（通用化，接任意 `game/` 目录）。

| 新指标 | 实测结果 | 判定 |
|---|---|---|
| **A. 角色内部句长变异系数 CV** | 11 个角色全部 **0.47~0.70**，无一 < 0.45 | ❌ **不报红** —— 本作对白长度是自然的 |
| **B. 角色两两用词 Jaccard** | 45 对，中位 **0.168**，最高 **0.267**（灰毛×昔涟） | ❌ **不报红** —— 用词分化良好 |
| **C. 情绪句占比（问号 / 感叹号）** | 三月七 **80%** · 帕姆 **64%** · 缇宝 **55%** …<br>**剧本 0% · 阿那克萨 0%** | ✅ **抓到信号** |

**结论（这才是"核实后测试是否对自己有用"的结果）**：
三条新指标里**只有 C 值得做成规则**。A、B 是**真缺口**（C1-C6 完全没覆盖），
但**在本作上已经达标** —— 不做成闸门，只登记。
**C 是真的缺口且有信号**：两个角色**一句问号感叹号都没有**，而最高的角色到 80% ——
这正是 PersonaWeaver 说的"反应分布过窄"。
（剧本 0% 可能是设定：它是旁白式解说角色；阿那克萨 0% 是学究人设。**但两者同时为 0，值得人看一眼。**）

→ **已写成房规 #41**（对白类产出的"反应分布"检查）+ 存探针工具。

### 3. 同一周另外两条"赔在里面"的旁证

- **`max-sixty/worktrunk`（8,365★ / Rust）**：git worktree 管理 CLI，专为并行 agent 设计。
  它提醒的是第十六辑那条"多 agent 并行收益已转负"的**另一半**：
  **协调税 = 沟通成本 + 冲突成本**；**后半是可以工程化的**（一人一棵工作树，互不踩）。
  → 我们选了单 agent 串行路线没错；**但哪天真要并行，消冲突的优先级高于再加一个 agent。**
  https://github.com/max-sixty/worktrunk
- **两个记忆项目，选错了会赔在合规上**：
  `tigerless-labs/agent-memory`（966★ / **MIT** / Python，**Markdown 是真相源**，
  本地排序检索不要 API key，一个 store 同时给 Claude Code 和 Codex 用）
  vs `tinyhumansai/openhuman`（40,058★ / **GPL-3.0** / Rust 桌面应用）。
  → **已有等价物（`mistakes/` + `.workbuddy/memory/`），不替换**；
  可取的是「**一个 store 跨外壳共享**」—— 换桥换 shell 时记忆不跟着换。
  ⚠️ **GPL-3.0 比 MIT/Apache 严得多，商用前必须确认。**

---

## 三、VS Code / Copilot：把"省还是不省"做成了一个显式旋钮

**本辑第一次把 VS Code 与 Copilot 单独列为一条线**（用户点名要看 VSCode）。

- **VS Code 1.138 / 1.139（Insiders）**：
  · **Auto 模型三档**：`Efficiency` / `Balance` / `Intelligence` ——
  把"省钱还是要好"从猜变成**一个下拉框**（VS Code / Copilot CLI / Copilot app 全端）；
  · 模型选择器加了 **`Thinking Effort`** 与 **`Context Size`** 两个控件（1.139, 09-18）；
  · **Agents 窗口里跑本地 Dev Containers**（agent 用项目自己的工具链，需 Docker）；
  · **定时循环 agent 任务**（1.137 起按小时/天/周，public preview）· **实验性语音模式**
  （可中途口头改方向）· **Agent Merge**（agent 自己开 PR 并走完 review + CI）；
  · PR 全合并后自动把会话标 Done（opt-in）。
- **GitHub Copilot**：
  · **code review 自动 resolve**：后面一次提交修掉了，之前的评论自动关闭；
  接受建议时**顺手写 commit message**；
  · **Lite 档 = 多 agent ensemble**，GitHub 自家数字：
  **已解决评论 高危 +47% / 中 +31% / 低 +11%，review 成本 −8%**；
  · **企业级 agent 权限与沙箱**（不能被用户/工作区设置、自动批准或历史批准削弱）+
  JetBrains 沙箱公测；
  · **HydraFusion**（CLI `/experimental`）："本地 / 云 / 复合模型之间的自动语义路由"；
  · 用量指标把 **VS Code Agents 窗口**与编辑器 Agent Mode **分开统计**；
  · 节点：MAI-Code-1-Flash 退役；**9/28 起统一 Copilot 体验默认开启**；10/02 四个模型弃用。

**对我们的意义**：这三档是一个**可以直接类比到自己工作流的模式** ——
我们现在的分档是"上财远程 `qwen3.8:27b` 干重活 / 本地 qwen3:8b 干轻活"，
**但没有一个显式的旋钮，也没有记录每次为什么选哪档**。
（来源：https://github.blog/changelog/2026-09-18-github-copilot-weekly-releases-september-14/ ·
https://code.visualstudio.com/updates/v1_139 · https://aitooltier.com/tools/github-copilot）

---

## 四、模型上新与"口径账"（第十八辑已收 paddo / ProgramBench，本辑只补新面）

- **同日对撞（09-21/22）**：Anthropic **Claude Opus 5.5**（Artificial Analysis 智能指数 **58** 登顶，
  比 Opus 5 便宜 40%、快 30%）vs OpenAI **GPT-6 Sol + Luna**（Luna **$0.10 / $0.50** 每百万）。
  ⚠️ **口径分歧已公开**：Browser Use 测 browser agent 得到**相反结论**（Sol medium 66.9 > Opus 5.5 的 59.4，
  且便宜 3.5 倍）；Nate Herk 八项工作里七项选 Opus，付 $213 vs $74。
- **开源权重榜（Artificial Analysis，09-23 更新）前六**：GLM-5.3 (44.8) · Kimi K3 (43.6) ·
  GLM-5.3 Flash (41.8，**$0.24**) · Qwen3.8 2.4T-A95B (39.9) · Qwen3.8-Flash-Next (39.8，**$0.23**) ·
  **DeepSeek V4.1 Flash (39.5，231 tok/s，$0.53)**。
  → **第 3、5、6 名的价格是第 1 名的十分之一，智能差不到 6 分。**
- **阿里云栖官宣 Qwen 4**；路透另报阿里规划 **5–10 万亿参数**模型 + 自研芯片。
  **Qwen-Image-2.1** 在 Arena 图像编辑与文生图两榜拿下开源第一（编辑榜 1367 / 总榜 16）。
- **Hugging Face：transformers 可直接加载 GGUF**（传 `gguf_file` 即可）—— 本地推理离 llama.cpp 又近一步。
- **OpenRouter Batch API**：异步批量，24 小时内完成，**通常半价或更低**，已支持 70+ 模型。
- **Epoch AI**：达到同等 AI 性能的成本**平均每季度降约 47%（每年约 13 倍）**。
- **Yandex 开源 AliceAI Foundation**：80B MoE（**激活 3B**）、256K 上下文、KDA 混合注意力，从零训练。
- **语音榜**：Cartesia Sonic 3.6 在 Artificial Analysis Controlled Voice Arena 拿下 **9 种语言里的 8 种第一**；
  阶跃 StepAudio 3 在 STT 并列第一（**1.7% 错误率**）。
- **⚠️ 安全（本辑唯一一条"AI 被用来做坏事"的新形态）**：Cisco Talos 披露 **CLOSEDQUORUM** ——
  首个被报告的**完全自主 AI command-and-control 植入体**（Windows）。它采集主机数据，
  发给**最多四个商用模型 API**（DeepSeek / Qwen / Mistral / Gemini），**哪个动作赢得投票就执行哪个**。
  目标 = 凭据与加密钱包。**投票设计不是为了更聪明，是为了更难拔掉。**

---

## 五、游戏侧（本辑增量较小，且有一处必须剔除）

- **⚠️ 去重纪律执行一次（M-0001 第五种形态）**：搜索命中两篇
  "20 天一人做微信小游戏上线"（`hqwc.cn/a/1731390` / `mhpn.cn/news/2151456`，同一篇《像素农场》），
  与**第五辑已收的"20 天微信小游戏复盘"同源** → **主体剔除**，只记这次识别本身。
  又一次证明：**"ID 新 ≠ 内容新"。**
- **武侠 RPG 一天做完**（@0x0funky，09-17）：剧本 / 人设 / 战斗 / 水墨场景 / 动画 / UI / BGM 全与 AI 协同，
  **不到 1 天**；成本 **< $300**（GPT Pro 20x 用掉当周约 60% 额度 + Grok Build 约 50% + Lyria API $2）。
  剧本完成约 60%，22 张地图已做 11 个场景、20+ 角色；**战斗从即时制改成回合制**（更符合怀旧感）。
  → **可取的不是速度，是"改设计"这件事没被 AI 绑架。**
- **`FunplayAI/funplay-unity-mcp`（251★ / MIT / C#）**：20 模块 **91 工具**。分水岭是三个动词：
  `execute_code`（内存里现编现跑 C#）、**Play Mode 自动化**（进播放模式 + **模拟输入** + **截图**）、
  **instanceId 链式调用**。
  → **选型判据（可复用到任何引擎 MCP）：工具清单里有没有 run / input / screenshot。**
  只有 create 和 edit 的都是半成品（与第十七辑 `beckett-godot-mcp` 的 inspect/author/run/**SEE** 同一条）。
  同批 **`IvanMurzak/Godot-MCP`（251★ / Apache-2.0 / C#，42 工具 / 12 家族）** 更值得看一眼的点是：
  **它与同作者的 Unity-MCP 共用 `ReflectorNet` 反射底层**（NuGet 包），不是各写一套
  → **"项目之间有没有共享底层"比"工具数量"更能判断是不是认真的。**
- **美术/角色工具两条**：`sprited-ai/sprute` v1.0（开源 CLI，8 方向像素角色 Comfy 工作流）；
  **NPC Sprite Studio**（itch.io，$9 买断，32px 分层像素角色，头发与衣服共用同一动画网格，
  导出 8 层 PNG + JSON 帧数据，**含"AI 参与了代码与程序化图形"的披露**，离线 HTML 打开即用）。

---

## 六、AI Dev 自测结论（本轮，逐条给出"改了没有"）

| # | 对象 | 结论 | 落地动作 |
|---|---|---|---|
| 1 | **`mksglu/context-mode` #482 自我推翻** | ✅ **真有用，修正已有房规** | **房规 #40**：压缩工具输出 vs 压缩文风是两件事；房规 #36 的适用面被限定 |
| 2 | **arXiv 2609.26629 PersonaWeaver** | ✅🔬 **真有用，已实测** | 写探针 `_tools/dialogue_homogeneity_probe.py`，跑出三指标实测值（见 §二.2） |
| 3 | **差集结果** | ✅ **只有 1/3 值得落地** | **房规 #41**（反应分布检查）；A、B 只登记不落地 |
| 4 | **`alibaba/open-code-review`** | ✅ 真有用 | 判据「错不起的步骤不许交给模型」进决策原则（与已有 `check_*.py` 同路，未单独立项） |
| 5 | **`cloudflare/security-audit-skill`** | ✅ 真有用 | 两条规矩（生成者≠验证者 / 标准写流程不写提示词）进决策原则 |
| 6 | **`max-sixty/worktrunk`** | ⚠️ 有参考价值 | 协调税拆成"沟通 + 冲突"，记进 §二.3；当前单 agent 串行，不装 |
| 7 | **`tigerless-labs/agent-memory` / `openhuman`** | ⚠️ 只登记 | 已有等价物；**GPL-3.0 合规红线**已记 |
| 8 | **`alexgetmancom/claudecut`（37★）** | ⚠️ **只登记不能测** | 36-token 系统提示是 harness tax 的"地板"对照点；**本机 `claude` CLI 跑不了**（沙箱限制） |
| 9 | **VS Code / Copilot 三档** | ⚠️ 有参考价值 | 记进 §三；"没有显式分档旋钮"列为下一轮待办 |
| 10 | **游戏侧（武侠 RPG / Sprute / NPC Sprite Studio）** | ⚠️ 只登记 | 游戏线已终止；取的是"改设计不被 AI 绑架"与"披露写法"两点 |

**本轮的"改了"一共四处（都可复核）**：
`agent-house-rules.md` 39 → **41 条**（+#40 / #41）·
`_tools/dialogue_homogeneity_probe.py`（新，通用化探针）·
`index.html` **1104 → 1112**（第二十五版增补 8 张卡）·
`D:\34498\Documents\AGENTS.md`（**新** —— 承接第十八辑待办 #6，补齐工作区隐式约定）。

**去重纪律（本辑执行记录）**：剔除 **8 条已收录**
（`hi-godot/godot-ai` · `beckettlab/beckett-godot-mcp` · `Donchitos/Claude-Code-Game-Studios` = CCGS ·
以及 §五那条 20 天微信小游戏同源重复）与一批 0★ 同模板空壳。
**新形态识别**：**"同一篇稿子换个站发"** —— `hqwc.cn` / `mhpn.cn` 是同一批 SEO 站的镜像域名，
**以后看到这两个域名要直接怀疑同源**（M-0001 第五次形态变化）。

---

## 七、索引维护（本辑）

- `index.html` **第二十五版增补 8 张卡**（**1104 → 1112**，脚注 **[1104]-[1111]**），
  脚本 `insert_v25_cards.py`（幂等 + 页头锚点唯一断言 + **插入点 div 深度自检** + 重复仓库检测）。
- 卡片见：**🆕 第二十五版增补 · 口径**（8 项）。
- 全量实测数据（stars / forks / license / language / pushed / created）：`_r18_api_out.txt`（32 个仓库逐条 `gh api`）。
- 原始候选：`_r18_gh_out.txt`（15 查询 / 153 行）。

---

## 八、下一辑待办（承接 + 本辑新增）

**承接**
1. **索引仓库推送**（`86429ff` 之后的所有提交未推，走 `_tools/push_via_api.py`）
2. **`rpycdec` 自查**：对 `_backup/amphoreus-roast-1.9-pc.zip` 跑一次（两辑没轮到）
3. **找 `index.html` 里那个多余的 `</div>`**（div 计数差 −1，既有问题）
4. **试 Codex 本地 `config.yaml` → Ollama 纯离线路线**
5. 仍未闭合：活跃的开源 **Steam 上架/发行**工具（第十六辑起三次未闭合）

**本辑新增**
6. **给"模型分档"做一个显式旋钮**：我们现在是"远程 27B 干重活 / 本地 8b 干轻活"，
   但**没有记录每次为什么选哪档**。可抄 Copilot 的 Efficiency/Balance/Intelligence 三档写法。
7. **`D:\34498\Documents\.workbuddy\memory\MEMORY.md` 瘦身** —— harness tax 实测里它是
   **最大的单块（4,733 token）**，而房规 #38 要求"记忆按 token 计预算"。
8. **量一次自己闸门的召回率**（被 `security-audit-skill` 的"一次只找到一半"提醒）——
   做法：往已验收的版本里**故意塞回一个已知 bug**，看六道闸门有几道报红。
9. **DSH 上下文插件二轮评估**（等脱离 rc）+ **Codex 本地纯离线**

---

*本辑统计*：新增约 **38 条**信源（中文约 6 / 官方与英文约 18 / GitHub 14）→ 累计约 **605 条**；
`index.html` **1112** 项（+8）；`agent-house-rules.md` **41** 条（+2）；
`mistakes/` **18** 条；新增工具 1 个（`_tools/dialogue_homogeneity_probe.py`）+ 新文件 `AGENTS.md`。
