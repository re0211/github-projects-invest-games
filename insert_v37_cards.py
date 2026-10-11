# -*- coding: utf-8 -*-
"""第三十七版增补：把第三十二辑「有人正面拆了 Cubism Core 那堵墙」的 22 个条目登记进 index.html。

本辑候选：gh 路 30 条（27 条正文 + 5 条边缘登记）、cn 路 16 条、official 路 21 条。
与 `index.html`（1279 项）及全部历史存档机器比对，本版 22 条命中 **0**。

**本辑主线：前六辑反复在同一个地方卡住 —— 「不买 Cubism Editor 就没有 moc3 渲染器」。这一辑出现了正面拆墙的人。**

1. **`AyagamiDev/ayagami`（★351 · Rust · Apache-2.0）**——索引里第一条**公开、活跃、声称已实现 MOC3 加载与渲染**
   的开源库（wgpu 后端，支持到 SDK 5.0 的 MOC3 特性），并划了明确的法律姿态：
   **只用黑盒逆向，从不反汇编/反编译专有软件**（写进了 contributor policy）。
   配套 `ayagami-gd`（★39，Godot 绑定）与 `manosaba-live2d`（同一 Godot 工程里把
   「官方 gd_cubism + Cubism Native 5-r.5」与「Ayagami（Rust）」**并行跑**的对照实验台）。
2. **Cubism Editor 的 External API（本机 22033 端口）被第三方围建出一整簇工具** ——
   `Turboism`（Windows 优先的插件框架，支持表列出 **5.2.03 / 5.3.02 / 5.3.03 各配「精确版本适配器」**）、
   `cubism-editor-computer-use`（**官方 5.4 alpha 编辑 API 样例 + 异步 Python 客户端**）、
   `NanaBetterCubism`（对话驱动，编辑统一走 **preview → 确认 → 后端事务 → 回读验证**）、
   `cubihub`（多版本 Cubism 的工程管理器 + Mesh Preset 读写 + 日志→摘要）。
3. **「单图 → 可用模型」多了一条技术栈**：`illust2psd`（★8）走 **ISNet 去背景 + SAM2 语义分割 + OpenCV inpaint**，
   直接产出**符合 Cubism 图层命名规范的分层 PSD**（含 `layer_taxonomy.yaml`），
   与已收录的 See-through（Depth 拆层）是两条不同的路。
4. **桌宠的表情信号源换了**：`Agent-desktop-pet`（CodexPet 2.0）把 **12 个编码 Agent 的实时状态**映射成 9 种表情，
   **只读本地会话记录、不联网**；`AAAAGENT`（★143）则公开了角色的**分层 PSD 设计稿**（但非商用）。
5. **官方口径两处被推翻 + 一处退役可回滚**（official 路，记在 `csdn-social-summary.md`）：
   ① **Cubism 5.4 SDK alpha 确实存在**（上一辑「5.4 无配套 SDK」不成立）；
   ② **npm `easy-live2d` 真实存在且已 1.0.0**（上一辑「包名不存在、勿再追」有误）；
   ③ **`creatorsforum.live2d.com` 本轮 HTTP 200**（上一辑记 403）→ **退役名单可回滚**。

**inbox 顺延**：`/skill-doctor`（连续第十一轮）；`moeru-ai/airi` 已实测闭环（见 `csdn-social-summary.md`）。

数据来源：2026-10-11 GitHub REST API 实测（`gh api repos/<r>` 逐条，主 agent 已复验全部 22 条）。
幂等：已存在本版标记则跳过。
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1278"'
FIRST_NEW_FOOTNOTE = 1279
MARKER = "第三十七版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十六版增补 2026-10-11',
    '共 1279 个项目',
    '第三十四版增补 18 项 + 第三十五版增补 24 项 + 第三十六版增补 22 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十七版增补 2026-10-11',
    '共 1301 个项目',
    '第三十四版增补 18 项 + 第三十五版增补 24 项 + 第三十六版增补 22 项 + 第三十七版增补 22 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm37c1", name="ayagami（彩紙）—— 第一条公开的「黑盒逆向 moc3」开源渲染器",
        url="https://github.com/AyagamiDev/ayagami",
        lang="Rust", stars="351",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="一个**从零黑盒逆向、完全开源**的 2D 木偶加载与渲染库 —— **直接读 Live2D 的 `.moc3`**，"
              "渲染用 wgpu（Vulkan / Metal / DX / OpenGL / WebGL / WebGPU 全后端）。"
              "作者宣称：不用付版税、无需任何人许可，商用、内置模型、加载用户模型的软件都能用。",
        analogy="前六辑一直卡在同一堵墙前：想不买 Cubism Editor 就把 moc3 显示出来，**没有合法的开源渲染器**。"
                "要么用 Inochi2D 那套换格式，要么只做 JSON 解析不碰网格。ayagami 是第一个正面拆墙的 —— "
                "而且它拆的方式很关键：**只用黑盒逆向（看输入输出反推格式），从不反汇编/反编译专有软件**，"
                "把「格式兼容」和「破解软件」两件事在法律上分开。",
        warn="⚠️ 作者自述 **API 很不稳定、还没有文档**，crates.io 尚未发版；"
             "**表达式 / pose / 动作文件仍是 TODO**（目前只有加载 + 参数驱动 + 物理）→ 做得成挂件，做不成完整 VTuber。"
             "「黑盒逆向合法」是**作者的法律主张**，商用前请自行复核（各地对专有格式逆向的认定不同）；"
             "许可双标（README 写 MIT + Apache-2.0，GitHub 只识别出 Apache-2.0）→ **以仓库内 LICENSE 原文为准**。",
        ext=(88, "8.8/10", "开源 + 多后端 + 活跃（3 个月涨到 ★351），是「合法读 moc3」这条线的天花板候选"),
        use=(70, "7.0/10", "现在别押：API 不稳、无文档、动作未支持 · 但**每辑应复查一次进度**"),
        src="创建 2026-07-11 · 推送 2026-09-14 · 351★ · Apache-2.0 · Rust · 信源 [1279]",
    ),
    dict(
        nid="rpm37c2", name="ayagami-gd —— 把「非官方 moc3 渲染器」接进 Godot",
        url="https://github.com/AyagamiDev/ayagami-gd",
        lang="Rust", stars="39",
        tags=[("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="Ayagami 的 **Godot 绑定** —— 把上面那个 moc3 渲染器接进 Godot 引擎，同一组织维护、更新同步。",
        analogy="Godot 侧原本只有一条路：`gd_cubism` 走**官方 Cubism Native SDK**（要下 SDK、认许可）。"
                "ayagami-gd 是「**Godot + 非官方 moc3 渲染器**」这条新组合 —— 不装官方 SDK 也能在 Godot 里放 Live2D。",
        warn="⚠️ 依赖母项目 → 母项目 API 不稳它也稳不了；且需 **Godot 4.7**（而 gd_cubism 的二进制仍 target 4.3 ABI，"
             "两者版本要求不同，别混着装）。",
        ext=(72, "7.2/10", "多一个引擎出口，但完全受母项目成熟度拖累"),
        use=(58, "5.8/10", "不用 Godot 就不采用 · 若要，先等母项目出稳定版"),
        src="推送 2026-09-15 · 39★ · MIT · Rust · 信源 [1280]",
    ),
    dict(
        nid="rpm37c3", name="manosaba-live2d —— 官方路线 vs 开源路线的「对照实验台」",
        url="https://github.com/pakholeung37/manosaba-live2d",
        lang="C++", stars="0",
        tags=[("t-mod", "模块化"), ("t-warn", "注意")],
        plain="一份 Godot 4 的端到端 Live2D 对比 demo —— **同一个模型、两条运行时并行跑**："
              "一条走 `gd_cubism v0.9.1 + Cubism Native 5-r.5`（官方），另一条走 **Ayagami（Rust 开源）**。",
        analogy="想知道「开源那套到底行不行」，看文档没用 —— 要有人把两条路**放在同一个工程里现场比**。"
                "这个仓库就是那台实验台，而且它顺带暴露了两个硬事实："
                "gd_cubism 的二进制仍 target **Godot 4.3 ABI**，而内置的 Ayagami 扩展要 **Godot 4.7**。",
        warn="⚠️ ★0、无 license、单人、路径写死 macOS（README 里全是 `/Applications/...`）；只是 demo，不是产品。",
        ext=(45, "4.5/10", "本身没有工程价值，价值全在「可比」"),
        use=(60, "6.0/10", "不直接采用 · 但它是「开源替代成熟了没有」最快的一手信号源"),
        src="推送 2026-09-16 · 0★ · 无许可证 · C++ · 信源 [1281]",
    ),
    dict(
        nid="rpm37c4", name="inox2d —— Inochi2D 的 Rust 重写版运行时",
        url="https://github.com/Inochi2D/inox2d",
        lang="Rust", stars="298",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="Inochi2D 的**原生 Rust 重写版**运行时 —— 不走 D 语言那套依赖，把傀儡（puppet）渲染带进 Rust 生态，"
              "附 OpenGL 与 WebGL 两个可跑示例。",
        analogy="Inochi2D 本体是 **D 语言**（索引已收 ★1811 的 SDK 与它的编辑器），D 的工具链对普通人是个门槛。"
                "inox2d 等于把同一个渲染能力**翻译成了大众语言**（Rust），顺带让 Web 端也有了一条不依赖 Cubism Core 的路。",
        warn="⚠️ 许可显示 **NOASSERTION**（GitHub 没识别出标准 SPDX）→ 商用前必须去仓库根读 LICENSE 原文。",
        ext=(78, "7.8/10", "同一个格式多语言出口，Web 端尤其有想象空间"),
        use=(55, "5.5/10", "不写 Rust 就用不上 · 但它是「Inochi2D 阵营在补运行时」的明确信号"),
        src="推送 2026-09-23 · 298★ · 许可证不明 · Rust · 信源 [1282]",
    ),
    dict(
        nid="rpm37c5", name="inochi-viewer —— Inochi2D 官方的「最小查看器」",
        url="https://github.com/Inochi2D/inochi-viewer",
        lang="D", stars="47",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="Inochi2D 官方出的**最小傀儡查看器** —— 只干一件事：打开傀儡文件看长什么样，不建模、不改文件。",
        analogy="前几辑把 Inochi2D 工具链补成了「SDK 本体 + 编辑器」，但**少了「查看器」这一环** —— "
                "等于工具箱里有车床和扳手，却没有一把尺子。评估一套不熟的工具时，"
                "「能不能先看成品」往往决定要不要继续投入。",
        warn="⚠️ D 语言 GUI 程序，Windows 上要现成二进制才好用；不碰 D 工具链的人价值有限。",
        ext=(40, "4.0/10", "功能单一但位置关键（工具链闭环）"),
        use=(42, "4.2/10", "只为让 Inochi2D 那条线的索引闭环"),
        src="推送 2026-09-15 · 47★ · BSD-2-Clause · D · 信源 [1283]",
    ),
    dict(
        nid="rpm37c6", name="inochi2d-toolkit —— 用 CLI + MCP 操作「只有 GUI」的格式",
        url="https://github.com/yanjingzhaisun/inochi2d-toolkit",
        lang="Python", stars="0",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="给 Inochi2D 写的**命令行 + MCP 服务** —— 在「只有 GUI 编辑器」的傀儡格式上做**文件级**读写、"
              "结构校验、往返自检（TRNSRTS 容器 I/O）。",
        analogy="上一辑刚补了针对 **Cubism Editor** 的 MCP，这里是**同一思路换到 Inochi2D 侧**。"
                "关键差别在「文件级」而不是「模拟点击 UI」：前者稳定可测，后者一改版就碎。"
                "这条通用做法值得记 —— **GUI-only 的创作工具，可以用 CLI + MCP 在文件层绕过界面**，把「人点」变成「脚本改」。",
        warn="⚠️ ★0、单人、9 月刚建，API 会变；别写进正式流水线。",
        ext=(70, "7.0/10", "思路可迁移到任何 GUI-only 的美术格式"),
        use=(48, "4.8/10", "不玩 Inochi2D 就不直接用，抄思路"),
        src="推送 2026-09-24 · 0★ · MIT · Python · 信源 [1284]",
    ),
    dict(
        nid="rpm37c7", name="inochi2d-autorig-claude —— 那句「Cubism 根本不能自动绑骨」",
        url="https://github.com/henceketh/inochi2d-autorig-claude",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="用 Claude 给 **Inochi2D** 做自动绑骨的项目 —— 并在 README 里明确划死一条边界："
              "**Cubism 根本不能被全自动绑骨**（原文：`This rigs Inochi2D, not Live2D Cubism — Cubism cannot be autorigged at all.`）。",
        analogy="它的价值不在代码，**在那句断言**。索引里已有一堆「单图→模型全自动」的乐观项目，"
                "这是第一条公开把话说明白的：「哪些能自动、哪些不能」是**结构性硬限，不是工程量问题**。"
                "作者还给了折中方案：对 Cubism 只产出「绑骨配方」（图层改名、参数表、变形器规划、keyform 清单）交给人执行 —— "
                "**AI 提议、人裁决**，正好对上房规 #45。",
        warn="⚠️ 无 license；纯个人观点项目，**那句断言需自己复核，勿当权威结论引用**。",
        ext=(65, "6.5/10", "认知价值 > 代码价值：能省掉大量「拿 AI 硬刚 Cubism 绑骨」的试错"),
        use=(62, "6.2/10", "不采用其脚本 · 但把那条边界抄进认知"),
        src="推送 2026-10-05 · 0★ · 无许可证 · Python · 信源 [1285]",
    ),
    dict(
        nid="rpm37c8", name="ayatsuri_2d（操り2D）—— 又一个宣称「直接吃 moc3 v3–v6」的 Rust 栈",
        url="https://github.com/Yoru-KenomoVT/ayatsuri_2d",
        lang="Rust", stars="2",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "注意")],
        plain="从零写的开源替代栈 —— Rust 实现 2D 傀儡实时变形 + 绑骨编辑器，宣称端到端支持 **moc3 v3 到 v6**，"
              "自带 C ABI 让 Unity / UE / Godot / Python / JS 都能嵌入，自创 `.aom`（Ayatsuri Open Model）作保存格式。",
        analogy="索引里敢碰 moc3 兼容层的只有两家：一个是 ★351 的 ayagami（已经跑起来），"
                "一个是它（★2，README 自带徽章写 `moc3 v3 to v6`）。**两家都盯同一堵墙** —— "
                "这说明「moc3 兼容层」已经成了开源阵营公认的必争点，而不是某一个人的怪念头。",
        warn="⚠️ 「支持 moc3 v3–v6」是**作者单方宣称、无第三方验证**；README 自标 status = Early；"
             "★2、GPL-3.0（有传染性）；项目名/品牌疑为新号，无历史信誉。",
        ext=(58, "5.8/10", "方向对但太早，且宣称未验证"),
        use=(35, "3.5/10", "现在不采用 · 只登记「有人在做」这个事实"),
        src="推送 2026-09-13 · 2★ · GPL-3.0 · Rust · 信源 [1286]",
    ),
    dict(
        nid="rpm37c9", name="illust2psd —— 单张立绘 → 可直接导入 Cubism 的分层 PSD",
        url="https://github.com/CVIndomitable/illust2psd",
        lang="Python", stars="8",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "注意")],
        plain="**单张角色立绘 → 多图层 PSD**：自动去背景（ISNet）+ 语义分割（SAM2）+ 面部精细拆分 + "
              "遮挡区修复（OpenCV inpaint），输出**符合 Cubism 图层命名规范**的 RGB 8-bit PSD，并带 MCP server 可被 agent 调用。",
        analogy="「单图→模型」此前全靠 **See-through** 那一套（按深度拆层）。illust2psd 走的是**另一条技术栈**："
                "**先语义分割、再修遮挡**，而且终点不是「拆好的图」而是**Cubism 能直接吃的分层工程**。"
                "它还带一张 `layer_taxonomy.yaml` —— 这张**图层命名表本身就能抄进自己的立绘规格书**。",
        warn="⚠️ 作者自标 **Alpha / 不建议生产环境**，接口与输出格式可能随时变；"
             "要跑 SAM2 + ISNet，**16GB 内存 + 无独显的机器压力较大**（未标最低配置）；"
             "输出是「能导入」**不是「绑好骨」** —— 绑骨仍要人（呼应上一条：Cubism 不能自动绑骨）。",
        ext=(80, "8.0/10", "把「美术素材标准化」这一段自动化，是整条链上最值钱的一段"),
        use=(68, "6.8/10", "现在别押（Alpha）· 但图层命名表立刻可用"),
        src="推送 2026-03-29 · 8★ · MIT · Python · 信源 [1287]",
    ),
    dict(
        nid="rpm37c10", name="cormy-live2d —— 「正规的 Cubism 工程长什么样」的拆解范本",
        url="https://github.com/jcs130/cormy-live2d",
        lang="JavaScript", stars="0",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="一个「可复现的 Live2D 角色制作源文件」合集 —— 把某个角色的模型、表情、动作与**制作源文件**一起公开。",
        analogy="索引里收的多是「工具」或「成品模型」，**「制作源文件 + 可复现 rig」这种教学/模板型仓库一直是空档**。"
                "对「想做第一个模型、但不知道正规工程该长什么样」的人，这类仓库是**照着拆的范本** —— "
                "看一遍正规的目录结构 / 参数 / 变形器规划，比自己瞎试省得多。",
        warn="⚠️ 角色是第三方 IP，**源文件仅供学习，商用必侵权**；GPL-3.0 对衍生也有限制；★0、建仓当天推送。",
        ext=(40, "4.0/10", "不可扩展，只作学习材料"),
        use=(55, "5.5/10", "不采用资产 · 可下载源文件逐层对照学结构"),
        src="推送 2026-10-10 · 0★ · GPL-3.0 · JavaScript · 信源 [1288]",
    ),
    dict(
        nid="rpm37c11", name="whale-maid-svg-layers ——「先用矢量重绘、再分层」这条私家流水线",
        url="https://github.com/daoming07280/whale-maid-svg-layers",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="一个具体案例的**分层原始素材**：用 SVG 重绘的角色，拆成 **59 层** PSD/SVG，走 `psd2live → moc3` 流水线。",
        analogy="这是与 See-through（位图按深度拆层）**相反**的一条路：**先矢量重绘、再分层**。"
                "矢量天然干净、层可无损缩放、边缘不会糊 —— 代价是**重绘的人工**。"
                "对「素材本来就糊、拆出来没法用」的情况，重绘反而是省事的那条。",
        warn="⚠️ 无 license、★0、个人实验；「59 层」是否每层都合规可用未经验证；素材是他人 IP，不可商用。",
        ext=(38, "3.8/10", "只是素材，做法可借"),
        use=(45, "4.5/10", "采用思路（矢量重绘降低绑骨难度），不采用素材"),
        src="推送 2026-09-21 · 0★ · 无许可证 · Python · 信源 [1289]",
    ),
    dict(
        nid="rpm37c12", name="UnityLive2DExtractor-Unofficial —— 上游停更后的社区维护分支",
        url="https://github.com/zwa73/UnityLive2DExtractor-Unofficial",
        lang="C#", stars="57",
        tags=[("t-mod", "模块化"), ("t-warn", "注意")],
        plain="**社区维护版**的 Unity Live2D 提取器 —— 把 Unity 工程里的 Live2D 资源扒回成 `motion3 / physics3 / model3`。",
        analogy="索引里收的是**上游**（★634，早已停更）与另一个 fork。这个 `zwa73` 分支才是"
                "「**原版停更之后还能不能用**」这个实际问题的答案 —— 而 ★57 说明确实有人靠它吃饭。",
        warn="⚠️ 代码停在 2024-08；**提取他人游戏模型有版权风险**，仅限自有/授权内容；依赖 AssetStudio.dll 等预编译库。",
        ext=(55, "5.5/10", "解包老游戏专用，覆盖面窄"),
        use=(42, "4.2/10", "不做 Unity 解包就无关 · ★57 说明需求真实存在"),
        src="推送 2024-08-21 · 57★ · MIT · C# · 信源 [1290]",
    ),
    dict(
        nid="rpm37c13", name="nnnotes —— 面向单个商业手游的「一站式」Live2D 资产工具箱",
        url="https://github.com/MetaSekaiLab/nnnotes",
        lang="Python", stars="15",
        tags=[("t-mod", "模块化"), ("t-warn", "注意")],
        plain="某商业音游的**离线数据工具箱** —— catalog / 打包资源 / masterdata / 剧情 / **Live2D** / 音频 一站式解包。",
        analogy="此前索引里只有零散的 `UnityLive2DExtractor`，**没有「面向一个具体游戏、成体系」的数据工具箱**。"
                "它示范的是「**成体系地扒一个游戏**」该有哪些模块 —— 这个结构本身比代码更有参考价值。",
        warn="⚠️ 版权用途明确（研究单个商业游戏），**仅供研究，不可商用/分发**；另有同源 `nnnotes-standalone`（★0）疑为衍生版。",
        ext=(35, "3.5/10", "面向单个游戏，不可迁移"),
        use=(30, "3.0/10", "不采用 · 为「游戏资产提取」补一个体系化实例"),
        src="推送 2026-10-10 · 15★ · MIT · Python · 信源 [1291]",
    ),
    dict(
        nid="rpm37c14", name="GFLMotionConverter —— 把游戏私有动作格式转回标准 motion3/physics3",
        url="https://github.com/SuomiKP31/GFLMotionConverter",
        lang="C#", stars="10",
        tags=[("t-mod", "模块化"), ("t-warn", "注意")],
        plain="把从 **UABE 导出的《少女前线》Live2D 动作/物理文件**，转换成能用的 `motion3.json` / `physics3.json`。",
        analogy="索引里 moc3 相关工具多是「读 / 看」，**「把游戏内私有动作格式转回标准格式」的转换器此前没有**。"
                "它代表一类真实困境：**模型能读出来，但动作是私有格式，读出来也没法用**。",
        warn="⚠️ 只针对《少女前线》一种格式；代码停更（2022）；GPL-3.0；游戏素材版权风险。",
        ext=(30, "3.0/10", "单一游戏专用"),
        use=(28, "2.8/10", "不采用 · 为「动作/物理迁移」补一个实例"),
        src="推送 2022-05-25 · 10★ · GPL-3.0 · C# · 信源 [1292]",
    ),
    dict(
        nid="rpm37c15", name="Turboism —— Cubism Editor 的第三方插件框架（附逐版本适配表）",
        url="https://github.com/turboism/Turboism",
        lang="Java", stars="3",
        tags=[("t-mod", "模块化"), ("t-new", "新"), ("t-warn", "注意")],
        plain="**Windows 优先**的 Cubism Editor 运行时增强工具 + 插件框架 —— 用 Java agent + 公开 SDK 给编辑器加"
              "参数/网格工具、PSD 工具、调色板增强与本地自动化。",
        analogy="它对「5.3.x 到底改了什么」给了一条**第三方硬证据**：支持表列出 "
                "**5.2.03 / 5.3.02 / 5.3.03 各配一个「精确版本适配器（Exact-version adapters）」** —— "
                "说明 5.3.x 的**内部接口在变**，社区只好逐版本适配。索引里此前没有任何「给 Cubism Editor 做插件框架」的条目。",
        warn="⚠️ **AGPL-3.0-only**（传染性强）；**它不分发 Cubism Editor、也不绕过其许可**，你必须已有合法授权的编辑器；"
             "插件**会改工程内容**，作者明确提醒「用前自行备份」。",
        ext=(72, "7.2/10", "把 Editor 里的重复动作自动化，是「重度用 Editor」的人真正想要的"),
        use=(60, "6.0/10", "Windows 优先 + 基准人物环境对口 · 但 AGPL + ★3，先观察"),
        src="推送 2026-10-08 · 3★ · AGPL-3.0 · Java · 信源 [1293]",
    ),
    dict(
        nid="rpm37c16", name="cubism-editor-computer-use —— 官方 5.4 alpha「编辑 API」的样例 + 异步 Python 封装",
        url="https://github.com/pakholeung37/cubism-editor-computer-use",
        lang="Python", stars="0",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="**Cubism Editor 外部应用 API 的样例集 + 异步 Python 客户端** —— fork 自官方样例的 5.4 alpha 分支，"
              "补齐了 `cubism_async/`（session / dispatcher / identity / specs）。",
        analogy="索引里的 MCP 工具都停在「**读**参数 / 控制参数」，**这里是「写（编辑）」的官方样例** —— "
                "`04_EditSample` 正是 **Cubism 5.4 alpha 的编辑 API 示例**。"
                "这是「从控制走向真实建模自动化」的分水岭物料；`cubism_async/` 的分层更是"
                "**「如何跟本机 GUI 程序握手」可直接照抄的范式**。",
        warn="⚠️ 上游是 **alpha**，接口随时变；需本机装 Cubism Editor 5.4 alpha 并开启 External API（默认端口 **22033**）；"
             "安全性上，HTML 样例每次加载都要在编辑器里**手动授权**。",
        ext=(75, "7.5/10", "官方开放「编辑」后，第三方自动化空间被真正打开"),
        use=(52, "5.2/10", "要吃 5.4 alpha + 正版 Editor 才用得上 · 抄它的握手分层"),
        src="推送 2026-09-16 · 0★ · MIT · Python · 信源 [1294]",
    ),
    dict(
        nid="rpm37c17", name="NanaBetterCubism —— 对话驱动改 Cubism 工程，带事务与回读校验",
        url="https://github.com/sena-nana/NanaBetterCubism",
        lang="Rust", stars="0",
        tags=[("t-mod", "模块化"), ("t-new", "新"), ("t-warn", "注意")],
        plain="**对话驱动的 Cubism Editor Agent** —— 通过 `127.0.0.1:22033` 连本机 Editor，用官方 External API 全量工具，"
              "所有结构编辑统一走「**preview → 确认 → 后端事务 → 回读验证**」。",
        analogy="用 agent 改美术资产，所有人的第一反应都是「**改坏了怎么办**」。"
                "这个项目的答案是一套设计模式：**先预览、再确认、在一个事务里改、改完回读校验**，且可取消。"
                "索引里没有任何条目给出这种「可回滚的模型编辑」范式 —— 这套模式**任何想给美术工具接 AI 的人都该抄**。",
        warn="⚠️ ★0、依赖 Tauri + 较新 Node/Yarn，环境偏重；"
             "作者明写「**不做权限批准门，也不提供本地文件直接编辑**」→ **安全边界全靠模型自觉**，谨慎；"
             "是某个特定项目的特化精简版，通用性未知。",
        ext=(70, "7.0/10", "「可回滚的 AI 编辑」这个模式可复用到任何生成/编辑工具"),
        use=(50, "5.0/10", "不直接用 · 抄那套 preview→确认→事务→回读 的安全流程"),
        src="推送 2026-09-07 · 0★ · MIT · Rust · 信源 [1295]",
    ),
    dict(
        nid="rpm37c18", name="cubihub —— Cubism 工程本身的管理器（多版本 + Mesh Preset + 日志诊断）",
        url="https://github.com/RainTrap341/cubihub",
        lang="Rust", stars="0",
        tags=[("t-mod", "模块化"), ("t-warn", "注意")],
        plain="**Cubism Editor 的离线项目管理器**（Tauri 2 + React）—— 自动扫描本机装了哪些 Cubism 版本（4/5 系列）、"
              "维护项目库、**绑定启动版本一键开项目**、读写 **网格布点预设（Mesh Presets）**、工程备份、"
              "**粘贴编辑器日志自动出问题摘要**。",
        analogy="索引里的工具全在做「模型 / 运行时」，**没有人做「管 Cubism 工程本身」**。"
                "它戳中一个很实际的痛点：**多个 Cubism 版本共存时，项目该用哪个版本开**、工程怎么备份、"
                "报错日志看不懂怎么办。「日志 → 摘要建议」这一条尤其实用。",
        warn="⚠️ ★0、单人、3 月建仓后无更新；备份是「打开文件夹让你手动替换」，**不是自动还原**。",
        ext=(55, "5.5/10", "痛点是真痛点，但项目自身停滞"),
        use=(50, "5.0/10", "不重度用 Cubism 就用不上 · 「按版本绑定启动 + 工程备份」的思路值得自建脚本时借"),
        src="推送 2026-03-21 · 0★ · MIT · Rust · 信源 [1296]",
    ),
    dict(
        nid="rpm37c19", name="Agent-desktop-pet（CodexPet 2.0）—— 表情由「Agent 工作状态」驱动",
        url="https://github.com/shicheng5589-oss/Agent-desktop-pet",
        lang="Python", stars="20",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-ok", "持续更新")],
        plain="贴在 Windows 桌面上的 Live2D 小桌宠 —— **它跟着 Codex / Claude Code / Gemini 等 12 个 Agent 的实时状态换表情**"
              "（思考中 / 执行中 / 等你 / 出错 / 完成…共 9 个状态），眼睛带惯性跟鼠标，"
              "**只读本地会话记录、不联网**。",
        analogy="同类桌宠的表情来源只有两种：**你手动切**，或者 **LLM 对话驱动**。"
                "它把第三种信号源拿了出来 —— **编码 agent 的工作状态**。"
                "对天天盯 agent 跑任务、同时维护一个索引站的人，这几乎是量身定做："
                "**你不用看屏幕就知道 agent 是卡住了还是在干活**。",
        warn="⚠️ 许可 **NOASSERTION**（仓库内有 THIRD-PARTY.md，装前务必读）；"
             "**需自备 Live2D 模型**（仓库不含模型）；状态解析依赖各 agent 本地会话文件格式，**agent 更新可能解析失败**。",
        ext=(65, "6.5/10", "「状态→表情」这套映射可复用到任何长跑任务"),
        use=(78, "7.8/10", "**本辑最可能明天就用上的一条**：Windows 原生 + Python + 只读本地不联网 + 活跃"),
        src="推送 2026-10-11 · 20★ · 许可证不明 · Python · 信源 [1297]",
    ),
    dict(
        nid="rpm37c20", name="AAAAGENT —— Agent 伴侣，并公开了角色的分层 PSD 设计稿",
        url="https://github.com/phoiex/AAAAGENT",
        lang="TypeScript", stars="143",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "注意")],
        plain="带语音、情绪记忆、**微信接入**、能跟 Codex / DeepSeek Harness 联动的 Live2D 伴侣"
              "（macOS 优先，Windows 开发中），仓库里直接放了角色设计稿 `whale-layers.psd`。",
        analogy="索引里的 AI 桌宠多是「LLM 聊天 + Live2D 立绘」；它把"
                "「**与编码 Agent 联动 + 情绪记忆 + IM（微信）**」捆成了一体，"
                "并且**公开了角色的分层 PSD 设计稿** —— 对「想知道一个能上线的伴侣角色，工程上长什么样」的人，这是稀缺素材。",
        warn="⚠️ README 明写 **Noncommercial only; attribution required** → **商用直接排除**；"
             "macOS 优先、**Windows 还在开发中** → 基准人物现在装了也跑不起来。",
        ext=(60, "6.0/10", "设计稿与状态机可参考，代码受非商用限制"),
        use=(45, "4.5/10", "不采用（非商用 + Windows 未完成）· 可下载 PSD 当分层规范范本"),
        src="推送 2026-10-10 · 143★ · 许可证不明（非商用）· TypeScript · 信源 [1298]",
    ),
    dict(
        nid="rpm37c21", name="live2d-desktop-pet-electron —— 两个可直接抄的实现细节",
        url="https://github.com/fyisgod/live2d-desktop-pet-electron",
        lang="TypeScript", stars="0",
        tags=[("t-mod", "模块化"), ("t-new", "新")],
        plain="把 **VTube Studio 导出的 Live2D 模型**变成桌面宠物：Electron + Cubism 5 SDK for Web，"
              "**自带 VTS 导入器 + 逐像素点击穿透**。",
        analogy="桌面宠物类的 Electron 项目不少，但少见两件事："
                "① **「VTube Studio 导入器」** —— 直接吃 VTS 生态里已有的海量现成模型，省掉建模；"
                "② **「逐像素点击穿透」** —— 不规则形状下鼠标能穿过透明区，这是桌面宠物**真正能日常用起来**的关键细节。"
                "这两点都是可以直接搬到自己项目里的具体做法。",
        warn="⚠️ ★0、单人、刚建仓，无使用验证；Electron 打包体积大。",
        ext=(50, "5.0/10", "项目本身太新，价值在两条现成实现"),
        use=(52, "5.2/10", "不直接用 · 抄 VTS 导入 + 逐像素命中测试"),
        src="推送 2026-09-19 · 0★ · MIT · TypeScript · 信源 [1299]",
    ),
    dict(
        nid="rpm37c22", name="ZerolanPlayground —— 首次出现的呈现形态：AR 叠加",
        url="https://github.com/AkagawaTsurunaki/ZerolanPlayground",
        lang="C#", stars="32",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="用 Unity + Vuforia 做的 **AR 虚拟角色展示** —— 把 Cubism Live2D 模型叠到摄像头实拍画面上。",
        analogy="索引里 Live2D 的呈现形态一直是「2D 屏幕 / 桌面 / 网页」，"
                "**AR（增强现实）叠加是第一次出现**，而且是「Live2D + 图像识别」的具体组合 —— "
                "比如**用一张实体卡片触发看板娘**。补的是「还能放在哪儿」这个维度。",
        warn="⚠️ 无 license；代码停在 2025-07；AR + Unity + Vuforia 对「16GB Windows 的 Ren'Py 用户」门槛过高；"
             "Vuforia 另有商用条款。",
        ext=(48, "4.8/10", "呈现形态上有新意，但依赖重"),
        use=(28, "2.8/10", "不采用 · 仅登记一个全新的呈现维度"),
        src="推送 2025-07-01 · 32★ · 无许可证 · C# · 信源 [1300]",
    ),
]

FOOTNOTES = [
    (1279, "https://github.com/AyagamiDev/ayagami", "AyagamiDev/ayagami",
     "351★ · Apache-2.0 · Rust · 创建 2026-07-11 · 推送 2026-09-14 · GitHub REST API 实测"),
    (1280, "https://github.com/AyagamiDev/ayagami-gd", "AyagamiDev/ayagami-gd",
     "39★ · MIT · Rust · 推送 2026-09-15 · GitHub REST API 实测"),
    (1281, "https://github.com/pakholeung37/manosaba-live2d", "pakholeung37/manosaba-live2d",
     "0★ · 无许可证 · C++ · 推送 2026-09-16 · GitHub REST API 实测"),
    (1282, "https://github.com/Inochi2D/inox2d", "Inochi2D/inox2d",
     "298★ · 许可证不明 · Rust · 推送 2026-09-23 · GitHub REST API 实测"),
    (1283, "https://github.com/Inochi2D/inochi-viewer", "Inochi2D/inochi-viewer",
     "47★ · BSD-2-Clause · D · 推送 2026-09-15 · GitHub REST API 实测"),
    (1284, "https://github.com/yanjingzhaisun/inochi2d-toolkit", "yanjingzhaisun/inochi2d-toolkit",
     "0★ · MIT · Python · 推送 2026-09-24 · GitHub REST API 实测"),
    (1285, "https://github.com/henceketh/inochi2d-autorig-claude", "henceketh/inochi2d-autorig-claude",
     "0★ · 无许可证 · Python · 推送 2026-10-05 · GitHub REST API 实测"),
    (1286, "https://github.com/Yoru-KenomoVT/ayatsuri_2d", "Yoru-KenomoVT/ayatsuri_2d",
     "2★ · GPL-3.0 · Rust · 推送 2026-09-13 · GitHub REST API 实测"),
    (1287, "https://github.com/CVIndomitable/illust2psd", "CVIndomitable/illust2psd",
     "8★ · MIT · Python · 推送 2026-03-29 · GitHub REST API 实测"),
    (1288, "https://github.com/jcs130/cormy-live2d", "jcs130/cormy-live2d",
     "0★ · GPL-3.0 · JavaScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1289, "https://github.com/daoming07280/whale-maid-svg-layers", "daoming07280/whale-maid-svg-layers",
     "0★ · 无许可证 · Python · 推送 2026-09-21 · GitHub REST API 实测"),
    (1290, "https://github.com/zwa73/UnityLive2DExtractor-Unofficial", "zwa73/UnityLive2DExtractor-Unofficial",
     "57★ · MIT · C# · 推送 2024-08-21 · GitHub REST API 实测"),
    (1291, "https://github.com/MetaSekaiLab/nnnotes", "MetaSekaiLab/nnnotes",
     "15★ · MIT · Python · 推送 2026-10-10 · GitHub REST API 实测"),
    (1292, "https://github.com/SuomiKP31/GFLMotionConverter", "SuomiKP31/GFLMotionConverter",
     "10★ · GPL-3.0 · C# · 推送 2022-05-25 · GitHub REST API 实测"),
    (1293, "https://github.com/turboism/Turboism", "turboism/Turboism",
     "3★ · AGPL-3.0 · Java · 推送 2026-10-08 · GitHub REST API 实测"),
    (1294, "https://github.com/pakholeung37/cubism-editor-computer-use", "pakholeung37/cubism-editor-computer-use",
     "0★ · MIT · Python · 推送 2026-09-16 · GitHub REST API 实测"),
    (1295, "https://github.com/sena-nana/NanaBetterCubism", "sena-nana/NanaBetterCubism",
     "0★ · MIT · Rust · 推送 2026-09-07 · GitHub REST API 实测"),
    (1296, "https://github.com/RainTrap341/cubihub", "RainTrap341/cubihub",
     "0★ · MIT · Rust · 推送 2026-03-21 · GitHub REST API 实测"),
    (1297, "https://github.com/shicheng5589-oss/Agent-desktop-pet", "shicheng5589-oss/Agent-desktop-pet",
     "20★ · 许可证不明 · Python · 推送 2026-10-11 · GitHub REST API 实测"),
    (1298, "https://github.com/phoiex/AAAAGENT", "phoiex/AAAAGENT",
     "143★ · 许可证不明（DSE 非商用）· TypeScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1299, "https://github.com/fyisgod/live2d-desktop-pet-electron", "fyisgod/live2d-desktop-pet-electron",
     "0★ · MIT · TypeScript · 推送 2026-09-19 · GitHub REST API 实测"),
    (1300, "https://github.com/AkagawaTsurunaki/ZerolanPlayground", "AkagawaTsurunaki/ZerolanPlayground",
     "32★ · 无许可证 · C# · 推送 2025-07-01 · GitHub REST API 实测"),
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

    desc = ('第三十二辑三路调研（gh 路 30 条 / cn 路 16 条 / official 路 21 条），本版取 22 项，'
            '主题 **有人正面拆了 Cubism Core 那堵墙**。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/&lt;r&gt;` 逐条实测（主 agent 已复验全部 22 条）。'
            '<strong>本辑主线：① 前六辑反复卡在「不买 Cubism Editor 就没有 moc3 渲染器」，'
            '这一辑出现了正面拆墙的人 —— AyagamiDev/ayagami（★351 · Rust · Apache-2.0）'
            '是索引里第一条公开、活跃、声称已实现 MOC3 加载与渲染的开源库，'
            '而且划清法律姿态：只用黑盒逆向、从不反汇编专有软件；配套 ayagami-gd（★39）与 manosaba-live2d'
            '（官方 gd_cubism 与 Ayagami 在同一 Godot 工程并行跑的对照实验台）；'
            '② Cubism Editor 的本机 External API（22033 端口）被第三方围建出一整簇工具 —— '
            'Turboism（附 5.2.03/5.3.02/5.3.03 逐版本适配器）、cubism-editor-computer-use'
            '（官方 5.4 alpha 编辑 API 样例 + 异步 Python 客户端）、NanaBetterCubism'
            '（preview→确认→事务→回读验证）、cubihub（多版本工程管理 + Mesh Preset）；'
            '③「单图→可用模型」多了一条技术栈：illust2psd（ISNet + SAM2 + inpaint）直接产出符合 Cubism '
            '命名规范的分层 PSD，与 See-through 的深度拆层是两条不同的路；'
            '④ 桌宠的表情信号源换了 —— Agent-desktop-pet 把 12 个编码 Agent 的实时状态映射成 9 种表情、'
            '只读本地不联网；⑤ 官方侧两处口径被推翻 + 一处退役可回滚（5.4 SDK alpha 确实存在 / '
            'npm easy-live2d 真实存在且已 1.0.0 / creatorsforum.live2d.com 本轮 HTTP 200）。</strong>')

    block = ['    <div class="group" data-page-node-id="rpm37g">',
             '      <div class="group-title" data-page-node-id="rpm37gt">🆕 第三十七版增补 · 有人正面拆了 Cubism Core 那堵墙：第一条公开的 moc3 开源渲染器 + Editor External API 工具簇（22 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm37gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm37r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm37ra%s">%s</a> — %s</div>'
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
