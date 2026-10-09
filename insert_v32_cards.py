# -*- coding: utf-8 -*-
"""第三十二版增补：把第二十七辑「Live2D 深化」的 16 个条目登记进 index.html。

本辑候选池约 112 条（GitHub 32 / 中文社媒 23 / 官方与海外 57），
GitHub 路 32 个仓库全部走 `gh api repos/<r>` 实测，与上一辑（第二十六辑）零重复。

**本辑主线：上一辑说「Live2D 的钱花在拆图上」，这一辑发现更准确的说法是——
钱花在 Editor 授权上，而 Editor 买的其实是「绑骨」这一件事；渲染用的 Core 是免费下载的。**
于是本辑的票全投给了「绕开 Editor 也能干活」的东西：
用 Python 读写 motion3（不用 Editor 就能编动作）、用 Python 直接跑运行时（不用前端）、
以及官方自己出的、用深度学习做「素材分け」的 Photoshop 插件（唯一无版权风险的 AI 路径）。

**另一条主线是排错**：本轮拿到的一手报错（纹理集未生成 / core 版本不统一 /
Cubism 5 的 moc3 第三方库不吃 / 16GB 内存导出 OOM）比教程值钱得多。

**本机实测一条（上轮欠账 #2 的部分闭环）**：Ren'Py 8.5.3 SDK 自带
`renpy/gl2/live2d.py` + `live2dcsm.pxi`，官方文档原话「Ren'Py supports Live2D animations
in the Cubism 3, 4 and 5 formats」；`config.gl2 = True`（`renpy/config.py:1050`）；
`has_live2d()` 用 try/except 优雅降级。**但** `lib/` 下没有 `Live2DCubismCore.dll`
（`live2d.py:67` 会去找它）→ 必须先按文档把 `CubismSdkForNative-5-r.1.zip` 放进 SDK 目录，
再用 launcher 的「Install Live2D Cubism SDK for Native」装一次，否则 `has_live2d()` 恒为 False。

数据来源：2026-10-10 GitHub REST API 实测 + WebFetch 一手页面（`_r27/`）。
幂等：已存在标记则退出 0。
用法：python insert_v32_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1182"'
FIRST_NEW_FOOTNOTE = 1183
MARKER = "第三十二版增补"

HEAD_OLD = [
    '数据抓取：2026-09-09 · 第三十一版增补 2026-10-10',
    '共 1183 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-09-09 · 第三十二版增补 2026-10-10',
    '共 1199 个项目',
    '第二十九版增补 12 项 + 第三十版增补 15 项 + 第三十一版增补 15 项 + 第三十二版增补 16 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm32c1", name="live2d-py（把 Live2D 运行时搬进 Python：不用写前端）",
        url="https://github.com/EasyLive2D/live2d-py",
        lang="C++", stars="576",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="用 Python 扩展直接封装 **Live2D Native SDK**，在 Pygame / PySide6 / GLFW 这类"
              "OpenGL 窗口里加载并驱动模型，同时支持 Cubism 2.1 与 3.0+。",
        analogy="上一辑给你的是「网页里显示 Live2D」的零件（要懂 JS）；"
                "这条是把同一件事**装进 Python 的壳子里**——你会 Python，就等于已经会用它了。",
        warn="**不含 Cubism Core 与 Framework**，需自己从官网下载（**Core 免费**）；"
             "源码编译要 C++17 + CMake 3.26 + Python 3.11+。",
        ext=(90, "9.0/10", "接 Ollama 的最短通路：qwen3 出文本 → 自己写「情绪 → 参数名」映射 → "
                           "SetParameterValue 推表情；比整套 Web 前端轻一个数量级"),
        use=(85, "8.5/10", "本辑对用户画像适配度最高的一条；2026-09-30 仍在推送 · MIT · ⚠️ 未本机编译过"),
        src="推送 2026-09-30 · 576★ · MIT · C++ · 信源 [1183]",
    ),
    dict(
        nid="rpm32c2", name="live2d-motion3（不买 Cubism Editor 也能编动作）",
        url="https://github.com/EasyLive2D/live2d-motion3",
        lang="Python", stars="31",
        tags=[("t-make", "建模"), ("t-warn", "星少但有用")],
        plain="纯 Python 读写 `motion3.json`，带一个 PySide6 曲线编辑器，还能用 matplotlib "
              "把动作曲线画出来看。",
        analogy="Pro 授权买的是 Editor 这个**整体**；这个项目把其中「做动作」那一块"
                "**拆成了三个 Python 脚本**——你只缺做动作的话，就不必为整套买单。",
        warn="依赖 PySide6 + live2d-py + matplotlib，Python 3.10+；项目 2026-05 后未再推送。",
        ext=(88, "8.8/10", "与上一张卡同一作者、上下游关系：它编动作 → live2d-py 播放；"
                           "四种插值段（直线/三次贝塞尔/水平）齐全"),
        use=(82, "8.2/10", "**直接补上「预算有限」的最大缺口**；star 低不代表价值低，⚠️ 未本机实测"),
        src="推送 2026-05-15 · 31★ · MIT · Python · 信源 [1184]",
    ),
    dict(
        nid="rpm32c3", name="RenpyLive2DEyeFollowDemo（Ren'Py 8 时代的眼随+点击换动作）",
        url="https://github.com/rc14193/RenpyLive2DEyeFollowDemo",
        lang="Ren'Py", stars="4",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="Ren'Py + Live2D 下让**模型眼睛跟着鼠标走**、点击时切换动作的演示工程。",
        analogy="眼睛跟随和点击反馈是视觉小说里**性价比最高的两种「活起来」**——"
                "不需要绑骨、不需要动捕，只要模型有这两个参数就能做。",
        warn="只有 4 星、demo 级规模；2025-09-26 后未再推送。",
        ext=(80, "8.0/10", "填上一辑 renpy-live2d（2021 停更）留下的空档，证明 Ren'Py 8 时代仍有人在做"),
        use=(86, "8.6/10", "许可干净（MIT）、年份新、与用户栈 100% 对口、改动量小；.rpy 可直接抄"),
        src="推送 2025-09-26 · 4★ · MIT · Ren'Py · 信源 [1185]",
    ),
    dict(
        nid="rpm32c4", name="RenpyLive2DTraceSample（Ren'Py ← 外部进程 的接线图）",
        url="https://github.com/kojimio/RenpyLive2DTraceSample",
        lang="Ren'Py", stars="1",
        tags=[("t-make", "建模"), ("t-warn", "demo 级")],
        plain="用 Pymouth（口型）+ OpenSeeFace（免费面捕）通过**端口通信**驱动 Ren'Py 里的 "
              "Live2D 模型。",
        analogy="与其说它是成品，不如说它是一张**拓扑图**：外部程序算好动作数据 → 走端口 → "
                "Ren'Py 收下。把 Ollama 塞进同一个端口协议，就是「本地 LLM 驱动立绘」。",
        warn="1 星、2025-07 后未更新，工程规模是 demo 级；但 Apache-2.0 是同类里最宽松的。",
        ext=(84, "8.4/10", "对想接 Ollama 的人，这张图比代码值钱"),
        use=(70, "7.0/10", "当作架构参考抄思路，不要当成品依赖"),
        src="推送 2025-07-04 · 1★ · Apache-2.0 · Ren'Py · 信源 [1186]",
    ),
    dict(
        nid="rpm32c5", name="seethrough-live2d-pipeline（把 AI 粗分层修到能绑骨）",
        url="https://github.com/Kota-Ohno/seethrough-live2d-pipeline",
        lang="Python", stars="9",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="把 ComfyUI-See-through 的粗糙分层输出，加工成 **Cubism 能读、能绑骨的高质量分层 PSD**"
              "（重投影 → 边缘细化 → 面部清理 → 写 PSD）。",
        analogy="上一辑的 See-through 只能把立绘**撕成几片**；这条负责把撕下来的片"
                "**修边、排序、放大到 4096**，让它真的能缝。是那半截链路的补完。",
        warn="README 留了一条花钱买不到的硬知识：**Python pytoshop 写出的 PSD 在 Cubism 里会"
             "「图层名能识别但什么都不显示」**，分水岭在 header channels / layer_count / "
             "global layer mask info。作者诚实声明不保证静止 PSD 的绑骨品质。",
        ext=(87, "8.7/10", "单张立绘 → 可动模型 的完整链路上唯一补齐中间三步的项目；依赖 Node + Real-ESRGAN"),
        use=(80, "8.0/10", "MIT、Python 写的、2026-09-21 仍在推送；⚠️ 未本机跑过"),
        src="推送 2026-09-21 · 9★ · MIT · Python · 信源 [1187]",
    ),
    dict(
        nid="rpm32c6", name="open-vt（Godot 写的开源 2D VTuber 宿主）",
        url="https://github.com/erodozer/open-vt",
        lang="GDScript", stars="282",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="**Godot 写的开源 2D VTuber 软件**，支持 OpenSeeFace 与 VTubeStudio（Wi-Fi TCP）"
              "两种追踪源，透明窗口便于 OBS 采集。",
        analogy="目标若从「VN 立绘」外扩到「能动的角色 + 录屏/直播」，这是开源侧成本最低的宿主。"
                "用 **Godot 而不是 Unity**——16GB 机器跑 Unity 那一套是负担。",
        warn="README 自称追求与 VTS 的功能对等，但不含插件生态与 VNet。",
        ext=(78, "7.8/10", "与 VTube Studio 资产兼容（VTS 与 OpenVT 可共用同一套文件），不绑定商业软件"),
        use=(76, "7.6/10", "MIT + 2026-09-25 仍在推送 + 支持免费面捕 OpenSeeFace；⚠️ 未本机实测"),
        src="推送 2026-09-25 · 282★ · MIT · GDScript · 信源 [1188]",
    ),
    dict(
        nid="rpm32c7", name="《数字人应用技术探索（三）》—— 报错原文+解法+最终路径三者齐全",
        url="https://adg.csdn.net/695333b95b9f5f31781bcb3f.html",
        lang="中文", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "排错")],
        plain="作者把「装 Cubism → 打开分层 PSD → 导出 moc3 报错 → 排错 → 再导出 → "
              "放进 Web Demo 人物不显示 → 换官方 SDK 才跑通」的**完整失败链**原样贴出，"
              "连 F12 控制台日志都在。",
        analogy="教程教你**顺风时怎么走**；这种帖子教的是**逆风时怎么爬出来**——"
                "对第一次做的人，后者省的时间是前者的十倍。",
        warn="作者不是营销号（文里有「效果还是没出来……奇怪」这种真实语气）。"
             "注意 `blog.csdn.net` 主站被安全验证拦截，只有 `adg.csdn.net` 子域能直取。",
        ext=(82, "8.2/10", "可抽成一张「Web 端 Live2D 三连排查表」：先看纹理集 → 再看 core 版本是否统一 → 换官方 SDK 最小闭环"),
        use=(88, "8.8/10", "**本轮唯一一条三者齐全的中文一手排错记录**，2025-06-26 发布"),
        src="CSDN · 大志哥123 · 2025-06-26 · WebFetch 全文 · 信源 [1189]",
    ),
    dict(
        nid="rpm32c8", name="AITuberKit 中文排错文档（导出参数组合给得很具体）",
        url="https://docs.aituberkit.com/zh/guide/troubleshooting",
        lang="中文", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "排错")],
        plain="官方把「自制模型在 AITuberKit 里渲染不出来」的根因和绕法写清楚了："
              "**给任一 ArtMesh 开「生成蒙版」+ 导出时选 SDK for Web / Cubism 4.2**。",
        analogy="和上一张卡是**同一个报错的两个独立解法**（一个换 SDK、一个开蒙版），"
                "合起来就是一棵决策树：先试开蒙版（1 分钟），不行再降版本导出。",
        warn="⚠️ 这条里最关键的一句：**Cubism 5 导出的 .moc3（v4）第三方库不兼容**。"
             "所以「用最新版导出」这个直觉在这件事上是错的。",
        ext=(80, "8.0/10", "与官方论坛帖、Zenn 实录三方互证同一结论"),
        use=(90, "9.0/10", "**任何人导出模型给第三方播放器/引擎前都该先看一眼**，可直接抄"),
        src="AITuberKit 官方文档（中文）· 发布日期未核实 · WebFetch 全文 · 信源 [1190]",
    ),
    dict(
        nid="rpm32c9", name="《【live2d教程】从零开始做模型吧》25 集合集（附分好层的练手立绘）",
        url="https://www.bilibili.com/video/BV1c4411s7NR/",
        lang="中文", stars="—",
        tags=[("t-make", "建模")],
        plain="25 集完整建模视频课，简介里**直接给了分好层的练手立绘网盘**（提取码 gy2u）。"
              "播放 68.2 万。",
        analogy="学 Live2D 最卡的一步是**没有能拆的图**——教程再多，手里只有一张成品立绘也无从下手。"
                "这条直接把练手素材递给你。",
        warn="⚠️ 网盘链接是 2019 年的，**是否失效未核实**；版本是 Cubism 3/4 时代，"
             "菜单名与 5.3 有差异，照做时要自己翻译。",
        ext=(72, "7.2/10", "UP 主 縁の翼 的 QQ 群号与上一辑从官方社区页拿到的群号完全对上 —— 两个来源互证"),
        use=(80, "8.0/10", "25 集体量够从 0 走到能做；先解决「没素材练」这个真瓶颈"),
        src="B站 · UP 主 縁の翼 · 2019-05-25 · WebFetch 页面 · 信源 [1191]",
    ),
    dict(
        nid="rpm32c10", name="Live2D 官方手册：物理摆锤参数的**正名**（照妖镜）",
        url="https://docs.live2d.com/en/cubism-editor-manual/physical-operation-setting/",
        lang="官方文档", stars="—",
        tags=[("t-make", "建模"), ("t-warn", "校正基准")],
        plain="官方对四个摆锤参数给了方向性描述与经验区间：`Length`（周期）、"
              "`Ease of swinging`（摆动量，**经验法则 0.7~0.99**）、`Reaction time`（=1 为标准）、"
              "`Speed of convergence`（=1 为标准）。",
        analogy="中文圈流传的「发梢阻尼 0.3-0.5、重力 2.5-3.5」这类数字，"
                "**在官方手册里根本找不到叫「阻尼」「重力」的参数**——名字就不存在。",
        warn="**这条最大的用途是当照妖镜**：拿中文博客的数字去软件里找「阻尼」字段，"
             "会找半天找不到，因为参数名就不叫这个。上一辑那条 CSDN「避坑指南」疑似 AI 生成的判断，"
             "本轮据此进一步坐实。",
        ext=(75, "7.5/10", "作为参数校正基准，可批量验伪中文圈的野数字"),
        use=(92, "9.2/10", "**省的是「照着错误数字找半天」的时间**；调物理前先看这一页"),
        src="Live2D 官方 Editor 手册（英文）· 发布日期未核实 · 搜索片段核实 · 信源 [1192]",
    ),
    dict(
        nid="rpm32c11", name="官方「素材分け」Photoshop 插件（唯一无版权风险的 AI 路径）",
        url="https://docs.live2d.com/en/cubism-editor-manual/material-separation-ps-plugin-download/",
        lang="官方文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "官方"), ("t-warn", "需 PRO")],
        plain="**Live2D 官方自己出的** Photoshop 插件，用 DeepLearning 做「切抜き（Cut Out）」与"
              "「Color Fill / Transparency Fill」，专门自动化建模的前工程——也就是最费人力那段。",
        analogy="别的 AI 拆图方案都在用扩散模型（训练数据来源说不清）；"
                "**官方这个明确声明不用扩散模型、无训练数据版权风险**——"
                "等于官方替你把「这图能不能商用在作品里」这个问题答了。",
        warn="⚠️ 需要 **PRO license** + Photoshop 2024/2025；官方推荐 NVIDIA 8GB 显存，"
             "CPU 也能跑（会慢）。页标注 Updated: 10/28/2025。",
        ext=(86, "8.6/10", "官方 + 深度学习 + 无版权风险，三者交集里唯一的一条"),
        use=(84, "8.4/10", "本轮 AI 方向第二名；对「要发行、怕版权」的场景尤其关键"),
        src="Live2D 官方 Editor 手册 · Updated 2025-10-28 · WebFetch 全文 · 信源 [1193]",
    ),
    dict(
        nid="rpm32c12", name="Zenn 实录：一张 AI 立绘 → VTube Studio 能动的模型，实费不到 4 美元",
        url="https://zenn.dev/shakebenn/articles/e9b4c797d103ed",
        lang="日文", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "一手实测")],
        plain="不会画画的人用 **See-through + ComfyUI** 把 1 张 AI 立绘做成 VTube Studio 里能动的"
              "Live2D 模型，耗时 **2 天**，GPU 实费 **不到 4 美元**；文章把 4 个搜不到的坑"
              "写成了可检索的报错文本。",
        analogy="别的教程给你**愿景**，这篇给你**账单**：2 天 + 4 美元 + 4 个具体报错。"
                "有账单的经验才是能拿来估自己要花多少的经验。",
        warn="最通用的那条知识是 **moc3 第 5 字节判版本**（05 = SDK 5.0~5.2 / 06 = SDK 5.3）——"
             "任何人导出模型都该知道；里面还提到 Cubism 5.3 的 moc3 在 VTube Studio 上存疑。",
        ext=(88, "8.8/10", "对「预算有限 + 16GB 本机」给了可复制的低价路径：云 GPU 花几美元，本地只跑脚本"),
        use=(90, "9.0/10", "**本轮 AI 方向第一名**；日文机翻可读，报错原文是跨语言通用的"),
        src="Zenn · shakebenn · 2026-07-08 · WebFetch 全文 · 信源 [1194]",
    ),
    dict(
        nid="rpm32c13", name="Zenn：Electron + Python + Ollama + Live2D 桌面宠物（几乎量身定做）",
        url="https://zenn.dev/zeur/articles/7bfe5936f3b765",
        lang="日文", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "一手实测")],
        plain="一个**离线可用**的 Live2D 桌面宠物：Electron + PIXI.js 前端 / "
              "**Python（FastAPI + WebSockets）后端** / 语音 VOICEVOX / 对话 **Google Gemini 或 Ollama**。"
              "Python 端每 0.1s 广播 `lipsync`，前端 `setParameterValueById('ParamMouthOpenY', …)`。",
        analogy="前端只是个**壳子**，干活的全在 Python，Live2D 只是渲染层——"
                "「会一点 Python、不熟前端、本机跑 Ollama」的人看到这个架构会觉得很亲切。",
        warn="目标是桌宠不是视觉小说，但**「Python ↔ WebSocket ↔ Live2D 参数」这条通路可以整体搬走**。",
        ext=(85, "8.5/10", "架构图里明写 Ollama；本地 LLM 驱动 Live2D 的现成参考实现"),
        use=(87, "8.7/10", "本轮对画像最贴合的一条工程范例；⚠️ 未本机搭建"),
        src="Zenn · Zeur · 2026-01-19 · WebFetch 全文 · 信源 [1195]",
    ),
    dict(
        nid="rpm32c14", name="easy-live2d（把 Web SDK 封装成像 Pixi sprite 一样好用的轻量库）",
        url="https://github.com/Panzer-Jack/easy-live2d",
        lang="TypeScript", stars="213",
        tags=[("t-make", "建模"), ("t-ok", "持续更新")],
        plain="把 Live2D Web SDK 包成 Pixi.js sprite 一样好用的轻量库，README 中英双语。",
        analogy="上一辑的 pixi-live2d-display 是**零件**，这个是**装好的模块**——"
                "目标是「不知道前端也能用」。",
        warn="创建 2025-04-27，比较新；生态与长期维护性待观察。",
        ext=(70, "7.0/10", "若要做网页版试玩/预览页，这是 MIT + 活跃 + 有中文文档的最优候选"),
        use=(60, "6.0/10", "用户主路径是 Ren'Py，**当前不需要**；登记备用"),
        src="推送 2026-09-24 · 213★ · MIT · TypeScript · 信源 [1196]",
    ),
    dict(
        nid="rpm32c15", name="官方论坛：16GB 内存用户导出 moc3 直接 OOM（帖子未结）",
        url="https://community.live2d.com/discussion/comment/4259",
        lang="官方论坛", stars="—",
        tags=[("t-warn", "硬风险"), ("t-make", "建模")],
        plain="**Windows 10 / i5-12400F / GTX1650 / 16GB RAM** 的用户导出 moc3 时报 "
              "`java.lang.OutOfMemoryError: Java heap space`；官方给了 3 条排查方向，"
              "但**帖子没有最终解决方案（未结帖）**。",
        analogy="官方推荐 8GB 就够用——**那是跑编辑器的数，不是导出时的数**。"
                "导出阶段可能把 16GB 吃满。这条直接回答了「我这台 16GB 够不够」。",
        warn="⚠️ 请按「**已知风险**」而不是「已知解药」记：帖子未解决。"
             "可操作的预防是**控制纹理集大小与 warp deformer 分割数**。",
        ext=(68, "6.8/10", "官方自建论坛，一手；可继续追帖"),
        use=(88, "8.8/10", "**本轮对用户最扎心的一条**——和他机器配置几乎一致"),
        src="Live2D 官方 Creators Forum · 2025-08 · WebFetch 全文（含官方回复）· 信源 [1197]",
    ),
    dict(
        nid="rpm32c16", name="Ren'Py 官方 Live2D Cubism 文档（**本机实测**：支持 Cubism 3/4/5）",
        url="https://docs.renpy.org/en/stable/live2d.html",
        lang="官方文档", stars="—",
        tags=[("t-make", "建模"), ("t-ok", "本机验证")],
        plain="Ren'Py **原生**支持 Live2D，官方文档原话「Ren'Py supports Live2D animations in the "
              "Cubism 3, 4 and 5 formats」。本机 SDK 实测：`renpy/gl2/live2d.py` 与 `live2dcsm.pxi` 在，"
              "`config.gl2 = True`（`renpy/config.py:1050`），`has_live2d()` 用 try/except 优雅降级。",
        analogy="上一辑说「Cubism 5 的 moc3 第三方库不吃」——**那是第三方库的问题**，"
                "Ren'Py 用的是官方 Native SDK，**5 也吃**。走 Ren'Py 这条正路正好绕开第三方兼容坑。",
        warn="⚠️ **本机实测的前置条件**：`lib/` 下没有 `Live2DCubismCore.dll`（`live2d.py:67` 会去找它）"
             "→ 必须先按文档把 `CubismSdkForNative-5-r.1.zip` 放进 SDK 目录，再用 launcher 的"
             "「Install Live2D Cubism SDK for Native」装一次，否则 `has_live2d()` 恒为 False。"
             "另：文档提示商用可能需要购买 Live2D 授权。",
        ext=(92, "9.2/10", "唯一一条**本机验证过**的入口；也是唯一能绕开第三方库版本坑的官方路径"),
        use=(86, "8.6/10", "上轮欠账 #2 的部分闭环：可行性与前置条件已核实，真跑还差一个 .moc3 文件"),
        src="Ren'Py 8.5.3 SDK 本机验证 + 官方文档 · 2026-10-10 · 信源 [1198]",
    ),
]

FOOTNOTES = [
    (1183, "https://github.com/EasyLive2D/live2d-py", "EasyLive2D/live2d-py",
     "576★ · MIT · C++ · 推送 2026-09-30 · GitHub REST API 实测"),
    (1184, "https://github.com/EasyLive2D/live2d-motion3", "EasyLive2D/live2d-motion3",
     "31★ · MIT · Python · 推送 2026-05-15 · GitHub REST API 实测"),
    (1185, "https://github.com/rc14193/RenpyLive2DEyeFollowDemo", "rc14193/RenpyLive2DEyeFollowDemo",
     "4★ · MIT · Ren'Py · 推送 2025-09-26 · GitHub REST API 实测"),
    (1186, "https://github.com/kojimio/RenpyLive2DTraceSample", "kojimio/RenpyLive2DTraceSample",
     "1★ · Apache-2.0 · Ren'Py · 推送 2025-07-04 · GitHub REST API 实测"),
    (1187, "https://github.com/Kota-Ohno/seethrough-live2d-pipeline", "Kota-Ohno/seethrough-live2d-pipeline",
     "9★ · MIT · Python · 推送 2026-09-21 · GitHub REST API 实测"),
    (1188, "https://github.com/erodozer/open-vt", "erodozer/open-vt",
     "282★ · MIT · GDScript · 推送 2026-09-25 · GitHub REST API 实测"),
    (1189, "https://adg.csdn.net/695333b95b9f5f31781bcb3f.html", "CSDN《数字人应用技术探索（三）》",
     "2025-06-26 · 大志哥123 · WebFetch 全文"),
    (1190, "https://docs.aituberkit.com/zh/guide/troubleshooting", "AITuberKit 故障排除（中文）",
     "官方中文文档 · WebFetch 全文"),
    (1191, "https://www.bilibili.com/video/BV1c4411s7NR/", "B站《从零开始做模型吧》25 集合集",
     "UP 主 縁の翼 · 2019-05-25 · 播放 682,063 · WebFetch"),
    (1192, "https://docs.live2d.com/en/cubism-editor-manual/physical-operation-setting/",
     "Live2D 官方手册 · Physical Operation Setting", "官方 Editor 手册 · 搜索片段核实"),
    (1193, "https://docs.live2d.com/en/cubism-editor-manual/material-separation-ps-plugin-download/",
     "Live2D 官方「素材分け」Photoshop 插件", "官方手册 · Updated 2025-10-28 · WebFetch 全文"),
    (1194, "https://zenn.dev/shakebenn/articles/e9b4c797d103ed", "Zenn · AI 一张图做可动 Live2D 全记录",
     "shakebenn · 2026-07-08 · WebFetch 全文"),
    (1195, "https://zenn.dev/zeur/articles/7bfe5936f3b765", "Zenn · Electron+Python+Ollama+Live2D 桌宠",
     "Zeur · 2026-01-19 · WebFetch 全文"),
    (1196, "https://github.com/Panzer-Jack/easy-live2d", "Panzer-Jack/easy-live2d",
     "213★ · MIT · TypeScript · 推送 2026-09-24 · GitHub REST API 实测"),
    (1197, "https://community.live2d.com/discussion/comment/4259", "Live2D 官方论坛 · 16GB 导出 OOM",
     "2025-08 · 官方 staff 已回复 · 帖子未结 · WebFetch 全文"),
    (1198, "https://docs.renpy.org/en/stable/live2d.html", "Ren'Py 官方文档 · Live2D Cubism",
     "Ren'Py 8.5.3 SDK 本机验证 2026-10-10"),
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

    desc = ('第二十六辑三路调研（GitHub 32 / 中文社媒 28 / 官方与海外 26），本版取 15 项，'
            '主题 **Live2D 制作**：优先「省拆图与绑骨人力」+「接得进游戏/网页/直播的运行时」+「AI × Live2D」。'
            '所有 ★ / 许可证 / 语言 / 推送日均走 `gh api repos/<r>` 实测，主 agent 另抽 5 个复核。'
            '<strong>本辑主线：Editor 授权买的是「绑骨」，不是「渲染」——渲染用的 Core 免费</strong> ——'
            '所以票投给「绕开 Editor 也能干活」的东西：Python 读写 motion3 编动作、Python 直接跑运行时、'
            '以及官方用深度学习做「素材分け」的 PS 插件（唯一无版权风险的 AI 路径）。'
            '另一条主线是排错：Cubism 5 的 moc3 第三方库不吃、纹理集未生成、16GB 导出 OOM。')

    block = ['    <div class="group" data-page-node-id="rpm32g">',
             '      <div class="group-title" data-page-node-id="rpm32gt">🆕 第三十二版增补 · Live2D 深化：Python 侧工具与排错实录（16 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm32gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm32r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm32ra%s">%s</a> — %s</div>'
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
