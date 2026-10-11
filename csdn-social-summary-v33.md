# 跨平台游戏制作 × AI 开发资源梳理（2026-10-11 · 第三十三辑 · **轮子开始分叉：一边继续攻 moc3，一边干脆绕开**）

> 本辑为 Live2D 连续第九轮。**这一辑没有新的「拆墙者」，但出现了两件结构性的东西：**
> ① 官方 **5.4 alpha2 手册正文第一次被读完** —— 里面既有对制作小白直接有用的 **PSD 导入增强**，
> 也有一条**单向门**式的数据兼容警告，且 **alpha 可用期 10/18 到期（距本辑 7 天）**；
> ② 桌宠线上出现一个**被写成架构主张的范式**：「**你的桌宠不需要大脑**」——
> 不给你一个新 AI，而是**给你已有的 ta 装一具身体**。
> 三路候选：gh 33 条（+13 行边缘登记） · cn 19 条 · official 26 条；落索引 **24 卡**（1301 → **1325**）。
> 所有 ★ / 许可证 / 日期均走 `gh api repos/<r>` 实取，**主 agent 已把 34 个候选仓库逐条复验**（见 §四）。

---

## 一、上轮待办检查（7 条 → **闭环 3 条 / 顺延 4 条**）

| # | 上轮待办 | 状态 | 结果一句话 |
|---|---|---|---|
| ① | **实际装 `Agent-desktop-pet`**（先读 THIRD-PARTY.md） | ⚠️ **半闭环** | **许可边界读清了，但装不上** —— 它要求 **64 位 CPython 3.12**（`vendor/` 里的二进制按 3.12 编译），本机只有 3.13.12 与 3.11.9。详见 §五 |
| ② | **复查 `ayagami` 进度**（每辑一次） | ✅ | **本轮无推进**：GitHub **无任何 release**；crates.io 上 `ayagami` 只占了个名（`0.0.0-reserved`，2026-06-14 建，**未真正发布**）；代码最后推送仍是 **2026-09-14** |
| ③ | `/skill-doctor` | ❌ 顺延 | **连续第十二轮** |
| ④ | 实装 airi 的 Windows 包 | ❌ 顺延 | — |
| ⑤ | **核 Inochi2D v0.8.6 MSI 在 Win11 能不能跑** | ✅ | **静态核完**（下载 MSI+zip 实测，非猜测）：**没有 OS 版本闸门**、x64、自带 SDL2/freetype、用了 Win10 1703+ 的 DPI API → **Win11 无结构性障碍**；真实风险只有两个：**需要 VC++ 运行库** + **依赖 OpenGL 驱动**。详见 §五 |
| ⑥ | **决策原则瘦身**（224 行超 200） | ❌ 顺延 | 本轮上下文被 §五 的实测吃掉 |
| ⑦ | **给 `doc_ref_check` 补 C4** | ✅ | **已落地并自证**：`--selftest` **9/9 → 12/12**；C4 = 「同文件同一量多处声明须两两相等」（M-0032）。详见 §六 |

> ③ 这条已顺延十二轮。**它不是一个"待办"，是一个信号**：说明「给自己做工具」这件事永远排在「给索引加内容」后面。
> 下轮把它**排在所有调研动作之前**（先做，做完再开三路）。

---

## 二、本辑一句话

**上一辑有人正面拆了「渲染 moc3」那堵墙；这一辑的看点不在墙，而在墙两侧长出了两丛完全不同的轮子 ——
一丛继续攻格式（开源解析、自研渲染器），另一丛干脆不碰 `.moc3`（自研运行时 + 把「拆图」这一步自动化）。
同时，官方那条 alpha 线给了一个硬期限：想试 5.4 的新能力，只剩 7 天；而它存出来的文件，旧版打不开。**

---

## 三、主线一：官方 5.4 alpha2 手册（本辑唯一「一手正文级」新增）

### 1. Editor 5.4 alpha2 用户手册 —— 两节新增，其中一节直接改 PSD 准备流程

- URL：https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html （页首 `09/07/2026`）
- **① PSD 导入增强（对做模型的人最有用）**：官方原文 ——
  `Previously, a PSD with a "1 layer = 1 ArtMesh" structure was required, but now PSDs with a "merged multiple layers = 1 ArtMesh" structure can also be imported as-is.`
  也就是说：**以前 PSD 必须一层对一个 ArtMesh，现在多层可以合并当一个**；合并图层组、合并蒙版、除尘这些**原先靠 Photoshop 脚本做的事，搬进了编辑器**。
  两个坑写在手册里：**不想被合并的图层组，名字前加 `*`**；**别带调整图层或图层效果**。
- **② 数据兼容（单向门）**：`Models saved with 5.4.00 alpha2 cannot be loaded in 5.4.00 alpha1 or editors prior to 5.3.`
  并补一刀：`since this is an alpha version, there is no guarantee that it will be loadable in future 5.4.00 beta or later editors.`
  → **翻译成人话：用 alpha2 存过的正式工程，旧版打不开，未来的 beta 也不保证打不开 —— 别拿它存真东西。**
- **社区验真**：论坛有用户正好踩坑求「回退 alpha1」（https://creatorsforum.live2d.com/t/3976 ，2026-09-16），
  官方回复明确 **不支持前向兼容**（`前方互換には対応しておらず`）。这是官方正文之外的真实世界佐证。
- 可复用性：**落地**。理由：① PSD 合并能力**只在 alpha2**（正式的 5.3.04 没有）；② 而 alpha2 存的文件是单向门 → **做法是：另存副本再试，别覆盖原文件**。

### 2. ⏰ 时间敏感：5.4 alpha 可用期 **截至 2026-10-18**（距本辑 7 天）

- URL：https://www.live2d.com/en/information/cubism-5_4-alpha/ ·
  https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html
- 原文：`Available until "October 18, 2026." After this date, the alpha version will no longer be available.`
- 可复用性：**落地** —— 想试「多层合并导入 PSD」的，**10/18 前**；过期后这一入口整体下线，只能等 beta。**这是本辑唯一有期限的结论。**

### 3. 官方口径复核（**三路主干的版本口径本轮逐条未变**）

| 项 | 本轮复核结果 | 对比上一辑 |
|---|---|---|
| Editor 正式版 | **5.3.04（2026-09-03）**，页内**无 5.3.05** | 未变 |
| Release History 大表 | 最新仍 `09/03/2026 · Cubism 5.3.04`，**5.4 未进表**（只在页顶横幅） | 未变 |
| 产品页 `cubism/update` | 仍写 **Ver.5.3.00** —— **与 docs 表 5.3.04 冲突连续第 3 轮未修** | 未变 |
| SDK 术语 | **Cubism 5 SDK = ≤R6 / Cubism 5.4 SDK = ≥R7 alpha1** | 未变 |
| SDK 两条破坏性变更 | ① Unity **模型计算顺序**改了（物理结果与 R5 不同）② **Json Version Tag** 认不出就加载失败 | 未变 |
| SDK 公告主线 | 最新仍 **Unreal R1 beta2（2026-09-29）**；**主线无 R6/R7** | 未变 |
| 官网新闻 | 首条仍 **2026.07.17**，近 3 个月无新增 | 未变 |
| GitHub org `Live2D` | 最近推送仍 **2026-09-29**，**无 R7 tag** | 未变 |
| 5.4 SDK alpha2 手册 | **404** —— Editor 有 alpha2，**SDK 手册仍停在 alpha1** | 新增探测 |
| 竞品 Spine | 正式版仍 **4.3.26（2026-09-07）**，4.3.27 Unreleased | 未变 |
| Inochi2D | `inochi-creator` 最新仍 **v0.8.6（2024-09-18）** | 未变 |

> **一句话给小白**：你该装的还是 **5.3.04**；5.4 现在只有 alpha（10/18 下线），**看可以，存不行**。

---

## 四、主线二：「大脑和身体分离」—— 桌宠线第一次出现被写清楚的架构主张

### 1. `zziying/ai-live2d-body`（★46）—— 一份「为什么不用现成框架」的设计文档

- URL：https://github.com/zziying/ai-live2d-body （README.md + human-guide.md，**目录只有 2 个文件**）
- 主张：airi / Open-LLM-VTuber 这类框架会**给你一个新的 AI**（人格来自框架自己的 prompt、记忆存框架自己的库）；
  本篇主张**桌宠没有大脑**，只做三件事：① 显示 ta 的状态 ② 把你的触摸传回 ta 的 session ③ 给 ta 一套身体 API。
  配套代码版 `zziying/ai-live2d-body-starter`（★17）。
- 可复用性：**参考（当设计纲领）**。⚠️ **无许可证**、只有两份 md，**不是能依赖的项目**。
- **为什么这条重要**：它正对「已经有一个天天用的 agent」的人 —— **不是换一个新 AI，而是给已有的 ta 装身体**。

### 2. 同日期的「身体」侧供给（本方向本辑最密集）

| 项目 | ★ | 许可 | 一句话 | 可复用性 |
|---|---|---|---|---|
| `qiyueblues-design/zhuomianling`（桌面灵） | 27 | MIT | **Windows + local-first 的桌宠框架**，模型由用户自备；`docs/adr/0001-记忆权威账本.md` 把记忆层写成了架构决策，GPT-SoVITS 走配置文件接入 | **落地**（本机画像正面命中；27★ 三个月，先当框架读） |
| `kiyotakali/Miru` | 175 | Apache-2.0 | 本地优先 + 长期记忆 + 多端同步，**三平台都出安装包**（`Miru-Windows-x64-Setup.exe` / dmg / apk） | **落地→参考**（本辑最成熟） |
| `ice-only/localai-rag-live2d` | 21 | MIT | 本地 RAG + 长期记忆 + Live2D，体量小 | **参考**（已有 Ollama 的话改造成本最低） |
| `hhjk21/Firefly-Companion-AI-` | 27 | MIT | **双窗口解耦 + 鼠标穿透** + 本地 ONNX 语义记忆 + GPT-SoVITS | **参考**（工程结构可抄，**角色素材版权归米哈游，禁商用**） |
| `goodko/xiaozhi-ios` | 128 | MIT | iOS 端：Live2D 形象 + 实时语音 + **MCP 工具调用** | **参考**（本辑唯一像样的移动端） |
| `ochiru520/Mio` | 49 | MIT | Windows 本地优先 agent：对话/记忆/日记/语音/QQ/Live2D 一体 | **参考**（与桌面灵交叉对照） |
| `yuri-os/YuriOS` | 34 | Apache-2.0 | 「模型/记忆/角色三权归用户」，日更 | **参考**（口径最清楚，别被 slogan 带走） |
| `ExpiredPopsicle/SnekStudio` | 418 | GPL-3.0 | **Godot 4.7 写的 VTuber 软件，作者自述生产直播跑了 3 年**（只吃 **VRM 0.x**） | **参考**（3D 路线的重型对照，与 `.moc3` 不互通） |
| `menglimi/astrbot_plugin_live_stream_companion` | 58 | MIT | **B 站弹幕 → LLM → VTube Studio → OBS 字幕**全链打通，日更 | **参考/落地**（直播集成唯一全链） |
| `HanetakaChou/Brioche-Puppet` | 14 | LGPL-3.0 | 纯 C++ VTuber 软件，真三平台构建脚本 | **参考** |

---

## 五、上轮待办的两处实测（本辑的「动手」部分）

### 1. `Inochi2D inochi-creator v0.8.6` 在 Win11 能不能跑 —— **静态核完（下载实物解析，非猜测）**

- 方法：`gh api` 取 release asset → 下载 **MSI（23.96MB）** 与 **win32 zip（22.27MB）**，用自建 `_tools/msi_probe.py`
  读 MSI 的 Property / LaunchCondition 表，再用 PE 头解析主程序依赖。
- **结论：Win11 无结构性障碍**，证据三条：
  ① **MSI 里唯一的 LaunchCondition 是 `NOT WIX_DOWNGRADE_DETECTED`** —— **没有任何 OS 版本闸门**（不写 `VersionNT >= …`）；
  ② 主程序 `inochi-creator.exe` 是 **PE32+ / x86-64**，`MinimumOSVersion = 6.0`，**且引用了 Win10 1703+ 才有的 `SetProcessDpiAwarenessContext`** → 它本来就是按现代 Windows 编的；
  ③ DLL 依赖全部自带（`SDL2.dll` / `freetype.dll`），运行时只需 **`VCRUNTIME140.dll` + `VCRUNTIME140_1.dll`**（= 装一次 VC++ 2015–2022 x64 运行库）。
- **真实风险（不是"能不能跑"而是"跑得起来吗"）**：它依赖 **`OpenGL32.dll`** —— 在没装好显卡驱动的机器/虚拟机/远程桌面上，
  会退到微软的软件 OpenGL 1.1，**编辑器可能起不来或渲染异常**。这是唯一的实质风险点。
- 另外一条**顺手发现的**：v0.8.6 这个 2024-09 的 release 下，**2026-06-07 又新加了两个资产** `inpfix` / `inpfix.exe`（下载 358 次）——
  **"老 release 挂新资产"** 是又一个「`updated_at` 骗人」的形态。MSI 安装器**带简繁体中文语言包**（`zh-CN.mo` / `zh-TW.mo`）。
- 可复用性：**参考** —— 结论是「能装」，但编辑器本体**停更 2 年 1 个月**（v0.8.6 = 2024-09-18），
  **不买 Editor 这条路真正的短板从来不是能不能装，是没人再维护它**。
- 复现命令：`python _tools/msi_probe.py <path.msi>`（本轮新建，只读，不安装、不写注册表）。

### 2. `Agent-desktop-pet`（CodexPet 2.0）—— **许可读清了，但装不上**

- URL：https://github.com/shicheng5589-oss/Agent-desktop-pet （★20 · Python · **NOASSERTION** · 推送 2026-10-11 · 建 2026-09-25）
- **THIRD-PARTY.md 读到的许可边界**（这是上轮待办要的那一步）：
  - 仓库自己的代码是 **MIT**；但里面带的 **`live2dcubismcore.min.js` 是 Live2D 公司专有授权**（文件头写 "Redistributable Code"）——
    **可以随程序分发，但不能单独拿去卖/改许可**；
  - **`web/model/`（角色模型）的授权跟代码的 MIT 是两回事**，通常属于模型作者 —— 仓库自己也写明「别把别人的模型随仓库发到 GitHub」。
- **装不上的原因（本轮新发现，值得记一笔）**：README 的「运行环境」写死 **64 位 CPython 3.12**
  （`vendor/` 里的 `pythonnet` 等二进制是按 3.12 编译的）。**本机托管运行时是 3.13.12、系统是 3.11.9 —— 没有 3.12。**
- 可复用性：**参考**。理由：它是「agent 状态 → 表情」这条线里最完整的一个样本（12 个 Agent 状态 → 9 种表情、只读本地不联网），
  但**环境钉子比想象中硬**：要么装个 3.12，要么自己改 vendor。→ **顺延到下一轮**（下轮先决定：装 3.12 还是放弃）。

---

## 六、自测与「有用就改」（本辑落地的改动）

### 1. ✅ `doc_ref_check.py` 补 C4「同量一致」（上轮待办 ⑦，本辑闭环）

- **要解决的问题（M-0032）**：同一个文件里两处声明同一个量，改一处漏一处 —— **两边同时"看起来正常"，没有任何东西会报**。
- **判据设计（三条边界都是实测撞出来的，不是想出来的）**：
  1. 标签归一化 = **紧邻数字的两个字**（"又说落索引 1257 项" 与 "索引 1301 项" 视为同一个量）；
  2. **数字前面同行出现反引号标识符** → 判为「按条目罗列的明细行」，跳过 ——
     否则 `` `a/b` ★38 · 下载次数 38 次 `` 和 `` `c/d` ★51 · 下载次数 511 次 `` 会被当成"自相矛盾"（**首版实测假警**）；
  3. 标签前一个字是否定词（不/未/无/没/零）→ 跳过 —— 否则「路径**存在** 20 条」与「路径**不存在** 0 条」会撞车（**首版实测假警**）。
- **实测**：对 5 个真实文档跑 **0 假警**；`--selftest` 从 **9/9 → 12/12**（新增 N9 应红 / N10 应绿 / N11 两个假警回归位）。
- **已知盲区（写进脚本头注释）**：**跨文件**的同一个量对不上，C4 抓不到（如 `AGENTS.md` 的「1301 项」vs `index.html` 的真实卡数）——
  那属于「有外部真相」的闸门（`index_metrics.py`）的活，**不在这里重复造**。

### 2. ✅ 新建 `_tools/msi_probe.py`（只读解析 MSI 元数据）

- 用途：**"这包装不装得上"这个问题第一次有了不靠猜的答案** —— 读 Property / LaunchCondition / File 表 + PE 头依赖。
- 本轮已用它回答了 Inochi2D 那个悬了两轮的问题（§五.1）。

### 3. ⚠️ 收集到但**本轮不改**的（写清为什么）

- **「`updated_at ≠ pushed_at` 应成文规则」**（gh 路提出）：本辑至少 3 处靠 `pushed_at` 才识破假活
  （`Obs-Live2D-Plugin` updated 2026-09 但 **pushed 2020-06**；`LitStronger/live2d-moc3` updated 2026-10 但 **pushed 2021-02**；
  `inochi-creator` 老 release 挂新资产）。**建议落成「索引卡固定同时打印两个日期」** —— 但改卡片模板会动到 1290 张卡，
  **超上下文 → 留下一轮**（见 §九）。
- **榜单类**（Artificial Analysis 2026-10-11 快照 / `aichangelog.dev`）：与 Live2D 制作无关，**只作背景**，不落地。
  ⚠️ 顺手探明：`theaic.io` **仍 HTTP 000**（连续两轮）、`mlcommons.org`（MLPerf）**403（WAF，新探明）**。

---

## 七、中文侧（真正有硬信息的三块，其余被农场淹没）

### 1. 律所解读《〈人工智能拟人化互动服务管理暂行办法〉施行满月》—— **本辑执行价值最高的一条**

- URL：https://www.lawzj.cn/news_view.aspx?TypeId=5&Id=1753&Fid=t2:5:2 （2026-08-28，卓建律所）
- **硬结论**：
  - **罚款其实不高**：拒不整改一般 **1–10 万元**，造成生命健康损害 **10–20 万元**；
  - **真正的强约束是分发渠道**：应用分发平台须核验安全评估与备案材料，**可不予上架 / 暂停 / 下架**；
  - **安全评估触发线（量化）**：**注册用户破 100 万，或月活超过 10 万**；
  - **三层递进义务**：① 持续展示 **AI 非真人身份标识** → ② 动态风险提示 → ③ **连续使用超 2 小时强制提醒**；
  - **易被忽视**：禁止用情感挽留话术（"再陪我一会"）阻碍退出。
  - 处理路径对照：豆包引导至第三方 App / 通义千问关入口 / 腾讯元宝 2026-06-30 关停 / 网易云"妙时" 2026-07-14 停运。
- 可复用性：**落地** —— 任何要把本地 LLM 桌宠**对外发布**的人，这三条（AI 标识 / 2 小时提醒 / 禁情感挽留）就是最低合规集。

### 2. 腾讯云官方文档《2D 端渲染场景概述》—— 商用 2D 数智人的预算基线

- URL：https://cloud.tencent.com/document/product/1240/118294
- 硬数字：SDK 包体 **Android 24MB → ≈7.5MB**、**iOS 38.8MB → ≈12.5MB**；基础模型包 **82MB → ≈58MB**；
  **V1.3 起首帧渲染延迟 1450ms → 450ms**；授权为**年包**（应用/设备/小程序三模式，**不含 TTS**）。
- 可复用性：**落地（当预算基线）**。⚠️ 是**商用授权**不是开源。

### 3. 米画师《语音对话助理 Live2D 形象设计》—— 一份可直接当规格书的需求单

- URL：https://www.mihuashi.com/projects/11719641 （预算 ¥1,000–3,000，试稿费 500 元/张）
- 可抄的部分：**要动的部位必须断开**（头发分前/后/侧缕、眼分眼白/瞳孔/高光/上下睫毛/眼皮、嘴分上唇/下唇/口腔内部…）；
  **可动部位必须画完整**（后脑勺头发画全、裙摆内侧画到 —— "只画到脸边缘一转头就穿帮"）；
  **分辨率建议 ≥2048×2048**；**转头幅度决定补画量**（要左右 30° 以上，必须补侧脸）；阴影/高光最好也分层。
- 可复用性：**落地**。⚠️ 与已收的米画师**承制橱窗**是不同条目（这条是**需求方发包单**）。

### 4. 其余（参考级）

- 掘金《XiaoMate 更新》：**同一个 app 内挂 Live2D + VRM + GLB + GLTF 四类模型**（Live2D 走 PIXI + Cubism 4，3D 走 Three.js，按扩展名自动选适配器）
  https://juejin.cn/post/7689485292671565878 （2026-09-27）· 项目 `oddmeta/xiaomate-desktop`（★4）
- 腾讯搜一搜盘点《从 29 元到 2000 元…》：软件派 **璇玑·貂蝉 29 元买断** / **桌面小猫 9.9 元、200+ 造型、用户破万**；
  **MeaPet**（Live2D+PNG 双渲染、对接 Ollama、SQLite 存记忆）/ **DoroPet**（8 种模型后端）；
  硬件派 **ropet 2000 元/台（卖出近 2 万台）** / **StackChan 59 美元（Kickstarter 超目标 45 倍）**
  https://so.html5.qq.com/page/real/search_news?docid=70000021_3096a9e153982452
- 今日头条《教你养"AI桌面宠物"》：把"本地部署"讲成两步 —— `ollama pull qwen:latest` + 地址填 `http://localhost:11434`
  https://m.toutiao.com/article/7687912255379489319
- 程序员客栈两条：`f25h-233/live2dpet`（★7 · GPL-3.0，**四进程 ZeroMQ IPC 解耦**：渲染/推理/TTS/监控 —
  "桌宠一卡全卡"的直接解法）· `mystiafly/Touhou_Pet`（★15，LangGraph ReAct + Qdrant + DataBank 记忆）
- 发行样本：indienova《不/存在的你，和我》主机版（PC 版 2024-12 上 Steam，**2 万+ 评测、93% 好评**；NS 港区 **38 港币**；主线约 2 小时）
  https://indienova.com/indie-game-news/the-noexistencen-of-you-and-me-nintendo-switch-ps4-ps5-released/
- `nanlingyin/SoulLink_Live2D`（★38）—— 一条可回查的「**口型不动**」排查法：有声音但「口 開閉」恒为 0.00 →
  逐个确认 ① TTS 播放时是否创建 `AnalyserNode` ② 音量是否映射到 `ParamMouthOpenY`（来源 CSDN `g470641382`，非 `weixin_*`）

---

## 八、负结论（**一律写「本轮未命中」，不写「不存在」**）

| 方向 | 本轮结果 | 查法入口 | 复测条件 |
|---|---|---|---|
| **「单图/提示词 → 可部署 `.moc3`」** | **零新增可信工具**：搜到的全部止步于「到自研运行时」或「到 PSD 绑定」 | GitHub 搜索 `image-to-live2d` / `moc3 export` / `one image live2d` | 出现真正产出 `.moc3` 的仓库 |
| **纯自研 `.moc3` 解析器** | 仍稀缺且玩具化（`moc3-rs` ★6、`jz315/…-sys` ★1 是"读"不是"渲"） | 同上 | 这条线已被 `ayagami` 占住 |
| **Cubism Editor 自动化** | **近零新增**（仅 `madosuki/live2dManager` ★1 其实是 Web SDK 封装） | GitHub `cubism editor api` | 上一辑 `CubismExternalEditMCP` ★34 已吃满 |
| **VTube Studio 官方/半官方插件** | **零命中**（官方 `DenchiSoft/VTubeStudio` ★1313 是 **API 文档仓**不是插件市场） | GitHub `vtuber studio plugin` | VTS 插件生态在 GitHub 基本空白 |
| **音频驱动口型（独立 lip-sync）** | 延续上辑**无独立命中**（都是整包在桌宠里） | GitHub `lipsync live2d` | 维持 |
| **知乎 / B 站正文** | **本轮仍取不到**：B 站检索触发敏感审批超时、知乎无正文级证据 | 站内搜索 + WebFetch | **下轮改人工浏览器取帖** |
| **HN / dev.to** | 仍无料：HN `live2d` **2167 命中全误召**（fuzzy 把 "lived/live diff" 算进来）；dev.to 仍 **2 篇**（最新 2026-06-08） | Algolia API / dev.to API | 出现标题含 Live2D 的非误召条目 |
| **退役源复测** | `Reddit` / `note.com` / `theaic.io` 均 **HTTP 000**（与退役名单一致，本辑已复测）；**`creatorsforum.live2d.com` 本轮 200**（进一步确认退役已回滚） | — | 每辑复测一次 |

**CSDN 侧**：教程类约**七成为 `weixin_*` 同模板农场**；`wenku.csdn.net/answer|column` 与 `blog.csdn.net/gitblog_*` 是站内 AI 聚合/AIGC 搬运 → 中文"Live2D 制作教程"几乎无可采一手料。

**本辑新增的编造留痕**（照旧登记，见到直接剔）：`bryh.cn/news/102191`（给 5.3 编造「物理参数调节范围扩大 40%」「帧率 +15~20fps」等精确数字，**官方日志查无任何百分比**）；
`tzjp.cn/news/73233` + CSDN `weixin_30843121`（上辑已判编造，**本轮带同文镜像再次浮出**，说明该批镜像仍在持续分发）；
`3dmplay.com.cn`（编造机构 "StatVista" 与「下载量环比激增 314%」）；`ruan6.com`（**破解教程**，合规风险）。
镜像农场族复现：`hqwc.cn` / `mhpq.cn` / `mhpn.cn` / `sheratonhq.com` / `live2d.net.cn` / `tzjp.cn` / `bryh.cn`。

---

## 九、索引与文档维护

- `index.html` **1301 → 1325**：新建 `insert_v38_cards.py` 增补 **24 卡**（脚注 `[1301]`–`[1324]`，新增分组 1 个 → 308 组）。
  跑前用 `insert_guard_probe.py` 对 v38 本身做保险丝验证（**6/6**：P0 语法 + 1 正 + 5 反）。
- **存档**：`cp csdn-social-summary.md csdn-social-summary-v32.md`（v32 = 第三十二辑全文）。
- **闸门（改前改后各跑一次）**：`index_metrics` E1–E7 + 恒等式（页头 1325 / 脚注 1324 / 卡片 1314）· `gate_recall_probe` 漏检 0 假警 0 ·
  `doc_ref_check` **12/12**（本辑补 C4）· `insert_guard_probe --selftest` 7/7 · `house_rules --check` 6/6 · `mistakes_seal` 33/33 ·
  `skill_budget` 21 技能 0 超预算 · `memory_health` rc=0。
- **本辑改动的共享文件**：`_tools/doc_ref_check.py`（补 C4 + 3 条自测）、`_tools/msi_probe.py`（新建）、
  `.workbuddy/memory/MEMORY.md`（闸门清单 19→20、`doc_ref_check` 9/9→12/12）、
  `~/.workbuddy/skills/round-research-index/SKILL.md`（闸门命令行补 C4）。
- **上轮留下的疑点，本辑未解（留指针）**：`daoming07280/live2d-auto-pipeline` ↔ `mw2wbyys6t-sudo/live2d-auto-pipeline`
  （同名不同 owner）· `empty-sekai/nnnotes-standalone` ↔ `MetaSekaiLab/nnnotes` —— 两条都**未核**。

---

## 十、下一辑待办（**按顺序做**）

1. **`/skill-doctor`** —— **连续第十二轮**。**排在所有调研动作之前**：先做，做完再开三路。
2. **`Agent-desktop-pet` 的环境钉子做决定**：装 3.12，还是改 `vendor/`？**本轮已把许可边界与阻塞点核清，只差一个决定。**
3. **`updated_at` vs `pushed_at` 落进卡片模板**（本辑至少 3 处靠它识破假活）—— 注意这是**动 1290 张卡的批量改动**，先设计低风险做法（如只加到 `src-line` 拼接处）。
4. **`wan-h/awesome-digital-human-live2d`（★2425）正面评一次** —— 本辑最大的漏网（两个辑都只登记未深评）。
5. **DSH 插件生态单独成辑**（`dsh-plugin-shop` ★1009 / `ds-harness-remote` ★309 / `dsh-plugin-registry`）——
   这是**本机所跑运行时自身**的生态，别再混在 Live2D 里。
6. **`ayagami` 进度复查**（每辑一次，本辑无推进）。
7. **决策原则瘦身**（`game-production-pipeline.md` 224 行超 200，照房规的做法：**压正文、不撤条款**）—— 连续第二轮顺延。
8. **上轮两条同源疑点收口**（见 §九）。
9. **人工浏览器取知乎/B站正文**（连续多轮被登录墙拦）。

---

*本辑三路候选：gh 33 条（+13 行边缘登记）· cn 19 条 · official 26 条；落索引 **24 卡**；*
*累计经验帖约 1490 → **约 1515 条**；索引 **1325 项**；房规 23 条 / 189 行；决策原则 23 条 / 224 行；mistakes **33 条**；*
*新建脚本：`insert_v38_cards.py`、`_tools/msi_probe.py`；新存档：`csdn-social-summary-v32.md`；闸门：`doc_ref_check` 补 **C4**（12/12）；*
***本辑最硬的两条：① 官方 5.4 alpha2 的「多层合并 PSD」真有用，但它存的文件是单向门，且 10/18 到期；② 桌宠线第一次有人把「你的 agent 不需要新大脑，只需要一具身体」写成了架构主张。***
