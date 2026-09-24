# -*- coding: utf-8 -*-
"""第二十七版增补：把第二十一辑 GitHub 那一路新发现的 8 个条目登记进 index.html。

本辑 GitHub 调研：逐仓库 `gh api repos/<r>` 实测（stars / forks / license / language /
pushed_at / created_at 全部走 REST API，无一估算）→ 逐条 grep 过 18 份存档 + 1120 项索引。
剔掉的已收录项：`banjtheman/renpy_mcp_server` · `Muanchen2/renpy-mcp` ·
`EleutherAI/lm-evaluation-harness` · `IvanMurzak/Godot-MCP` / `Unity-MCP` / `Unreal-MCP`。

本辑主线：**「判据外移 + 先核实再落笔」** —— 记忆在写入前加只读探针、压缩先无损剪枝、
确定性检查要能合并且不调模型。

⚠️ 本脚本的四道保护已由 `_tools/insert_guard_probe.py` 用**真实历史版本**做过 6 例正负验证
（1 正例 + 5 反例），不再是"从未被反例验证过"的状态。

数据来源：2026-09-24 用 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v27_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1119"'
FIRST_NEW_FOOTNOTE = 1120
MARKER = "第二十七版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第二十六版增补 2026-09-24',
    '共 1120 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第二十七版增补 2026-09-24',
    '共 1128 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm27c1", name="agent-systems-handbook（生产级 Agent 系统的对照读本）",
        url="https://github.com/Prompthon-IO/agent-systems-handbook",
        lang="MDX", stars="316",
        tags=[("t-make", "AI × 约定"), ("t-ok", "已登记未安装")],
        plain="**本批星数第二高（316★ / MDX / 未声明协议）。** 覆盖生产级 Agent 系统的完整面向："
              "工作流、工具、**记忆系统**、**上下文工程**、MCP/A2A 互操作、评测、可观测性、多智能体架构，"
              "配套站点 `labs.prompthon.io`。topics 里明确带 `context-engineering` / `agent-memory`。",
        analogy="我们把注意力都花在「怎么让它干活」上，**「怎么知道它干得对不对」几乎是空白** —— "
                "我们的闸门测的是「产物格式对不对」，没有任何一条测「这一轮任务完成率是多少」。"
                "这份手册的作用是当**对照表**：拿它逐项问「我们缺哪一环」。",
        ext=(76, "7.6/10", "**最好用的方式不是读，是当 checklist 用**："
                           "把它的七个面向当成七行，逐行填「我们有 / 没有 / 有但不测」。"
                           "本辑自测已经用了一次 —— 结论是**我们缺「评测」与「可观测」两环**"),
        use=(55, "5.5/10", "纯文档、零运行成本、无 key；⚠️ 但 **license=NOASSERTION**（非标准/未明确）"
                           "→ **正文可读、结论可引用，文字与图不要直接搬进项目**"),
        src="最近推送 2026-09-24 · 316★ · 未声明协议 · MDX · 信源 [1120]",
    ),
    dict(
        nid="rpm27c2", name="vscode-ollama（本地 Ollama 直连 VS Code 的自主编码 agent）",
        url="https://github.com/warm3snow/vscode-ollama",
        lang="TypeScript", stars="67",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已核实待试")],
        plain="**本批与我们的画像最重合的一个（67★ / MIT / TypeScript，已上架 VS Marketplace）。** "
              "本地模型聊天 + 可视化思维过程 + 保留历史，并带一个自主编码 agent："
              "`read / write / edit / grep / find / ls / bash` 读写工作区、危险操作先确认，"
              "另有 `codebase-search / plan / implement / review` 内置子智能体，可串行或并行分派。",
        analogy="我们此前评估过的外壳要么是云端优先，要么要另装 CLI。这个是**不需要任何云端 key 的本地路线**，"
                "而且**上架了官方市场**（装起来就是一次点击，不是从源码构建）—— "
                "对「不想再折腾一套构建链」是决定性的差别。",
        ext=(84, "8.4/10", "**`bash` + `grep` + 写入三件套正是我们 `check_*.py` 工作流需要的**；"
                           "内置的 `plan` 子智能体可以拿来做「先出计划再改文件」那一步"),
        use=(78, "7.8/10", "MIT 可读改、Marketplace 直装、明确本地 Ollama。"
                           "⚠️ **两条硬提醒**：①并行子智能体会**同时压 16GB 内存**，"
                           "按房规「>2 并行只增协调税」**只开 plan + implement 两个**；"
                           "②按 M-0002，**先在 `/tmp` 级别的测试目录里验一次再接管真实仓库**"),
        src="最近推送 2026-09-01 · 67★ · MIT · TypeScript · 信源 [1121]",
    ),
    dict(
        nid="rpm27c3", name="Awesome-Agent-Context-Compression（上下文压缩综述 + 论文清单）",
        url="https://github.com/YerbaPage/Awesome-Agent-Context-Compression",
        lang="Markdown", stars="90",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已登记未安装")],
        plain="**长程 Agent 上下文压缩的综述 + 论文清单（EMNLP 2026 主会收录，90★ / MIT / 纯 Markdown）。** "
              "按**观测压缩 / 轨迹压缩 / 计划与推理压缩 / 记忆状态压缩 / 表示层压缩**五类切分，"
              "覆盖编码、网页、研究三类 Agent 与多智能体。不含可运行代码。",
        analogy="**它的用处不是给答案，是给分类学。** 我们手里已经有三个压缩相关的具体实现"
                "（DSH 的 `dsh-compaction`、社区的守卫派、`dsh-compressor`），"
                "但**没有一个统一坐标系去判断它们各属于哪一类、失败模式是什么** —— 这份清单就是那把尺。",
        ext=(72, "7.2/10", "**用来给「要不要装某个压缩插件」提供判据**：先定位它属于五类里的哪一类、"
                           "再看这一类的已知失败模式（综述类文档最值钱的就是失败模式）"),
        use=(62, "6.2/10", "纯 Markdown、零依赖、离线可读、MIT —— **成本几乎为零，随时可查**。"
                           "⚠️ 但它**不含实现**，不要指望读完就能省 token"),
        src="最近推送 2026-08-26 · 90★ · MIT · Markdown · 信源 [1122]",
    ),
    dict(
        nid="rpm27c4", name="llm-quant-bench（量化档位到底损失多少精度 —— 硬件与目标机同量级）",
        url="https://github.com/yrougy/llm-quant-bench",
        lang="HTML", stars="10",
        tags=[("t-make", "AI × 验证"), ("t-ok", "已核实待试")],
        plain="**专门量化「GGUF 各档位损失多少精度」的基准**：同一硬件、同一 harness、同一 prompt，"
              "只变量化级别，回答「从 Q6_K 降到 IQ2_XXS 掉多少分」。"
              "跑 BigCodeBench（单元测试）、MUSR（多选题）、BFCL 函数调用（AST 匹配，固定 1000 样本 seed 42），"
              "全部经 `inspect_ai` + llama.cpp，**无 LLM judge、完全确定性**。",
        analogy="**它的硬件就是我们的量级**：**2×RTX 3060 12G / GTX 1070 8G**（消费级）、"
                "llama.cpp `llama-server`、KV cache q4_0、上下文 16384–32768。"
                "我们一直在凭经验选量化档，**它给的是同一台机器上的对照数** —— 这是本批对我们最直接有用的一个。",
        ext=(74, "7.4/10", "**「选 Q4 还是 Q5」从此有数可依**，不必再靠体感；"
                           "「无 LLM judge、完全确定性」也符合我们「判据外移到确定性代码」的主线"),
        use=(70, "7.0/10", "评测集与方法论可**直接复现**。⚠️ 两条：①**`license=null`** → "
                           "结论可引、**代码不要抄进项目**；②作者已因太慢**暂缓 GPQA**，别指望全绿"),
        src="最近推送 2026-09-16 · 10★ · 未声明协议 · HTML · 信源 [1123]",
    ),
    dict(
        nid="rpm27c5", name="llm-arena-vram-calc（把榜单分数换成「我的卡跑不跑得动」）",
        url="https://github.com/kmvaidya/llm-arena-vram-calc",
        lang="Python", stars="2",
        tags=[("t-make", "AI × 验证"), ("t-ok", "已核实待试")],
        plain="**把 Arena 开源模型榜与「参数量 + 各精度显存估算」交叉**，回答"
              "「我的显卡实际能跑哪个最强的模型」。给 **222 个模型**补参数量（已解析 **171 个，77%**），"
              "按 BF16 / FP8 等精度出「每张单卡能跑的最好模型」，"
              "并把 **25% 服务开销（KV cache + 激活 + 框架）** 计入估算。",
        analogy="我们的核心约束是 **16GB 机器**，而每次选型都要人工去算「这个 30B 的 Q4 能不能塞下」。"
                "**它把这步变成一次查询。** 那 25% 服务开销尤其重要 —— 我们自己拍脑袋时最容易漏的就是这块。",
        ext=(68, "6.8/10", "**方法论比数据更值**：把「显存 = 权重 + KV + 激活 + 框架开销」写成公式，"
                           "以后我们自己估任何新模型都能套"),
        use=(58, "5.8/10", "MIT + Python + 纯数据加工（**不用跑推理**）。"
                           "⚠️ 两条：①它的目标档位偏 **H100/B200 大卡**，"
                           "**要自己补一档 12~16GB 消费卡**（RTX 3060 12G / 4070 级）才对我们有意义；"
                           "②README 自述 **AA 数据可能陈旧**（抓取失败时用缓存）→ 数字要复核"),
        src="最近推送 2026-09-23 · 2★ · MIT · Python · 信源 [1124]",
    ),
    dict(
        nid="rpm27c6", name="ghost（本地优先 MCP 记忆：Ollama 可选、不装也能跑）",
        url="https://github.com/wcatz/ghost",
        lang="Go", stars="2",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="给 Claude Code / opencode / Cursor / Codex / Goose 等客户端**共用一份 SQLite 记忆**："
              "存记忆、任务与决策，用 **SQLite FTS5 + 可选本地 embedding** 检索；"
              "**Ollama 是可选**（不装也能全文检索）；consolidation / resolution / supersession "
              "**默认 dry-run，可撤销可关闭**。Go 写的单文件服务，需 Go 1.26+。",
        analogy="**「优雅降级」是这一个最值得抄的设计**：不装 embedding 就退回 FTS5 全文检索，"
                "而不是报错或降智。第十九辑 `tigerless-labs/agent-memory` 的口号是"
                "「plain Markdown as the source of truth」，这个把它做成了**可执行的单文件服务** —— "
                "「一个项目约定在一个客户端学到、下一个客户端能用」正好对应我们在多 harness 之间搬约定的处境。",
        ext=(76, "7.6/10", "**默认 dry-run 的整理/合并/取代**正是我们 `mistakes/` 缺的那一环："
                           "我们现在**只增不合并**（v20 待办 #2 已记），它给了一个「先试算、可撤回」的模板"),
        use=(64, "6.4/10", "`go install github.com/wcatz/ghost/cmd/ghost@latest` + `ghost mcp init`；"
                           "**单文件 SQLite 可自己审阅**（符合房规 #46「记忆要能被查、也要能被审」）。"
                           "⚠️ 2★ 新项目、需 Go 1.26+ → 按 M-0002 **先备好 `mistakes/` 的回滚点再试**"),
        src="最近推送 2026-09-24 · 2★ · Apache-2.0 · Go · 信源 [1125]",
    ),
    dict(
        nid="rpm27c7", name="dsh-plugin-hub（DSH 插件聚合索引站：一键 ETL + 每小时刷新）",
        url="https://github.com/helloHupc/dsh-plugin-hub",
        lang="HTML", stars="13",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已核实待试")],
        plain="**DSH 插件聚合索引站**：合并 **6 个数据源**（GitHub `dsh-plugin` topic 与五个 awesome 列表），"
              "实测去重后 **~3,700+ 条**、未分类率 ~8%，**每小时刷新**，线上 `dsh-plugin-hub.hupc.site`。"
              "**纯 Python + 静态页**：`python3 scripts/aggregate.py` 跑 ETL，`--offline` 用缓存调试，"
              "再 `python3 -m http.server` 本地预览。",
        analogy="**它和我们要做的事情是同一件事，只是对象不同** —— 我们维护的是「游戏 × AI 项目索引」，"
                "它维护的是「DSH 插件索引」。**多源去重 + 分类 + 定时刷新 + 静态页**这条流水线"
                "我们每条都是手写的（`insert_vN_cards.py` 一版一份），它是**自动化的一版**。",
        ext=(82, "8.2/10", "**可抄的不是页面，是流水线的形状**：多源抓取 → 去重 → 分类 → 静态产出 → 定时刷新。"
                           "本辑我们刚把「去重」这一步的判据外移成了可检查项（`index_metrics.py`），"
                           "**它的形状正好是下一步**"),
        use=(66, "6.6/10", "MIT + Python + 静态页，**与「维护静态索引站 + 写 Python 检查脚本」画像完全对齐**。"
                           "⚠️ 需联网抓 GitHub API（我们的环境走代理没问题，但要注意速率限制）"),
        src="最近推送 2026-09-24 · 13★ · MIT · HTML · 信源 [1126]",
    ),
    dict(
        nid="rpm27c8", name="godot-mcp-cli（把引擎交互做成 CLI 而不是 MCP —— 为了省 token）",
        url="https://github.com/nguyenchiencong/godot-mcp-cli",
        lang="GDScript", stars="12",
        tags=[("t-make", "游戏 × 引擎"), ("t-ok", "已登记未安装")],
        plain="把 Godot 交互做成 **CLI 而非直接 MCP**，理由写得很直白：**只有工具输出进上下文，省 token**。"
              "覆盖场景/节点/脚本/着色器编辑、运行时场景快照、表达式求值、断点与单步调试、输入模拟、"
              "**把场景渲染成 PNG 给视觉模型看**，以及生成 `project_guide.md` / `AGENTS.md`。",
        analogy="**这是本辑「上下文预算」主线在工具选型上的直接落点。** 我们一直在做 MCP 化的相反方向，"
                "而它给出的是反向取舍：**同一个能力，MCP 进上下文的是「工具定义」，CLI 进上下文的是「输出」** —— "
                "工具定义是常驻的、输出是一次性的。对 16GB + 小模型的机器，这个差别很大。",
        ext=(78, "7.8/10", "**可映射到 Ren'Py 的最小工具链**：`launch` → `lint` → `test` → "
                           "`截图` → `check_release.py`，**用 CLI 串起来而不是做成 MCP**。"
                           "我们其实已经有这些命令，缺的是「按 CLI 优先原则重新组织」这个决定"),
        use=(44, "4.4/10", "Godot 侧代码不可复用（本作 Ren'Py，且游戏线 2026-09-23 已终止）；"
                           "**取的是「CLI 优先、MCP 次之」这条判据**，不是实现"),
        src="最近推送 2026-09-23 · 12★ · MIT · GDScript · 信源 [1127]",
    ),
]

FOOTNOTES = [
    ("1120", "https://github.com/Prompthon-IO/agent-systems-handbook",
     "Prompthon-IO/agent-systems-handbook", "316 · 2026-09-24 · 未声明 · MDX"),
    ("1121", "https://github.com/warm3snow/vscode-ollama",
     "warm3snow/vscode-ollama", "67 · 2026-09-01 · MIT · TypeScript"),
    ("1122", "https://github.com/YerbaPage/Awesome-Agent-Context-Compression",
     "YerbaPage/Awesome-Agent-Context-Compression", "90 · 2026-08-26 · MIT · Markdown"),
    ("1123", "https://github.com/yrougy/llm-quant-bench",
     "yrougy/llm-quant-bench", "10 · 2026-09-16 · 未声明 · HTML"),
    ("1124", "https://github.com/kmvaidya/llm-arena-vram-calc",
     "kmvaidya/llm-arena-vram-calc", "2 · 2026-09-23 · MIT · Python"),
    ("1125", "https://github.com/wcatz/ghost",
     "wcatz/ghost", "2 · 2026-09-24 · Apache-2.0 · Go"),
    ("1126", "https://github.com/helloHupc/dsh-plugin-hub",
     "helloHupc/dsh-plugin-hub", "13 · 2026-09-24 · MIT · HTML"),
    ("1127", "https://github.com/nguyenchiencong/godot-mcp-cli",
     "nguyenchiencong/godot-mcp-cli", "12 · 2026-09-23 · MIT · GDScript"),
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

    desc = ('第二十一辑的 GitHub 那一路逐仓库走 REST API 实测'
            '（stars / forks / license / language / pushed / created 无一估算），'
            '再逐条 grep 过 18 份存档 + 1120 项索引。'
            '剔掉的已收录项：<code>banjtheman/renpy_mcp_server</code> · '
            '<code>Muanchen2/renpy-mcp</code> · <code>EleutherAI/lm-evaluation-harness</code> · '
            '<code>IvanMurzak/Godot-MCP</code>·<code>Unity-MCP</code>·<code>Unreal-MCP</code>。'
            '<strong>本版主线是「判据外移 + 先核实再落笔」—— '
            '记忆在写入前加只读探针、压缩先无损剪枝、确定性检查要能合并且不调模型。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm27g">',
             '      <div class="group-title" data-page-node-id="rpm27gt">🆕 第二十七版增补 · 判据外移 + 先核实再落笔（8 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm27gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm27r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm27ra%s">%s</a> — %s</div>'
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
