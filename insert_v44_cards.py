# -*- coding: utf-8 -*-
"""第四十四版增补（2026-10-12）：Live2D —— GitHub 生产链 / 桌宠 AI + 国内经验帖（18 项）。
幂等、锚点断言、div 深度自检、重复仓库检测。改 index.html 前已用 insert_guard_probe 验过。
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1452"'
FIRST_NEW_FOOTNOTE = 1453
MARKER = "第四十四版增补"

HEAD_OLD = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11 · 第四十一版增补 2026-10-11 · 第四十二版增补 2026-10-11 · 第四十三版增补 2026-10-12 · 第四十三版补录 2026-10-12 · 第四十三版再补录 2026-10-12',
    '共 1453 个项目',
    '第四十三版再补录 3 项（均与上版零重复）',
]
HEAD_NEW = [
    HEAD_OLD[0] + ' · 第四十四版增补 2026-10-12',
    '共 1471 个项目',
    '第四十三版再补录 3 项（均与上版零重复） + 第四十四版增补 18 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm44g1", name="VTuber-Python-Unity（★558）—— 同时支持 3D 和 Live2D 的虚拟形象实现，Python 驱动 Unity",
        url="https://github.com/mmmMMM44/VTuber-Python-Unity",
        lang="开源", stars="558",
        tags=[("t-ok", "开源"), ("t-pet", "桌宠"), ("t-make", "驱动")],
        plain="一个用 Python + Unity 实现的虚拟形象项目，同时覆盖 3D 和 Live2D 两种模型。本质是把面捕 / 语音 / 表情这些「驱动信号」用 Python 算出来，再喂给 Unity 里的模型。",
        analogy="相当于给 Live2D / 3D 模型做了一层「驱动中间件」：你不用在 Unity 里手写每一条追踪逻辑，用 Python 侧统一处理输入（摄像头、麦克风、聊天），Unity 只管渲染。",
        ext=(70, "70", "Python 侧可扩展性强，能接任意输入源；但依赖 Unity，二次开发需要 C# / Unity 基础。"),
        use=(75, "75", "想做「会动的桌宠 / 直播形象」且已有 Unity 底子的人，这是现成脚手架；纯新手门槛偏高。"),
        src="gh 实测 ★558 / MIT / C# · 信源 [1453]",
    ),
    dict(
        nid="rpm44g2", name="Live2D Cubism SDK for Unity 文档中文翻译（★29）—— 官方英文手册的社区中译",
        url="https://github.com/gtf35/live2d_unity_sdk_chinese_document",
        lang="文档", stars="29",
        tags=[("t-ok", "官方"), ("t-make", "文档"), ("t-zh", "中文")],
        plain="把 Live2D 官方 Cubism SDK for Unity 的英文文档翻译成中文，施工中。对看英文手册吃力的中文开发者是直接刚需。",
        analogy="官方手册是权威但全是英文；这份翻译相当于给那本「说明书」配了中文版，省掉每次查词典的摩擦。",
        ext=(40, "40", "翻译覆盖度看提交频率，目前施工中；但「官方手册」这个源本身是权威。"),
        use=(85, "85", "用 Unity 接 Live2D 的中文开发者，把它当官方手册的对照本最实用。"),
        src="gh 实测 ★29 / LGPL-2.1 / 施工中 · 信源 [1454]",
    ),
    dict(
        nid="rpm44g3", name="layer2rig-cubism-plugin —— 用 MCP 桥接 + Codex 工作流做 Live2D Cubism 绑定",
        url="https://github.com/Tian-9/layer2rig-cubism-plugin",
        lang="开源", stars="1",
        tags=[("t-make", "AI"), ("t-make", "绑定"), ("t-new", "新")],
        plain="一个把「分层 PSD → Cubism 绑定」做成 MCP 工具 + Codex 工作流的插件。定位是让 AI 编码助手能按规范驱动 Cubism Editor 做绑定，而不是手动点。",
        analogy="这是「AI 做绑定」方向的一个早期样本：把重复的绑定操作抽象成可被 LLM 调用的工具，和这一两年「AI 自动拆层 → 自动绑定」的流水线思路一致。",
        ext=(55, "55", "思路新颖（MCP + Codex 驱动 Cubism），但 ★1、无 license、未验证，属于「方向信号」不是「成品」。"),
        use=(50, "50", "想研究「AI 自动绑定」管线的人值得看思路；直接拿来用为时过早。"),
        src="gh 实测 ★1 / 无 license / Python · 信源 [1455]",
    ),
    dict(
        nid="rpm44g4", name="live2d-chatbot-demo（★96）—— Python + JS 的 Live2D 聊天机器人演示",
        url="https://github.com/nladuo/live2d-chatbot-demo",
        lang="开源", stars="96",
        tags=[("t-ok", "开源"), ("t-pet", "AI"), ("t-make", "桌宠")],
        plain="一个用 Python 后端 + 前端 JS 把 Live2D 模型接上聊天 AI 的演示项目。模型能根据对话内容动嘴、变表情。",
        analogy="这就是「会聊天的看板娘」的最小可运行样本：后端管对话（接任意 LLM），前端管 Live2D 渲染和口型同步。",
        ext=(65, "65", "后端可换任意 LLM（含本地 Ollama），前端是标准 Live2D Web 渲染；结构清晰好改。"),
        use=(80, "80", "想做「AI 桌宠 / 聊天形象」的人，这是比从零搭更省事的起点；你这套 Ollama 栈能直接对接。"),
        src="gh 实测 ★96 / 无 license / Jupyter · 信源 [1456]",
    ),
    dict(
        nid="rpm44g5", name="mate-human（★11）—— 把 Live2D Cubism 5 Web SDK 与 Fay 数字人框架深度集成",
        url="https://github.com/Yancheng-s/mate-human",
        lang="开源", stars="11",
        tags=[("t-ok", "开源"), ("t-make", "AI"), ("t-zh", "国产")],
        plain="把 Live2D Cubism 5 的 Web SDK 和 Fay（开源数字人 AI 框架）接在一起的开源项目，目标是一个本地可跑的中文数字人。",
        analogy="相当于给 Live2D 模型套了个「大脑 + 嘴」：Fay 负责对话和语音，Cubism 5 Web SDK 负责把模型在浏览器里渲染出来并跟着说话动。",
        ext=(60, "60", "国产协议（木兰 PSL-2.0）合规友好，Web 端部署简单；★11 说明还早。"),
        use=(70, "70", "想要「本地中文数字人」的人，这个组合（Fay + Live2D Cubism 5 Web）值得跟。"),
        src="gh 实测 ★11 / MulanPSL-2.0 / Python · 信源 [1457]",
    ),
    dict(
        nid="rpm44g6", name="UE-Live2D（★25）—— 把 Live2D Cubism Native SDK 接入 Unreal Engine 的插件",
        url="https://github.com/stkrwork/UE-Live2D",
        lang="开源", stars="25",
        tags=[("t-make", "引擎"), ("t-make", "Unreal"), ("t-ok", "开源")],
        plain="一个 Unreal Engine 插件，把 Live2D Cubism 的 Native SDK 集成进 UE，让虚幻项目能直接显示和驱动 Live2D 模型。",
        analogy="对应 Unity 早就有的 CubismComponents，这是给 Unreal 用户补上的「官方 SDK 接入层」——虽然官方也有 beta2 插件，社区版给了另一条路。",
        ext=(55, "55", "MIT 可改；但和官方 Unreal 插件（beta2）功能重叠，选哪个看你是否信官方维护。"),
        use=(60, "60", "用 Unreal 做项目、想塞一个 Live2D 形象的人有得选了；纯 Unity / Web 用户用不上。"),
        src="gh 实测 ★25 / MIT / C++ · 信源 [1458]",
    ),
    dict(
        nid="rpm44g7", name="pymouth（★10）—— 基于 Python 的 Live2D 口型同步库",
        url="https://github.com/organics2016/pymouth",
        lang="开源", stars="10",
        tags=[("t-ok", "开源"), ("t-make", "AI"), ("t-make", "口型")],
        plain="一个 Python 库，专门做 Live2D 模型的口型（lip sync）同步，根据音频自动驱动嘴部参数。",
        analogy="做「会说话的 Live2D」最烦的就是嘴要对上声音；pymouth 把「听声音 → 动嘴」这一步封装成了 Python 调用，和语音识别 / LLM 串起来很顺。",
        ext=(60, "60", "MIT、Python 生态，能和你的 Ollama / 语音栈直接拼；★10 偏小但方向对。"),
        use=(75, "75", "做本地 AI 对话形象时，口型同步这一环可以省掉自己写 FFT / 能量分析。"),
        src="gh 实测 ★10 / MIT / Python · 信源 [1459]",
    ),
    dict(
        nid="rpm44g8", name="live2d-Live-Assistant（★4）—— 用 Python + HTML 做的 Live2D 桌面 AI 伴侣「Hyori」",
        url="https://github.com/JSNrepo/live2d-Live-Assistant",
        lang="开源", stars="4",
        tags=[("t-ok", "开源"), ("t-pet", "AI"), ("t-pet", "桌宠")],
        plain="一个用 Python + HTML 构建的 Live2D 桌面 AI 伴侣项目（叫 Hyori），模型能根据对话做表情和动作。",
        analogy="这就是「AI 桌宠」的一个具体实现样本——和待办里那套 luckui/HiyoriAI 是同一条路线（本地 LLM 驱动桌面 Live2D）。",
        ext=(50, "50", "★4、很早期，但路线和你的「本机 Ollama + Live2D」目标完全对口。"),
        use=(65, "65", "想「真跑一遍 AI 桌宠」时，它和 HiyoriAI 一起当作参考样本。"),
        src="gh 实测 ★4 / MIT / Python · 信源 [1460]",
    ),
    dict(
        nid="rpm44g9", name="Virtual-Avatar-Intelligent-Driving-System（★4）—— 基于 Python 的 Live2D 多模态虚拟形象驱动系统",
        url="https://github.com/Hatsukoi-0115/Virtual-Avatar-Intelligent-Driving-System",
        lang="开源", stars="4",
        tags=[("t-ok", "开源"), ("t-make", "AI"), ("t-new", "多模态")],
        plain="一个 Python 项目，目标是在 Windows 上把摄像头、麦克风、实时语音识别、情绪理解串起来，驱动 Live2D 模型做表情和动作。",
        analogy="把「看（摄像头）+ 听（ASR）+ 懂情绪 + 动模型」整条链路打通，是「多模态桌宠」的一个较完整样本。",
        ext=(55, "55", "思路完整（多模态输入 → 模型驱动），但 ★4、无 license、未验证。"),
        use=(60, "60", "研究「桌宠怎么感知环境并回应」时参考价值高。"),
        src="gh 实测 ★4 / 无 license / Python · 信源 [1461]",
    ),
    dict(
        nid="rpm44g10", name="lpk2moc3（★18）—— 带 GUI 的 .lpk 提取 moc3 工具",
        url="https://github.com/Arkueid/lpk2moc3",
        lang="开源", stars="18",
        tags=[("t-make", "工具"), ("t-make", "格式"), ("t-make", "提取")],
        plain="一个带图形界面的小工具，从 .lpk 文件里提取 Live2D 的 moc3 模型。.lpk 是某些打包格式，这工具帮你把模型抠出来。",
        analogy="相当于「解包器」：别人把 Live2D 模型塞进 .lpk 时，你用它能把 moc3 还原出来做研究或迁移。",
        ext=(50, "50", "专注单一功能（lpk → moc3），Python + GUI 好用；但无 license，商用要谨慎。"),
        use=(55, "55", "遇到 .lpk 包裹的模型、想提取 moc3 时的一件趁手工具。"),
        src="gh 实测 ★18 / 无 license / Python · 信源 [1462]",
    ),
    dict(
        nid="rpm44g11", name="moc3-reader-re（★17）—— 通过逆向实现的 Java 版 moc3 文件读取器",
        url="https://github.com/QiE2035/moc3-reader-re",
        lang="开源", stars="17",
        tags=[("t-make", "格式"), ("t-make", "Java"), ("t-make", "逆向")],
        plain="一个 Java 写的 moc3 文件读取器，作者通过逆向 Cubism 格式实现，能解析 moc3 内部结构。",
        analogy="和之前收的 py-moc3（纯 Python 字节级 round-trip）是同一条「格式透明化」路线，只不过这次是 Java 版、偏读取。",
        ext=(60, "60", "逆向实现、可扩展读 moc3；但和 py-moc3 一样，受 Cubism Core 许可约束，只能读不能打包 Core。"),
        use=(65, "65", "需要在 Java 生态里读 moc3、或想理解 moc3 格式结构时参考。"),
        src="gh 实测 ★17 / 无 license / Java · 信源 [1463]",
    ),
    dict(
        nid="rpm44g12", name="Live2D-JavaBinding（★16）—— Live2D Cubism SDK 的 Java 封装",
        url="https://github.com/Eatgrapes/Live2D-JavaBinding",
        lang="开源", stars="16",
        tags=[("t-make", "SDK"), ("t-make", "Java"), ("t-make", "封装")],
        plain="把 Live2D Cubism SDK 用 Java 封装起来，让 Java / Kotlin 开发者能调用 Cubism 功能。",
        analogy="和已有的 cubism-rs（Rust）、Live2D-Python 一个性质：给某个语言生态补上 Cubism 的官方封装层。",
        ext=(55, "55", "MIT、Java 生态可用；但要注意和「官方 Core 不进 GitHub」的合规边界（只封装、不打包 Core）。"),
        use=(60, "60", "做 Java / Android 端 Live2D 的人，比自己 JNI 调 Native 更省事。"),
        src="gh 实测 ★16 / MIT / Java · 信源 [1464]",
    ),
    dict(
        nid="rpm44w1", name="CSDN《Live2D 看板娘全攻略：从模型绑定到网页接入》—— 中文实操长文",
        url="https://blog.csdn.net/weixin_33824385/article/details/164274377",
        lang="经验帖", stars="—",
        tags=[("t-make", "经验帖"), ("t-zh", "中文"), ("t-make", "版权")],
        plain="一篇中文长文，从「模型从哪来」讲起：自制（Cubism Editor 免费版够练手）、免费素材（itch.io / Booth，注意授权）、约稿定制（国内几百到几千元）。重点强调了版权意识——没有 ReadMe / 规约的一律默认不可商用。",
        analogy="相当于给「想做 Live2D 看板娘」的新手画了一张全流程图，把最容易踩的版权坑先标红了。",
        ext=(70, "70", "实操性强、覆盖全流程；但「看板娘」偏向网页展示，不是完整角色动画。"),
        use=(85, "85", "中文用户入门 Live2D + 网页接入最省事的一篇；版权提醒尤其该看。"),
        src="CSDN 路 · 2026-10-12 核对 · blog.csdn.net 一手 · 信源 [1465]",
    ),
    dict(
        nid="rpm44w2", name="CSDN《打造一个可定制工作流的桌面女友》—— Electron + Live2D + AI",
        url="https://blog.csdn.net/qiwoo_weekly/article/details/154970175",
        lang="经验帖", stars="—",
        tags=[("t-make", "经验帖"), ("t-pet", "桌宠"), ("t-make", "AI")],
        plain="一篇中文教程，用 Electron 起项目、集成 live2d-widget 显示 Live2D 模型，再接 AI（文中用 Lobster AIgo）做「会对话的桌面伴侣」。从下载官方示例模型（Haru）到 localhost 加载资源一步步写。",
        analogy="这就是「AI 桌宠」的保姆级搭建笔记：Electron 当壳、Live2D 当脸、LLM 当脑，三段拼起来。",
        ext=(65, "65", "步骤细、能照抄；但 AI 那部分用的第三方服务，换成你自己的 Ollama 要改。"),
        use=(80, "80", "想「真跑一遍 AI 桌宠」时，这篇的 Electron + Live2D 骨架可以直接借鉴。"),
        src="CSDN 路 · 2026-10-12 核对 · blog.csdn.net 一手 · 信源 [1466]",
    ),
    dict(
        nid="rpm44w3", name="巴哈姆特《Live2D 教學、學習資源整理》—— 繁中社区资源大合集",
        url="https://forum.gamer.com.tw/C.php?bsn=60608&snA=3363",
        lang="经验帖", stars="—",
        tags=[("t-make", "经验帖"), ("t-zh", "繁中"), ("t-make", "资源")],
        plain="一篇繁体中文（台湾）社区的 Live2D 学习资源整理帖，持续更新。收了官方手册、B 站双语字幕教学、Discord 社群、模型商城（nizima / Booth / Sketchfab）、拆图教程（高可动域建模、部件准备）等。",
        analogy="相当于繁中圈的「Live2D 资源导航页」，把散在各处的教程 / 社群 / 素材站串成一张地图。",
        ext=(75, "75", "资源密度高、社区维护；但部分链接会过期，且偏「资源索引」不是「深度教程」。"),
        use=(80, "80", "想系统找 Live2D 学习资料（尤其繁中 / 双语）时的最佳入口。"),
        src="巴哈姆特论坛 · 2026-10-12 核对 · forum.gamer.com.tw 一手 · 信源 [1467]",
    ),
    dict(
        nid="rpm44w4", name="yysuni《做一个 Live2D》—— 前端开发者自己做看板娘的踩坑笔记",
        url="https://www.yysuni.com/blog/live2d-note",
        lang="经验帖", stars="—",
        tags=[("t-make", "经验帖"), ("t-make", "个人"), ("t-make", "前端")],
        plain="一个前端开发者的个人博客，记录自己从零做 Live2D 看板娘的过程：Cubism Editor 只有一款、免费版有限制、用 AI 生成正身图、Figma 不行必须 PS 分层、关键帧 / 镜像动作 / 导出踩的坑。",
        analogy="相当于「一个前端第一次做 Live2D」的真实流水账，把软件逻辑（关键帧记录操作、四角形状合成）讲得挺清楚，适合同样前端背景的人。",
        ext=(60, "60", "真实个人经验、通俗易懂；但只做到「上下左右看」的简单效果，深度有限。"),
        use=(70, "70", "前端开发者想「给网站加个 Live2D」时，这篇的视角最贴近。"),
        src="个人博客 · 2026-10-12 核对 · yysuni.com 一手 · 信源 [1468]",
    ),
    dict(
        nid="rpm44w5", name="Live2D Cubism 官方教程站（docs.live2d.com）—— 从入门到嵌入的权威视频教程",
        url="https://docs.live2d.com/zh-CHS/cubism-editor-tutorials/top",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "教程"), ("t-zh", "中文")],
        plain="Live2D 官方教程站，中文可用。从 10 分钟「眨眼」、基础教程（6 次课）、模板功能、嵌入用教程（模型准备 / 物理 / 导出 / Viewer 操作）到提高动态质量技巧，都有官方视频。",
        analogy="做任何 Live2D 项目的「说明书起点」——所有第三方教程都该以它为准，尤其涉及 SDK 版本和导出口径时。",
        ext=(90, "90", "官方一手、权威、免费、持续更新（2026-01 还在加页面）；这是判断「某教程对不对」的基准。"),
        use=(95, "95", "无论新手老手，遇到「这一步到底官方怎么规定」都该回来查。"),
        src="official 路 · 2026-10-12 核对 · docs.live2d.com 一手 · 信源 [1469]",
    ),
    dict(
        nid="rpm44w6", name="live2d.net.cn《Live2D 从建模到出图流程》—— 中文步骤拆解",
        url="https://www.live2d.net.cn/tuijian/live-wobvois.html",
        lang="经验帖", stars="—",
        tags=[("t-make", "经验帖"), ("t-zh", "中文"), ("t-make", "流程")],
        plain="一篇中文站把 Live2D 制作拆成清晰的三段闭环：PSD 规范拆分 → 导入 → 网格 / 变形器 / 参数绑定 → 纹理图集与导出，并强调「导出文件清单 + SDK 口径 + Viewer 最小闭环验证」来避免返工。",
        analogy="和官方教程互补的「中文速查版」：把官方那套流程压缩成可对照的步骤清单，新手照着走不容易乱。",
        ext=(55, "55", "中文、结构清晰；但属 SEO 内容站，深度不如官方，且可能转载汇编。"),
        use=(65, "65", "想快速对照「这一步该干嘛」时方便；深度问题还是回官方。"),
        src="中文内容站 · 2026-10-12 核对 · live2d.net.cn 一手 · 信源 [1470]",
    ),
]

FOOTNOTES = [
    (1453, "https://github.com/mmmMMM44/VTuber-Python-Unity", "mmmMMM44/VTuber-Python-Unity（★558 / MIT / C#）",
     "gh api 实测 ★558 / forks 高 / MIT / C# / 同时覆盖 3D + Live2D · 信源 [1453]"),
    (1454, "https://github.com/gtf35/live2d_unity_sdk_chinese_document", "gtf35/live2d_unity_sdk_chinese_document（★29 / LGPL-2.1）",
     "gh api 实测 ★29 / LGPL-2.1 / 施工中 · 官方 Cubism Unity SDK 文档中译 · 信源 [1454]"),
    (1455, "https://github.com/Tian-9/layer2rig-cubism-plugin", "Tian-9/layer2rig-cubism-plugin（★1）",
     "gh api 实测 ★1 / 无 license / Python · MCP 桥接 + Codex 工作流驱动 Cubism 绑定 · 信源 [1455]"),
    (1456, "https://github.com/nladuo/live2d-chatbot-demo", "nladuo/live2d-chatbot-demo（★96）",
     "gh api 实测 ★96 / 无 license / Jupyter · Python + JS 的 Live2D 聊天机器人演示 · 信源 [1456]"),
    (1457, "https://github.com/Yancheng-s/mate-human", "Yancheng-s/mate-human（★11 / 木兰 PSL-2.0）",
     "gh api 实测 ★11 / MulanPSL-2.0 / Python · Cubism 5 Web SDK + Fay 数字人框架 · 信源 [1457]"),
    (1458, "https://github.com/stkrwork/UE-Live2D", "stkrwork/UE-Live2D（★25 / MIT）",
     "gh api 实测 ★25 / MIT / C++ · Unreal Engine 插件接入 Cubism Native SDK · 信源 [1458]"),
    (1459, "https://github.com/organics2016/pymouth", "organics2016/pymouth（★10 / MIT）",
     "gh api 实测 ★10 / MIT / Python · Live2D 口型同步库 · 信源 [1459]"),
    (1460, "https://github.com/JSNrepo/live2d-Live-Assistant", "JSNrepo/live2d-Live-Assistant（★4 / MIT）",
     "gh api 实测 ★4 / MIT / Python + HTML · 桌面 AI 伴侣 Hyori · 信源 [1460]"),
    (1461, "https://github.com/Hatsukoi-0115/Virtual-Avatar-Intelligent-Driving-System", "Hatsukoi-0115/Virtual-Avatar-Intelligent-Driving-System（★4）",
     "gh api 实测 ★4 / 无 license / Python · 多模态（摄像头+ASR+情绪）驱动 Live2D · 信源 [1461]"),
    (1462, "https://github.com/Arkueid/lpk2moc3", "Arkueid/lpk2moc3（★18）",
     "gh api 实测 ★18 / 无 license / Python · 带 GUI 的 .lpk → moc3 提取器 · 信源 [1462]"),
    (1463, "https://github.com/QiE2035/moc3-reader-re", "QiE2035/moc3-reader-re（★17）",
     "gh api 实测 ★17 / 无 license / Java · 逆向实现的 moc3 读取器 · 信源 [1463]"),
    (1464, "https://github.com/Eatgrapes/Live2D-JavaBinding", "Eatgrapes/Live2D-JavaBinding（★16 / MIT）",
     "gh api 实测 ★16 / MIT / Java · Cubism SDK 的 Java 封装 · 信源 [1464]"),
    (1465, "https://blog.csdn.net/weixin_33824385/article/details/164274377", "CSDN《Live2D 看板娘全攻略》",
     "CSDN 路 · 2026-10-12 核对 · 模型来源三条路线（自制 / 免费素材 / 约稿）+ 版权提醒 · blog.csdn.net 一手 · 信源 [1465]"),
    (1466, "https://blog.csdn.net/qiwoo_weekly/article/details/154970175", "CSDN《打造可定制工作流的桌面女友》",
     "CSDN 路 · 2026-10-12 核对 · Electron + Live2D + AI 桌宠保姆级笔记 · blog.csdn.net 一手 · 信源 [1466]"),
    (1467, "https://forum.gamer.com.tw/C.php?bsn=60608&snA=3363", "巴哈姆特《Live2D 教學、學習資源整理》",
     "巴哈姆特论坛 · 2026-10-12 核对 · 繁中社区资源大合集（官方手册 / B站双语 / Discord / 商城 / 拆图教程）· forum.gamer.com.tw 一手 · 信源 [1467]"),
    (1468, "https://www.yysuni.com/blog/live2d-note", "yysuni《做一个 Live2D》",
     "个人博客 · 2026-10-12 核对 · 前端开发者从零做看板娘的踩坑笔记 · yysuni.com 一手 · 信源 [1468]"),
    (1469, "https://docs.live2d.com/zh-CHS/cubism-editor-tutorials/top", "Live2D Cubism 官方教程站",
     "official 路 · 2026-10-12 核对 · 从入门到嵌入的权威中文视频教程 · docs.live2d.com 一手 · 信源 [1469]"),
    (1470, "https://www.live2d.net.cn/tuijian/live-wobvois.html", "live2d.net.cn《从建模到出图流程》",
     "中文内容站 · 2026-10-12 核对 · 三段闭环中文速查 · live2d.net.cn 一手 · 信源 [1470]"),
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
        u = c.get("url") or ""
        if not u:
            continue
        if u in src:
            bad.append("URL 已存在，别重复登记：%s" % u)
        if "github.com/" in u:
            slug = u.split("github.com/")[-1].lower()
            if len(slug) >= 8 and slug in src.lower():
                bad.append("仓库已存在，别重复登记：%s" % u)

    si = src.find(SECTION_S3)
    if src.count(SECTION_S3) != 1:
        bad.append("%s 出现 %d 次" % (SECTION_S3, src.count(SECTION_S3)))
        ins = -1
    else:
        ins = si

    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if bad or ins < 0 or fend < 0:
        for x in bad:
            print("❌ " + x)
        print("未改动 index.html")
        return 1

    desc = ('第四十四版增补（18 项）：**① GitHub 生产链与桌宠 AI** —— '
            '收了 Python 驱动 Unity 的 VTuber-Python-Unity（★558）、Cubism Unity 文档中译（★29）、'
            'MCP + Codex 驱动 Cubism 绑定的 layer2rig、Live2D 聊天机器人演示（★96）、'
            'Cubism 5 Web + Fay 国产数字人、UE 插件、口型同步库 pymouth、多模态驱动系统等；'
            '**② 格式透明化工具** —— lpk2moc3 提取器、逆向 moc3 读取器、Java 封装；'
            '**③ 国内 / 官方经验帖** —— CSDN 看板娘全攻略（含版权提醒）、Electron+Live2D+AI 桌宠笔记、'
            '巴哈姆特繁中资源大合集、前端个人踩坑笔记、官方教程站、中文速查流程。')

    block = ['    <div class="group" data-page-node-id="rpm44gg">',
             '      <div class="group-title" data-page-node-id="rpm44ggt">🆕 第四十四版增补 · GitHub 生产链 / 桌宠 AI + 国内经验帖（18 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm44ggd">' + b(desc) + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm44r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm44ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    for o, n in zip(HEAD_OLD, HEAD_NEW):
        if src.count(o) != 1:
            print("二次校验失败：页头锚点 %s 出现 %d 次" % (o[:40], src.count(o)))
            return 1
        src = src.replace(o, n)

    open(HTML, "w", encoding="utf-8").write(src)
    print("✅ 已插入 %s：%d 张卡 + %d 条脚注（[%d]-[%d]）"
          % (MARKER, len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE, FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    print("   页头：1453 → 1471 项；卡片 1436 → %d" % (1436 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
