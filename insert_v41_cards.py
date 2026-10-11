# -*- coding: utf-8 -*-
"""第四十一版增补：把第三十七辑「agent 长出身体 + 一条流水线的三处塌方被官方认领」的 24 个条目登记进 index.html。

三路候选：gh 路 32 条 / cn 路 24 条 / official 路 8 条（复核 17 条）。
与 `index.html`（1379 项）及全部历史存档机器比对，本版 24 条命中 **0**。

**本辑主线：① 「给 AI 装一个 Live2D 身体」从主张变成重复模式（Codex / Claude Code / DSH / 造一个 MCP 都有人做）；
② 官方论坛一轮认领三条：Unity 描画割り込み功能自带 bug、motion3.json 覆盖重导入崩、
   Unreal SDK 官方否认停摆（20 天后 beta2 落地闭环）；
③ 5.4 alpha 可用期「09-14 vs 10-18」的跨辑口径冲突本轮正式收口 = 10-18（09-14 是 alpha1 下线日）；
④ 中文侧本辑最硬的不是教程而是「纠纷金额」——法院把「精度不达标退稿」判成 7627 元付 4000。
⑤ 顺手完成上辑待办①：22 个改名仓库的 href + 显示名已就地更正（44 href / 23 脚注显示名 / 1 卡面名）。

数据来源：2026-10-11 GitHub REST API 逐条实测（★ / license / 语言 / 创建 / 推送 / 更新，主 agent 已把 32 个候选逐条复验，与子 agent 汇报零出入）。
幂等：已存在本版标记则跳过。
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1378"'
FOOTER_MARK = '  <footer data-page-node-id="rq7xrixbWVHwdFs2CDNYhJ">'
FIRST_NEW_FOOTNOTE = 1379
MARKER = "第四十一版增补"

HEAD_OLD = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11',
    '共 1379 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11 · 第四十一版增补 2026-10-11',
    '共 1403 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项 + 第四十一版增补 24 项（均与上版零重复）',
]

CARDS = [
    # ---------- A. agent × Live2D（本辑主线） ----------
    dict(
        nid="rpm41c1", name="daidai-live2d-pet —— 桌宠头顶弹「Codex / Claude Code 正在干什么」（★12）",
        url="https://github.com/Rosa134/daidai-live2d-pet",
        lang="JavaScript", stars="12",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="Electron 桌宠，**直接监听 Codex / Claude Code 的会话状态**，在角色头顶弹中文气泡，"
              "并按「思考 / 运行工具 / 回复 / 完成」四态切换模型动作。另有一套「陪伴模式」："
              "接 OpenAI 兼容接口 + 火山引擎 TTS + **RMS 口型同步** + 随机肢体动作。",
        analogy="上两辑有人提出「**你的桌宠不需要大脑**」——别给它装 AI，给它装身体。这一条就是**那句话的现成实现**："
                 "它自己不会聊天（陪伴模式是附加的），它干的事是**把 agent 的内部状态翻译成表情**。"
                 "同时开三四个 agent 跑长任务的人，最缺的就是「它们现在到哪一步了」这个可瞥一眼的界面。",
        ext=(72, "72", "两种模式都给足了扩展位：工作提醒模式的状态→动作映射是**一张表**，加一个宿主只要加一行；陪伴模式的 TTS/LLM 都是可替换后端。"),
        use=(80, "80", "MIT、开箱即用、有打包产物。**这是本辑 gh 路唯一标「落地」的桌宠**。"),
        src="创建 2026-06-03 · 推送 2026-07-25 · 更新 2026-07-25 · 12★ · MIT · JavaScript · 信源 [1379]",
    ),
    dict(
        nid="rpm41c2", name="dsh-live2d —— 把 Live2D 塞进 DSH 插件的官方挂载点（★0）",
        url="https://github.com/hacxy/dsh-live2d",
        lang="TypeScript", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="DSH 插件版 Live2D 桌宠：基于 `lrplrplrp/live2d` 改造，**砍掉对话框 / 小游戏 / 外部 API**，"
              "只留 DSH 状态驱动、拖拽缩放、眼睛跟随、实时推送，并深度集成 DSH 设置页。",
        analogy="它的价值不在代码量，在**它把「DSH 插件协议 → Live2D」这条接口走通了**，而且走的是公开挂载点"
                 "（`window.ModuleLoader + ctx.slots + webServer SSE`），第三方沙箱评级 **L5 运行时通过**。"
                 "换言之：想给 DSH 做一个 Live2D 身体，**照抄这个骨架就行**，不用自己猜插件 API。",
        warn="⚠️ 母本 `lrplrplrp/live2d` 最后推送 **2025-03-29**，比多数下游还旧；本仓自己也停在 2026-08-18。"
             "**当接口范本，别当依赖。**",
        ext=(55, "55", "DSH 插件体系仍在快速换版（本仓针对 dsh 0.1.2-alpha.1 验证），接口会漂。"),
        use=(60, "60", "★0，只对本机「DSH + 索引站」这条线有直接意义；主力价值是**协议样本**。"),
        src="创建 2026-08-18 · 推送 2026-08-18 · 更新 2026-09-11 · 0★ · MIT · TypeScript · 信源 [1380]",
    ),
    dict(
        nid="rpm41c3", name="xiaoya —— 「会听会说会行动」的中文数字人助手（★1）",
        url="https://github.com/kongweiguang/xiaoya",
        lang="TypeScript", stars="1",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="实时语音对话 + **自然打断** + Live2D 神态/口型同步 + 本地语音处理 + **MCP 工具扩展**，"
              "喊的口号是「让 AI 从回答问题走向完成任务」。",
        analogy="前面两条是「agent → 表情」的**单向管道**；这一条是**双向**的：Live2D 不只是状态指示灯，"
                 "而是**交互的界面**（你说话它听得见，它办事你能看见）。这是「Live2D 当 agent 的脸」这条命题最完整的一种提法。",
        warn="⚠️ 2026-10-07 才创建、★1，**当天仍在推**；别当依赖，当**架构参照**看。",
        ext=(70, "70", "实时语音（LiveKit）+ Live2D 口型 + MCP 三件套分层清楚，每件都能单独换。"),
        use=(35, "35", "太新，跑起来大概率要自己填坑；可抄的是**「神态 ⇄ 工具调用」的状态映射**。"),
        src="创建 2026-10-07 · 推送 2026-10-11 · 更新 2026-10-11 · 1★ · MIT · TypeScript · 信源 [1381]",
    ),

    # ---------- B. 桌宠宿主换代 ----------
    dict(
        nid="rpm41c4", name="bongo-cat-next —— Tauri 2 + Next.js 15 的现代猫咪桌宠（★151）",
        url="https://github.com/liwenka1/bongo-cat-next",
        lang="TypeScript", stars="151",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="Tauri 2 + Next.js 15 的 Live2D 猫咪桌宠，BongoCat 系**最有维护的那一支**："
              "pixi-live2d-display 渲染 + `rdev` 跨平台设备事件（键盘响应）+ 透明窗 + 点击穿透 + 多模型切换 + 托盘 + 全局热键 + 多窗口 + 中英 i18n。",
        analogy="BongoCat 这一族在索引里出现过好几次（多为 Electron 或纯网页）。这一支的区别是**把壳换成了 Tauri**："
                 "同样的透明窗 + 键鼠监听，安装包和常驻内存都小一截。**看「桌面宠物怎么正确地跟系统事件打交道」，这一支是当前最干净的样本。**",
        ext=(78, "78", "hooks 拆得很清楚（`_useCore` / `_useModelLoader` / `_useMotionPlayer` / `_useMouseEvents`），换模型或换动作逻辑都只动一个文件。"),
        use=(82, "82", "★151、MIT、结构清晰、还在推；是研究「Tauri 多窗口 + Live2D」的首选读物。"),
        src="创建 2025-06-12 · 推送 2026-08-16 · 更新 2026-09-26 · 151★ · MIT · TypeScript · 信源 [1382]",
    ),
    dict(
        nid="rpm41c5", name="Ark-Pets —— 本辑唯一千星通用桌宠框架，带平面重力场（★1124）",
        url="https://github.com/isHarryh/Ark-Pets",
        lang="Java", stars="1124",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="明日方舟主题桌宠 ArkPets：**平面重力场物理**（干员能被丢出去、会站在窗口边缘）+ 透明模式点击穿透 + 开机自启；"
              "实测**运行内存约 50–80MB**，模型库持续更新；仅 Windows（Mac/Linux 开发中）。",
        analogy="大多数桌宠是「贴在桌面上的图」。它把**物理**放了进来 —— 角色有重量、会被甩出去、会掉到别的窗口上。"
                 "而且这个体量只要 **50–80MB 内存**，对本机 16GB 的预算是很好的「桌宠常驻成本」基准线。",
        warn="⚠️ **GPL-3.0 传染**，自用无碍、做产品要想清楚；本体是 Java。",
        ext=(60, "60", "模型库与主题强绑定（明日方舟），换题材要自己重做一套角色资源。"),
        use=(70, "70", "低内存 + 物理交互的**体感基准**；★1124 说明这条路有人真的在用。"),
        src="创建 2022-09-15 · 推送 2026-09-26 · 更新 2026-10-11 · 1124★ · GPL-3.0 · Java · 信源 [1383]",
    ),
    dict(
        nid="rpm41c6", name="mea-pet-public —— Live2D 与 PNG 差分「一键切换」的双引擎桌宠（★44）",
        url="https://github.com/NekoHome-Studio/mea-pet-public",
        lang="Python", stars="44",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="Python + PyQt5 桌宠，**Live2D 与 PNG 差分两套渲染引擎可热切**：Live2D 走 WebGL 硬件加速，"
              "PNG 差分走逐帧绘制；接 AI 对话（Ollama / DeepSeek / MiMo）+ 日语 TTS + 记忆养成 + 屏幕观察吐槽。"
              "立绘量很大：**180+ 张立绘 / 18 种表情 / 5 套服装 / 2 种朝向**。",
        analogy="**「低配机的退路」是本条的题眼。** Live2D 好看但吃 GPU；这台机器 16GB、显卡一般，跑不动时的 Plan B 是"
                 "「PNG 差分逐帧」—— 立绘量堆够，观感也能接受，而且能耗几乎为零。它把这两条路做成一个开关，"
                 "等于把「渲染方式」降级成了配置项。",
        warn="⚠️ 作者自称早期项目、不完善；启动脚本走**清华镜像**装依赖（本机镜像一贯 403，可能要改源）。",
        ext=(65, "65", "「渲染引擎可热切」这个抽象本身可复用；AI/TTS 后端都是可替换模块。"),
        use=(55, "55", "功能面很全但完成度自述不高；**当作「双引擎切换」的设计参考**，不要当作可直接投产的桌宠。"),
        src="创建 2026-07-09 · 推送 2026-10-05 · 更新 2026-10-11 · 44★ · MIT · Python · 信源 [1384]",
    ),

    # ---------- C. 格式 / 逆向轮子 ----------
    dict(
        nid="rpm41c7", name="py-moc3 —— 纯 Python 读写 .moc3，零依赖、能读能写（★4）",
        url="https://github.com/Ludentes/py-moc3",
        lang="Python", stars="4",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-tool", "工具")],
        plain="纯 Python（仅标准库）的 `.moc3` 二进制**读写**库，发布在 PyPI（`pip install py-moc3`）。"
              "格式拆解写得很清楚：**64 字节头**（magic `MOC3` + 版本 + 端序）+ **640 字节段偏移表（160 × uint32）**"
              "+ 从第 1984 字节起约 100 个 64 字节对齐的 typed array（struct-of-arrays）。"
              "支持版本 **V3.00 / V3.03 / V4.00 / V4.02 / V5.00**，read→write 做到**字节级 round-trip**（自带 `moc3 verify`）。",
        analogy="**本辑对「维护索引站的个人」最有用的一条。** 前六辑一直卡在「不买 Cubism Editor 就读不了 moc3」，"
                 "于是每次想批量看一眼模型参数范围、改个 texture index，都要开 GUI 或者上重型轮子。"
                 "这个是**命令行 + 纯 Python + 零依赖**：`pip install` 完就能扫目录里几百个 moc3、导出参数清单。"
                 "注意它和「渲染 moc3」是两件事 —— 它不做渲染，只做**文件级读写**，所以没有任何图形栈负担。",
        ext=(75, "75", "有了读写就能做批处理（改路径、统一版本、抽元数据）；`moc3 verify` 还能当**文件完整性校验器**用。"),
        use=(78, "78", "零依赖 + PyPI 直装 + MIT。**本机当天就能用**。"),
        src="创建/推送 2026-04-08 · 更新 2026-08-25 · 4★ · MIT · Python · PyPI 0.1.0（周下载约 131–145）· 信源 [1385]",
    ),
    dict(
        nid="rpm41c8", name="live2d-tools —— 反着来：.moc3 还原成 PSD 或可编辑 .cmo3（★4）",
        url="https://github.com/alksdesu/live2d-tools",
        lang="C++", stars="4",
        tags=[("t-make", "建模"), ("t-tool", "工具")],
        plain="模型转换工具箱（原名 live2d2psd）：**每个 drawable 单独渲染成一层**导出 PSD，并保留原 Part 分组层级与命名；"
              "另一路从 moc3 二进制里**恢复几何 / 变形器 / 参数 / 物理**，生成可继续编辑的 `.cmo3`（CAFF 容器 + XML 序列化）。"
              "自带模型查看器（可开 `.model3.json` / `.moc3`，带变形器系统、参数面板、Pose 切换）。",
        analogy="上两辑的流水线是「PSD → 绑定 → moc3」的**正向**；这一条是**逆向**，救的是「**工程文件丢了、只剩运行时文件**」这种事故。"
                 "对上一条 `py-moc3` 是互补：那个负责「字节级读写」，这个负责「**语义级还原**」（把二进制还原成能继续编辑的工程）。",
        warn="⚠️ **无 LICENSE 文件**（默认保留全部权利）→ 先别商用。"
             "另注意：网页直取别名 `alksdesu/live2d2psd`，而 `gh api` 对该别名返回 **404（本机代理假阴性，非仓库不存在）**。",
        ext=(70, "70", "逆向链路的扩展空间大（能不能同时吐 Spine / 能不能批量转），但取决于作者是否继续维护。"),
        use=(45, "45", "抢救场景专用、无许可证、★4；**当备用工具登记**。"),
        src="创建 2026-05-10 · 推送 2026-07-13 · 更新 2026-09-24 · 4★ · **无许可证** · C++ · 信源 [1386]",
    ),
    dict(
        nid="rpm41c9", name="LumaStage —— ★1 但带一张「VTS 兼容性验收矩阵」（★1）",
        url="https://github.com/Lendic42/LumaStage",
        lang="TypeScript", stars="1",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="开源 VTuber studio（Windows/macOS 桌面端 + 局域网 iPhone Face ID 追踪），目标是与 VTube Studio 的模型文件**互操作**。"
              "仓库里的 `compatibility.md` 是一张**硬核验收矩阵**：逐行标注 Cubism 3/4/5 模型发现、"
              "VTS sidecar 的 parameter mapping / 表情热键 / 场景热键 / 插件 API 各自处于「Full / 兼容子集 / 尽力而为 / 计划中」，"
              "并在官方 Haru 样例与第三方模型上实测过。**明确声明不复制 VTS 代码、不解密受保护模型、不绕过作者限制。**",
        analogy="**它不是拿来跑的，是拿来抄的。** ★1 的仓库本身没什么用，但那张矩阵回答了做 Live2D 宿主时最贵的一个问题："
                 "「**我到底要兼容到什么程度才算兼容？**」—— 哪些必须 Full、哪些可以 Best effort，它替你排好了序。"
                 "这类「验收清单」在开源侧极稀缺，前几辑收的 `AutoLive2d` 也是因为同一理由被收。",
        warn="⚠️ ★1、GPL-3.0-only、最后推送 2026-07-18；**别期待它被维护**。",
        ext=(80, "80", "矩阵式兼容声明是一个可复制的**文档范式** —— 以后自己的项目也照这个格式写。"),
        use=(40, "40", "跑不了；但那张表的阅读价值超过很多能跑的仓库。"),
        src="创建/推送 2026-07-18 · 更新 2026-07-18 · 1★ · NOASSERTION（实为 GPL-3.0-only）· TypeScript · 信源 [1387]",
    ),
    dict(
        nid="rpm41c10", name="VTubeStudio（官方仓库）—— 整个生态的「事实标准接口」（★1313）",
        url="https://github.com/DenchiSoft/VTubeStudio",
        lang="C#", stars="1313",
        tags=[("t-make", "建模"), ("t-tool", "工具")],
        plain="⚠️ **这一仓不是 VTS 本体，是它的 API 文档 + 示例插件**。它定义了整个 Live2D VTuber 生态的事实标准接口："
              "模型加载 / 表情 / 动作 / 物理覆盖 / 参数注入 / 事件订阅。",
        analogy="把这个仓库当**接口规范**看，不当实现看。理由很直接：上一条 LumaStage 的兼容矩阵，"
                 "是**对着这套 API 写的**；BongoCat 系、桌宠系的「怎么把状态喂给模型」，最终也要跟这套参数名对齐。"
                 "**索引里第一次出现这条「标准本身」**，它补的是谱系缺口，不是工具缺口。",
        ext=(85, "85", "只要生态里还有人做 VTS 插件，这套 API 就是最稳的锚点；★1313 且 2026-09-28 仍在推。"),
        use=(50, "50", "你不需要它来跑东西；**需要它来对齐参数名**。"),
        src="创建 2019-11-11 · 推送 2026-09-28 · 更新 2026-10-11 · 1313★ · MIT · C# · 信源 [1388]",
    ),
    dict(
        nid="rpm41c11", name="inochi-session —— 全开源路线的配套宿主，但已停推 11 个月（★407）",
        url="https://github.com/Inochi2D/inochi-session",
        lang="D", stars="407",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="Inochi2D 官方的直播/串流应用，也就是「**完全开源 2D 木偶**」这条替代路线的配套宿主。"
              "用自己的 INP 绑定格式（模型要在 Inochi Creator 里做），**授权全开、无运行时费用**，Linux 原生一等公民。",
        analogy="这是索引里第一次把 Inochi2D 的**播放端**补齐 —— 之前只有创作端 `inochi-creator`。"
                 "但要注意一个**分裂状态**：创作端稳定版仍停 `v0.8.6（2024-09-18）`，而这个播放端最后推送是 **2025-11-08**，"
                 "**但核心库 `Inochi2D/inochi2d` 本轮仍有推送（2026-10-03，★1811）**。"
                 "也就是说：**底层在动、上层两端都在停**。",
        warn="⚠️ **最后推送 2025-11-08（约 11 个月未动）**。对「Cubism 许可有顾虑、想全开源」是唯一退路，但别指望活跃维护。",
        ext=(55, "55", "授权全开是最大优势（无运行时费用）；但生态小、格式私有（INP 不通用）。"),
        use=(45, "45", "许可洁癖场景的备选；日常用 Live2D 的话不需要它。"),
        src="创建 2021-07-11 · 推送 2025-11-08 · 更新 2026-10-10 · 407★ · BSD-2-Clause · D · 信源 [1389]",
    ),

    # ---------- D. 中文侧一手 ----------
    dict(
        nid="rpm41c12", name="easy-live2d v0.4.0 —— 「一行代码语音口型同步」（掘金）",
        url="https://juejin.cn/post/7624422672950149158",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="作者自己的更新说明：v0.4.0 内部几乎重写（单体 → monorepo）。卖点是**「5 行加载模型，1 行播语音口型」**："
              "`await sprite.playVoice({voicePath:'/sounds/hello.mp3'})` 就自动 RMS 口型。"
              "新增 **Cubism 3/4/5 全版本模型兼容**、修掉渲染冲突（Live2D 现在就是一个普通 Pixi Sprite）、"
              "新增 **Tauri 支持**、支持 **远程音频 URL**（可直接对接 TTS）。",
        analogy="**「TTS → 远程 URL → 一行口型」正好是本机「本地 Ollama 角色站」缺的那一块。** 前几辑做口型要么自己算 RMS，"
                 "要么接 VTS。这一版把「语音驱动嘴巴」压成了一个函数调用，而且模型不用改。"
                 "⚠️ 社区在评论区给出一条比正文更有信息量的情报：`guansss/pixi-live2d-display` **长期不维护、issue 无人回**，"
                 "所以有人转投这个库 —— 新旧技术选型的分水岭在这里。",
        warn="⚠️ **不打包 Cubism Core**（Live2D 政策所限）：要自己去官网下 `Live2D Cubism SDK for Web`，"
             "把 `Core/` 放进 `/packages/cubism/`。另：掘金本站**部分帖子会被风控拦**（同一篇 A1 就触发过 `X-TT-System-Error: 3`）。",
        ext=(80, "80", "已支持 Tauri（可做桌宠）、远程音频、Cubism 3/4/5；仓库 `Panzer-Jack/easy-live2d` 早已在索引 [r32]。"),
        use=(75, "75", "**本辑 cn 路唯一「自带 RMS 口型同步」的现成 Web 方案**，MIT 系、还在更新。"),
        src="掘金 · 作者自述 · 2025 · 正文 2026-10-11 取 · Core 需自取 · 信源 [1390]",
    ),
    dict(
        nid="rpm41c13", name="《从零开始的 Live2D 使用手册》—— 中文侧最长的手写总纲（NGA）",
        url="https://bbs.nga.cn/read.php?tid=25357826",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="本辑中文侧**最长、最完整**的手写手册。硬数字：**纹理图集一般 2048×2048 够用，最高可选 16834×16834**；"
              "导出 `.moc3` 时**为兼容选 SDK 3.3、以 1/1 大小输出**；免版**单模型图层数 ≤30**。"
              "物理功能区逐项释义：**入力/影响度每类总上限 100%**、长度越大摆得越慢、易晃度参考 **0.7~0.99**、收敛速度 >1 更快。"
              "还给了模型模板的授权口径（**个人势可商用，初音未来与 Unity 酱除外，禁 R18/R18G**）与四种面捕软件的导入路径。",
        analogy="**它相当于「纯手工路线」的中文总纲。** 对你尤其有用的一点：即便以后全走 AI 自动化，"
                 "**里面的数值区间仍然是校验基准** —— 比如「免版图层 ≤30」这条，正好能用来判断 AI 拆层的结果是不是超规格；"
                 "「影响度每类总上限 100%」也能当自动绑定的合法性断言。",
        warn="⚠️ 本机 **curl 直连 `bbs.nga.cn` 返回 403**（正文经搜索快照取得）；引用时以正文内容为准。",
        ext=(70, "70", "是「基准数字表」而不是教程：可以拿它的区间去做自动化结果的 sanity check。"),
        use=(80, "80", "免费、中文、成体系；**手上有它，很多零散教程可以不看**。"),
        src="NGA 论坛 · 2021-02 帖 · 繁体/简体混排 · 2026-10-11 取正文（curl 403，走快照）· 信源 [1391]",
    ),
    dict(
        nid="rpm41c14", name="法院把「模型精度不达标退稿」判成：7627 元付 4000，平台退 3627（搜狐）",
        url="https://www.sohu.com/a/1081564601_121138606",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="**本辑中文侧最重要的数字锚点。** ① 北京市海淀区人民法院 2026 年审结：原告**7627 元**定制虚拟主播 Live2D 模型，"
              "以精度不达标要求退稿退款；法院依《民法典》787 条认定定作人有**任意解除权**，但查明画师**已完成约八成工作量**，"
              "**酌情判原告支付报酬 4000 元、平台退还 3627 元** —— 「不满意 ≠ 全额退款」。"
              "② 米画师案例：委托方付 **669 元**细化虚拟服装，发现多处 AI 痕迹、画师拿不出任何草稿/过程文件，"
              "**平台仲裁认定原创性不足，取消画师资格并封号，669 元全额退回**。"
              "③ 法律口径：《消保法》55 条「退一赔三」（不足 500 补到 500）；另一案原告因**未存提示词/参数/修改过程**而败诉。",
        analogy="**这条不是教程，是「约稿双方的行为准则」。** 它把一件很抽象的事量化了：**「做完 80%」值 4000 元**。"
                 "对要外包的人是「验收节点要前置、过程文件要索取」；对做的人是「**做一点存一点**」—— 第二案输就输在拿不出过程证据。"
                 "**举证能力决定胜负**，这句话对双方都成立。",
        ext=(60, "60", "法律口径可迁移到所有「定制创作」场景（美术、配音、建模同构）。"),
        use=(85, "85", "**要外包或接单的人，这条的实操价值高于任何技术贴。**"),
        src="搜狐号 · 2026-09-28 · 2026-10-11 取正文（HTTP 200）· 信源 [1392]",
    ),
    dict(
        nid="rpm41c15", name="《约稿指南 · Live2D 篇》—— 可直接当 checklist 的雇方手册（AcFun）",
        url="https://www.acfun.cn/a/ac34532498",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="雇佣方视角的五条：① 先看模型师**作品展示**里的动作/表情是否达你要求；"
              "② 把想要的效果**在平台聊天里描述**（日后未达标可当维权证据）；"
              "③ **在原画草稿阶段**就让模型师确认拆分要求（有些模型师不做拆分，或拆分加钱）；"
              "④ **务必确认工程文件是否加钱**（「很多是直接 ×2」）；⑤ **提前告知会用哪个面捕软件**（普通摄像头 / 安卓 / iOS Face ID 差异大）。",
        analogy="**「草稿期确认拆分」「工程文件 ×2」「先报面捕软件」这三条，在本辑抓到的 7 个橱窗里全部被独立印证**，"
                 "说明它们是**行业通例而非个例**。这类「三条独立来源都成立」的条款，比任何单个教程的结论都可信。",
        ext=(50, "50", "是**流程清单**不是技术内容，本身没有扩展空间；价值在于把谈判点提前。"),
        use=(80, "80", "五条全是可执行动作，且在平台聊天里**留痕**这一点法律上很实在。"),
        src="AcFun · 2022-04-22 · Ichigo麻婆豆腐 · 2026-10-11 取正文（HTTP 200）· 信源 [1393]",
    ),
    dict(
        nid="rpm41c16", name="数万元定制的模型，被 300 元挂上 Etsy 卖了 36 笔（中国台湾 · 游戏角落）",
        url="https://game.udn.com/game/story/122089/9245705",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="中国台湾 VTuber「星の沛沛」发现自己**花费数万元**委制的形象，被以 **300 元**低价挂上 Etsy 贩售，"
              "**已上架约三个月、累计 36 笔交易**。接案工作室称是**合作建模师出走后的个人行为**，去年底已要求停售；"
              "但**模型仍持续出现在 Etsy、淘宝**，且**被盜賣的不只一件**。当事人宣布**永久停用该套模型**并下架相关直播内容。",
        analogy="这是「**工作室分包 → 建模师出走 → 模型流入二手市场**」的**完整责任链坏例**，而且链条上每一环都真实发生过。"
                 "对应上一条的法律结论：光有口头约定没用，**外包协议里必须写清转售禁令与违约后果**，"
                 "并且要留得住「谁在什么时间交付了什么」的证据。",
        warn="⚠️ 本机 **curl 直连 `game.udn.com` 返回 000**（超时），正文经其他通道取得；引用以正文为准。",
        ext=(40, "40", "是**风险案例**，没有可扩展的技术面；价值在于给外包协议提供真实反面教材。"),
        use=(65, "65", "只要你会外包或接单，这条就是必读；技术侧无内容。"),
        src="游戏角落（联合报系）· 中国台湾 · 2026-10-11 取正文 · 信源 [1394]",
    ),
    dict(
        nid="rpm41c17", name="米画师 4 个橱窗/企划：把「工程文件值多少钱」算出来（价格锚）",
        url="https://www.mihuashi.com/stalls/1346364",
        lang="橱窗", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="本辑从米画师抓到 4 个可交叉验证的价格样本（**同一平台不同建模师价差 >2 倍**）："
              "**① 高精建模 ¥3666**（全口型适配吐舌、全身物理、赠 5 贴图表情；图层 >500 与不对称**底价 ×1.2**；兽耳 200 / 兽尾 100）；"
              "**② 顶精建模 ¥3700**（已售 31 件、197 条评价、完成率 97%；**需工程文件 ×2**、加急 ×1.5、"
              "**交稿后小改 30 元/次、大改 50–100 元/次**、拆分 200–300）；"
              "**③ 特价橱窗 1500 起**（Q 版 800；按键表情 +30~50、兽耳 +90、兽尾 +50）；"
              "**④ 雇方企划 ¥800~1100（买断 + 必须给 `.cmo3` 工程）**。",
        analogy="**把 ① ② 和 ④ 摆在一起，能算出一个很少被公开的数字：工程文件大约值 2500–2900 元。**"
                 "（3666/3700 的橱窗**不给工程**，800–1100 的企划**必须给工程**。）"
                 "另外 ③ 的「兽耳 +90」对上 ① 的「兽耳 200」，说明**报价看人不看平台** —— 同平台能差一倍多。"
                 "最后一条最实用：**「交稿后小改 30 / 大改 50–100」是本辑唯一把「售后成本」量化的橱窗**。",
        ext=(35, "35", "价格锚本身不可拓展；但它给出的「验收维度清单」（九轴角度、口型条数、物理段数）可以拿来写自己的需求书。"),
        use=(70, "70", "要外包时的**预算校准器**；也是理解「工程文件为什么贵」的最短路径。"),
        src="米画师橱窗/企划 4 处（stalls/1346364 · 109695 · 737745 · projects/11751348）· 2026-10-11 取 · 信源 [1395]",
    ),
    dict(
        nid="rpm41c18", name="B 站工房 3 个橱窗：一条龙 3500/4300/5000 与「不对称 ×1.5」（价格锚）",
        url="https://gf.bilibili.com/item/detail/1100725007",
        lang="橱窗", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="B 站工房三例：**①「立绘＋拆分＋建模」一条龙 ¥3500 / 组合 ¥4300 / 顶精 ¥5000**（含 3–5 个按键表情、"
              "工期 30 天内、**默认可商用不加收**；VB 全套 300）；"
              "**② 常驻建模 ¥800（粉丝 ¥600）**（不对称/坐姿等特殊角度 **×1.5**；额外换发型 100、服饰 300；**只给运作档不给工程**）；"
              "**③ 排稿 ¥4200（粉丝 4000）**（**X 轴 35 度往上最高 60、Y 轴 30 度往上**；"
              "含 VB 嘴/果冻眼/眉眼联动/**嘴型基础 44**；加急 ×2、**需工程文件 ×2**）。",
        analogy="**「不对称」这个加成项跨平台口径不一，很有意思**：B 站这边是 **×1.5**，米画师那边是 **×1.2**。"
                 "同一个物理上一样的改动，不同平台差 25 个百分点 —— 说明**没有行业统一价，只有各家自己的定价惯例**。"
                 "另外 ③ 给出的「**嘴型基础 44**」是本辑唯一量化「口型条数」的样本，对照 ① 米画师的「3× 口型」与「3×4」，"
                 "**「口型数」其实是一个公开可比、却极少被写在需求书里的验收维度**。",
        ext=(35, "35", "同上：价格不可拓展，但「验收维度」可抽取（角度上限、口型条数、加急倍数）。"),
        use=(70, "70", "与上一条互为交叉验证；B 站工房的「一条龙」报价是**画师+建模一体**的少见样本。"),
        src="哔哩哔哩工房 3 处（item/detail/1100725007 · 1104727036 · mall itemsId=1100516069）· 2026-10-11 取 · 信源 [1396]",
    ),
    dict(
        nid="rpm41c19", name="给网站加 Live2D 看板娘：三条必踩的坑（博客园）",
        url="https://www.cnblogs.com/fengbohan/p/18913452/add-live2d-kanswer-to-the-website-zx5hws",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-tool", "工具")],
        plain="WordPress + Sakurairo 主题实测，一行 CDN 接入 `live2d-widgets`。**三条踩坑清单**："
              "① 刷新没看板娘 → 先等半分钟，或 **`fastly.jsdelivr.net` 被墙**（在浏览器直接访问那个 `autoload.js` 就能判定）；"
              "② 本地引入要把 `dist/autoload.js` 第 8–9 行的 `live2d_path` 改成自己域名路径，**末尾 `/` 必须加**；"
              "③ 增删模型改 `dist/waifu-tips.json`，关键字段是 `paths`（须为 `model.json` 或 `model3.json`）。"
              "另给 jsdelivr 加速格式 `https://cdn.jsdelivr.net/gh/用户/仓库@版本/路径`。",
        analogy="**这三条全是「静默失败」。** 尤其第 ① 条：CDN 被墙时页面不报错、控制台也不一定红，"
                 "只是模型不出来 —— 没有清单就得盲猜。这一类「**不报错但不对**」的坑，正好是本项目一直在记的那类（M-0008 家族）。",
        ext=(60, "60", "`live2d-widget` 本体是 GPL-3.0（索引已有卡）；这条只补**使用姿势与排错**。"),
        use=(78, "78", "三条直接抄；如果哪天要在索引站或别处挂看板娘，这条就是排错顺序表。"),
        src="博客园 · 博涵 · 2025-06-06 · 2026-10-11 取正文（HTTP 200）· 信源 [1397]",
    ),
    dict(
        nid="rpm41c20", name="《如何画出标准 VTuber Live2D 立绘 + 拆图》—— 画师兼建模者的一手细则（中国台湾）",
        url="https://moonku44.com/live2d-psd/",
        lang="文章", stars="cn",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="作者**既是画师也是建模者**（非聚合站）。画布规范：**A4 / 300–350 dpi / RGB 8bit / sRGB / 最长边约 4000 px（头身比大可到 6000）**；"
              "须画**纯正面**立绘、善用对称尺。拆分细到眼=高光/眼褶阴影/上睫毛/上眼皮/上眼线/眼球/眼白/下睫毛/下眼线/下眼皮；"
              "嘴=上唇+遮盖皮肤/上牙/下牙/口腔内/舌头/下唇+遮盖皮肤/下唇阴影；**脖子要延长到嘴巴高度**（抬头需要延伸）。"
              "交档六查：线条与上色合并、涂层点阵化并合并、**图层模式改「通常」、透明度设 100%**、检查同名图层与杂点。",
        analogy="**它是「验收清单」而不是教程。** 上一辑收过一份简版（画手向 30 分钟版），"
                 "这一份是**粗/细两档里的细档** —— 拆分粒度到「上眼皮 / 下眼皮分开」，交档要求到「图层模式必须改通常」。"
                 "这两样都是**出问题时才会发现的隐性规格**（图层模式不对，导入后颜色就变了）。",
        warn="⚠️ 本机 **curl 返回 406**（拒绝），正文经其他通道取得；引用以正文为准。",
        ext=(55, "55", "内容可直接写进约稿规格书；不含工具链，扩展性一般。"),
        use=(80, "80", "要外包或自己画时的**交档标准**，与 A6/A7 的简版互为粗细两档。"),
        src="moonku44（中国台湾 · 一手博客）· 2025-04-14 内容大更新 · 2026-10-11 取正文 · 信源 [1398]",
    ),

    # ---------- E. 官方一手 ----------
    dict(
        nid="rpm41c21", name="官方认领 bug①：Unity 里模型压不过 Sprite —— 「描画割り込み機能」现不具合",
        url="https://creatorsforum.live2d.com/t/3991",
        lang="官方论坛", stars="ofc",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="用户报：Unity 里 Live2D 模型 prefab 的 `Order in Group` 与 Sprite 的 `Order in Layer` 各设 500 / -500、"
              "又给 Z 坐标拉开差距，**Scene 与 Game 视图里 Sprite 仍然盖在模型前面**。"
              "官方 2026-10-07 回复：`Cubism 5 SDK for Unity R5 以降`要在模型网格之间夹别的对象，"
              "要用**「描画割り込み機能（Z-Interlocking）」**；"
              "**`ただし、描画割り込み機能は現在不具合がございます。こちらは次回のリリースで修正いたします`**。",
        analogy="**这条的价值是「省掉一整轮盲调」。** 「怎么调都反」是 Unity 里最耗时间的一类问题，"
                 "官方直接指定了唯一通路（R5+ 的描画割り込み機能），并且**承认它现在有 bug、下个版本才修**。"
                 "所以现阶段正确的决策是：**别把「模型与背景 Sprite 之间的图层穿插」当可交付项**，等官方修。",
        ext=(45, "45", "属 SDK 侧缺陷，用户只能规避；R5 以下没有这个功能，老版本连规避通路都没有。"),
        use=(75, "75", "做 Unity 集成的人必读；本机不走 Unity 的话记「结论」即可。"),
        src="官方论坛 creatorsforum · 2026-10-05 提问 → 2026-10-07 官方回复 · 2026-10-11 取 · 信源 [1399]",
    ),
    dict(
        nid="rpm41c22", name="官方认领 bug②：用「参数变多」的 motion3.json 覆盖重导入 → 数组越界崩",
        url="https://creatorsforum.live2d.com/t/3978",
        lang="官方论坛", stars="ofc",
        tags=[("t-make", "建模"), ("t-warn", "注意")],
        plain="用户环境 `Cubism 5 SDK for Unity R4 / Windows 11 / Unity 2022.3.62f2`。"
              "**用同名、但参数/曲线数变多的新 `motion3.json` 覆盖重导入后**，抛："
              "`System.IndexOutOfRangeException ... at Live2D.Cubism.Framework.MotionFade.CubismFadeMotionData.CreateInstance(...)`。"
              "官方 2026-09-30：`確認したところ、こちらは Cubism SDK の不具合になります`，会在后续更新修。",
        analogy="**这是一条可以直接照做的规避规则**：覆盖前**先删旧的 `.fade.asset`**，或者干脆新建工程导入。"
                 "为什么值得单独记：它描述的是**「同名文件 + 内容变多」**这种极常见的迭代方式 —— "
                 "做模型一定会遇到「改完动作再覆盖」，而崩溃发生在**运行时**而不是导入时，很难往「覆盖」这个方向想。",
        ext=(45, "45", "SDK 侧缺陷；规避动作明确（删 .fade.asset / 新工程）。"),
        use=(78, "78", "Unity 集成方必读；非 Unity 路线也可记住「同名覆盖有风险」这个模式。"),
        src="官方论坛 creatorsforum · 2026-09-17 提问 → 2026-09-30 官方回复 · 2026-10-11 取 · 信源 [1400]",
    ),
    dict(
        nid="rpm41c23", name="官方否认「Unreal SDK 停摆」，20 天后 beta2 落地闭环",
        url="https://creatorsforum.live2d.com/t/3973",
        lang="官方论坛", stars="ofc",
        tags=[("t-make", "建模"), ("t-tool", "工具")],
        plain="用户 2026-09-08 问：Unreal 版 SDK 更新停在 2025-05-29，是不是不打算支持了？"
              "官方(`nakayasu_staff`) 2026-09-09 回："
              "**`Unreal Engine 向け SDK の今後のサポートにつきまして、開発・サポートを停止する予定はございません。現在、次期アップデートのリリースに向けて開発を進めております。`**"
              "—— 而它的「次期アップデート」就是 **20 天后（2026-09-29）发布的 `5-r.1-beta.2`**。",
        analogy="这是一条**闭环证据**：官方说「没停、在做下个版本」→ 20 天后版本真的发了。"
                 "对「要不要选 Unreal 路线」这类决策，最怕的就是「没人明说它死没死」；这一帖把口径钉死了。"
                 "同时它也是本项目的口径纪律样本：**「没更新」不等于「停了」**，要先问再下结论。",
        ext=(80, "80", "路线选择更明确（Unreal 可继续等）；也说明官方论坛是拿**路线级承诺**的有效渠道。"),
        use=(40, "40", "本机不碰 Unreal；但「**停更 ≠ 停摆**」这条判断纪律对任何依赖都适用。"),
        src="官方论坛 creatorsforum · 2026-09-08 提问 → 2026-09-09 官方回复 · 关联 Unreal `5-r.1-beta.2`(09-29) · 信源 [1401]",
    ),
    dict(
        nid="rpm41c24", name="⭐跨辑口径冲突收口：5.4 alpha 可用期是 **10-18**，不是 09-14",
        url="https://creatorsforum.live2d.com/t/3976",
        lang="官方论坛", stars="ofc",
        tags=[("t-make", "建模"), ("t-warn", "注意"), ("t-new", "新")],
        plain="**本辑解决了一个连续两辑悬着的口径冲突。** 官网 5.4 公告页两处原话是 "
              "`Available until \"October 18, 2026.\" After this date, the alpha version will no longer be available.` "
              "→ **整条 alpha 线的可用期 = 2026-10-18**；"
              "同页另一句 `Please note that alpha1 will no longer be available after September 14, 2026.` "
              "→ **09-14 只是 `alpha1` 的单独下线日**。本页官方回复(`enoko_staff`, 2026-09-17)复证同一口径："
              "`alpha1 は「2026年9月14日」まで利用可能で、期限が過ぎると使用できなくなる`。"
              "另：官方明确 **alpha 版没有「前方兼容」** —— 用 5.4 alpha2 存过的工程，**5.3 打不开也编辑不了**（`前方互換には対応しておらず`）。",
        analogy="**「09-14」这个数字之所以会跑偏，是因为它读起来像整条线的期限，实际只是其中一个版本的下线日。**"
                 "这正是本项目反复撞的那类错：**同一个数字出现在两个层级上**（整条线 vs 单个版本），"
                 "拿错了层级就会在下一轮被当成「已过期」而误判。"
                 "附带结论同样重要：**alpha 工程是单向门** —— 存了就回不去 5.3，想试 alpha 必须先备份、另存工程名。",
        ext=(60, "60", "口径已收口；后续复测条件 = alpha 线出现 alpha3 或 beta。"),
        use=(80, "80", "**要试 5.4 alpha 的人必读**：可用期是 10-18，且工程不可回退。"),
        src="官方论坛 creatorsforum · 2026-09-16 提问 → 2026-09-17 官方回复 · 官网公告页交叉复证 · 信源 [1402]",
    ),
]

FOOTNOTES = [
    (1379, "https://github.com/Rosa134/daidai-live2d-pet", "Rosa134/daidai-live2d-pet",
     "12★ · MIT · JavaScript · 创建 2026-06-03 · 推送/更新 2026-07-25 · REST 实测 · 内置 Codex / Claude Code 状态气泡，MIT 可自由改"),
    (1380, "https://github.com/hacxy/dsh-live2d", "hacxy/dsh-live2d",
     "0★ · MIT · TypeScript · 创建/推送 2026-08-18 · 更新 2026-09-11 · REST 实测 · ⚠️ 母本 `lrplrplrp/live2d` 最后推送 2025-03-29，比下游还旧"),
    (1381, "https://github.com/kongweiguang/xiaoya", "kongweiguang/xiaoya",
     "1★ · MIT · TypeScript · 创建 2026-10-07 · 推送/更新 2026-10-11 · REST 实测 · LiveKit 实时语音 + Live2D 口型 + MCP 工具"),
    (1382, "https://github.com/liwenka1/bongo-cat-next", "liwenka1/bongo-cat-next",
     "151★ · MIT · TypeScript · 创建 2025-06-12 · 推送 2026-08-16 · 更新 2026-09-26 · REST 实测 · ⚠️ 同名 `cherrol/bongo-cat-next` 为 fork(true)，只收本体"),
    (1383, "https://github.com/isHarryh/Ark-Pets", "isHarryh/Ark-Pets",
     "1124★ · GPL-3.0 · Java · 创建 2022-09-15 · 推送 2026-09-26 · 更新 2026-10-11 · REST 实测 · 实测运行内存约 50–80MB；仅 Windows"),
    (1384, "https://github.com/NekoHome-Studio/mea-pet-public", "NekoHome-Studio/mea-pet-public",
     "44★ · MIT · Python · 创建 2026-07-09 · 推送 2026-10-05 · 更新 2026-10-11 · REST 实测 · Live2D 与 PNG 差分双引擎热切"),
    (1385, "https://github.com/Ludentes/py-moc3", "Ludentes/py-moc3",
     "4★ · MIT · Python · 创建/推送 2026-04-08 · 更新 2026-08-25 · REST 实测 · PyPI `py-moc3` 0.1.0（周下载约 131–145）· 零依赖，read→write 字节级 round-trip"),
    (1386, "https://github.com/alksdesu/live2d-tools", "alksdesu/live2d-tools",
     "4★ · **无许可证** · C++ · 创建 2026-05-10 · 推送 2026-07-13 · 更新 2026-09-24 · REST 实测 · ⚠️ 别名 `live2d2psd` 经 `gh api` 返回 404（本机代理假阴性，非不存在）"),
    (1387, "https://github.com/Lendic42/LumaStage", "Lendic42/LumaStage",
     "1★ · NOASSERTION（实为 GPL-3.0-only）· TypeScript · 创建/推送/更新 2026-07-18 · REST 实测 · 价值在 `compatibility.md` 那张 VTS 兼容性验收矩阵"),
    (1388, "https://github.com/DenchiSoft/VTubeStudio", "DenchiSoft/VTubeStudio",
     "1313★ · MIT · C# · 创建 2019-11-11 · 推送 2026-09-28 · 更新 2026-10-11 · REST 实测 · **不是 VTS 本体，是 API 文档 + 示例插件**"),
    (1389, "https://github.com/Inochi2D/inochi-session", "Inochi2D/inochi-session",
     "407★ · BSD-2-Clause · D · 创建 2021-07-11 · 推送 2025-11-08 · 更新 2026-10-10 · REST 实测 · ⚠️ 已约 11 个月未推送；核心库 Inochi2D/inochi2d 仍有推送（2026-10-03，★1811）"),
    (1390, "https://juejin.cn/post/7624422672950149158", "掘金《easy-live2d v0.4.0 — 全面进化的 Live2D Web 开发体验》",
     "cn 路 · 作者自述 · 「5 行加载模型、1 行播放语音口型同步」`playVoice()` 自动 RMS；新增 Cubism 3/4/5 兼容、Tauri 支持、远程音频 URL；评论区内 MooreThreads 工程师称 pixi-live2d-display 长期不维护"),
    (1391, "https://bbs.nga.cn/read.php?tid=25357826", "NGA《[科普] 从零开始的 Live2D 使用手册》",
     "cn 路 · 2021-02 · Elegetic aka. 羽久藍月夜 · 纹理图集 2048²（上限 16834²）· 导出选 SDK 3.3 · 免版图层 ≤30 · 影响度每类总上限 100% · 易晃度 0.7–0.99 · ⚠️ 本机 curl 403，正文走快照"),
    (1392, "https://www.sohu.com/a/1081564601_121138606", "搜狐《画师自曝偷偷用 AI 接稿圈钱，委托方花钱能要求退一赔三吗》",
     "cn 路 · 2026-09-28 · 海淀法院 2026 年判：7627 元定制 → 画师已完成约八成 → 判委托人付报酬 4000 元、平台退 3627 元；米画师 669 元 AI 案全额退回 + 封号"),
    (1393, "https://www.acfun.cn/a/ac34532498", "AcFun《约稿指南 · Live2D 篇 — 如何获得你想要的 Live2D 效果》",
     "cn 路 · 2022-04-22 · Ichigo麻婆豆腐 · 草稿期确认拆分 / 工程文件常「×2」/ 先报面捕软件（普通摄像头 vs 安卓 vs iOS Face ID）"),
    (1394, "https://game.udn.com/game/story/122089/9245705", "游戏角落（中国台湾）《VTuber 花数万买断 Live2D 模型，竟被以 300 元当公用模型盗卖》",
     "cn 路 · 中国台湾 · 定制模型被 300 元挂 Etsy、上架约三个月 36 笔交易；工作室称系合作建模师出走个人行为；⚠️ 本机 curl 000（超时）"),
    (1395, "https://www.mihuashi.com/stalls/1346364", "米画师 4 处价格锚（stalls/1346364 · 109695 · 737745 · projects/11751348）",
     "cn 路 · 高精 ¥3666 / 顶精 ¥3700（需工程 ×2、交稿后小改 30 大改 50–100）/ 特价 1500 起（Q 版 800、兽耳 +90）/ 企划 ¥800–1100 买断且**必须给 .cmo3** → 反推「工程文件约值 2500–2900 元」"),
    (1396, "https://gf.bilibili.com/item/detail/1100725007", "B 站工房 3 处价格锚（1100725007 · 1104727036 · mall itemsId=1100516069）",
     "cn 路 · 一条龙 ¥3500/4300/5000（默认可商用不加收）· 常驻 ¥800（不对称 ×1.5，只给运作档）· 排稿 ¥4200（X 轴 35–60°、Y 轴 30°+、嘴型基础 44、加急 ×2）"),
    (1397, "https://www.cnblogs.com/fengbohan/p/18913452/add-live2d-kanswer-to-the-website-zx5hws", "博客园《给网站添加 live2d 看板娘》",
     "cn 路 · 2025-06-06 · 三条静默失败：fastly.jsdelivr.net 被墙（页面不报错）/ `live2d_path` 末尾 `/` 必须加 / `waifu-tips.json` 的 `paths` 须为 model.json 或 model3.json"),
    (1398, "https://moonku44.com/live2d-psd/", "moonku44《如何画出一个标准 VTuber Live2D 立绘 + 拆图教学》（中国台湾一手）",
     "cn 路 · 2025-04-14 大更新 · A4 / 300–350dpi / 最长边约 4000px（可到 6000）· 拆分到上/下眼皮分立 · 交档六查（图层模式改「通常」、透明度 100%、点阵化合并）· ⚠️ 本机 curl 406"),
    (1399, "https://creatorsforum.live2d.com/t/3991", "官方论坛《Unity 中 Sprite 显示顺序压不过模型》",
     "official 路 · 2026-10-05 提问 → 2026-10-07 官方回复 · **R5 起用「描画割り込み機能」，且官方承认该功能「現在不具合」、下个 release 才修**"),
    (1400, "https://creatorsforum.live2d.com/t/3978", "官方论坛《覆盖重导入 motion3.json 后 IndexOutOfRangeException》",
     "official 路 · 2026-09-17 提问（Unity R4 / Win11 / Unity 2022.3.62f2）→ 2026-09-30 官方认领为 **SDK 不具合** · 规避：覆盖前删旧 `.fade.asset` 或新建工程"),
    (1401, "https://creatorsforum.live2d.com/t/3973", "官方论坛《Unreal 向け SDK の更新が停止》",
     "official 路 · 2026-09-08 提问 → 2026-09-09 官方 `nakayasu_staff` 明确「**開発・サポートを停止する予定はございません**」→ 20 天后 `5-r.1-beta.2`（09-29）落地闭环"),
    (1402, "https://creatorsforum.live2d.com/t/3976", "官方论坛《急需回退 5.4 alpha1》+ 官网 5.4 alpha 公告页",
     "official 路 · **本轮口径收口**：官网两处原话 `Available until \"October 18, 2026.\"` = 整条 alpha 线可用期 **10-18**；`September 14, 2026` 仅指 **alpha1** 下线日（官方 2026-09-17 复证）。另：alpha 版**无前方兼容** —— alpha2 存的工程 5.3 打不开"),
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

    # ⚠️ 脚注只放最后一个旧脚注之后（沿用既有规则）；不做位置迁移（见本轮待办①）
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

    desc = ('第三十七辑三路调研（gh 路 32 条 / cn 路 24 条 / official 路 8 条新增 + 17 条口径复核），本版取 24 项，'
            '主题 **「AI 长出身体 + 一条流水线的塌方被官方认领」**。'
            '所有 ★ / 许可证 / 语言 / 创建·推送·更新日全部走 GitHub REST API 逐条实测（子 agent 报的 32 个候选已由主 agent 逐条复验，零出入）。'
            '<strong>本辑主线：① 「给 AI 装一个 Live2D 身体」从上一辑的**架构主张**变成**重复模式** —— '
            'Codex / Claude Code 状态气泡（daidai-live2d-pet）、DSH 插件版（dsh-live2d）、'
            '以及把「Live2D 当交互界面而非指示灯」的双向实现（xiaoya）同时出现；'
            '② 官方论坛一轮**认领三件事**：Unity 里模型压不过 Sprite 是指定的「描画割り込み機能」且**该功能现在不具合**、'
            '覆盖重导入 `motion3.json` 触发 `IndexOutOfRangeException` 属 **SDK 不具合**、'
            '以及**否认 Unreal SDK 停摆**（20 天后 beta2 落地闭环）；'
            '③ **跨辑口径冲突正式收口**：5.4 alpha 可用期 = **2026-10-18**（09-14 只是 alpha1 的下线日）；'
            '④ **格式线终于有了不做渲染的纯 Python 读写器** `py-moc3`（零依赖、字节级 round-trip），'
            '与逆向方向的 `live2d-tools`（moc3 → PSD / 可编辑 .cmo3）互补；'
            '⑤ 中文侧本辑最硬的不是教程而是**纠纷金额** —— 法院把「精度不达标退稿」判成 7627 元付 4000，'
            '配上 7 个橱窗/工房价格锚，第一次能反推出「工程文件约值 2500–2900 元」。</strong>'
            '️ 另有两条谱系补全：VTubeStudio 官方仓（**API 事实标准本身**）与 Inochi2D 的播放端 `inochi-session`。')

    block = ['    <div class="group" data-page-node-id="rpm41g">',
             '      <div class="group-title" data-page-node-id="rpm41gt">🆕 第四十一版增补 · AI 长出身体：三处塌方被官方认领 + 中文侧第一次量化「纠纷金额」（24 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm41gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm41r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm41ra%s">%s</a> — %s</div>'
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
    print("   页头：1379 → 1403 项；卡片 1362 → %d" % (1362 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
