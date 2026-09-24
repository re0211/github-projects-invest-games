# -*- coding: utf-8 -*-
"""第二十八版增补：把第二十二辑新发现的 13 个条目登记进 index.html。

本辑候选池是历史最大（gh 路 28 条正式 + 主 agent 直查花叔生态 14 条 = 42 个），
8 个装不下 → **本版收紧到 13 项**，优先取「与我们画像重合度最高 + 本轮头条」的，
其余在 `csdn-social-summary.md` 第二十二辑的「下一辑待办」里逐条登记。

逐仓库仍是 `gh api repos/<r>` 实测（stars / license / language / updated_at 无一估算），
再逐条 grep 过 19 份存档 + 1128 项索引。剔掉的已收录项见本辑 gh 路去重报告。

本辑主线：**待办闭环 + 一手源** —— 追了两轮的《DeepSeek Harness：从开机到拆开》一手源找到了
（`alchaincyf/deepseek-harness-orange-book`，★1302），并顺带查出整个橙皮书/skill 生态。

⚠️ 本脚本的四道保护（页头锚点 / 最后脚注锚点 / section 唯一性 + 插入点 div 深度 / 重复仓库检测）
沿用第二十七版，已由 `_tools/insert_guard_probe.py` 用真实历史版本做过 6 例正负验证。

数据来源：2026-09-24 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v28_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1127"'
FIRST_NEW_FOOTNOTE = 1128
MARKER = "第二十八版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第二十七版增补 2026-09-24',
    '共 1128 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第二十八版增补 2026-09-24',
    '共 1141 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项 + 第二十八版增补 13 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm28c1", name="headroom（把「压缩」挪到进上下文之前）",
        url="https://github.com/headroomlabs-ai/headroom",
        lang="Python", stars="73669",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="**本批星数第一（73669★ / Python / Apache-2.0）。** 在工具输出、日志、文件、"
              "RAG 片段**进入 LLM 之前**先压缩它们。官方数据：编码 agent 省约 **20% token**、"
              "**JSON 省 60~95%**、答案不变。提供**库 / 代理 / MCP server 三种形态**。",
        analogy="我们现有的压缩手段都是**进了上下文之后才想办法**（会话摘要、手工裁剪）。"
                "这个是在**门口拦** —— 位置比「改 prompt」更通用。对 16GB 机器跑小模型收益尤其明显："
                "省下的窗口直接变成能多塞的代码。",
        ext=(78, "7.8/10", "**库 / 代理 / MCP 三形态，接法不挑客户端**；"
                           "先拿 JSON 与日志两类试收益，再决定要不要全局开"),
        use=(70, "7.0/10", "Apache-2.0 干净。⚠️ 两条：①**7 万星这种量级的增长速度本身要另核**"
                           "（本辑未做「是否真人关注」的核实，只看 issue/PR 结构）；"
                           "②压缩产物是**替身不是本体**（第二十一辑已定），原始字节要自己留底"),
        src="最近推送 2026-09-24 · 73669★ · Apache-2.0 · Python · 信源 [1128]",
    ),
    dict(
        nid="rpm28c2", name="omnigent（harness 之上的统一调度层）",
        url="https://github.com/omnigent-ai/omnigent",
        lang="Python", stars="10197",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已登记未安装")],
        plain="开源 agent 框架兼**「元 harness」**：把 Claude Code、Codex、Cursor、Pi 与自定义 agent "
              "编排到一起，**换 harness 不用重写代码**，可加策略与沙箱、跨设备实时协作。Apache-2.0。",
        analogy="我们的痛点是**同一套约定要在 dsh / Claude Code / 多个 CLI 之间各抄一遍**。"
                "它把这一层抽出来。但「元 harness」本身**是新增的一层复杂度** —— "
                "对单机 16GB 偏重，先读架构再决定引不引入。",
        ext=(68, "6.8/10", "**adapter 接口设计可抄**：把「换外壳不改约定」做成一层显式接口，"
                           "比我们现在靠人肉同步强"),
        use=(55, "5.5/10", "Apache-2.0、概念干净。⚠️ **不要因为星数高就装** —— "
                           "按 M-0002，先确认它在 16GB 上能不能跑起来再谈价值"),
        src="最近推送 2026-09-24 · 10197★ · Apache-2.0 · Python · 信源 [1129]",
    ),
    dict(
        nid="rpm28c3", name="engram（agent 自己读写的持久记忆，Go 单二进制）",
        url="https://github.com/Gentleman-Programming/engram",
        lang="Go", stars="6786",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="面向 AI 编码 agent 的**持久记忆系统**：agent 无关的 **Go 单二进制**，内含 "
              "**SQLite + FTS5**、MCP server、HTTP API、CLI 与 TUI。与同作者的 `gentle-ai` 是配套生态。",
        analogy="我们的 `mistakes/` + `MEMORY.md` 是**人写给人看的记忆**；它是**agent 自己读写**的记忆。"
                "两者不冲突 —— 但它的**写入去重**与**检索**那套，是我们「只增不合并」的现状最缺的一半。",
        ext=(72, "7.2/10", "**单二进制 + SQLite 在 16GB Windows 上几乎零负担**；"
                           "先接 dsh 看跨会话召回是不是真的有用，别一上来就迁记忆"),
        use=(74, "7.4/10", "Go 二进制直接跑、MIT。⚠️ 记忆类工具的通病：**装之前先想清楚"
                           "「谁的记忆、给谁看、失效了怎么退」**，否则会多一份互相矛盾的记忆源"),
        src="最近推送 2026-09-24 · 6786★ · MIT · Go · 信源 [1130]",
    ),
    dict(
        nid="rpm28c4", name="darwin-skill（让 skill 自己进化：评估→改进→测试→保留或回滚）",
        url="https://github.com/alchaincyf/darwin-skill",
        lang="Markdown", stars="6086",
        tags=[("t-make", "AI × 约定"), ("t-ok", "已登记未安装")],
        plain="把 **skill 的进化做成棘轮**：评估 → 改进 → 测试 → **保留或回滚**"
              "（autoresearch 式自主优化）。作者是花叔，与本批 `huashu-skills` / 橙皮书同一生态。",
        analogy="正好对上我们挂了很久的一条待办 —— **「列出没被用过的 skill / skill 该不该活」**。"
                "它的关键不是「生成新 skill」，而是**每次改动都必须先能测、且回滚是默认动作**。",
        ext=(74, "7.4/10", "**流程可抄**：给我们 19 个技能补上「评估 → 测试 → 保留/回滚」这一环，"
                           "比继续加新技能重要"),
        use=(55, "5.5/10", "纯 skill 仓库（Markdown），零运行成本。⚠️ **它假设的是 Claude Code 的 skill 格式**，"
                           "本机是 `SKILL.md` + 自建闸门 → **必须自己适配**，不能照搬"),
        src="最近推送 2026-09-24 · 6086★ · Markdown · 信源 [1131]",
    ),
    dict(
        nid="rpm28c5", name="OpenCursor（VS Code 里直连本地 Ollama 的开源编码 agent）",
        url="https://github.com/PawanOsman/OpenCursor",
        lang="TypeScript", stars="6024",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已核实待试")],
        plain="开源版「类 Cursor」的 **VS Code 扩展**：agent 式对话、**多 provider（含 OpenAI / Ollama / "
              "llama.cpp）**、语义搜索、MCP 支持。",
        analogy="明确支持**本地 Ollama** —— 对「不付订阅、也不上云」这条路是直接可用的选项，"
                "而且**装法是一次点击**，不是从源码构建（这点决定了它会不会真的被用起来）。",
        ext=(66, "6.6/10", "和我们「VS Code + 本地模型做 agent」的画像完全重合；"
                           "可用来替代一部分 Cursor 场景"),
        use=(70, "7.0/10", "⚠️ **license 未核实**（`gh api` 返回 null）→ 引用时**不要写许可证名**；"
                           "按房规先在测试目录里验一次再接管真实仓库"),
        src="最近推送 2026-09-24 · 6024★ · 未声明协议 · TypeScript · 信源 [1132]",
    ),
    dict(
        nid="rpm28c6", name="nocturne_memory（可回滚 + 可视化的 MCP 长期记忆）",
        url="https://github.com/Dataojitori/nocturne_memory",
        lang="Python", stars="1371",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="轻量、**可回滚、可视化**的 MCP 长期记忆服务器，用**图状结构化记忆替代向量 RAG**，"
              "号称任何模型 / 会话 / 工具都能持久；是 OpenClaw 的 drop-in 替代。",
        analogy="记忆系统普遍缺的两块它都有：**可回滚**（被污染能退回上一状态）与**可视化**"
                "（能看见里面到底存了什么）。我们的 `mistakes/` 现在是**只增不合并、也不能回滚**。",
        ext=(70, "7.0/10", "「图状记忆 vs 向量 RAG」是一种可对照的路线；"
                           "先只看它的**回滚与可视化**两个机制，别整套换"),
        use=(66, "6.6/10", "Python + MCP，本地起服务即可、MIT。⚠️ 新项目、单人维护，"
                           "**别把唯一一份记忆押上去**"),
        src="最近推送 2026-09-24 · 1371★ · MIT · Python · 信源 [1133]",
    ),
    dict(
        nid="rpm28c7", name="huashu-skills（52 个 skill 的总目录 + 机器可读清单）",
        url="https://github.com/alchaincyf/huashu-skills",
        lang="Markdown", stars="1607",
        tags=[("t-make", "AI × 约定"), ("t-ok", "已登记未安装")],
        plain="花叔全部开源 Agent Skills 总目录：**16 旗舰 + 14 人物视角 + 22 内置 = 52 个**，"
              "分层分类 + AI Agent 安装协议 + **机器可读 `skills.json`** + 更新检查机制。",
        analogy="我们的技能是**散装**的：没有机器可读清单、没有版本、没有更新检查，"
                "而且**刚被提醒「技能目录该整理了」**。52 个 skill 的分层与命名方式可以直接当对照表用。",
        ext=(68, "6.8/10", "**`skills.json` + 更新检查**这两样是我们 19 个技能缺的基础设施，"
                           "照它的形状补一份比继续加技能划算"),
        use=(62, "6.2/10", "纯 Markdown / JSON，零成本可读。⚠️ 里面大量是「人物视角」类 skill，"
                           "与我们的用法不同 —— **只抄结构，不抄内容**"),
        src="最近推送 2026-09-24 · 1607★ · Markdown · 信源 [1134]",
    ),
    dict(
        nid="rpm28c8", name="deepseek-harness-orange-book（追了两轮的一手源，闭环）",
        url="https://github.com/alchaincyf/deepseek-harness-orange-book",
        lang="HTML", stars="1302",
        tags=[("t-make", "AI × 上下文"), ("t-new", "本轮头条")],
        plain="橙皮书《**DeepSeek Harness：从开机到拆开**》。含**完整系统提示词**、"
              "**129 行默认启动清单**、**三份未编辑原始会话日志**、AI 给自己造工具的 **19 步现场记录**"
              "（工具清单 32 → 33 行）、四种运行模式、技能与插件机制、代码库考古与事故复盘。"
              "PDF / EPUB / HTML 免费下载。作者花叔在 **DSH 开源日（2026-08-13，MIT）后 24 小时内**写完。",
        analogy="**官方文档没有的部分**（系统提示词原文、默认启动清单、原始日志）正好补上我们"
                "「读源码」之外最缺的一环：**运行时真实长什么样**。前两辑一直把它标成「被两篇文引为"
                "一手实测、但取不到 URL」—— 本轮取到了，**待办闭环**。",
        ext=(72, "7.2/10", "**先读「129 行启动清单」与三份原始日志**这两块 —— "
                           "它们能直接对照我们自己 harness 的启动开销（本机固定前缀实测 18,828 token）"),
        use=(68, "6.8/10", "免费 PDF/EPUB/HTML。⚠️ 两条边界：①**CC BY-NC-SA 4.0**（非商用）；"
                           "②本辑**只核实到 README 自述，正文未逐页读** → 引用时标清来源层级"),
        src="建于 2026-08-14 · 最近推送 2026-09-24 · 1302★ · CC BY-NC-SA 4.0 · HTML · 信源 [1135]",
    ),
    dict(
        nid="rpm28c9", name="dsh-vision-router（给纯文本 agent 装上眼睛）",
        url="https://github.com/ysr666/dsh-vision-router",
        lang="JavaScript", stars="1116",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已核实待试")],
        plain="给「纯文本」的 DSH agent 装上眼睛：内置**免 key 的视觉链**，外加像素级视觉工具"
              "（问答、grounding、裁剪、**像素 diff**、取色、**OCR**、SVG 描摹、抠图、截图）。"
              "一条命令装，**无需 Python**。",
        analogy="我们做视觉小说时最缺的正是**「让 agent 自己看图对不对」** —— "
                "现有做法是人工看截图（还踩过「按缩放看会吞掉低对比度小字」的坑）。"
                "「把图片轮次当成普通工具调用轮」这个设计很巧。",
        ext=(76, "7.6/10", "**像素 diff + OCR 可以直接接进我们的界面验收**"
                           "（现在还在靠人眼看截图）"),
        use=(72, "7.2/10", "MIT、免 key、**无需 Python** → Windows 环境友好，装错成本低。"
                           "⚠️ 单人维护，当辅助别当唯一防线"),
        src="最近推送 2026-09-24 · 1116★ · MIT · JavaScript · 信源 [1136]",
    ),
    dict(
        nid="rpm28c10", name="okf-agent-memory（Git 原生记忆：记忆即文件，可 diff 可版本化）",
        url="https://github.com/okf-memory/okf-agent-memory",
        lang="Go", stars="722",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="**Git 原生**的 agent 持久记忆，实现 Google **OKF v0.2** 规范；纯 Go、内嵌 MCP server，"
              "内存内 BM25 搜索**亚 300µs**、渐进式披露，宣称省 **80%** 上下文膨胀，**零外部数据库**。",
        analogy="「Git 原生」意味着**记忆可 diff、可版本化、可同步** —— 正好贴合我们"
                "「一切产出进仓库 + 靠 `git status` 收尾对账」的习惯。记忆要是能进 git，"
                "「谁改了什么、什么时候改的」就不用靠自觉了。",
        ext=(70, "7.0/10", "**「记忆即文件 + 进 git」这条路线对我们兼容性最好**，"
                           "不用引入一个新的数据库"),
        use=(68, "6.8/10", "MIT、纯 Go 无依赖、Windows 友好。⚠️ 注意它记的是**事实**，"
                           "而我们的 `mistakes/` 记的是**教训** —— 两类不该混在一个文件里"),
        src="最近推送 2026-09-23 · 722★ · MIT · Go · 信源 [1137]",
    ),
    dict(
        nid="rpm28c11", name="huashu-report（报告规范是从 41 份真报告反推的）",
        url="https://github.com/alchaincyf/huashu-report",
        lang="Markdown", stars="422",
        tags=[("t-make", "AI × 约定"), ("t-ok", "已登记未安装")],
        plain="**机构级研究报告 skill**：规范从 2026 年顶级机构报告**反向提炼**（"
              "**42 份采集 / 41 份进量化基线**：Stanford / McKinsey / BCG / OpenAI / PwC / World Bank），"
              "**6 种报告原型 + 8 种图表模式** + 可复用生产流水线，跨 agent 通用。",
        analogy="我们在做的事就是「调研 → 单文件 HTML 报告」。它的做法是**不凭空写规范，"
                "而是从 41 份真报告反推** —— 这正是我们「判据外移、先核实再落笔」的同构做法。"
                "**拿它当对标，比拿它当模板更有用。**",
        ext=(74, "7.4/10", "**6 种报告原型可以直接对照我们现有的报告结构**，"
                           "问「我们为什么一直是同一种形状」"),
        use=(60, "6.0/10", "纯 skill / Markdown，零运行成本。⚠️ **「41 份进量化基线」是作者自述，"
                           "本辑未抽样验证** → 别把它的数字当结论引用"),
        src="最近推送 2026-09-24 · 422★ · Markdown · 信源 [1138]",
    ),
    dict(
        nid="rpm28c12", name="GameStringer（识别引擎 → 抽文本 → AI 翻译 → 打回补丁）",
        url="https://github.com/rouges78/GameStringer",
        lang="TypeScript", stars="119",
        tags=[("t-make", "AI × 游戏"), ("t-ok", "已核实待试")],
        plain="桌面程序：自动**识别单机游戏的引擎、抽取文本、用本地或云端 AI 翻译、再把译文补丁打回游戏**。"
              "支持 **20+ 引擎、20+ AI 提供方、11 种界面语言**。",
        analogy="和视觉小说本地化**直接对口**；「识别引擎 → 抽文本 → 翻译 → 回填」这条流水线"
                "本身就是可抄的架构，而且**可接本地 Ollama 不上云**。",
        ext=(62, "6.2/10", "**回填逻辑**最值得看：我们现在改文本是手工改 `.rpy`，"
                           "它的「补丁回填」思路可以借"),
        use=(55, "5.5/10", "⚠️ **source-available，不是标准 OSI 许可** → **商用前必须看条款**；"
                           "只当参考实现，别把它的代码搬进项目"),
        src="最近推送 2026-09-23 · 119★ · NOASSERTION · TypeScript · 信源 [1139]",
    ),
    dict(
        nid="rpm28c13", name="sqz（零 LLM 调用的上下文压缩器）",
        url="https://github.com/ojuschugh1/sqz",
        lang="Rust", stars="629",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="Rust 写的上下文压缩器，在工具输出进入模型前压缩，把**重复内容去重成 13-token 的引用**；"
              "Claude Code / Cursor / Codex / Zed 及任意 MCP 客户端可用，**零 LLM 调用**。",
        analogy="**零 LLM 调用**是关键：不额外占本地算力、不引入延迟、不需要第二个模型。"
                "对 16GB 机器这是「**先上它、看 0 成本能省多少**」的那一步 —— 省不动再考虑上模型压缩。",
        ext=(66, "6.6/10", "**确定性去重**符合我们「判据外移到确定性代码」的主线；"
                           "可作 headroom 之外的低成本对照"),
        use=(70, "7.0/10", "Rust 单二进制、本地零开销。⚠️ **license 未核实**（`gh api` 返回 null）"
                           "→ 引用时不要写许可证名"),
        src="最近推送 2026-09-24 · 629★ · 未声明协议 · Rust · 信源 [1140]",
    ),
]

FOOTNOTES = [
    (1128, "https://github.com/headroomlabs-ai/headroom", "headroomlabs-ai/headroom",
     "73669★ · Apache-2.0 · Python · 2026-09-24 · GitHub REST API 实测"),
    (1129, "https://github.com/omnigent-ai/omnigent", "omnigent-ai/omnigent",
     "10197★ · Apache-2.0 · Python · 2026-09-24 · GitHub REST API 实测"),
    (1130, "https://github.com/Gentleman-Programming/engram", "Gentleman-Programming/engram",
     "6786★ · MIT · Go · 2026-09-24 · GitHub REST API 实测"),
    (1131, "https://github.com/alchaincyf/darwin-skill", "alchaincyf/darwin-skill",
     "6086★ · Markdown · 2026-09-24 · GitHub REST API 实测"),
    (1132, "https://github.com/PawanOsman/OpenCursor", "PawanOsman/OpenCursor",
     "6024★ · license=null（未核实）· TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1133, "https://github.com/Dataojitori/nocturne_memory", "Dataojitori/nocturne_memory",
     "1371★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
    (1134, "https://github.com/alchaincyf/huashu-skills", "alchaincyf/huashu-skills",
     "1607★ · Markdown · 2026-09-24 · GitHub REST API 实测"),
    (1135, "https://github.com/alchaincyf/deepseek-harness-orange-book",
     "alchaincyf/deepseek-harness-orange-book",
     "1302★ · 正文声明 CC BY-NC-SA 4.0（license 字段为 null）· 建于 2026-08-14 · HTML · 2026-09-24 实测"),
    (1136, "https://github.com/ysr666/dsh-vision-router", "ysr666/dsh-vision-router",
     "1116★ · MIT · JavaScript · 2026-09-24 · GitHub REST API 实测"),
    (1137, "https://github.com/okf-memory/okf-agent-memory", "okf-memory/okf-agent-memory",
     "722★ · MIT · Go · 2026-09-23 · GitHub REST API 实测"),
    (1138, "https://github.com/alchaincyf/huashu-report", "alchaincyf/huashu-report",
     "422★ · Markdown · 2026-09-24 · GitHub REST API 实测"),
    (1139, "https://github.com/rouges78/GameStringer", "rouges78/GameStringer",
     "119★ · NOASSERTION · TypeScript · 2026-09-23 · GitHub REST API 实测"),
    (1140, "https://github.com/ojuschugh1/sqz", "ojuschugh1/sqz",
     "629★ · license=null（未核实）· Rust · 2026-09-24 · GitHub REST API 实测"),
]


def b(s):
    """把 markdown 的 **粗体** 转成 HTML 的 <strong>。"""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)


def render_card(c):
    n = c["nid"]
    name_inner = ('<a href="%s" target="_blank" data-page-node-id="%sn">%s</a>'
                  % (c["url"], n, c["name"])) if c["url"] else c["name"]
    tags = "\n".join(
        '          <span class="tag %s" data-page-node-id="%st%d">%s</span>'
        % (cls, n, i, txt) for i, (cls, txt) in enumerate(c["tags"], 1))
    extra = ""
    if c.get("warn"):
        extra += ('        <div class="analogy" data-page-node-id="%sw"><b data-page-node-id="%swb">'
                  '注意：</b>%s</div>\n' % (n, n, c["warn"]))
    return '''      <div class="card" data-page-node-id="{n}">
        <div class="card-top" data-page-node-id="{n}t">
          <span class="card-name" data-page-node-id="{n}mn">{name}</span>
          <span class="lang" data-page-node-id="{n}l">{lang}</span>
          <span class="stars" data-page-node-id="{n}s">{stars}</span>
{tags}
        </div>
        <p class="plain" data-page-node-id="{n}p">{plain}</p>
        <div class="analogy" data-page-node-id="{n}a"><b data-page-node-id="{n}ab">打个比方：</b>{analogy}</div>
{extra}        <div class="grid2" data-page-node-id="{n}g">
          <div class="mini" data-page-node-id="{n}m1"><span class="lbl" data-page-node-id="{n}m1l">可拓展性</span><div class="bar" data-page-node-id="{n}m1b"><div class="bar-track" data-page-node-id="{n}m1t"><div class="bar-fill" style="width:{ew}%;background:var(--make)" data-page-node-id="{n}m1f"></div></div><span class="bar-num" data-page-node-id="{n}m1n">{en}</span></div><div class="val" style="margin-top:6px" data-page-node-id="{n}m1v">{ev}</div></div>
          <div class="mini" data-page-node-id="{n}m2"><span class="lbl" data-page-node-id="{n}m2l">实用性</span><div class="bar" data-page-node-id="{n}m2b"><div class="bar-track" data-page-node-id="{n}m2t"><div class="bar-fill" style="width:{uw}%;background:var(--make)" data-page-node-id="{n}m2f"></div></div><span class="bar-num" data-page-node-id="{n}m2n">{un}</span></div><div class="val" style="margin-top:6px" data-page-node-id="{n}m2v">{uv}</div></div>
        </div>
        <div class="src-line" data-page-node-id="{n}c">{src}</div>
      </div>
'''.format(n=n, name=name_inner, lang=c["lang"], stars=c["stars"], tags=tags,
           plain=b(c["plain"]), analogy=b(c["analogy"]), extra=b(extra),
           ew=c["ext"][0], en=c["ext"][1], ev=b(c["ext"][2]),
           uw=c["use"][0], un=c["use"][1], uv=b(c["use"][2]), src=c["src"])


def main():
    src = open(HTML, encoding="utf-8").read()

    if MARKER in src:
        print("已存在%s，跳过（幂等）" % MARKER)
        return 0

    bad = []
    for o in HEAD_OLD:
        if src.count(o) != 1:
            bad.append("页头锚点出现 %d 次（要求 1）：%s" % (src.count(o), o[:60]))
    for num, _u, _s, _m in FOOTNOTES:
        if ('id="r%s"' % num) in src:
            bad.append("信源 [%s] 已被占用" % num)
    for c in CARDS:
        if c["url"] and c["url"].split("github.com/")[-1].lower() in src.lower():
            bad.append("仓库已存在，别重复登记：%s" % c["url"])

    si = src.find(SECTION_S3)
    if src.count(SECTION_S3) != 1:
        bad.append("%s 出现 %d 次（要求 1）" % (SECTION_S3, src.count(SECTION_S3)))
        ins = -1
    else:
        ins = si
        seg = src[src.find("<section", 10000):si]
        d = 0
        for m in re.finditer(r"<div[\s>]|</div>", seg):
            d += 1 if m.group(0).startswith("<div") else -1
        if d != 0:
            bad.append("插入点前 div 深度为 %d（应为 0），会嵌错层" % d)

    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次（要求 1）" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if bad:
        print("锚点校验失败，未改动文件：")
        for x in bad:
            print("  " + x)
        return 1

    desc = ('第二十二辑的 GitHub 路逐仓库走 REST API 实测（stars / license / language / updated 无一估算），'
            '再逐条 grep 过 19 份存档 + 1128 项索引。本辑候选池是历史最大（42 个），'
            '本版收紧到 13 项，其余在第二十二辑的「下一辑待办」里逐条登记。'
            '<strong>本辑主线是「待办闭环 + 一手源」—— 追了两轮的'
            '《DeepSeek Harness：从开机到拆开》一手源找到了（★1302），并顺带查出整个橙皮书 / skill 生态。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm28g">',
             '      <div class="group-title" data-page-node-id="rpm28gt">🆕 第二十八版增补 · 待办闭环 + 一手源（13 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm28gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm28r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm28ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]

    for old, new in zip(HEAD_OLD, HEAD_NEW):
        src = src.replace(old, new, 1)

    open(HTML, "w", encoding="utf-8", newline="\n").write(src)

    print("OK  插入 %d 张卡片 + %d 条信源脚注（[%s]-[%s]）+ 3 处页头计数"
          % (len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE,
             FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
