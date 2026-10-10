# -*- coding: utf-8 -*-
"""第三十四版增补：把第二十九辑「Live2D × Agent 与开源编辑器」的 18 个条目登记进 index.html。

本辑候选池约 413 条（8 组 GitHub 搜索去重后），关键词命中且未收录 296 条；
与 `index.html`（1215 项）及全部历史存档机器比对，命中 0。

**本辑主线：前三辑一直在答「不买 Editor 怎么凑合」，本辑第一次有人把两件事做实了。**

1. **编辑器本身被开源实现了** —— `umamoorg/umamo`（GPL-3.0 / Kotlin）：README 明确
   **CMO3 与 MOC3 双向导入导出，兼容到 Cubism 5.4**，带 `dump / convert / diff / extract` CLI。
   ⚠️ 但 alpha、**动画功能还没做**、且格式知识是**黑盒观察逆向**出来的。
2. **绑定这件事被做成了「agent 可写、可 diff、可自证」** —— `RevStudio/Rev2D`（MIT）：
   **一个绑定 = 一个 `*.r2d.json`**，2600+ 测试、35 条 CLI、**18 个 MCP 工具**、
   无 GPU 的确定性渲染器；motion3/exp3/physics3/cdi3/model3 **双向**，
   但 **`.moc3` 不支持**（专有二进制）。
3. **「绕开 Editor」整件事的账突然变了** —— 官方学生优惠：Cubism PRO indie 三年
   **$238.20 → $57.16（76% OFF）**，一次性买断、毕业后可继续用、中国区支持**学信网验证码**。

**上轮欠账 #4 闭环（法务）**：`Ariakage/live2d-agent-kit` 的 `THIRD_PARTY_NOTICES.md`
把 psd2live 的 GPL 边界讲清楚了 —— kit 自身代码 **MIT**，但 `integrations/psd2live/*.kt`
与 `patches/*.patch` 因与 GPL 引擎一起编译而是 **GPL-3.0-only**；psd2live 本体只下载到
被忽略的本地缓存、**不随包分发**。→ **GPL 传染的是工具代码，不是它产出的模型文件**。

**另一个闭环**：gamemale 复核 —— HTTP 200 但返回 **Cloudflare Turnstile 挑战页**，
上一辑「结构性不可取」的判定成立（本辑不再单独投入）。

数据来源：2026-10-11 GitHub REST API 实测（`gh api repos/<r>` + `readme`）+ WebSearch/WebFetch 一手页面（`_r29/`）。
幂等：已存在本版标记则跳过。
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1214"'
FIRST_NEW_FOOTNOTE = 1215
MARKER = "第三十四版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十三版增补 2026-10-10',
    '共 1215 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项 + 第三十二版增补 16 项 + 第三十三版增补 16 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十四版增补 2026-10-11',
    '共 1233 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项 + 第三十二版增补 16 项 + 第三十三版增补 16 项 + 第三十四版增补 18 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm34c2", name="Rev2D（把 Live2D 绑定做成「一个 JSON」给 agent 写）",
        url="https://github.com/RevStudio/Rev2D",
        lang="TypeScript", stars="7",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新"), ("t-warn", "星少但有用")],
        plain="「Live2D / Spine 风格的 2D 绑定与动画，**为 AI agent 而造**」。核心主张：**一个绑定 = 一个 "
              "`*.r2d.json`** —— 参数、骨骼、warp 变形器、部件、关键形绑定、IK、物理、分层动画全在这一个文件里，"
              "按 id 寻址、以画布像素为单位，所以**可以 diff、可以 review、可以程序生成**。"
              "再配一个无 GPU、无浏览器的**确定性 headless 渲染器**（同样的模型和输入永远出同样的像素），"
              "能出调试叠层、contact sheet、GIF、PNG 序列。35 条 CLI 命令（全带 `--json`）+ "
              "**18 个 MCP 工具的 MCP server**（返回渲染图）。",
        analogy="上一辑的 `live2d-add-motion` 只能「给已有模型加动作」。Rev2D 是**连模型带动作都能让 agent "
                "从零写、并且自己证明它对** —— 判据不是「看起来对」，是渲染图加 `inspect` / `analyze` 的数字。"
                "这个思路和我们的房规 #33「规则要能被测」是同一件事。",
        warn="⚠️ **`.moc3` 不支持**：README 明说是专有未公开二进制。它能搬的是 **motion3 / exp3 / physics3 / "
             "cdi3 / model3 这些 JSON**，美术网格和变形器搬不了。→ 它不是「替代 Live2D」，"
             "是「在 Live2D 旁边给 agent 一个可写的沙盘」。"
             "⚠️ 每次转换都会出一份**报告**，列出被近似或被丢弃的特性（带稳定编码），不会静默丢东西。"
             "⚠️ 7★、很新；Node ≥ 22，编辑器端到端测试需本机装 Chrome。",
        ext=(95, "9.5/10", "MIT + 2600+ 测试 + 18 个 MCP 工具 + 可 diff 的 JSON 格式 —— "
                           "目前见过的**最能接 agent 流水线**的一个"),
        use=(85, "8.5/10", "用法：agent 在 Rev2D 模型上编动作 → 渲染 + 数字自检 → 导出 `.motion3.json` → "
                           "拿回 Cubism Viewer / SDK 里放 · MIT · 推送 2026-10-06"),
        src="推送 2026-10-06 · 7★ · MIT · TypeScript · 信源 [1215]",
    ),
    dict(
        nid="rpm34c3", name="live2d-agent-kit（Codex 做 Live2D 的完整流水线 + 把 GPL 边界讲清了）",
        url="https://github.com/Ariakage/live2d-agent-kit",
        lang="Python", stars="26",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="帮 Codex 和其他 coding agent 把**参考图或分层 PSD 做成能跑的 `.moc3`**。含拆层配方、"
              "psd2live 适配器与累计补丁、本地 NCNN 动漫 4× 超分（RGB 与 alpha 分开）、"
              "原生 Core 校验 + 浏览器实测、打包脚本，以及嘴周色差 / 闭眼接缝 / 断发的修复记录。"
              "示例角色 Pink Sakura：24 源层 / 26 Drawable / 24 参数，2048²→8192² 超分，"
              "**202 个原生姿态 + 22 项 Web 检查**。带 `SKILL.md`。",
        analogy="上一辑我们只敢说「改 JSON 那层是安全的」。这条把**整条链**都摊开了 —— 连「先修拆层和遮罩，"
                "再做超分」（混入发片的衣服像素会跟着头发动，提高分辨率只会让断口更明显）这种**顺序**都写清了。",
        warn="⚠️ **本辑最重要的法务澄清（上轮欠账 #4 闭环）**：`THIRD_PARTY_NOTICES.md` 写得很清楚 —— "
             "kit 自己的代码是 **MIT**，但 `integrations/psd2live/*.kt` 与 `patches/psd2live-agent-kit.patch` "
             "因为和 GPL 引擎一起编译，**是 GPL-3.0-only**；而 psd2live 本体只下载到被忽略的本地缓存、"
             "**不随包分发**。→ **GPL 传染的是工具代码，不是它产出的模型文件**（示例资产另按 CC BY 4.0）。"
             "**这仍不是法律意见，但终于有了一份可引用的依据。**"
             "⚠️ 需要 Git / Python 3.10+ / **JDK 21** / Node 22+。",
        ext=(90, "9.0/10", "有 `SKILL.md` + `tools/catalog.json` + `tools/commands.md`，"
                           "agent 最容易接的一档；CLI 每一步都有独立入口"),
        use=(88, "8.8/10", "先跑 `scripts/doctor.sh` 通最小几何示例，**确认本机导出链与 Core 可用**再碰美术 · "
                           "MIT + GPL-3.0 · 推送 2026-09-12"),
        src="推送 2026-09-12 · 26★ · MIT + GPL-3.0 · Python · 信源 [1216]",
    ),
    dict(
        nid="rpm34c4", name="官方学生优惠（Cubism PRO 三年 $57.16，中国区支持学信网）",
        url="https://student.live2d.com/en/student-discount/",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="官方 Live2D Student Discount Program：学生和教职员工买 **Live2D Cubism PRO indie 三年计划 "
              "76% OFF —— $238.20 → $57.16**。一次性买断、**不自动续费**、功能与标准 PRO 相同、"
              "**毕业后可以一直用到订阅期满**。中国区入口 `live2d.jp/chn/student-discount`，"
              "**没有学校邮箱也可以用「学信网验证码」申请**。另有 LEAP 教育支援计划：向教育机构"
              "**无偿**提供 Editor PRO 授权（已 200+ 家）。",
        analogy="前三辑一直在算「不买 Editor 怎么绕」。这条是**把问题本身砍掉一半** —— "
                "三年 57 美元（约 ¥450），可能比绕路花掉的时间还便宜。",
        warn="⚠️ **口径打架**：英文学生页写 **76% OFF**，日文官网首页写 **80% OFF**，中文二手教程写「2.4 折」"
             "（= 76% off，与英文一致）→ **以结算页为准，别信宣传语**（M-0001 的五种重复形态之外，"
             "这是第 6 种：**同一件事的多个官方口径**）。"
             "⚠️ 优惠券**只在 Live2D Store/EN 有效**；审核约 5–6 天；仅适用于 indie 三年计划。",
        ext=(30, "3.0/10", "它不是工具，没有可拓展性 —— 但它会让上面好几条的「绕路价值」重新估值"),
        use=(98, "9.8/10", "**本辑对用户最实际的一条**：在校生身份直接可用，中国区支持学信网验证码申请"),
        src="官方学生优惠页 · 2026-10-11 核实 · 信源 [1217]",
    ),
    dict(
        nid="rpm34c5", name="cubism-go（Go 版非官方 SDK，Core 5.x/6.x 自动选版）",
        url="https://github.com/aethiopicuschan/cubism-go",
        lang="Go", stars="32",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="非官方 Go 实现，靠 `ebitengine/purego` 直接调 Cubism Core 动态库（不需要 cgo）。"
              "**Core 5.x 与 6.x 会按版本自动选择** —— 这正是上一辑讲的 ABI 问题的正面应对："
              "不用你手动切，库自己认。带 Ebiten 渲染器，也可自定义渲染器。",
        analogy="上一辑我们把 ABI 从玄学变成了「一个可以查的数字」。这条更进一步 —— "
                "**让库自己查，人不用记**。",
        warn="⚠️ README 明确：Core 6 只覆盖**既有 Core 接口**，**新的混合模式与离屏合成（offscreen）没实现**，"
             "**用了离屏的模型会直接 load error**。⚠️ Go 需 1.27.1+。⚠️ 需要自备 Core 动态库与模型。",
        ext=(85, "8.5/10", "purego 绑定，容易被别的 Go 项目嵌一层；renderer 可换"),
        use=(70, "7.0/10", "用户主力是 Ren'Py / Python，Go 不是首选；但它是**ABI 自动选版**这个思路的现成样本"),
        src="推送 2026-09-17 · 32★ · MIT · Go · 信源 [1218]",
    ),
    dict(
        nid="rpm34c6", name="Agent Avatar（给你正在跑的编码 agent 装一个 Live2D 身体）",
        url="https://github.com/joyparkray/agent-avatar",
        lang="TypeScript", stars="1",
        tags=[("t-make", "建模"), ("t-new", "新"), ("t-warn", "星少但有用")],
        plain="把你**正在用的编码 agent 的真实运行状态**变成桌面上的 Live2D 角色：思考 / 跑工具 / "
              "等待你审批 / 报错各有状态，不用回终端去看那轮跑完没有。五个连接器："
              "**Claude Code · Codex · Hermes · DeepSeek Harness · WorkBuddy**，"
              "支持 Cubism 3/4/5 模型，可跟最近活跃的 agent 或钉住某一个。有文档化的 Bridge Protocol。",
        analogy="别的桌宠是「自己编一套状态哄你玩」，这个是**把真状态接过来** —— "
                "它明确说自己不是又一个带头像的聊天机器人。",
        warn="⚠️ 1★、**创建仅 5 周**，属 alpha。⚠️ **WorkBuddy 连接器要重启应用**才生效；"
             "Codex 要 `/hooks` 人工批准一次（作者特意解释了这不是偷懒）。"
             "⚠️ **要不要往主力 agent（WorkBuddy / DSH）里装第三方插件，得你先放人审一遍再装** —— "
             "别让 agent 自己装。",
        ext=(75, "7.5/10", "Bridge Protocol 文档化，新增 harness 不用改桌面层；五个连接器共用一份状态契约"),
        use=(65, "6.5/10", "方向对、也好玩，但**今天不建议直接装进主力 WorkBuddy** —— 观望 · "
                           "MIT · 推送 2026-10-09"),
        src="推送 2026-10-09 · 1★ · MIT · TypeScript · 创建 2026-09-04 · 信源 [1219]",
    ),
    dict(
        nid="rpm34c7", name="dsh-live2d-pets（DSH 的 Live2D 桌宠插件，一行命令装）",
        url="https://github.com/cyanfish-x/dsh-live2d-pets",
        lang="TypeScript", stars="30",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-new", "新")],
        plain="给 DeepSeek Harness 请个看板娘：`dsh plugin --profile web add dsh-live2d-pets` 一行装。"
              "内置 5 个策展模型（Hiyori / Haru / Mao / Mark / Natori），也可填 `.model3.json` 的 URL 或"
              "**本机绝对路径**（插件 Host 转成同源 HTTP 加载）。宠物实时镜像 agent 的"
              "思考 / 空闲 / 出错 / 完成 / 等审批（SSE 推送）；六种人设台词可自定义；"
              "摸头 / 摸腿 / 摸手分部位反应 + 鼠标跟随 + 拖动停靠。",
        analogy="上一辑我们查清了 Ren'Py 要 Core ≥ 5.3；这条提醒**另一个方向也有版本问题** —— "
                "它的渲染栈停在 pixi-live2d-display 0.4.0 + PixiJS 6.5.10 + **Cubism Core 4**。",
        warn="⚠️ 技术栈停在 **Core 4** —— 按上一辑的 ABI 结论，它对 Cubism 5.3+ 导出的模型可能不吃，"
             "**先确认自己的模型是 Core 4 还是 5**。⚠️ npm 第三方插件，非官方。⚠️ 仓库还有 "
             "`ankesu/dsh-live2d-pet`（★4）与 `A8Chann/dsh-pet-live2d`（★38）两个同题插件，别装重。",
        ext=(70, "7.0/10", "带 `docs/adr/` 与 `docs/spec/`，插件结构规整，可照着写自己的 DSH 插件"),
        use=(75, "7.5/10", "用户本机就在跑 DSH，这条是**现成可装**的 · MIT · 推送 2026-09-24"),
        src="推送 2026-09-24 · 30★ · MIT · TypeScript · 信源 [1220]",
    ),
    dict(
        nid="rpm34c8", name="Amahane-Hikari-Live2D（Codex 主导做出来的一套成品与制作记录）",
        url="https://github.com/luomo66ccff/Amahane-Hikari-Live2D",
        lang="TypeScript", stars="112",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="「用 OpenAI Codex 主导做出来的一套 Live2D」—— 带 WebGL 查看器、跑过的工具清单和制作记录。"
              "是「AI 主导制作」这条路的一个**成品样本**，而不只是又一篇教程。",
        analogy="教程告诉你「应该这么做」，成品记录告诉你「**实际做到了哪一步、卡在哪**」。"
                "判断 AI 能替你做多少，后者有用得多。",
        warn="⚠️ **NOASSERTION**（没有明确 LICENSE）→ **看可以，别直接抄资产**。"
             "⚠️ 星数与「有多少能复用」不成比例，先读记录再决定。",
        ext=(60, "6.0/10", "主要是记录与查看器，不是可复用库"),
        use=(65, "6.5/10", "想知道「AI 主导到底做到什么程度」，这份记录比教程实在 · 推送 2026-09-21"),
        src="推送 2026-09-21 · 112★ · NOASSERTION · TypeScript · 信源 [1221]",
    ),
    dict(
        nid="rpm34c9", name="untitled-pixi-live2d-engine（PixiJS v8 一库吃 Cubism 2–5，自带口型同步）",
        url="https://github.com/Untitled-Story/untitled-pixi-live2d-engine",
        lang="TypeScript", stars="78",
        tags=[("t-make", "建模"), ("t-ok", "持续更新"), ("t-warn", "星少但有用")],
        plain="PixiJS v8 的 Live2D 引擎，**Cubism 2 / 3 / 4 / 5 全支持**，自带原生渲染管线与**口型同步**。",
        analogy="上一辑的 `pixi-live2d5`（★12）只管 Cubism 5，是单版本分叉；这条是「一库吃全版本」，"
                "省得为一个版本号换一套库 —— 对上一辑那个 ABI 坑，这是**最省事的规避方式**。",
        warn="⚠️ 项目较新（创建与推送都在 2026-09），需自行核对它自带的 Core 版本要求。"
             "⚠️ 名字里的 `untitled` 不是笔误，仓库就这么叫。",
        ext=(80, "8.0/10", "Pixi v8 原生管线 + lip-sync 内置，网页端够用"),
        use=(80, "8.0/10", "做网页试玩 / 宣传页时，如果手上的模型版本混杂，**优先它而不是单版本分叉** · "
                           "MIT · 推送 2026-09-20"),
        src="推送 2026-09-20 · 78★ · MIT · TypeScript · 信源 [1222]",
    ),
    dict(
        nid="rpm34c10", name="soullink-emotion-sdk（框架无关的 Live2D 表情动作 SDK，Apache-2.0）",
        url="https://github.com/nanlingyin/soullink-emotion-sdk",
        lang="TypeScript", stars="144",
        tags=[("t-make", "建模"), ("t-mod", "模块化"), ("t-ok", "持续更新")],
        plain="**框架无关**的实时 Live2D 表情与动作 SDK，面向桌面伴侣类应用：把「现在该摆什么表情 / "
              "放什么动作」这件事从具体渲染框架里抽出来单独做一层。",
        analogy="大部分 Live2D 库是「渲染 + 控制」捆在一起卖。这条只做**控制层**，"
                "渲染用哪家你自己定 —— 这也是它能用 Apache-2.0 而不是 GPL 的原因之一。",
        warn="⚠️ 面向「桌面伴侣」场景设计的，塞进视觉小说要自己接一层。"
             "⚠️ 144★ 但创建时间不长，API 可能还会动。",
        ext=(75, "7.5/10", "框架无关 + Apache-2.0，是同类里**许可最干净**的一个"),
        use=(70, "7.0/10", "真要在 VN 里做「情绪驱动表情」而不是只切 preset，这条是个起点 · 推送 2026-09-30"),
        src="推送 2026-09-30 · 144★ · Apache-2.0 · TypeScript · 信源 [1223]",
    ),
    dict(
        nid="rpm34c11", name="live-ascii（在终端里渲染 Live2D，支持人脸追踪）",
        url="https://github.com/Arcelyth/live-ascii",
        lang="Rust", stars="234",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="一个**跑在终端里**的 Live2D Cubism 模型渲染器，支持人脸追踪把真人表情映射到字符画上。",
        analogy="本辑最没用也最好玩的一条。但它的价值是证明了一件事：**渲染不一定要 GUI** —— "
                "这对「想在 CI / 无头环境里检查模型动没动」是个可行的思路。",
        warn="⚠️ 234★ 但本质是玩具向；真要靠它做验收还得另找。⚠️ Rust 写的，改起来门槛不低。",
        ext=(65, "6.5/10", "无头渲染这条路可行，但它是 ASCII 输出，不能直接产出可比对像素"),
        use=(55, "5.5/10", "玩票 / 无头思路参考；不进产线 · MIT · 推送 2026-08-29"),
        src="推送 2026-08-29 · 234★ · MIT · Rust · 信源 [1224]",
    ),
    dict(
        nid="rpm34c12", name="spive2d（Spine 与 Live2D 的轻量查看器）",
        url="https://github.com/lmmtrr/spive2d",
        lang="JavaScript", stars="138",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="一个**简单**的 Spine 与 Live2D 查看器（另有 `1098542053/spive2d-web` 是带 Go 后端的网页版）。"
              "主打「打开就能看」，不做编辑。",
        analogy="Cubism Viewer 是官方的、也是重的。这条是那种「别人发我一个模型，我想先瞄一眼」时"
                "**懒得开大软件**的选择。",
        warn="⚠️ 网页版那个仓库（★0）与本体不是同一个作者，别混。⚠️ 只查看，不能改。",
        ext=(60, "6.0/10", "功能面窄，但单一职责反而稳"),
        use=(75, "7.5/10", "「先看看这个模型长什么样、动作对不对」的最短路 · MIT · 推送 2026-10-09"),
        src="推送 2026-10-09 · 138★ · MIT · JavaScript · 信源 [1225]",
    ),
    dict(
        nid="rpm34c13", name="prometheus-avatar（用 LLM 输出驱动 Live2D / 3D 头像的 SDK）",
        url="https://github.com/myths-labs/prometheus-avatar",
        lang="TypeScript", stars="17",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="用 **LLM 的输出去驱动** Live2D / 3D 头像的开源 SDK —— 让大模型说出来的话直接映射到表情与动作。",
        analogy="听起来很美，但上一辑我们已经判过一次这类方案：**单机视觉小说的对话是写死的**，"
                "运行时让 LLM 改参数这条路，在 Ren'Py 上根本不成立（Ren'Py 无法在运行时改单个参数）。",
        warn="⚠️ **只在「你真要做 AI 主播 / 实时陪伴」时才有用**；对写死的 VN 剧本是走偏。"
             "⚠️ 17★、很新。",
        ext=(70, "7.0/10", "对接层抽象得还行，可换模型后端"),
        use=(50, "5.0/10", "对用户**当前**的视觉小说项目不成立；做 AI 主播才 reconsider · "
                           "MIT · 推送 2026-10-09"),
        src="推送 2026-10-09 · 17★ · MIT · TypeScript · 信源 [1226]",
    ),
    dict(
        nid="rpm34c14", name="Open Avatar Creator（浏览器端开源绑定工具，自有 .oar 格式）",
        url="https://github.com/Hera-Berg/open-avatar-creator",
        lang="TypeScript", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="浏览器里跑的 2D 绑定工具：导入 PSD → 骨骼 + 网格变形绑定 → 对着人脸追踪**实时测** → "
              "导出单一 `.oar` 文件。所有绑定逻辑都在浏览器，模型不出本机。core 122 + creator 65 个测试，"
              "`docker compose up --build` 起。",
        analogy="和 Umamo 是两条路：Umamo 求**跟 Live2D 互通**，这条求**彻底另起炉灶** —— "
                "它连格式都是自己的。",
        warn="⚠️ **自有 `.oar` 格式，与 Live2D 不通** —— 它只是「替代」，不能吃 / 吐 moc3。"
             "所以「已有 Live2D 资产」的人用不上。⚠️ 0★、刚创建，纯前瞻。",
        ext=(65, "6.5/10", "core 不依赖 DOM / React，一个 evaluator 保证「这里看着对 = studio 里也对」"),
        use=(55, "5.5/10", "今天用不上；当作「开源绑定工具该怎么分层」的参考 · 推送 2026-10-10"),
        src="推送 2026-10-10 · 0★ · TypeScript · 信源 [1227]",
    ),
    dict(
        nid="rpm34c15", name="vtuber-pipeline（See-through 与 PSD2Live 之间的对接层）",
        url="https://github.com/lk2168/vtuber-pipeline",
        lang="Python", stars="2",
        tags=[("t-make", "建模"), ("t-mod", "模块化")],
        plain="一张动漫立绘 → 能在 VTube Studio 里直播的 Live2D 模型。定位很窄也很清楚："
              "它是 **See-through（拆层）与 PSD2Live（绑定）之间的对接层**，把两段的输入输出对上。",
        analogy="上一辑分别记了 See-through 和 psd2live，中间那段「怎么把前者的输出喂给后者」一直没人写。"
                "这条就是那段胶水。",
        warn="⚠️ 2★、个人项目，**接口会随上游两个项目变动**。⚠️ 同类还有 "
             "`flowingduskpro/jpg-to-live2d-workflow`（★4）与 `lvhaojie456/image-to-live2d`（★2），"
             "都是同一条链的变体，别重复造。",
        ext=(70, "7.0/10", "只做对接，边界清楚，好替换"),
        use=(65, "6.5/10", "已经在用 See-through + psd2live 的人才需要它 · MIT · 推送 2026-09-23"),
        src="推送 2026-09-23 · 2★ · MIT · Python · 信源 [1228]",
    ),
    dict(
        nid="rpm34c16", name="《一张立绘自动生成 Live2D，最后是怎么散架的》（第一手失败实录）",
        url="https://note.com/dn0288/n/nf89c79d14d27",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="第一手失败实录。作者做了全自动流水线（去背景 → 生成 29 个部件草稿 → 贴图映射到通用 rig → "
              "导出含 `.moc3` 的 zip），**23 个测试全过、29 个部件齐全、Cubism Viewer 里能加载**。"
              "然后插进真实立绘一动就散架：长发形状套不上短发、肩部冒出重复部件、眼嘴位置对不上导致重叠或消失、"
              "脸 / 脖子 / 躯干接缝露缝。作者的结论：**单张立绘里根本不包含「让它动起来」所需的那些信息** —— "
              "刘海挡住的眼睛、闭着的嘴里的牙齿舌头、被头发衣服挡住的脖子肩膀、正面图推不出的侧脸与后脑深度。",
        analogy="上一辑我们有反证、本辑有正面证据；这条把两半合成**一句完整判断**："
                "自动化能帮你把「文件生成」跑通，但**跑通 ≠ 能上直播 / 能进游戏**。"
                "缺的那部分不是 AI 精度问题，是**原图里就没有**。",
        warn="⚠️ 生成式 AI 能「像那么回事地补全」，但**「像那么回事」≠「原作者想要的那个正确答案」**。"
             "⚠️ note.com 直连超时（已列入退役源），本文内容经搜索快照获得 → **标注为二手**。",
        ext=(40, "4.0/10", "它不是工具，是一份**判据**：用它来判断别人吹的「一键生成」到哪一步为止"),
        use=(90, "9.0/10", "**本辑最该读的一条（不是最该用的）** —— 以后再看到「一张图自动生成 Live2D」"
                           "的宣传，先拿它对一遍"),
        src="note.com 第一手复盘 · 2026-10-11 经搜索快照核实（直连超时）· 信源 [1229]",
    ),
    dict(
        nid="rpm34c17", name="《live2D 全栈制作教程 / 避坑》（中文长篇实战，含对 AI 的一手吐槽）",
        url="https://cloudymount789.github.io/blog/live2d_note/",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="一份很长的中文全链路实战手册，作者自己画立绘（7 小时）+ 手动拆层（**14 小时**）踩出来的坑："
              "拆分三原则（**完整性** —— 遮挡部分必须补全；独立性；命名）、布点、变形器父子层级、"
              "九轴、物理摆锤的输入类型（**位置 X 会回位、角度不回位**，两者影响度不同才自然）、"
              "导出前必须编辑纹理图集。还记了「不到万不得已不要删关键帧，会把一整个环境弄坏」这类血泪。",
        analogy="官方手册告诉你「按钮在哪」，这种帖告诉你「**先确认拆层没问题再开始布点**，"
                "否则后面十几个小时白干」。",
        warn="⚠️ 帖子里有一句值得单独摘出来：**「问 AI 很难解决这类问题，他们会一直编造软件的功能」** —— "
             "这和我们的 **M-0028**（LLM 在小众垂直 GUI 软件上编造选项）是同一件事，"
             "只是这次是真人从**被坑的一方**写下来的独立佐证。⚠️ 个人博客，注意内容会随作者改动。",
        ext=(40, "4.0/10", "作为教程不可拓展；作为**判据来源**可复用"),
        use=(88, "8.8/10", "想认真动手做第一个模型，这份比任何「五分钟上手」都值 · 信源 [1230]"),
        src="个人博客（GitHub Pages）· 2026-10-11 核实 · 信源 [1230]",
    ),
    dict(
        nid="rpm34c18", name="WebGAL 官方 Live2D 立绘文档（中文 VN 引擎的两个 js 就能跑）",
        url="http://docs.openwebgal.com/live2D.html",
        lang="文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="中文视觉小说引擎 WebGAL 的 Live2D 接入说明：自行取得授权 → 下载 `live2d.min.js` 与 "
              "`live2dcubismcore.min.js` 放进指定目录（定制引擎 / 单个游戏 / 源码三处之一）→ "
              "模型目录丢进 `game/figure` → 用 `changeFigure:xxx.json -motion=angry -expression=angry01` "
              "直接切动作和表情。",
        analogy="用户做的是 Ren'Py，但这条说明**中文 VN 引擎这条路上 Live2D 只要两个 js + 一个目录就能跑** —— "
                "比 Ren'Py 那套「要先装 Native Core，否则 `has_live2d()` 静默返回 False」轻得多。",
        warn="⚠️ 文档原话：「本项目的作者没有使用任何 Live2D SDK 的源码和模型，由于使用 Live2D 造成的"
             "任何版权纠纷，皆由二次开发者或制作者自行承担」。⚠️ WebGAL 4.6 portable 模式下，"
             "用户数据目录是安装目录下的 `data` 文件夹。",
        ext=(70, "7.0/10", "WebGAL 本身是 Pixi.js 生态，自定义效果空间大"),
        use=(75, "7.5/10", "如果以后想换中文引擎试水，这条说明 Live2D 不是换引擎的阻碍 · 官方文档 · 信源 [1231]"),
        src="WebGAL 官方文档 · 2026-10-11 核实 · 信源 [1231]",
    ),
    dict(
        nid="rpm34c19", name="doro-live2d-web（免构建的 Live2D 网页查看器，顺带补一句模型 json 的坑）",
        url="https://github.com/so0420/doro-live2d-web",
        lang="JavaScript", stars="3",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="**没有构建步骤**的 Live2D Cubism 网页查看器：运行时库全部打进本地，**断网也能跑**；"
              "支持 ArtMesh 级点击判定、拖拽摆弄、表情切换、导出透明 PNG。默认模型是 Dororong（作者 0x4682B4，"
              "免费分发），也可换其他 **Cubism 4/5** 模型。",
        analogy="上几辑我们一直在找「先瞄一眼模型对不对」的最短路。这条更短：不用 npm build，"
                "把模型丢进去就能开。",
        warn="⚠️ **模型文件不随仓分发**（版权归原作者，仓库只给查看器代码），要自己去 BOOTH / Ko-fi 下，"
             "**下之前先看清分发页的使用条款**。"
             "⚠️ 最有价值的是它记的那个坑：**原始 `model3.json` 里 `Expressions` / `Motions` / `HitAreas` "
             "三项可能根本没有** —— 所以「表情切不动、动作抓不到、点击没反应」不一定是库的错，"
             "它的 `setup-model` 脚本会补上这些字段。⚠️ 3★、NOASSERTION（无明确许可证），别抄代码只学思路。",
        ext=(55, "5.5/10", "零构建 + 离线可用，作为「临时看一眼」的脚手架很合适；但无许可证"),
        use=(70, "7.0/10", "**「模型 json 缺 Expressions/Motions/HitAreas」这句是通用知识**，"
                           "不只对这个查看器成立 · 推送 2026-08-27"),
        src="推送 2026-08-27 · 3★ · NOASSERTION · JavaScript · 信源 [1232]",
    ),
]

FOOTNOTES = [
    (1215, "https://github.com/RevStudio/Rev2D", "RevStudio/Rev2D",
     "7★ · MIT · TypeScript · 推送 2026-10-06 · GitHub REST API 实测"),
    (1216, "https://github.com/Ariakage/live2d-agent-kit", "Ariakage/live2d-agent-kit",
     "26★ · MIT + GPL-3.0 · Python · 推送 2026-09-12 · GitHub REST API 实测"),
    (1217, "https://student.live2d.com/en/student-discount/",
     "student.live2d.com · Live2D Student Discount Program",
     "官方页 · $238.20 → $57.16（76% OFF）· 三年 indie · 2026-10-11 WebFetch 核实"),
    (1218, "https://github.com/aethiopicuschan/cubism-go", "aethiopicuschan/cubism-go",
     "32★ · MIT · Go · 推送 2026-09-17 · GitHub REST API 实测"),
    (1219, "https://github.com/joyparkray/agent-avatar", "joyparkray/agent-avatar",
     "1★ · MIT · TypeScript · 推送 2026-10-09 · GitHub REST API 实测"),
    (1220, "https://github.com/cyanfish-x/dsh-live2d-pets", "cyanfish-x/dsh-live2d-pets",
     "30★ · MIT · TypeScript · 推送 2026-09-24 · GitHub REST API 实测"),
    (1221, "https://github.com/luomo66ccff/Amahane-Hikari-Live2D", "luomo66ccff/Amahane-Hikari-Live2D",
     "112★ · NOASSERTION · TypeScript · 推送 2026-09-21 · GitHub REST API 实测"),
    (1222, "https://github.com/Untitled-Story/untitled-pixi-live2d-engine",
     "Untitled-Story/untitled-pixi-live2d-engine",
     "78★ · MIT · TypeScript · 推送 2026-09-20 · GitHub REST API 实测"),
    (1223, "https://github.com/nanlingyin/soullink-emotion-sdk", "nanlingyin/soullink-emotion-sdk",
     "144★ · Apache-2.0 · TypeScript · 推送 2026-09-30 · GitHub REST API 实测"),
    (1224, "https://github.com/Arcelyth/live-ascii", "Arcelyth/live-ascii",
     "234★ · MIT · Rust · 推送 2026-08-29 · GitHub REST API 实测"),
    (1225, "https://github.com/lmmtrr/spive2d", "lmmtrr/spive2d",
     "138★ · MIT · JavaScript · 推送 2026-10-09 · GitHub REST API 实测"),
    (1226, "https://github.com/myths-labs/prometheus-avatar", "myths-labs/prometheus-avatar",
     "17★ · MIT · TypeScript · 推送 2026-10-09 · GitHub REST API 实测"),
    (1227, "https://github.com/Hera-Berg/open-avatar-creator", "Hera-Berg/open-avatar-creator",
     "0★ · TypeScript · 推送 2026-10-10 · GitHub REST API 实测"),
    (1228, "https://github.com/lk2168/vtuber-pipeline", "lk2168/vtuber-pipeline",
     "2★ · MIT · Python · 推送 2026-09-23 · GitHub REST API 实测"),
    (1229, "https://note.com/dn0288/n/nf89c79d14d27",
     "note.com/dn0288 · 一张立绘自动生成 Live2D 的失败实录",
     "第一手复盘 · 23 测试全过但一动就散架 · 2026-10-11 经搜索快照核实（直连超时）"),
    (1230, "https://cloudymount789.github.io/blog/live2d_note/",
     "cloudymount789 · live2D 全栈制作教程 / 避坑",
     "中文长篇实战手册 · 拆层 14 小时的一手坑 · 2026-10-11 核实"),
    (1231, "http://docs.openwebgal.com/live2D.html", "docs.openwebgal.com · 关于 Live2D",
     "WebGAL 官方文档 · 两个 js + game/figure 目录即可用 · 2026-10-11 核实"),
    (1232, "https://github.com/so0420/doro-live2d-web", "so0420/doro-live2d-web",
     "3★ · NOASSERTION · JavaScript · 推送 2026-08-27 · GitHub REST API 实测"),
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

    desc = ('第二十九辑三路调研（GitHub 8 组搜索去重后 413 条候选，关键词命中且未收录 296 条；'
            '中文站群 5 组；官方 2 组），本版取 18 项，主题 **Live2D × Agent 与开源编辑器**。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测，README 逐份 `gh api readme` 拉取核对。'
            '<strong>本辑主线：前三辑在答「不买 Editor 怎么凑合」，本辑第一次有人把两件事做实 ——'
            '① 编辑器本身被开源实现了（`umamoorg/umamo`，CMO3/MOC3 双向读写，兼容到 Cubism 5.4，'
            '但 alpha、无动画）；② 绑定被做成了「一个 JSON」给 agent 写与自证（`RevStudio/Rev2D`，'
            'MIT、2600+ 测试、18 个 MCP 工具，但 `.moc3` 不支持）</strong>。'
            '③ 同时「绕开 Editor」整件事的账变了：官方学生优惠三年 **$57.16**（中国区支持学信网验证码）。'
            '**上轮欠账 #4 闭环**：`Ariakage/live2d-agent-kit` 的 THIRD_PARTY_NOTICES 讲清了 psd2live 的 GPL 边界 —— '
            '传染的是工具代码，不是产出的模型文件。')

    block = ['    <div class="group" data-page-node-id="rpm34g">',
             '      <div class="group-title" data-page-node-id="rpm34gt">🆕 第三十四版增补 · Live2D × Agent 与开源编辑器：编辑器被开源了、绑定成了一个 JSON、以及学生优惠（18 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm34gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm34r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm34ra%s">%s</a> — %s</div>'
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
