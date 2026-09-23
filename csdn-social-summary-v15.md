# 跨平台游戏制作 × AI 开发资源梳理（2026-09-21 · 第十五辑）

> 搜索覆盖：GitHub（本辑新收录的项目全部走 **REST API 实测** stars / 协议 / 推送日期，
> 没有一个数字是估的）/ CSDN · 稀土掘金 · 阿里云开发者社区 · 今日头条 · 腾讯网 · Trae 官方社区 /
> 个人技术博客 / 大模型公司官方发布页（DeepSeek · 通义 · 智谱 · 月之暗面）/
> 英文社区（Hacker News、r/gamedev、r/godot）/ Ren'Py 本地化工具生态
>
> 上一辑（第十四辑）的主线是**「可达性」**——不只是"断言过没过"，而是"**这条分支走不走得到**"。
> 这一辑顺着它再往"做"的那一侧走一步：**可达性是"验"的问题，那"做"的那一侧呢？**
> 答案是——**凡是能用工具自动化的环节，都不该继续靠人对账**。
>
> **本辑主线 = 「把人工环节交给工具」。**
>
> 已有索引：`index.html`（**1079** 项 GitHub 项目，本辑新增 5 张卡 → 第二十版 + 第二十一版增补）
> + 前十四辑经验帖（累计约 404 条 + 本辑 **45 条** ≈ **449 条**）
> + `game-production-pipeline.md`（9 步工具链 + 决策原则 44 条）
> + `agent-house-rules.md`（32 条房规）+ `mistakes/`（错误记忆 15 条）
>
> 上一辑存档：`csdn-social-summary-v14.md`

---

## 本辑一句话

**第 10 轮做英文版，586 条中文字面量里 166 条 SDK 提取不到、其中约 70 条玩家可见，
全部靠人工对账。**而社区里早就有人把这件事写成了工具 ——
**你手写一遍才明白的痛点，总有人已经替你做成了脚本。**

---

## 一、Ren'Py 本地化工具（本辑最可直接落地的一组 · 4 条）

**为什么单独成组**：刚刚做完英文版，全程手工对账；这一组就是"下次不用手工"的答案。
**下面每个项目的 stars / 协议 / 推送日期，都是 2026-09-21 用 GitHub API 实测的**（`gh search repos`），
不是抄的排行榜。

### 1. abse4411/projz_renpy_translation —— 中文社区的 Ren'Py 机翻工具（**209★**）

一句话：把 Ren'Py 项目的 `.rpy` 文件批量抽出来、机翻、再塞回去的工具，作者是中文用户，
README 也是中文的。

| 项 | 值 |
|---|---|
| 语言 / 协议 | GPL-3.0 |
| 最后推送 | 2026-08-01 |
| 状态 | **已在 `index.html` 里**（本辑不重复登记卡片） |

**为什么值得知道**：它就是"第 10 轮那件苦力活"的现成答案 —— 我们手工数出"586 条里 166 条提取不到"，
它做的事本质上就是替你把"提取 → 翻译 → 回填"这条链走完。
**但要注意它和我们的路线不同**：它是"机翻整个项目"，我们的做法是"走 Ren'Py 官方的翻译层
（`tl/<语言>/`）+ 闸门验漏"。**前者省力，后者可维护** —— 已经在做的项目继续走官方层更划算，
新项目可以拿它省第一遍的力。

### 2. Lord0fTurk/RenLocalizer —— 多引擎桌面翻译器（**35★** · 本辑新收录）

一句话：一个**桌面软件**（不是命令行脚本），打开就能自动翻译 Ren'Py 视觉小说的 `.rpy` 文件，
可以切换多个翻译引擎，也支持走**本地模型（Ollama）**。

| 项 | 值 |
|---|---|
| 最后推送 | **2026-09-18**（三天前，非常活跃） |
| 收录理由 | 唯一一个把"多引擎 + 本地模型"做进 GUI 的 Ren'Py 翻译器 |

**可拓展性（7.0/10）**："多引擎可切换"这个设计本身值得抄 ——
我们第 10 轮的翻译是"模型初翻 + 人工过"，如果换成一个可配置的引擎层，
以后要换翻译模型（比如换成本地 Qwen）只需要改一个配置，不用动流程。

**实用性（3.0/10）**：**本作现在用不上** —— 英文版已经翻完且过了 R1~R5 五道闸门，
再用它跑一遍只会把已经人工校对过的译文覆盖掉。
**它的正确用法是"下一个项目的第一遍"**，或者给"新增了大量台词后的初翻"用。

### 3. kobaltcore/renpy-translate（15★ · MIT）：走 Google Cloud Translate API 的翻译脚本

体量小、协议干净（MIT）、思路直白 —— **适合当"最小可读样本"**：
想看"Ren'Py 翻译自动化到底要处理哪些边角"的话，它比上面两个大项目更容易读透。
更新停在 2025-05，属于"稳定不再改"而不是"废弃"。

### 4. Darkmet98/Monika（5★ · MIT，2026-07）—— Ren'Py 翻译 ↔ CAT 工具互通

一句话：在 Ren'Py 的翻译文件和**专业翻译软件**（CAT，如 Trados / memoQ 那类）之间做导入导出。
**它解决的是"要交给专业译者的项目"这个问题** —— 本作是单人 hobby 项目，用不上；
但"翻译文件能被专业工具读写"这件事，对将来真要做商业化本地化是必需的接口。

> **这一组的共同教训**：第 10 轮我们花了大量时间在"哪些中文字面量提取不到"上
> （`Character("...")` 的名字、`textbutton`、`renpy.input`、screen 里的 `text`、两张数据表……）。
> 上面这些工具**每一个都必须面对同一批边角** —— 去看它们怎么处理，
> 比再读一遍官方文档更快。

---

## 二、游戏制作与拓展（中文社区实测 · 6 条）

### 5. 《RenPy 网页化实战 + GitHub Actions 校验》（CSDN，2026）

把 Ren'Py 游戏导出成网页版，并用 **GitHub Actions + Headless Chrome** 在每次提交后
自动截首屏、检查渲染是否正常，还写了 WebGL 上下文丢失的排查过程。

🔗 https://blog.csdn.net/weixin_33507732/article/details/164353021

**人话**：它给"怎么让游戏自动证明自己没坏"提供了另一条路 ——
我们的 `testcases.rpy` 是**在游戏内部**跑断言 + 截图；它是在**外部**用无头浏览器截。
两者互补：外部截图能验证"发行包在别人机器上跑起来长什么样"，这是内部测试做不到的。

**可拓展性 8/10**：本作已经有 `_shots/` 截图回路，缺的正是"**在打包产物上跑一遍**"这一环。
这条思路可以直接嫁接到 `check_release.py` 之后 —— **打完包，启动一次，截图对一眼**。

### 6. 《Unity 单元测试入门笔记》（稀土掘金，2026）

EditMode / PlayMode 双模式 + NUnit 示例 + `asmdef` 配置，是 Unity 侧"测试怎么搭"的入门笔记。

🔗 https://juejin.cn/post/7652196310042591266

**对本作的意义**：引擎不同（Ren'Py 无这套），但那份"**两类测试分工**"的思路是通用的 ——
一类测纯逻辑（不启动游戏），一类测真实运行。我们的 `check_*.py`（纯静态）与
`testcases.rpy`（真跑游戏）正好就是这两类，**这条笔记等于给我们的分工找了个旁证**。

### 7. 《独游作者控诉 demo 被逆向搬空》（腾讯网，2026-09）

2026 年 9 月发生的真实事件：作者的 Steam demo 被人反编译、改个标就拿去上架。
文里给了可操作的建议 —— 用 IL2CPP / 加混淆 / **把 demo 和正式版拆开**。

🔗 https://new.qq.com/rain/a/20260912A05GM400

**为什么收它**：本作是 Ren'Py（**打包产物是明文脚本**，比 IL2CPP 好扒得多）。
这条对我们的直接含义是 —— **发行时想清楚"哪些内容不该进 demo"**，
而不是等出了事再补。属于"知道了不一定用得上，但不知道会吃亏"的那一类。

### 8. 《Kook Zimage 立绘生成流程（真实项目验证）》（CSDN，2026）

三步导出 + 分层命名，附《星尘守望者》"一周做 4 个主角立绘"的案例。

🔗 https://blog.csdn.net/weixin_42612405/article/details/157500173

**和我们的关系**：本作的立绘走的是**绿幕生图 → 程序化抠图**（`tools/prep_sprites.py`）。
这条是**另一个流派：直接生成透明底 + 分层文件**。两个流派的胜负手在于
"**边缘质量**" —— 我们的绿幕流程实测残留绿边 ≤0.001%，这是它的护城河；
分层流派的优势是"改一个表情不用重出整张图"。**先记下，不动**（本作 14 张立绘已验收）。

### 9. 《游戏语音声音克隆工具推荐》（今日头条，2026）

GPT-SoVITS / CosyVoice / Fishaudio / Qwen3-TTS 的**本地 vs 云端选型清单**。

🔗 https://toutiao.com/article/7685449479754908195

**和我们的关系**：本作第 6 轮用的是 **Kokoro 中文模型**（本地、离线、零 API 成本），
当时的结论是"女声普遍带电音，选音色要按量出来的高频能量挑，不要按性别挑"。
这条清单里 **CosyVoice / GPT-SoVITS 都支持"参考音频"** —— 也就是
**这正是我们当时说的"真要做情绪化演出，应该换支持参考音频的模型"那一条路**。
→ **第 11 轮（帕姆配音）开工前值得先看看这两个**。

### 10. 《从零开始开发视觉小说：Ren'Py 入门实战》（个人博客，2026）

VS Code + 插件配置、`scene`/`show` 立绘切换、资源目录约定，带可运行代码。

🔗 http://heibaimeng.com/post/300

**为什么收**：作为"Ren'Py 入门第一课"的**参照系** —— 回头看看新手上手会卡在哪，
对我们自己写文档（README 的"想改点什么"那一节）是有用的输入。

---

## 三、AI 开发与使用（中文社区实测 · 8 条）

### 11. 《Claude Code 并行开发：Subagents + Git Worktree》（CSDN，2026）

用 **subagents + git worktree** 做并行开发的完整案例（Spring Boot 订单重构），
含可复制的 `CLAUDE.md` 模板和避坑清单。

🔗 https://blog.csdn.net/m0_37988015/article/details/161508408

**人话**：`git worktree` 让同一个仓库有多个"平行工作目录"，于是可以让几个 agent
**各改各的、互不打架**；`CLAUDE.md` 则是给 agent 的"房规"。
→ **和我们的 `agent-house-rules.md`（32 条房规）是同一个东西** ——
只不过我们用一份共享的 markdown，它用每个仓库里的 `CLAUDE.md`。
**可拓展性 8/10**：本作现在只有一个 agent 串行作业，暂时不需要并行；
但"**多条线同时推进时靠 worktree 隔离**"这条，在做索引/调研这类可并行的活时已经用得上
（本次调研就是三个 agent 并行跑的）。

### 12. 《2026 主流 AI 编程工具深度横评（5 款各写一个项目）》（CSDN，2026）

Cursor / Claude Code / Trae / 通义灵码等实测对比 + 按角色选型。

🔗 https://blog.csdn.net/df2209/article/details/162838096

**注意**：本工作区早有 7 款 agent 工具的横向评测报告（用户自建）。这条的增量是
**"各写一个完整项目"这个评测方法** —— 比"做完形填空式的 benchmark"更接近真实使用。
**收它是因为方法，不是结论。**

### 13. 《2026 我用过的 5 款 AI 编程工具真实体验》（个人博客，2026）

个人复盘，最值钱的是那句**"AI 生成的代码必须逐行审，涉及钱和权限的逻辑自己写"**。

🔗 https://wangchenyu.com/aitool/155741.html

**和本工作区的关系**：这条和我们的决策原则**完全同向** ——
pipeline 里那条"**AI 写标准模块可信、写手感/边界/性能必须亲手验**"是同一句话的另一个版本。

### 14. 《Ollama 保姆级实操教程（2026 本地部署）》（阿里云开发者社区，2026）

qwen3 / deepseek-r1 选型 + 踩坑（**C 盘被模型占满**、显存不足、接口不可达）。

🔗 https://developer.aliyun.com/article/1760276

**为什么收它**：本工作区的 `ccgs-cn-config` 就是"本地/远程模型接入"的自建工具，
这条里的三个坑我们**全踩过**（尤其"C 盘占满" —— 用户明确要求所有产出默认落 D 盘，
理由就是这个）。可以当"给别人讲这套东西时用的现成教材"。

### 15. 《Claude Code MCP 实战：5 分钟配好》（今日头条，2026）

filesystem / github 两个 MCP 的配置模板 + 连接失败排查。

🔗 https://toutiao.com/a7645761919512609280

**和本作的关系**：本作 ROADMAP 里有一条明确决定 —— **"本项目不用 MCP"**
（第十辑论证过"Ren'Py 纯文本不需要 MCP"；第十一辑实测某 Ren'Py MCP 会把我们的 OFL 字体
换成商业字体）。**这条不动摇结论**，但它的"连接失败排查"清单对"以后想接别的 MCP"是有用的。

### 16. 《16 个 GitHub 工具专治 AI 味》（今日头条，2026）

`stop-slop` / `Humanizer-zh` / `shuorenhua` 等中文去味工具，给了一套"三步法"。

🔗 https://toutiao.com/a7664809057202569743

**和本作的关系（本辑最相关的一条之一）**：本作第 5 轮做过 `tools/check_dialogue.py`，
六条规则查"AI 腔"（套话 / 编辑脚注 / 长句 / 口癖 / 口吻分化）。
**我们的做法是"自己定规则 + 自己量阈值"，这些工具是"别人攒的通用规则集"** ——
可以把它们的规则表当**外部对照**，看有没有我们漏掉的形态。
⚠️ 但注意：通用"去 AI 味"工具是为**中文通用文本**设计的，本作是**角色对白**，
"NPC 说套话是设定（本作吐槽的就是套话），旁白和内心说套话才是 AI 味" ——
这条区分它们没有，**直接套用会误伤**。

### 17. 《Trae 深度使用与生产力全开指南》（Trae 官方社区，2026）

Builder 模式、用 `.traeignore` 降低幻觉、终端联动、多模型切换。

🔗 https://forum.trae.cn/t/topic/1452

**为什么收**：`.traeignore` 这个做法**可以直接借** ——
本工作区有大量 `_*.txt` 临时日志和 `_shots/` 截图，
"让 agent 别去读这些"能省不少上下文。属于**看完立刻能做的小改进**。

### 18. 《程序员做游戏美术：AI 把成本压到接近 0》（CSDN，2026）

MJ → Firefly → PS 的立绘五步流程，外加像素风 SD + LoRA。

🔗 https://blog.csdn.net/tanden/article/details/160431471

**和我们的关系**：本作的背景与立绘是"生成 → 程序化后处理"（抠图 / 去绿边 / 裁边 / 体型归一）。
这条给的是"**后处理在 PS 里手工做**"的版本。**我们的流程更适合批量**
（14 张立绘一次处理完），**它的流程更适合单张精修**。先记下。

---

## 四、大模型公司官方与英文社区（10 条）

> 这一组来自一次**独立的官方/英文源调研**。取舍标准只有一条：
> **"它能不能改变我下一步要做什么"** —— 所以像"融了多少钱""谁又发了人事公告"这类一律不在表内。
> **可信度标签**：标"社区聚合"的是二手信息（模型名准确性**未逐个核实**），其余取自官方文档/博客。

### 19. Qwen3-Max 文档更新（阿里云百炼官方，2026-09-14）

256K 上下文（思考模式 32K 输出），**agent 编程与工具调用**专项升级。

🔗 https://help.aliyun.com/en/model-studio/model-qwen3-max

**对本作**：国内可达、便宜。Ren'Py 的 Python 脚本调试、中文文案润色、美术 prompt 都能用。
⚠️ **但 `Qwen3-Max` 这个名字在本索引的 v9 / v11 里已经出现过** —— 所以**本辑不把它登记成新条目**，
只记这次文档更新的日期与数值。

### 20. GLM-5.3（智谱官方文档，2026-08-19）

编程能力较 5.2 提升 50%，Terminal Bench 3.0 开源 SOTA，新增**代码审计 / 漏洞发现**能力。

🔗 https://docs.bigmodel.cn/cn/update/new-releases

**对本作**：Z.ai / 百炼 API 国内可达，可当主编码助手。⚠️ `GLM-5.x` 在 v3 / v6~v12 已多次出现，
**同样不重复登记**。

### 21. Kimi K2 0905（月之暗面官方博客，2026-09-05）—— 本辑性价比最高的一条

强化 agentic coding、256K 上下文；MoE **1T 总参 / 32B 激活**；**开源（modified MIT）**；
**$0.15 / $2.5 每百万 token**。

🔗 https://www.kimi.com/zh-tw/blog/kimi-k2

**对本作**：**便宜到可以拿它做"中→英初翻"**，而且权重开源 —— 以后真要自托管也有路。
**可拓展性 8/10**：第 10 轮的英文译文是"模型初翻 + 人工过"；再要加内容时，
这个价位适合"**先把整批初翻跑出来，人只做校对**"。**实用性 7/10**。

### 22. DeepSeek V4（Flash-0731 / Pro-0813）

MIT 开源权重、**1M 上下文**；Flash 284B / 13B 激活，Pro 1.6T / 49B。

🔗 https://www.thundercompute.com/blog/deploy-deepseek-v4-locally

**对本作**：API 直连便宜，适合批处理初翻；**但本地跑不动**（Flash 也是 284B 级），
个人机器只能走 API。⚠️ 官方发布页未逐字打开，规格是拿官方 checkpoint 日期与这份部署指南对上的。

### 23. OpenAI GPT-5（官方，2026-08-07）

400K 上下文，三档（gpt-5 / mini / nano），强化 coding 与 agentic。

🔗 https://openai.com/gpt-5

**对本作**：**网页 / App 在大陆日常不可达，别当主力**。但 `mini`（$0.25/$2）与
`nano`（$0.05/$0.40）经代理可用 —— **适合"大批量本地化初稿"这种一次性的苦力活**。

### 24. teo-lin/renpy-translator —— 完全离线的 Ren'Py 本地 LLM 翻译

一句话：**不联网**，用本地 LLM（RTX 3060 / 5070 笔记本、6GB+ 显存）翻 Ren'Py 的 `.rpy`，
**保留 `{rpy}` 标签与变量**。

🔗 https://github.com/teo-lin/renpy-translator

**为什么值得知道**：它把两件最难的事一起做了 —— "**离线**"和"**占位符保真**"。
而"占位符保真"正好是我们 `check_i18n.py` 的 **R3**。
→ **去看它怎么保证 `[变量]` 不被翻坏**，比我们自己想一遍更省事。
⚠️ **此链接未逐字核对**（按"未核实"记录）。

### 25. RenLocalizer 的完整能力（第 2 条的补充）

除"多引擎可切换"之外，它还支持 **Ollama 本地 LLM / DeepSeek**、能处理 `.rpyc` 与 `.rpa`
（**打包后**的资源，不只是源码）、带 **SyntaxGuard**（防止翻译写坏语法导致游戏崩）、
并且有 **CLI 模式可批处理整包**。

→ **`SyntaxGuard` 这个设计最值得抄**：我们的闸门都是"**事后验**"，
它是"**写入前先拦**"。**两种都该有** —— 写入前能拦住的，就不该等到跑闸门才发现。

### 26. 《AI 编码 agent 的不舒适真相》（英文社区，2026）

采用率 **84%**，但**信任度只有 29%**；AI 写的代码会累积维护债与安全债，必须人工 review。

🔗 https://www.codewithseb.com/blog/uncomfortable-truths-ai-coding-agents-2026

**为什么收**：这个"84% vs 29%"的落差，就是本工作区那 32 条房规存在的理由。

### 27. HN《本地模型现在真的好用了》（2026-06-15 · 1004 分）

M2 64GB 实测 Mistral 7B / Gemma3 / Qwen3 MoE，结论是"**本地推理已经达到实用**"。

🔗 https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/

**对本作**：给"本地 Ollama 路线"提供了外部佐证。
（日期略早于本辑窗口，但它是这个方向上引用最多的一篇，值得留档。）

### 28. 社区聚合：本地可跑的编码模型清单（**社区聚合，仅供参考**）

- KDnuggets《2026 可本地跑的编码模型》：
  https://www.kdnuggets.com/top-7-coding-models-you-can-run-locally-in-2026
- ai-master.dev（聚合 r/LocalLLaMA 的每月推荐）：
  https://ai-master.dev/en/article/meilleurs-llm-locaux-septembre-2026
  —— 提到 `Qwen3.6-35B-A3B`（16GB 显存可跑、3B 激活、20–40 tok/s）

**⚠️ 这两条是社区聚合，不是官方来源，模型名的准确性没有逐个核实。**
收它们的唯一理由是：**"多大显存能跑什么"正是本机的约束。**

**这里要分清一个容易混的概念**：表里说的是**显存 16GB**，
而本机是**内存 16GB**（跑 Ollama 时靠量化模型 + 部分卸载），**两者不是一回事** ——
"16GB 显存能跑的模型"不等于"本机能跑"。别把这张表当成"我明天就能拉这个"。

---

## 五、GitHub 项目（21 条 · 全部逐条实测核实）

> **数据来源**：2026-09-21 用 `gh api` 逐条核实（stars / license / language / pushed_at / **archived**），
> 并逐个在 `index.html` 里 grep 去重 —— **21 条全部为新**。
> 其中 **4 条已单独立卡进 `index.html`**（第二十一版增补：[1075]-[1078]），
> 其余 17 条以链接形式留在这里。
>
> **为什么只挑 4 条立卡**：索引的容量不该被"顺手看到的"占满 ——
> 立卡的那 4 条各自回答了一个**我们已经在做的问题**，其余的在表里留链接就够了。

### 游戏制作与拓展（9 条）

| 仓库 | ★ | 协议 | 语言 | 推送 | 一句话 | 可拓展性 |
|---|---|---|---|---|---|---|
| [**Icemic/moyu**](https://github.com/Icemic/moyu) 🆕**卡** | 97 | MPL-2.0 | Rust | 09-19 | 跨平台视觉小说引擎（React + QuickJS） | 对照它的分层设计看我们的 `00_config` / `script` 切得对不对 |
| [carenalgas/popochiu](https://github.com/carenalgas/popochiu) | 355 | MIT | GDScript | 09-21 | Godot 的点选式冒险游戏插件 | 接 Godot 4 做叙事解谜 |
| [soimy/maxrects-packer](https://github.com/soimy/maxrects-packer) | 245 | MIT | JS | 09-21 | 2D 精灵图集合图（maxrects 算法） | 接美术导出 / 自动化构建管线 |
| [addmix/godot_aerodynamic_physics](https://github.com/addmix/godot_aerodynamic_physics) | 204 | MIT | GDScript | 09-19 | Godot 空气动力学节点 | 飞行 / 载具类项目 |
| [j20001970/GDMP](https://github.com/j20001970/GDMP) | 131 | MIT | C++ | 09-20 | Godot 的 MediaPipe 插件（手势 / 姿态驱动角色） | 体感 / 直播互动游戏 |
| [script-gd/gdcc](https://github.com/script-gd/gdcc) | 92 | LGPL-3.0 | Java | 09-21 | GDScript 的 AOT 编译器（编成 GDExtension 提速） | 接性能敏感的熱路径逻辑 |
| [RPG-Maker-Translation-Tools/rpgmtranslate-qt](https://github.com/RPG-Maker-Translation-Tools/rpgmtranslate-qt) | 25 | WTFPL | C++ | 09-16 | RPG Maker 翻译 / 编辑 GUI | **本地化工作流**：汉化 RPG Maker 最轻量的 GUI |
| [nt7011/RPG-Maker-Live-Translator](https://github.com/nt7011/RPG-Maker-Live-Translator) | 22 | AGPL-3.0 | TS | 09-12 | RPG Maker **边玩边翻**，零预提取 | 接机翻 API 做即时汉化 |
| [**kphutt/gdmutant**](https://github.com/kphutt/gdmutant) 🆕**卡** | 3 | MIT | Python | 09-21 | **变异测试**：测出"绿测"漏掉的 bug | **本批最值钱的思路**：把"闸门自己也要被验"自动化 |

### AI 开发与工具链（12 条）

| 仓库 | ★ | 协议 | 语言 | 推送 | 一句话 | 可拓展性 |
|---|---|---|---|---|---|---|
| [**lidge-jun/opencodex**](https://github.com/lidge-jun/opencodex) 🆕**卡** | 15,728 | MIT | TS | 09-21 | **代理网关**：让 Codex / Claude Code 跑在任意模型上 | 与 `ccgs-cn-config` 同题，可对照它做"客户端与模型解耦" |
| [**iamfakeguru/agent-md**](https://github.com/iamfakeguru/agent-md) 🆕**卡** | 968 | MIT | Shell | 09-21 | 生产级 agent 指令集（`CLAUDE.md` / `AGENTS.md` 那一类） | 给 `agent-house-rules.md` 做一次外部对照审计 |
| [kvcache-ai/Mooncake](https://github.com/kvcache-ai/Mooncake) | 6,628 | Apache-2.0 | C++ | 09-21 | 分离式推理服务（月之暗面同款） | 集群级部署；个人机器用不上，**知道它存在**即可 |
| [Q00/ouroboros](https://github.com/Q00/ouroboros) | 6,055 | MIT | Python | 09-21 | 自进化 Agent OS（评测准入式自迭代） | 接评测集做 agent 自训练 |
| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | 5,128 | 自定义 | Go | 09-21 | MCP **官方** Go SDK | 写 Go 版 MCP server / client |
| [microsoft/agent-framework-go](https://github.com/microsoft/agent-framework-go) | 621 | MIT | Go | 09-21 | 微软多 Agent 编排框架（Go） | 后端多 agent 流水线 |
| [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) | 1,146 | MIT | Python | 09-21 | OpenHands 的 agent SDK（模块化，不绑整套） | 用自有的工具链接 agent |
| [seoes/proval](https://github.com/seoes/proval) | 87 | AGPL-3.0 | TS | 09-21 | 自托管 LLM 代码审查（本地模型审 PR） | 接 GitLab / Forgejo / GitHub |
| [hybridindie/godot-mcp](https://github.com/hybridindie/godot-mcp) | 21 | MIT | Python | 09-21 | Godot + MCP 双向驱动（自然语言操控编辑器） | 接任何 MCP client —— **但本作已明确决定不用 MCP** |
| [MockLoop/mockloop-mcp](https://github.com/MockLoop/mockloop-mcp) | 17 | MIT | Python | 09-21 | OpenAPI → mock 的 MCP | AI 辅助接口联调 |
| [m-newhauser/gliner25-compaction](https://github.com/m-newhauser/gliner25-compaction) | 7 | Apache-2.0 | TS | 09-21 | **本地上下文压缩**（GLiNER，证据优先） | 读大文件 / 长任务时省 token |
| [everdict/everdict](https://github.com/everdict/everdict) | 2 | Apache-2.0 | TS | 09-21 | agent 评测运行时（harness 无关） | 接任意 agent 做回归评测 |

**这一路没找到的**（如实记录，免得下次重复找）：
"AI 文风检测"类**近三个月没有像样的开源项目**（命中项多为 0★ 空壳或 pure awesome-list）；
"游戏 mod 框架 / Steam 上架工具 / TTS 配音工具"**活跃开源新项目极少**；
像素/2D 资源独立工具大多已被既有大库（Aseprite / Godot 生态）吸收。

---

## 六、这一辑里"立刻能做"的三件事

1. **给 `check_release.py` 加一步"打包后真跑一次"**（来自 #5 的 headless 截图思路）——
   现在闸门只查"文件在不在"，不查"跑起来对不对"。成本低，收益直接。
2. **借 `.traeignore` 的思路**（来自 #17）：给工作区加一份"让 agent 忽略临时产物"的清单，
   省上下文。**注意**：`.workbuddy/` 程序目录**不能**排除。
3. **第 11 轮（帕姆配音）开工前先看 CosyVoice / GPT-SoVITS 的参考音频能力**（来自 #9）——
   这是第 6 轮就写下的"真要做情绪演出就得换模型"那条路的现成候选。

---

## 收录统计

| 类别 | 本辑新增 | 累计 |
|---|---|---|
| 中文社区经验帖 | **14 条** | 约 418 条 |
| 大模型官方 / 英文社区 | **10 条** | 约 428 条 |
| GitHub 项目（条目 / 立卡） | **21 条**（其中 5 张立卡） | **1079 项** |

**查重说明**：本辑 14 条中文经验帖的 URL / 文章 ID / 作者名，逐个在前十四辑存档
（`csdn-social-summary-v2…v14.md`）与 `index.html` 里 grep 过 —— **全部为新**。
被查出的**已在索引里、本辑不重复收录**的有：`projz_renpy_translation`、`Qwen3-Max`、`GLM-5.x`。
官方 / 英文源那 10 条另做过一次 grep，与中文索引无重叠。

**⚠️ 本轮的一个流程教训（写在这里免得下次再犯）**：
派调研 Agent 时，我把索引路径写成了 `D:\34498\Documents\csdn-social-summary.md`，
**漏了 `github-projects-invest-games\` 这一层** → 三个 Agent 都没能真正查重。
**上面的查重是我自己补做的**。给 Agent 派"查重"这类活，路径必须给全。
