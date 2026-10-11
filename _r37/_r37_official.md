# 第三十七辑 · official 路（2026-10-11）

> 采集时间：2026-10-11 20:2x–20:4x（本文件所有 HTTP/API 取值均为该日）
> 本路负责：`live2d.com` 官方站点与文档 · `community.live2d.com`（Vanilla 论坛）· `creatorsforum.live2d.com`（Discourse 官方论坛）· 海外社区 · 竞品/替代
> 路径硬编码：索引 `index.html`（**1362 卡片**）· 经验帖 `csdn-social-summary.md` · 去重基线 `_r37/_dedupe_urls.txt`（**1379 行**）+ `_r37/_dedupe_gh.txt`（**1337 行**）
> 口径纪律：**结算页 > 产品页；docs Release History 表 > 产品页；同一站内跨区块交叉验证**；负结论一律写「本轮未命中」

---

## 一、本路一句话

**官方主干版本口径本轮逐条未变**（Editor 5.3.04 / 5.4 alpha2 / SDK「R6→R7 alpha1」/ Unreal R1 beta2 / 学生 $46·$46.40 / 官网新闻停 2026-07-17 / Spine 4.3.26 / Inochi2D creator 停滞）；
**真正的新东西全在官方论坛一手**：官方本轮**新认领两条 SDK bug**（① Unity R4 `motion3.json` 覆盖重导入 `IndexOutOfRangeException`；② Unity R5+「描画割り込み機能」现有不具合），并**出面否认 Unreal SDK 已停摆**（9-9 说「不会停、正在做下个版本」→ 9-29 beta2 落地，闭环）。
**⚠️ 5.4 alpha 可用期冲突本轮正式收口 = 采信 `2026-10-18`**，`2026-09-14` 是 **alpha1 的下线日**（被 cn 路误当成整条 alpha 线的可用期，详见 §二·末条 + O4）。

---

## 二、官方主干口径逐条复核表（变了 / 未变，都写）

| 项 | 上辑记的值 | 本轮实测 | 判定 | 出处 URL |
|---|---|---|---|---|
| Editor 正式版 | 5.3.04（2026-09-03） | **5.3.04（09/03/2026）**，无 5.3.05 | ✅ **未变** | https://docs.live2d.com/en/cubism-editor-manual/updates-history5-3/ |
| Release History 大表 | 表内无 5.4 | 表顶仍 `09/03/2026 Cubism 5.3.04`，表首横幅仍 `5.4 alpha Now Available.` | ✅ **未变** | https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title/ |
| Editor alpha | 5.4 alpha2 | 手册修订记录仍 `alpha2 09/07/2026` / `alpha1 07/14/2026`，无 alpha3 | ✅ **未变** | https://cubism.live2d.com/editor-alpha/doc/manual/alpha2/en/index.html |
| **⚠️ 5.4 alpha 可用期** | **09-14（cn）vs 10-18 冲突未归一** | **官方页两处原话 `Available until "October 18, 2026."`；`September 14, 2026` 仅指 `alpha1 will no longer be available after`** | ✅ **本轮收口 = 采信 10-18** | https://www.live2d.com/en/information/cubism-5_4-alpha/ |
| SDK 术语 | R6 → R7 alpha1 | `Cubism 5 SDK …up to and including…R6.` / `Cubism 5.4 SDK …from…R7 alpha1 onward.` | ✅ **未变** | https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html |
| SDK 两条破坏性变更 | 已在档 | ①计算顺序改为与 Original Workflow 一致；②`Version tag` 认不出的 json 加载不了 | ✅ **未变** | https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha1/en/index.html |
| SDK alpha2 手册 | 404（仅 alpha1） | `sdk-unity-alpha/.../alpha2/` → **HTTP 404**；alpha1 → 200 | ✅ **未变（第 4 次复现）** | https://cubism.live2d.com/sdk-unity-alpha/doc/manual/alpha2/en/index.html |
| Unreal SDK | R1 beta2（2026-09-29） | releases 顶部仍 `5-r.1-beta.2 | 2026-09-29` | ✅ **未变** | https://api.github.com/repos/Live2D/CubismUnrealEngineComponents/releases |
| SDK 公告线 | 主流最新 Unreal R1 beta2 | `docs.../cubism-sdk-manual/top/` `Updated: 09/29/2026`，倒序首条仍 `Notification of Cubism 5 SDK R1 beta2 release (09/29/2026)` | ✅ **未变** | https://docs.live2d.com/en/cubism-sdk-manual/top/ |
| 各线 SDK tag | Unity `5-r.4.2`/`5-r.5`、Web/Native/Java `5-r.5` | 逐条一致（Unity `5-r.4.2` 2026-05-14 / Unreal `5-r.1-beta.2` 09-29 / Web+Native `5-r.5` 04-02 / Java `5-r.5` 06-04），**仍无 R7 tag** | ✅ **未变** | https://api.github.com/repos/Live2D/CubismUnityComponents/releases 等 |
| GitHub org 推送 | 停 2026-09-29 | 最近推送仍 `2026-09-29`（Unity/Unreal），10 月无新 repo | ✅ **未变** | https://api.github.com/orgs/Live2D/repos?sort=pushed&per_page=10 |
| **产品页版本号冲突** | 产品页 `Ver.5.3.00` vs docs `5.3.04`（已连续 4 轮+） | 产品页 `Latest Updates` 首条仍 `2026.01.20 : Ver.5.3.00`；docs 表仍 5.3.04 → **冲突持续** | ⚠️ **未变（冲突未修）** | https://www.live2d.com/en/cubism/update/ |
| 学生优惠（学生页） | `$46 USD` / ¥7,344 / 80% / 截止 2027-03-31 | 原样：`Regular Price $ 231 USD [¥36,720]` / `80 % OFF` / `Student Discount Price $ 46 USD [¥7,344]` / `Offer ends March 31, 2027` | ✅ **未变** | https://student.live2d.com/en/student-discount/ |
| 学生优惠（Store 结算） | `$46.40 USD` [¥7,344]，$231.99 | 原样：`3yr $46.40 USD [¥7,344]`、`$231.99 USD [¥36,720]/3yr`、`80% OFF` | ✅ **未变（$46 vs $46.40 裂缝仍在）** | https://store.live2d.com/en/ |
| 76% 遗留文案 | 仍在 | 5.4 alpha 公告页仍 `76% OFF coupon for a 3-year …PRO subscription`（该页 `80%` = **0 命中**） | ✅ **未变** | https://www.live2d.com/en/information/cubism-5_4-alpha/ |
| 官网新闻 | 首条 2026-07-17 | 首条仍 `2026.07.17 Campaign Get 20% OFF Live2D Cubism PRO! Ends Monday, July 27, 2026`（已过期活动） | ✅ **未变（至少连续 4 辑以上冻结）** | https://www.live2d.com/en/information/ |
| Spine | 4.3.26 | changelog 顶仍 `4.3.27 Unreleased` / `4.3.26 7 Sep 2026` | ✅ **未变** | https://esotericsoftware.com/spine-changelog |
| Inochi2D（creator） | 停滞 | `inochi-creator` releases 顶仍 `v0.8.6 | 2024-09-18` | ✅ **未变（creator 停更）** | https://api.github.com/repos/Inochi2D/inochi-creator/releases |
| **未收录待办**：Release History 正确 URL | 上辑 `/release-history/` 404 未解 | **`/en/cubism-editor-manual/release-history/` → 404（复现）**；正确入口 = **`updates-history/`（Hub，导航含 `Release History` 分组）+ `new-feature-introduction-title/`（大版本表）+ `updates-history5-3/`（5.3 patch 明细）** | ✅ **本轮解决** | https://docs.live2d.com/en/cubism-editor-manual/updates-history/ |

> **§二·末条 · 5.4 alpha 可用期冲突收口依据（原话）**
> - 官网 5.4 公告页（`https://www.live2d.com/en/information/cubism-5_4-alpha/`）**两处**原文：`Available until "October 18, 2026." After this date, the alpha version will no longer be available.` → **这是「整条 alpha 线」的可用期 = 10-18**。
> - 同页另一句：`Please note that alpha1 will no longer be available after September 14, 2026. If you wish to continue using the alpha version after this date, please install alpha2.` → **`09-14` 是 `alpha1` 的下线日**。
> - 官方论坛同口径复证：`/t/3976` 官方 `enoko_staff`（2026-09-17）原文 `alpha1は「2026年9月14日」まで利用可能で…`（见 O4）。
> - **结论：cn 路「可用期至 2026-09-14」= 把 alpha1 下线日错当整条线可用期；本路采信 `2026-10-18`。**

---

## 三、⭐ 新增一手正文（每条 ###）

### O1. ⭐官方新认领 bug：Unity 中 Live2D 模型与 Sprite 显示顺序 —— 官方指「描画割り込み機能」，并承认该功能**现不具合** · creatorsforum · 2026-10-05 → 2026-10-07
- URL：https://creatorsforum.live2d.com/t/3991
- 正文要点（抄原话）：
  - 用户 `harusame`（2026-10-05）：`Live2Dモデルのプレハブの「Order in Group」…SpriteのOrder in Layer…をそれぞれ「500」「-500」と差をつけてみたり…Z座標に差をつけたりしたのですがSceneビューでもGameビューでもSpriteが手前に表示されてしまいます`（**用 `Order in Group` / Z 坐标都压不过 Sprite**）。
  - 官方 `ono-at-live2d-com`（2026-10-07）：`Cubism 5 SDK for Unity R5以降では、Cubismモデルのメッシュ間に別のオブジェクトをはさみ込む場合、「描画割り込み機能」を利用します`；**`ただし、描画割り込み機能は現在不具合がございます。こちらは次回のリリースで修正いたします`**。
- 对「做模型的人」有什么用：**✅ 落地**（Unity 集成方）—— 「模型/Sprite 前后层级怎么调都反」时，官方指定通路是 **R5+ 的「描画割り込み機能（Z-Interlocking）」**；且该功能**官方承认当前有 bug、下个 release 才修** → 现阶段别把「模型与背景 Sprite 之间的图层穿插」当可交付项。

### O2. ⭐官方新认领 SDK bug：用**参数数变多**的 `motion3.json` 覆盖重导入 → Unity `IndexOutOfRangeException` · creatorsforum · 2026-09-17 → 2026-09-30
- URL：https://creatorsforum.live2d.com/t/3978
- 正文要点（抄原话）：
  - 用户 `koha`（2026-09-17）：环境 `Cubism 5 SDK for Unity R4（5-r.4） / Windows 11 / Unity 2022.3.62f2`；现象 `同名の新しいモーションデータで上書きして再インポートしたところ、` **`System.IndexOutOfRangeException: Index was outside the bounds of the array. at Live2D.Cubism.Framework.MotionFade.CubismFadeMotionData.CreateInstance(...)`**。
  - 官方 `ono-at-live2d-com`（2026-09-30）：`はい、確認したところ、こちらはCubism SDKの不具合になります`；`こちらの修正内容につきましては、今後の更新で対応いたします`。
- 对「做模型的人」有什么用：**✅ 落地（Unity 集成方）** —— 用同名新的 `motion3.json`（**参数/曲线数增加**）覆盖工程里旧文件会触发 `MotionFade` 侧数组越界崩溃；官方定性为 SDK bug、待后续版本修。**短期规避：覆盖前先删旧 `.fade.asset` / 用全新建工程导入。**

### O3. ⭐官方否认 Unreal SDK 停摆：`開発・サポートを停止する予定はございません` —— 20 天后 beta2 落地，闭环 · creatorsforum · 2026-09-08 → 2026-09-09
- URL：https://creatorsforum.live2d.com/t/3973
- 正文要点（抄原话）：
  - 用户 `unun`（2026-09-08）：`UnrealEngine向けのSDKの更新が2025-05-29で停止していますが、今後UnrealEngineをサポートする予定はないと考えていいでしょうか？`
  - 官方 `nakayasu_staff`（2026-09-09）：**`Unreal Engine向けSDKの今後のサポートにつきまして、開発・サポートを停止する予定はございません。現在、次期アップデートのリリースに向けて開発を進めております。`**
- 对「做模型的人」有什么用：**✅ 落地** —— 这条把「Unreal SDK 是不是死了」的问题**在官方口径上钉死**：没死；且其**「次期アップデート」= 20 天后（09-29）发布的 `5-r.1-beta.2`**（见 §二 Unreal 条）。选 Unreal 路线可继续等。

### O4. ⭐5.4 alpha 可用期冲突的**官方原始出处**：`alpha1は「2026年9月14日」まで利用可能` · creatorsforum · 2026-09-16 → 2026-09-17
- URL：https://creatorsforum.live2d.com/t/3976
- 正文要点（抄原话）：
  - 用户 `2168627360`（2026-09-16，标题「急需回退5.4alpha1」）：`以前はalpha1でテクスチャアトラスを配置したプロジェクトを5.3で開いて編集を続けることができましたが、現在はalpha2で保存したプロジェクトが編集を続けられなくなっています`（**alpha2 存的工程回不到 5.3**）。
  - 官方 `enoko_staff`（2026-09-17）：`新しいバージョン（…alpha版）で編集、保存したファイルを古いバージョン（…5.3）で開いて編集を行うこと（いわゆる前方互換）には対応しておらず…`；**`alpha1は「2026年9月14日」まで利用可能で、期限が過ぎると使用できなくなる`**。
- 对「做模型的人」有什么用：**✅ 落地** —— ① **`09-14` 的官方语境 = alpha1 到期**（本路收口 10-18 的直接佐证）；② **alpha 版无「前方兼容」**：用 5.4 alpha2 存过的工程，**5.3 打不开也编辑不了** → 想用 alpha 的，务必先备份 / 另存工程名。

### O5. 官方答疑：在 5.3.02 里做动画保存后「模型数据消失」—— 实为存了 `.can3`、**没存 `.cmo3`** · creatorsforum · 2026-09-13 → 2026-09-18
- URL：https://creatorsforum.live2d.com/t/3974
- 正文要点（抄原话）：
  - 用户 `ラド`（2026-09-13，`Cubism Editor 5.3.02`）：做完 XY 轴/物理/表情，做流泪动画「一通りキーを打って保存をして閉じました」，次日 `モデルデータの名前がUnt…`（模型数据变 Untitled、原数据找不到）。
  - 官方 `enoko_staff`（2026-09-18）：`アニメーションファイル（can3）を作成して保存したので「Untitled Animation.can3」が出来上がります。これは通常の挙動です`；`アニメーションファイルは保存されますが、モデルファイルは保存されません`；并追问是否在关闭前对 `.cmo3` 的「保存吗」提示点了保存。
- 对「做模型的人」有什么用：**✅ 落地** —— 分清 **`.cmo3`（模型）vs `.can3`（动画）是两份文件**；只存动画 ≠ 存模型。给「模型莫名变 Untitled/丢改动」一个非 bug 的官方解释与自查点。

### O6. 功能请求升级：单参数**往复（30→0）时无法「只在返回段自动隐藏」**，用户转正式 Feature Request · creatorsforum · 2026-09-28 → 2026-10-01
- URL：https://creatorsforum.live2d.com/t/3985
- 正文要点（抄原话）：
  - 用户 `017`（2026-09-28）：用 blend shape 做「条纹自下而上流动」，参数 `0→30` 映射权重 `0→100%`；但返回时「逆再生」露馅，只能**在时间轴上对每次返回手动补打「不透明度」key**，反复动画下 `作業負担が非常に大きい`。
  - 用户自结（2026-10-01）：`現在のLive2Dの仕様では「単一パラメータの往復で、戻りのみ自動で非表示にする」といった挙動を直接制御することは難しい`；于是把帖 `カテゴリを質問から機能追加・要望へ変更`，请求「按参数增减方向切换不同值/blend shape」。
- 对「做模型的人」有什么用：**⚠️ 参考** —— 明确「**同一参数的往返无法分段自动化**」是当前规格缺口；做循环特效时预留手工补 key 的工作量，别指望纯参数驱动。

### O7. 老帖复活：`デフォーマを削除し、パラメータを子要素に反映` 的 **blend shape 支持已实现** · creatorsforum · 2022-11 → 2026-10-08
- URL：https://creatorsforum.live2d.com/t/1189
- 正文要点（抄原话）：
  - 轨迹：用户 `月_十` 2022-11 问「消除变形器并由子物体继承参数，不会继承融合变形」→ 官方 2022-11-18 `目前Blendshape不支持…` → 用户 2026-04-23 再问能否支持 → 官方 2026-04-30 `今のところはまだご要望を実現できておりません…開発チームにご要望を共有` → **用户 2026-10-08：`ブレンドシェイプ「デフォーマを削除し、パラメータを子要素に反映する」要望 実装されてました。ありがとうございます`**。
- 对「做模型的人」有什么用：**⚠️ 参考** —— 一个「**用户长跑 4 年的功能请求已落地**」的一手确认（blend shape 现可「删 deformer 并让子元素继承参数」），做表情/形变时可复核该能力；也说明官方对需求积累是会兑现的。

### O8. community 论坛·性能一手：「复杂 Warp Deformer 性能问题」+ 用户规避技巧，官方 10-01 转开发组 · community.live2d.com · 2026-09-11 → 2026-10-01
- URL：https://community.live2d.com/discussion/2385
- 正文要点（抄原话，Discourse 之外的 Vanilla 论坛，经 `/api/v2/comments?discussionID=2385` 取正文）：
  - 用户回复（2026-09-14）：`there is an issue with having anything in root, lags the model in general, (to the point it can be 5seconds + lag)`（**根目录里放任何东西都会拖慢模型，可达 5 秒以上卡顿**）。
  - 用户（2026-09-24，环境 `RTX 3060 / i7 10700K / 32GB`）：`it's just showing the name of the method that is taking a long time. The problem is that it's being called even when other deformers that can't af…`（耗时方法被无关 deformer 也调用）。
  - 官方 `enoko_staff`（2026-10-01）：`We have shared this issue with the development team.`
- 对「做模型的人」有什么用：**⚠️ 参考** —— 复杂 Warp Deformer 有**性能放大**问题（官方已转开发组）；实操规避：**别把部件摊在根目录、用分组收纳**，可减卡顿。

---

## 四、竞品 / 替代品动态

- **Spine（Esoteric）**：正式版仍 **4.3.26（7 Sep 2026）**，`4.3.27` 仍 **Unreleased**（changelog 原文 `4.3.27 Unreleased Improved file IO retries, locking, and clean up.`）→ **未变**。https://esotericsoftware.com/spine-changelog
- **Inochi2D（开源替代）**：**creator 停更**（`inochi-creator` 稳定版仍 `v0.8.6 | 2024-09-18`），**但核心库 `Inochi2D/inochi2d` 本轮有新推送 `2026-10-03`（★1811）** → 「创作端停滞、SDK/核心仍在动」的**分裂状态**（上辑只记了 creator 停滞，本轮补齐核心库活跃事实）。https://api.github.com/repos/Inochi2D/inochi-creator/releases · https://api.github.com/orgs/Inochi2D/repos?sort=pushed
- **VRM / VRoid（3D 替代路线）**：`vrm.dev` → **200**；`vroid.com/en/studio` → **403（WAF）**。本轮**未取得**可引用的 VRM/VRoid 新动态 → 记「本轮未命中」。
- **AI / Live2D 相关**：`dev.to` 仍 2 篇（最新 `2026-06-08`），`HN` 仍 2167 命中全误召 → **海外社区本轮未命中新料**（见 §六）。

---

## 五、可达性复测表

| 源 | 本轮实测 | 处置 |
|---|---|---|
| `community.live2d.com` | **200**（Vanilla 论坛；`/api/v2/discussions` 可用，`/latest.json` 404） | 可读；改用 Vanilla API 取列表 |
| `creatorsforum.live2d.com` | **200**（`/latest.json` 可用） | 可读；本轮主要一手来源 |
| `docs.live2d.com` | **200** | 可读 |
| `cubism.live2d.com`（alpha 手册） | **200**（alpha2 手册 / SDK alpha1）；SDK alpha2 → **404** | 可读 |
| `store.live2d.com` / `student.live2d.com` | **200** | 可读 |
| `store.steampowered.com` | **200** | **延续上辑回滚结论**，仍可读 |
| `esotericsoftware.com` | **200** | 可读 |
| `vrm.dev` | **200** | 可读（无新料） |
| `vroid.com` | **403**（WAF） | 本轮未命中 |
| `note.com` | **000**（本轮复测 1 次） | **维持退役**（本轮未命中，非「不存在」） |
| `reddit.com`（`/r/Live2D/.json`） | **000** | 维持退役（本轮未命中） |
| `medium.com` | **000** | 维持退役（本轮未命中） |
| `hn.algolia.com` | **200** 但**全误召** | 无料 |

---

## 六、负结论（一律写「本轮未命中」）

1. **Editor 5.3.05 未命中**。入口 `updates-history5-3/` + `new-feature-introduction-title/`；最新仍 `5.3.04 (09/03/2026)`。复测条件：出现 `5.3.05` 行。
2. **5.4 未进 Release History 大表、未上官网新闻**。入口 `new-feature-introduction-title/`（表内无 5.4）+ `live2d.com/en/information/`（首条仍 `2026.07.17`）。复测条件：5.4 beta 发布。
3. **SDK 主公告线未出现 R6/R7**。入口 `docs.../cubism-sdk-manual/top/`（`Updated: 09/29/2026`）。复测条件：主公告线出现新 `Notification … R6/R7`。
4. **GitHub org `Live2D` 无 10 月推送、无 R7 tag**。入口 `api.github.com/orgs/Live2D/repos?sort=pushed` + 5 仓库 `/releases`；最近推送仍 `2026-09-29`。复测条件：出现 10 月推送或 R7 tag。
5. **5.4 SDK alpha2 手册未命中**。`sdk-unity-alpha/.../alpha2/` → **404**（alpha1 → 200）。复测条件：该路径返回 200。
6. **HN 无料**。入口 `hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story`；命中 2167，**真 story 0**（全误召）。复测条件：出现标题含 "Live2D" 的非误召条目。
7. **dev.to 无新帖**。入口 `dev.to/api/articles?tag=live2d`；命中 2，最新 `2026-06-08`。复测条件：count>2 或最新日期 >2026-06-08。
8. **Reddit / note.com / medium.com / vroid.com 未命中**。入口各 URL → **000 / 000 / 000 / 403**（退役名单+WAF，本轮复测复现）。复测条件：返回 200。
9. **`creatorsforum` 10-02 后新增帖未命中「更多」**：`/latest.json` 30 条中，`last_posted_at > 2026-10-02` 者仅 `/t/3993`、`/t/3992`、`/t/3991`、`/t/3979`（末条回复）；前 3 已由他路/他辑掌握，**新增正文仅 /t/3991**（见 O1）。
10. **`community.live2d.com` 10-02 后新帖未命中**：`/api/v2/discussions?sort=-dateLastComment` 首条仍 `disc/2389`（`2026-10-06`，R35 已收），无更晚讨论。复测条件：出现 `disc/2390+`。

---

## §去重报告

**方法**：每条先 `grep -iF "<URL 片段>" _r37/_dedupe_urls.txt`；新增条目再对 `csdn-social-summary.md` 与 `index.html` 二次比对。

#### A. 命中基线 → 只记「有无变化」（复核条目）
`new-feature-introduction-title`（line 命中 1）· `cubism-5_4-alpha`（1）· `community.live2d.com`（2）· `inochi2d`（6）· `esotericsoftware`（1）· `store.live2d.com`/`student.live2d.com`/`cubism/update`/`docs` 各页 —— 均按「复核，未变」处理。

#### B. 0 命中 → 收录（新条目 / 新入口）
| 条目 | URL 片段 | dedupe_urls | csdn-summary | index.html |
|---|---|---|---|---|
| O1 `/t/3991` | `t/3991` | **0** | 0 | 0 |
| O2 `/t/3978` | `t/3978` | **0** | 0 | 0 |
| O3 `/t/3973` | `t/3973` | **0** | 0 | 0 |
| O4 `/t/3976` | `t/3976` | **0** | 0 | 0 |
| O5 `/t/3974` | `t/3974` | **0** | 0 | 0 |
| O6 `/t/3985` | `t/3985` | **0** | 0 | 0 |
| O7 `/t/1189` | `t/1189` | **0** | 0 | 0 |
| O8 `disc/2385` | `discussion/2385` | **0** | 0 | 0 |
| §二末 新入口 `updates-history/` | `updates-history/` | 0 | 0 | 0 |

> 已知帖 `/t/3983`、`/t/3979`、`/t/3986`、`/t/3989`、`/t/3975`、`community disc/2389/2386` → `csdn-social-summary.md` 各 **1 命中**（已被他辑收），本轮**不计新条**。

#### C. 本路条数
**复核条目 17 条（§二）+ 新增一手正文 8 条（O1–O8）+ 竞品动态 2 条 + 可达性复测 12 项**；其中 **O1/O2/O3/O4 为高价值官方一等一手**（两条新认领 bug + Unreal 支持确认 + alpha 可用期原始出处）。
