# -*- coding: utf-8 -*-
"""第三十版增补：把第二十五辑新发现的 15 个条目登记进 index.html。

本辑候选池 75 条（GitHub 28 / 中文社媒 24+ / 官方与海外 23），
其中 GitHub 路 28 个仓库全部走 `gh api repos/<r>` 实测（★ / 许可证 / 语言 / 推送日无一估算）。
本版取 15 项，优先「上下文与记忆（本辑第一优先）+ DSH 生态 + 编辑器 + 安全」。

主线：**压缩与记忆从"技巧"变成"基础设施"** —— 官方 API 有了压缩策略、社区有了记忆插件
市场、五朵云给了五套 memory 路线；但**账要自己算**（压缩=额外一次采样、harness 首调 30,271 token）。

数据来源：2026-09-24 GitHub REST API 实测（`_r25/_r25_gh.md`）。
幂等：已存在标记则退出 0。
用法：python insert_v30_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1152"'
FIRST_NEW_FOOTNOTE = 1153
MARKER = "第三十版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第二十九版增补 2026-09-24',
    '共 1153 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项 + 第二十八版增补 13 项 + 第二十九版增补 12 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十版增补 2026-09-24',
    '共 1168 个项目',
    '第二十五版增补 8 项 + 第二十六版增补 8 项 + 第二十七版增补 8 项 + 第二十八版增补 13 项 + 第二十九版增补 12 项 + 第三十版增补 15 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm30c1", name="ai-memory（跨厂商把上下文从 A 家交给 B 家）",
        url="https://github.com/akitaonrails/ai-memory",
        lang="Rust", stars="8256",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="给各种 agent coding CLI 做**长期记忆**，并提供**跨厂商 handoff**：把上下文从一家 agent 交接到另一家。"
              "本辑 ★ 最高的一条。Rust 单二进制 / MIT / 最近推送 2026-09-23。",
        analogy="我们平时在 DSH、Claude Code、本地 Ollama 之间倒腾上下文，靠的是**手写 md**（MEMORY.md / handoff 笔记）。"
                "它是把这件手工活做成**一个能装、能查的组件**，且不绑某一家 CLI —— 这正是我们缺的那一环。",
        ext=(80, "8.0/10", "**跨厂商**这个定位天然可扩展：换客户端不用重写记忆层，"
                           "与本站「约定要在多个外壳间保持一份」的现状直接对口"),
        use=(72, "7.2/10", "Rust 单二进制、16GB 机器零压力；⚠️ **未本机实测**（只核 API / README / 目录），"
                           "按房规先登记不装；562 forks 说明有人真在用"),
        src="最近推送 2026-09-23 · 8256★ · MIT · Rust · 信源 [1153]",
    ),
    dict(
        nid="rpm30c2", name="dsh-market（DSH 插件的可视化市场，当雷达用）",
        url="https://github.com/dsh-market/dsh-market",
        lang="TypeScript", stars="4476",
        tags=[("t-mod", "DSH 插件"), ("t-ok", "已核实待试")],
        plain="直接嵌在 DeepSeek Harness 里的**插件市场**：浏览、搜索、一键安装。MIT / TypeScript。",
        analogy="我们不是插件作者，装它意义有限；但它是**观察「dsh 生态里哪些插件真有量」的最佳观测点**。"
                "本辑实测：社区精选列表 **3,632 个插件**（要求声明 `dsh.bundle` 且能 `dsh plugin add`），"
                "其中**记忆类 173 个** —— 说明「跨会话记忆」已是成规模的一类需求。",
        ext=(55, "5.5/10", "生态观测价值高于使用价值；分类分布可直接用来判断某条支线值不值得跟进"),
        use=(48, "4.8/10", "⚠️ 它是 dsh 内嵌界面，本机若不跑 dsh 就用不上"),
        src="最近推送 2026-09-24 · 4476★ · MIT · TypeScript · 信源 [1154]",
    ),
    dict(
        nid="rpm30c3", name="paritok-4b-v1（网关侧非破坏压缩，照 BASE_URL 挂载）",
        url="https://github.com/Paritok-official/paritok-4b-v1",
        lang="Python", stars="1455",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="**非破坏性上下文压缩网关**：用自家开源 4B 模型在请求进主模型前压缩历史，"
              "宣称第一轮省 25%、长会话省到 85%+，对 Claude Code / Cursor / Codex / 任意 `BASE_URL` agent 都是 drop-in。Apache-2.0。",
        analogy="跟第二十九版收的 Context-Gateway 是**同一类做法**（都在门口拦），"
                "差别在**它自带一个压缩模型**。对我们 16GB 机器来说那个 4B 模型是负担（要跟主模型抢显存），"
                "**该抄的是接口形态，不是它的模型**。",
        ext=(70, "7.0/10", "「零客户端改动、只换 BASE_URL」是通用解法，换前端不用重写"),
        use=(52, "5.2/10", "⚠️ 4B 模型本地跑要额外显存 → **不直接采用**；只作「网关侧压缩」的参考实现"),
        src="最近推送 2026-09-20 · 1455★ · Apache-2.0 · Python · 信源 [1155]",
    ),
    dict(
        nid="rpm30c4", name="nobodywho（把本地 LLM 塞进游戏当 NPC 大脑）",
        url="https://github.com/nobodywho-ooo/nobodywho",
        lang="Rust", stars="1346",
        tags=[("t-make", "AI × 游戏"), ("t-warn", "许可证注意")],
        plain="面向游戏 / 任意设备的**本地 LLM 推理引擎**，让游戏里直接跑本地模型，做**真正离线**的 AI NPC。Rust。",
        analogy="我们做 AI NPC 的常见路线是「游戏进程 → 本地 HTTP → Ollama」，多一跳、还得开着服务。"
                "它是**把推理引擎嵌进游戏进程**。对我们 16GB 机器关键是：**能不能直接挂我们已有的 GGUF 权重**。",
        ext=(75, "7.5/10", "「任何设备本地跑 LLM」这个目标与我们的本地路线同源，可当 NPC 推理层的候选"),
        use=(58, "5.8/10", "⚠️ **EUPL-1.2 是弱著佐权**，二次分发需注意；未实测能否挂 Ollama 的 GGUF"),
        src="最近推送 2026-09-24 · 1346★ · EUPL-1.2 · Rust · 信源 [1156]",
    ),
    dict(
        nid="rpm30c5", name="agnix（给 agent 指令文件配一个 linter）",
        url="https://github.com/agent-sh/agnix",
        lang="Rust", stars="423",
        tags=[("t-make", "AI × 工具链"), ("t-ok", "已核实待试")],
        plain="AI 编程助手「缺失的 linter + LSP」：校验 `CLAUDE.md` / `AGENTS.md` / `SKILL.md` / hooks / MCP 配置，"
              "覆盖主流 IDE 插件并支持自动修复。Rust 单二进制 / Apache-2.0。",
        analogy="我们天天写 agent 指令文件（房规、skills、AGENTS.md），**全靠人眼和自家闸门**。"
                "它把这件事变成**确定性校验** —— 正对房规 #33「规则要能被测」的方向："
                "**能机械化的部分交给机器**。",
        ext=(72, "7.2/10", "通用：任何维护 agent 指令集的项目都用得上"),
        use=(75, "7.5/10", "Rust 单二进制、Apache-2.0、装完即用；是本版**最该先试**的一条"),
        src="最近推送 2026-09-20 · 423★ · Apache-2.0 · Rust · 信源 [1157]",
    ),
    dict(
        nid="rpm30c6", name="marm-memory（三合一记忆层，全部落在本地 SQLite）",
        url="https://github.com/Lyellr88/marm-memory",
        lang="Python", stars="402",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="local-first 的「三合一」AI 记忆层 + MCP server：会话历史 + 代码库索引 + 概念图谱，"
              "全融进本地 SQLite，零云、隐私优先，支持多 agent swarm。Apache-2.0。",
        analogy="「**全都落在本地一个 SQLite 文件里**」恰好是我们要的形态：能 grep、能 git、不用起向量库。"
                "比引入向量数据库轻得多，也更容易审计。",
        ext=(68, "6.8/10", "MCP 接口可被多个客户端复用 → 换外壳不用重做记忆"),
        use=(65, "6.5/10", "Python 依赖需留意；⚠️ 未实测索引体积与 16GB 机器上的表现"),
        src="最近推送 2026-09-24 · 402★ · Apache-2.0 · Python · 信源 [1158]",
    ),
    dict(
        nid="rpm30c6b", name="billion-context（小窗口够用论：100K 上下文也能跑长会话）",
        url="https://github.com/ranxianglei/billion-context",
        lang="TypeScript", stars="267",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="中文作者的**上下文压缩插件**，专治小窗口：主张「100K 上下文足矣」，宣称省 5 倍 token，"
              "支持数月级、数十亿 token 的单会话。MIT。",
        analogy="它冲的正是我们的痛点：**本地小参数模型 + 小窗口**。"
                "与「把整库塞进 prompt」相反，它走的是**让会话活得久但喂得少**。",
        ext=(65, "6.5/10", "小窗口 + 省 token 是通用诉求，中文文档降低了读源码成本"),
        use=(70, "7.0/10", "MIT / TypeScript / 中文文档，本版对我们画像最贴合的一条；⚠️ 宣称数字未独立复核"),
        src="最近推送 2026-09-24 · 267★ · MIT · TypeScript · 信源 [1159]",
    ),
    dict(
        nid="rpm30c7", name="tokenfold（可逆压缩，零第三方调用）",
        url="https://github.com/snchimata/tokenfold",
        lang="Rust", stars="205",
        tags=[("t-make", "AI × 上下文"), ("t-ok", "已核实待试")],
        plain="provider 中立的**私有上下文压缩器**：可逆压缩 schema 与日志，**全程在你自己边界内、零第三方调用**。"
              "Rust / Apache-2.0。",
        analogy="「**零第三方调用**」对我们这条本地路线是硬加分 —— 数据不出本机。"
                "「**可逆**」也和「摘要不可逆地丢信息」是两种哲学，值得对照读。",
        ext=(62, "6.2/10", "Rust 单二进制，适合放在本地 Ollama 前面做日志 / schema 瘦身"),
        use=(64, "6.4/10", "Apache-2.0 商用无忧；⚠️ 未实测压缩率"),
        src="最近推送 2026-09-21 · 205★ · Apache-2.0 · Rust · 信源 [1160]",
    ),
    dict(
        nid="rpm30c8", name="distill（不调用任何 LLM 的上下文智能层）",
        url="https://github.com/Siddhant-K-code/distill",
        lang="Go", stars="181",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="给 LLM agent 的「上下文智能层」：**持久记忆 + 写入时去重 + 敏感度打标 + 冲突检测 + 分层衰减**，"
              "约 12ms，**不调用任何 LLM**。Go / MIT。",
        analogy="我们 `mistakes/` 的做法（写前先检索、避免重复登记）**正是「写入时去重」的手工版**。"
                "「**不调 LLM**」意味着它不烧 token、不占显存 —— 对 16GB 机器是零成本的一层。",
        ext=(75, "7.5/10", "纯确定性组件，与我们的「闸门优先」思路同源；分层衰减是我们最薄的一环"),
        use=(70, "7.0/10", "Go 单二进制、MIT；⚠️ 未实测 12ms 这个数字"),
        src="最近推送 2026-09-24 · 181★ · MIT · Go · 信源 [1161]",
    ),
    dict(
        nid="rpm30c9", name="mneme（DSH 的「会做梦的记忆」插件）",
        url="https://github.com/slow-stack/mneme",
        lang="JavaScript", stars="121",
        tags=[("t-mod", "DSH 插件"), ("t-ok", "已核实待试")],
        plain="DeepSeek Harness 的**跨会话记忆插件**：离线私密，睡眠时自动整合（autoDream），并在记忆面板里可视化。MIT。",
        analogy="第二十辑收过 Anthropic 的 **Claude Dreaming**（读会话 + 旧记忆 → 写新 store，旧的保留）。"
                "这个是**同一思路的 dsh 侧实现**，可拿来对照「记忆整合」到底怎么落地，"
                "而不是只在概念层讨论「agent 该不该做梦」。",
        ext=(60, "6.0/10", "思路通用（记忆整合），实现绑 dsh"),
        use=(55, "5.5/10", "MIT / JS 接入成本低；⚠️ 本机目前没有 dsh 会话在跑，先登记"),
        src="最近推送 2026-09-24 · 121★ · MIT · JavaScript · 信源 [1162]",
    ),
    dict(
        nid="rpm30c10", name="vibe-check（vibe coding 的安全清单：规则 + 审计 + 人工核对）",
        url="https://github.com/benavlabs/vibe-check",
        lang="Python", stars="112",
        tags=[("t-make", "AI × 安全"), ("t-ok", "已核实待试")],
        plain="给 vibe coded 应用的**安全清单**：一份 AI rules 文件 + 自动审计 + 人工核对步骤，三条腿一起上。Python / MIT。",
        analogy="本辑官方路有一条硬证据：**9,041 个 vibe-coded 应用实测，91.0% 至少含一个漏洞，65.8% 的漏洞被判高危**，"
                "且**改 harness / 改提示词能降低但不能消除**。所以「AI rules + 自动审计」这种**制度化**的做法才站得住。",
        ext=(70, "7.0/10", "规则集可直接抄进自己的 agent 指令；通用"),
        use=(68, "6.8/10", "MIT / Python，轻量；⚠️ 规则集需按自己项目改"),
        src="最近推送 2026-09-18 · 112★ · MIT · Python · 信源 [1163]",
    ),
    dict(
        nid="rpm30c11", name="vibe-security-radar（AI 写的代码引入了哪些漏洞，做成清单）",
        url="https://github.com/HQ1995/vibe-security-radar",
        lang="Python", stars="110",
        tags=[("t-make", "AI × 安全"), ("t-ok", "已核实待试")],
        plain="持续追踪「**由 AI 写的代码所引入的漏洞**」的雷达，把 AI 编码带来的真实安全事件做成可追踪清单。Python / MIT。",
        analogy="它是**情报源**不是扫描器：把散落的「某公司被 vibe coded 应用泄数据」这类事件攒成清单。"
                "我们做「vibe coding 安全」主题时，这类**可追溯的事件表**比再写一篇观点文有用。",
        ext=(58, "5.8/10", "情报类，价值随事件积累增长"),
        use=(60, "6.0/10", "MIT / Python，轻量；与本辑 vibe-check 互补（一个给规则，一个给事件）"),
        src="最近推送 2026-09-12 · 110★ · MIT · Python · 信源 [1164]",
    ),
    dict(
        nid="rpm30c12", name="dsh-win32（在原生 Windows 上跑 DeepSeek Harness，不用 WSL）",
        url="https://github.com/sjh9714/dsh-win32",
        lang="TypeScript", stars="68",
        tags=[("t-mod", "DSH 插件"), ("t-ok", "已核实待试")],
        plain="在**原生 Windows**（无需 WSL）上修复并诊断 DeepSeek Harness：官方 PowerShell、Workspace 写入、"
              "快捷方式与旧预设修复。MIT。",
        analogy="**我们就是 Windows 工作区**，且这台机器的沙箱限制一堆（缺 coreutils、PowerShell stdout 不回传、"
                "后台进程不持久）。「不用 WSL」直击痛点，★ 不高但**方向极准**。",
        ext=(55, "5.5/10", "场景专用，但在我们的平台上就是刚需"),
        use=(66, "6.6/10", "MIT / TypeScript；⚠️ ★68 / 3 forks，属早期；先登记，等真要跑 dsh 时优先试它"),
        src="最近推送 2026-09-24 · 68★ · MIT · TypeScript · 信源 [1165]",
    ),
    dict(
        nid="rpm30c13", name="ollama-vscode（Ollama 官方 VS Code 扩展）",
        url="https://github.com/ollama/ollama-vscode",
        lang="TypeScript", stars="52",
        tags=[("t-make", "AI × 编辑器"), ("t-ok", "已核实待试")],
        plain="**Ollama 官方的 VS Code 扩展**：把本机 Ollama 模型直接接进编辑器对话。MIT / TypeScript。",
        analogy="与「16GB + 本地模型」画像**零摩擦**：不用网关、不用 key，装完就能在编辑器里用本机模型。"
                "和之前的做法（手写 HTTP 调用 / 第三方插件）比，**官方出品**少一层信任成本。",
        ext=(58, "5.8/10", "通用：任何在 VS Code 里想用本地模型的人"),
        use=(72, "7.2/10", "官方 + 直连本地 Ollama + MIT，本版**最该先装**的一条；⚠️ open issues 28 条，功能在补齐"),
        src="最近推送 2026-09-14 · 52★ · MIT · TypeScript · 信源 [1166]",
    ),
    dict(
        nid="rpm30c14", name="agent-memory-kit（记忆就是文件夹里的纯文本，写入要你点头）",
        url="https://github.com/awrshift/agent-memory-kit",
        lang="Python", stars="34",
        tags=[("t-make", "AI × 记忆"), ("t-ok", "已核实待试")],
        plain="把 agent 记忆做成**你文件夹里的纯文本文件**，且必须「**agent 提议、你批准**」才写入，每行带日期；"
              "支持会话 handoff，并在你点头后升级为知识与规则。MIT。",
        analogy="和我们 `.workbuddy/memory/` + `mistakes/` 的形态**几乎一样** —— 差别是它把「**人在环批准**」"
                "写成了机制（我们靠纪律）。可 grep、可 git diff、不会被黑盒记忆污染。",
        ext=(62, "6.2/10", "思路可直接照搬到任何维护本地知识库的个人"),
        use=(64, "6.4/10", "MIT / Python；★34 属早期，**当设计参考读**比当工具用更划算"),
        src="最近推送 2026-09-24 · 34★ · MIT · Python · 信源 [1167]",
    ),
]

FOOTNOTES = [
    (1153, "https://github.com/akitaonrails/ai-memory", "akitaonrails/ai-memory",
     "8256★ · MIT · Rust · 2026-09-24 · GitHub REST API 实测"),
    (1154, "https://github.com/dsh-market/dsh-market", "dsh-market/dsh-market",
     "4476★ · MIT · TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1155, "https://github.com/Paritok-official/paritok-4b-v1", "Paritok-official/paritok-4b-v1",
     "1455★ · Apache-2.0 · Python · 2026-09-24 · GitHub REST API 实测"),
    (1156, "https://github.com/nobodywho-ooo/nobodywho", "nobodywho-ooo/nobodywho",
     "1346★ · EUPL-1.2 · Rust · 2026-09-24 · GitHub REST API 实测"),
    (1157, "https://github.com/agent-sh/agnix", "agent-sh/agnix",
     "423★ · Apache-2.0 · Rust · 2026-09-24 · GitHub REST API 实测"),
    (1158, "https://github.com/Lyellr88/marm-memory", "Lyellr88/marm-memory",
     "402★ · Apache-2.0 · Python · 2026-09-24 · GitHub REST API 实测"),
    (1159, "https://github.com/ranxianglei/billion-context", "ranxianglei/billion-context",
     "267★ · MIT · TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1160, "https://github.com/snchimata/tokenfold", "snchimata/tokenfold",
     "205★ · Apache-2.0 · Rust · 2026-09-24 · GitHub REST API 实测"),
    (1161, "https://github.com/Siddhant-K-code/distill", "Siddhant-K-code/distill",
     "181★ · MIT · Go · 2026-09-24 · GitHub REST API 实测"),
    (1162, "https://github.com/slow-stack/mneme", "slow-stack/mneme",
     "121★ · MIT · JavaScript · 2026-09-24 · GitHub REST API 实测"),
    (1163, "https://github.com/benavlabs/vibe-check", "benavlabs/vibe-check",
     "112★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
    (1164, "https://github.com/HQ1995/vibe-security-radar", "HQ1995/vibe-security-radar",
     "110★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
    (1165, "https://github.com/sjh9714/dsh-win32", "sjh9714/dsh-win32",
     "68★ · MIT · TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1166, "https://github.com/ollama/ollama-vscode", "ollama/ollama-vscode",
     "52★ · MIT · TypeScript · 2026-09-24 · GitHub REST API 实测"),
    (1167, "https://github.com/awrshift/agent-memory-kit", "awrshift/agent-memory-kit",
     "34★ · MIT · Python · 2026-09-24 · GitHub REST API 实测"),
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

    desc = ('第二十五辑三路调研（GitHub 28 / 中文社媒 24+ / 官方与海外 23），'
            '本版取 15 项，优先「上下文与记忆 + DSH 生态 + 编辑器 + 安全」。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测，无一估算。'
            '<strong>本辑主线：压缩与记忆从「技巧」变成「基础设施」—— 官方 API 有了压缩策略、'
            '社区有了插件市场、五朵云给了五套 memory 路线；但账要自己算'
            '（Anthropic 压缩=额外一次采样、harness 首调实测 30,271 token）。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm30g">',
             '      <div class="group-title" data-page-node-id="rpm30gt">🆕 第三十版增补 · 上下文·记忆·dsh·编辑器（15 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm30gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm30r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm30ra%s">%s</a> — %s</div>'
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
