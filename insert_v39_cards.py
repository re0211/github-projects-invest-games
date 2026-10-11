# -*- coding: utf-8 -*-
"""第三十九版增补：把第三十四辑「身体侧供给爆炸 + 官方一手根因」的 24 个条目登记进 index.html。

本辑候选：gh 路 34 条正文（+26 行边缘登记）、cn 路 22 条、official 路 25 条。
与 `index.html`（1325 项）及全部历史存档机器比对，本版 24 条命中 **0**。

**本辑主线：上一辑在看「墙两侧长出两丛轮子」；这一辑的看点变了 —— 「身体」侧的供给第一次压过「格式」侧，
而官方论坛的一手正文第一次给出了「模型越做越存不动」的根因。**

1. **桌宠「身体」侧本辑最密集** —— `Project-N-E-K-O/N.E.K.O`（★3044，会主动找你玩的 AI 猫娘）、
   `jofizcd/Soul-of-Waifu`（★1386，Live2D/VRM 双头像 + 本地 LLM）、`marine841023/duty-on`（★3，
   Tauri 2 + Rust，**监听你的 AI 编码 agent 状态**）、`Lsc-91-69/dsh-live2d-avatar`（★1，DSH 插件把 Live2D 变桌宠）、
   `1704919/WuziDesktopPet`（★2，Godot 4.7 Windows 桌宠）。
2. **绕开 Cubism 的绑定线出现「可验证流水线」** —— `rig-c/core`（★12）把 rig spec 编译成 **Spine 4.3** skeleton，
   先做命名断言 + spine-core round-trip 校验、**只输出通过校验的结果**，并以 agent skill 形式分发；配 `rig-c/parts`。
3. **格式线继续补厚度** —— `Eatgrapes/Mocari`（★47 纯 Rust moc3 运行时）、`UlyssesWu/D2Evil`（★139 C# waifu 格式解析）、
   `MangoLion/stretchystudio`（★504 静态插画→网格可变形）。
4. **官方论坛 4 条一手正文（本辑最硬，全部新增）** —— ① **5.3「保存失败」根因**：
   **不是文件大（470MB），是参数数「相乘」爆炸**，解法 = **blend shape（加法）替代普通 key**；
   ② **Unity 6.6 + URP3D** 下「Scene 能渲染、运行时不渲染」，官方已复现认领；
   ③ 外部联携 API **做不到的 4 件事**（复制对象 / 复制 keyform / 左右镜像）；
   ④ 图集反转复制后 `NoArtMesh` 是**规格不是 bug**，附官方恢复法。
5. **AI 开发侧**：DSH 生态继续成形（`MemTensor/MemOS` ★11802 / `crafter-station/petdex` ★4226 /
   `bruc3van/awesome-dsh-plugin` ★402 —— 生态里**唯一明确做去伪复核**的清单）。

**inbox 顺延**：`/skill-doctor` 本轮**已做**（21 技能逐个体检，见 csdn 汇总）；
`updated_at` vs `pushed_at` 双向落进卡片（本版 src 行起固定打印两个日期）。

数据来源：2026-10-11 GitHub REST API + 官方站/论坛实测（`gh api repos/<r>` 逐条，主 agent 已复验全部 20 个候选仓库，
与子 agent 汇报零出入）。幂等：已存在本版标记则跳过。
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1324"'
FIRST_NEW_FOOTNOTE = 1325
MARKER = "第三十九版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十八版增补 2026-10-11',
    '共 1325 个项目',
    '第三十六版增补 22 项 + 第三十七版增补 22 项 + 第三十八版增补 24 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十九版增补 2026-10-11',
    '共 1355 个项目',
    '第三十六版增补 22 项 + 第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项（均与上版零重复）',
]

# ext = (条宽百分比, 显示分值, 说明)  use 同
CARDS = [
    # ---------- A. 桌宠「身体」侧（本辑最密集） ----------
    dict(
        nid="rpm39c1", name="N.E.K.O —— 会主动找你玩的 AI 猫娘（★3044）",
        url="https://github.com/Project-N-E-K-O/N.E.K.O",
        lang="Python", stars="3044",
        tags=[("t-make", "建模"), ("t-ok", "每日更新"), ("t-new", "新")],
        plain="一个**会主动来找你玩**的 AI 猫娘：实时陪伴、**主动发起对话**、一起看共享媒体，带「具身情绪引擎」，由**本地 LLM** 驱动。",
        analogy="多数桌宠是「你点它才动」。它是反过来 —— **它先动**。这在产品上是个关键分岔：把桌宠从「宠物挂件」变成「有自己节奏的室友」。"
                "而且它是 **Apache-2.0 + Python 栈**，和你本机 Ollama 的路子同一条。",
        warn="⚠️ 「主动发起」是把双刃剑：它会消耗推理（本地还行，接云就要注意账单），也会在你要专注时打扰你 —— 官方默认的打扰节奏要自己调。",
        ext=(85, "8.5/10", "身体 + 人格 + 主动性三层都齐，是桌宠侧最完整的参考实现"),
        use=(75, "7.5/10", "Python + 本地 LLM，本机可直接试；当日仍在推送"),
        src="创建 2025-06-29 · 推送 2026-10-11 · 更新 2026-10-11 · 3044★ · Apache-2.0 · Python · 信源 [1325]",
    ),
    dict(
        nid="rpm39c2", name="Soul-of-Waifu —— Live2D / VRM 双头像的桌面伴侣（★1386）",
        url="https://github.com/jofizcd/Soul-of-Waifu",
        lang="Python", stars="1386",
        tags=[("t-make", "建模"), ("t-warn", "低频更新"), ("t-new", "新")],
        plain="桌面角色扮演 & AI 伴侣应用，**同时支持 Live2D 与 VRM 头像**、语音、本地 LLM，从聊天一路演进到 RPG / 桌面陪伴。",
        analogy="它的价值在**功能面最全**：想看「一个成熟的 AI 伴侣该有哪些模块」时，翻它一份就够。"
                "但它是 **GPL-3.0** —— 你若想二次分发/闭源上架，传染性会咬人。",
        warn="⚠️ **GPL-3.0 传染**：链接使用没问题，但改了它再分发包必须开源。自用无碍，做产品要先想清楚。",
        ext=(60, "6.0/10", "功能面最全的整合参考，但不宜当底座"),
        use=(55, "5.5/10", "Python 可跑；GPL 与「已 1.5 个月未推送」两条要权衡"),
        src="创建 2023-09-02 · 推送 2026-08-28 · 更新 2026-10-11 · 1386★ · GPL-3.0 · Python · 信源 [1326]",
    ),
    dict(
        nid="rpm39c3", name="duty-on —— 桌宠当你的 AI 编码 agent 状态灯（★3）",
        url="https://github.com/marine841023/duty-on",
        lang="Rust", stars="3",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="**Tauri 2 + Rust** 的 Live2D 桌宠，核心功能是**监听你的 Trae / Qoder 等 AI 编码 agent 的实时状态** —— agent 在等你输入时，用模型的动作提醒你。",
        analogy="这就是上一辑「你的桌宠不需要大脑」那句主张的**具体实现**：桌宠不参与推理，它只当**状态显示器**。"
                "对你这种「开着好几个 agent 跑长任务」的人，这是**真实痛点**（agent 卡在等你确认，你去干别的了）。",
        warn="⚠️ 极小项目（★3、单人），且 —— **反向异常**：`updated_at`(2026-08-23) 比 `pushed_at`(2026-10-09) **还旧**，"
             "说明它连 README 都没顺手更新。**别当依赖，当范式抄**。",
        ext=(70, "7.0/10", "范式清楚、Rust+Tauri 体量小；但只有一个人维护"),
        use=(45, "4.5/10", "想法可直接抄，代码成熟度不够"),
        src="创建 2026-08-03 · 推送 2026-10-09 · 更新 2026-08-23（⚠️ 反向异常）· 3★ · MIT · Rust · 信源 [1327]",
    ),
    dict(
        nid="rpm39c4", name="dsh-live2d-avatar —— DSH 插件：把 Live2D 变桌宠并显示 agent 状态（★1）",
        url="https://github.com/Lsc-91-69/dsh-live2d-avatar",
        lang="JavaScript", stars="1",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="DSH（DeepSeek Harness）插件：把 Live2D 模型变成桌宠，**实时展示 agent 的状态与「内心想法」**。",
        analogy="它的价值不在代码（★1、刚建 4 天），而在**它证明了这条接口是通的** —— "
                "「DSH 插件协议 → Live2D 桌宠」之间不需要什么魔法，一个 MIT 的小插件就够了。",
        warn="⚠️ 刚建仓（2026-10-07），MIT、代码量小，**只能当样例读**，不要当依赖。",
        ext=(55, "5.5/10", "接口打通的证据，方向对"),
        use=(35, "3.5/10", "太新太小，仅作样例"),
        src="创建 2026-10-07 · 推送 2026-10-07 · 更新 2026-10-07 · 1★ · MIT · JavaScript · 信源 [1328]",
    ),
    dict(
        nid="rpm39c5", name="WuziDesktopPet —— Godot 4.7 写的 Windows 桌宠（★2）",
        url="https://github.com/1704919/WuziDesktopPet",
        lang="GDScript", stars="2",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="基于 **Godot 4.7** 的 Windows 桌宠：随机动画、**离线对话**、桌面互动，还带图片转换与批量重命名。",
        analogy="Godot 在 Windows 上有**原生透明窗**优势 —— 不用折腾 Electron 的窗口穿透，这是它相对 Web 栈的真正卖点。"
                "而且它顺手把「离线对话」做进来了，等于把 LLM 环节也放进了同一个工程。",
        warn="⚠️ 刚建仓（2026-10-10）、★2，**是骨架不是成品**。",
        ext=(65, "6.5/10", "Godot 原生透明窗 + 离线对话，路线有前途"),
        use=(40, "4.0/10", "太新，先围观"),
        src="创建 2026-10-10 · 推送 2026-10-11 · 更新 2026-10-11 · 2★ · MIT · GDScript · 信源 [1329]",
    ),
    # ---------- B. 绕开 Cubism 的绑定线 ----------
    dict(
        nid="rpm39c6", name="rig-c/core —— 把「AI 自动绑定」做成可验证流水线（★12）",
        url="https://github.com/rig-c/core",
        lang="TypeScript", stars="12",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="**「AI 编写 2D rigging」**：把 rig spec 编译成 **Spine 4.3** 的 skeleton 格式；"
              "先用**命名断言 + spine-core round-trip 校验**，**只输出通过校验的结果**，并以 **agent skill** 形式分发。",
        analogy="本辑「方向最有意思」的一个。它做了三件别家没做的事：① **不碰 Cubism**，改输出 Spine 格式（另一条合法路）；"
                "② 把「AI 生成」和「机器校验」绑成一条流水线 —— **校验不过就不出结果**，这正是房规 #33 的形态；"
                "③ 以 skill 分发，说明它天生是喂给 agent 用的。",
        warn="⚠️ **许可证是 NOASSERTION**（自定义/未声明），商用前必须自己读一遍许可文件。★只有 12，属早期。",
        ext=(80, "8.0/10", "「生成 + 校验」闭环 + 绕开 Cubism，方向价值高"),
        use=(50, "5.0/10", "早期项目 + 许可不明，先学结构"),
        src="创建 2026-08-22 · 推送 2026-10-11 · 更新 2026-10-11 · 12★ · 许可未声明 · TypeScript · 信源 [1330]",
    ),
    dict(
        nid="rpm39c7", name="rig-c/parts —— 把一张画组装成 rig-ready 图层 + 带权重网格（★2）",
        url="https://github.com/rig-c/parts",
        lang="TypeScript", stars="2",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="`rig-c/core` 的配套件：把一张画（先经 see-through 那类工具分层）**组装成 rig-ready 的 PNG 图层 + 带权重的网格 rig spec**，再交给 core 编译校验。",
        analogy="（配套参考：`rig-c/core` 的输入侧）它把「图层准备」这一步也自动化了 —— "
                "整条链于是变成：**单图 → 分层 → 组装成 rig spec → 编译校验 → Spine skeleton**。",
        ext=(50, "5.0/10", "必须与 core 成套，单用无意义"),
        use=(30, "3.0/10", "配套件，不单独评估"),
        src="创建 2026-09-27 · 推送 2026-10-11 · 更新 2026-10-11 · 2★ · MIT · TypeScript · 信源 [1331]",
    ),
    dict(
        nid="rpm39c8", name="Mocari —— 纯 Rust 的 moc3 运行时实验（★47）",
        url="https://github.com/Eatgrapes/Mocari",
        lang="Rust", stars="47",
        tags=[("t-make", "建模"), ("t-warn", "更新放缓"), ("t-new", "新")],
        plain="纯 Rust 的 Live2D/Cubism 运行时实验，**自己解析 moc3** —— Rust 生态里最接近「绕开官方 Cubism SDK 自建运行时」的实现。",
        analogy="与上一辑的 `ayagami`、`moc3-rs` 同一条路（自己读格式，不链接官方专有 Core）。"
                "它的意义是**确认这条路上有多少人**：目前是 ayagami 领跑，Mocari 是 Rust 侧唯一有实质代码量的第二家。",
        warn="⚠️ 实验性质、非成品；且 `updated_at`(2026-10) 比 `pushed_at`(2026-07) 新 3 个月 —— **热度虚高**。",
        ext=(45, "4.5/10", "方向对、推进偏慢，一人维护"),
        use=(25, "2.5/10", "不能当依赖，可当格式参考"),
        src="创建 2026-05-31 · 推送 2026-07-13 · 更新 2026-10-10（⚠️ 差 3 个月）· 47★ · MIT · Rust · 信源 [1332]",
    ),
    dict(
        nid="rpm39c9", name="D2Evil —— C# 侧的 waifu 格式解析库（★139）",
        url="https://github.com/UlyssesWu/D2Evil",
        lang="C#", stars="139",
        tags=[("t-make", "建模"), ("t-warn", "更新放缓"), ("t-new", "新")],
        plain="托管端（.NET/C#）的 waifu 模型解析库，**能读 moc3 / psd 等多种格式** —— C#/Unity 侧做格式解析、格式转换的参考实现。",
        analogy="本辑 moc3 侧**星最高、格式覆盖最全**的一个。你若走 Unity/C# 路线，它是「不装官方 SDK 也能把文件读开」的现实选项。",
        warn="⚠️ 许可证 **NOASSERTION（自定义，需自查）**；已约 4 个月无推送。",
        ext=(55, "5.5/10", "格式覆盖最全，但停更倾向 + 许可不明"),
        use=(40, "4.0/10", "Unity/C# 路线可看，Web/Python 路线无关"),
        src="创建 2019-09-21 · 推送 2026-06-07 · 更新 2026-09-24 · 139★ · 许可未声明 · C# · 信源 [1333]",
    ),
    dict(
        nid="rpm39c10", name="stretchystudio —— 静态插画 → 网格可变形角色（★504）",
        url="https://github.com/MangoLion/stretchystudio",
        lang="JavaScript", stars="504",
        tags=[("t-make", "建模"), ("t-warn", "已停更"), ("t-new", "新")],
        plain="把静态插画转成**网格可变形角色**的 FOSS 2D 动画工具，**直接对标 Live2D 的核心「网格/变形器」能力**，纯浏览器端跑。",
        analogy="它复刻的是 Live2D 最值钱的那部分 —— 「让一张平面画能被网格拉变形」。"
                "但请注意：**网格变形 ≠ Live2D**，它没有参数绑定、没有物理、没有口型 —— 那是另一半工作量。",
        warn="⚠️ **已停更**：`pushed_at` 2026-04-28 vs `updated_at` 2026-10-10（差 5.5 个月）。★504 只是历史热度。",
        ext=(60, "6.0/10", "思路适合低成本复刻，但不是活跃项目"),
        use=(35, "3.5/10", "停更，只能当参考实现读"),
        src="创建 2026-04-12 · 推送 2026-04-28 · 更新 2026-10-10（⚠️ 差 5.5 个月）· 504★ · MIT · JavaScript · 信源 [1334]",
    ),
    dict(
        nid="rpm39c11", name="ComfyUI-PSD-Layers —— 把 AI 分层结果存成可编辑 PSD（★4）",
        url="https://github.com/coeyes/ComfyUI-PSD-Layers",
        lang="JavaScript", stars="4",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="ComfyUI 节点：把分层分割结果**保存成可编辑的 PSD**、可逐层读取并还原 Photoshop 混合模式 —— 补上「AI 分层 → Live2D 可用素材」的最后一公里。",
        analogy="「单图 → 模型」链路上人人都在做分割，**但极少有人把输出做成 PSD**。而这个节点正好补在最缺的一环："
                "**分割模型给你 PNG，Live2D 要 PSD**。",
        warn="⚠️ ★4，很新（2026-08）；需要 ComfyUI 环境。",
        ext=(65, "6.5/10", "卡位精准，是链路缺口上的小齿轮"),
        use=(55, "5.5/10", "有 ComfyUI 就能直接试"),
        src="创建 2026-08-24 · 推送 2026-09-10 · 更新 2026-10-03 · 4★ · MIT · JavaScript · 信源 [1335]",
    ),
    # ---------- C. 桥 / 运行时 / 整合 ----------
    dict(
        nid="rpm39c12", name="VTubeStudioJS —— 用代码驱动 Live2D 的表情与动作（★68）",
        url="https://github.com/Hawkbat/VTubeStudioJS",
        lang="TypeScript", stars="68",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "已核实待试")],
        plain="VTube Studio API 的 **Node / 浏览器 JS 实现** —— 用代码驱动 Live2D 模型的表情、动作、参数。",
        analogy="想做「LLM 状态 → Live2D 表情」的桥，这是**最省事的 JS 侧通道**："
                "你不用自己接 Cubism SDK，只要往 VTube Studio 发消息。MIT，直接用。",
        ext=(70, "7.0/10", "成熟 API 封装，接表情/动作最省事"),
        use=(65, "6.5/10", "MIT + 稳定；前提是你用 VTube Studio 做宿主"),
        src="创建 2021-07-14 · 推送 2026-08-22 · 更新 2026-08-22 · 68★ · MIT · TypeScript · 信源 [1336]",
    ),
    dict(
        nid="rpm39c13", name="Motiv2D —— 同时吃 Spine2d 与 Live2D 的查看器（★45）",
        url="https://github.com/o0Nomar0o/Motiv2D",
        lang="JavaScript", stars="45",
        tags=[("t-mod", "模块化"), ("t-warn", "更新放缓"), ("t-new", "新")],
        plain="**同时支持 Spine2d 与 Live2D** 的查看器，纯 JS 实现（不依赖官方 SDK 播放层）。",
        analogy="双格式查看器的**组织方式**值得借鉴 —— 如果你的索引站要放模型预览，"
                "「一套壳、两个后端解析器」比写两套页面划算得多。",
        warn="⚠️ 约 3 个月无推送（`pushed_at` 2026-06-26 vs `updated_at` 2026-09-14）。",
        ext=(55, "5.5/10", "双格式抽象值得学"),
        use=(40, "4.0/10", "更新放缓，可读不宜依赖"),
        src="创建 2026-02-03 · 推送 2026-06-26 · 更新 2026-09-14 · 45★ · MIT · JavaScript · 信源 [1337]",
    ),
    dict(
        nid="rpm39c14", name="JunOS —— 自托管 AI 伴侣：Live2D + 持久记忆 + 关系动力学（★5）",
        url="https://github.com/efficiencyx/JunOS",
        lang="JavaScript", stars="5",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="自托管 AI 伴侣：带 **Live2D 动画、语音对话、持久记忆与关系动力学**，由本地 LLM 驱动，Web 应用形态。",
        analogy="关键词是 **「关系动力学」** —— 多数 AI 伴侣只记事实，它多记一层「你俩关系进展到哪了」。"
                "这种「状态不只是数据，还有关系」的设计，比堆功能更接近伴侣产品的本质。",
        warn="⚠️ ★5、新建（2026-08），Apache-2.0；架构成熟度未知。",
        ext=(65, "6.5/10", "「关系状态」这一层设计值得抄"),
        use=(40, "4.0/10", "太新，架构参考为主"),
        src="创建 2026-08-21 · 推送 2026-10-09 · 更新 2026-10-09 · 5★ · Apache-2.0 · JavaScript · 信源 [1338]",
    ),
    # ---------- D. AI 辅助制作 ----------
    dict(
        nid="rpm39c15", name="anime-segmentation —— 动漫抠图/分割的通用底座（★849）",
        url="https://github.com/SkyTNT/anime-segmentation",
        lang="Python", stars="849",
        tags=[("t-make", "建模"), ("t-warn", "已停更"), ("t-ok", "已核实待试")],
        plain="高精度**动漫角色抠图 / 分割**模型（去背景、出 alpha），是「单图 → 分层素材」链路里**最常被复用的底座**。",
        analogy="做「单图 → Live2D 模型」的人几乎都会经过它。它的定位是**链路第一环**："
                "先把角色从背景里切出来，后面才有分层和绑定。",
        warn="⚠️ **模型本身已停更**：`pushed_at` 2025-05-21 vs `updated_at` 2026-10-11（差约 17 个月，仅资产/README 更新）。"
             "好在 Apache-2.0 + 已成熟，本地可离线推理 —— 「停更」对推理模型不等于不能用。",
        ext=(50, "5.0/10", "链路第一环，但不再迭代"),
        use=(60, "6.0/10", "成熟可用，Apache-2.0，本机可离线跑"),
        src="创建 2022-08-14 · 推送 2025-05-21 · 更新 2026-10-11（⚠️ 差 17 个月）· 849★ · Apache-2.0 · Python · 信源 [1339]",
    ),
    dict(
        nid="rpm39c16", name="motion-mirror —— 本地优先的动作迁移（★127）",
        url="https://github.com/halli75/motion-mirror",
        lang="Python", stars="127",
        tags=[("t-make", "建模"), ("t-warn", "更新放缓"), ("t-new", "新")],
        plain="本地优先的**动作迁移**：把参考视频里的动作「搬」到任意角色图上，基于 Wan2.1-VACE，是托管动作控制工具的本地开源替代。",
        analogy="它与「Live2D 动作生成 / 表情差分」是同一个问题域：**怎么不做手工 K 帧就得到动作**。"
                "两条路不同 —— Live2D 走参数变形，它走视频生成。**可以并用来对照**。",
        warn="⚠️ 依赖 **Wan2.1-VACE**，对 16GB 内存的机器**显存要求未知，需实测**；不能默认它跑得动。",
        ext=(60, "6.0/10", "问题域对口，可作参数变形路线的对照"),
        use=(35, "3.5/10", "依赖重，本机可行性未验证"),
        src="创建 2026-04-13 · 推送 2026-07-22 · 更新 2026-10-08 · 127★ · MIT · Python · 信源 [1340]",
    ),
    dict(
        nid="rpm39c17", name="Live2DPet —— JS 栈的 AI 桌宠 + VOICEVOX（★86）",
        url="https://github.com/x380kkm/Live2DPet",
        lang="JavaScript", stars="86",
        tags=[("t-make", "建模"), ("t-warn", "更新放缓"), ("t-new", "新")],
        plain="AI 驱动的 Live2D 桌宠伴侣，集成 **VOICEVOX TTS**。",
        analogy="「Live2D 显示 + TTS + LLM」这个最小骨架，它给的是 **JS 栈版本**（对应 Python 栈是 Open-LLM-VTuber 那一支）。"
                "想抄骨架的话，挑与你目标语言一致的那份。",
        warn="⚠️ 约 3.5 个月无推送（`pushed_at` 2026-06-22 vs `updated_at` 2026-10-02）。",
        ext=(50, "5.0/10", "骨架清晰，但已放缓"),
        use=(40, "4.0/10", "可读骨架，别当依赖"),
        src="创建 2026-02-11 · 推送 2026-06-22 · 更新 2026-10-02 · 86★ · MIT · JavaScript · 信源 [1341]",
    ),
    # ---------- E. 官方一手（本辑最硬） ----------
    dict(
        nid="rpm39c18", name="官方根因：5.3「保存失败」不是文件大，是参数数「相乘」爆炸",
        url="https://creatorsforum.live2d.com/t/3979",
        lang="官方论坛", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "已核实待试"), ("t-new", "新")],
        plain="用户报「470MB 的模型保存时一直提示『输出失败』」。官方（`enoko_staff`，2026-10-09）给出一条**制作小白最该知道的结论**："
              "**文件 470MB 不是直接原因**；真正原因是**该部件挂在太多参数上，keyform 的处理量按参数数「相乘」增长**，"
              "超过可保存范围。解法：把这类表情参数**改用 blend shape**（走「加法」而非「乘法」），或把 key 打在**包住整个嘴的 deformer** 上、"
              "而不是直接打在唇的 ArtMesh 上。",
        analogy="这条把一个很常见的误判堵死了：**模型越做越存不动，第一反应是「文件太大了，删点素材吧」** —— 官方说不是。"
                "真正会爆炸的是**参数在末端网格上的组合数**。这也解释了为什么「把 key 打在聚合层的 deformer 上」比打在末端 ArtMesh 上更省。",
        warn="⚠️ 官方也给了一条**应急处方**（本项目的具体场景）：「先把上唇上新增的 key 删掉」。别把应急当通用解。",
        ext=(70, "7.0/10", "官方一手根因，直接改变建模手法"),
        use=(85, "8.5/10", "**本辑对「做模型的人」最有用的一条**，改法明确、成本零"),
        src="官方论坛 /t/3979 · 用户报障 2026-09-22 · 官方根因回复 2026-10-09 · 原始 JSON 已读 · 信源 [1342]",
    ),
    dict(
        nid="rpm39c19", name="Unity 6.6 + URP3D：Scene 能渲染、运行时不渲染（官方已复现）",
        url="https://creatorsforum.live2d.com/t/3986",
        lang="官方论坛", stars="—",
        tags=[("t-mod", "模块化"), ("t-warn", "新"), ("t-new", "新")],
        plain="用户报告：Unity **6.6 + Universal 3D + Cubism SDK for Unity R5** 下，**Scene 视图能渲染、运行时不渲染**。"
              "官方（2026-10-02）确认**:在支持环境中复现了该现象**，正在调查。帖内还给了**前置坑**："
              "Unity 6.6 上 `GetInstanceID()` 过时会导致编译错误，需打 **CubismUnityComponents PR #96** 补丁。",
        analogy="这条是「**为什么 2D 路线（如 Ren'Py）更稳**」的旁证：3D 引擎的版本联调面越宽，"
                "「引擎升级 × SDK 版本 × 渲染管线」的组合就越容易出**只在运行时暴露**的问题。",
        warn="⚠️ 官方只认领调查、**未给修复时间**。**未修前别把 Unity 6.6 + URP3D 上生产**。",
        ext=(55, "5.5/10", "Unity 集成方的确定性风险，非可拓展性"),
        use=(50, "5.0/10", "对 Unity 用户是必须知道的坑；对 2D 路线是旁证"),
        src="官方论坛 /t/3986 · 报障 2026-09-30 · 官方认领 2026-10-02 · 原始 JSON 已读 · 信源 [1343]",
    ),
    dict(
        nid="rpm39c20", name="外部联携 API 做不到的 4 件事（用户向官方点名）",
        url="https://creatorsforum.live2d.com/t/3989",
        lang="官方论坛", stars="—",
        tags=[("t-mod", "模块化"), ("t-warn", "新"), ("t-new", "新")],
        plain="用户（2026-10-05）向官方要功能：现在的 External API **能**加参数 key、改对象属性与层级，"
              "但**不能**① 复制既有对象 ② 复制含 keyform 的对象 ③ 把顶点/形状按指定轴左右镜像 ④ 在指定 key 之间复制形状 ——"
              "所以「左右眼/左右部件镜像」这类工程**目前无法纯靠 API 完成**。",
        analogy="上一辑我们记了「第三方在 Cubism 的 External API（22033 端口）外围建了一整簇工具」。"
                "这条是**那条路的能力边界**：边界之内（加参数、改层级）已能自动化，**边界之外（镜像、复制）还得人点**。"
                "知道边界在哪，比知道 API 存在更有用。",
        ext=(45, "4.5/10", "官方 API 的能力边界，自动化规划必须知道"),
        use=(65, "6.5/10", "避免在「镜像复制」上白费功夫"),
        src="官方论坛 /t/3989 · 2026-10-05 · 本轮无官方回复 · 原始 JSON 已读 · 信源 [1344]",
    ),
    dict(
        nid="rpm39c21", name="图集反转复制后显示 NoArtMesh —— 官方：这是规格，不是 bug",
        url="https://creatorsforum.live2d.com/t/3975",
        lang="官方论坛", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "已核实待试"), ("t-new", "新")],
        plain="做完 mesh、打参数前先自动排版了纹理图集；之后「复制左眼 → 左右反转 → 粘到右眼」，"
              "结果图集里**所有反转复制来的右眼部件都显示 `NoArtMesh`**。官方（2026-09-24）定性："
              "**这不是不具合，是 Cubism Editor 规格内的行为**，数据没坏。恢复法：在部件/变形器面板里**右键那个源图（左眼）→「设为所选 ArtMesh 的输入图像」**。"
              "官方（10-01）补充：建模画面显示正常的话，**可以照常继续做**。",
        analogy="做「左右镜像部件」的人一定会撞上这个。它的价值是两句话：**① 症状不是 bug，别删工程重来；② 恢复只要三步右键**。",
        ext=(35, "3.5/10", "单一操作问题，非可拓展性"),
        use=(80, "8.0/10", "**做镜像部件时的官方标准操作**，省一次重做"),
        src="官方论坛 /t/3975 · 报障 2026-09-14 · 官方定性 2026-09-24 / 2026-10-01 · 原始 JSON 已读 · 信源 [1345]",
    ),
    # ---------- F. DSH / Agent 生态 ----------
    dict(
        nid="rpm39c22", name="MemOS —— 自演化记忆 OS（★11802）",
        url="https://github.com/MemTensor/MemOS",
        lang="TypeScript", stars="11802",
        tags=[("t-mod", "模块化"), ("t-ok", "每日更新"), ("t-new", "新")],
        plain="自演化记忆操作系统：**超持久记忆 + 混合检索 + 跨任务技能复用**，宣称省 35.24% token，支持 DSH。",
        analogy="这是「**上下文与记忆管理**」方向本辑最完整的一个。它要解决的问题正是我们自己也有的："
                "**记忆只增不 merge，越滚越贵**。它的「混合检索 + 技能复用」是可借鉴的两条机制。",
        warn="⚠️ 单方宣称的 35.24% 数字**未独立复现**，按「宣称」读。",
        ext=(80, "8.0/10", "记忆/上下文方向最完整，Apache-2.0 活跃"),
        use=(60, "6.0/10", "架构可借鉴；宣称数字待自测"),
        src="创建 2025-07-06 · 推送 2026-10-10 · 更新 2026-10-11 · 11802★ · Apache-2.0 · TypeScript · 信源 [1346]",
    ),
    dict(
        nid="rpm39c23", name="petdex —— 面向各家编码 agent 的动画桌宠公共画廊（★4226）",
        url="https://github.com/crafter-station/petdex",
        lang="TypeScript", stars="4226",
        tags=[("t-make", "建模"), ("t-ok", "每日更新"), ("t-new", "新")],
        plain="面向 Codex / Claude Code / **DSH** / Hermes / OpenCode / Gemini CLI 等一堆 agent 的**动画桌宠公共画廊**。",
        analogy="它把「AI 工具」和「桌宠」两条线**直接接上了** —— 而且它的形态是**画廊**（资源 + 分发），"
                "这恰好是你自己在做的事：**用一个站把分散的供给组织起来**。看它怎么分类与分发，比看它有几只宠物有用。",
        ext=(70, "7.0/10", "「桌宠 + agent」交叉点的资源组织方式值得学"),
        use=(55, "5.5/10", "资源型项目，MIT"),
        src="创建 2026-05-02 · 推送 2026-10-10 · 更新 2026-10-11 · 4226★ · MIT · TypeScript · 信源 [1347]",
    ),
    dict(
        nid="rpm39c24", name="awesome-dsh-plugin —— 生态里唯一做「去伪复核」的清单（★402）",
        url="https://github.com/bruc3van/awesome-dsh-plugin",
        lang="JavaScript", stars="402",
        tags=[("t-mod", "模块化"), ("t-ok", "每日更新"), ("t-new", "新")],
        plain="DSH 插件精选列表：**每天自动抓取 `dsh-plugin` 项目并逐个复核**，剔除蹭标签的项目，按场景分类 + 热度排行。",
        analogy="本辑 DSH 侧**最该先看的一条**。原因不是它内容多好，而是 —— DSH 插件生态里 **star 普遍异常高（数万级）且同题材聚合/市场类重复项目极多**，"
                "**唯 star 会把你带沟里**。它是唯一明确把「去伪」写进流程的。"
                "**找插件从这里入口，别从搜索入口。**",
        warn="⚠️ ★402，但它的价值恰恰是**替你在一个 star 失真的生态里做减法**。",
        ext=(60, "6.0/10", "去伪流程本身就是稀缺点"),
        use=(70, "7.0/10", "找 DSH 插件的正确入口，MIT、每日更新"),
        src="创建 2026-08-13 · 推送 2026-10-11 · 更新 2026-10-11 · 402★ · MIT · JavaScript · 信源 [1348]",
    ),
]

FOOTNOTES = [
    (1325, "https://github.com/Project-N-E-K-O/N.E.K.O", "Project-N-E-K-O/N.E.K.O",
     "3044★ · Apache-2.0 · Python · 创建 2025-06-29 · 推送/更新 2026-10-11 · GitHub REST API 实测"),
    (1326, "https://github.com/jofizcd/Soul-of-Waifu", "jofizcd/Soul-of-Waifu",
     "1386★ · GPL-3.0 · Python · 创建 2023-09-02 · 推送 2026-08-28 · 更新 2026-10-11 · GitHub REST API 实测"),
    (1327, "https://github.com/marine841023/duty-on", "marine841023/duty-on",
     "3★ · MIT · Rust · 创建 2026-08-03 · 推送 2026-10-09 · 更新 2026-08-23（⚠️ updated 早于 pushed，反向异常）· GitHub REST API 实测"),
    (1328, "https://github.com/Lsc-91-69/dsh-live2d-avatar", "Lsc-91-69/dsh-live2d-avatar",
     "1★ · MIT · JavaScript · 创建/推送/更新 2026-10-07 · GitHub REST API 实测"),
    (1329, "https://github.com/1704919/WuziDesktopPet", "1704919/WuziDesktopPet",
     "2★ · MIT · GDScript · 创建 2026-10-10 · 推送/更新 2026-10-11 · GitHub REST API 实测"),
    (1330, "https://github.com/rig-c/core", "rig-c/core",
     "12★ · 许可未声明 · TypeScript · 创建 2026-08-22 · 推送/更新 2026-10-11 · GitHub REST API 实测"),
    (1331, "https://github.com/rig-c/parts", "rig-c/parts",
     "2★ · MIT · TypeScript · 创建 2026-09-27 · 推送/更新 2026-10-11 · GitHub REST API 实测"),
    (1332, "https://github.com/Eatgrapes/Mocari", "Eatgrapes/Mocari",
     "47★ · MIT · Rust · 创建 2026-05-31 · 推送 2026-07-13 · 更新 2026-10-10（⚠️ 差 3 个月）· GitHub REST API 实测"),
    (1333, "https://github.com/UlyssesWu/D2Evil", "UlyssesWu/D2Evil",
     "139★ · 许可未声明 · C# · 创建 2019-09-21 · 推送 2026-06-07 · 更新 2026-09-24 · GitHub REST API 实测"),
    (1334, "https://github.com/MangoLion/stretchystudio", "MangoLion/stretchystudio",
     "504★ · MIT · JavaScript · 创建 2026-04-12 · 推送 2026-04-28 · 更新 2026-10-10（⚠️ 差 5.5 个月）· GitHub REST API 实测"),
    (1335, "https://github.com/coeyes/ComfyUI-PSD-Layers", "coeyes/ComfyUI-PSD-Layers",
     "4★ · MIT · JavaScript · 创建 2026-08-24 · 推送 2026-09-10 · 更新 2026-10-03 · GitHub REST API 实测"),
    (1336, "https://github.com/Hawkbat/VTubeStudioJS", "Hawkbat/VTubeStudioJS",
     "68★ · MIT · TypeScript · 创建 2021-07-14 · 推送/更新 2026-08-22 · GitHub REST API 实测"),
    (1337, "https://github.com/o0Nomar0o/Motiv2D", "o0Nomar0o/Motiv2D",
     "45★ · MIT · JavaScript · 创建 2026-02-03 · 推送 2026-06-26 · 更新 2026-09-14 · GitHub REST API 实测"),
    (1338, "https://github.com/efficiencyx/JunOS", "efficiencyx/JunOS",
     "5★ · Apache-2.0 · JavaScript · 创建 2026-08-21 · 推送/更新 2026-10-09 · GitHub REST API 实测"),
    (1339, "https://github.com/SkyTNT/anime-segmentation", "SkyTNT/anime-segmentation",
     "849★ · Apache-2.0 · Python · 创建 2022-08-14 · 推送 2025-05-21 · 更新 2026-10-11（⚠️ 差 17 个月）· GitHub REST API 实测"),
    (1340, "https://github.com/halli75/motion-mirror", "halli75/motion-mirror",
     "127★ · MIT · Python · 创建 2026-04-13 · 推送 2026-07-22 · 更新 2026-10-08 · GitHub REST API 实测"),
    (1341, "https://github.com/x380kkm/Live2DPet", "x380kkm/Live2DPet",
     "86★ · MIT · JavaScript · 创建 2026-02-11 · 推送 2026-06-22 · 更新 2026-10-02 · GitHub REST API 实测"),
    (1342, "https://creatorsforum.live2d.com/t/3979", "creatorsforum /t/3979（5.3 保存失败根因）",
     "官方论坛一手 · 用户报障 2026-09-22 · 官方 enoko_staff 根因回复 2026-10-09 · 原始 JSON 已读 · **本辑对建模最有用**"),
    (1343, "https://creatorsforum.live2d.com/t/3986", "creatorsforum /t/3986（Unity 6.6+URP3D 运行时黑屏）",
     "官方论坛一手 · 报障 2026-09-30 · 官方 ono-at-live2d-com 复现并认领 2026-10-02 · 附 CubismUnityComponents PR #96 前置补丁 · 原始 JSON 已读"),
    (1344, "https://creatorsforum.live2d.com/t/3989", "creatorsforum /t/3989（外部联携 API 能力边界）",
     "官方论坛一手 · 用户要望 2026-10-05 · 本轮无官方回复 · 原始 JSON 已读"),
    (1345, "https://creatorsforum.live2d.com/t/3975", "creatorsforum /t/3975（图集反转 NoArtMesh 属规格）",
     "官方论坛一手 · 报障 2026-09-14 · 官方定性 2026-09-24 + 补充 2026-10-01 · 原始 JSON 已读"),
    (1346, "https://github.com/MemTensor/MemOS", "MemTensor/MemOS",
     "11802★ · Apache-2.0 · TypeScript · 创建 2025-07-06 · 推送 2026-10-10 · 更新 2026-10-11 · GitHub REST API 实测 · 35.24% 为单方宣称"),
    (1347, "https://github.com/crafter-station/petdex", "crafter-station/petdex",
     "4226★ · MIT · TypeScript · 创建 2026-05-02 · 推送 2026-10-10 · 更新 2026-10-11 · GitHub REST API 实测"),
    (1348, "https://github.com/bruc3van/awesome-dsh-plugin", "bruc3van/awesome-dsh-plugin",
     "402★ · MIT · JavaScript · 创建 2026-08-13 · 推送/更新 2026-10-11 · GitHub REST API 实测"),
    # ---- 非卡片信源（本辑引用，不进卡片） ----
    (1349, "https://www.nekomaido.com/blog/live2d-psd-preparation", "喵僕《Live2D 拆分準備與 PSD 圖層整理》",
     "cn 路 · **做模型前必须先定的图层规范**：Cubism 5.3+ 支持一般图层/混合模式/剪贴蒙版（需在 Live2D 内重新剪贴 ID）；"
     "不支持 蒙版/图层样式/调整图层/智能对象/文字图层/向量图层（须先在 PS 转成一般图层）；**图层避免重名**（导入不报错、替换时报错）"),
    (1350, "https://forum.gamer.com.tw/Co.php?bsn=60608&sn=40198", "巴哈姆特《Live2D 教學、學習資源整理》",
     "cn 路 · 中文圈结构最完整的一份「指路 + 资源」楼（GP 209，持续更新）：官方源 / 可回查的建模大佬名单（其模型展示片常带工程文件展示）/ 拆圖專區 / nizima 可网页浏览模型参数"),
    (1351, "https://zhangwenbao.com/claude-code-tips.html", "保哥《Claude Code 高效开发的 20 个实战技巧》",
     "cn 路 AI 开发 · 硬机制：`/clear` `/compact` `/context`；`git worktree` 多会话并行；**「修正两次以上还不对 = 上下文已被失败方案污染」→ 清空重开**；"
     "**「如果 AI 能看到自己代码的运行结果，代码质量能提升 2~3 倍」**"),
    (1352, "https://juejin.cn/post/7610305771625005107", "掘金《2026 年 AI 辅助开发踩坑复盘与 SOP》",
     "cn 路 AI 开发 · **长文本诅咒有量化**：把团队 1.2 万字 Java 规约整体注入 → Token 指数上升 / 上下文丢失 / **智力降级**（注意力被驼峰命名与注释格式分散）；"
     "破局 = 解耦成**每个微规则包 ≤1000 字**、按需加载"),
    (1353, "https://vocus.cc/article/69be1711fd89780001b84296", "vocus《設計 CLAUDE.md 增加 Claude Code 生產力》",
     "cn 路 AI 开发 · 分层写法：全局 CLAUDE.md（只写工作风格）/ 项目条件式规则 / 项目 CLAUDE.md；**「CLAUDE.md 超过 200 行 → 权重变平，AI 更容易忽略关键指令」**（与上方 1.2 万字互为实证）；"
     "context 压力下的护栏：「做不到完整品质就诚实中止，不要硬凑」"),
    (1354, "https://store.steampowered.com/app/4753800/", "Steam · RPG Developer Bakin Live2D Toolkit（DLC）",
     "official 路 · 2026-06-17 上架 · ¥77 · SmileBoom 官方 DLC：把 Cubism 做的 Live2D 模型导入 Bakin 做的游戏。"
     "**Steam 源本轮从 HTTP 000 翻转为 200（上轮判退役，本轮回滚）**；同屏另两款：Cursor for Live2D ¥42（桌面跟随播放器）/ Figryne Cast Studio Live2D Addon ¥77（单摄像头实时面捕工作室）"),
]


def b(s):
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
        if c["url"] and "github.com/" in c["url"]:
            slug = c["url"].split("github.com/")[-1].lower()
            if slug in src.lower():
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

    desc = ('第三十四辑三路调研（gh 路 34 条正文 + 26 行边缘登记 / cn 路 22 条 / official 路 25 条），本版取 24 项，'
            '主题 **「身体」侧供给第一次压过「格式」侧 + 官方一手给出了「模型越做越存不动」的根因**。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/&lt;r&gt;` 逐条实测（主 agent 已复验全部 20 个候选仓库，零出入）。'
            '<strong>本辑主线：① 桌宠「身体」侧本辑最密集 —— N.E.K.O（★3044 会主动找你玩的 AI 猫娘）/ Soul-of-Waifu（★1386 Live2D+VRM）/ '
            'duty-on（Rust，**监听你的 AI 编码 agent 状态**）/ dsh-live2d-avatar（DSH 插件）/ WuziDesktopPet（Godot 4.7）；'
            '② 绕开 Cubism 的绑定线出现「可验证流水线」—— rig-c/core 把 rig spec 编译成 Spine 4.3，先做命名断言 + round-trip 校验、'
            '只输出通过校验的结果，并以 agent skill 分发；③ 官方论坛 4 条一手正文（本辑最硬）：'
            '**5.3「保存失败」的根因不是文件大（470MB），是参数数「相乘」爆炸 → 改用 blend shape（加法）替代普通 key**；'
            'Unity 6.6 + URP3D 下「Scene 能渲染、运行时不渲染」官方已复现；外部联携 API 做不到的 4 件事（复制对象 / 复制 keyform / 左右镜像）；'
            '图集反转复制后 NoArtMesh 属规格并附官方恢复法；'
            '④ AI 开发侧：DSH 生态继续成形（MemOS ★11802 / petdex ★4226 / awesome-dsh-plugin ★402 —— 生态里唯一明确做去伪复核的清单）。'
            '⑤ 本版起 src 行**固定同时打印 pushed_at 与 updated_at**，差 &gt;30 天标「⚠️ 假活」、反向（updated 更旧）也标 —— 本辑抓到 1 处反向异常（duty-on）。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm39g">',
             '      <div class="group-title" data-page-node-id="rpm39gt">🆕 第三十九版增补 · 「身体」侧供给压过「格式」侧 + 官方一手：「存不动」的根因是参数相乘（24 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm39gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm39r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm39ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]

    for o, n in zip(HEAD_OLD, HEAD_NEW):
        if src.count(o) != 1:
            print("二次校验失败：页头锚点 %s 现在出现 %d 次" % (o[:40], src.count(o)))
            return 1
        src = src.replace(o, n)

    open(HTML, "w", encoding="utf-8").write(src)
    print("✅ 已插入 %s：%d 张卡 + %d 条脚注（[%d]-[%d]）"
          % (MARKER, len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE, FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    print("   页头：1325 → 1355 项；卡片 1314 → %d" % (1314 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
