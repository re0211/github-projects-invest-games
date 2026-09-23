# -*- coding: utf-8 -*-
"""第二十五版增补：把第十九辑 GitHub 那一路新发现的 8 个条目登记进 index.html。

本辑 GitHub 调研：15 个查询 → 153 行候选 → 32 个仓库逐条 `gh api repos/<r>` 实测
（stars / forks / license / language / pushed_at / created_at 全部走 REST API，无一估算）
→ 逐条 grep 过 18 份存档 + 1104 项索引，剔掉已收录的
（hi-godot/godot-ai · beckettlab/beckett-godot-mcp · Donchitos/Claude-Code-Game-Studios = CCGS）
与一批 0★ 空壳，剩下 8 条"与本工作区直接对话"的。

数据来源：2026-09-23 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v25_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1103"'
FIRST_NEW_FOOTNOTE = 1104
MARKER = "第二十五版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第二十四版增补 2026-09-23',
    '共 1104 个项目',
    '第二十三版增补 9 项 + 第二十四版增补 10 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第二十五版增补 2026-09-23',
    '共 1112 个项目',
    '第二十三版增补 9 项 + 第二十四版增补 10 项 + 第二十五版增补 8 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm25c1", name="context-mode（在 MCP 层把工具输出挡在上下文之外）",
        url="https://github.com/mksglu/context-mode",
        lang="TypeScript", stars="23,982",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="**本辑最该读的一个，不是因为它省了 98%，而是因为它后来删掉了自己最出名的功能。** "
              "它是一个装在 **MCP 协议层**的拦截层：工具（Bash / Read / curl）的原始输出"
              "**先进沙箱**，超过 `LARGE_OUTPUT_THRESHOLD = 100KB` 的**不截断**"
              "—— 写进 SQLite **FTS5** 全文索引，只给模型回一个**指针**，要用再 `ctx_search` 取片段。"
              "覆盖 **17 个平台**（Claude Code / Codex / Cursor / Copilot CLI / agy / Qwen Code …），"
              "npm 安装量 **331,200+**。",
        analogy="房规 #34 是「上下文是预算，JIT 加载」。这个项目把那句话"
                "**做成了协议层的一块板子** —— 不是劝模型少读，是**让大数据根本进不来**。"
                "与我们的差别：我们靠 `mistakes/` + 分层记忆（靠自觉），它靠 hook（靠强制）。",
        ext=(92, "9.2/10", "**三个可直接抄的机制**：① 阈值外部化 + 指针（不是截断 —— "
                           "截断会丢尾巴，指针不会）② `PreToolUse` 强制路由（不让裸工具把输出倒进上下文）"
                           "③ dispatcher **fail-open**（hook 缺失时 exit 0，因为 Copilot 会把 exit-1 "
                           "当成 Deny，直接把整个 agent 砖化）"),
        use=(80, "8.0/10", "**⚠️ 先读它的 #482 再决定怎么抄**：早期版本会到处注入"
                           "「Terse like caveman（像穴居人一样简洁）」，"
                           "**Moonshot AI 在 kimi-k2.5 上的报告显示：激进的简洁提示会损害编码/推理基准** "
                           "→ 作者**全量移除了 22 处注入点**，改成「不干预最终答案文风」"),
        warn="**这是本辑最重要的一条分辨**：**「压缩工具输出」和「压缩模型说话方式」是两件事，"
             "前者纯赚，后者有代价。** 房规 #36（i-have-adhd 八条）针对的是"
             "**给人读的产出**，不是给模型的系统提示 —— 别把两者混着用（已写成房规 #40）。"
             "另：license 是 NOASSERTION（非标准），商用前要确认。",
        src="创建 2026-02-23 · 最近推送 2026-09-23 · 23,982★ / 1,729 forks · NOASSERTION · TypeScript · 信源 [1104]",
    ),
    dict(
        nid="rpm25c2", name="open-code-review（把「不能错的步骤」从模型手里拿走）",
        url="https://github.com/alibaba/open-code-review",
        lang="Go", stars="40,091",
        tags=[("t-make", "AI × 评审"), ("t-ok", "已登记未安装")],
        plain="**阿里内部跑了两年、几万开发者代码之后开源出来的 AI code review CLI。** "
              "核心不是「换个更强的模型」，而是**混合架构**："
              "**选文件、打包文件、规则匹配这些「错不起」的步骤交给确定性工程逻辑**，"
              "**只有需要动态判断的那一小段交给 agent**。官方对比通用 agent（含 Claude Code）："
              "**同底座模型下，precision 与 F1 显著更高，token 消耗约 1/9。**",
        analogy="我们的六道 `check_*.py` 闸门（dialogue / font / audio / sprites / balance / release）"
                "**走的就是这条路** —— 判据写成代码，不交给模型。这个项目给了一个更大的样本："
                "**生产规模下，专用管线比「通用 agent + 一条 skill」更稳、更可预测。**",
        ext=(88, "8.8/10", "**「错不起的步骤应该确定性化」这条判据可以直接照抄**："
                           "下次给任何流程加 AI 环节之前，先问「哪几步错了就是事故」—— 那几步不许交给模型"),
        use=(70, "7.0/10", "`npm install -g @alibaba-group/open-code-review` 一行可装、配模型端点即可跑；"
                           "**但它是 review 向**，我们当前的瓶颈在「生成侧」→ **先记判据，暂不落地**"),
        src="创建 2026-05-18 · 最近推送 2026-09-23 · 40,091★ / 2,880 forks · Apache-2.0 · Go · 信源 [1105]",
    ),
    dict(
        nid="rpm25c3", name="agent-skills（生产级 agent 工程技能库）",
        url="https://github.com/addyosmani/agent-skills",
        lang="JavaScript", stars="98,643",
        tags=[("t-make", "AI × 技能"), ("t-ok", "已登记未安装")],
        plain="**本批星数最高的一个（98,643★ / 10,365 forks）**："
              "面向 AI 编码 agent 的**生产级工程技能库** —— 代码审查、调试、优化这类"
              "「每次都要重新讲一遍」的能力，打包成可复用的 skill。",
        analogy="**它就是「技能」这个形态的规模化证明**：第十七辑我们刚给技能加了预算闸门"
                "（`_tools/skill_budget.py`，判据 ≤500 行 / ≤5000 token / description ≤1024 字符），"
                "说明我们已经承认**技能是常驻上下文的固定开销** —— "
                "而 9.8 万星说明**大家都把能力往这一层塞**。",
        ext=(82, "8.2/10", "**可当作我们技能库的对照样本**：看别人把一个 skill 切多大、"
                           "description 怎么写、什么时候该外置到 `references/`"),
        use=(55, "5.5/10", "**通用工程向**（审查/调试/优化），与本工作区主力（游戏 + 调研索引）"
                           "交集不大；且星数高不等于适合我们 —— **按房规 #35，真要对比得先隔离个人配置再量**"),
        src="创建 2026-02-15 · 最近推送 2026-09-23 · 98,643★ / 10,365 forks · MIT · JavaScript · 信源 [1106]",
    ),
    dict(
        nid="rpm25c4", name="security-audit-skill（发现问题的人不许验证自己）",
        url="https://github.com/cloudflare/security-audit-skill",
        lang="JavaScript", stars="20,680",
        tags=[("t-make", "AI × 验证"), ("t-ok", "已登记未安装")],
        plain="**Cloudflare 把自己内部挖漏洞的六阶段流程打包成 agent skill**："
              "侦察 → 覆盖率主导的狩猎 → 候选验证 → 结构化输出 → **独立验证** → 报告。"
              "两条硬规矩：① **发现问题那个 agent 永不负责验证它**（对抗式验证）；"
              "② 「纵深防御的缺口本身不算漏洞」这类**判断标准被写死在流程里**，不留给模型自由裁量。"
              "团队自测：**跑一次只能找到反复跑能找到的约一半** —— 所以流程是为「多轮累积」设计的。",
        analogy="**「一次只能找到一半」这个数字，是整个验证侧最诚实的自述。** "
                "我们的 `mistakes/` 和六道闸门也一样 —— 房规 #31 就写过"
                "「闸门保证的是没坏，不是好」。差别在于：我们**从来没量过自己的召回率。**",
        ext=(86, "8.6/10", "**两条可直接落地的规矩**：① 生成者 ≠ 验证者 "
                           "② 判断标准写进**流程**，不写进**提示词**（写进提示词 = 每次可能被重新解释）"),
        use=(60, "6.0/10", "`npx skills add` 一行装；**但它是安全审计向**，"
                           "我们当前没有可审计的目标仓库 → **抄两条规矩，不装工具**"),
        src="创建 2026-06-18 · 最近推送 2026-09-14 · 20,680★ / 1,173 forks · MIT · JavaScript · 信源 [1107]",
    ),
    dict(
        nid="rpm25c5", name="worktrunk（并行 agent 的 git worktree 管家）",
        url="https://github.com/max-sixty/worktrunk",
        lang="Rust", stars="8,365",
        tags=[("t-make", "AI × 协作"), ("t-ok", "已登记未安装")],
        plain="**一个 Rust 写的 git worktree 管理 CLI，专门给「多个 agent 同时干一个仓库」用。** "
              "每个 agent 一条独立工作树，互不覆盖；创建 / 切换 / 清理都是一条命令。",
        analogy="第十六辑记下一条反直觉结论：**多 agent 并行的收益已经转负** —— "
                "Codex 工程师公开警告 >2 个并行只增「协调税」，有人用 1,393 个 agent 重构单文件"
                "**烧掉 $20,000**。我们因此选了单 agent 串行。"
                "worktrunk 提醒的是另一半：**协调税 = 沟通成本 + 冲突成本，后半是可以工程化的。**",
        ext=(78, "7.8/10", "**把「协调税」拆开看**：沟通成本（agent 之间要说清各自干了什么）"
                           "**vs 冲突成本（改到同一个文件）** —— 后者能用工具消掉，前者不能"),
        use=(50, "5.0/10", "**我们当前不需要**（单 agent 串行已跑通）；"
                           "**等哪天真的要并行时，这是第一个该装的** —— 优先级高于再多一个 agent"),
        warn="同类一批都是 5~114★ 的新项目（`axonel/axonel` 独立验证 + 人工介入 / `TennnisAI/Agency` 桌面端 / "
             "`r2luna/floe` 键盘流 / `Mrjwj34/berth` 无守护进程）—— **全是 2026-09 新建，未定型**。",
        src="创建 2025-10-17 · 最近推送 2026-09-23 · 8,365★ / 294 forks · NOASSERTION · Rust · 信源 [1108]",
    ),
    dict(
        nid="rpm25c6", name="agent-memory（记忆是 Markdown 文件，不是向量库）",
        url="https://github.com/tigerless-labs/agent-memory",
        lang="Python", stars="966",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已登记未安装")],
        plain="**一个长期记忆运行时，卖点是一句话：plain Markdown as the source of truth。** "
              "本地排序检索（不要 API key），**一个 store 同时给 Claude Code 和 Codex 用** —— "
              "也就是说换外壳不换记忆。2026-09-01 创建，三周 966★。",
        analogy="**这正是我们已经在做的事，只是做在文件系统层**："
                "`.workbuddy/memory/`（日志）+ `mistakes/`（错误记忆）+ `agent-house-rules.md`（房规）。"
                "房规 #34 的结论也是这句：**记忆是文件，不是上下文**（Grok Build 的"
                "「每轮结束后在后台复习对话、写成 markdown 笔记」是同一个答案）。",
        ext=(84, "8.4/10", "**「记忆能被 diff、能被 commit、能被 grep」是一个真判据**："
                           "向量库里的记忆**查得到但看不懂**，Markdown 里的记忆**既能查也能审**"),
        use=(65, "6.5/10", "**已有等价物**（`mistakes/` + `.workbuddy/memory/`），**不替换**；"
                           "可取的是「**一个 store 跨外壳共享**」—— 我们换桥 / 换 shell 时记忆不跟着换"),
        warn="同一批里还有 `tinyhumansai/openhuman`（40,058★ / **GPL-3.0** / Rust 桌面应用）"
             "与 `IotA-asce/oldhand`（git 追踪的「机构记忆」）。"
             "**openhuman 是 GPL-3.0，比 MIT/Apache 严得多，商用前必须确认合规。**",
        src="创建 2026-09-01 · 最近推送 2026-09-23 · 966★ / 64 forks · MIT · Python · 信源 [1109]",
    ),
    dict(
        nid="rpm25c7", name="claudecut（把系统提示词砍到 36 个 token）",
        url="https://github.com/alexgetmancom/claudecut",
        lang="Shell", stars="37",
        tags=[("t-make", "AI × 评测"), ("t-ok", "已登记未安装")],
        plain="**一个极端的对照实验：把 Claude Code 身上几乎所有东西都砍掉** —— "
              "只留**一个 shell 工具**、**36 个 token 的系统提示词**、**封顶的上下文窗口**，"
              "看模型还剩多少能力。2026-09-20 创建。",
        analogy="**它和第十七辑的 `harness-token-efficiency` 是同一个问题的两端**："
                "那边是「把个人配置**加回去**，token 涨了 39~52%」；这边是「把固定块**全拿掉**，看地板在哪」。"
                "**我们用 `_tools/harness_tax_probe.py` 量出自己的调用侧固定前缀 = 20,900 token"
                "（技能 13% / MCP 50% / 记忆 37%，占 200k 窗口 10.45%）** —— "
                "我们落在两端之间的某个位置，而且第一次有数了。",
        ext=(80, "8.0/10", "**「地板在哪」是选型必需的信息**：不知道下限，"
                           "就没法判断现在这套外壳的开销是「必要」还是「惯性」"),
        use=(40, "4.0/10", "**37★ / 创建三天 / 单人** → 按 M-0002 **只登记不采用**；"
                           "且本工作区跑不了 `claude` CLI（沙箱限制），**实测这条路是封的**"),
        warn="它的价值是**作为一个可引用的对照点**，不是一个要装的工具。"
             "同类：`AngelCantugr/context-inspector`（0★ / 09-22，按条按类看上下文被什么吃掉了）。",
        src="创建 2026-09-20 · 最近推送 2026-09-20 · 37★ / 1 fork · MIT · Shell · 信源 [1110]",
    ),
    dict(
        nid="rpm25c8", name="funplay-unity-mcp（91 个工具，且能「看见」运行中的游戏）",
        url="https://github.com/FunplayAI/funplay-unity-mcp",
        lang="C#", stars="251",
        tags=[("t-make", "游戏 × 引擎"), ("t-ok", "已登记未安装")],
        plain="**Unity 编辑器 MCP 服务器：20 个模块 / 91 个内置工具。** "
              "除了常规的建场景、写脚本，三个能力是分水岭："
              "① `execute_code` —— **在内存里现编现跑 C#**；"
              "② **播放模式自动化**：进 Play Mode、**模拟输入**、**截图**；"
              "③ **结构化返回 + instanceId 链式调用**（一次调用的结果能喂给下一次）。",
        analogy="**第十四辑的可达性主线在这里落地成了工具能力**："
                "「AI 做完之后有没有人真的跑一遍」—— "
                "只有**能进 Play Mode、能模拟输入、能截图**的 MCP 才谈得上「验证」。"
                "对照第十一辑那条：**Ziva 的整局试玩里，GPT-5.6 Terra 跑了 6 次一次结果都没读**。",
        ext=(80, "8.0/10", "**选型判据（可复用到任何引擎 MCP）**："
                           "看它的工具清单里有没有 **run / input / screenshot** 三个动词。"
                           "**只有 create 和 edit 的，都是半成品** —— 与第十七辑 "
                           "`beckett-godot-mcp` 的「inspect / author / run / **SEE**」是同一条判据"),
        use=(35, "3.5/10", "**本作是 Ren'Py；且游戏线 2026-09-23 已终止** → "
                           "**当「引擎侧 AI 接入的当前上限形态」收着**，不装"),
        warn="同批 **`IvanMurzak/Godot-MCP`（251★ / Apache-2.0 / C#，42 工具 / 12 家族）** "
             "更值得看一眼的点是：**它与同作者的 Unity-MCP 共用 `ReflectorNet` 反射底层**（NuGet 包），"
             "不是各写一套 → **「项目之间有没有共享底层」比「工具数量」更能判断是不是认真的。**",
        src="创建 2026-03-12 · 最近推送 2026-09-17 · 251★ / 19 forks · MIT · C# · 信源 [1111]",
    ),
]

FOOTNOTES = [
    ("1104", "https://github.com/mksglu/context-mode",
     "mksglu/context-mode", "23,982 · 2026-09-23 · NOASSERTION · TypeScript"),
    ("1105", "https://github.com/alibaba/open-code-review",
     "alibaba/open-code-review", "40,091 · 2026-09-23 · Apache-2.0 · Go"),
    ("1106", "https://github.com/addyosmani/agent-skills",
     "addyosmani/agent-skills", "98,643 · 2026-09-23 · MIT · JavaScript"),
    ("1107", "https://github.com/cloudflare/security-audit-skill",
     "cloudflare/security-audit-skill", "20,680 · 2026-09-14 · MIT · JavaScript"),
    ("1108", "https://github.com/max-sixty/worktrunk",
     "max-sixty/worktrunk", "8,365 · 2026-09-23 · NOASSERTION · Rust"),
    ("1109", "https://github.com/tigerless-labs/agent-memory",
     "tigerless-labs/agent-memory", "966 · 2026-09-23 · MIT · Python"),
    ("1110", "https://github.com/alexgetmancom/claudecut",
     "alexgetmancom/claudecut", "37 · 2026-09-20 · MIT · Shell"),
    ("1111", "https://github.com/FunplayAI/funplay-unity-mcp",
     "FunplayAI/funplay-unity-mcp", "251 · 2026-09-17 · MIT · C#"),
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

    desc = ('第十九辑的 GitHub 那一路跑了 <strong>15 个查询 / 153 行候选</strong>，'
            '32 个仓库逐条走 REST API 实测 stars / forks / license / language / pushed / created，'
            '<strong>再逐条 grep 过 18 份存档 + 1104 项索引</strong>。'
            '剔掉的已收录项：<code>hi-godot/godot-ai</code> · '
            '<code>beckettlab/beckett-godot-mcp</code> · '
            '<code>Donchitos/Claude-Code-Game-Studios</code>（= 本工作区在用的 CCGS）。'
            '<strong>本版主线是「省下来的 vs 赔进去的」—— '
            '压缩工具输出是纯赚，压缩模型的说话方式和行为分布要赔。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm25g">',
             '      <div class="group-title" data-page-node-id="rpm25gt">🆕 第二十五版增补 · 口径（8 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm25gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm25r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm25ra%s">%s</a> — %s</div>'
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
