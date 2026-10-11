# R33 · Live2D 制作专题 —— official 路（官方 / 海外社区 / 榜单）

- 轮次：第 33 轮（连续第 9 轮做 Live2D）
- 调研日期：2026-10-11（本文件所有 HTTP/API 取值均为该日）
- 对照基线：R32（同日）——Editor 5.3.04、5.4 alpha2、`Cubism 5 SDK ≤R6 / Cubism 5.4 SDK ≥R7 alpha1`、两处破坏性变更、creatorsforum 403→200、easy-live2d 1.0.0
- 查重基线：`_r33\_dedupe_urls.txt`（1418 行）+ `_r33\_dedupe_gh.txt`（1274 行）
- 口径纪律：结算页 > 产品页；docs Release History 表 > 产品页；**同一站内跨区块交叉验证**；负结论写「本轮未命中」
- 本路定位：**官方与海外社区路**。本轮核心新增 = **Editor 5.4 alpha2 手册正文**（R32 只从论坛取到 alpha2 的 build 号，没读过手册）

---

## 一、Editor 正式线（复核：逐条未变）

### 1. Cubism Editor 5.3 主线仍收在 **5.3.04（2026-09-03）**，无 5.3.05 · docs.live2d.com · 复核 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/ （**在 `_r33/_dedupe_urls.txt` 中 0 命中**；R32 的核心产出页，本轮只记「有无变化」）
- 原文证据（页面倒序，照抄版本行）：
  > `5.3.04 (09/03/2026)` → 仅一行：`Fixed an issue where items in the parts palette might be highlighted in a different color than usual when dragging.`
  > `5.3.04 beta1 (07/30/2026)` / `5.3.03 (06/16/2026)` / `5.3.03 beta1 (05/14/2026)` / `5.3.02 (04/02/2026)` / `5.3.01 (02/24/2026)` / `5.3.00 (01/20/2026)`
  > 页顶横幅改为：`5.4 alpha Now Available.`（R32 同）
- 一句话：**与 R32 完全一致**，5.3.04 仍是最新正式版，**5.3.05 不存在**；patch 明细页自 09/03 后无新增。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**落地** —— 小白继续装 **5.3.04**；「新建 PSD 模型可选 5.2 混合模式」等 5.3.x 结论全部继续有效。
- 核实程度：页面已读（curl 原始 HTML → 去标签）

### 2. Release History 大版本表：最新仍 `09/03/2026 · Cubism 5.3.04`，表内**无 5.4** · docs.live2d.com · 复核 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title/ （`_dedupe_urls.txt` line 8，**已收录**，本条只记变化）
- 原文证据（表格倒序首 6 行）：
  > `09/03/2026 Cubism 5.3.04` / `07/30/2026 Cubism 5.3.04 beta1` / `06/16/2026 Cubism 5.3.03` / `05/14/2026 Cubism 5.3.03 beta1` / `04/02/2026 Cubism 5.3.02` / `03/03/2026 Cubism 5.3.02 beta1`
  > 表首横幅：`5.4 alpha Now Available.` / `Click here to visit the announcement page for the alpha version.`
- 一句话：**未变** —— 大表仍以 5.3.04 收尾，5.4 只在页顶横幅出现、**未进版本表**（说明 5.4 仍在 alpha，未「发布」）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**参考** —— 索引如写「最新版本」应取「Editor 5.3.04（正式）/ 5.4 alpha（评估版，勿用于生产）」，**不能写成一个数**。
- 核实程度：页面已读

### 3. 产品页 `cubism/update` 仍写 **Ver.5.3.00**，与 docs 表 5.3.04 的官方口径冲突**持续** · live2d.com · 复核 2026-10-11
- 地址：https://www.live2d.com/en/cubism/update/ （`_dedupe_urls.txt` 中 **0 命中**）
- 原文证据：
  > 产品页「Latest Updates」逐条：`2026.01.20 : Ver.5.3.00` / `2025.02.04 : Ver.5.2.00` / `2024.07.30 : Ver.5.1.00` / `2023.09.21 : Ver.5.0.00`；大标题仍为 `Cubism Editor 5.3.00 released!`
  > docs Release History 表（第 2 条）：`09/03/2026 Cubism 5.3.04`
- 一句话：**冲突未修**（第 3 轮连续复现）——产品页落后 4 个 patch。**取值以 docs 表为准 = 5.3.04**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**落地** —— 「别看产品页写着 5.3.00 就以为没更新」，这是官方站内跨区块口径冲突的又一活样本。
- 核实程度：页面已读

---

## 二、5.4 alpha 线（本轮核心新增：R32 未读过的 alpha2 手册）

### 4. ⭐新增：Cubism **Editor 5.4 alpha2 用户手册**（2026-09-07）—— 补了「数据兼容」与「跨版本覆盖警告」两节 · cubism.live2d.com · 2026-09-07
- 地址：https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html （**`_dedupe_urls.txt` / index.html / csdn-summary 均 0 命中 → 收录**）
  （对照：alpha1 手册 = `.../alpha1/en/index.html`、`2026/07/14`）
- 原文证据（Revision History，照抄）：
  > 标题：`Live2D Cubism Editor 5.4 alpha2 User Manual`　页首日期：`09/07/2026`
  > `alpha2　09/07/2026　Added the following descriptions. ● "Notes on Data Compatibility" ● "Warning When Overwriting a Model of a Different Version" ● Update history ○ "Alpha version period" ○ "PSD Import Enhancements"`
  > `alpha1　07/14/2026　First edition`
- 一句话：alpha2 手册相对 alpha1 **新增两节**（数据兼容说明 + 跨版本覆盖警告）与两段更新历史（alpha 可用期、PSD 导入增强）→ 与 R32 从论坛拿到的「alpha2 build=2026/09/07」对上。
- 与上一轮差异：**新增**（R32 只知道 alpha2 存在与 build 号，**未读正文**）。
- 可复用性：**参考** —— 手册日期与结构本身是「alpha2 已发但仅评估用」的官方锚点。
- 核实程度：页面已读

### 5. ⭐新增·破坏性·落地：alpha2 保存的模型**打不开于 alpha1 / 5.3 之前**，且不保证 beta 能读 · cubism.live2d.com · 2026-09-07
- 地址：https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html （「Notes on Data Compatibility」节）
- 原文证据（照抄）：
  > `Models saved with 5.4.00 alpha2 cannot be loaded in 5.4.00 alpha1 or editors prior to 5.3.`
  > `Also, since this is an alpha version, there is no guarantee that it will be loadable in future 5.4.00 beta or later editors.`
  > `Please note that if you overwrite a model that was saved with an older version, the data may become unusable except in alpha2.`
- 一句话：这是 5.4 alpha 的**第二条硬约束**（第一条是 R32 记的 SDK 侧破坏性变更）——**alpha2 存的数据是「单向门」**：旧版打不开，未来 beta 也不保证能开；覆盖保存还会把数据「锁死」在 alpha2。
- 与上一轮差异：**新增**（本轮首次拿到官方正文原文）。
- 可复用性：**落地** —— 一句话给小白：**「别用 5.4 alpha2 存任何正式项目」**；要试就另存副本、别覆盖原文件。
- 核实程度：页面已读

### 6. ⭐新增·落地：alpha2 **PSD 导入增强** —— 支持「多图层合并 = 1 ArtMesh」，可不再写 PS 脚本 · cubism.live2d.com · 2026-09-07
- 地址：https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html （「PSD Import Enhancements」节）
- 原文证据（照抄）：
  > `When importing a PSD file, multiple layers can now be merged and handled as a single model image/ArtMesh. Previously, a PSD with a "1 layer = 1 ArtMesh" structure was required, but now PSDs with a "merged multiple layers = 1 ArtMesh" structure can also be imported as-is.`
  > `Operations that were previously provided via a Photoshop script, such as merging layer groups, merging masks, and dust cleanup, can now also be performed within the editor.`
  > `Add "*" to the name of layer groups you do not want to merge` / `Do not include adjustment layers or layer effects`
- 一句话：**这是本轮对「制作小白」最有用的一条** —— 以前 PSD 必须「一层一个 ArtMesh」，现在**多层可合并当一个 ArtMesh**；合并图层组、合蒙版、除尘从 PS 脚本搬进编辑器；`*` 前缀的图层组不合并；**别带调整图层/图层效果**。
- 与上一轮差异：**新增**（R32 完全没提 PSD 导入增强）。
- 可复用性：**落地** —— 直接改变 PSD 准备流程；但注意**目前只在 alpha2**，5.3.04 正式版尚无此能力。
- 核实程度：页面已读

### 7. ⭐新增·参考：alpha2 其余改动（跨版本覆盖警告 / PSD 画质弹窗取消 / auto layout 换算法）· cubism.live2d.com · 2026-09-07
- 地址：https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html （Update history / Precautions 节）
- 原文证据（照抄）：
  > `When overwriting a CMO3 file, a warning message is now displayed if the editor version differs from the one used for the previous save.`（并新增「Model File Version Display」，例：`5.2.02 (0000)`，括号内为内部版本号）
  > `When importing a PSD, the dialog for selecting the display quality of model images is no longer shown; the image is now set to actual size by default.`
  > `5.4 alpha's auto layout feature uses a new algorithm for the packing method to place objects, resulting in different layout results even with the same settings as in 5.3 and earlier.`
- 一句话：alpha2 还加了**覆盖不同版本 CMO3 时的警告弹窗**（可选择另存新文件）；PSD 导入不再弹画质选择、默认实际尺寸；**贴图集 auto layout 换打包算法 → 与 5.3 同设置结果也不同**（换了 5.4 别以为图集没变）。
- 与上一轮差异：**新增**。
- 可复用性：**参考** —— 「同设置结果不同」这条提醒：**不要把 5.3 的图集布局当基准去比 5.4 alpha**。
- 核实程度：页面已读

### 8. alpha 可用期仍 **截至 2026-10-18**（距今 7 天），alpha1 已于 2026-09-14 下线 · live2d.com / 手册 · 复核 2026-10-11
- 地址：https://www.live2d.com/en/information/cubism-5_4-alpha/ （`_dedupe_urls.txt` line 1410，已收录，只记变化）
- 原文证据：
  > `Available until "October 18, 2026." After this date, the alpha version will no longer be available.`
  > `Note: The availability period has been extended with the release of alpha2. Please note that alpha1 will no longer be available after September 14, 2026. If you wish to continue using the alpha version after this date, please install alpha2.`
- 一句话：**未变** —— 可用期与 R32 一致（10/18）；**距本轮仅剩 7 天**，之后 5.4 alpha 全面下线、等 beta。
- 与上一轮差异：**无变化**（复现，只补「剩余 7 天」这一时间敏感提醒）。
- 可复用性：**落地** —— 想试 5.4 新功能（如第 6 条 PSD 合并）的，**10/18 前**抓紧；过期后这一入口消失。
- 核实程度：页面已读

### 9. ⭐新增·社区验真：论坛用户求「回退 5.4 alpha1」，官方回复**明确不做前向兼容** · creatorsforum · 2026-09-16/17
- 地址：https://creatorsforum.live2d.com/t/3976 （`/t/3976.json`）
- 原文证据：
  > 标题：`急需回退5.4alpha1`（用户 2168627360，2026-09-16）：`以前はalpha1でテクスチャアトラスを配置したプロジェクトを5.3で開いて編集を続けることができましたが、現在はalpha2で保存したプロジェクトが編集を続けられなくなっています。`
  > 官方回复（`enoko_staff`，2026-09-17）：`alpha版はあくまでも新機能を先取りしてお試しいただくためのお試し版です。…新しいバージョン（今回の場合はalpha版）で編集、保存したファイルを古いバージョン（今回の場合は5.3）で開いて編集を行うこと（いわゆる前方互換）には対応しておらず…`
- 一句话：**第 5 条的「人肉实证」** —— 有用户正好踩中「alpha2 存档在 5.3 打不开」的坑，官方回复「alpha 就是试用版、**不支持前向兼容**」。这是官方正文之外的真实世界佐证。
- 与上一轮差异：**新增**（R32 只引了 /t/3983 的 alpha2 崩溃帖）。
- 可复用性：**落地** —— 强化「别用 alpha 存正式项目」这条；也给「图集自动排版很香但要等 beta」一个用户侧需求样本。
- 核实程度：页面已读（主帖 + 官方回帖）

### 10. ⭐新增：论坛官方帖 —— alpha2 发布公告（2026-09-07）与 5.4 alpha **用户问卷**（5–10 分钟） · creatorsforum · 2026-09-07
- 地址：https://creatorsforum.live2d.com/t/3969 （公告）· https://creatorsforum.live2d.com/t/3972 （问卷）
- 原文证据：
  > `/t/3969` 标题 `Cubism Editor 5.4.00 alpha2`，发帖人 `enoko_staff`，2026-09-07：`このalpha版は、Cubism Editor 5.4 に搭載予定の新機能や改善点を、正式リリースに先駆けて、いち早くお試しいただける、利用期間限定の評価用バージョンです。`
  > `/t/3972` 标题 `Cubism Editor / SDK 5.4.00 alpha版 アンケート受付中！`：`アンケートへの回答時間の目安は5～10分程度です。`（Google 表单，按语言分页）
- 一句话：官方在论坛**用日文官号发 alpha2 公告并征集问卷** —— 印证「5.4 的官方沟通主要走论坛 + docs，不走官网新闻」。
- 与上一轮差异：**新增**（论坛公告帖 R32 未列）。
- 可复用性：**参考** —— 想给 5.4 提需求/反馈，这是官方唯一公开收集渠道（第 11 条同源）。
- 核实程度：页面已读

### 11. ⭐新增：论坛实问 —— Unity 里 Live2D 与 Sprite 的**显示顺序**，官方答「用描画割り込み機能（R5 起）」 · creatorsforum · 2026-10-05/07
- 地址：https://creatorsforum.live2d.com/t/3991 （`/t/3991.json`）
- 原文证据：
  > 提问（`harusame`，2026-10-05）：`Live2Dモデルのプレハブの「Order in Group」…SpriteのOrder in Layerをそれぞれ「500」「-500」と差をつけてみたり、Z座標に差をつけてみたりしたのですが…`
  > 官方回复（`ono-at-live2d-com`，2026-10-07）：`Cubism 5 SDK for Unity R5以降では、Cubismモデルのメッシュ間に別のオブジェクトをはさみ込む場合、「描画割り込み機能」を利用します。`（附 docs 教程链接）
- 一句话：官方给出 Unity 集成侧的**正统答案** —— 想控制 Live2D 模型与 Sprite 的绘制前后关系，R5 起用「**描画割り込み機能**（drawing interleaving）」，而不是硬调 `Order in Layer`/Z 坐标。
- 与上一轮差异：**新增**。
- 可复用性：**落地（Unity 集成方）** —— 与「Ren'Py 2D 游戏」目标不同赛道，但对做「Live2D + Unity 立绘」的读者是可直接照抄的官方口径。
- 核实程度：页面已读（主帖 + 官方回帖）

### 12. ⭐新增：论坛新帖（10 月）——5.3.04「笔刷划割网格 β 按钮消失」· AE 插件 2026 追踪失效 · creatorsforum · 2026-10-09
- 地址：https://creatorsforum.live2d.com/t/3993 · https://creatorsforum.live2d.com/t/3992 （`/t/3993.json`、`/t/3992.json`）
- 原文证据：
  > `/t/3993`（`白ぬこ`，2026-10-09）：`【Cubism Editorのバージョン】Cubism Editor 5.3.04 …ストロークによるメッシュ割り(β) のボタンが無くなってしまったのですが不具合でしょうか？`
  > `/t/3992`（`st`，2026-10-09）：`live2dのAEプラグインを使いモデルにAEに持ってきたのですが、ヌルにトラッキングの動きを反映させることが … ヌルが全く動きません。after effects2026での症状です。`
- 一句话：**最新（10-09）两条未获官方回复的用户报障** —— ① 5.3.04 上「stroke 网格划割(β)」按钮消失（与第 1 条 5.3.04 只有一处面板高亮修复吻合，可能是回归/显示问题）；② Live2D AE 插件在 **After Effects 2026** 里 Null 追踪失效。
- 与上一轮差异：**新增**（10 月新帖）。
- 可复用性：**参考** —— 提醒「5.3.04 + AE 2026」组合目前有用户报障，**未获官方确认**，暂按「留意」处理（不是定论）。
- 核实程度：页面已读

---

## 三、SDK 线（复核：官方术语与破坏性变更逐条未变）

### 13. 官方术语复核：**Cubism 5 SDK = ≤ R6；Cubism 5.4 SDK = ≥ R7 alpha1**（未变）· cubism.live2d.com · 复核 2026-10-11
- 地址：**https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html**（`_dedupe_urls.txt` / index.html **0 命中**；R32/csdn-summary 记的是其短链 `cubism.live2d.com/link/manual5_4_alpha_sdk_en`，**本条的最终落地 URL 是首次落到去重基线之外**）
- 原文证据（「SDK Support for Cubism 5.3 New Features · Terminology」节，照抄）：
  > 标题：`Live2D Cubism 5 SDK R7 alpha1 User Manual`　页首日期：`2026/07/14`
  > `Cubism 5 SDK refers to SDK versions up to and including Cubism 5 SDK R6.`
  > `Cubism 5.4 SDK refers to SDK versions from Cubism 5 SDK R7 alpha1 onward.`
- 一句话：**口径未变**（与 R32 一致）——「Cubism 5 SDK」= R6 及以前，「**Cubism 5.4 SDK**」= **R7 alpha1 起**。SDK 是**分线各自版本**，不能写成一个数。
- 与上一轮差异：**无变化**（复现；本轮补上**可直读的最终 URL** 与页首日期）。
- 可复用性：**参考** —— 索引/文档写版本时按此措辞。
- 核实程度：页面已读

### 14. 5.4 SDK 两条**破坏性变更**仍在（未变）· cubism.live2d.com · 复核 2026-10-11
- 地址：https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html （「Compatibility of Cubism 5 SDK R7 alpha」节）
- 原文证据（照抄）：
  > `Changes Affecting Compatibility ● Change in Model Calculation Order ● Json Version Tag Identification Function ● Parameter Controller`
  > 计算顺序：`The calculation order has been updated to match the Original Workflow-based SDKs. As a result of this change, parameter update results involving physics simulation will differ from those in the R5 Official SDK.`（回退法：替换 `Assets/Live2D/Cubism/Framework/CubismUpdateExecutionOrder.cs` 的常量）
  > Json：`The SDK now identifies the Version tag in Json files … Json files exported with Cubism Editor up to Cubism 5.4 alpha that contain a Version tag not recognized by the R7 alpha SDK can no longer be loaded.`
- 一句话：**两条未变** —— ① Unity 计算顺序改为与 Native/Web 的 Original Workflow 一致，**涉及物理模拟的参数结果会与 R5 不同**（可改常量回退）；② SDK 开始**识别 json 的 Version tag，认不出的直接加载不了**（`.model3.json` 报错且不建 prefab）。
- 与上一轮差异：**无变化**（复现；R32 的「两个破坏性变更」结论本轮原文复核通过）。
- 可复用性：**落地（工程方）** —— 从 R5 升级到 R7 alpha 前，先跑一遍物理参数回归；外部导入的 json 要留意 Version tag。
- 核实程度：页面已读

### 15. Parameter Controller 支持范围仍为「5.4 SDK **alpha1 仅 Unity**，其他平台 beta1 起」（未变）· cubism.live2d.com · 复核 2026-10-11
- 地址：https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html （「SDK Support for Cubism 5.3 New Features」表）
- 原文证据：
  > 特性支持表：`Parameter Controller | Cubism 5 SDK: ✕ | Cubism 5.4 SDK: △`
  > `For the SDK, alpha1 supports SDK for Unity only. Support for other platforms is planned from beta1 onward.`
  > `model state set` 与 `Expanded editing support for external application integration API` 均标注为 **editor-only、SDK 不支持**
- 一句话：**未变** —— Parameter Controller 在 5.4 SDK 里 alpha1 **只有 Unity**；`model state set` 与「外部联动 API」是**编辑器独有、SDK 不支持**。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**参考** —— 别指望非 Unity 平台现在就能吃 Parameter Controller。
- 核实程度：页面已读

### 16. SDK 官方公告线**逐条未变**：最新仍 Unreal R1 beta2（2026-09-29）· docs.live2d.com · 复核 2026-10-11
- 地址：https://docs.live2d.com/en/cubism-sdk-manual/top/ （`_dedupe_urls.txt` **0 命中**，但 R32 第 12 条已记其内容，本条只记变化）
- 原文证据（`Updated: 09/29/2026`，公告倒序，照抄）：
  > `Notification of Cubism 5 SDK R1 beta2 release (09/29/2026)` → `Cubism 5 SDK for Unreal Engine R1 beta2`
  > `Notification of Cubism 5 SDK MotionSync Plugin R2_1 release (08/25/2026)` → `for Native R2_1` / `for Unity R2_1`
  > `Notification of Cubism 5 SDK R5 release (06/04/2026)` → `Cubism 5 SDK for Java R5`
  > `Notification of Cubism 5 SDK R4_2 release (05/14/2026)` → `Cubism 5 SDK for Unity R4_2`
  > `Notification of Cubism 5 SDK R5 release (04/02/2026)` → `for Native R5` / `for Web R5` / `for Unity R5`
  > 页顶横幅：`5.4 alpha Now Available.`
- 一句话：**未变** —— 主公告线**没有出现 R6 / R7**（R6/R7 属「5.4 SDK」新线，仅存在于 alpha 手册），主线下最新仍是 Unreal R1 beta2（09/29）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**参考** —— 团队内 Unity 集成锚定 `R5 + R4_2` 并存，与 R32 一致。
- 核实程度：页面已读

### 17. GitHub org `Live2D`：最近推送仍停在 **2026-09-29**，无新仓库 / 新 release（未变）· github.com/Live2D · 复核 2026-10-11
- 地址：https://api.github.com/orgs/Live2D/repos?sort=pushed
- 原文证据（最近 8 个，照抄）：
  > `Live2D/CubismUnityComponents | 2026-09-29T05:22:19Z | ★264`、`Live2D/CubismUnrealEngineComponents | 2026-09-29T03:34:21Z | ★32`、`Live2D/CubismUnityMotionSyncComponents | 2026-08-25 | ★3`、`Live2D/CubismNativeMotionSyncComponents | 2026-08-25 | ★5`、`Live2D/CubismSpecs | 2026-08-05 | ★22`、`Live2D/CubismNativeFramework | 2026-06-26 | ★264`
  > `CubismUnityComponents` releases API 顶部：`5-r.4.2 (2026-05-14)` / `5-r.5 (2026-04-02)`（**无 R6/R7 tag**）
- 一句话：**未变** —— 组织内 10 月无动作，且 GitHub 上**没有 R7 alpha 的 tag/release**（R7 alpha 只在 alpha 下载站，不入公开仓库）。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**参考** —— 工程向。
- 核实程度：API 已读

---

## 四、官网新闻 / 授权定价 / npm（含跨区块口径）

### 18. 官网新闻仍停在 **2026.07.17**，近 3 个月无新增（未变）· live2d.com · 复核 2026-10-11
- 地址：https://www.live2d.com/en/information/ （`_dedupe_urls.txt` line 1409，已收录，只记变化）
- 原文证据（日期倒序）：`2026.07.17 / 2026.07.14 / 2026.03.20 / 2026.02.13 / 2026.01.20 / 2025.11.14 …`（首条仍为 2026.07.17）
- 一句话：**未变** —— 5.3.01–5.3.04、5.4 alpha1/alpha2 **均未上官网新闻**；官方新动向只在 docs / 论坛。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**参考** —— 「新闻少 ≠ 停摆」，版本看 docs Release History 表。
- 核实程度：页面已读

### 19. ⭐新增：学生优惠**跨区块数字又裂了一处** —— 学生页 `$46 USD` vs Store 结算 `$46.40 USD`（¥7,344 相同）· live2d.com/store.live2d.com · 复核 2026-10-11
- 地址：https://student.live2d.com/en/student-discount/ （`_dedupe_urls.txt` line 1407）· https://store.live2d.com/en/ · https://www.live2d.com/en/information/cubism-5_4-alpha/ （页尾，line 1410）
- 原文证据（照抄）：
  > 学生页：`Regular Price $ 231 USD [¥36,720] / 3yr　80 % OFF　Student Discount Price $ 46 USD [¥7,344]　Offer ends March 31, 2027`
  > Store EN：`… Student Discount with a massive 80% OFF … *You must use the coupon code to receive the discount. 3yr $46.40 USD [¥7,344] Quantity`
  > info 页（alpha 公告页尾）：`… to receive a 76% OFF coupon for a 3-year Live2D Cubism Editor PRO subscription`（**76% 遗留文案仍在**）
- 一句话：本轮新增一处「同站跨区块不一致」——**学生页 `$46 USD`、Store 结算 `$46.40 USD`**（¥7,344 相同）；R32 记的「76% vs 80%」遗留文案**仍在**（info 页 + alpha 页尾）。
- 与上一轮差异：**新增**（$46 vs $46.40 是 R32 未发现的第三处数字裂缝）。
- 可复用性：**落地** —— 学生党认定 **「80% OFF / ≤$46.4 / ¥7,344 三年，截止 2027-03-31」**；$46 与 $46.40 差额属官方四舍五入口径，不必纠结；**别信 76% 的老文案**。
- 核实程度：页面已读（4 个 URL 交叉）

### 20. ⭐新增：npm `@laplace.live/three-live2d` **0.10.1（2026-10-03）** —— 面向 **three.js WebGPU** 渲染器的 Live2D 渲染器 · npm · 2026-10-03
- 地址：https://registry.npmjs.org/@laplace.live%2Fthree-live2d · https://www.npmjs.com/package/@laplace.live/three-live2d （**去重基线 0 命中**）
- 原文证据（registry JSON，照抄）：
  > `latest: 0.10.1`　`2026-10-03T13:28:00.597Z`
  > `description: Live2D Cubism renderer for the three.js WebGPURenderer`
  > `repository: github.com/laplace-live/persona`（monorepo，目录 `packages/three-live2d`）
  > 版本线（尾部）：`0.9.0 → 0.9.1 → 0.9.2 → 0.10.0 → 0.10.1`
- 一句话：**新入口** —— 把 Live2D 接到 **three.js 的 WebGPU 渲染器**上（不是 Pixi.js 路线），10 月初仍在活跃发版。
- 与上一轮差异：**新增**（R32 只收录到 `easy-live2d` 这类 Pixi 封装，未含 three.js/WebGPU 线）。
- 可复用性：**不采用（对 Ren'Py 本地项目）** —— Ren'Py 吃不了 npm；此为 **Web/WebGPU 前端**路线，仅供技术选型参考。
- 核实程度：API 已读

### 21. ⭐新增：npm `@charivo/render-live2d` **0.6.6（2026-10-06）** · npm · 2026-10-06
- 地址：https://registry.npmjs.org/@charivo%2Frender-live2d （**去重基线 0 命中**）
- 原文证据：
  > `latest: 0.6.6`　`2026-10-06T10:55:54.504Z`
  > `description: Live2D rendering engine for Charivo`　`repository: github.com/zeikar/charivo`（目录 `packages/render-live2d`）
  > 首次发布：`2025-10-14`
- 一句话：**新的独立渲染引擎**（Charivo 项目下的子包），10 月仍在维护。
- 与上一轮差异：**新增**。
- 可复用性：**不采用** —— 依附于 Charivo 生态、无独立文档，对「Ren'Py 小白」不构成可用轮子；仅作 Web 侧活跃度信号。
- 核实程度：API 已读

### 22. ⭐更新：npm `pixi-live2d-display-webgal` **0.5.19（2026-10-02）** / `easy-live2d` 仍 **1.0.0（2026-09-24，未变）** · npm · 2026-10-11
- 地址：https://registry.npmjs.org/-/v1/search?text=live2d （命中 `total: 448`）· https://registry.npmjs.org/easy-live2d
- 原文证据：
  > `pixi-live2d-display-webgal | 0.5.19 | 2026-10-02 | Live2D plugin for PixiJS`（R32 基线未含此包）
  > `easy-live2d | 1.0.0 | modified 2026-09-24 | dist-tags {latest:1.0.0, uat:1.0.0-uat.0}`（**与 R32 一致，未变**）
  > 同屏其它活跃项：`untitled-pixi-live2d-engine 1.4.0 (2026-09-20)`（其 GitHub 仓库 `Untitled-Story/...` 已在基线 line 421）、`live2d-widgets 1.0.1 (2026-05-22)`
- 一句话：npm 侧 **Pixi 系仍在更新**（webgal 分支 10-02）；`easy-live2d` **仍 1.0.0、无新版本**。
- 与上一轮差异：`easy-live2d` **无变化**；`pixi-live2d-display-webgal` 为**新增条目**。
- 可复用性：**参考（Web 侧）** —— 做网页 Live2D 的轮子池；对本项目（Ren'Py）不直接可用。
- 核实程度：API 已读

---

## 五、竞品 / 海外社区 / 榜单

### 23. Spine 最新正式版仍 **4.3.26（2026-09-07）**，4.3.27「Unreleased」（未变）· esotericsoftware.com · 复核 2026-10-11
- 地址：https://esotericsoftware.com/spine-changelog （**去重基线 0 命中**；R32 第 19 条已记内容）
- 原文证据（changelog 顶部，照抄）：
  > `4.3.27 Unreleased　Improved file IO retries, locking, and clean up.　Launcher 4.3.08: improved running offline with Windows.`
  > `4.3.26　7 Sep 2026　Fixed favor tool crash when the frame changes. Fixed loading some projects with deform timelines. Import PSD: improved source mesh [name:pattern] error messages.`
  > `4.3.25　6 Sep 2026` / `4.3.24　6 Sep 2026`
- 一句话：**未变** —— 4.3.27 仍处 Unreleased，正式版仍是 4.3.26（09-07），9 月上旬的密集小修之后再无新条目。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**参考** —— Live2D 的主要商业竞品；偏骨骼动画路线。
- 核实程度：页面已读

### 24. Inochi2D 仍**停滞**：`inochi-creator` 最新仍 **v0.8.6（2024-09-18）**（未变）· GitHub API · 复核 2026-10-11
- 地址：https://api.github.com/repos/Inochi2D/inochi-creator/releases
- 原文证据：`v0.8.6 | 2024-09-18T01:36:44Z | prerelease false` / `v0.8.5 | 2024-05-26` / `v0.8.3 | 2023-09-16`
- 一句话：**未变** —— 最新稳定版仍是 2024-09 的 0.8.6，14 个月无稳定版；与 R32 的「生态停滞」判定一致。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**不采用** —— 工具停更 → 无社区/无教程风险。
- 核实程度：API 已读

### 25. 海外社区仍无料：HN `live2d` 2167 命中**全误召**；dev.to 仍 **2 篇（最新 2026-06-08）**（未变）· 负结论 · 复核 2026-10-11
- 地址：https://hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story · https://dev.to/api/articles?tag=live2d
- 原文证据：
  > HN：`nbHits: 2167`，日期倒序首屏为 `Show HN: Claude Remote`、`Ask HN: map enshittification` 等 **同名/近似误召**，**无一条真·Live2D story**
  > dev.to：`count 2` —— `2026-06-08 Open-LLM-VTuber Review`、`2026-04-04 easy-live2d v0.4.0`
- 一句话：**未变** —— HN 对本主题**本轮仍未命中**（`search_by_date` 的 fuzzy 匹配把 "lived/live diff" 算进来，须人工过滤）；dev.to 无新帖。
- 与上一轮差异：**无变化**（复现）。
- 可复用性：**不采用** —— 无料。
- 核实程度：API 已读

### 26. 榜单：Artificial Analysis 可达（2026-10-11 快照）；「The AI Changelog」`theaic.io` 仍 000，替代入口 `aichangelog.dev` 可读；MLPerf 403 · 榜单 · 2026-10-11
- 地址：https://artificialanalysis.ai/ · https://theaic.io/ · https://aichangelog.dev/ · https://mlcommons.org/benchmarks/
- 原文证据（**带快照日期**，照抄）：
  > Artificial Analysis（200，标题 `AI Model & API Providers Analysis`）首页最新条目：`8 Oct GPT-6 Sol (Daybreak Blue, max)` / `7 Oct Anthropic has released Claude Haiku 5.5` / `1 Oct Grok 4.7 (Low)` / `30 Sept Gemini 4 Argon: Google is back…`
  > aichangelog.dev（200，标题 `AI Model Changelog — Track every AI model update in one place`）：`6 Providers　85 Models　72 Active　191 Updates Tracked`，最新条 `Sep 22, 2026 New Release OpenAI GPT-6 Sol … 1,050,000-token context window`
  > `theaic.io` → **HTTP 000**（与 R32 一致）；`mlcommons.org` / `/benchmarks/` → **HTTP 403**（WAF 拦截）
- 一句话：**新增** —— 榜单线带日期快照：AA（10-11 快照，条目到 10-08）、aichangelog.dev（最新 2026-09-22，85 模型/191 更新）。**theaic.io 仍不可达**（R32 记 000，本轮复现）；**MLPerf 401/403 不可直读**（新发现）。
- 与上一轮差异：R32 只探到 theaic.io=000；本轮**新找到可直读的 `aichangelog.dev`**，并首次探明 **mlcommons.org=403**。
- 可复用性：**不采用（对本专题）** —— 均为 LLM 模型榜，与 Live2D 制作无直接关系；仅作「AI 上游生态」背景，且**必须带快照日期**（本条目已带）。⚠️ 名称存疑：`aichangelog.dev` 标题为「AI Model Changelog」，**不确认即 team-lead 点名的「The AI Changelog」**。
- 核实程度：AA / aichangelog 页面已读；theaic.io / mlcommons 仅探测

---

## 本路去重报告 + 各源命中率

**去重执行**：每条先 `grep -iF "<关键词>" _r33/_dedupe_urls.txt index.html csdn-social-summary.md csdn-social-summary-v31.md`。

- **命中基线 → 只记「有无变化」不重复收录**：
  - `cubism-editor-manual/new-feature-introduction-title`（line 8，第 2 条）
  - `www.live2d.com/en/information/`（line 1409，第 18 条）· `.../cubism-5_4-alpha/`（line 1410，第 8/19 条）
  - `student.live2d.com/en/student-discount/`（line 1407，第 19 条）
  - `easy-live2d`（npm 包 R32 已收 1.0.0，第 22 条只记「未变」）
  - `cubism-sdk-manual/top`（0 命中于 urls.txt，但 R32 第 12 条已记内容 → 第 16 条按复核处理）
  - `updates-history5-3`（0 命中于 urls.txt，但 R32 第 1–4 条的核心产出 → 第 1 条按复核处理）
  - `cubism.live2d.com/link/manual5_4_alpha_sdk_en`（短链；R32/csdn-summary 已记「R7 alpha1 / 破坏性变更」→ 第 13/14/15 条按复核处理）
  - `github.com/EsotericSoftware/spine-runtimes`（基线 line 119；第 23 条改用 `spine-changelog` 入口）
  - `github.com/Inochi2D/inochi-creator`（基线 line 176；第 24 条只记 releases 复核）
  - `Untitled-Story/untitled-pixi-live2d-engine`（基线 line 421；第 22 条仅在同屏列表提及，不计新条）
- **0 命中 → 收录（新入口/新条目）**：
  - `cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html`（第 13/14/15 条，**首次落到可直读最终 URL**）
  - `cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html`（第 4/5/6/7 条，**全新**）
  - `creatorsforum.live2d.com/t/3976` · `/t/3969` · `/t/3972` · `/t/3991` · `/t/3993` · `/t/3992`（第 9/10/11/12 条；`creatorsforum` 在 index.html 仅 1 处旧引用，这些**单帖 ID 均 0 命中**）
  - `spine-changelog`（第 23 条）· `artificialanalysis`（第 26 条）· `aichangelog.dev`（第 26 条）
  - npm：`@laplace.live/three-live2d`（第 20 条）· `@charivo/render-live2d`（第 21 条）· `pixi-live2d-display-webgal`（第 22 条）
- **关键词查重命中（弃）**：`dsh-pet-live2d` 在 index.html 命中 1（已记 `A8Chann/dsh-pet-live2d`）→ **弃**，不重复计。

**各源命中率（本轮 official 路）**：

| 源 | 入口 | 结果 |
|---|---|---|
| docs Editor patch 明细页 `updates-history5-3` | curl HTML | ✅ 复核（5.3.04，未变） |
| docs Editor Release History 表 | curl HTML | ✅ 复核（表内无 5.4） |
| **Editor 5.4 alpha2 手册** | curl HTML | ✅ **有（本轮核心新增：数据兼容 + PSD 导入增强）** |
| Editor 5.4 alpha1 手册（对照） | curl HTML | ✅ 有（2026/07/14） |
| **SDK R7 alpha1 手册（最终 URL）** | curl HTML | ✅ 有（R6/R7 口径 + 2 破坏性变更，均未变） |
| live2d.com 新闻 / 产品页 / 5.4 公告页 | curl HTML | ✅ 有（新闻停 07.17；产品页 5.3.00 vs docs 5.3.04 冲突仍在；76% 文案仍在） |
| docs SDK 手册公告线 | curl HTML | ✅ 有（最新 Unreal R1 beta2 09/29，无 R6/R7） |
| Creators Forum `/latest.json` + 6 单帖 | curl JSON | ✅ **200**（新帖 10-09 ×2、10-05 ×2、回退帖 09-16、公告/问卷 09-07） |
| GitHub org `Live2D` repos/releases | curl API | ✅ 有（最近推送 09-29；无 R7 tag） |
| npm registry（search + 3 包 + easy-live2d） | curl JSON | ✅ **有（three-live2d / charivo / webgal 三个新条目）** |
| esotericsoftware changelog | curl HTML | ✅ 有（Spine 4.3.26 未变） |
| GitHub `Inochi2D/inochi-creator` releases | curl API | ✅ 有（停滞未变） |
| dev.to API | curl JSON | ❌ 2 篇，无新 |
| HN Algolia API | curl JSON | ❌ 空（2167 全误召） |
| Artificial Analysis | curl HTML | ✅ 有（10-11 快照） |
| aichangelog.dev（The AI Changelog 候选） | curl HTML | ✅ 有（最新 2026-09-22） |
| theaic.io | curl | ❌ HTTP 000（R32 同） |
| mlcommons.org（MLPerf） | curl | ❌ HTTP 403（WAF，新探明） |
| Reddit / note.com | curl | ❌ HTTP 000（退役，复测复现） |

**本轮条数**：**26 条**（含 **6 条全新**：第 4–7、9–12 中属 alpha2 手册与 10 月论坛；另 npm 3 条、榜单 1 条；其余 15 条为复核「未变」）。
**最硬的 3 条**：① **Editor 5.4 alpha2 手册正文**（数据兼容单向门 + PSD 多图层合并，R32 未读过手册）；② **SDK 线 R6/R7 口径与 2 破坏性变更原文复核通过（未变）**；③ **npm `@laplace.live/three-live2d`（three.js WebGPU 渲染 Live2D，10-03 新入口）**。
**口径有无新变动**：**Editor/SDK 版本口径全部未变**（5.3.04 / 5.4 alpha2 / R6→R7 alpha1 / 两破坏性变更）；**新增变动**仅在 alpha2 手册的「数据兼容」与「PSD 导入」两节（属 5.4 线内部细化，未触及 5.3/R6 既有口径）。

---

## 负结论（含查法入口 / 命中数 / 复测条件）

> 纪律：一律写「**本轮未命中**」，不写「不存在」。

1. **Editor 5.3.05 未命中**。查法入口 `docs.../updates-history5-3/` + `new-feature-introduction-title/`；命中数：0（最新仍 5.3.04 / 09-03）。**复测条件**：下次出现 `5.3.05` 行或 5.4 进大版本表。
2. **5.4 未进 Release History 大表、未上官网新闻**。入口 `new-feature-introduction-title/`（表内无 5.4）+ `live2d.com/en/information/`（首条仍 2026.07.17）；命中数 0。**复测条件**：5.4 beta 发布时。
3. **SDK 主公告线未出现 R6/R7**。入口 `docs.../cubism-sdk-manual/top/`（`Updated: 09/29/2026`）；命中数 0。R6/R7 仅存于 alpha 手册（5.4 SDK 线）。**复测条件**：主公告线出现新 `Notification of ... R6/R7`。
4. **GitHub org `Live2D` 无 10 月动作、无 R7 tag**。入口 `api.github.com/orgs/Live2D/repos?sort=pushed` + `/CubismUnityComponents/releases`；最近推送仍 2026-09-29；releases 顶仍 `5-r.4.2`。**复测条件**：出现 10 月推送或 R7 tag。
5. **5.4 SDK alpha2 手册未命中**。查法：`/sdk-unity-alpha/doc/manual/alpha2/en/index.html` → **404**（仅 alpha1 存在）。即 **Editor 有 alpha2、SDK 手册仍停在 alpha1**。**复测条件**：alpha2 手册路径返回 200。
6. **HN 无料**。入口 `hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story`；命中数 2167，**真 story 0**（全误召）。**复测条件**：出现标题含 "Live2D" 的非误召条目。
7. **dev.to 无新帖**。入口 `dev.to/api/articles?tag=live2d`；命中数 2，最新 2026-06-08。**复测条件**：count>2 或最新日期 >2026-06-08。
8. **The AI Changelog 官方域未得到**。入口 `theaic.io`（000，R32 同）、`theaichangelog.com`（000）、`ai-changelog.com`（000）；改用 `aichangelog.dev` 作替代（名称存疑）。**复测条件**：`theaic.io` 返回 200，或确认官方域。
9. **MLPerf 不可直读**。入口 `mlcommons.org` / `/benchmarks/` / `/benchmarks/inference-datacenter/` 均 **403**（WAF）。**复测条件**：换 UA/代理后返回 200。
10. **退役源复测复现**：`Reddit`（`reddit.com/r/Live2D/` → 000）· `note.com`（000）· `theaic.io`（000）—— 与既知退役名单一致；**退役源仍应每辑复测一次**（本辑已完成）。
