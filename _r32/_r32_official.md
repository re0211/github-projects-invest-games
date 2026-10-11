# R32 · Live2D 制作 × 实战测评 × 上新 —— official 路（官方 / 海外社区 / 榜单）

- 轮次：第 32 轮（连续第 8 轮做 Live2D）
- 调研日期：2026-10-11
- 对照基线：R31（同日）——Editor 5.3.04、SDK 分线版本（Unity R5+R4_2 / Unreal R1 beta2 / MotionSync R2_1 / Java R5 / Native·Web R5）、学生优惠 80% OFF（截止 2027-03-31）、AE Plugin R7
- 本轮硬任务：**补读 Cubism Editor 5.3.01 / 5.3.02 / 5.3.03 / 5.3.04「各自更新了什么」**（连续两轮欠账）
- 查重基线：`_r32\_dedupe_urls.txt`（1396 行，含 live2d 相关 46 行）
- 口径纪律：以结算页 > 首页；docs Release History 表 > 产品页；同一站内跨区块交叉验证

---

## 一、Cubism Editor 5.3.01–5.3.04 逐版 changelog（本轮硬任务）

> **来源唯一入口**：`https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/`（页面标题「Update history | Editor Manual」，正文首行注：`Note: Updates to the beta version are also reflected in the official version.`）。
> **口径说明**：官方把「beta1 写全套改动、正式版只写 beta 之后新增的修补」——所以某版本的实质内容要看它的 **beta1**，正式版条目常常只有一行。本页**不在** `_r32/_dedupe_urls.txt`（新入口，R31 只读了大版本表 `new-feature-introduction-title`，没进这个 patch 明细页）。

### 1. Cubism Editor **5.3.01** 更新了什么 · docs.live2d.com · 2026-02-24
- 地址：https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/
- 原文证据：
  > `5.3.01 (02/24/2026)`
  > `Modeling 《 Improvement items 》`
  > `Fixed a problem in which multiple items could not be selected in the project palette.`
  > `When creating a new model from a PSD file, the "Cubism 5.2 blend mode or earlier" format can now be selected.`
- 一句话：**5.3.01 无 beta 阶段**（表里从 5.3.00 直接跳到 5.3.01），是一次小修：修项目面板多选失效；新建模型时可选择「Cubism 5.2 及更早的混合模式」格式。
- 与已有口径的差异：R31 只记了日期 `02/24/2026 → 5.3.01`，**未记内容**；本轮补齐，并确认它没有 beta1（R31 表也印证 02/24 前无 5.3.01 beta1 行）。
- 可复用性：**参考** —— 与小白制作无直接关系（纯编辑器面板 bug 修复）；仅提醒「5.3.01 起新建 PSD 模型可回退 5.2 混合模式」这一点在导入老素材时有用。
- 核实程度：页面已读

### 2. Cubism Editor **5.3.02** 更新了什么 · docs.live2d.com · 2026-04-02
- 地址：https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/
- 原文证据：
  > `5.3.02 (04/02/2026)`
  > `Fixed a problem that prevented pasting when editing meshes in multiple ArtMeshes.`
  > —— 其下 `5.3.02 beta1 (03/03/2026)` 记载实质内容：`A [Reset mesh] function has been added to the mesh edit mode to reset the mesh to its initial state.` / `Fixed a problem that caused an error when editing continued with overlapping vertices in mesh edit mode. Overlapping vertices are automatically merged.` / `A [Reset mesh]...` 等
- 一句话：正式版 5.3.02 只修「多 ArtMesh 同时改网格时无法粘贴」；实质新功能在 **beta1**：网格编辑模式新增 **[Reset mesh]**（把网格重置回初始态）、重叠顶点自动合并、glue ID 长名自动缩短、扩展 warp deformer 防parent变形、撤销时部件展开态不跳动等。
- 与已有口径的差异：R31 只记日期 `04/02/2026 → 5.3.02`；本轮补齐内容，且指出「实质功能看 beta1」。
- 可复用性：**落地** —— `[Reset mesh]` 和「重叠顶点自动合并」是**建模小白做网格时的高频救命项**（手工分网格搞坏了可直接重置，不用重导 PSD）。
- 核实程度：页面已读

### 3. Cubism Editor **5.3.03** 更新了什么 · docs.live2d.com · 2026-06-16
- 地址：https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/
- 原文证据：
  > `5.3.03 (06/16/2026)`
  > `The beta has been removed and released as an official release version.`
  > —— 其下 `5.3.03 beta1 (05/14/2026)` 记载实质内容：`Added to the parameter palette the ability to move a parameter selected with [Subject to move] to any location with [Move here].` / `Added to the parameter palette the ability to "Set all parameter values as default."` / `Added to the Mesh Edit mode menu the ability to [Paste in copied shape].` / `Added [Edit target] to the tool details of the parameter controller tool.` 等约 20 条
- 一句话：5.3.03 正式版**只有一句「移除 beta 标记、发布正式版」**，全部实质内容在 **beta1**：参数面板新增 **[Subject to move]/[Move here]**（拖拽移动参数到任意位置）、**[Set all parameter values as default]**、网格编辑 **[Paste in copied shape]**（粘贴已复制形状）、参数控制器全面增强（可单独删除、可拖拽设定目标、旋转 deformer 显示开关等）。
- 与已有口径的差异：R31 只记日期 `06/16/2026 → 5.3.03`；本轮补齐，并给出「正式版=提正」的机制说明。
- 可复用性：**落地** —— 「参数移动/排序」和「Set all parameter values as default」直接改善**参数表整理**（Live2D 新手最容易把参数顺序搞乱）；`[Paste in copied shape]` 对网格复用有用。
- 核实程度：页面已读

### 4. Cubism Editor **5.3.04** 更新了什么 · docs.live2d.com · 2026-09-03（最新正式版）
- 地址：https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/
- 原文证据：
  > `5.3.04 (09/03/2026)`
  > `Fixed an issue where items in the parts palette might be highlighted in a different color than usual when dragging.`
  > —— 其下 `5.3.04 beta1 (07/30/2026)` 记载实质内容：`Added a "Display in a new window" icon to the log palette.` / `Added influence display to the tooltips for editing physics groups.` / `Added "Brush shape" and "Angle" to the [Tool details] palette for [Edit Glue].` / `Added a [Clear GUID] option to the [Export Model Parameters] function.` / `Changed the name of the function [View motion changes as image] to [View motion changes in graph format].` 等约 18 条
- 一句话：正式版 5.3.04 只修一处（拖拽时部件面板高亮色异常）；实质在 **beta1**：日志面板可开新窗口、物理组 tooltip 显示**影响值**、Glue 编辑新增笔刷形状与角度、导出模型参数新增 **[Clear GUID]**、函数更名 等。
- 与已有口径的差异：R31 只记 `09/03/2026 → 5.3.04`；本轮补齐，并澄清 R31 表格里 `07/30/2026 → 5.3.04 beta1` 即该版实质内容。
- 可复用性：**参考** —— 物理组「影响值提示」对调物理参数有帮助；其余偏工程；`[Clear GUID]` 老手才用。
- 核实程度：页面已读

> **小结（口径纠正）**：R31/索引把「5.3.01–5.3.04 只是版本号，未读内容」列为欠账——**本轮已读全**。规律：**5.3.01 无 beta（纯修补）；5.3.02/03/04 均为「beta1 写全套 + 正式版只写一行」**，且 **5.3.03 正式版仅一句「去 beta」**。索引如需一句话概括：*5.3.01 修面板多选｜5.3.02 网格编辑加 Reset mesh｜5.3.03 参数面板可拖拽排序｜5.3.04 物理提示+GUID 清理*。

---

## 二、厂商官网 / 公告 / 授权定价

### 5. ⚠️口径纠正：Cubism **5.4 SDK alpha 已存在**（R31「5.4 无配套 SDK」不成立）· live2d.com · 公告 2026-07-14 / 复核 2026-10-11
- 地址：https://www.live2d.com/en/information/cubism-5_4-alpha/ （⚠️ 此 URL **已在基线** `_r32/_dedupe_urls.txt` line 1388，本条只记「本轮读到的正文 + 纠正」，不重复计数）
- 原文证据：
  > `We have released the alpha versions of Cubism Editor 5.4 and Cubism SDK 5.4!`
  > `Available until "October 18, 2026." After this date, the alpha version will no longer be available.`
  > `Note: The availability period has been extended with the release of alpha2. Please note that alpha1 will no longer be available after September 14, 2026.`
  > `The Cubism SDK includes sample models that allow you to verify the operation of the Parameter Controller.` / `[Hashtag] #Live2D #cubism54_alpha`
- 一句话：5.4 alpha **Editor 与 SDK 双发**；alpha2 可用至 **2026-10-18**，alpha1 已于 **2026-09-14** 下线；5.4 功能重心是 **Parameter Controller（参数控制器）**，官方在 SDK 里放了示例模型供验证；alpha 免费，但**产出数据仅限个人使用、不得在 VGen/nizima 售卖**。
- 与已有口径的差异：**纠正 R31 负结论②**（R31 写「5.4 仅 Editor alpha，未配套 5.4 SDK」——实为 Editor+SDK 同发 alpha）。
- 可复用性：**参考** —— alpha 是限时评估版、明说「数据不保证兼容、可能损坏」，小白**不要**用它做正式项目；等 5.4 正式版再上。
- 核实程度：页面已读

### 6. ⚠️ 上轮误判「退役」的源可回滚：`creatorsforum.live2d.com` 本轮 **HTTP 200**（R31 记 403）· Creators Forum · 2026-10-11
- 地址：https://creatorsforum.live2d.com/ （不在 `_r32/_dedupe_urls.txt`；Discourse 论坛，可读 `/latest.json`）
- 原文证据：
  > 页面标题：`Live2Dクリエイターズフォーラム - Live2D公式フォーラム`
  > 版块：`Cubism Editor / SDK 5.4 alpha — みなさんからのご意見・ご要望を通して、Cubism Editor 5.4の機能をより良いものへと改良していきます。`
  > 版块计数：`一般 … 75` / `Cubism Editor / SDK 5.4 alpha … 0` / `Cubism Editor … 1`
- 一句话：**R31 记为 403 的官方创作者论坛本轮可直接访问**（Discourse，`/latest.json` 亦可读）→ **退役名单可回滚**；论坛专设「**Cubism Editor / SDK 5.4 alpha**」意见收集版块，印证 5.4 双 alpha。
- 与已有口径的差异：**纠正 R31 的「403 不可达」判断**（本轮 200，可能是上轮临时故障/风控）。
- 可复用性：**参考** —— 非制作教程、是官方反馈渠道；对小白价值在于「5.4 有问题/想提需求可去官方论坛」，而非直接落地。
- 核实程度：页面已读 + API 已读

### 7. 论坛实报：**Cubism Editor 5.4.00 alpha2 启动崩溃**（官方回复「调查中」）· Creators Forum · 2026-09-25
- 地址：https://creatorsforum.live2d.com/t/3983 （`/t/3983.json`）
- 原文证据：
  > 标题：`【Cubism 5.4.00 alpha2】初回同意完了後、起動時に command_loginApplication で NullPointerException が発生する（EXE / D3D BAT双方で再現）`
  > 正文：`Cubism Editor: 5.4.00 alpha2　Build表示: 504000001 / 2026/09/07`，`同一PCに Cubism Editor 5.3.04 も別実体として存在し、5.3.04側は正常に起動・作業できています。`
  > 官方回复（2026-10-01）：`Live2Dスタッフでございます。…ただいま調査を行っております。`
- 一句话：**5.4.00 alpha2 的构建日期 = 2026/09/07（build 504000001）**（R31 只知到 5.4 alpha，未定到 alpha2）；该 alpha2 存在启动即 `NullPointerException` 的已知问题，官方截至 2026-10-01 仍在调查。同机 5.3.04 正常。
- 与已有口径的差异：R31 称 5.4「仅 alpha」——精确到 **alpha2 / build 2026-09-07**，且确认有未修复崩溃。
- 可复用性：**不采用** —— 明确告知小白别装 5.4 alpha2 做生产（会崩）；**落地** 的是「继续用 5.3.04」这一结论。
- 核实程度：页面已读（主帖 + 官方回帖）

### 8. 官网英文新闻仍停在 2026.07.17（近 3 个月无新增，锚点未变）· live2d.com · 2026-10-11
- 地址：https://www.live2d.com/en/information/
- 原文证据：列表按日期倒序 —— `2026.07.17 / 2026.07.14 / 2026.03.20 / 2026.02.13 / 2026.01.20 / 2025.11.14 …`（首条仍为 2026.07.17）
- 一句话：与 R31 一致，官网新闻**未新增**；5.3.01–5.3.04 与 5.4 alpha2 **均未发新闻稿**（改动只在 docs/论坛）。
- 与已有口径的差异：无（复现 R31）。
- 可复用性：**参考** —— 提醒「新闻发得少 ≠ 项目停摆」，版本要去看 docs Release History 表。
- 核实程度：页面已读

### 9. 产品页 5.3.00 vs docs 表 5.3.04 的官方口径冲突仍在（R31 未修）· live2d.com · 2026-10-11
- 地址：https://www.live2d.com/en/cubism/update/
- 原文证据：产品页「Latest Updates」逐条 —— `2026.01.20 : Ver.5.3.00` / `2025.02.04 : Ver.5.2.00` / `2024.07.30 : Ver.5.1.00` / `2023.09.21 : Ver.5.0.00`，且大标题仍为 `Cubism Editor 5.3.00 released!`；**无 5.3.01–5.3.04**。而 docs Release History 表（见第 1–4 条）为 **5.3.04**。
- 一句话：产品页只列大版本、落后 4 个 patch；**冲突持续**。索引取值应「**以 docs Release History 表为准 = 5.3.04**」。
- 与已有口径的差异：无（复现 R31 第 9 条，作为口径纪律的持续证据）。
- 可复用性：**落地** —— 提醒小白「装 5.3.04，别看产品页写着 5.3.00 就以为没更新」。
- 核实程度：页面已读

### 10. Live2D 官方 GitHub 组织：最近推送仍停在 2026-09-29，无新仓库 / 新发布 · github.com/Live2D · 2026-10-11
- 地址：https://api.github.com/orgs/Live2D/repos?sort=pushed
- 原文证据（最近 4 个）：`CubismUnityComponents | pushed 2026-09-29T05:22:19Z | ★264`、`CubismUnrealEngineComponents | pushed 2026-09-29T03:34:21Z | ★32`、`CubismUnityMotionSyncComponents | pushed 2026-08-25 | ★3`、`CubismNativeMotionSyncComponents | pushed 2026-08-25 | ★5`
- 一句话：组织内活跃仓库最近一次推送即 **2026-09-29（Unity / Unreal，对应 R31 已记的 Unreal R1 beta2）**；无 10 月新动作、无新仓库。
- 与已有口径的差异：无（与 R31 的 SDK 日期线一致，作为「10 月无更新」的锚点）。
- 可复用性：**参考** —— 工程向；小白无需跟。
- 核实程度：API 已读

### 11. ⚠️ 跨区块口径复现：英文 info 页「学生优惠」区块仍写 **76% OFF**（≠结算页 80%）· live2d.com · 2026-10-11
- 地址：https://www.live2d.com/en/information/cubism-5_4-alpha/ （页尾 Student Discount 区块）
- 原文证据：> `The Live2D Student Discount Program allows students and faculty … to receive a 76% OFF coupon for a 3-year Liv[e2D Cubism Editor PRO subscription]`
- 一句话：R31 定位的「**同一站内 76% vs 80% 文案并存**」在本轮又找到一个落点 —— 英文站 **info 页**（非首页）同样写 **76% OFF**；而学生专页 `student.live2d.com/en/student-discount/` 与 Store/EN 结算页均为 **80% OFF（$46 USD/¥7,344，截止 2027-03-31）**。
- 与已有口径的差异：R31 把 76% 归因到「英文首页的另一区块」；本轮证实 **不止首页，info 页也有 76% 文案**——即「76%」是英文站**多处**遗留文案。**取值仍以结算页 80% 为准**。
- 可复用性：**落地** —— 学生党认定「**80% OFF / ¥7,344 三年**」这一数，别被 76% 文案带偏。
- 核实程度：页面已读

---

## 三、SDK 各线版本（Unity / Unreal / Web / Native / Java / MotionSync / AE）

### 12. SDK 官方公告线**逐条未变**（最新仍 Unreal R1 beta2 @ 2026-09-29）· docs.live2d.com · 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-sdk-manual/top/
- 原文证据（公告倒序，照抄）：
  > `Notification of Cubism 5 SDK R1 beta2 release (09/29/2026)` → `Cubism 5 SDK for Unreal Engine R1 beta2`
  > `Notification of Cubism 5 SDK MotionSync Plugin R2_1 release (08/25/2026)` → `for Native R2_1` / `for Unity R2_1`
  > `Notification of Cubism 5 SDK R5 release (06/04/2026)` → `Cubism 5 SDK for Java R5`
  > `Notification of Cubism 5 SDK R4_2 release (05/14/2026)` → `Cubism 5 SDK for Unity R4_2`
  > `Notification of Cubism 5 SDK R5 release (04/02/2026)` → `for Native R5` / `for Web R5` / `for Unity R5`
  > 页顶横幅：`5.4 alpha Now Available.`
- 一句话：SDK 各线版本与 R31 完全一致（**分线各自版本**：Unity R5 + R4_2 并存 / Native·Web·Java R5 / Unreal R1 beta2 / MotionSync R2_1）；页顶已挂「5.4 alpha Now Available」，与第 5 条呼应（**5.4 SDK alpha 确实已出**）。
- 与已有口径的差异：无（复现），但**页顶横幅「5.4 alpha」是 SDK 线已进 5.4 的旁证**，可用于佐证第 5 条纠正。
- 可复用性：**参考** —— 团队内 Live2D+Unity 集成方按此锚定版本。
- 核实程度：页面已读

### 13. UniVRM 升到 **v0.131.3**（VRM 3D 化身生态，与 Live2D 对照）· github.com/vrm-c/UniVRM · 2026-10-02
- 地址：https://github.com/vrm-c/UniVRM/releases （`/releases` API 不在 `_r32/_dedupe_urls.txt`）
- 原文证据（releases 倒序）：`v0.131.3 | 2026-10-02T12:08:42Z`、`v0.131.2 | 2026-07-24`、`v0.131.1 | 2026-06-19`、`v0.131.0 | 2025-12-12`
- 一句话：**UniVRM 最新 v0.131.3（2026-10-02）**，是 10 月内少数仍在更新的「虚拟形象格式」工程（对照：Live2D SDK 线 9-29 后无新）。
- 与已有口径的差异：无（基线未含 UniVRM 版本，属增量）。
- 可复用性：**不采用** —— VRM 是 3D 路线，与「Ren'Py + Live2D」2D 工作流不同；仅作生态对照。
- 核实程度：API 已读

---

## 四、海外社区 / 榜单（HN / dev.to / 新闻聚合）

### 14. ⚠️口径纠正：npm 包 **`easy-live2d` 确实存在**，已到 **v1.0.0（2026-09-24）**（R31「包名不存在、勿再追」有误）· npm · 2026-09-24
- 地址：https://www.npmjs.com/package/easy-live2d （npm registry：`https://registry.npmjs.org/easy-live2d`）—— 该 npm URL **不在** `_r32/_dedupe_urls.txt`（基线只收录过其 **GitHub 仓库** `github.com/Panzer-Jack/easy-live2d`，见 index `[1196]`）
- 原文证据（npm registry JSON，照抄）：
  > `"name": "easy-live2d"`, `dist-tags: {latest: "1.0.0", uat: "1.0.0-uat.0"}`
  > `created: 2025-05-04  modified: 2026-09-24`
  > 版本线：`0.4.0(2026-04-03) → 0.4.1 → 0.4.2 → 0.4.3 → 0.4.4(2026-04-15) → 1.0.0-uat.0(2026-09-17) → 1.0.0(2026-09-24)`
  > `1.0.0 description: 基于 Pixi.js 封装的 轻量级 Live2D Web SDK`；依赖 `@pixi/sound ^6.0.1`
  > GitHub（对照）：`Panzer-Jack/easy-live2d` · MIT · ★213 · pushed 2026-09-24
- 一句话：`easy-live2d`（Pixi.js 封装、支持 Cubism 3/4/5、一行 `playVoice()` 口型同步、鼠标跟随/hit 交互/拖拽、含中英文档与 StackBlitz playground）**已发 npm 1.0.0**。R31 判定「各 registry 不存在（勿再追）」**只对 PyPI/crates 成立；npm 上是真实且活跃的包**（R31 可能漏查 npm）。
- 与已有口径的差异：**纠正 R31 负结论⑤**（`easy-live2d` 非「不存在」；其 GitHub 早在 index `[1196]`，本轮补上 **npm 注册表 + 1.0.0 版本**）。
- 可复用性：**落地（有条件）** —— 若做 **网页/桌面（Tauri）** 的 Live2D 助手，这是现成轮子；但基准是 **Ren'Py 本地项目**，Ren'Py 不能直接吃 npm → 故对「Ren'Py 小白」是**参考**，对「Web/桌面前端」才是**落地**。
- 核实程度：API 已读（npm registry JSON + GitHub API）

### 15. dev.to：live2d 标签仅两篇，最新仍 2026-06-08（无新料）· dev.to · 2026-10-11
- 地址：https://dev.to/api/articles?tag=live2d
- 原文证据：全部文章 —— `2026-06-08 | Open-LLM-VTuber Review: Offline AI Companion with Live2D`、`2026-04-04 | easy-live2d v0.4.0: A Milestone Release for Live2D on the Web`
- 一句话：与 R31 一致，dev.to 无新帖；但 R31 **只提到 06-08 那篇**，漏了 04-04 的 `easy-live2d v0.4.0` 发布说明（正是第 14 条的线索来源）。
- 与已有口径的差异：补 R31 遗漏的第二篇（它早于 R31 所称「最新」日期，不矛盾，但内容相关）。
- 可复用性：**参考** —— 开发者社区对 Live2D Web 集成的存量讨论入口。
- 核实程度：API 已读

### 16. HN Algolia：`live2d` 按日期检索 2167 命中，**近一年无相关 story**（负结论）· HN · 2026-10-11
- 地址：https://hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story
- 原文证据：`nbHits: 2167`，但日期倒序首屏命中的是 `Show HN: Claude Remote`、`livediff`、`livedin.co.uk` 等**同名误召**（"lived"/"live diff"），**无一条真·Live2D story**。
- 一句话：HN 对本主题**仍无产出**（与 R31 第 23 条一致）；`search_by_date` 的 fuzzy 匹配把 "lived" 也算进去了，需人工过滤。
- 与已有口径的差异：无（复现）。
- 可复用性：**不采用** —— 无料。
- 核实程度：API 已读

### 17. 「The AI Changelog」仍未取到（域名探测 HTTP 000）· 榜单/聚合 · 2026-10-11
- 地址（探测）：https://theaic.io/ → **HTTP 000**（不可达/超时）
- 原文证据：`HTTP:000 SIZE:0`（curl 无响应）
- 一句话：team-lead 点名的「The AI Changelog」本轮未能定位到可用域名（`theaic.io` 000）；**建议下轮换域名或直接退役**。
- 与已有口径的差异：无（本轮新增探测）。
- 可复用性：**不采用** —— 源不可达。
- 核实程度：仅探测（未读页面）

---

## 五、替代栈官方（Inochi2D / Spine / VTube Studio / Warudo / VRM）

### 18. Inochi2D：官网可达但**版本停滞近 2 年**（最新稳定版 v0.8.7 = 2024-10）· inochi2d.com / GitHub · 2026-10-11
- 地址：https://inochi2d.com/ ＋ https://inochi2d.com/download ＋ GitHub releases API（`github.com/Inochi2D/*` 仓库 **已在基线** line 175/176；本条列**官网** URL，未在 dedupe）
- 原文证据：
  > 官网：`Inochi2D is a framework for realtime 2D puppet animation … Royalty-free`（Games Development 一栏 `…with physics and advanced compositing, royalty-free`）
  > 下载页：`Inochi Creator`（开源绑定工具，免费评估版「a 10 second reminder screen will show on every startup」）、`Inochi Session`（`completely free`，可用 `VTubeStudio, MeowFace, VMC and OpenSeeFace` 做面捕）
  > Blog 页：`There are no posts currently. Check back soon!`；wiki `/wiki` → **404**
  > GitHub：`inochi2d` ★1811 / pushed 2026-10-03 / 最新 release = **nightly(2025-09-18)**、稳定 **v0.8.7(2024-10-02)**；`inochi-creator` ★1242 / 最新 **v0.8.6(2024-09-18)**；`inochi-session` ★407 / 最新 **v0.8.7(2024-09-19)**
- 一句话：Inochi2D =「**开源、免版税**」的 Live2D 替代（Creator 绑定 + Session 直播），但**已近 2 年无稳定版发布**（稳定停在 2024-10 的 0.8.7，仅有 2025-09-18 的 nightly）；博客空、wiki 404。**生态基本停滞**。
- 与已有口径的差异：基线只有仓库 URL、无「停滞」判定；本轮补上版本与停滞证据。
- 可复用性：**不采用（现状）** —— 对游戏制作小白，工具停更意味着无社区/无教程风险；**除非**只做免版税实验，否则不建议押注。
- 核实程度：页面已读 + API 已读

### 19. Spine 最新正式版 **4.3.26（2026-09-07）**，4.3.27「Unreleased」· esotericsoftware.com · 2026-10-11
- 地址：https://esotericsoftware.com/spine-changelog
- 原文证据（changelog 顶部，照抄）：
  > `4.3.27 Unreleased  Improved file IO retries, locking, and clean up.  Launcher 4.3.08: improved running offline with Windows.`
  > `4.3.26  7 Sep 2026  Fixed favor tool crash when the frame changes. Fixed loading some projects with deform timelines. Import PSD: improved source mesh [name:pattern] error messages.`
  > `4.3.25  6 Sep 2026  Fixed failure to start for some Windows.`
  > `4.3.24  6 Sep 2026  Show weights view when a non-weighted mesh is selected with the weights tool. …`
- 一句话：Spine（Live2D 的主要商业竞品，做骨骼动画/Bone 驱动）**最新正式版 4.3.26（2026-09-07）**，其上 4.3.27 仍是「Unreleased」；近期为密集小修（9 月 6 日连发 4.3.24/4.3.25/4.3.26）。
- 与已有口径的差异：无（基线只有 `github.com/EsotericSoftware/spine-runtimes`，无 changelog 页/版本号）。
- 可复用性：**参考** —— Spine 是**付费**、且工作流偏骨骼（≠Live2D 的网格变形）；对「Ren'Py 看板娘/立绘」场景双方各有取舍，Spine 更适合**游戏角色骨骼动画**。
- 核实程度：页面已读

### 20. VTube Studio 官方版本 **1.35.10**（2026-07-08）——**以官方 Trello 为准**，第三方 APK 站版本号不可信 · denchisoft.com/Trello · 2026-10-11
- 地址：https://denchisoft.com/ ＋ 官方开发看板 https://trello.com/b/fFUocd23 （Trello JSON：`/b/fFUocd23.json`）
- 原文证据：
  > 官网：`VTube Studio is available for iOS (iPhone/iPad), Android and Steam (PC/Mac). … face tracking via webcam (using OpenSeeF[ace])`、`VTube Studio now also supports hand tracking!`
  > 官方 Trello「Released / Changelog」列表（倒序）：`VTS Version 1.35.10 | 2026-07-08`、`1.35.7 | 2026-05-20`、`1.35.2 | 2026-04-11`、`1.35.0 | 2026-03-31`、`1.34.0 | 2026-03-28`、`1.33.2 | 2026-03-26`
  > 近期 Done（2026-09~10）：`Syphon (like Spout2) support for macOS`(10-06)、`API: NDIConfigRequest now requires explicit permission`(09-04)、`Event API: Added ArtMeshTrackingEvent / ExpressionToggledEvent`(08-24)
- 一句话：VTS 官方最近的版本记录为 **1.35.10（2026-07-08）**；开发看板持续在动（9–10 月有 macOS Syphon、API 权限、Event API 扩展）。⚠️ **中文第三方下载站所标 `v1.28.15` / `1.32.71` 均与官方不符**（口径纪律：以官方 Trello 为准）。
- 与已有口径的差异：基线未含 VTS 版本；且本轮**实测第三方站点版本号不可靠**（同款应用三个站给出 1.28.15 与 1.32.71 两种）。
- 可复用性：**参考** —— VTS 是 Live2D 模型的**驱动/直播前端**（不是制作工具）；做「桌面看板娘」时与 Ren'Py 是并行的另一条路，非替代。
- 核实程度：页面已读 + Trello JSON 已读

### 21. Warudo：3D VTubing 软件，官网为 JS 单页、无可直读更新页 · warudo.app · 2026-10-11
- 地址：https://warudo.app/（`/changelog` 亦返回同一 SPA 外壳）
- 原文证据（meta 描述，照抄）：
  > EN：`Warudo is the flexible & personalized 3D VTubing software you have always wanted. Built-in face & hand tracking, custom 3D assets, Twitch/YouTube integration, blueprint system, C# plugins`
  > ZH：`Warudo 是一款极高可玩性与自由度的 3D 虚拟直播软件。内置面部和手部捕捉，自由导入外部 3D 素材，哔哩哔哩 / Twitch / YouTube 观众互动，可编程蓝图系统，C# 插件`
- 一句话：Warudo 定位 **3D** 虚拟直播（内置面/手捕捉、蓝图、C# 插件），与 Live2D 的 2D 路线**不同赛道**；官网是前端渲染 SPA，**无静态更新日志可抓**（HTML 仅 1.9KB 外壳）。
- 与已有口径的差异：无（基线未含 Warudo）。
- 可复用性：**不采用** —— 3D 路线、且是实时直播工具，与「Ren'Py 2D 游戏」目标不符；仅作生态全景之一。
- 核实程度：页面已读（仅 meta，正文为 JS 渲染未取到）

---

## 已收录（剔除）

以下 URL 命中 `_r32/_dedupe_urls.txt`，本轮不再重复收录：

- https://github.com/Panzer-Jack/easy-live2d （基线 line 297；= index `[1196]`。**注意**：其 npm 包 `easy-live2d` 未在基线，故第 14 条以 npm URL 收录）
- https://github.com/Inochi2D/inochi2d 、https://github.com/Inochi2D/inochi-creator （基线 line 175/176；第 18 条改以官网 `inochi2d.com` 收录）
- https://github.com/EsotericSoftware/spine-runtimes （基线 line 119；第 19 条改以 changelog 页收录）
- https://www.live2d.com/en/information/cubism-5_4-alpha/ （基线 line 1388；第 5 条只记纠正、不重复计数）
- https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title （基线；大版本 Release History 表，R31 已记。本轮**新页**为 `updates-history5-3`，见第 1–4 条）
- https://www.live2d.com/en/cubism/update/ （R31 第 9 条已记；第 9 条为复现）
- https://www.live2d.com/en/sdk/download/unity/ · /native/ · /web/ · /java/ · /motionsync/ （R31 已记）
- https://store.live2d.com/en/ · https://student.live2d.com/en/student-discount/ （R31 已记；第 11 条为复现）
- https://docs.live2d.com/en/cubism-sdk-manual/top/ （R31 已记；第 12 条为复现）
- https://dev.to/andrew-ooo/open-llm-vtuber-review-offline-ai-companion-with-live2d-327m （R31 第 24 条提及）

---

## 负结论

1. **Cubism 5.3 主线收尾，无 5.3.05**：5.3.04（2026-09-03）仍是最新正式版，**5.3.05 不存在**；下一个节点是 **5.4**（现处 **alpha2**，见第 5/7 条）。
2. **R31 两处负结论被推翻**：①「5.4 无配套 SDK」→ **实为 Editor+SDK 双 alpha**；②「`easy-live2d` 各 registry 不存在、勿再追」→ **npm 上真实存在且已 1.0.0**。索引需同步修正。
3. **R31 一处「退役」可回滚**：`creatorsforum.live2d.com` 本轮 **HTTP 200**（R31 记 403）→ 官方论坛可用，建议从退役名单移除。
4. **官网新闻停更**：`live2d.com/en/information/` 最新仍 **2026.07.17**，近 3 个月无新增（5.3.01–5.3.04、5.4 alpha2 皆未发新闻）。
5. **Live2D GitHub 无 10 月动作**：组织内最近推送 = **2026-09-29**（Unity/Unreal），无新仓库。
6. **HN 无料**：`live2d` `search_by_date` 2167 命中近一年全为误召，无真 story。
7. **dev.to 无新帖**：live2d 标签最新仍 2026-06-08（存量仅两篇）。
8. **替代栈现状**：Inochi2D **停滞**（稳定版停在 2024-10）；Spine 活跃（4.3.26 / 2026-09-07）；VTube Studio 活跃（1.35.10 / 2026-07-08）；Warudo 3D 路线、官网无静态日志。
9. **本研究未投入的退役源**（沿用，见报告）：`Reddit`（TLS 重置）、`itch.io`/`Steam`/`note.com`/`Medium`/`YouTube`（HTTP 000）、`Stack Overflow`（live2d 标签不存在）、`Godot 官方论坛`（近真空）；新增探测 **theaic.io（The AI Changelog）→ HTTP 000**。

---

## 本路去重报告 + 各源命中率

**去重执行**：每条先 `grep -iF "<关键词>" _r32/_dedupe_urls.txt index.html csdn-social-summary.md csdn-social-summary-v30.md`。
- **命中即弃**：`github.com/Panzer-Jack/easy-live2d`（已有 index[1196]）、`github.com/Inochi2D/inochi2d`·`inochi-creator`、`github.com/EsotericSoftware/spine-runtimes`、`cubism-5_4-alpha`（line 1388）→ 这些 URL 不重复收录，改用**未在基线的新入口**（npm / inochi2d.com / spine-changelog）或**只记纠正**。
- **关键词查重命中**：`easy-live2d`(1)、`Panzer-Jack`(1)、`inochi`(2)、`esotericsoftware`(1)、`VTube`(3，均为无关的 Open-LLM-VTuber 等)、`Cocos`(2，无关)。新页面 `updates-history5-3`、`creatorsforum`、`trello.com/b/fFUocd23`、`vrm-c/UniVRM`、`inochi2d.com`、`spine-changelog` **均在基线中为 0 命中** → 收录。

**各源命中率（本轮 official 路）**：

| 源 | 入口 | 结果 |
|---|---|---|
| docs Release History **patch 明细页** `updates-history5-3` | curl 原始 HTML | ✅ **有（本轮核心产出，5.3.01–5.3.04 全读）** |
| live2d.com 5.4 alpha 公告页 | curl | ✅ 有（**5.4 SDK alpha 纠正**；URL 已在基线） |
| live2d.com 官网新闻 `information` | curl | ✅ 有（仍停 2026.07.17） |
| live2d.com 产品页 `cubism/update` | curl | ✅ 有（5.3.00 vs docs 5.3.04 冲突复现） |
| docs SDK 手册公告线 `sdk-manual/top` | curl | ✅ 有（逐条未变） |
| Creators Forum | curl + `/latest.json` | ✅ **200（R31 记 403，已回滚）** |
| Creators Forum 单帖 | `/t/3983.json` 等 | ✅ 有（5.4.00 alpha2 崩溃） |
| GitHub org `Live2D` repos/releases | `gh api` | ✅ 有（无 10 月新动作） |
| GitHub `vrm-c/UniVRM` releases | `gh api` | ✅ 有（v0.131.3） |
| GitHub `Inochi2D/*` releases | `gh api` | ✅ 有（停滞证据） |
| npm registry | curl JSON | ✅ **有（`easy-live2d` 1.0.0，纠正 R31）** |
| dev.to API | curl JSON | ✅ 有（2 篇，无新） |
| HN Algolia API | curl JSON | ❌ 空（全误召） |
| esotericsoftware changelog | curl | ✅ 有（Spine 4.3.26） |
| denchisoft.com + Trello | curl + JSON | ✅ 有（VTS 1.35.10） |
| warudo.app | curl | ⚠️ 仅 meta（SPA，正文 JS 渲染） |
| theaic.io（The AI Changelog） | curl | ❌ HTTP 000 |
| Reddit / itch.io / Steam / note.com / Medium / YouTube | — | ❌ 退役，未投入 |

**本轮条数**：21 条（含 4 条 patch changelog + 2 条 R31 口径纠正 + 1 条退役回滚）。
**最硬口径纠正**：① **5.4 SDK alpha 存在**（推翻 R31「无配套 SDK」）；② **`easy-live2d` npm 真实存在且 1.0.0**（推翻 R31「包不存在、勿再追」）；③ **Creators Forum 403→200**（退役可回滚）；④ **Cubism 5.4.00 alpha2 build=2026/09/07 且启动崩溃调查中**。
**本可通但上轮误判退役的源**：**`creatorsforum.live2d.com`（明确可回滚）**。
