# -*- coding: utf-8 -*-
"""第二十九版增补：把第二十三辑新发现的 12 个条目登记进 index.html。

本辑候选池 74 条（GitHub 30 / 中文社媒 29 / 官方与海外 17，三路交叉零重复），
其中 GitHub 路 30 个仓库全部走 `gh api repos/<r>` 实测（★ / 许可证 / 语言 / 推送日
无一估算）。本版取 12 项，优先「上下文管理（本辑第一优先）+ DSH 生态 + 游戏」。

⚠️ **本辑抓到一处口径事故**：子 agent 报 `AdamPlatin123/dsh-plugin-radar` 为 ★420，
`gh api` 实测 **★1467**；而 ★419 其实属于 `liangmianya/dsh-synapse`。
→ ★ 数**串位**。卡片一律以 API 实测为准，并在卡内标注该分歧（承接 M-0019）。

⚠️ 另：中文路点名的 4 个仓库（`Cimpress-MCP/governance-mcp` / `mbuche/spec-kit-go` /
`justinbchau/claudeplay` / `gitcoderdev/awesome-claude-code-subagents`）**`gh api` 全部 404**，
`gh search` 也只搜到名字相近的别家仓库 → 按 M-0002 **不登记**。

本脚本的四道保护（页头锚点 / 最后脚注锚点 / section 唯一性 + 插入点 div 深度 / 重复仓库检测）
沿用第二十八版，已由 `_tools/insert_guard_probe.py` 用真实历史版本做过 6 例正负验证。

数据来源：2026-09-24 GitHub REST API 实测。
幂等：已存在标记则退出 0。
用法：python insert_v29_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1140"'
FIRST_NEW_FOOTNOTE = 1141
MARKER = "第二十九版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第二十八版增补 2026-09-24',
    '共 1141 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项 + 第二十八版增补 13 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第二十九版增补 2026-09-24',
    '共 1153 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项 + 第二十八版增补 13 项 + 第二十九版增补 12 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm29c1", name="Context-Gateway（把压缩做成门口的透明代理）",
        url="https://github.com/Compresr-ai/Context-Gateway",
        lang="Go", stars="642",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="放在**编码 Agent 与模型 API 之间的 Go 代理**：在历史**真正超窗之前**就在后台预压缩，"
              "到触发点直接换入**已经算好的**摘要，而不是等超窗了再停下来现算。Apache-2.0。",
        analogy="我们已有的压缩手段（会话摘要、手工裁剪）都是**进了上下文之后才想办法**，"
                "它是在**门口拦**。关键差别是**预计算** —— 把「停下来等摘要」这段延迟提前消化掉。"
                "而且它是**代理层**，不绑 Claude Code / Cursor 某个具体前端。",
        ext=(74, "7.4/10", "**代理层 = 换客户端不用重写**，这一点对我们「约定要在多个外壳间同步」"
                           "的痛点是通用的；仓库带 Dockerfile + 测试 + 发布工作流，可当参考实现读"),
        use=(70, "7.0/10", "Apache-2.0 / Go。⚠️ **未本机实测**：只核了 API、README、源码目录与 CI，"
                           "没跑远程安装脚本 —— 按房规先登记不装"),
        src="最近推送 2026-09-23 · 642★ · Apache-2.0 · Go · 信源 [1141]",
    ),
    dict(
        nid="rpm29c2", name="codex-task-pointer（压缩后重新锚定主线的小指针）",
        url="https://github.com/big0lives/codex-task-pointer",
        lang="PowerShell", stars="234",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="用「**目标 + 下一步**」这样一枚极小的任务指针 + Codex hooks，"
              "让长任务在**跨过自动压缩之后**能重新锚定主线，不漂移。",
        analogy="它**不造记忆库**，只解决最常见的那件事：**做过又做、目标漂移**。"
                "「记得少但记得准」这个取向和我们 `mistakes/` 的路线一致，"
                "比那些「什么都记」的记忆系统更容易真的用起来。",
        ext=(78, "7.8/10", "**本批可拓展性最高**：CAS、防重复键、原子写入、**压缩后重注入**"
                           "这四件都是能直接搬进我们自己外壳的零件"),
        use=(72, "7.2/10", "MIT / PowerShell。⚠️ 只登记未实测 —— 安装会改用户 Codex hooks，"
                           "不代用户执行。**它的 Windows 安装器支持 `-WhatIf` + 备份 + 回滚**，"
                           "这个形状值得抄（我们写写入型闸门刚踩过 M-0023）"),
        src="最近推送 2026-09-24 · 234★ · MIT · PowerShell · 信源 [1142]",
    ),
    dict(
        nid="rpm29c3", name="opencode-working-memory（长期记忆只给 900 token 的额度）",
        url="https://github.com/sdwolf4103/opencode-working-memory",
        lang="TypeScript", stars="193",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="把 OpenCode 自带的 compaction **顺手**用于记忆抽取，分开维护**跨会话 workspace memory** "
              "与**当前会话 hot state**，全程**不额外调用模型**。",
        analogy="最值得抄的是**配额**：默认长期记忆只给 **约 900 token / 28 条**，"
                "并让热状态**只在 epoch 边界刷新以保护前缀缓存**。"
                "我们「记忆按 token 计预算」那条房规一直缺一个具体数字，这里有了参照。",
        ext=(72, "7.2/10", "**「记忆要有硬上限」+「热状态不动前缀」** 两条合起来，"
                           "正好是我们 `MEMORY.md` 瘦身之后该有的运行机制"),
        use=(74, "7.4/10", "MIT / TypeScript，`npm view` 实测有可装版本 1.6.9。"
                           "⚠️ 未接入真实会话做长期效果测试；另带**凭据脱敏与衰减**，这两点我们还没有"),
        src="最近推送 2026-09-23 · 193★ · MIT · TypeScript · 信源 [1143]",
    ),
    dict(
        nid="rpm29c4", name="self-compact-pi-agent（让 agent 看见自己的用量，再强制它压缩）",
        url="https://github.com/disler/self-compact-pi-agent",
        lang="TypeScript", stars="53",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已登记未实测")],
        plain="让 Pi Agent **看见自己的上下文用量**，在**软提醒 / 警告 / 硬截止**三道阈值之间"
              "主动写 `note_to_self` 并触发压缩；**硬截止后只允许调用 `self_compact`**。",
        analogy="这一条把「上下文是预算」做成了**机制而不是口号**：先给预算表（看得见），"
                "再给强制动作（硬截止后只剩一条路）。我们只有预算表（探针），没有强制动作。",
        ext=(76, "7.6/10", "**「看得见 + 到点强制」这个组合可抄** —— "
                           "我们第十八辑做了探针，但到阈值之后仍靠人自觉"),
        use=(58, "5.8/10", "MIT，但要求 Pi v0.85.1 + Node 24 + `just`，本机**环境不满足** → 只登记。"
                           "★53 说明还很早期，别当成熟方案"),
        src="最近推送 2026-09-23 · 53★ · MIT · TypeScript · 信源 [1144]",
    ),
    dict(
        nid="rpm29c5", name="cliffcompaction（透明代理 + 只观察不改写模式）",
        url="https://github.com/nguyenvuthientrang/cliffcompaction",
        lang="Python", stars="34",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="透明 API 代理：请求越过 token 阈值时，把旧历史换成"
              "「**开头原文 + 单条摘要 + 最近若干轮**」。Agent **不用改一行代码**就能接。",
        analogy="**最值得抄的是 `--shadow` 模式：只观察、不改写。** 我们新写的写入型闸门"
                "（M-0023 那次事故）最缺的就是这一步 —— 先跑一遍看它想改什么，再决定放不放行。",
        ext=(68, "6.8/10", "**`--shadow` 观察模式 + 按原始前缀链哈希匹配**，"
                           "正好是「代理层压缩 vs 客户端原生压缩」的对照实验装置"),
        use=(64, "6.4/10", "MIT / Python，`pip index versions` 实测已发布 0.1.0。"
                           "⚠️ 未启动代理实测；★34 早期项目"),
        src="最近推送 2026-09-24 · 34★ · MIT · Python · 信源 [1145]",
    ),
    dict(
        nid="rpm29c6", name="prompt-cache-skills（逐个审计外壳的缓存断点）",
        url="https://github.com/OnlyTerp/prompt-cache-skills",
        lang="Python", stars="114",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="**逐个审计**编码 Agent 外壳的**请求组装方式**，提供可移植技能修复"
              "缓存断点、动态时间戳、缺失的 cache key。",
        analogy="我们 `AGENTS.md` §四 那条「**不变项在前、变化项在后**」一直只有原则、没有对照表。"
                "它给了 13 份已完成审计，**还区分「已证实工作 / 需要修 / 闭源无法验证」**——"
                "这个三分法本身就是判据外移的样本。",
        ext=(74, "7.4/10", "**「稳定前缀放前、动态块放后」有了逐外壳的实测清单**，"
                           "可以直接拿来对我们的桥与外壳做一次自查"),
        use=(62, "6.2/10", "⚠️ **许可证未声明**（GitHub API 为 NOASSERTION）→ 引用时不要写许可证名。"
                           "另：它的双请求缓存探针**会产生真实模型费用**，未运行"),
        src="最近推送 2026-09-18 · 114★ · 未声明协议 · Python · 信源 [1146]",
    ),
    dict(
        nid="rpm29c7", name="dsh-synapse（把 DSH 会话投影成可拖拽的地图）",
        url="https://github.com/liangmianya/dsh-synapse",
        lang="JavaScript", stars="419",
        tags=[("t-make", "AI × 外壳"), ("t-ok", "已核实待试")],
        plain="把同一工作区的 DSH **会话、追问与 fork 投影成可拖拽缩放的地图**，"
              "并保持**原生 session log 为唯一事实源**。",
        analogy="**最关键的一句：地图只保存布局，删掉 `$DSH_HOME/synapse/` 不伤会话。** "
                "这是「视图与数据分离」做对了的样本 —— 很多可视化工具把历史另存一份，"
                "于是两边会打架（我们自己在 M-0005 踩过并发写同一文件）。",
        ext=(70, "7.0/10", "**从画布切回对话仍是同一个 DSH session** —— "
                           "升级成可视化分支导航，而不另造一个历史库"),
        use=(68, "6.8/10", "MIT / JavaScript，`npm view` 实测 0.4.1。"
                           "⚠️ 未在本机 DSH web profile 安装（本轮无 DSH 会话在跑）"),
        src="最近推送 2026-09-24 · 419★ · MIT · JavaScript · 信源 [1147]",
    ),
    dict(
        nid="rpm29c8", name="dsh-plugin-radar（插件生态雷达：发现→验证→快照）",
        url="https://github.com/AdamPlatin123/dsh-plugin-radar",
        lang="Python", stars="1467",
        tags=[("t-make", "AI × 外壳"), ("t-new", "本轮头条")],
        plain="持续**发现 DSH 插件 → 检查包结构 → 用隔离运行环境做兼容性实测**，"
              "每 15 分钟输出一次快照。当日快照标注 **1345 个确认插件 / 13556 次测试**。",
        analogy="**它不是又一份手工 awesome 清单，是一条流水线**：候选发现 → 克隆验证 → "
                "runtime test → 可追溯状态 → JSON 下游接口。这正好打在我们的痛点上 —— "
                "M-0016（README 写了 ≠ 能装）只能一条条人工试，它是**机器批量试**。",
        ext=(80, "8.0/10", "**本批可拓展性最高**：「用隔离环境实测可安装性」这个动作，"
                           "是我们去重工序里唯一还靠人肉的一环，可以直接照它的形状做"),
        use=(66, "6.6/10", "MIT / Python。⚠️ 两条：①**★ 数有分歧** —— 二手来源报 420，"
                           "`gh api` 2026-09-24 实测 1467（★419 实际属于 `dsh-synapse`，疑为串位）；"
                           "②只登记未复跑其 K8s 验证管线，**具体插件仍要按测试日期复核**"),
        src="最近推送 2026-09-24 · 1467★（API 实测）· MIT · Python · 信源 [1148]",
    ),
    dict(
        nid="rpm29c9", name="re-engine-mcp（让 agent 在**活着的游戏**里改东西）",
        url="https://github.com/praydog/re-engine-mcp",
        lang="C#", stars="34",
        tags=[("t-make", "AI × 游戏"), ("t-ok", "已登记未实测")],
        plain="借 REFramework.NET 把**运行中的**《生化危机》《怪物猎人》《DMC》等 RE Engine 游戏的"
              "对象、日志与热重载**暴露为 MCP 工具**（50+ 个）。",
        analogy="和「读资源文件」的方案是两回事：它能在**活游戏里**查对象图、读写字段、调方法、"
                "编译插件、**看错误再修**。这让「AI 辅助 Modding」第一次成为**真闭环** —— "
                "改了能立刻看见，而不是猜。",
        ext=(70, "7.0/10", "**「运行 — 观察 — 操作 — 验证」这个回路的形状**，"
                           "对任何引擎的 AI 辅助改造都成立，不只对 RE Engine"),
        use=(50, "5.0/10", "MIT / C#。⚠️ **无公开 release**，依赖 REFramework nightly + 对应 C# API + .NET 10 → "
                           "只登记未实测；★34 早期"),
        src="最近推送 2026-09-23 · 34★ · MIT · C# · 信源 [1149]",
    ),
    dict(
        nid="rpm29c10", name="renforge-mcp（Ren'Py 的运行—观察—操作—验证回路）",
        url="https://github.com/alex-jordan547/renforge-mcp",
        lang="Python", stars="10",
        tags=[("t-make", "AI × 游戏"), ("t-ok", "已核实待试")],
        plain="Ren'Py 的 **MCP + CLI + Web 控制台**：检查项目、启动游戏、看截图 / 场景树、"
              "**点击运行中的界面**，并把可编辑布局**保存回源码**。",
        analogy="和那些只「生成 `.rpy`」的方案不同，它补齐了**后半段回路**。"
                "而且**每个工具显式传 `project_path`** —— 这个细节很关键："
                "我们第十一辑踩过 Ren'Py MCP 用白名单判据乱改字体的坑（M-0008），显式传路径至少不会改错项目。",
        ext=(66, "6.6/10", "**还管翻译统计**，对做过本地化的视觉小说直接对口；"
                           "「把布局改回源码」这一点是其它工具没有的"),
        use=(48, "4.8/10", "MIT / Python，`pip index versions` 实测 0.7.2。"
                           "⚠️ **★10 极早期**；游戏线已终止，本条只作工具形态参考，不落地"),
        src="最近推送 2026-09-13 · 10★ · MIT · Python · 信源 [1150]",
    ),
    dict(
        nid="rpm29c11", name="mobilegym（可复现的 GUI agent 评测，不是真机点击榜单）",
        url="https://github.com/Purewhiter/mobilegym",
        lang="Python", stars="799",
        tags=[("t-make", "AI × 评测"), ("t-ok", "已核实待试")],
        plain="在浏览器里**并行模拟手机应用**，用**结构化状态 + 代码级 judge** 对 GUI Agent "
              "做可验证评测与在线强化学习。**28 个应用 / 416 个参数化任务模板**。",
        analogy="**单实例约 400MB 内存**——16GB 本机跑得动。最重要的是它用**代码级 judge** "
                "而不是「看起来像不像」，这跟我们「判据外移到确定性代码」是同一条路。"
                "比那些不可复现的真机点击榜单更适合当**回归测试**。",
        ext=(76, "7.6/10", "**新 app / task / agent / judge 都走模块清单扩展** —— "
                           "这个扩展方式可以直接抄来组织我们自己的闸门"),
        use=(60, "6.0/10", "Apache-2.0 / Python，EMNLP 2026 Main 接收。⚠️ 约 1.9GB companion dataset 未下载、"
                           "未复跑排行榜，**性能数字仅按仓库公开口径登记**"),
        src="最近推送 2026-09-24 · 799★ · Apache-2.0 · Python · 信源 [1151]",
    ),
    dict(
        nid="rpm29c12", name="PIArena（提示注入攻防的统一评测入口）",
        url="https://github.com/sleeepeer/PIArena",
        lang="Python", stars="52",
        tags=[("t-make", "AI × 安全"), ("t-ok", "已核实待试")],
        plain="统一运行**提示注入攻击与防御评测**的 ACL 2026 工具箱，把 AgentDojo / AgentDyn / "
              "InjecAgent 接到**同一个实验入口**。",
        analogy="对**工具调用型** agent 做上线前安全回归，比看通用问答 benchmark 实际得多。"
                "我们有「外部内容不得直写记忆」那条房规（#46），但**没有验证它的手段** —— "
                "这正是能补上的那一半。",
        ext=(70, "7.0/10", "**可自定义攻击 / 防御 / 数据集**，并能在 workspace、slack、travel、"
                           "shopping、github 等场景横向比较防护效果"),
        use=(58, "5.8/10", "MIT / Python。⚠️ 未下载模型与数据集跑完整评测，"
                           "**只登记可复现实验入口**；★52 早期"),
        src="最近推送 2026-09-22 · 52★ · MIT · Python · 信源 [1152]",
    ),
]

FOOTNOTES = [
    (1141, "https://github.com/Compresr-ai/Context-Gateway", "Compresr-ai/Context-Gateway",
     "642★ · Apache-2.0 · Go · 2026-09-24 · GitHub REST API 实测"),
    (1142, "https://github.com/big0lives/codex-task-pointer", "big0lives/codex-task-pointer",
     "234★ · MIT · PowerShell · 2026-09-24 · GitHub REST API 实测"),
    (1143, "https://github.com/sdwolf4103/opencode-working-memory", "sdwolf4103/opencode-working-memory",
     "193★ · MIT · TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1144, "https://github.com/disler/self-compact-pi-agent", "disler/self-compact-pi-agent",
     "53★ · MIT · TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1145, "https://github.com/nguyenvuthientrang/cliffcompaction", "nguyenvuthientrang/cliffcompaction",
     "34★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
    (1146, "https://github.com/OnlyTerp/prompt-cache-skills", "OnlyTerp/prompt-cache-skills",
     "114★ · 未声明协议（NOASSERTION）· Python · 2026-09-24 · GitHub REST API 实测"),
    (1147, "https://github.com/liangmianya/dsh-synapse", "liangmianya/dsh-synapse",
     "419★ · MIT · JavaScript · 2026-09-24 · GitHub REST API 实测"),
    (1148, "https://github.com/AdamPlatin123/dsh-plugin-radar", "AdamPlatin123/dsh-plugin-radar",
     "1467★ · MIT · Python · 2026-09-24 · GitHub REST API 实测（⚠️ 二手来源报 420，疑与 dsh-synapse 串位）"),
    (1149, "https://github.com/praydog/re-engine-mcp", "praydog/re-engine-mcp",
     "34★ · MIT · C# · 2026-09-24 · GitHub REST API 实测"),
    (1150, "https://github.com/alex-jordan547/renforge-mcp", "alex-jordan547/renforge-mcp",
     "10★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
    (1151, "https://github.com/Purewhiter/mobilegym", "Purewhiter/mobilegym",
     "799★ · Apache-2.0 · Python · 2026-09-24 · GitHub REST API 实测"),
    (1152, "https://github.com/sleeepeer/PIArena", "sleeepeer/PIArena",
     "52★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
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

    desc = ('第二十三辑三路调研（GitHub 30 / 中文社媒 29 / 官方与海外 17），'
            '本版取 12 项，优先「上下文管理 + DSH 生态 + 游戏」。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测，无一估算。'
            '<strong>本辑主线是「核实本身」—— 抓到一处 ★ 数串位（dsh-plugin-radar 二手报 420、'
            'API 实测 1467），另有 4 个中文帖点名的仓库 `gh api` 全部 404、按 M-0002 不登记。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm29g">',
             '      <div class="group-title" data-page-node-id="rpm29gt">🆕 第二十九版增补 · 上下文管理与核实（12 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm29gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm29r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm29ra%s">%s</a> — %s</div>'
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
