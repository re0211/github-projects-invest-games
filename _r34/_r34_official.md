# R34 · Live2D 制作专题 —— official 路（官方 / 海外社区 / 竞品）

- 轮次：第 34 轮（连续第 10 轮做 Live2D）
- 调研日期：2026-10-11（本文件所有 HTTP/API 取值均为该日）
- 对照基线：R33（同日）——Editor 5.3.04、5.4 alpha2 手册（PSD 导入增强 + 数据兼容单向门）、`Cubism 5 SDK ≤R6 / Cubism 5.4 SDK ≥R7 alpha1`、两条破坏性变更、creatorsforum 200、Unreal R1 beta2(09/29)、Spine 4.3.26、Inochi2D v0.8.6、学生页 $46 vs Store $46.40
- 查重基线：`_r34/_dedupe_urls.txt`（1453 行）+ `_r34/_dedupe_gh.txt`
- 对照经验帖：`csdn-social-summary.md`（第三十三辑全文）
- 口径纪律：结算页 > 产品页；docs Release History 表 > 产品页；**同一站内跨区块交叉验证**；负结论写「本轮未命中」
- 本路定位：**官方与海外社区路**。本轮重点 = 逐条核官方版本口径有无变化 + 论坛一手正文 + 海外社区
- 本路条数：**25 条**（含 5 条全新官方论坛一手：第 7/17/18/19/20 条；第 16 条为新入口、第 24 条为新来源 Steam）

> **一眼结论（R34）**：官方版本口径与 R33 **逐条一致、零变动**（Editor 5.3.04 / 5.4 alpha2 / SDK R6→R7 alpha1 / 两条破坏性变更 / 各分线版本）；**真正的新东西全在官方论坛一手正文里** ——
> ① **5.3「保存失败」根因被官方定性**：不是文件大，是**参数数「相乘」爆炸**，对策 = **blend shape 替代 normal key**（第 17 条，本轮最有用）；
> ② **alpha2 启动崩溃帖有官方进展**：10-05 官方仍在查，并**点名怀疑「用 AI agent 启动」**（第 7 条，对 agent 自动化 Cubism 是警告）；
> ③ **Unity 6.6 + URP3D「运行时黑屏」被官方复现认领**（第 18 条）。
> **口径被推翻/修正的条目：无**（官方三个版本口径均未变）；**新增裂缝只有「计数分歧」一处**（产品页 5.3.00 vs docs 5.3.04 冲突的轮次计数，见第 3 条）。

---

## 一、Editor 正式线（复核：逐条未变）

### 1. Cubism Editor 主线仍收在 **5.3.04（2026-09-03）**，无 5.3.05 · docs.live2d.com · 复核 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/ （`_r34/_dedupe_urls.txt` **0 命中**；R33 第 1 条的核心产出页，本轮只记「有无变化」）
- 原文证据（页面倒序，照抄版本行）：
  > `5.3.04 (09/03/2026)` → 仅一行：`Fixed an issue where items in the parts palette might be highlighted in a different color than usual when dragging.`
  > `5.3.04 beta1 (07/30/2026)` / `5.3.03 (06/16/2026)` / `5.3.03 beta1 (05/14/2026)` / `5.3.02 (04/02/2026)` / `5.3.02 beta1 (03/03/2026)` / `5.3.01 (02/24/2026)` / `5.3.00 (01/20/2026)`
  > 页顶横幅：`5.4 alpha Now Available.`
- 一句话：**与 R33 完全一致** —— 5.3.04 仍是最新正式版，**5.3.05 未命中**；patch 明细页自 09/03 后无新增条目。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**✅ 落地** —— 小白继续装 **5.3.04**。
- 核实程度：页面已读（curl 原始 HTML → 去标签）

### 2. Release History 大版本表：最新仍 `09/03/2026 · Cubism 5.3.04`，表内**无 5.4** · docs.live2d.com · 复核 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title/ （`_r34/_dedupe_urls.txt` line 14，**已收录**，本条只记变化）
- 原文证据（表格倒序首 8 行，照抄）：
  > `09/03/2026 Cubism 5.3.04` / `07/30/2026 Cubism 5.3.04 beta1` / `06/16/2026 Cubism 5.3.03` / `05/14/2026 Cubism 5.3.03 beta1` / `04/02/2026 Cubism 5.3.02` / `03/03/2026 Cubism 5.3.02 beta1` / `02/24/2026 Cubism 5.3.01` / `01/20/2026 Cubism 5.3.00`
  > 表首横幅：`5.4 alpha Now Available`
- 一句话：**未变** —— 大表仍以 5.3.04 收尾，5.4 只在页顶横幅出现、**未进版本表**（= 5.4 仍在 alpha，未「发布」）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— 索引写「最新版本」须写成「Editor 5.3.04（正式）/ 5.4 alpha（评估版，勿用于生产）」，**不能写成一个数**。
- 核实程度：页面已读

### 3. 产品页 `cubism/update` 仍写 **Ver.5.3.00**，与 docs 表 5.3.04 的官方口径冲突**持续** · live2d.com · 复核 2026-10-11
- 地址：https://www.live2d.com/en/cubism/update/ （`_r34/_dedupe_urls.txt` 中 **0 命中**）
- 原文证据：
  > 产品页「Latest Updates」逐条：`2026.01.20 : Ver.5.3.00` / `2025.02.04 : Ver.5.2.00` / `2024.07.30 : Ver.5.1.00` / `2023.09.21 : Ver.5.0.00`；大标题仍为 `Cubism Editor 5.3.00 released`
  > docs Release History 表（第 2 条）：`09/03/2026 Cubism 5.3.04`
- 一句话：**冲突未修**（产品页落后 4 个 patch）。**取值以 docs 表为准 = 5.3.04**。
- ⚠️ **计数分歧（照录，不擅自归一）**：R33 自述为「第 3 轮连续复现」；但 `csdn-social-summary-v31.md`（第 31 辑）第 146 行原文写「这条冲突**挂了两辑**」→ 按此推：第 31 辑=2 轮 → 第 32 辑=3 轮 → **本轮（第 34 辑）应为第 4 轮**。**本轮记为「连续第 4 轮复现」，并标注与 R33「第 3 轮」自述存在 ±1 分歧。**
- 与上一轮差异：**无变化内容**（又一条复现）；计数口径见上。
- 可复用性：**✅ 落地** —— 官方站内跨区块口径冲突的活样本：「别看产品页写 5.3.00 就以为没更新」。
- 核实程度：页面已读

### 4. 官网新闻首条仍 **2026.07.17**（一条已过期的 PRO 20% 折扣 Campaign），至少连续 4 轮无新增 · live2d.com · 复核 2026-10-11
- 地址：https://www.live2d.com/en/information/ （`_r34/_dedupe_urls.txt` 中命中；R33 第 18 条已记，只记变化）
- 原文证据（日期倒序，含标题）：
  > `2026.07.17 Campaign Get 20% OFF Live2D Cubism PRO! Ends Monday, July 27, 2026` ← **首条仍为此条，且其活动日 07-27 早已过去**
  > `2026.07.14 Product Info Cubism 5.4 Alpha Release Announcement` / `2026.03.20 Campaign …2026 Spring Inspiration Sale! Ends Monday, Mar 30, 2026` / `2026.02.13` / `2026.01.20` / `2025.11.14`
- 一句话：**未变** —— 5.3.01–5.3.04、5.4 alpha1/alpha2 **均未上官网新闻**；官方新动向只在 docs / 论坛。首条为一个**已过期**的促销 Campaign，进一步说明新闻页近乎冻结。
- 与上一轮差异：**无变化**（复现）；`csdn-social-summary-v31.md`/`v32.md` 均记 07.17 → **至少连续 4 轮未更新**。
- 可复用性：**⚠️ 参考** —— 「新闻少 ≠ 停摆」，版本看 docs Release History 表。
- 核实程度：页面已读

> ⚠️ **本轮专项核查：20 周年** —— 对 `_p_news.html` 搜 `anniversary|周年|20th|20 year` **0 命中**（见 §去重报告·负结论）。官方新闻页本轮**未命中任何周年/纪念活动**。

---

## 二、5.4 alpha 线（复核 + ⭐本轮新变化：崩溃帖有官方进展）

### 5. Cubism **Editor 5.4 alpha2 用户手册**修订记录**未新增**（仍停在 09/07/2026）· cubism.live2d.com · 复核 2026-10-11
- 地址：https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html （`_r34/_dedupe_urls.txt` line 9，**已收录**；R33 第 4–7 条已读全文，本轮只记「修订记录有无新变化」）
- 原文证据（Revision History，照抄）：
  > 标题：`Live2D Cubism Editor 5.4 alpha2 User Manual`
  > `alpha2 09/07/2026 Added the following descriptions. ● "Notes on Data Compatibility" ● "Warning When Overwriting a Model of a Different Version" ● Update history ○ "Alpha version period" ○ "PSD Import Enhancements"`
  > `alpha1 07/14/2026 First edition`
  > 章节清单（本轮复核仍为这些）：`PSD import enhancements / Parameter controller / Model state set / Enhanced auto layout of Texture Atlas / Expanded editing functions for external application integration API / Precautions for Use / Sample data`
- 一句话：**未变** —— 手册修订记录最新条目仍是 **alpha2 / 09/07/2026**，无 `alpha3`、无新修订行；R33 读到的「数据兼容单向门」「PSD 多层合并导入」两节原文**本轮原样复现**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— alpha2 手册是「5.4 现状」的官方锚点。
- 核实程度：页面已读

### 6. alpha 可用期仍 **截至 2026-10-18**（距今 7 天），alpha1 已于 2026-09-14 下线；76% 遗留文案仍在 · live2d.com · 复核 2026-10-11
- 地址：https://www.live2d.com/en/information/cubism-5_4-alpha/ （`_r34/_dedupe_urls.txt` 中命中，已收录，只记变化）
- 原文证据：
  > `Available until "October 18, 2026"`（页面两处均为此日期）
  > `… to receive a 76% OFF coupon for a 3-year Live2D Cubism Editor PRO subscription` ← **76% 遗留文案仍在**
  > `September 14, 2026`（alpha1 下线说明仍在）
- 一句话：**未变** —— 可用期与 R33 一致（10/18）；**距本轮仅剩 7 天**，之后 5.4 alpha 全面下线、等 beta。
- 与上一轮差异：**无变化**（复现，只补「剩余 7 天」时间敏感提醒）。
- 可复用性：**✅ 落地** —— 想试 5.4 新功能（如 PSD 多层合并）的，**10/18 前**抓紧；过期后这一入口消失。
- 核实程度：页面已读

### 7. ⭐新增·官方进展：alpha2「启动时 `command_loginApplication` NullPointerException」报障帖**仍未解决**，官方 10-05 追问「是不是用 AI agent 启动的？」· creatorsforum · 2026-09-25 → 2026-10-05
- 地址：https://creatorsforum.live2d.com/t/3983 （`/t/3983.json`；**单帖 ID 在 `_r34/_dedupe_urls.txt` 中 0 命中**；R33 仅提及「R32 只引了 /t/3983 的 alpha2 崩溃帖」，未记进展 —— 本条补进展）
- 原文证据（照抄关键句）：
  > 标题：`【Cubism 5.4.00 alpha2】初回同意完了後、起動時に command_loginApplication で NullPointerException が発生する（EXE / D3D BAT双方で再現）`
  > 用户 `コノエ_姫野`（2026-09-25）：`Cubism Editor: 5.4.00 alpha2 Build表示: 504000001 / 2026/09/07`；`同一PCに Cubism Editor 5.3.04 も別実体として存在し、5.3.04側は正常に起動・作業できています`；`「誠に申し訳ありませんが起動時にエラーが発生しました…」`
  > 官方 `enoko_staff`（2026-10-01）：`ただいま調査を行っております。`
  > 官方 `enoko_staff`（2026-10-05）：`本件につきまして、ただいま引き続き調査を行っております。… Cubism Editorの起動方法を教えてくださいませ。通常通りCubism Editor.exeをクリックして起動しているのか、それともAIエージェント等を使用して起動しているのか…`
- 一句话：**官方一手正文的新进展** —— ① 崩溃**仍未确认根因、未修复**（截至 10-05）；② 官方把怀疑方向指向**启动方式**（正常人点 exe？还是**用 AI agent 等启动**？）—— 这与本专题「用 agent 驱动 Cubism」的路线**直接相关**：官方已明确把「AI agent 启动」列为可疑变量。
- 与上一轮差异：**新增**（R33 只登记了该帖存在，未记 10-01/10-05 两条官方回复）。
- 可复用性：**✅ 落地**（对「想用 agent 自动化 Cubism」的人是个官方警告信号）：**别指望 alpha2 在自动化启动下稳定**；此 bug 与 5.4 alpha 可用期叠加 → 想试 5.4 也别挂在 agent 流程里。
- 核实程度：页面已读（主帖 + 官方 2 回帖）

---

## 三、SDK 线（复核：**分线各自版本**，逐条未变）

> 口径纪律：**SDK 是分线各自版本，别写成一个数。** 下列版本均由「官方公告线 + 各平台 GitHub releases」双入口交叉验证（docs 下载页 `/sdk/download/<platform>/` 为 JS 渲染，正文不吐版本号，故不采信其正文）。

### 8. 官方术语复核：**Cubism 5 SDK = ≤ R6；Cubism 5.4 SDK = ≥ R7 alpha1**（未变）· cubism.live2d.com · 复核 2026-10-11
- 地址：https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html （`_r34/_dedupe_urls.txt` **0 命中**；R33 第 13 条首次落到此最终 URL，本条只记变化）
- 原文证据（照抄）：
  > `Cubism 5 SDK refers to SDK versions up to and including Cubism 5 SDK R6.`
  > `Cubism 5.4 SDK refers to SDK versions from Cubism 5 SDK R7 alpha1 onward.`
- 一句话：**口径未变** —— 「Cubism 5 SDK」= R6 及以前，「**Cubism 5.4 SDK**」= **R7 alpha1 起**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— 索引/文档按此措辞写版本。
- 核实程度：页面已读

### 9. 5.4 SDK 两条**破坏性变更**仍在（未变）· cubism.live2d.com · 复核 2026-10-11
- 地址：https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html
- 原文证据（照抄）：
  > 计算顺序：`The calculation order has been updated to match the Original Workflow-based SDKs`（涉及物理模拟的参数结果会与 R5 不同）
  > Json：`… Version tag in Json files exported from Cubism Editor, such as model3.json …`；`… Version tag not recognized by the R7 alpha SDK can no longer be loaded.`
- 一句话：**两条未变** —— ① Unity 计算顺序改为与 Original Workflow 一致（物理结果与 R5 不同）；② SDK 识别 json 的 Version tag，**认不出的直接加载不了**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**✅ 落地（工程方）** —— 从 R5 升 R7 alpha 前先跑物理回归；外部导入的 json 留意 Version tag。
- 核实程度：页面已读

### 10. **SDK 分线各自最新版本**（双入口交叉验证；**未变**）· GitHub API + docs 公告线 · 复核 2026-10-11
- 入口：`https://www.live2d.com/en/sdk/download/<unity|web|native|java>/`（JS 页，仅取「有/无」）+ `https://api.github.com/repos/Live2D/<repo>/releases` + `https://docs.live2d.com/en/cubism-sdk-manual/top/`
- 原文证据（各线 releases 顶部 tag，照抄）：
  | 分线 | 最新 release tag | 日期 | 备注 |
  |---|---|---|---|
  | **Unity** | `5-r.4.2`（2026-05-14）· 次新 `5-r.5`（2026-04-02） | — | **R4_2 与 R5 并存**，R4_2 反而更晚 |
  | **Unreal** | `5-r.1-beta.2`（2026-09-29） | — | **全 SDK 线里最新的一条** |
  | **Web** | `5-r.5`（2026-04-02） | — | — |
  | **Native** | `5-r.5`（2026-04-02） | — | — |
  | **Java** | `5-r.5`（2026-06-04） | — | — |
  | **MotionSync** | `R2_1`（2026-08-25，Native + Unity） | — | 公告线 |
- 一句话：**全部未变** —— 与 R33 完全一致：Unreal R1 beta2（09/29）是全家族最新；Unity 两条线 **R5 + R4_2 并存**。
- 与上一轮差异：**无变化**（复现，双入口）。
- 可复用性：**⚠️ 参考** —— 团队 Unity 集成锚定 `R5 + R4_2`；**别把 SDK 版本写成一个数**。
- 核实程度：API + 页面已读

### 11. SDK 官方公告线**逐条未变**：最新仍 Unreal R1 beta2（2026-09-29）· docs.live2d.com · 复核 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-sdk-manual/top/ （`_r34/_dedupe_urls.txt` **0 命中**，但 R33 第 16 条已记其内容，本条只记变化）
- 原文证据（`Updated: 09/29/2026`，公告倒序，照抄）：
  > `Notification of Cubism 5 SDK R1 beta2 release (09/29/2026)` / `Notification of Cubism 5 SDK MotionSync Plugin R2_1 release (08/25/2026)` / `Notification of Cubism 5 SDK R5 release (06/04/2026)` / `Notification of Cubism 5 SDK R4_2 release (05/14/2026)` / `Notification of Cubism 5 SDK R5 release (04/02/2026)`
  > 页顶横幅：`5.4 alpha Now Available.`
- 一句话：**未变** —— 主公告线**没有 R6 / R7**（R6/R7 属「5.4 SDK」新线，仅存在于 alpha 手册），主线下最新仍是 Unreal R1 beta2（09/29）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考**。
- 核实程度：页面已读

### 12. 5.4 SDK **alpha2 手册仍 404**（仅 alpha1 存在）—— Editor 有 alpha2、SDK 手册停在 alpha1 · cubism.live2d.com · 复核 2026-10-11
- 地址：`https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha2/en/index.html` → **HTTP 404**（对照：`.../alpha1/en/index.html` → **HTTP 200**）
- 一句话：**未变** —— 第 3 轮连续复现：**Editor 手册有 alpha2，SDK 手册仍停在 alpha1**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— 即「5.4 SDK 仍只有 alpha1 可读」，别找 alpha2 SDK 手册。
- 核实程度：探测（404/200 已确认）

### 13. GitHub org `Live2D`：最近推送仍停在 **2026-09-29**，无新仓库 / 无 R7 tag（未变）· github.com/Live2D · 复核 2026-10-11
- 地址：https://api.github.com/orgs/Live2D/repos?sort=pushed&per_page=10
- 原文证据（最近 10 个，照抄）：
  > `Live2D/CubismUnityComponents | 2026-09-29 | ★264`、`Live2D/CubismUnrealEngineComponents | 2026-09-29 | ★32`、`CubismUnityMotionSyncComponents | 2026-08-25 | ★3`、`CubismNativeMotionSyncComponents | 2026-08-25 | ★5`、`CubismSpecs | 2026-08-05 | ★22`、`CubismNativeFramework | 2026-06-26 | ★264`、`CubismJavaSamples/JavaFramework | 2026-06-04`、`CubismWebSamples ★392 / CubismWebFramework ★237 | 2026-04-02`
  > 各线 releases 顶部**均无 `R7` tag**（见第 10 条表）
- 一句话：**未变** —— 组织内 10 月无动作，GitHub 上**没有 R7 alpha 的 tag/release**（R7 alpha 只在 alpha 下载站，不入公开仓库）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— 工程向。
- 核实程度：API 已读

---

## 四、官网新闻 / 授权定价 / npm

### 14. ⭐学生优惠**跨区块数字裂缝仍在**：学生页 `$46 USD` vs Store 结算 `$46.40 USD`（¥7,344 相同，80% OFF，截止 2027-03-31）· live2d.com / store.live2d.com · 复核 2026-10-11
- 地址：https://student.live2d.com/en/student-discount/ （`_r34/_dedupe_urls.txt` 命中）· https://store.live2d.com/en/ （**0 命中**，R33 已记其内容）
- 原文证据（照抄）：
  > 学生页：`Regular Price $ 231 USD [¥36,720]` / `80 % OFF` / `Student Discount Price $ 46 USD [¥7,344]` / `Offer ends March 31, 2027`
  > Store EN：`Student Discount with a massive 80% OFF—for a limited time only` / `3yr $46.40 USD [¥7,344]`（同页其它档位另有 `$231.99 USD [¥36,720]` 等）
  > 5.4 alpha 公告页页尾：`76% OFF coupon for a 3-year Live2D Cubism Editor PRO subscription`（**76% 遗留文案仍在**，见第 6 条）
- 一句话：**未变** —— 第 4 轮连续复现：学生页 `$46 USD`、Store 结算 `$46.40 USD`（¥7,344 相同）；`76% vs 80%` 遗留文案仍在。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**✅ 落地** —— 学生党认定 **「80% OFF / ≤$46.4 / ¥7,344 三年，截止 2027-03-31」**；$46 与 $46.40 差额属官方四舍五入口径；**别信 76% 老文案**。
- 核实程度：页面已读（3 个 URL 交叉）

### 15. npm 侧复核：`easy-live2d` 仍 1.0.0、`@laplace.live/three-live2d` 仍 0.10.1、`@charivo/render-live2d` 仍 0.6.6（均未变）；检索总量 448 → **449** · npm · 复核 2026-10-11
- 地址：https://registry.npmjs.org/easy-live2d · https://registry.npmjs.org/@laplace.live%2Fthree-live2d · https://registry.npmjs.org/@charivo%2Frender-live2d · https://registry.npmjs.org/-/v1/search?text=live2d&size=20
- 原文证据（registry JSON，照抄）：
  > `easy-live2d | latest 1.0.0 | 2026-09-24`（**与 R33 一致，未变**）
  > `@laplace.live/three-live2d | latest 0.10.1 | 2026-10-03 | created 2026-08-16 | "Live2D Cubism renderer for the three.js WebGPURenderer"`（未变）
  > `@charivo/render-live2d | latest 0.6.6 | 2026-10-06`（未变）
  > 同屏其它活跃项：`untitled-pixi-live2d-engine 1.4.0 (2026-09-20)`、`pixi-live2d-display-webgal 0.5.19 (2026-10-02)`、`live2d-widgets 1.0.1 (2026-05-22)`
  > 本轮 `search?text=live2d` 命中 `total: 449`（R33 为 448）
- 一句话：**npm 侧无新版本** —— R33 记的三个包（easy-live2d / three-live2d / charivo）**本轮全部未变**；检索总量 +1，但首屏无 10 月新发布的 Live2D 包。
- 与上一轮差异：**无实质变化**（三个包 version 未动）。
- 可复用性：**❌ 不采用（对 Ren'Py 本地项目）** —— Ren'Py 吃不了 npm；此为 **Web 前端**路线，仅供技术选型参考。
- 核实程度：API 已读

### 16. npm 补充：`@proj-airi/unplugin-live2d-sdk` 0.1.7（2026-04-14）—— AIRI 生态的「Vite 一键拉 Live2D SDK」插件（非新发，无变化）· npm · 复核 2026-10-11
- 地址：https://registry.npmjs.org/@proj-airi%2Funplugin-live2d-sdk （**`_r34/_dedupe_urls.txt` 0 命中**）
- 原文证据：
  > `latest 0.1.7 | 2026-04-14T21:36:05Z | created 2025-03-15`
  > `description: Vite plugin to download Live2D SDK`　versions tail `0.1.2 → … → 0.1.7`
- 一句话：这是 **AIRI（`moeru-ai/airi`）官方 org 下的子包** —— 做 Web 端 Live2D 时，**用插件自动拉 SDK**（免手放 Cubism 核心文件）。首次落到去重基线之外。
- 与上一轮差异：**新增条目**（R33 未列；但**不是新发布**，最后发版 2026-04，本轮无变化）。
- 可复用性：**⚠️ 参考（Web 侧）** —— 做网页 Live2D 的工程便利项；对 Ren'Py 不直接可用。
- 核实程度：API 已读

---

## 五、论坛一手正文 / 竞品 / 海外社区 / 商业生态

### 17. ⭐新增·官方一手·高复用：5.3「保存失败（出力に失敗）」根因 —— **参数数量是相乘增长**，官方建议改用 **blend shape** 替代普通 key · creatorsforum · 2026-09-22 → 2026-10-09
- 地址：https://creatorsforum.live2d.com/t/3979 （`/t/3979.json`；**单帖 ID 0 命中**，全新）
- 原文证据（照抄关键句）：
  > 标题：`Failed to Output error when saving the file`；用户 `zainulabideen.ht`（2026-09-22）：`約470MBのサイズのLive2Dモデルを制作していますが、新しい表情を作成している際にファイルの保存ができない…レイヤーやデフォーマを選択してキーを設定した後、ファイルを保存しようとすると、Live2Dは…「出力に失敗しました」というエラーを表…`
  > 官方 `enoko_staff`（2026-10-09，**根因回复**）：`おそらく口周りのオブジェクトについているパラメータが多すぎることが原因である可能性が高い`；`キーフォームはパラメータ数の掛け合わせで処理が増えていくので、キーの掛け合わせによる処理が非常に多くなったことで保存できる範囲を超えてしまったものと思われます`；`ファイルサイズが470MBであることが直接の原因ではありません`；`問題が顕著な表情パラメータは、通常のキーではなくブレンドシェイプで作成することをおすすめいたします。掛け算ではなく足し算の計算になるので、少ない処理で変形させることができます`；`とりあえず応急処置として…上唇に追加したキーを削除してください`
- 一句话：**本轮「制作小白」最有用的一条官方一手结论** —— ① 保存失败**不是文件大小（470MB）造成**；② 根因是**该部件挂在太多参数上，keyform 处理量按参数数「相乘」爆炸**；③ 解法：把表情参数改用 **blend shape（加法，不是乘法）**，或把 key 打在**包住整个嘴的 deformer**上，而不是直接打在唇的 ArtMesh 上。
- 与上一轮差异：**新增**。
- 可复用性：**✅ 落地** —— 直接给出「模型越做越存不动/越卡」的工程对策（**blend shape 替代 key、key 打在聚合 deformer 而非末端 mesh**）；且证明**与文件体积无必然关系**，别再盲目删素材。
- 核实程度：页面已读（主帖 + 官方 10-09 根因回复）

### 18. ⭐新增·官方复现：Unity **6.6 + URP3D** 下 Live2D「场景里能渲染、运行时不渲染」· creatorsforum · 2026-09-30 → 2026-10-02
- 地址：https://creatorsforum.live2d.com/t/3986 （`/t/3986.json`；**0 命中**）
- 原文证据（照抄）：
  > 用户 `ritto`（2026-09-30）：`Unity6.6 にて Universal 3D でプロジェクトを新規作成`；`CubismSdkForUnity-5-r.5.unitypackage をインポート`；`GetInstanceID() 関連のエラーが発生するので Fix compile errors on Unity 6.6 caused by obsolete GetInstanceID … PR #96 … のパッチを適用`；现象：`シーンには描画されるけど実行すると描画されない`
  > 官方 `ono-at-live2d-com`（2026-10-02）：`Cubism 5SDK for Unity R5は、macOS BigSurとiOS12はサポート対象外となっております。ただし、サポート環境にて現象の再現を確認いたしました。こちら調査いたします`
- 一句话：**官方确认为真 bug 且已复现** —— Unity **6.6 + URP3D + SDK for Unity R5** 组合下「Scene 视图渲染、运行时不渲染」；官方 10-02 认领调查。帖内还给出**已知前置坑**：Unity 6.6 上 `GetInstanceID()` 过时导致的编译错误，需打 **CubismUnityComponents PR #96** 补丁。
- 与上一轮差异：**新增**。
- 可复用性：**✅ 落地（Unity 集成方）** —— ① Unity 6.6 装 R5 先打 `PR #96`（`GetInstanceID` 过时修复）；② Unity 6.6 + URP3D 目前有「运行时黑屏」级 bug，**未获修复前别上生产**（可作为「用 Ren'Py 的 2D 路线为何更稳」的旁证）。
- 核实程度：页面已读（主帖 + 官方回帖）

### 19. ⭐新增：用户向官方**要外部联携 API 的「复制 / 左右镜像 keyform」能力**（10-05）· creatorsforum · 2026-10-05
- 地址：https://creatorsforum.live2d.com/t/3989 （`/t/3989.json`；**0 命中**）
- 原文证据（照抄）：
  > 标题：`【要望】外部連携APIにオブジェクト・キーフォームの複製／左右反転機能を追加してほしい`；用户 `まくまざわりんこ`（2026-10-05）：
  > `現在のAPIではパラメータキーの追加やオブジェクト属性・階層の編集は可能ですが、既存オブジェクトの複製、キーフォーム形状のコピー、頂点やフォームの左右反転ができないため、この工程を外部ツールから完結できません`；希望 API：`オブジェクト／階層の複製` / `キーフォームを含む複製` / `指定軸を基準としたフォームの反転` / `指定キー間のフォームコピー`
- 一句话：**外部联携 API 的能力边界被用户点名** —— 现在能加参数 key、改层级/属性，但**不能复制对象、不能复制 keyform 形状、不能左右镜像顶点** → 所以「左右眼/左右部件镜像」这类自动化**目前无法纯靠 API 完成**。
- 与上一轮差异：**新增**。
- 可复用性：**✅ 落地（对「想用脚本/agent 自动化 Cubism」的人）** —— 明确列出**当前 API 做不到的 4 件事**，避免在「镜像复制」上白费功夫；也说明官方 API 正被用户推着扩。
- 核实程度：页面已读（主帖；本轮无官方回复）

### 20. ⭐新增：纹理图集**反转变换后自动排版报 `NoArtMesh`**，官方定性「**非不具合、属规格**」并给恢复法 · creatorsforum · 2026-09-14 → 2026-10-04
- 地址：https://creatorsforum.live2d.com/t/3975 （`/t/3975.json`；**0 命中**）
- 原文证据（照抄）：
  > 用户 `ELU`（2026-09-14）：做完全部件 mesh + 打参数前先自动排版图集，之后「复制左眼→左右反转→粘到右眼」，结果 `テクスチャアトラスでその反転コピペした右目パーツ全てが『NoArtMesh』と表示`
  > 官方 `enoko_staff`（2026-09-24）：`今回の現象は不具合ではなく、Cubism Editorの仕様の範囲で起きている`；恢复法：`パーツパレットまたはデフォーマパレットで… 反転コピーの元になった左目の画像を右クリック ➞「選択アートメッシュの入力画像として設定」`
  > 官方（2026-10-01）：`モデリング画面ではパーツが問題なく表示できているようですので、そのままモデリングを続けていただいて問題ございません`
- 一句话：**官方口径（非 bug）** —— 「反转复制」后图集显示 `NoArtMesh` 是**规格内行为，数据没坏**；修复是「选中该 ArtMesh → 右键源图（左眼）→ 设为该 ArtMesh 的输入图像」。
- 与上一轮差异：**新增**。
- 可复用性：**✅ 落地** —— 做「左右镜像部件」时的**官方标准操作**；并给「该症状不是 bug、别删工程」的定心丸。
- 核实程度：页面已读（主帖 + 官方 2 回帖）

### 21. 复现：10-09 两条新用户报障仍**未获官方回复** —— 5.3.04「笔刷网格划割(β) 按钮消失」· AE 插件在 AE2026 失效 · creatorsforum · 2026-10-09
- 地址：https://creatorsforum.live2d.com/t/3993 · https://creatorsforum.live2d.com/t/3992 （`/t/3993.json`、`/t/3992.json`）
- 原文证据：
  > `/t/3993`（`白ぬこ`，2026-10-09）：`Cubism Editor 5.3.04 …ストロークによるメッシュ割り(β) のボタンが無くなってしまったのですが不具合でしょうか？`
  > `/t/3992`（`st`，2026-10-09）：`live2dのAEプラグインを使い…ヌルにトラッキングの動きを反映させることが … ヌルが全く動きません。after effects2026での症状です。`
- 一句话：**未变**（R33 记的两条 10-09 报障，本轮复核仍**各 1 帖、无官方回复**）—— 「5.3.04 + AE2026」组合仍是**未确认的报障**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— 按「留意」处理，不当作定论。
- 核实程度：页面已读

### 22. Spine 最新正式版仍 **4.3.26（2026-09-07）**，4.3.27「Unreleased」（未变）· esotericsoftware.com · 复核 2026-10-11
- 地址：https://esotericsoftware.com/spine-changelog （`spine-changelog` 在 `_r34/_dedupe_urls.txt` **0 命中**；R33 第 23 条已记内容）
- 原文证据（changelog 顶部，照抄）：
  > `4.3.27 Unreleased` / `4.3.26 7 Sep 2026 Fixed favor tool crash when the frame changes. Fixed loading some projects with deform timelines. Import PSD: improved source mesh [name:pattern] error messages.` / `4.3.25 6 Sep 2026` / `4.3.24 6 Sep 2026`
- 一句话：**未变** —— 4.3.27 仍处 Unreleased，正式版仍是 4.3.26（09-07）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**⚠️ 参考** —— Live2D 的主要商业竞品，偏骨骼动画路线。
- 核实程度：页面已读

### 23. Inochi2D 仍**停滞**：`inochi-creator` 最新仍 **v0.8.6（2024-09-18）**（未变）· GitHub API · 复核 2026-10-11
- 地址：https://api.github.com/repos/Inochi2D/inochi-creator/releases
- 原文证据：`v0.8.6 | 2024-09-18 | prerelease false` / `v0.8.5 | 2024-05-26` / `v0.8.3 | 2023-09-16`
- 一句话：**未变** —— 最新稳定版仍是 2024-09 的 0.8.6，**13 个月无稳定版**；生态停滞判定维持。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**❌ 不采用** —— 工具停更 → 无社区/无教程风险。
- 核实程度：API 已读

### 24. ⭐新增·源可读性翻转：Steam 商店搜索**本轮可读（200）**（上轮记 HTTP 000）；命中的 2026 年 Live2D 商业软件 3 款 · store.steampowered.com · 2026-10-11
- 地址：https://store.steampowered.com/search/?term=live2d · 详情走 `https://store.steampowered.com/api/appdetails?appids=<id>`
- 原文证据（appdetails，照抄）：
  > `Cursor for Live2D`（appid **4956950**）| `type: game` | `released: 7 Sep, 2026` | dev/pub `Bluebearry Studio` | `¥42.00` | `Import any Live2D model and let it follow your mouse, with physics effects, hotkey-triggered expressions, and idle animations.`（**生成式命名，实为「桌面跟随型 Live2D 播放器」**）
  > `Figryne Cast Studio Engine - Live2D Addon`（appid **5015260**）| `type: dlc` | `released: 3 Sep, 2026` | dev/pub `Mimizuku & co., Inc.` | `¥77.00` | `Use Live2D Cubism models as your avatar in Figryne Cast Studio Engine. Real-time face and expression tracking from a single webcam — in the same studio as your VRM setup…`
  > `RPG Developer Bakin Live2D Toolkit`（appid **4753800**）| `type: dlc` | `released: 17 Jun, 2026` | dev/pub `SmileBoom Co.Ltd.` | `"Live2D Toolkit" is an expansion DLC that lets you import Live2D models created with Live2D Cubism into games made with RPG Developer Bakin.`
  > 同屏还命中（游戏居多，非工具）：`hololive Dreams (2026-07-22)`、`PLATiNA :: LAB (2026-09-09)`、`Your Fiancée (2026-09-17)`
- 一句话：**新增来源** —— ① **Steam 搜索本轮从 000 变为 200 可读**（与退役名单不同，值得记）；② 2026 年在 Steam 上架了三款**以 Live2D 为卖点的商业成品**：桌面跟随播放器（¥42）、**单摄像头实时面捕 VTuber 工作室的 Live2D 插件**（¥77）、**RPG Developer Bakin 的 Live2D 导入 DLC**。
- 与上一轮差异：**新增**（R33 把 Steam 列为「HTTP 000 超时·不再投入」；本轮实测为 200，故记一次）。
- 可复用性：**⚠️ 参考** —— 对「做本地 Live2D 桌面/游戏集成」的读者是**商业成品风向**（尤其 Bakin DLC 与 Figryne 插件，都是「引擎/工作室挂 Live2D」的主流形态）；对 Ren'Py 无直接可用轮子。
- 核实程度：API 已读（3 个 appdetails + 搜索页）

### 25. 海外社区仍无料：HN `live2d` **2167 命中全误召**；dev.to 仍 **2 篇（最新 2026-06-08）**（未变）· 负结论 · 复核 2026-10-11
- 地址：https://hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story · https://dev.to/api/articles?tag=live2d
- 原文证据：
  > HN：`nbHits: 2167`，日期倒序首屏为 `Show HN: Claude Remote`、`Show HN: swe-mux`、`Ask HN: map enshittification` 等 **同名/近似误召**，**无一条真·Live2D story**
  > dev.to：`count 2` —— `2026-06-08 Open-LLM-VTuber Review: Offline AI Companion with Live2D`、`2026-04-04 easy-live2d v0.4.0: A Milestone Release for Live2D on the Web`
- 一句话：**未变** —— HN 对本主题**本轮仍未命中**（`search_by_date` 的 fuzzy 把 "lived/live diff" 算进来，须人工过滤）；dev.to 无新帖。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**❌ 不采用** —— 无料。
- 核实程度：API 已读

---

## §去重报告

**方法**：每条先 `grep -iF "<URL 或关键词>" _r34/_dedupe_urls.txt`；新增条目再对 `csdn-social-summary.md`（第三十三辑）与 `index.html` 二次比对。

#### A. 命中基线 → 只记「有无变化」，不重复收录（复核条目）

| 条目 | 命中位置 | 处理 |
|---|---|---|
| 第 2 条 `new-feature-introduction-title` | `_dedupe_urls.txt` **line 14** | 只记变化（未变） |
| 第 5 条 `editor-alpha/doc/manual/alpha2` | `_dedupe_urls.txt` **line 9** | 只记变化（未变） |
| 第 6 条 `cubism-5_4-alpha` | `_dedupe_urls.txt` 命中 | 只记变化（未变） |
| 第 14 条 `student.live2d.com` | `_dedupe_urls.txt` 命中 | 只记变化（未变） |
| 第 15 条 `easy-live2d` / `@laplace.live/three-live2d` | `_dedupe_urls.txt` 命中（R33 已收） | 只记变化（未变） |
| 第 22 条 `esotericsoftware` | `_dedupe_urls.txt` **line 129**（github.com/EsotericSoftware/spine-runtimes） | 第 22 条用 `spine-changelog` 入口，按复核 |
| 第 23 条 `Inochi2D` | `_dedupe_urls.txt` 6 命中（inochi2d / inochi-viewer / inochi-creator …） | 只记 releases 复核（未变） |
| 第 4 条 `www.live2d.com/en/information` | R33 第 18 条已记 | 只记变化（未变） |
| 第 1 条 `updates-history5-3` / 第 3 条 `cubism/update` / 第 11 条 `cubism-sdk-manual/top` | `_dedupe_urls.txt` **0 命中**，但 R33 均已记内容 | 按「复核」处理 |
| 第 8/9 条 `sdk-unity-alpha/doc/manual` | `_dedupe_urls.txt` **0 命中**，R33 第 13/14 条已记 | 按「复核」处理 |

#### B. 0 命中 → 收录（新入口 / 新条目）

- **论坛单帖**（`creatorsforum.live2d.com/t/<id>`，单帖 ID 全部 0 命中）：
  第 7 条 `/t/3983`（**进展新增**）· 第 17 条 `/t/3979`（**全新**）· 第 18 条 `/t/3986`（**全新**）· 第 19 条 `/t/3989`（**全新**）· 第 20 条 `/t/3975`（**全新**）· 第 21 条 `/t/3993`、`/t/3992`（复现）
- **npm**：第 16 条 `@proj-airi/unplugin-live2d-sdk`（**首次落到基线之外**；但非新发布）
- **Steam**：第 24 条 `store.steampowered.com` / 三个 appid（**全新来源**）

#### C. 关键词查重命中（弃）

- `store.live2d.com`：`_dedupe_urls.txt` 0 命中，但 R33 第 19 条已记其内容 → 第 14 条按「跨区块复核」处理。
- `charivo`：`_dedupe_urls.txt` 0 命中，但 R33 第 21 条已收 `@charivo/render-live2d` → 第 15 条按「复核」处理，不计新条。
- `laplace.live`：`_dedupe_urls.txt` 1 命中 → 归入第 15 条复核。
- 全部新条目对 `csdn-social-summary.md` **0 命中**（`t/3979`/`t/3983`/`t/3986`/`t/3989`/`t/3975`/`blend shape`/`Cursor for Live2D`/`Figryne`/`Bakin`/`steampowered`/`unplugin-live2d`/`anniversary` 均 0）。

#### D. 各源命中率（本轮 official 路）

| 源 | 入口 | 结果 |
|---|---|---|
| docs Editor patch 明细页 `updates-history5-3` | curl HTML | ✅ 复核（5.3.04，未变） |
| docs Editor Release History 表 | curl HTML | ✅ 复核（表内无 5.4） |
| Editor 5.4 alpha2 手册 | curl HTML | ✅ 复核（修订记录未变） |
| live2d.com 新闻 / 产品页 / 5.4 公告页 | curl HTML | ✅ 有（新闻停 07.17；产品页冲突仍在；76% 文案仍在） |
| docs SDK 手册公告线 / SDK 各平台下载页 | curl HTML | ✅ 公告线未变；下载页为 JS 渲染不吐版本（改走 releases） |
| SDK R7 alpha1 手册（最终 URL） | curl HTML | ✅ 复核（R6/R7 口径 + 2 破坏性变更未变） |
| SDK alpha2 手册 | curl | ❌ **404**（仅 alpha1 200） |
| GitHub org `Live2D` repos + 5 仓库 releases | curl API | ✅ 有（推送停 09-29；各线 tag 未变，**无 R7**） |
| Creators Forum `/latest.json` + 5 单帖 | curl JSON | ✅ **200**（新帖 /t/3979、/t/3986、/t/3989、/t/3975 + 进展帖 /t/3983） |
| 学生页 / Store / 5.4 公告页 | curl HTML | ✅ 有（$46 vs $46.40 裂缝仍在） |
| npm（search + 4 包） | curl JSON | ✅ 有（三包未变；总量 448→449） |
| esotericsoftware spine-changelog | curl HTML | ✅ 有（Spine 4.3.26 未变） |
| GitHub `Inochi2D/inochi-creator` releases | curl API | ✅ 有（停滞未变） |
| **Steam 商店搜索 + appdetails** | curl HTML/JSON | ✅ **200（上轮记 000）** —— 3 款 2026 Live2D 商业软件 |
| HN Algolia API | curl JSON | ❌ 空（2167 全误召） |
| dev.to API | curl JSON | ❌ 2 篇，无新 |
| Reddit / note.com / itch.io | curl | ❌ **HTTP 000**（退役，复测复现） |
| Stack Overflow `/questions/tagged/live2d` | curl | ❌ **HTTP 403**（WAF，新探明） |

**本轮条数**：**25 条**（含 **5 条全新官方论坛一手**：第 7、17、18、19、20 条；第 16 条为**新入口**、第 24 条为新来源 **Steam**；其余为复核「未变」与跨区块复核）。

---

## 负结论（含查法入口 / 命中数 / 复测条件）

> 纪律：一律写「**本轮未命中**」，不写「不存在」。

1. **Editor 5.3.05 未命中**。入口 `docs.../updates-history5-3/` + `new-feature-introduction-title/`；命中数 0（最新仍 5.3.04 / 09-03）。复测条件：出现 `5.3.05` 行或 5.4 进大版本表。
2. **5.4 未进 Release History 大表、未上官网新闻**。入口 `new-feature-introduction-title/`（表内无 5.4）+ `live2d.com/en/information/`（首条仍 2026.07.17）；命中数 0。复测条件：5.4 beta 发布时。
3. **官网「20 周年 / anniversary」内容未命中**。查法：对 `_p_news.html` grep `anniversary|周年|20th|20 year`；命中数 **0**。复测条件：新闻页出现周年字样。
4. **SDK 主公告线未出现 R6/R7**。入口 `docs.../cubism-sdk-manual/top/`（`Updated: 09/29/2026`）；命中数 0。R6/R7 仅存于 alpha 手册（5.4 SDK 线）。复测条件：主公告线出现新 `Notification of ... R6/R7`。
5. **GitHub org `Live2D` 无 10 月动作、无 R7 tag**。入口 `api.github.com/orgs/Live2D/repos?sort=pushed` + 5 仓库 `/releases`；最近推送仍 2026-09-29；各线 tag 顶仍 `5-r.4.2` / `5-r.1-beta.2` 等。复测条件：出现 10 月推送或 R7 tag。
6. **5.4 SDK alpha2 手册未命中**。查法：`/sdk-unity-alpha/doc/manual/alpha2/en/index.html` → **404**（alpha1 → 200）。即 **Editor 有 alpha2、SDK 手册仍停在 alpha1**。复测条件：alpha2 手册路径返回 200。
7. **HN 无料**。入口 `hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story`；命中数 2167，**真 story 0**（全误召）。复测条件：出现标题含 "Live2D" 的非误召条目。
8. **dev.to 无新帖**。入口 `dev.to/api/articles?tag=live2d`；命中数 2，最新 2026-06-08。复测条件：count>2 或最新日期 >2026-06-08。
9. **Reddit 未命中（本机 TLS 重置）**。入口 `reddit.com/r/Live2D/` → **HTTP 000**；与 R33 一致。复测条件：返回 200。
10. **note.com / itch.io 未命中**。入口 `note.com/search?q=live2d`、`itch.io/search?q=live2d` → 均 **HTTP 000**（退役名单一致，本辑复测复现）。复测条件：返回 200。
11. **Stack Overflow 标签未命中**。入口 `stackoverflow.com/questions/tagged/live2d` → **HTTP 403（WAF）**（新探明；该标签历史亦可能不存在）。复测条件：返回 200 或换 UA 后确认标签。
12. **Steam 源口径翻转**：R33 记 `store.steampowered.com` **HTTP 000 超时**；本轮实测搜索页 **200**、appdetails API **200**（见第 24 条）。复测条件：续监 `store.steampowered.com` 可达性，避免误判为「永久退役源」。
