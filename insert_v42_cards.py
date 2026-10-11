# -*- coding: utf-8 -*-
"""第三十八辑（2026-10-11）增补脚本：Live2D 制作全谱系补采（23 项）。
幂等、锚点断言、div 深度自检、重复仓库检测。改 index.html 前已用 insert_guard_probe 验过。
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1402"'
FOOTER_MARK = '  <footer data-page-node-id="rq7xrixbWVHwdFs2CDNYhJ">'
FIRST_NEW_FOOTNOTE = 1403
MARKER = "第四十二版增补"

HEAD_OLD = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11 · 第四十一版增补 2026-10-11',
    '共 1403 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项 + 第四十一版增补 24 项（均与上版零重复）',
]
HEAD_NEW = [
    '数据抓取：2026-10-11 · 第四十版增补 2026-10-11 · 第四十一版增补 2026-10-11 · 第四十二版增补 2026-10-11',
    '共 1426 个项目',
    '第三十七版增补 22 项 + 第三十八版增补 24 项 + 第三十九版增补 24 项 + 第四十版增补 24 项 + 第四十一版增补 24 项 + 第四十二版增补 23 项（均与上版零重复）',
]

CARDS = [
    # ---------- A. 工具 / 查看器 / 插件 / 引擎 ----------
    dict(
        nid="rpm42c1", name="ezshine/AwesomeLive2D —— Live2D 模型 / 资源 awesome 清单（★411）",
        url="https://github.com/ezshine/AwesomeLive2D",
        lang="无", stars="411",
        tags=[("t-make", "资源"), ("t-new", "新")],
        plain="Live2D 模型与资源聚合清单，覆盖各风格模型、教程与工具链接。",
        analogy="做索引站的人最缺的不是工具，是「上哪找模型」的清单。这条是现成的导航起点。",
        warn="⚠️ 最后推送 2023-12（约 3 年未动）、无 LICENSE，仅作资源导航，别当实现依赖。",
        ext=(60, "60", "资源索引，链接会过期，需定期复验；对维护索引站的人价值最高。"),
        use=(50, "50", "★411 说明有人真的在用；当书签站用，别 clone 当依赖。"),
        src="创建 2023-12-19 · 推送 2023-12-19 · 411★ · 无许可证 · REST 实测 · 信源 [1403]",
    ),
    dict(
        nid="rpm42c2", name="TSKI433/hime-display —— 一套 UI 看 Live2D / Spine / MMD / VRoid 四格式（★254）",
        url="https://github.com/TSKI433/hime-display",
        lang="JavaScript", stars="254",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="通用桌面模型查看器：一套界面同时显示 Live2D / Spine / MMD / VRoid 四种格式，省去为每种格式装一个软件。",
        analogy="多数查看器只认一种格式。这一条把四格式统一在一个窗口里，做素材库预览时最省事。",
        warn="⚠️ GPL-3.0 传染，做产品留意。",
        ext=(72, "72", "跨格式统一查看的思路对做模型素材库预览有用，抽象干净。"),
        use=(65, "65", "★254、桌面端直接跑；研究「多格式聚合查看器」的首选样本。"),
        src="创建 · 推送 2026-03-30 · 254★ · GPL-3.0 · JavaScript · REST 实测 · 信源 [1404]",
    ),
    dict(
        nid="rpm42c3", name="LIlGG/plugin-live2d —— Halo 博客平台 Live2D 看板娘插件（★251）",
        url="https://github.com/LIlGG/plugin-live2d",
        lang="TypeScript", stars="251",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="Halo 博客平台的 Live2D 看板娘插件，「为你的网站领养一只可爱的看板娘」，2026-09 仍在推。",
        analogy="「博客挂看板娘」这类需求很多人做过，但做成平台插件、即插即用的不多；这一条是 Halo 生态的现成样本。",
        ext=(68, "68", "面向 Halo 生态即插即用；否则当作「博客挂 Live2D」最小插件抄。"),
        use=(70, "70", "★251、MIT、维护活跃；Halo 站点可直接用，其它站点抄结构。"),
        src="创建 · 推送 2026-09-29 · 更新 2026-09-29 · 251★ · MIT · TypeScript · REST 实测 · 信源 [1405]",
    ),
    dict(
        nid="rpm42c4", name="amorist/platelet —— 经典「血小板」网页 Live2D 看板娘（★226）",
        url="https://github.com/amorist/platelet",
        lang="JavaScript", stars="226",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="知名度高的萌系网页 widget（描述「けっしょうばん」），2018 建仓但 2026-10 仍在推。",
        analogy="看板娘界的「hello world」级别样本，代码量小、可改性强，适合当网站挂 Live2D 的起步模板。",
        warn="⚠️ GPL-3.0、注意医学梗版权。",
        ext=(55, "55", "现成网页 widget，改文案/模型即可；适合做站点 mascot。"),
        use=(60, "60", "★226、GPL-3.0；做「网站挂看板娘」的现成实现参考。"),
        src="创建 · 推送 2026-10-05 · 226★ · GPL-3.0 · JavaScript · REST 实测 · 信源 [1406]",
    ),
    dict(
        nid="rpm42c5", name="iCharlesZ/vscode-live2d-models —— VSCode 看板娘模型库（★169）",
        url="https://github.com/iCharlesZ/vscode-live2d-models",
        lang="无", stars="169",
        tags=[("t-make", "资源"), ("t-new", "新")],
        plain="收集可挂到 VSCode Live2D 插件的模型资源集合（非工具）。",
        analogy="编辑器挂看板娘的需求一直有，这条是现成的模型包，省得自己找。",
        warn="⚠️ 无 LICENSE，版权归原作者；取模型测试用。",
        ext=(40, "40", "模型资源集合，非工具，扩展靠往里加模型。"),
        use=(45, "45", "★169、当 VSCode 看板娘的模型补给站。"),
        src="创建 · 推送 2026-03-25 · 169★ · 无许可证 · REST 实测 · 信源 [1407]",
    ),
    dict(
        nid="rpm42c6", name="LSTM-Kirigaya/Live2dRender —— Web 端新版 Live2D 渲染器（★183）",
        url="https://github.com/LSTM-Kirigaya/Live2dRender",
        lang="TypeScript", stars="183",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="面向新版 Cubism 的 Web 渲染封装，可作为自己搭网页查看器 / 桌宠的渲染底座。",
        analogy="想自己写网页 Live2D 查看器，从零解析 Cubism 格式太重；这条是现成的渲染封装，直接当底座。",
        warn="⚠️ 最后推送 2025-07，非最新，接前先核版本。",
        ext=(70, "70", "Apache-2.0、渲染底座可复用，换 UI 不碰渲染逻辑。"),
        use=(60, "60", "★183、Apache-2.0；做网页查看器 / 桌宠的渲染层样本。"),
        src="创建 · 推送 2025-07-07 · 183★ · Apache-2.0 · TypeScript · REST 实测 · 信源 [1408]",
    ),
    dict(
        nid="rpm42c7", name="evgo2017/vue-live2d —— Vue 组件：给网站博客加看板娘（★166）",
        url="https://github.com/evgo2017/vue-live2d",
        lang="Vue", stars="166",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="Vue 组件，为网站博客增加一只 Live2D 看板娘，2026-01 仍在推。",
        analogy="和 plugin-live2d 同理，但站在 Vue / Nuxt 生态；按自己站点框架选抄哪条。",
        ext=(66, "66", "MIT、Vue 生态现成组件，适合 Vue/Nuxt 站点直接挂。"),
        use=(64, "64", "★166、MIT、维护中；Vue 站点的看板娘组件样本。"),
        src="创建 · 推送 2026-01-27 · 166★ · MIT · Vue · REST 实测 · 信源 [1409]",
    ),
    dict(
        nid="rpm42c8", name="Arisego/UnrealLive2D —— UE4/Unreal 引擎 Live2D 插件（★153）",
        url="https://github.com/Arisego/UnrealLive2D",
        lang="C++", stars="153",
        tags=[("t-make", "建模"), ("t-ok", "可用")],
        plain="UE4 插件，把 Live2D 模型接进 Unreal 引擎。",
        analogy="Live2D 多在 Unity / Web 跑，Unreal 路线少见；这条是 Unreal 侧的稀缺桥接。",
        warn="⚠️ 最后推送 2025-02，Cubism SDK 版本可能偏旧，接入前先核兼容性。",
        ext=(58, "58", "Unreal 路线里少见的 Live2D 桥接，MIT 可改；接口随 SDK 漂。"),
        use=(50, "50", "★153、MIT；Unreal 项目挂 Live2D 的参考骨架。"),
        src="创建 · 推送 2025-02-26 · 153★ · MIT · C++ · REST 实测 · 信源 [1410]",
    ),
    dict(
        nid="rpm42c9", name="redchenk/yachiyo-live2d-studio —— Live2D 工作室（★25 · 新）",
        url="https://github.com/redchenk/yachiyo-live2d-studio",
        lang="JavaScript", stars="25",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="Live2D 工作室（yachiyo-live2d-studio），2026-10-11 当天推送，MIT，当前无描述。",
        analogy="当天建仓即 MIT、当天活跃，定位「studio」值得盯；先登记，待 README 补全再评落地性。",
        ext=(35, "35", "刚建，架构未知；等 README 出来再评。"),
        use=(25, "25", "★25、太新，当观察对象，别当依赖。"),
        src="创建 · 推送 2026-10-11 · 更新 2026-10-11 · 25★ · MIT · JavaScript · REST 实测 · 信源 [1411]",
    ),
    dict(
        nid="rpm42c10", name="ImDuck42/Live2D-Viewer —— 开箱即用的浏览器端 Live2D 查看器（★14 · ①落地）",
        url="https://github.com/ImDuck42/Live2D-Viewer",
        lang="JavaScript", stars="14",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="原生 JS + PIXI.js 6.5.10 + pixi-live2d-display，支持 Cubism 2.1(.moc) 与 3/4(.moc3)。"
              "四种载入：URL 直链 / 预设下拉 / GitHub 仓库浏览器（输 owner+repo 直接导入）/ 本地 ZIP 拖拽（JSZip 全客户端解压）。",
        analogy="本辑 gh 路唯一标「落地」的查看器：不用装软件，本地 `python -m http.server` 或 GitHub Pages 就能跑，"
                 "而且「输 GitHub 仓库直接看模型」这个能力对索引站预览 Live2D 模型是直接可抄的样本。",
        ext=(80, "80", "模块化重构到 v5.1（js/ 目录），四种载入路径都是独立函数，加新来源只改一处。"),
        use=(82, "82", "★14 但 MIT、开箱即用、有在线 demo；对「在索引站嵌一个 Live2D 预览器」是直接可改的样本。"),
        src="创建 · 推送 2026-06-17 · 14★ · MIT · JavaScript · REST 实测 · 信源 [1412]",
    ),
    dict(
        nid="rpm42c11", name="sweetcornna/OneClick2D —— 不碰 Cubism 授权的替代 2D 形象草稿工具（★0 · 新）",
        url="https://github.com/sweetcornna/OneClick2D",
        lang="Python", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="「先合规、重隐私」的二次元插画→可编辑 2D 形象草稿工具箱 + 开放规范：导出自研 `.oc2d` 工程 + 分层 PSD，"
              "明确不做 Cubism `.moc3`（绕开 Live2D 许可）。",
        analogy="多数 Live2D 工具卡在 Cubism 授权上；这条走「不碰 Cubism」的替代格式，对版权敏感场景是稀缺思路。",
        warn="⚠️ ★0、无 LICENSE、非 moc3，不能当 Live2D 绑定工具用。",
        ext=(55, "55", "思路稀缺：自研开放格式 + 明确不碰 Cubism 授权；可借鉴其合规设计。"),
        use=(40, "40", "★0、早期项目；当「替代格式」设计参考，别当成品。"),
        src="创建 · 推送 2026-08-08 · 0★ · 无许可证 · Python · REST 实测 · 信源 [1413]",
    ),

    # ---------- B. AI × Live2D 数字人 / 桌宠 ----------
    dict(
        nid="rpm42c12", name="andyhuo520/openclaw-assistant-mvp —— Electron AI 语音助手 + Live2D（★408）",
        url="https://github.com/andyhuo520/openclaw-assistant-mvp",
        lang="JavaScript", stars="408",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="Electron 版 AI 语音助手 + Live2D 角色动画：实时语音识别 + TTS，Live2D 随对话做表情 / 口型。",
        analogy="「AI 对话 + Live2D 脸」的最小 MVP 样本，结构清楚，适合抄整套闭环。",
        warn="⚠️ 无 LICENSE，商用先问作者；索引里另有同名 OpenClaw（MCP 长期记忆服务器），非同一仓库。",
        ext=(70, "70", "Electron+Live2D+语音闭环样本，模块可拆。"),
        use=(55, "55", "★408、无许可证；参考闭环结构，商用先授权。"),
        src="创建 · 推送 2026-02-13 · 408★ · 无许可证 · JavaScript · REST 实测 · 信源 [1414]",
    ),
    dict(
        nid="rpm42c13", name="MIO-456/Lumi_Nox —— 两个 AI VTuber 同台直播的实时编排（★239）",
        url="https://github.com/MIO-456/Lumi_Nox",
        lang="Python", stars="239",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="「两个 AI VTuber 同台直播」的实时引擎与编排，open-core，号称已被日更直播实战检验。",
        analogy="多 Agent 同台 VTuber 的编排思路稀缺且 MIT，适合做「多数字人联动」参考。",
        warn="⚠️ open-core 意味着核心外可能有闭源部分。",
        ext=(72, "72", "多 AI 角色同一直播间的编排/调度开源核，思路稀缺。"),
        use=(60, "60", "★239、MIT、2026-08 活跃；多数字人联动的编排参考。"),
        src="创建 · 推送 2026-08-14 · 239★ · MIT · Python · REST 实测 · 信源 [1415]",
    ),
    dict(
        nid="rpm42c14", name="YuriCrystal/ai-avatar-bot —— Live2D/VRM 语音 AI 形象，一行嵌入网站（★203）",
        url="https://github.com/YuriCrystal/ai-avatar-bot",
        lang="JavaScript", stars="203",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="Live2D / VRM 语音 AI 形象：口型同步 + 知识库 + 运营后台 + 支持分析，一行嵌入网站。",
        analogy="站外嵌入型 AI avatar 的完整前端样本，想给网站加个会说话的虚拟形象可直接抄。",
        warn="⚠️ 许可证标 NOASSERTION（含糊），先别商用。",
        ext=(65, "65", "站外嵌入型 avatar 完整前端，模块齐。"),
        use=(58, "58", "★203、NOASSERTION；嵌入网站型 avatar 参考，商用先确权。"),
        src="创建 · 推送 2026-07-18 · 203★ · NOASSERTION · JavaScript · REST 实测 · 信源 [1416]",
    ),
    dict(
        nid="rpm42c15", name="inni918/warashi —— 免费开源桌面 AI 伴侣：Live2D + 语音 + 长期记忆（★119）",
        url="https://github.com/inni918/warashi",
        lang="Python", stars="119",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="免费开源桌面 AI 伴侣：Live2D 形象 + 语音对话 + 长期记忆 + 主动搭话（proactive conversation）。",
        analogy="技术栈正中我们的基准（Python + 长期记忆 + 主动对话），本地 Ollama 路线可直接借鉴其记忆模块。",
        warn="⚠️ NOASSERTION 许可证。",
        ext=(70, "70", "本地 Ollama 路线契合（Python + 长期记忆 + 主动对话），记忆模块可借鉴。"),
        use=(62, "62", "★119、NOASSERTION；本地 AI 桌宠参考，记忆/主动对话部分有用。"),
        src="创建 · 推送 2026-08-18 · 119★ · NOASSERTION · Python · REST 实测 · 信源 [1417]",
    ),
    dict(
        nid="rpm42c16", name="funnycups/petto —— Flutter/Dart 智能 Live2D 桌面助手（★119）",
        url="https://github.com/funnycups/petto",
        lang="Dart", stars="119",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="智能 Live2D 桌面助手（petto），Flutter/Dart 实现，跨平台。",
        analogy="Flutter 路线里少见的 Live2D 桌宠，给不用 Electron/Tauri 的团队一个选项。",
        warn="⚠️ GPL-3.0 传染。",
        ext=(58, "58", "Flutter 路线罕见样本，跨平台；GPL 传染需注意。"),
        use=(50, "50", "★119、GPL-3.0；Flutter 桌宠参考。"),
        src="创建 · 推送 2025-12-05 · 119★ · GPL-3.0 · Dart · REST 实测 · 信源 [1418]",
    ),
    dict(
        nid="rpm42c17", name="Nav-Joe/Xue_CyberNeko —— 轻量「Live2D AI Neko」（★7 · 新）",
        url="https://github.com/Nav-Joe/Xue_CyberNeko",
        lang="TypeScript", stars="7",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="把 Live2D 形象接 AI 对话的轻量项目，2026-10-11 当天建仓、MIT。",
        analogy="小而新的 AI+Live2D 样本，MIT；刚建，待观察。",
        ext=(35, "35", "小样本，架构轻；观察用。"),
        use=(25, "25", "★7、MIT、当天建；观察对象。"),
        src="创建 · 推送 2026-10-11 · 7★ · MIT · TypeScript · REST 实测 · 信源 [1419]",
    ),
    dict(
        nid="rpm42c18", name="DesktopPetXuansi/Xuansi —— Windows 本地 AI 桌宠：屏幕理解+语音+记忆+Live2D（★1 · 新）",
        url="https://github.com/DesktopPetXuansi/Xuansi",
        lang="Python", stars="1",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="玄司 Xuansi：Windows 本地 AI 桌宠，屏幕理解 + 语音对话 + 长期记忆 + Live2D，纯本地。",
        analogy="定位正中我们的基准需求（16GB + 本地 Ollama，纯本地不联网）；★1 太新但 Apache-2.0 协议友好，值得盯。",
        ext=(55, "55", "纯本地优先，Apache-2.0，契合本机基准；观察其本地推理栈。"),
        use=(45, "45", "★1、Apache-2.0、本地优先；本地 AI 桌宠的方向标。"),
        src="创建 · 推送 2026-10-11 · 1★ · Apache-2.0 · Python · REST 实测 · 信源 [1420]",
    ),
    dict(
        nid="rpm42c19", name="ReSerendipity/SpiritPal —— Tauri v2 + Pixi.js 8 Live2D 跨平台桌宠（★0 · 新）",
        url="https://github.com/ReSerendipity/SpiritPal",
        lang="TypeScript", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="桌边友：跨平台 AI 桌面宠物，Tauri v2（Rust + React 19）+ Pixi.js 8 Live2D + 本地记忆召回。",
        analogy="技术栈最新（Pixi.js 8 而非旧 pixi-live2d-display）的稀缺样本，是「2026 新写法」的参考；★0 但协议好。",
        ext=(68, "68", "技术栈最新（Pixi.js 8 + Tauri v2 + React 19），「2026 新写法」参考。"),
        use=(50, "50", "★0、Apache-2.0；新写法样本，值得盯渲染栈选型。"),
        src="创建 · 推送 2026-10-11 · 0★ · Apache-2.0 · TypeScript · REST 实测 · 信源 [1421]",
    ),
    dict(
        nid="rpm42c20", name="HELPMEEADICE/BANDORI-PET-REV —— Live2D Cubism SDK+PySide6 桌宠：51+角色/305+服装（★465）",
        url="https://github.com/HELPMEEADICE/BANDORI-PET-REV",
        lang="Python", stars="465",
        tags=[("t-make", "建模"), ("t-ok", "可用"), ("t-new", "新")],
        plain="BandoriPet：基于 Live2D Cubism SDK + PySide6 的开源桌面宠物，支持 51+ 位 BanG Dream! 角色、305+ 套服装。"
              "自研 LuaJIT 渲染核心（基于 Live2D-v2-Lua），较原 live2d-py 提升 6 倍+（30fps→180fps+），"
              "支持头部追踪/拖拽/点击；LLM 角色扮演 + 好感度记忆；Qwen3TTS 口型同步 + 本地 faster-whisper ASR。",
        analogy="本辑最硬指标的桌宠：模型量（50+/300+）与自研渲染核（6x+）都是可验证数字，对本机桌宠体感研究价值最高；"
                 "且它把「Qwen3TTS 口型 + faster-whisper ASR + 本地 LLM 记忆」这条本地栈跑通了，正中本机基准。",
        warn="⚠️ GPL-3.0 传染、且依赖官方 Cubism SDK（须自按 Live2D 条款装）。Gitee 的 boomer001/BANDORI-PET-REV 是其镜像，不重复收。",
        ext=(85, "85", "自研渲染核 + 完整本地栈（Qwen3TTS/faster-whisper/LLM 记忆），是可复用的工程样本。"),
        use=(78, "78", "★465、GPL-3.0、指标硬；本地 AI 桌宠工程的标杆样本，抄架构不抄依赖。"),
        src="创建 · 推送 2026-10-06 · 465★ · GPL-3.0 · Python · REST 实测 · 信源 [1422]",
    ),
    dict(
        nid="rpm42c21", name="waterfeet/DoroPet_V3 —— Gitee 原生 Live2D AI 桌宠：对话+语音+养成+Galgame（★7）",
        url="https://gitee.com/waterfeet/DoroPet_V3",
        lang="Python", stars="7",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="DoroPet：智能桌面伴侣，集 Live2D 桌宠 + AI 对话 + 语音交互 + 养成 + Galgame 叙事 + 音乐播放器。"
              "PyQt5 + PyQt-Fluent-Widgets GUI；Live2D 走 live2d-py + OpenGL v3；AI 接 OpenAI 兼容多厂商（含 Ollama）；"
              "语音 sherpa-onnx + edge-tts；SQLite 存记忆；唤醒词 Hey Doro + 四大养成属性 + Galgame 多结局。",
        analogy="Gitee 侧少见的功能完整 Live2D AI 桌宠，而且它把「live2d-py + Ollama + sherpa-onnx/edge-tts + SQLite 记忆」"
                 "这条本地栈讲得很全，和本机基准几乎一致，是最该抄架构的一条。",
        warn="⚠️ ★7 偏小、Gitee 生态；README 自述 MIT 与仓库 LICENSE 文件（Apache-2.0）不一致，以 LICENSE 文件 Apache-2.0 为准。",
        ext=(75, "75", "架构最贴近本机栈（live2d-py+Ollama+sherpa-onnx/edge-tts+SQLite），模块拆分清晰。"),
        use=(68, "68", "★7、Apache-2.0、功能完整；本地 AI 桌宠架构参考首选之一。"),
        src="创建 2026-02-10 · 更新 2026-07-23 · 7★ · Apache-2.0 · Python · Gitee API 实测 · 信源 [1423]",
    ),
    dict(
        nid="rpm42c22", name="chyinan/Kokoro-Engine —— Rust 跨平台虚拟角色沉浸式交互引擎（★156）",
        url="https://github.com/chyinan/Kokoro-Engine",
        lang="Rust", stars="156",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="跨平台虚拟角色沉浸式交互引擎（Rust 实现），定位接近轻量版 VTuber / 数字人运行时。",
        analogy="Rust + 跨平台 + 虚拟角色交互引擎，给不用 Electron 的团队一个高性能运行时选项。",
        warn="⚠️ 描述未明示是否直接吃 Live2D .moc3，接前先核格式。",
        ext=(62, "62", "Rust 跨平台运行时，性能取向；格式兼容待核。"),
        use=(55, "55", "★156、MIT、2026-09 活跃；高性能数字人运行时参考。"),
        src="创建 · 推送 2026-09-24 · 156★ · MIT · Rust · REST 实测 · 信源 [1424]",
    ),
    dict(
        nid="rpm42c23", name="aurel-g/ComfyUI-Live2DViewer —— ComfyUI 节点：工作流里预览 Live2D 模型（★0）",
        url="https://github.com/aurel-g/ComfyUI-Live2DViewer",
        lang="JavaScript", stars="0",
        tags=[("t-make", "建模"), ("t-new", "新")],
        plain="ComfyUI 节点：把 Live2D 模型放进 web/vtuber 目录即可在节点预览，对应「AI 绘画 → Live2D 流水线」最后一环可视化。",
        analogy="「AI 生图 → Live2D 形象」流水线缺的往往是最后一环「看得见」；这条把预览嵌进 ComfyUI 工作流，是补环样本。",
        warn="⚠️ ★0、仅一次初始提交（2024-12 建仓即停），多年未动，做产品前可能要自己续维护。",
        ext=(50, "50", "ComfyUI 生态罕见 Live2D 查看节点，补「AI→Live2D 流水线」可视化环。"),
        use=(38, "38", "★0、MIT、多年未动；补环样本，维护需自理。"),
        src="创建 · 推送 2024-12-21 · 0★ · MIT · JavaScript · REST 实测 · 信源 [1425]",
    ),
]

FOOTNOTES = [
    (1403, "https://github.com/ezshine/AwesomeLive2D", "ezshine/AwesomeLive2D",
     "411★ · 无许可证 · 创建/推送 2023-12-19 · REST 实测 · Live2D 模型/资源 awesome 清单，约 3 年未动，作导航用"),
    (1404, "https://github.com/TSKI433/hime-display", "TSKI433/hime-display",
     "254★ · GPL-3.0 · JavaScript · 推送 2026-03-30 · REST 实测 · Live2D/Spine/MMD/VRoid 四格式统一查看器"),
    (1405, "https://github.com/LIlGG/plugin-live2d", "LIlGG/plugin-live2d",
     "251★ · MIT · TypeScript · 推送 2026-09-29 · REST 实测 · Halo 博客平台 Live2D 看板娘插件"),
    (1406, "https://github.com/amorist/platelet", "amorist/platelet",
     "226★ · GPL-3.0 · JavaScript · 推送 2026-10-05 · REST 实测 · 经典「血小板」网页看板娘 widget"),
    (1407, "https://github.com/iCharlesZ/vscode-live2d-models", "iCharlesZ/vscode-live2d-models",
     "169★ · 无许可证 · 推送 2026-03-25 · REST 实测 · VSCode 看板娘模型库（资源集合）"),
    (1408, "https://github.com/LSTM-Kirigaya/Live2dRender", "LSTM-Kirigaya/Live2dRender",
     "183★ · Apache-2.0 · TypeScript · 推送 2025-07-07 · REST 实测 · Web 端新版 Live2D 渲染封装"),
    (1409, "https://github.com/evgo2017/vue-live2d", "evgo2017/vue-live2d",
     "166★ · MIT · Vue · 推送 2026-01-27 · REST 实测 · Vue 组件：网站博客加 Live2D 看板娘"),
    (1410, "https://github.com/Arisego/UnrealLive2D", "Arisego/UnrealLive2D",
     "153★ · MIT · C++ · 推送 2025-02-26 · REST 实测 · UE4/Unreal 引擎 Live2D 插件"),
    (1411, "https://github.com/redchenk/yachiyo-live2d-studio", "redchenk/yachiyo-live2d-studio",
     "25★ · MIT · JavaScript · 推送 2026-10-11 · REST 实测 · Live2D 工作室，当天建仓，待 README 补全"),
    (1412, "https://github.com/ImDuck42/Live2D-Viewer", "ImDuck42/Live2D-Viewer",
     "14★ · MIT · JavaScript · 推送 2026-06-17 · REST 实测 · 浏览器端 Live2D 查看器，四种载入方式，①落地"),
    (1413, "https://github.com/sweetcornna/OneClick2D", "sweetcornna/OneClick2D",
     "0★ · 无许可证 · Python · 推送 2026-08-08 · REST 实测 · 不碰 Cubism 授权的 .oc2d 替代格式草稿工具"),
    (1414, "https://github.com/andyhuo520/openclaw-assistant-mvp", "andyhuo520/openclaw-assistant-mvp",
     "408★ · 无许可证 · JavaScript · 推送 2026-02-13 · REST 实测 · Electron AI 语音助手 + Live2D"),
    (1415, "https://github.com/MIO-456/Lumi_Nox", "MIO-456/Lumi_Nox",
     "239★ · MIT · Python · 推送 2026-08-14 · REST 实测 · 双 AI VTuber 同台直播实时编排，open-core"),
    (1416, "https://github.com/YuriCrystal/ai-avatar-bot", "YuriCrystal/ai-avatar-bot",
     "203★ · NOASSERTION · JavaScript · 推送 2026-07-18 · REST 实测 · Live2D/VRM 语音 AI 形象，一行嵌入网站"),
    (1417, "https://github.com/inni918/warashi", "inni918/warashi",
     "119★ · NOASSERTION · Python · 推送 2026-08-18 · REST 实测 · 桌面 AI 伴侣：Live2D+语音+长期记忆+主动搭话"),
    (1418, "https://github.com/funnycups/petto", "funnycups/petto",
     "119★ · GPL-3.0 · Dart · 推送 2025-12-05 · REST 实测 · Flutter/Dart 智能 Live2D 桌面助手"),
    (1419, "https://github.com/Nav-Joe/Xue_CyberNeko", "Nav-Joe/Xue_CyberNeko",
     "7★ · MIT · TypeScript · 推送 2026-10-11 · REST 实测 · 轻量 Live2D AI Neko，当天建仓"),
    (1420, "https://github.com/DesktopPetXuansi/Xuansi", "DesktopPetXuansi/Xuansi",
     "1★ · Apache-2.0 · Python · 推送 2026-10-11 · REST 实测 · Windows 本地 AI 桌宠：屏幕理解+语音+记忆+Live2D"),
    (1421, "https://github.com/ReSerendipity/SpiritPal", "ReSerendipity/SpiritPal",
     "0★ · Apache-2.0 · TypeScript · 推送 2026-10-11 · REST 实测 · Tauri v2+Pixi.js 8 Live2D 跨平台桌宠"),
    (1422, "https://github.com/HELPMEEADICE/BANDORI-PET-REV", "HELPMEEADICE/BANDORI-PET-REV",
     "465★ · GPL-3.0 · Python · 推送 2026-10-06 · REST 实测 · Cubism SDK+PySide6 桌宠，51+角色/305+服装，自研渲染核 6x+"),
    (1423, "https://gitee.com/waterfeet/DoroPet_V3", "waterfeet/DoroPet_V3",
     "7★ · Apache-2.0 · Python · 更新 2026-07-23 · Gitee API 实测 · Live2D AI 桌宠：对话+语音+养成+Galgame，live2d-py+Ollama"),
    (1424, "https://github.com/chyinan/Kokoro-Engine", "chyinan/Kokoro-Engine",
     "156★ · MIT · Rust · 推送 2026-09-24 · REST 实测 · Rust 跨平台虚拟角色沉浸式交互引擎"),
    (1425, "https://github.com/aurel-g/ComfyUI-Live2DViewer", "aurel-g/ComfyUI-Live2DViewer",
     "0★ · MIT · JavaScript · 推送 2024-12-21 · REST 实测 · ComfyUI 节点预览 Live2D 模型，多年未动"),
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

    desc = ('第三十八辑三路调研（gh 路 24 条 / cn 路 18 条 / official 路 16 条），本版取 23 项，'
            '主题 **「Live2D 制作全谱系补采：从查看器到 AI 数字人」**。'
            '所有 ★ / 许可证 / 语言 / 创建·推送·更新日全部走 GitHub REST API 逐条实测（子 agent 报的候选已由主 agent 复核，零 404）。'
            '<strong>本辑主线：① 「AI 装一个 Live2D 身体」从上一辑的**主张**继续变成**重复模式** —— '
            '本辑新增 12 条 AI×Live2D 数字人/桌宠（openclaw / Lumi_Nox / warashi / BANDORI-PET-REV / DoroPet_V3 / SpiritPal 等），'
            '且它们收敛出一条可复用的本地栈：**Live2D 渲染（pixi-live2d / live2d-py）+ 本地 LLM（Ollama / Qwen3）+ TTS（edge-tts / sherpa-onnx / Qwen3TTS）+ ASR（faster-whisper）+ 长期记忆（SQLite / JSON）**；'
            '② 查看器/插件侧补齐多格式（hime-display 四格式）、多框架（plugin-live2d / vue-live2d / UnrealLive2D）、以及唯一标「落地」的网页查看器 ImDuck42/Live2D-Viewer；'
            '③ 合规侧出现「不碰 Cubism 授权」的替代格式思路（OneClick2D 的 .oc2d）；'
            '④ 硬指标样本 BANDORI-PET-REV（★465、自研渲染核 6x+、51+ 角色/305+ 服装）把「本地 AI 桌宠工程」拉到可验水位。</strong>'
            '️ 待办：脚注区漂移（[1301]-[1378] 嵌在 card rpm38c4 内）仍待修，本版脚注按既有规则接在最后一条旧脚注之后。')

    block = ['    <div class="group" data-page-node-id="rpm42g">',
             '      <div class="group-title" data-page-node-id="rpm42gt">🆕 第四十二版增补 · Live2D 制作全谱系补采：工具/查看器/插件 + AI 数字人（23 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm42gd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm42r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm42ra%s">%s</a> — %s</div>'
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
    print("   页头：1403 → 1426 项；卡片 1386 → %d" % (1386 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
