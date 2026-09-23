# -*- coding: utf-8 -*-
"""第二十四版增补：把第十八辑 GitHub 那一路新发现的 10 个条目登记进 index.html。

本辑 GitHub 调研：15 个查询 → 147 行候选 → 逐条 `gh api repos/<r>` 实测
（stars / forks / license / language / pushed_at / created_at 全部走 REST API，无一估算）
→ 逐条 grep 过 17 份存档 + 1094 项索引，剔掉已收录
（fast-compaction-dsh / VibeGauge / dsh-desktop 类目 / jev-compaction 类目等）与一批 0★ 空壳
（`Hakeperty/AI-Game-engine` / `notfennecks/GameMatch` / 各类 `spec-kit` 复刻等），
剩下 10 条"与本工作区直接对话"的。

数据来源：2026-09-23 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v24_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1093"'
FIRST_NEW_FOOTNOTE = 1094
MARKER = "第二十四版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十三版增补 2026-09-23</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1094 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项 + 第二十二版增补 6 项 + 第二十三版增补 9 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十四版增补 2026-09-23</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1104 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项 + 第二十二版增补 6 项 + 第二十三版增补 9 项 + 第二十四版增补 10 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm24c1", name="clearai-dsh（把「认识论循环」装进 DSH）",
        url="https://github.com/Clearailhc/clearai-dsh",
        lang="JavaScript", stars="381",
        tags=[("t-make", "AI × 认识论"), ("t-ok", "只登记未安装")],
        plain="**DSH 生态里星最高的第三方插件**（381★）。它给的不是某个功能，是一条**纪律**："
              "**frame（框定）→ hypothesize（假设）→ plan → observe（观察）→ "
              "verify（验证）→ evaluate（评估）→ record（记录）** 七段循环。"
              "产物叫**领域本体** —— 你这个项目自己的词汇表和知识条目，下轮能按概念取回。"
              "README 原话：**每条边都要被证据和独立评估检验过**。",
        analogy="我们的 `mistakes/`（18 条错误记忆）和 `agent-house-rules.md`（39 条房规）"
                "其实在做同一件事的下半段 —— **记录**。它补的是上半段：**先有假设、再有观察、然后才许记录。**",
        ext=(88, "8.8/10", "**七段循环可以拆开单独用**：即使不装它，「frame → hypothesize → "
                            "verify」这三段也足够改掉「让 AI 直接给结论」的坏习惯"),
        use=(70, "7.0/10", "**只登记未安装**：本轮没有 DSH 会话在跑，装了测不出东西。"
                            "而且它产出的「本体」需要连续多轮研究才长得起来"),
        warn="**Apache-2.0，但它是「研究型」插件**：它假定你在做探索性工作。"
             "日常改 bug 这种明确任务用它七段循环，是**拿牛刀杀鸡且会拖慢节奏**。",
        src="创建 2026-09-12 · 最近推送 2026-09-23 · 381★ · Apache-2.0 · JavaScript · 信源 [1094]",
    ),
    dict(
        nid="rpm24c2", name="dsh-context（把上下文账单摊开给你看）",
        url="https://github.com/bowenliang123/dsh-context",
        lang="TypeScript", stars="1,502",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "强烈建议第一步装")],
        plain="**给 DSH 装一块「电表」**。它把每一次请求的上下文拆成六色："
              "系统提示 / **工具 Schema** / 你的消息 / 注入的上下文 / 助手回复 / 工具结果，"
              "直接显示「**77.6k / 262.1k（30%）**」，还会列出**最贵的 5 个工具 Schema** —— "
              "因为很多会话的隐形成本就藏在那儿。另有逐请求演进图、注入与压缩事件标记、"
              "以及一个跨会话的仪表盘（用量、成本、**缓存命中率**、活动热力图）。",
        analogy="**这就是第十八辑自测那件事的现成版本。** 我们用自己写的 "
                "`_tools/harness_tax_probe.py` 量出「调用侧固定前缀 20,900 token，"
                "其中 MCP 占 50%」，它做的是同一件事，只不过**长在会话里、能看历史曲线**。",
        ext=(92, "9.2/10", "**本辑第一顺位**：1,502★ / Apache-2.0 / 免构建免重启"
                            "（`dsh plugin --profile web add dsh-context`）。"
                            "「最贵的 5 个工具 Schema」这一栏直接对应我们的发现"),
        use=(80, "8.0/10", "**本机 `dsh 0.1.0-rc.6` 已装，随时可上**。"
                            "建议顺序：先装它把账单看清楚，再决定要不要上压缩类插件"),
        warn="**它读的是官方计量数据**（和输入框那个占用环同源），所以**数字不会打架** —— "
             "这一点比自己估的强。但它只解决「看得见」，不解决「怎么省」。",
        src="创建 2026-08-14 · 最近推送 2026-09-23 · 1,502★ · Apache-2.0 · TypeScript · 信源 [1095]",
    ),
    dict(
        nid="rpm24c3", name="ccompactor（把会话压成一份能交接的档案）",
        url="https://github.com/ccompactor/ccompactor",
        lang="TypeScript", stars="21",
        tags=[("t-make", "AI × 交接"), ("t-ok", "思路直接可抄")],
        plain="**把任意一个 coding agent 的会话（Claude Code / Codex / Pi）提取成"
              "「紧凑、可验证、带出处」的交接件**，让另一个 agent 能直接接着干。"
              "四条命令：`list` 看有哪些会话 / `find \"auth migration\"` 按话题找 / "
              "`extract claude:last` 出档案 / `handoff claude:last --to codex --run` 直接换工具续跑。"
              "它是 `handyutils/sctxx` 的 TypeScript 版（同一思路的第二个实现）。",
        analogy="**第十八辑那批中文帖说的「50% 交接规则」，缺的就是这么一个东西。** "
                "我们现在是靠「写 memory 文件」手工交接 —— 有损失，但至少是可控的损失。",
        ext=(80, "8.0/10", "**跨工具换手是它的独门点**：`--to codex` 意味着"
                            "「这个 agent 干到一半，换个 agent 接着干」不再是手工活"),
        use=(62, "6.2/10", "**只登记未安装**：本机没有 Claude Code / Codex 的会话文件"
                            "（我们走的是 WorkBuddy + 自己的桥），`claude:last` 取不到东西"),
        warn="**它压的是别人的会话格式**。如果有一天我们自己写的东西要长期跑，"
             "「带出处的交接件」这个格式值得先抄过来 —— **出处是关键**，"
             "没有出处的摘要就是我们第十七辑踩过的坑。",
        src="创建 2026-09-12 · 最近推送 2026-09-14 · 21★ · MIT · TypeScript · 信源 [1096]",
    ),
    dict(
        nid="rpm24c4", name="jev-compaction（只打分、不写字的压缩器）",
        url="https://github.com/Waxmell114514/jev-compaction",
        lang="Python", stars="3",
        tags=[("t-make", "AI × 上下文"), ("t-new", "本辑最新原理")],
        plain="**一句话纲领（README 原话）**：*一个只能打分、永远不能写字的上下文压缩器 —— "
              "这样 agent 的记忆里就不可能有原始记录中没有的事实。*"
              "这就是**逐字压缩**和**摘要压缩**的分界线：摘要是**生成**，生成就会改写；"
              "逐字压缩只做**选择** —— 打分、把低分行挪出去，保留下来的每一行**逐字节原样**，"
              "而且 append-only 的前缀**从不让 prompt cache 失效**。"
              "作者自测：一段 `npm install` 输出 749 → 391 token（−48%），整趟打分成本 $0.000031。",
        analogy="**第十七辑那句「摘要会把 `orderExport.ts:42:19` 变成『之前失败了』」，"
                "这一辑终于有人给出了替代方案。** 我们的 `mistakes/` 其实也是这个思路 —— "
                "**只记录发生了什么，不润色。**",
        ext=(85, "8.5/10", "**原理比星数重要**：「只打分不写」是一条可以自己实现的判据，"
                            "不依赖它这个仓库。我们的闸门全是这个路子"),
        use=(45, "4.5/10", "**3★、作者自测、需要 Jev 服务**：数字没有第三方复核，"
                            "本机也没有在跑的 agent 会话可以挂上去试"),
        warn="**$0.000031 是打分成本，不是省下的钱。** 真正的收益在「保留行逐字节原样」—— "
             "**可复查**才是它相对摘要的核心优势，不是那 48%。",
        src="创建 2026-09-19 · 最近推送 2026-09-23 · 3★ · MIT · Python · 信源 [1097]",
    ),
    dict(
        nid="rpm24c5", name="mcp-context-budget（开 MCP 之前先称一下）",
        url="https://github.com/KaryawanSurga/mcp-context-budget",
        lang="TypeScript", stars="1",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已用自研等价物")],
        plain="**连上你的 MCP 服务器，读出所有工具定义，按上下文 token 给每个工具排名** —— "
              "名字、描述、输入 schema 一起算。官方建议的三个使用时机："
              "**启用一个服务器之前** / **觉得 agent 变慢的时候** / **放进 CI 防止工具膨胀**。"
              "它自己的定位是「TokenSaver 管出去的，Context Budget 管进来的」。",
        analogy="**和我们的自测结论撞在同一处。** 实测：本机 7 个 MCP 服务器 / 95 个工具 = "
                "**10,519 token，占调用侧固定前缀的 50%**，其中 GitHub 一个就 45 个工具 / 2,293 token "
                "—— **连上就付，不用也付**。",
        ext=(78, "7.8/10", "**「启用前先量」这个动作是通用的**，不依赖它这个实现。"
                            "我们已用 `_tools/harness_tax_probe.py` 覆盖了同一需求"),
        use=(55, "5.5/10", "**1★、Node ≥ 20、需要真的连上服务器**：价值在提醒，不在工具本身。"
                            "但「放进 CI 防膨胀」这条对我们是个新角度"),
        warn="**1★ = 没有任何第三方用过。** 但它的**姊妹项目 TokenSaver** 提示了一个对称关系："
             "**进来的要称，出去的也要省** —— 我们只做了前半边。",
        src="创建 2026-09-18 · 最近推送 2026-09-18 · 1★ · MIT · TypeScript · 信源 [1098]",
    ),
    dict(
        nid="rpm24c6", name="dsh-novel-forge（把长篇写作的通病变成硬约束）",
        url="https://github.com/huangziyuan-general/dsh-novel-forge",
        lang="JavaScript", stars="13",
        tags=[("t-make", "AI × 写作"), ("t-ok", "与 check_dialogue 同源")],
        plain="**小说锻炉**：把 AI 长篇写作的通病做成**代码强制的硬约束** —— "
              "**事实账本**（设定不许自相矛盾）/ 上下文包 / **阶段门禁** / "
              "**零费用去 AI 味扫描** / 确定性审计 / 提案制修订。"
              "「零费用」这三个字是关键：**去 AI 味靠确定性规则扫，不靠再叫一次模型。**",
        analogy="**和我们第 5 轮的 `check_dialogue.py`（六条规则：编辑脚注 / 旁白套话 / "
                "填充词连用 / 朗读测试 42 字 / 角色口癖 / 口吻分化）是同一条路线的另一头** —— "
                "它管小说，我们管对白，但**都拒绝「再叫一次模型来判断」**。",
        ext=(82, "8.2/10", "**「事实账本 + 阶段门禁」这两个是我们可以直接抄的结构**："
                            "我们的 `ENDINGS` / `ACHIEVEMENTS` / `CHAPTERS` 三张表其实就是事实账本"),
        use=(58, "5.8/10", "**只登记未安装**：面向长篇小说，游戏线已终止。"
                            "但它的**零费用扫描**思路对「对白 AI 味」这条未闭合缺口是现成参照"),
        warn="**13★ 且是个人项目**，规则质量取决于作者自己踩过多少坑。"
             "抄**结构**（账本 / 门禁 / 确定性扫描），不要直接抄**规则表**。",
        src="创建 2026-09-11 · 最近推送 2026-09-21 · 13★ · MIT · JavaScript · 信源 [1099]",
    ),
    dict(
        nid="rpm24c7", name="dsh-nexttavern（DSH 长篇角色扮演，带长篇记忆）",
        url="https://github.com/a86582751/dsh-nexttavern",
        lang="JavaScript", stars="103",
        tags=[("t-make", "AI × 角色扮演"), ("t-new", "角色一致性老问题")],
        plain="**把 DSH 变成酒馆**：SillyTavern 角色卡导入、行动选项卡、分支对话管理、"
              "**长篇记忆**、**关键词与语义混合检索**、交互式角色卡创作。"
              "这些东西合起来回答的是一个具体问题：**角色在很长的时间里怎么不跑偏。**",
        analogy="**和第 3 轮「角色一致性三档方案」是同一道题。** 我们最后走的是"
                "「参考图 + 图生图」的**视觉**一致性（9/9 零漂移，没上 LoRA）；"
                "它解决的是**性格与记忆**的一致性 —— 另一半。",
        ext=(72, "7.2/10", "**GPL-3.0 是硬约束**：传染性协议，不能并进 MIT 系项目。"
                            "但「关键词 + 语义混合检索」这个做法可以自己实现"),
        use=(48, "4.8/10", "**只登记未安装**：游戏线已终止，当下没有角色扮演需求。"
                            "留着是因为 **NPC 记忆是我们列了六辑都没解决的题**"),
        warn="**GPL-3.0 + 个人项目**。而且角色扮演类插件最容易踩的是**内容合规** —— "
             "即便将来要用，也只能是「读它的记忆结构」。",
        src="创建 2026-09-11 · 最近推送 2026-09-23 · 103★ · GPL-3.0 · JavaScript · 信源 [1100]",
    ),
    dict(
        nid="rpm24c8", name="AetherFX（AI 能署名的游戏特效）",
        url="https://github.com/holokat/AetherFX",
        lang="Python", stars="1",
        tags=[("t-make", "游戏 × 特效"), ("t-new", "可署名三件套")],
        plain="**游戏 VFX，但作者可以是 agent**：描述一个效果（或把概念图丢给 agent），"
              "它用**带类型的积木块**拼出效果、**看自己的渲染**、自己迭代，"
              "产物是**一个小 JSON 文件**，到处都能播。三个设计点很硬："
              "**每一个编辑动作都是 MCP 工具**（附带 agent 需要的说明）/ "
              "**确定性可移植**（不写 shader、无二进制资产，贴图和网格全是程序化的）/ "
              "同一个模拟在 studio、导出、游戏里（一个小 C 库）跑出来一样。",
        analogy="**这就是我们一直说的「闸门要放在真实路径上」的正面样本。** "
                "它把「效果」变成**文本 + 确定性模拟**，于是**可 diff、可版本管理、可断言** "
                "—— 对比美术资产那种「生成完只能靠眼睛看」的东西，是另一个物种。",
        ext=(80, "8.0/10", "**1★，但三件套（agent 可署名 / 确定性 / 可移植）是通用范式**："
                            "任何「让 AI 产出资产」的环节都该往这个方向靠"),
        use=(35, "3.5/10", "**本机无 GPU 预览条件，且游戏线已终止**。纯登记"),
        warn="**1★ = 没人验证过。** 但「贴图和网格全程序化 → 无二进制资产」这一条，"
             "对我们第 7 轮那个 **62MB 发行包瘦身**的题是正面答案。",
        src="创建 2026-09-17 · 最近推送 2026-09-20 · 1★ · MIT · Python · 信源 [1101]",
    ),
    dict(
        nid="rpm24c9", name="UnityAssetDB（把资产引用变成可查询的数据库）",
        url="https://github.com/song-chaoyang/UnityAssetDB",
        lang="Rust", stars="49",
        tags=[("t-make", "游戏 × 工程化"), ("t-ok", "思路直接可抄")],
        plain="**Rust + SQLite + tree-sitter**：把工程里**所有 Unity 资产引用**变成"
              "一个可查询的数据库，提供 CLI 和 Web 界面。"
              "它解决的是一件很具体的事：**当 AI 问「这个 prefab 被谁用了」，"
              "别让它 grep 整个工程。**",
        analogy="**和我们的 `check_font_coverage.py` 是同一个思路的不同应用**："
                "把「需要全工程扫描才知道的事实」**预先算成一张表**，"
                "然后让 agent 查表而不是读文件 —— **省下的正是上下文。**",
        ext=(76, "7.6/10", "**「预计算成表 + 让 agent 查」是省上下文的正解**，"
                            "与引擎无关。我们的 `CHAPTERS` / `ENDINGS` 表已经在做这件事"),
        use=(40, "4.0/10", "**本机无 Unity 工程**，纯登记。但 49★ / MIT / Rust 说明它是正经工具"),
        warn="**它是「查询工具」不是「AI 工具」** —— 没有模型调用。"
             "这反而是优点：**确定性、零 token、可进 CI。**",
        src="创建 2026-08-21 · 最近推送 2026-09-22 · 49★ · MIT · Rust · 信源 [1102]",
    ),
    dict(
        nid="rpm24c10", name="URKit（Unity Mono 与 IL2CPP 通用 modding 框架）",
        url="https://github.com/Jadis0x/URKit",
        lang="C++", stars="25",
        tags=[("t-make", "游戏 × Modding"), ("t-ok", "与 DroidSpy 互补")],
        plain="**原生 C++ 的 Unity modding 框架，同时支持 Mono 和 IL2CPP 两种后端**。"
              "IL2CPP 这一半是难点：它把 C# 编译成了原生代码，"
              "常规的反射式注入在 IL2CPP 上不管用。",
        analogy="**和第七辑收的 DroidSpy（手机端 dnSpy，Unity Mono 解包 + MCP）正好是一对**："
                "**DroidSpy 负责「拆开看」，URKit 负责「装回去」。** "
                "对一个有 73 款游戏解包积累的人来说，这两半合起来才是完整链路。",
        ext=(70, "7.0/10", "**IL2CPP 支持是稀缺能力**：Unity 新版本默认 IL2CPP，"
                            "只支持 Mono 的工具会越来越不够用"),
        use=(42, "4.2/10", "**只登记未安装**：本机没有在做的 mod 工程，"
                            "且 C++ 框架的构建门槛高于脚本类工具"),
        warn="**modding 框架天然踩在合规边界上**（第七辑的 Harbour Masters 争议、"
             "房规里的同人三条边界）。**自用分析可以，分发要慎重。**",
        src="创建 2026-07-17 · 最近推送 2026-09-23 · 25★ · MIT · C++ · 信源 [1103]",
    ),
]

FOOTNOTES = [
    ("1094", "https://github.com/Clearailhc/clearai-dsh",
     "Clearailhc/clearai-dsh", "381 · 2026-09-23 · Apache-2.0 · JavaScript"),
    ("1095", "https://github.com/bowenliang123/dsh-context",
     "bowenliang123/dsh-context", "1,502 · 2026-09-23 · Apache-2.0 · TypeScript"),
    ("1096", "https://github.com/ccompactor/ccompactor",
     "ccompactor/ccompactor", "21 · 2026-09-14 · MIT · TypeScript"),
    ("1097", "https://github.com/Waxmell114514/jev-compaction",
     "Waxmell114514/jev-compaction", "3 · 2026-09-23 · MIT · Python"),
    ("1098", "https://github.com/KaryawanSurga/mcp-context-budget",
     "KaryawanSurga/mcp-context-budget", "1 · 2026-09-18 · MIT · TypeScript"),
    ("1099", "https://github.com/huangziyuan-general/dsh-novel-forge",
     "huangziyuan-general/dsh-novel-forge", "13 · 2026-09-21 · MIT · JavaScript"),
    ("1100", "https://github.com/a86582751/dsh-nexttavern",
     "a86582751/dsh-nexttavern", "103 · 2026-09-23 · GPL-3.0 · JavaScript"),
    ("1101", "https://github.com/holokat/AetherFX",
     "holokat/AetherFX", "1 · 2026-09-20 · MIT · Python"),
    ("1102", "https://github.com/song-chaoyang/UnityAssetDB",
     "song-chaoyang/UnityAssetDB", "49 · 2026-09-22 · MIT · Rust"),
    ("1103", "https://github.com/Jadis0x/URKit",
     "Jadis0x/URKit", "25 · 2026-09-23 · MIT · C++"),
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
    if si < 0:
        bad.append("找不到 %s" % SECTION_S3)
        ins = -1
    else:
        ins = src.find('<div class="group"', si)
        if ins < 0:
            bad.append("找不到插入点（s3 之后的第一个 group）")
        else:
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

    desc = ('第十八辑的 GitHub 那一路跑了 <strong>15 个查询 / 147 行候选</strong>，'
            '逐条走 REST API 实测 stars / forks / license / language / pushed / created，'
            '<strong>再逐条 grep 过 17 份存档 + 1094 项索引</strong>。'
            '本版主线是「<strong>账到期</strong>」—— 三笔同时到期的账：'
            'vibe coding 的维护账（第三个月崩）、摘要压缩的失真账'
            '（「只打分不写」的逐字压缩阵营成型）、模型发布的口径账'
            '（20 个真实已合并 commit 重放，Opus 5.5 零回归 vs Sol 五次回归）。'
            '<strong>本辑唯一实测：自己的 harness tax —— 调用侧固定前缀 20,900 token，'
            '其中 MCP 工具定义占 50%（95 个工具 / 10,519 token）。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm24g">',
             '      <div class="group-title" data-page-node-id="rpm24gt">🆕 第二十四版增补 · 账到期（10 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm24gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm24r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm24ra%s">%s</a> — %s</div>'
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
