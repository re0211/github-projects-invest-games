# 跨平台游戏制作 × AI 开发资源梳理（2026-09-23 · 第十六辑）

> 搜索覆盖：GitHub（本辑 19 个查询 / 268 条原始候选，stars · 协议 · 推送日期
> **全部走 REST API 实测**，无一估算）/ CSDN · 稀土掘金 · 阿里云开发者社区 · 今日头条 ·
> 腾讯网 · 个人技术博客 / 大模型公司官方与聚合站（Anthropic · OpenAI · Google · DeepSeek ·
> 通义 · 智谱 · 腾讯混元 · 面壁 · MiniMax）/ 英文社区（Hacker News · r/ClaudeAI ·
> r/gamedev · GIGAZINE · Artificial Analysis / Arena）
>
> 上一辑（第十五辑）的主线是**「把人工环节交给工具」**——
> 凡是能用工具自动化的环节，都不该继续靠人对账。
> 这一辑顺着它再走一步，撞上的却是它的**副作用**：
> **当"做出来"真的变便宜之后，同一道题会被所有人同时做。**
>
> **本辑主线 = 「同题海啸：便宜的是"做"，贵的是"分辨"和"协调"」。**
>
> 已有索引：`index.html`（**1085** 项 GitHub 项目，本辑新增 6 张卡 → 第二十二版增补）
> + 前十五辑经验帖（累计约 428 条 + 本辑 **约 45 条** ≈ **473 条**）
> + `game-production-pipeline.md`（9 步工具链 + 决策原则 **46** 条）
> + `agent-house-rules.md`（**33** 条房规）+ `mistakes/`（错误记忆 **16** 条）
>
> 上一辑存档：`csdn-social-summary-v15.md`

---

## 本辑一句话

**同一个模型，换一个"外壳"，成功率不变、账单翻倍**（UC Berkeley 实测 21 组，最高 5 倍差）；
**同一个题，一周之内会出现二十个实现**（`godot-mcp` 空壳、Jev 生态、14 个同模板 SEO 站）。
→ **"有没有"早不是问题了，"用哪个"才是。**

---

## 一、同题海啸的三个现场（本辑主线的证据）

**为什么单独先说这组**：它们不是三个新闻，是**同一件事的三个现场** ——
生产变便宜之后，冗余以指数速度堆积。

### 1. 引擎接入的洪水：一周 ~20 个 `godot-mcp` / `unity-mcp` 空壳

本辑 19 个查询里，`MCP godot` / `MCP unity` 两条命中的**几乎全是 0★ 新建仓**：
`AkiraZ1/godot-mcp`、`YasiruRF/godot-mcp`、`jxlee007/godot_mcp`、`magian1127/GodotMCP`、
`teratron/godot-mcp`、`KasuganoSorakog/UnityMCP`、`gitgomez/UnityMCPBridge`、
`lightning-strom/UnityMCPDemo`、`DFTGames/UnityMCPWorkflow`……（全部 2026-09-15~09-23 新建）
**注意这不是"质量差"**，而是**"这件事已经便宜到人人各做一份"**。
对照：第六辑我们收 Godot MCP 时它还是**稀缺物种**（32 工具就算多），现在它是**日用品**。

### 2. 去 AI 味的洪水：同期冒出 7~11 个同类工具

上一辑我们记下的缺口「**"AI 文风检测"近三个月没有像样的开源项目**」——
**本辑正式闭合**，而且是以"洪水"的方式闭合的：

| 工具 / 来源 | 数量级 | 关键点 |
|---|---|---|
| [**petergyang/no-ai-slop**](https://www.ai.jp.net/article/no-ai-slop-debuts-on-github-a-tool-that-strips-ai-sounding-phrasing-from-your-wr-e0280b?lang=sc) | **11,051★ · MIT · 规则式** | 识别 **20+ 种 AI 写作模式**（"不是 X 而是 Y"、夸张结尾…），可 `/no-ai-slop` 装进 Claude Code / Codex |
| [ai345.info 7 项目选型指南](https://www.ai345.info/ai-guide/remove-ai-flavor-skill-guide) | 7 个方案 | 给**可直接粘贴的改稿提示词**："只清套话，不新增事实；保留数字与引用" |
| [夜雨聆风 11 工具清单](https://www.yeyulingfeng.com/a/947636.html) | 11 个方案 | 把「**检测类**」与「**改写类**」分开 —— **我们缺检测、不缺改写** |

**对我们的直接价值**：`no-ai-slop` 与我们的 `tools/check_dialogue.py`（第 5 轮，六条规则）
**同源同构**（规则 + 阈值，不靠模型）。**它那 20 条模式可以作为我们的外部对照表**，
用来找我们六条规则漏掉的形态（见第七节"立刻能做"）。

> ⚠️ **仍未闭合的那一格**：现有工具**全部面向"通用文本"**，没有一个面向"角色对白"。
> 直接套到我们的剧本上会误伤 **NPC 的设定性套话**（房规已承认"NPC 说套话是设定，
> 旁白和内心说套话才是 AI 味"）—— 这一条**仍无解**，如实记下。

### 3. 发行侧的洪水：一家公司一天上架 29 款游戏

[Hard Shark Games 2026-09-15 一天放出 29 款 EA 游戏](https://mangodeveloper.com/articles/indie-publisher-drops-29-steam-games-in-one-day-and-the-math-might-actually-work)：
**同一段商店简介逐字复制**、扎堆用 **$50 的 Unity 模板**（`Supermarket Life Simulator`
与 `Checkout Frenzy` 截图里连杂货图都一样）、**全部 29 款只对"胶囊图"做了 AI 披露**。

- 成本：Steam 每个商店页 $100（营收过 $1,000 可退）→ 29 款共 **$2,900**
- 回收：Boxleiter 法估算，**仅 3 款 5 天就估到 $1,783**（低端）～ $5,000+（高端）
- 真相：该公司**全部 217 个商品历史峰值同时在线从未破 13 人**

**这条对我们的价值是"反向的安心"**：它说明 **AI 披露规则已经被用到了最薄的一层**
（只标胶囊图，不标代码与素材）。而我们老老实实标了"背景 / 立绘 / 语音都在范围内"——
按第十一辑的 Steam 披露规则，我们才是**少数派**，不必焦虑。

---

## 二、AI 开发与使用（本辑最高价值的一组 · 14 条）

### ★ 1. HarnessTax：同一个模型，换个外壳，**同一成功率、两倍的钱**

[UC Berkeley Sky Lab + Arena，2026-09-16 发布](https://www.ainews.tech/blog/measure-what-your-agent-harness-sends-per-call)，
7 个模型 × 3 个 harness（**Claude Code / Codex CLI / Pi**）= 21 组配对，各跑 30 道
SWE-bench Lite 与 Terminal-Bench 2.0，每道 3 次。

**最关键的一张数**（首次调用的上下文，token）：

| Harness | 工具数 | 首次调用输入 token |
|---|---|---|
| Pi（极简，MIT，仅 4 个工具） | 4 | **1,972** |
| Codex CLI | 3~9 | **11,308** |
| Claude Code | 23 | **27,011** |

- Claude Fable 5 在 Claude Code 里解开 **97.8%**、在 Pi 里 **96.7%** ——
  **成功率差 1.1 个点，成本差约 2 倍**（$1.33 vs $0.67）；**turn 数几乎一样**（15.3 vs 15.4）。
  → **"步数相同、每步更贵"**，这就是 harness tax。
- 跨模型几何平均：Claude Code 约 = **2.0× Pi**、**1.6× Codex**。
- 极值：**GPT-5.6 Luna 在 Pi 里 $0.03/次，在 Claude Code 里 $0.15/次 —— 5 倍。**

**为什么这条对我们特别值钱**：我们的整套 setup 就是 **Claude Code（客户端）→
`ccgs-cn-config` 桥（8787）→ 上财远程模型**。也就是说 **我们一直在付 harness tax，
但从没量过它**。作者给了**能在自己机器上跑的量法**：

```bash
# 从你实际工作的仓库里跑，量"读完你的 prompt 之前就载入了多少"
claude -p "Reply with the single word: ok" --output-format json \
  | jq '.usage.input_tokens + .cache_creation_input_tokens + .cache_read_input_tokens'

# 再拆开：多少来自配置、多少来自内置工具定义
claude -p "Reply with the single word: ok" --output-format json \
  --strict-mcp-config --disable-slash-commands --setting-sources project \
  | jq '.usage | .input_tokens + .cache_creation_input_tokens + .cache_read_input_tokens'
# 加 --tools "Bash,Read,Edit,Write" 只留四个工具；加 --tools "" 一个不留
```

作者机器上的实测：**空目录 30,271 令牌** → 去掉配置 18,809 →
只留 4 工具 **5,295** → 不留工具 2,441。
**"配置"占 11,462，"内置工具定义"占 16,368（占去配置后的 87%）。**

> **⚠️ 本辑没能实测成**：我们的桥当前**没在跑**（`127.0.0.1:8787` 无响应），
> 且本沙箱里 `claude` CLI 跑不起来（`claude.cmd` 内部调 `reg.exe` 被拦），
> 工具起的后台进程也不持久。**量法已记下，列为下一轮待办。**
> 好消息是我们那个桥是**薄翻译层**（112 行，只做 `/v1/messages` 转发 + 注入
> `thinking:disabled`，不自己加系统提示词），所以**tax 大概率全在客户端那一侧**。

### ★ 2. 多 agent 并行的边际收益**已经转负**：有人烧掉 $20,000

[AI 日报 2026-09-18](http://quidproquo.cc/posts/daily/2026-09-18-ai-agent-daily) 同一天两条**对立**信号：

- Anthropic：Claude Code Projects 做成"多云端 session 并行 + 跨 thread 共享记忆"
- OpenAI Codex 工程师 **Eric Provencher 公开警告**：**并行 sub-agent 超过两个只增加"协调税"**；
  有人用 **1,393 个 agent** 重构单个 Python 文件，**烧掉 $20,000**

**用法**：这条**直接给我们的单 agent 串行路线松了绑**。"agent 越多越好"至少在 2026-09
已经不再成立 —— 它和 §1 的 harness tax 是**同一个道理的两面**：**组织成本会吃掉规模收益**。

### ★ 3. 「规则要能被测」有了现成工具（本辑已落地）

见第七节与 `agent-house-rules.md` **房规 #33**。来源：
[`JakeSelby/agent-harness`](https://github.com/JakeSelby/agent-harness)（15★ · MIT · 已立卡 [1080]）
—— 每条规则要么配**确定性检测器**，要么写明"为什么判定不了"，否则 lint 直接失败；
`harness usage --rules` 报每条规则**触发几次**。它自曝**用这套抓出自己两个"上线了但什么都没做"的功能**。

### 4. 本地化 / 离线编码 agent 的**具体配置**

- [Codex 实战工作流（CSDN）](https://blog.csdn.net/weixin_29067143/article/details/166024856)：
  写 `~/.codex/config.yaml` 把 `base_url` 指向 Ollama `http://localhost:11434` / vLLM，
  **可跳过 `codex login` 纯离线跑**。→ **这条与我们本地 Ollama 路线直接对齐，第 11 轮前最该试。**
- [本地 diff 自动审查（CSDN）](https://blog.csdn.net/weixin_33521678/article/details/165954002)：
  `LocalLLMAgent` 类 + `ollama serve`，附完整可跑代码。原文用 `llama3:70b`（我们 16GB 跑不动），
  **换 `qwen3:8b` 量级即可复刻**，给 `check_*.py` 补一层"语义级"审查。
- [datapipesoft AI progress 09-20](https://datapipesoft.com/ai-progress-2026-09-20)：
  ① DeepSeek 发 **V4.1-Flash 的 KV-cache 压缩论文**；② **Claude Code v2.1.275-278 起
  无 `CLAUDE.md` 时回退读 `AGENTS.md`** → 跨工具约定**收敛为一份**；
  ③ [`tigerless-labs/agent-memory`](https://github.com/tigerless-labs/agent-memory)（约 950★）：
  **以纯 Markdown 为真相源**的长期记忆运行时，Claude Code 与 Codex 共享一份 ——
  **"可 diff、可 commit 的记忆"比向量库式记忆好维护得多**，值得实测。

### 5. 开源透明 vs 权限失控（同一天两件事）

[夜雨聆风 AI 日报 2026-09-19](https://www.yeyulingfeng.com/a/1038686.html)：

- **MiniMax 09-18 晚以 MIT 开源 MiniMax Code CLI**（终端级编码 agent，支持 BYOK / Plan Mode /
  子代理 / MCP）→ **新的可审计候选**
- **智谱 ZCode 被开发者逆向发现**：静默打包**整个工作区（含完整 `.git` 历史）**
  加密上传阿里云 OSS，官方致歉并承诺开源客户端 → **ZCode 的风险第二次坐实**
  （第九辑已记过一次"逆向风险"）。对应房规 **#24 指纹化验证**。

### 6. 其余（查阅型，不单独立项）

- [阿里云《AI 智能体的开发流程》](https://developer.aliyun.com/article/1764957)：
  提示词/工具/知识库/编排 + **评估（LLM-as-a-Judge、领域测试集）** + 安全护栏。
  它的"评测"一节可对照我们"闸门 = 评测"的定位。
- [阿里云《AI 原生研发组织的探索和实践》](https://developer.aliyun.com/article/1764752)：
  大厂自述"代码审查从通用规则走向专家级判断""代码自动修复的 Loop 工程""评测数据生产线"
  → **大厂也开始把"审查"当瓶颈**，正面印证第十五辑主线。
- [掘金《用 AI 写代码别只甩一句指令》](https://juejin.cn/post/7687855879103250484)：
  五步工作流 + 一份写给 AI 看的 `AGENTS.md`（一次 commit 一条功能 / 跑通 test+build 才算完成 /
  技术栈禁止擅改 / **明确列出"不做的范围"**）→ **"不做的范围"这一节我们房规里没有，值得补**。
- [HN: Local-coder](https://hn.rohankhatua.dev/item/49785853)：Ollama + OpenCode 编排器，
  `Explorer→Planner→Coder→Verifier→Reviewer`，**起因是"agent 说改了文件其实没改"** ——
  **这个失败模式我们同样会撞**，它的独立 Verifier 可直接借用。
- 留档：[`Forcefield`](https://news.ycombinator.com/item?id=49755908)（Go 写的本地优先 harness，
  低开销无遥测）、`ENZO`（Apache-2.0 自托管，300+ 模型 / 9 家 provider）。
- [GitHub 周榜（CSDN 09-14）](https://blog.csdn.net/nmy_2360/article/details/165288312) 里的
  [`EverettFish/holo-card-studio`](https://github.com/EverettFish/holo-card-studio)（**1,753★ · Python**）：
  一句话生成可编辑的 Blender 全息卡 + Three.js 交互页。**形态值得抄** ——
  **"技能本体只有代码和文字，生成物留在用户项目里"**，正是我们分发的正确姿势。

---

## 三、模型对比（本辑新开的一组 · 10 条）

> **为什么现在单列一组**：本辑的模型侧第一次出现"**同一天、两家、四个模型**"，
> 而且**竞争焦点从"参数纪录"转到了"单位经济性"**。这直接影响我们的选型约定。

### ★ 1. 09-22 同日对撞：Opus 5.5 vs GPT-6 Sol / Luna —— 打的是价格

[财联社 / 网易 2026-09-23](https://www.163.com/dy/article/L7G514VD05198CJN.html) ·
[saascity 详解](https://saascity.io/blog/gpt-6-sol-luna-claude-opus-5-5-september-2026) ·
[aiseoroundtable](https://aiseoroundtable.com/openai-anthropic-cheaper-models-price-war)

| 模型 | 定位 | 每百万 token（输入 / 输出） | 相对谁 |
|---|---|---|---|
| **Claude Opus 5.5** | Fable 级执行力的商用档 | **$4 / $20** | 比 Opus 5（$5/$25）**降价 20%**，典型负载成本 **-40%**，**快 30%+** |
| **GPT-6 Sol** | 大型工作马（多文件代码 / agent 循环） | **$2 / $10** | 比 GPT-5.6 Sol 促销价**再降 50%** |
| **GPT-6 Luna** | 高吞吐（分类 / 抽取 / 结构化解析） | **$0.10 / $0.50** | 目前最便宜的可用档 |

- 两家都在 09-22 **同日**发布，且**未互相给出 head-to-head**（Anthropic 拿 Opus 5.5 对 GPT-6 Astra
  与 GPT-5.6 Sol；OpenAI 拿 Sol/Luna 对 Opus 5 与 Fable 5）
- 独立评测 [Artificial Analysis](https://felloai.com/best-ai-of-2026)：**Opus 5.5 在 Intelligence Index
  拿到 57.6 的史上最高分**，10 个评测类目里领先 6 个；CursorBench 上比 GPT-5.6 Sol 高 11 分、
  成本约其三分之一
- **叙事变化**：两家 CEO 前几天还在公开呼吁"给前沿降温"，**转头就在价格上贴身肉搏**
  → 一位经济学家的评论是：这**可能同时压缩两家的盈利能力**，意味着**还会有下一轮降价**

**对我们的用法**：**新模型不需要追，但降价需要跟。** 我们的选型表（Qwen3-Max 管创意 /
DeepSeek 管代码 / 本地 Ollama 管离线）里，**价格一档的变动才值得动手**。

### ★ 2. "周抛时代"：最强模型的保质期撑不过一周

[今日头条 / 蓝鲸 2026-09-15](https://www.toutiao.com/article/7685663654603162147)：
9 月**前 4 天 4 家海外巨头连发**（Claude Fable 5.1 & Mythos 5.1 / Gemini 3.8 Flash + Cyber /
Muse Spark 1.3 / GPT-6 Astra），国内 Qwen3.8-Flash、GLM-5.3-Flash、混元 Hy4 preview 同期。
归因：**RSI 递归自我改进 + 训练流水线化**。

**→ 这是我们"不必追新"的最佳论据**：把"换模型"的门槛写成两条硬判据 ——
**① 成本显著下降 ② 突然能做以前做不到的事**；其余情况不动。
（本作 v1.9 的语音就是照这条走的：Kokoro 本地跑得动、成本为零，所以不换。）

### 3. 国产 9 月开源潮 + 一条硬数据

[中培伟业](https://www.zpedu.com/it/ai/44597.html)：
9-3 腾讯 **混元 Hy4 preview**（Apache-2.0，**770B 总参 / 49B 激活 / 1M 上下文**）、
9-3 智谱 **GLM-5.3-Flash**（MIT，320B，**可国产芯片全链路**）、9-8 面壁 **MiniCPM5-2B**。
**最硬的一条横评证据**：**OpenRouter 上开源模型处理的 token 占比，从 1 月 34% 升到 6 月 65%**。

### 4. DeepSeek V4.1-Flash 的分时定价（直接影响我们的翻译成本表）

[AI Magazine 09-16 核价](https://ai-magazine.com/deepseek-v4-1-flash-release-pricing-v4-pro-stays)：
V4.1-Flash（**552B MoE，输入激活 8B / 输出 16B，1M 上下文，384K 输出**）：

| 档 | 输入（缓存命中 / 未命中） | 输出 |
|---|---|---|
| **闲时** | **$0.003 / $0.15** | **$0.60** |
| **峰时** | $0.006 / $0.30 | $1.20 |

另：**9-14 原定下架 V4 Pro 被官方反转保留**。
→ **缓存命中 $0.003 那一档，直接决定"整批初翻跑一遍再人工校对"到底划不划算。**

### 5. Google 语音双发：3.8 Live + **3.5 Transcribe**

[Yahoo Tech 09-18](https://tech.yahoo.com/ai/gemini/articles/google-launches-voice-ai-models-160050996.html)：
**Gemini 3.8 Live**（$0.005/分钟音频输入，$0.018/分钟输出，**97 语言中途切换**，音频会话 15 分钟）
+ **Gemini 3.5 Transcribe**（**85 语言**，流式 WER ~4% / 非流式 ~2.6%，
**带说话人分离与词级时间戳**），**全部输出带 SynthID 水印**。

**→ 三条新信息里，最要紧的是 SynthID**：**云端 TTS 会有可检出水印，本地模型没有这个问题。**
这给"本作坚持本地 Kokoro 配音"又多了一条理由（除成本与隐私外）。

### 6. 榜单与聚合源（本辑新增的"查数据的地方"）

| 源 | 用途 |
|---|---|
| [Artificial Analysis](https://felloai.com/best-ai-of-2026)（月度更新） | 按**实测分数**排名，模型一出分就换榜首，不等投票榜 |
| [neuralstack 9 月发布甘特图](https://www.neuralstack.network/article/2026-09-21-ai-model-release-timeline-gpt-6-astra-claude-fable-gemini) | 密集发布期的**时间线索引** |
| [**liyupi/ai-model-world**](https://github.com/liyupi/ai-model-world)（171★，已立卡 [1081]） | 中文可视化，**556 个模型拟人化**；数据源 Epoch AI / models.dev / LiveBench / HuggingFace |

> 另记一条**选型信号**：小米 **MiMo-V2.6-Pro**（09-21，**纯 MIT**）在 Intelligence Index 拿 46.3，
> 跑一次 index 任务仅 **$0.13**（该榜最便宜）——**开源权重的性价比档还在快速下探**。

---

## 四、游戏制作与拓展（14 条）

### ★ 1. 本辑对"要不要公开用 AI"最有用的一条：Godot 社区调研

[Ziva 官方博客 2026-09-19](https://ziva.sh/blogs/use-claude-or-chatgpt-with-godot) 首次公开
**Godot 社区 2026 调研（11,195 人）**：

| 用法 | 占比 |
|---|---|
| 聊天式求助 | **42.6%** |
| agentic coding | **17.9%** |
| MCP | **4.9%** |
| **明确"不用 AI 且反对"** | **33.6%** |

**→ 33.6% 这个反对率是"发行时是否公开 AI 使用"的决策输入**：用 AI 的人不少，
但**明确反对的也占三分之一** —— 与第十二辑 Ramen Aura 访谈（"单人剧情玩家最反感 AI"）
方向一致，再次确认本作**只能走披露而非隐藏**。

它另给了**两条可直接改脚本名的命令**（虽是 Godot，思路通用）：
`godot --headless --path . --check-only --script res://player.gd`（纯语法检查）
与 `godot --headless --path . --quit-after 60`（**真跑主场景**）。
**"打包/启动前先做一次纯静态检查 + 真跑主场景"这两级，正是我们 `check_release.py` 缺的那一环。**

### ★ 2. AI 披露的两种正确/错误样本

- **对的样本**：[《Decide Your Fate》](https://gameagent.icu/posts/decide-your-fate-steam-horror)
  （09-16 上 Steam，盲眼杀手听音潜行）—— 商店页**主动披露"开发过程中曾使用 AI 工具辅助编码与文本撰写，
  所有内容均经开发者审核调整"**，并**照常说明玩法与适龄提示**。这是披露的**正确姿势**：
  **把披露当成商店页的一部分，而不是藏在小字里。**
- **薄的样本**：Hard Shark 的 29 款（见第一节）—— **只标胶囊图**。
- **有趣的样本**：[《时代：明末》](https://gameagent.icu/posts/era-late-ming-steam-launch)
  （09-16 上 Steam，**国区免费**）：**以自然语言指令推动剧情**的明末题材文本游戏，
  **开发者公开代码仓库支持二次创作**。→ 这是**我们所在品类（文本/叙事）**里
  "AI 创作 + 开源共创 + 免费"的一种活法，值得跟踪它后续怎么迭代。

### 3. "AI 声称改了 vs 实际改了"——这条工序我们没有

[Fate Tracker（Windows 本地 App，$49 买断无云）](https://www.newsoftoday.com/138084283/fate-tracker-releases-build-memory-for-vibe-coded-games-a-local-windows-app-with-verified-recovery)：
给 AI 做的游戏记 **"为什么这一版能跑"** —— 记录人的决策、**AI 声称改了什么 vs 磁盘实际改了什么
（SHA-256 比对）**、以及**已验证可还原**的快照；支持 Unity/Godot/Unreal/GameMaker/Defold/RPG Maker。

**→ 我们有 `mistakes/` + git，但"AI 声称改了 vs 实际改了"的哈希比对这道工序没有。**
它把"手感验证"和"**AI 谎报改动**"两件事都变成可还原记录 —— 与 §二.6 的 Local-coder Verifier 同源。**值得抄。**

### 4. AI 让"高同源度复刻"变便宜之后，争议点前移了

[搜狐：AI 复刻风波（土豆削皮游戏）](https://www.sohu.com/a/1079270953_122066679)：
《1,000,000 Potatoes》作者在 X **逐帧对比**《PotatoPlease》，指控"Ctrl+C/V + AI 渲染 + 上架"。
**→ 争议点已从"素材版权"前移到"整体视觉语言"**。Ren'Py 项目抄的是**对白与演出结构** ——
这条**直接影响我们第 5 轮文风自查的思路**：要防的不只是"抄了张图"，而是"演出手法整体像"。

### 5. Godot MCP 的**百分比收益**（本辑唯一给出数字的中文实测）

[今日头条 2026-09-16](https://www.toutiao.com/article/7685854263662166557)：
写码省 **30%–50%**，从零到可玩 Demo 由"几周压到几天"，**前提是需求必须极清楚**；
**多 agent 模式在 5000 行以上才划算**。
→ 这是"要不要上 MCP"的取舍依据（**我们的结论仍是：不需要**，本作已明确决定不用 MCP）。

### 6. 其余（同向复述或降权）

- [CSDN：Godot MCP 协议 + SKILL 编排](https://blog.csdn.net/weixin_29011395/article/details/165504977)：
  "感知—决策—执行—验证"闭环，强调**校验必须是可执行动作**（真读场景树，不能"脑子里检查"）
  → **本辑对闸门设计最有价值的一条**，正是 `check_*.py` 的原则。
- [CSDN：弹幕游戏单人 6 款、总流水 2000 万、开发者只拿 8%](https://blog.csdn.net/caelus_mv/article/details/166235891)：
  美术 AI 承担 70%、**单款成本 1000–1500 元、周期 15 天**。
  → **反面参照**：AI 把制作成本压到近 0 后，**利润全被渠道议价吃掉** ——
  提醒我们**发行/分发才是瓶颈**（与第十五辑 #17"谁来分发"同向，但这条给了具体分成数字）。
- [CSDN：一个人用 AI 开发微信小游戏](https://blog.csdn.net/weixin_42659252/article/details/166166057)：
  平台特有坑（微信运行时无 DOM）+ "把 AI 当结对搭档、人只做意图与验收"的分工描述。
- [clawdbytes: Making Games with OpenCode](https://clawdbytes.com/article/2026-09-22-making-games-with-open-code.html)：
  用终端 agent 做游戏开发流程。**流量极低、内容单薄**，只当"终端 agent 也能做游戏"的旁证。
- [AGI Hunt：Unity 动态天气系统 99% 代码由 Claude 写](https://agihunt.info/en/p/1a0a29d3fafd050404d54f27f01)：
  开发者 Arkitech-RG 的 GRIMLIFE（昼夜/天气/植被联动），**且反过来在引擎里自建调试工具**。
  → **"让 AI 写系统 + 让 AI 顺手写好调试工具"**这个组合拳比"写功能"更值钱。
- [SoonLab：Godot 侧 AI 三类对比](https://www.soonlab.ai/blog/best-ai-agents-for-godot)：
  核心判据是"能不能做**可复查的受控改动**" → **我们房规缺的正是"改动可复查"这一条成文规则。**
- [Pocket Chief! 上 Steam（App ID 4946240）](https://gameagent.icu/posts/pocket-chief-steam-launch)：
  桌宠式效率工具，**AI 走自建云、可接自己的模型端点** →
  "官方云 + 允许 BYO 本地端点"的商业化形态参考。
- [Sorceress: Decode What Is Vibe Coding](https://sorceress.games/blog/decode-what-is-vibe-coding-games-2026)：
  vibe coding 与手写的**责任边界表**。**厂商内容，降权看。**

---

## 五、开源 TTS：上一辑留下的缺口，本辑基本闭合（6 条）

**为什么单独成组**：第十一辑起就一直挂着"第 11 轮配音要不要换模型"这个问题，
候选一直悬空。**这一组把它填上了。**

| 方案 | 关键规格 | 对我们 |
|---|---|---|
| [**腾讯混元 AuK**](https://github.com/Tencent-Hunyuan/AuK) | **1,228★ · MIT**（09-22 推送） | **最强候选**：**一句话改台词 / 调情绪 / 克隆音色 / 降噪是同一个模型**，Base + Flash 两档，**Python API + CLI + Gradio + ComfyUI 节点**，可本地部署、含微调代码，主打中英。**"改几个字不重录整段"正是第 6 轮最缺的能力** |
| [**面壁 VoxCPM2**](https://github.com/OpenBMB/VoxCPM) | **37,898★ · Apache-2.0** | **参数 2B、底座 MiniCPM-4、tokenizer-free 扩散自回归**（直接生成连续音频，不走"切 token 再拼"），输出 **48kHz**（16kHz 参考音频内部超分），**30 语种**，**纯文字描述造新音色**（"30 岁女性、语速慢、语气温柔"）+ 参考音频克隆 + 风格指令。**"不靠参考音频造音色"是第 6 轮完全没有的能力**，正好解决"女声带电音只能按高频能量挑音色"那个痛点 |
| [Fish Speech / OpenAudio](https://aibars.net/zh/projects/722415997151219712) | **32,793★**（09-16 推送） | 无音素依赖、10–30 秒零样本克隆、PyQt6 + Gradio 双界面。**⚠️ 代码 Apache 但权重 CC-BY-NC-SA（非商用）** —— **做商业版配音时权重协议是红线** |
| [CosyVoice 3.0](http://www.lnrq.cn/news/4258) | Qwen2.5-0.5B 骨干，**5–60 秒零样本克隆**，11 语种，4090 实时比 ~4.2x，需下载约 5GB | 第七辑起就记着的"要做情绪演出就得换模型"的候选 |
| [GPT-SoVITS v4](https://blog.csdn.net/gitblog_00931/article/details/155045757) | **v4 原生输出 48kHz**（v3 是 24k）；5 秒零样本 / 1 分钟微调；RTF：**4090 = 0.014 / 4060Ti = 0.028 / M4 CPU = 0.526** | **注意 CPU 那档 0.526 = 慢一倍多但跑得动**，对我们的无独显机器是唯一可行的重档 |
| [7 款 AI 配音横评](http://www.lnrq.cn/news/4258) | Fish Speech S1-mini（0.5B 蒸馏）/ CosyVoice 3.0 / Azure / Google / Amazon | 选型时可以对着看 |

> **结论（对第 11 轮的直接影响）**：**帕姆配音不必再换模型** ——
> 现有 Kokoro 本地链路（103 音色、159 句已落地）先配完；**但要"改几个字不重录"或"调情绪"，
> 首选 `AuK`（MIT）与 `VoxCPM2`（Apache-2.0）**，两者权重协议都允许商用（Fish Speech 不行）。

---

## 六、GitHub 那一路（19 查询 / 268 候选 → 6 张立卡）

**这一路的结论本身就是一个数据点**：268 条原始候选里，
**只有 3 条已在索引**（说明索引没漏），而**筛掉的最多的一类是"同一件事的第 N 个实现"**。

### 剔除记录（如实登记，免得下次重复找）

| 剔除项 | 原因 |
|---|---|
| `ueboxai/uebox` / `XuanwnOvO/DroidSpy` | 第七辑已收 |
| `wilsjo2/OptiScaler-DLSSNR-PreSR-Multipass` | 第十三辑已收 |
| `bebabinlarsson-blip/Godot-MCP` | 第七/十一/十五辑已收 |
| **14 个 `*-dev.github.io` 同模板站** | `gpt-5-6-dev` / `kimi-api-dev` / `flux-3-dev` / `kilo-code-dev` / `siliconflow-dev` / `arc-ads` / `rork-ai` / `kling-api` / `tapnow-dev` / `runway-api` / `gemini-code-assist-dev`… **2026-09-21/22 批量创建、各约 10★、文案结构完全一致**（"…review from outside the company"）→ **SEO 内容农场，不收录**（M-0002） |

### 立卡 6 张（第二十二版增补，脚注 [1079]–[1084]）

| 仓库 | ★ | 协议 | 为什么立卡 |
|---|---|---|---|
| [**ikermoel/open-alternative-jev**](https://github.com/ikermoel/open-alternative-jev) | 51 | Apache-2.0 | 把 System 1 决策**搬回本地**（不改模型、只改调用方式）；**⚠️ 文档写 `pip install`，PyPI 实测 404** → M-0016 |
| [**JakeSelby/agent-harness**](https://github.com/JakeSelby/agent-harness) | 15 | MIT | **让每条规则能被测**（本辑已吸收为房规 #33） |
| [**liyupi/ai-model-world**](https://github.com/liyupi/ai-model-world) | 171 | MIT | 中文模型对比可视化（556 个模型），数据源值得记 |
| [**26048608982lp-ai/gamenumerics**](https://github.com/26048608982lp-ai/gamenumerics) | 0 | MIT | **游戏数值的确定性引擎**（17 工具 MCP：xlsx 导入 / 审曲线 / 战斗与抽卡模拟） |
| [**sayic/game-apk-reverse-engineering**](https://github.com/sayic/game-apk-reverse-engineering) | 9 | 无 | 把手游 APK 逆向写成**AI 能照着跑的清单**（与你的解包强项对口） |
| [**envy-ai/sprite-generator**](https://github.com/envy-ai/sprite-generator) | 0 | AGPL-3.0 | **四方向**角色精灵图生成（ComfyUI），"四方向"这个最小可用集很实用 |

### 其余候选（以链接留在本表，不进索引 —— 索引容量不该被"顺手看到的"占满）

| 仓库 | ★ | 一句话 |
|---|---|---|
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | **6,393** | Z.ai 官方编码 agent harness（**Apache-2.0**）—— 但见 §二.5 的静默上传争议 |
| [unreallabsai/unreal-agent](https://github.com/unreallabsai/unreal-agent) | **1,218** | "async-first agent harness"（Go / MIT），**一天起量** |
| [ruc-datalab/EvoOntology](https://github.com/ruc-datalab/EvoOntology) | 351 | 为 Claude Code / Codex 建"自进化本体层" |
| [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) · [NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) | 560 / 206 | **同名两个仓库、同一周出生** —— 同题海啸的又一例 |
| [Continuum-AI-Corp/OrcaPromptVault](https://github.com/Continuum-AI-Corp/OrcaPromptVault) | 25 | 系统提示词 / 工具 schema / harness 的**版本化可验证归档** |
| [vizuh/sabi](https://github.com/vizuh/sabi) | 15 | 按轮次做**模型 / effort / provider 路由**的推理调度 |
| [tallslab/threeforge](https://github.com/tallslab/threeforge) | 15 | three.js 游戏的**帧预算编译器 + 诊断**（含 MCP） |
| [wilsjo2/OptiScaler…](https://github.com/wilsjo2/OptiScaler-DLSSNR-PreSR-Multipass) | 677 | NVIDIA AI 改光照/细节/色彩的游戏 mod（**已在索引**） |
| [buddy/minesweeper](https://github.com/buddy/minesweeper) | 17 | 扫雷 LLM agent 跑分（一板、九模型并行、一钟） |
| [AmigaMeow/llm-leaderboard-data](https://github.com/AmigaMeow/llm-leaderboard-data) | 4 | **每日自动更新**的模型榜（LMArena + OpenRouter，5 个维度） |
| [xiongxingzhe/wishlistdoc-mcp](https://github.com/xiongxingzhe/wishlistdoc-mcp) | 0 | Steam 商店审计 / 销量锥形预测 / 独立游戏基准（**Steam 上架工具这一格仍很空**） |
| [iaramxs/AnyWorld](https://github.com/iaramxs/AnyWorld) · [lovetimo0421/yumina-oss](https://github.com/lovetimo0421/yumina-oss) | 12 / 5 | AI 当地下城主 / AI 原生互动小说世界引擎 |
| [meitipro1/questline](https://github.com/meitipro1/questline) | 0 | **模型负责叙述、合约负责判定**，每次掷骰都能被任何人从公开数据复算 |
| [zwsss152/rainy-night-ai-npc](https://github.com/zwsss152/rainy-night-ai-npc) | 0 | 中文 AI 叙事解谜 Demo（Three.js + FastAPI + LLM，独立角色记忆 + 剧情状态校验） |
| [adrian-wulf/gamewache](https://github.com/adrian-wulf/gamewache) | 0 | GameOps：崩溃哨兵 + **确定性黑盒回放** |

---

## 七、这一辑里"立刻能做"的三件事

1. **把 `no-ai-slop` 的 20 条模式与我们的 `check_dialogue.py` 做差集**（来自 §一.2）——
   我们缺的可能不是"再写一条规则"，而是"找出现有六条漏了哪些形态"。
   **注意保底口径**：它对"NPC 说套话是设定"无能为力，差集结果要人工过一遍再进闸门。
2. **量一次我们自己的 harness tax**（来自 §二.1）—— 命令已记在 §二.1，
   等桥能跑起来时执行；**先估**：我们的桥是 112 行薄翻译层，tax 应在客户端侧。
3. **第 11 轮（帕姆配音）开工前，先读 `AuK` 与 `VoxCPM2` 的 README**（来自 §五）——
   两者的权重协议都允许商用（Fish Speech 不行）；**重点是确认"改几个字不重录"怎么调**。

---

## 收录统计

| 类别 | 本辑新增 | 累计 |
|---|---|---|
| 中文社区经验帖 | **约 17 条** | 约 445 条 |
| 大模型官方 / 英文社区 / 聚合站 | **约 28 条** | 约 456 条 |
| GitHub 项目（候选 / 立卡） | **268 条候选 → 21 条值得记 → 6 张立卡** | **1085 项** |

**查重说明**：本辑中文 17 条、英文/官方 28 条的 URL / 文章 ID / 作者名 / 标题关键词，
逐个在前十五辑存档（`csdn-social-summary-v2…v15.md`）与 `index.html`（1079 项）里 grep 过。
GitHub 那 268 条候选**先自动去重（对照 index.html）再人工过**，
另做了一次**内容级查重**（不只比 URL，还比"这件事本身"）。

**⚠️ 本辑查重抓到的一个新形态（记下来免得下次再犯）**：
有几条**文章 ID 是新的、但内容与旧辑重复** —— 例如"GPT-6 Astra 种土豆"（新 ID，内容在第十辑）、
"The Archipelago"（v6/v14 已收）、"vibe coding 13 天"（v7/v8 已收）。
**"ID 新"不等于"内容新"** —— 查重必须**同时**比 URL 和**叙事主体**。
（这也是 M-0001 的第三次形态变化。）

**⚠️ 流程教训（承接第十五辑，这次做对了）**：派调研 Agent 时**给全了路径**
`D:\34498\Documents\github-projects-invest-games\`；Agent 回报中已明确写出
"已逐条 grep 过 v2–v15 存档与 index.html"并列出**已剔除的 16 项重复**。
**上一辑漏路径的坑没有重演。**

---

*本辑归档：`csdn-social-summary-v15.md`（第十五辑全量）*
*下一辑搜索缺口见文末"仍未闭合"两处 —— ① 面向"角色对白"的 AI 味检测 ② 活跃的开源 Steam 上架/发行工具*
