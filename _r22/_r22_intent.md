# 第二十二辑 · 三路共享意图文件（Foremerge 最小版首次实操）

> 目的：**开工前先写"我要查什么"，收工前先读**，压掉"两路查同一件事 / 两路同时 429"。
> 规则：① 只在自己的区块下追加，不删别人的字；② 开工前先读全文件，见到别人已声明的关键词 → 自己不查；
> ③ 收工前再读一次，确认自己没有和别人条目重复；④ 重复了不要偷偷删，写在"交叉"区说明。

## 本辑去重基线（三路共同）

- `index.html`（**1128 项**，1127 为最大脚注号 +1）
- `csdn-social-summary.md`（第二十一辑，约 741 条）+ `csdn-social-summary-v19.md` / `v20.md` / `v21.md`
- 上一辑原始产出 `_r21/*.md`；本辑另两路产出 `_r22/*.md`

## 分工（不重叠原则）

| 路 | 自己的地盘 | 明确不碰 |
|---|---|---|
| gh | GitHub / Gitee / HF 仓库、release、工具链代码 | 中文博客、厂商官网新闻页 |
| cn | CSDN / 掘金 / 知乎 / 公众号 / 少数派 / 机器之心 / 独游魔盒 / 腾讯 IMA | GitHub 仓库盘点、英文社区 |
| official | 厂商官网 + release notes、VS Code/Copilot/Cursor/JetBrains、HN / r/LocalLLaMA / DEV / note.com、AA / OpenRouter 榜单 | 中文博客站、GitHub 仓库盘点 |

## 中文侧独有的高冲突地带（历史重复源，重点防）

`hqwc.cn` / `mhpn.cn`（SEO 镜像站，见到即怀疑同源）· `weixin_29xxxxx` / `weixin_34xxxxx`
（同日同题材内容农场）· CSDN 数字 ID 换号复现旧内容 · 掘金"源码实战"系列会与 GitHub 侧撞车
（**源码解析帖归 cn，仓库本体归 gh**）

---

## gh 路声明（开工时间：2026-09-24 08:40）

**本辑 gh 路要查的关键词（一行一个，开工先声明）：**
1. renpy AI plugin / renpy llm
2. ai agent harness framework
3. context compression compaction LLM
4. agent memory MCP server
5. memory consolidation knowledge graph agent
6. vscode extension AI coding
7. vibe coding security scanner
8. local LLM inference ollama benchmark
9. LLM evaluation harness benchmark
10. deepseek harness DSH

**不查（归 cn）**：CSDN/掘金/知乎/公众号 源码解析帖
**不查（归 official）**：厂商官网 news / release notes / HN / r/LocalLLaMA

## cn 路声明（开工时间：2026-09-24）

- DeepSeek Harness 源码实战 第16章（怕浪猫系列收尾）
- DSH 深入理解 系列 009/010/011/013
- 花叔 橙皮书 DSH 从开机到拆开 一手源
- Claude Code 上下文管理 压缩 实战
- Codex CLI 使用 实战 中文
- memory 记忆管理 遗忘 冲突 中文 2026
- vibe coding 翻车 生产事故 复盘
- Ren'Py 视觉小说 AI 工作流 2026
- 独立游戏 发行 Steam 愿望单 复盘
- 模型测评 国产 GLM Kimi Qwen 2026-09


## official 路声明（开工时间：2026-09-24 15:35）

关键词（一行一个）：
- Anthropic Claude Code release notes / changelog
- Anthropic context editing / memory tool
- OpenAI Codex changelog
- Google Gemini DeepMind release
- DeepSeek DSH harness / DeepSeek release notes
- Qwen 通义 / GLM 智谱 / Kimi 月之暗面 / Doubao 豆包 / MiniMax 官方
- VS Code release notes / GitHub Copilot changelog
- Cursor changelog / JetBrains Copilot / Windsurf / Zed
- Hacker News AI coding / r/LocalLLaMA
- Artificial Analysis / LMArena / SWE-bench / OpenRouter / Epoch AI
- Unity Unreal Godot AI policy / Ren'Py AI
- vibe coding 官方政策

## 交叉区（收工前填：谁和谁撞了、怎么处理）

> cn 路收工时间：2026-09-24

> gh 路收工时间：2026-09-24 16:10

> official 路收工时间：2026-09-24 16:40

- **gh 路只写仓库本体，未复述任何博客机制**：本轮 28 条正式条目全部是 GitHub 仓库，`gh api` 核实，未引用 cn/official 的站外解读。与 cn 路 `## 交叉区` 第一条约定一致（DSH 仓库归 gh、机制帖归 cn；我未收任何 chino/花叔内容）。
- **DSH 生态区**：我收的全是**插件/仓库**（dsh-vision-router、DSH-X、billion-context-dsh、dsh-commandcode-provider）。cn 声明"收到 DSH 源码解析帖"、official 声明"收 DeepSeek DSH release notes"——三者实体不同（仓库 / 博客 / 发布说明），**无重复计条**；但同一 DSH 话题下会同时出现，请 team-lead 在合并时按"仓库/博客/官方"三分栏摆放。
- **OpenCursor（PawanOsman）**：official 路地盘含 "Cursor changelog / JetBrains / Zed"，但 OpenCursor 是**第三方开源 VS Code 扩展仓库**，非厂商 changelog，归 gh 无冲突。
- **vibe coding 安全**：我收两条**扫描器仓库**（vibescan、vibeship-scanner）；cn 收的是"翻车复盘帖"、official 若有"官方政策"——三者层级不同，不重复。
- **小模型/本地推理**：little-coder、ollama-benchmark 等归 gh；official 侧 Artificial Analysis / LMArena 榜单是**评测结论**，我这边是**评测工具仓库**，不冲突。

- **DSH 源码/文档**：cn 只收"源码解析帖"（腾讯技术工程 chino 拆解 → 我已收，URL `163.com/dy/article/L4AHS9B70518R7MO.html`）。**仓库本体（`deepseek-ai/deepseek-harness`）与 release/星数归 gh 路**。若 gh 路也要写 DSH，请只写仓库，不要复述 chino 那篇的机制细节；我这边也不收仓库。
- **DSH 英文侧**：`beri.net/learning/deepseek-harness-docs`、`developersdigest.tech/.../deepseek-harness-dsh-first-look` 两篇是**英文站**，按分工**归 official 路**（我读到但未收，若 official 已收，请注意它们含 `~218k stars / ~26k forks`、`CVE-2026-82533 (CVSS 9.4, 0.1.2-alpha.1 修复)` 等英文侧独有数字）。
- **模型上新**：DeepSeek V4.1 Flash（2026-09-10）我收的是**中文媒体转述**（湖南日报/腾讯新闻）。**厂商官网与 release notes 归 official 路**；若 official 也收了同名发布，请只保留官方口径，我的中文媒体条只作**中文侧资讯**登记，避免重复计条。GLM-5.3 同理（我收太平洋科技，非官网）。
- **vibe coding 安全**：`80aj.com`（转 Linux.do）与 r21 §5.x 的 TrustFall/MCP 投毒**不同源**，我这条是"架构选型翻车"（JSON 当数据库），非供应链攻击，**未与 r21 撞车**。
- **cue 显式提醒 team-lead**：r21 曾把 `Muse Spark / GPT-6 Astra / Fable 5` 判为"虚构"，本辑已用**南方周末 + 太平洋科技 + IMA** 三处证实为真，**该判定被推翻**，请在下一辑基线与判真伪规则里更正（详见 `_r22_cn.md` §8.3）。


---

### official 路对「交叉区」的补充（收工 2026-09-24 16:40）

- **DSH 三方实体确认（与 gh/cn 无重复计条）**：gh 收**仓库本体**（`deepseek-ai/deepseek-harness` 版本/星数/插件），cn 收**源码解析帖**（腾讯技术工程 chino 等），我收 **release notes 的机制变化**（`v0.1.6-alpha.1` 的 headless 会话续期 / SSH 远程工作区 / PTC 移出主进程）。**我已按 gh 的提醒，不复述 cn 那篇的源码细节，只写官方发布说明的行为契约**。合并时建议按 仓库 / 博客 / 官方发布说明 **三分栏**摆放。
- **Claude 上下文与记忆**：我收的是 **Anthropic 官方 API/docs 侧**（context editing beta header、memory tool、Claude Code 上下文文档、中途改工具/系统消息），cn 声明的是 **"Claude Code 上下文管理 压缩 实战"、"memory 记忆管理 遗忘 冲突 中文"** —— 按分工**官方文档归我、中文实战帖归 cn**，实体不同，不重复。
- **模型上新**：cn 收"国产 GLM / Kimi / Qwen 2026-09 中文媒体转述"，我这边**逐个 grep 后全剔**（`Omni-Flash` 在 v7(#26)/v11 命中、`MiMo-V2.6` 在 v18/v19 命中、`Kimi K3` 在 v7/v17 命中、`Xing4.0` 在 v10(#15) 命中）——**国产模型本轮在 official 侧零新增**，与 cn 的"中文媒体转述"不构成官方/非官方双报。
- **DSH 英文侧两篇（cn 提示归我）**：`beri.net/learning/deepseek-harness-docs`、`developersdigest.tech/.../deepseek-harness-dsh-first-look` —— **本轮未收细则**（时间预算不足以逐条核实其 `~218k stars / CVE-2026-82533 CVSS 9.4` 等数字），已登记为**下一辑 official 路待办**，请勿按重复计。
- **Cursor 归属**：gh 声明 `OpenCursor` 是第三方仓库、归 gh；我收的是 **Cursor 官方的"自托管机器"方向与 60% 内部 PR 数字**，**不同实体**，不重复。
- **vibe coding**：gh 收**扫描器仓库**、cn 收**翻车复盘帖**、我收**官方/社区的政策与立场**（OpenJev 热评、Stripe Kai、开发者过载、"写给人类看别用 LLM"）—— 三层不同，不重复。
- **Bend 2 "先例检查四问"**：`先例` 在 v20 §十 命中（四问 + 58/442 行 + SPARK 全在 v20 收过），**本辑 DEV.to 那篇是同一事件重述 → 我已剔**，特此说明（若 cn 或 gh 也读到，请同样按 v20 已收处理）。
