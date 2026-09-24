# 第二十二辑 · 主 agent 直查增补（2026-09-24）

> 这一份不属三路，是主 agent 处理**上轮待办 #1**（追《DeepSeek Harness：从开机到拆开》一手源）
> 时直查得到的。**待办 #1 已于本轮闭环。**

## 0. 待办 #1 闭环：一手源找到了

**《DeepSeek Harness：从开机到拆开》橙皮书** —— 作者**花叔**（HuaShu / `alchaincyf`）
- 仓库：https://github.com/alchaincyf/deepseek-harness-orange-book
- `gh api` 实测：**★1302** · license `null`（正文声明 **CC BY-NC-SA 4.0**）· 建于 **2026-08-14** · updated **2026-09-24**
- 官方口径（README）：「written within 24 hours of DeepSeek open-sourcing its agent harness (**Aug 13, 2026, MIT license**)」
  → **新事实：DeepSeek agent harness 开源日 = 2026-08-13，MIT 许可**
- 橙皮书内容（README 自述，**未逐页读**，标"官方自述"）：完整系统提示词 · **129 行默认启动清单** ·
  **三份未编辑原始会话日志** · AI 给自己造工具的现场记录（**19 步，工具清单 32 → 33 行**）·
  四种运行模式 · 技能与插件机制 · 代码库考古 · 事故复盘。四大板块：入门指南/运行机制/技术地基/哲学反思。
- 分发：PDF / EPUB / HTML 免费下载。
- 作者背景：独立开发者，**小猫补光灯**（App Store 付费榜第一）作者，"橙皮书"系列作者，
  CCTV《焦点访谈》"手搓经济"代表人物，全平台 50 万+ 读者，**自述从未手写过一行代码**。
- 官网 `huasheng.ai` · X `@AlchainHust` · GitHub `@alchaincyf`

> ⚠️ 核实边界：**README 自述已读，正文未读**（PDF 未下载）。标"官方自述"的字段不得当作实测证据引用。

## 1. 顺带查出的整个生态（全部 `gh api` 实测，**14 个均在 index.html 与 v19/v20/v21 中零命中**）

| 仓库 | ★ | 建/更新 | 一句话 |
|---|---|---|---|
| `alchaincyf/nuwa-skill` | **33169** | — / 09-24 | 「蒸馏任何人的思维方式」——心智模型 / 决策启发式 / 表达 DNA |
| `alchaincyf/huashu-design` | **24423** | — / 09-24 | HTML 原生设计 skill：高保真原型 / 幻灯片 / 动画 + 20 条设计哲学 + 5 维评审 + MP4 导出，**agent-agnostic** |
| `alchaincyf/zhangxuefeng-skill` | **10327** | — / 09-24 | 「张雪峰的认知操作系统」，由 `nuwa-skill` 生成 |
| `alchaincyf/darwin-skill` | **6086** | — / 09-24 | **让 skill 自己进化**：评估→改进→测试→保留或回滚（autoresearch 式） |
| `alchaincyf/hermes-agent-orange-book` | **4953** | — / 09-24 | Nous Research 开源 agent 框架 Hermes Agent 的橙皮书 |
| `alchaincyf/huashu-skills` | **1607** | — / 09-24 | 花叔全部 skill 总目录：16 旗舰 + 14 人物视角 + 22 内置 = **52 个** ｜ 机器可读 `skills.json` + 安装协议 + 更新检查 |
| `alchaincyf/deepseek-harness-orange-book` | **1302** | 08-14 / 09-24 | 见上 |
| `alchaincyf/huasheng_editor` | 756 | — / 09-24 | 花生公众号排版器 |
| `alchaincyf/huashu-report` | 422 | — / 09-24 | **机构级研究报告 skill**：规范从 2026 顶级机构报告反向提炼，42 份采集/41 份进量化基线（Stanford/McKinsey/BCG/OpenAI/**PwC**/World Bank），6 种报告原型 + 8 种图表模式 + 可复用流水线 |
| `alchaincyf/deepseek-v4-deep-dive` | 280 | 04-24 / 09-19 | DeepSeek V4 深度解读 · 73 页 PPT + 20 分钟讲稿 |
| `alchaincyf/3d-vibe-coding-handbook` | 264 | — / 09-24 | 《3D Vibe Coding 手册》配套仓库 |
| `alchaincyf/claude-code-orange-book` | 316 | — / 09-24 | Claude Code 橙皮书 |
| `alchaincyf/karpathy-skill` | 304 | — / 09-24 | Karpathy 的认知操作系统 |
| `alchaincyf/deepseek-influence-report` | 31 | 08-27 / 09-24 | 「发布节奏就是护城河」DeepSeek 开源影响力投研：22 页 + 34 个带口径数据点 + OpenRouter **85 周**份额复算 + 可复跑采集脚本 |

### 对我们最有用的三条（可复用性 = 落地）
1. **`darwin-skill`** —— 正好对上本机待办 #9「`/skill-doctor` 式自查：列出没被用过的 skill」。
   它的形状是**评估→改进→测试→保留或回滚**，等于把"skill 进化"做成棘轮。
2. **`huashu-report`** —— 与本项目「单文件 HTML 调研报告」流水线同题，且它的**规范是从 42 份真报告反向提炼**的
   （16GB 机器跑得动，纯 prompt/skill 层）。可作对标来源。
3. **`huashu-skills` 的 `skills.json` + 更新检查机制** —— 我们的技能没有"机器可读清单 + 版本/更新检查"。

### 待下一次核实的项（不确定，别当结论）
- 这些 skill 仓库大多是 **08–09 月新建**，★ 数增长很快（`nuwa-skill` 3.3 万）→ **需要一次"是否真人关注"的核实**
  （避免把刷量当热度）。核实办法：看去重后的 fork/issue/PR 结构，而不是只看 ★。
- `huashu-report` 声称"41 份进量化基线"，**抽样验证过再引用**。
