# -*- coding: utf-8 -*-
"""第二十三版增补：把第十七辑 GitHub 那一路新发现的 9 个条目登记进 index.html。

本辑 GitHub 调研：25 个查询 → 274 行候选 → 逐条 `gh api repos/<r>` 实测
（stars / forks / license / language / pushed_at / created_at 全部走 REST API，无一估算）
→ 剔掉 8 条已收录（grokbot-field-notes / JakeSelby-agent-harness / fennara-godot-ai /
hybridindie-godot-mcp / tallslab-threeforge / ruc-datalab-EvoOntology / CoplayDev-unity-mcp /
lovetimo0421-yumina-oss）与一批 0★ 空壳，剩下 9 条"与本工作区直接对话"的。

数据来源：2026-09-23 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v23_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1084"'
FIRST_NEW_FOOTNOTE = 1085
MARKER = "第二十三版增补"

HEAD_OLD = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十二版增补 2026-09-23</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1085 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项 + 第二十二版增补 6 项（均与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVCzIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第二十三版增补 2026-09-23</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1094 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项 + 第十六版增补 5 项 + 第十七版增补 6 项 + 第十八版增补 2 项 + 第十九版增补 1 项 + 第二十版增补 1 项 + 第二十一版增补 4 项 + 第二十二版增补 6 项 + 第二十三版增补 9 项（均与上版零重复）</span>',
]

CARDS = [
    dict(
        nid="rpm23c1", name="deepseek-harness（DSH 本体：万物皆插件）",
        url="https://github.com/deepseek-ai/deepseek-harness",
        lang="TypeScript", stars="233,987",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "本机已在用")],
        plain="**DSH 就是「外壳」（harness）本身**：它不训练模型，只把**模型放进一张工作台**里 —— "
              "读文件、执行命令、调插件、拆子任务，最后产出可运行的代码改动。"
              "它的设计口号只有一句：**Everything is a Plugin** —— 连桌面端、Web 端、插件市场"
              "都是插件。启动方式 = 在 `$DSH_HOME/profiles` 下叠一串**插件包补丁层**，"
              "再叠你自己的覆盖层（`dsh --profile web` / `--profile headless \"run the tests\"`）。",
        analogy="我们一直用「桥 → 上财千问 → 本地 Ollama」这套自建路线（`ccgs-cn-config`）。"
                "DSH 是**同一条命题的官方版本**：外壳决定固定开销、决定工具怎么暴露、决定上下文怎么回收 "
                "—— 第十六辑量到的 harness tax，这里就是那个「外壳」的正式形态。",
        ext=(90, "9.0/10", "**本辑第一顺位**：本机已装 `dsh 0.1.0-rc.6` 并跑通过，"
                            "插件系统（`dsh plugin add @scope/name`，底层就是 pnpm）"
                            "意味着「上下文管理」可以按需换装，而不用改自己写的桥"),
        use=(85, "8.5/10", "**真在用**：本工作区的技能库里已有 `dsh-session-log-repair`"
                            "（修 DSH 会话日志损坏 / 工作区迁移）—— 说明这条链路是活的，不是纸上的"),
        warn="**「可插拔」的另一面是供应链**：`dsh plugin` 走的是 pnpm 装包，"
             "插件会以**当前 dsh 进程的权限**运行（社区插件 README 原话）。"
             "装之前先读它的 SKILL.md / 脚本 / 有没有非必要网络请求 —— 与门房规 #33 同一条理。",
        src="创建 2026-08-13 · 最近推送 2026-09-22 · 233,987★ · MIT · TypeScript · 信源 [1085]",
    ),
    dict(
        nid="rpm23c2", name="awesome-dsh-plugin（DSH 插件精选）",
        url="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin",
        lang="Python", stars="16,705",
        tags=[("t-make", "AI × 目录"), ("t-ok", "已登记未安装")],
        plain="**DSH 生态的目录**：一份按用途分类的插件精选列表。对一个「万物皆插件」的外壳来说，"
              "**目录本身就是基础设施** —— 第十六辑的教训是「一周能长出二十个 `godot-mcp` 空壳」，"
              "那么「哪几个值得装」这件事必须有地方回答。",
        analogy="我们有自己的 `index.html`（1094 项）在做同一件事，只是**对象不同**："
                "我们索引的是「开源项目」，它索引的是「同一个外壳里的插件」。",
        ext=(75, "7.5/10", "**分类法可以抄**：它怎么把插件分组（上下文 / 工具 / UI / 路由 / 安全），"
                            "可以直接挪来给 `index.html` 的 AI 那一区做二级分类"),
        use=(60, "6.0/10", "16,705★ 但 **CC0-1.0 = 只收列表不背书**；"
                            "按 M-0002，条目进榜 ≠ 可用，仍要逐条回仓库核实"),
        src="创建 2026-08-13 · 最近推送 2026-09-23 · 16,705★ · CC0-1.0 · Python · 信源 [1086]",
    ),
    dict(
        nid="rpm23c3", name="dsh-context-window（用「换窗」代替「摘要压缩」）",
        url="https://github.com/CooperZhuang/dsh-context-window",
        lang="TypeScript", stars="0",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已登记未安装")],
        plain="**本辑最反直觉的一个设计**：上下文满了不要「摘要压缩」，而要**交接式换窗** —— "
              "给模型一个**可自己调用的 `new_context`**，让它把「下一步要干什么」写成交接说明，"
              "然后**开一个新窗口**接着干。附 token 预算提示。作者说是复刻 Codex 最新的做法。",
        analogy="本辑读到的四篇上下文管理文章（掘金 / CSDN / 菜鸟 / PEC）**全都把方向指向同一个点**："
                "摘要会**改写事实**（那份测试日志被摘要成「之前导出测试失败了」，"
                "`order-export.test.ts` / `5000ms` / `orderExport.ts:42:19` 全丢了）。"
                "「换窗 + 交接」是**保真**的，摘要不是。",
        ext=(85, "8.5/10", "**方向上最值钱的一张**：可直接对照我们工作区的"
                            "「一个章节一个入口 label + 快照基线」（第 9 轮那条"
                            "「跨『开始新游戏』边界 store 必被重置」的教训，本质就是一次换窗）"),
        use=(30, "3.0/10", "**0★ / 09-09 创建 / 单人**，代码还没被任何人用过；"
                            "而且它绑 DSH 的插件接口（rc 阶段，接口随时变）→ **先抄概念，后装代码**"),
        warn="同类还有四个（`PlxloYzb/dsh-context-management` 窗口化+可逆 / `yindf/taskfold` "
             "把工作折进具名任务 / `kolawong/fast-compaction-dsh` 判定式压缩 / "
             "`dvaJi/dsh-codex-context`）—— **全都 ≤7★**。这一片是「方向已对、实现未稳」，"
             "**别当成熟工具用**。",
        src="创建 2026-09-09 · 最近推送 2026-09-09 · 0★ · MIT · TypeScript · 信源 [1087]",
    ),
    dict(
        nid="rpm23c4", name="harness-token-efficiency（把 harness 差异做成可复现实验）",
        url="https://github.com/nmlemus/harness-token-efficiency",
        lang="Python", stars="0",
        tags=[("t-make", "AI × 评测"), ("t-ok", "已登记未安装")],
        plain="**一个预注册（PREREGISTRATION.md）的 harness 消融实验**：模型**锁死同一个**"
              "（`claude-sonnet-5`），只换外壳（Claude Code vs Pi），4 个数据科学任务 × 3 次重复，"
              "24/24 全过。第一次 pilot 报出的倍率是 **7.0x~13.7x**；作者随后**自己推翻**了这个数 —— "
              "因为 `run_trial.py` 调的是**没隔离的 `claude` 二进制**，本机 `~/.claude/` 里的"
              "110 个工具 / 10 个插件 / 7 个 MCP / 68 个自定义 agent / 全局 `CLAUDE.md` "
              "**全都漏进了每一次 trial 的上下文**，把 Claude Code 的 token 抬高了 **39~52%**。"
              "修法：`isolated_claude_environment()`。**改正后倍率是 4.2x~8.3x。**",
        analogy="第十六辑引的 HarnessTax（UC Berkeley + Arena）说「同模型换外壳，成本差约 2 倍」。"
                "这个仓库把同一件事**做成了能跑的实验，并且顺手证伪了自己的第一版结果** —— "
                "**「测出来的差值里，有多少是你的个人配置，有多少才是外壳」**。",
        ext=(85, "8.5/10", "**方法论直接可用**：任何「A 工具 vs B 工具」的对比，"
                            "先加一步「隔离个人配置」；否则量的是**自己的机器**，不是工具。"
                            "作者还留了可复用的口径：**同一单元格内 Pi 的 CV≈0.2%、"
                            "Claude Code 的 CV≈15~27%** → 比 Claude Code 需要更多重复次数"),
        use=(35, "3.5/10", "**0★**，作者自述这是 pilot；要跑真实验需要 API key + 时间。"
                            "**但它给的判据当天就能落地**（房规 #35）"),
        warn="作者自己在 README 里把「污染的那一版」留在 `runs-pilot1-contaminated/` 并**标注清楚了**，"
             "而不是删掉 —— 这比任何漂亮的结论都更值得抄（**失败的样本要留档**）。",
        src="创建 2026-09-06 · 最近推送 2026-09-08 · 0★ · MIT · Python · 信源 [1088]",
    ),
    dict(
        nid="rpm23c5", name="i-have-adhd（把答案放到第一行）",
        url="https://github.com/ayghri/i-have-adhd",
        lang="Python", stars="50,519",
        tags=[("t-make", "AI × 输出"), ("t-ok", "已登记未采纳完")],
        plain="**50,519★，一天涨 4,650★。** 它是一条**输出形态**规则（不是工具）："
              "假装读者有 ADHD —— ① **第一行就是可执行动作**（不是背景、不是计划）；"
              "② 多步工作要编号，每步一个动作；③ 结尾给**一个两分钟内能做完的下一步**；"
              "④ 抑制岔题（第二个问题留到最后单独问）；⑤ **每一轮都重述状态**"
              "（「5 步里的第 3 步完成了」）；⑥ 时间要给**具体单位**；⑦ **把完成的活显式写出来**；"
              "⑧ 报错用**陈述语气**（不用「啊哦」「好像有点问题」）。",
        analogy="这几乎是**你本人偏好的书面版**：你反复要的是「简洁直接」"
                "「plain-language 总结优先于技术 jargon」「不要反复确认」。"
                "差别在于它把「简洁」拆成了**八条可检查的动作**，而不是一句形容词。",
        ext=(80, "8.0/10", "**八条里最该抄的是 ⑤ 和 ③**："
                            "「重述状态」解决的是「跨轮次丢失进度」，"
                            "「一个具体下一步」解决的是「知道了但没动手」"),
        use=(70, "7.0/10", "**注意口径**：它是给「读输出的人」用的，不是给「写代码的 agent」用的。"
                            "我们的产出常常是**报告和索引**（要能当资料查），"
                            "**不能无条件套 8 条** —— 会牺牲可检索性"),
        warn="`disable-model-invocation: true` —— 它是**手动开关**（`/i-have-adhd`），"
             "不会自己生效。同类还有 `charlie947/answer-first`（19★，拆成 10 条通用规则）。",
        src="创建 2026-05-13 · 最近推送 2026-09-19 · 50,519★ · MIT · Python · 信源 [1089]",
    ),
    dict(
        nid="rpm23c6", name="godot-ai（生产级 Godot MCP）",
        url="https://github.com/hi-godot/godot-ai",
        lang="GDScript", stars="2,563",
        tags=[("t-make", "游戏 × 引擎"), ("t-ok", "已登记未安装")],
        plain="**本批 Godot MCP 里唯一「生产级」提法的那个**：一个 Snap 就能装的 MCP 服务 + AI 工具集，"
              "让 AI 助手**直接驱动 Godot 编辑器** —— 建节点、写脚本、跑场景。",
        analogy="第六辑收过 `tomyud1`（32 工具）与 **Godot MCP Omni**（1820 操作 / 59 域），"
                "第十六辑又看到**一周冒出约 20 个 `godot-mcp` 空壳**。这一条是那片洪水里"
                "**星数最高、且还在推**的那个 —— 洪水里要挑「有人真的在用」的。",
        ext=(80, "8.0/10", "配套值得一起看的是 `Erodenn/godot-mcp-runtime`（77★，"
                            "**零足迹** TypeScript MCP）与 `NPGameDev/godot-mcp-toolkit`（44★，编辑器内插件）"),
        use=(45, "4.5/10", "**本作是 Ren'Py，不是 Godot**；且游戏线 2026-09-23 已终止 → "
                            "**当「引擎侧 AI 接入的当前最佳形态」收着**，等重启或换引擎再用"),
        src="创建 2026-04-12 · 最近推送 2026-09-23 · 2,563★ · MIT · GDScript · 信源 [1090]",
    ),
    dict(
        nid="rpm23c7", name="beckett-godot-mcp（编辑器内，能「看见」结果的 MCP）",
        url="https://github.com/beckettlab/beckett-godot-mcp",
        lang="GDScript", stars="23",
        tags=[("t-make", "游戏 × 验证"), ("t-ok", "已登记未安装")],
        plain="一句话卖点里藏着本辑最该抄的四个动词：**inspect / author / run / SEE** —— "
              "**零 sidecar**（不需要外挂进程，MCP 服务活在 Godot 编辑器**里面**），"
              "让 Claude Code、Cursor 这类 agent 检查、编写、运行，并且**看到**结果。",
        analogy="第十四辑的主线是**「可达性」**，第十一辑的教训是"
                "「**试玩只对会读结果的模型有用**」（GPT-5.6 Terra 跑了 6 次试玩、一次结果都没读）。"
                "它把「**SEE**」直接写进了工具的能力列表 —— **能力清单里有没有「看」，是个分水岭**。",
        ext=(85, "8.5/10", "「**零 sidecar + 能力列表里含 SEE**」这两条可以当**引擎接入的选型判据**："
                            "凡是只给「写」不给「读 / 看 / 跑」的 MCP，都还是半成品"),
        use=(30, "3.0/10", "23★ / 06-19 创建；与本作引擎不同。**当判据收，不当工具装**"),
        src="创建 2026-06-19 · 最近推送 2026-09-19 · 23★ · MIT · GDScript · 信源 [1091]",
    ),
    dict(
        nid="rpm23c8", name="rpycdec（Ren'Py .rpyc / .rpymc 反编译）",
        url="https://github.com/cnfatal/rpycdec",
        lang="Python", stars="58",
        tags=[("t-make", "游戏 × 逆向"), ("t-ok", "已登记未安装")],
        plain="**专门反编译 Ren'Py 编译产物**（`.rpyc` / `.rpymc`）的工具 —— "
              "也就是把发布版游戏里的脚本还原回可读源码。",
        analogy="**你的强项正在这里**（73 款游戏解包、跨引擎对比）。而这一条对我们有额外一层意义："
                "本作自己就是 Ren'Py 项目 —— 上一轮我们把 `game/` 交付成发行包时，"
                "**自己的 `.rpyc` 也在里面**。**同一个工具既是研究工具，也是「我的发行包能被反编译到什么程度」的体检工具**。",
        ext=(80, "8.0/10", "可以加一条**自查**：拿它对着自己的 `amphoreus-roast` 发行包跑一次，"
                            "看**哪些东西是藏不住的**（这比读文档有用）"),
        use=(80, "8.0/10", "**58★、MIT、Python、2026-09-20 还在推** "
                            "→ 是这项里少见的**活跃**项目。**列进下一轮待办**"),
        warn="同类但方向相反的两个（都用 **AI 做翻译而不是逆向**）："
             "`DezFix/OctopusBridge`（3★，GPL-3.0，Windows，Twine/Ren'Py/RPG Maker/Tyrano "
             "**AI 辅助翻译 + 改 Mod**）与 `dihuangdebitebi/Renpy_RT_Tool`（0★，"
             "「选中 exe 就能边玩边翻」）。**都还很新，别指望稳。**",
        src="创建 2023-08-20 · 最近推送 2026-09-20 · 58★ · MIT · Python · 信源 [1092]",
    ),
    dict(
        nid="rpm23c9", name="game-design-review（四把尺子 + 阶段校准 + 红队）",
        url="https://github.com/liuyejinghong/game-design-review",
        lang="Python", stars="0",
        tags=[("t-make", "游戏 × 评审"), ("t-ok", "已登记未安装")],
        plain="**游戏策划视角的「试玩评审」agent skill**：给开发者一套**四把尺子**打分，"
              "按**阶段校准**（文字期 → 像素期，标准不同），并带一个**红队模式**"
              "（专门攻击你的设计，而不是夸它）。",
        analogy="我们的验收一直是**机械闸门**（lint / test / 五道 `check_*.py`）。"
                "房规 #31 已经写明：**闸门保证的是「没坏」，不是「好」** —— "
                "「这个能看了」这句判断一直没有人（或工具）来给。**它试图给这一句定标准。**",
        ext=(80, "8.0/10", "「**阶段校准**」这条最值得抄：同一个作品在「文字期」和「成品期」"
                            "**该被用不同的尺子量** —— 我们的闸门现在是**一套尺子从头用到尾**"),
        use=(25, "2.5/10", "**0★ / 创建与推送同日（09-19）/ 无 license** → "
                            "按 M-0002 **只登记，不采用**；它的价值在「有人在做这件事了」这个信号"),
        warn="同类三个都是 09-17~09-20 新建的 0★：`rakaascode/game-design-council`（正/反/主持三角辩）、"
             "`RomainYing/Game-design-theory`（玩家欲望 → 满足手法 → 系统）、"
             "`GabrielBigardi/gamedev-ai-skills`。**它们合起来说明一件事："
             "「评审」是 AI 游戏工具链里最后一块还没定型的环节。**",
        src="创建 2026-09-19 · 最近推送 2026-09-20 · 0★ · 无 license · Python · 信源 [1093]",
    ),
]

FOOTNOTES = [
    ("1085", "https://github.com/deepseek-ai/deepseek-harness",
     "deepseek-ai/deepseek-harness", "233,987 · 2026-09-22 · MIT · TypeScript"),
    ("1086", "https://github.com/awesome-dsh-plugin/awesome-dsh-plugin",
     "awesome-dsh-plugin/awesome-dsh-plugin", "16,705 · 2026-09-23 · CC0-1.0 · Python"),
    ("1087", "https://github.com/CooperZhuang/dsh-context-window",
     "CooperZhuang/dsh-context-window", "0 · 2026-09-09 · MIT · TypeScript"),
    ("1088", "https://github.com/nmlemus/harness-token-efficiency",
     "nmlemus/harness-token-efficiency", "0 · 2026-09-08 · MIT · Python"),
    ("1089", "https://github.com/ayghri/i-have-adhd",
     "ayghri/i-have-adhd", "50,519 · 2026-09-19 · MIT · Python"),
    ("1090", "https://github.com/hi-godot/godot-ai",
     "hi-godot/godot-ai", "2,563 · 2026-09-23 · MIT · GDScript"),
    ("1091", "https://github.com/beckettlab/beckett-godot-mcp",
     "beckettlab/beckett-godot-mcp", "23 · 2026-09-19 · MIT · GDScript"),
    ("1092", "https://github.com/cnfatal/rpycdec",
     "cnfatal/rpycdec", "58 · 2026-09-20 · MIT · Python"),
    ("1093", "https://github.com/liuyejinghong/game-design-review",
     "liuyejinghong/game-design-review", "0 · 2026-09-20 · 无 license · Python"),
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

    desc = ('第十七辑的 GitHub 那一路跑了 <strong>25 个查询 / 274 行候选</strong>，'
            '逐条走 REST API 实测 stars / forks / license / language / pushed / created，'
            '<strong>再逐条 grep 过 16 份存档 + 1085 项索引</strong>。'
            '剔掉的：8 条已收录（grokbot-field-notes / JakeSelby-agent-harness / '
            'fennara-godot-ai / hybridindie-godot-mcp / tallslab-threeforge / '
            'ruc-datalab-EvoOntology / CoplayDev-unity-mcp / lovetimo0421-yumina-oss）'
            '与一批 0★ 空壳。<strong>本版主线是「上下文」—— 一个外壳怎么决定你花多少钱、'
            '能记多久、以及你能不能验证自己测出来的数。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm23g">',
             '      <div class="group-title" data-page-node-id="rpm23gt">🆕 第二十三版增补 · 上下文是预算，不是仓库（9 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm23gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm23r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm23ra%s">%s</a> — %s</div>'
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
