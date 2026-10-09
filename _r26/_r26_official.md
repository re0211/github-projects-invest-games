# 第二十六辑 · 官方与海外路（r26-official）· Live2D 制作专题

- 调研日期：2026-10-10
- 主题窗口：2025-01 ~ 2026-10-10（以 Live2D 官方 Cubism 5 周期为主）
- 检索范围：live2d.com / cubism.jp / docs.live2d.com / github.com/Live2D / note.com / Zenn / Qiita /
  Booth / Reddit / dev.to / Unity Forum / itch.io / AI×Live2D 产品官网
- 去重基线：`index.html`（脚注 [765] 已收 `live2d/cubismnativeframework`）、
  `csdn-social-summary.md`(v25) / `-v23.md` / `-v22.md`（三份 `Live2D` / `Cubism` grep 计数均 0）
- 纪律：每条带 URL + 出处 + 核实方式；版本/价格/日期/star 未核到即写「未核实」，不凭印象填空

---

## 正文（逐条追加）

### 1. Live2D 官网首页新闻时间轴：Cubism 5.4 alpha、5.3.00 正式版与 2026 春季促销都在上面
- 链接：https://www.live2d.com/en/
- 出处：Live2D Inc. 官网首页 · Live2D Inc. · 新闻条目日期见下（页面本身未标最后更新）
- 核实方式：`WebFetch https://www.live2d.com/en/`
- 一句话：首页轮播/新闻区把 Live2D 官方近期动作一次性列出来了 —— 我看到的关键条目依次是
  「Cubism 5.4 Alpha Release Announcement」（Product Info）、「2026 Spring Inspiration Sale（Cubism PRO 20% off，截止 2026-03-30 EST）」（Campaign）、
  「Cubism Editor 5.3.00 Official Release!」（Product Info，新闻列表标注日期 **2025.11.14**）、
  「Our website now supports Thai!」（2025.10.14）、「Live2D Game Jam Winners Announcement!」（2025.09.05 附近）、
  「12th Live2D Creative Awards 征稿」、「Cubism Editor 5.3 alpha version Pre-release」（2025.02.04）、
  「Cubism Editor 5.2.00 Official Release!」（2024.12.24）、「Cubism Editor 5.1.00 Official Release!」（2024.07.30 附近）。
- 可拓展性：这条是整个 Live2D 官方动态的「入口清单」，往下可以长出一整张「版本 → 日期 → 对应 SDK 版本」时间轴；
  也方便以后查「某次改价是否真有官方公告」。
- 实用性：**参考** —— 对学生站主不是直接能用的资源，但**它是本轮所有价格/版本断言的上游出处**；
  另外页面上明确写了「Powering **500+ commercial titles**」和 For Enterprise 入口（https://www.live2d.com/en/business/ ），
  这是判断「Live2D 到底是不是行业标准」的一手口径。

### 2. Cubism Editor 5.4 Alpha：官方发给所有人的**免费**尝鲜版，但明确禁止拿它做成品
- 链接：https://www.live2d.com/en/information/cubism-5_4-alpha/
- 出处：Live2D Inc. 官方公告 · Live2D Inc. · WebFetch 返回页面时间戳 **2026.07.14**
- 核实方式：`WebFetch https://www.live2d.com/en/information/cubism_5_4-alpha/`（注：URL 片段实际为 `cubism-5_4-alpha`）
- 一句话：这是把 Cubism 5.4 的新功能提前放出来给创作者试用的**限时评估版**，全部用户免费，不需要付费 license
  （FREE 版也能试用，但被限制在 Cubism 5.3 为止的既有功能里）。
- 可拓展性：本条的信息增量，全部来自该页。
  - **时间表**：alpha1 在 **2026-09-14** 后不可再用；随 alpha2 发布整体延长，alpha 版提供到 **2026-10-18** 为止。
  - **可以和正式版共存**：官方 FAQ 明确回答，Cubism 5 与 5.4 alpha 装同一台 PC 没问题，
    因为 editor 设置的缓存与自动备份文件夹是分开的。
  - **⚠️ 硬约束（最该记住的一条）**：官方明确回答「能不能把 5.4 alpha 做的模型拿去 VGen / nizima 卖？
    能不能发布用 SDK 5.4 alpha 做出来的应用？」→ **都不行**（"Please refrain from selling or distributing this product,
    as data compatibility cannot be guaranteed. Please use all materials solely for personal use."），
    理由是数据兼容性不保证。
  - **SDK 迁移不保证**：官方写明 Cubism SDK 不保证 alpha → beta → release 之间、以及反向的数据迁移。
  - 反馈渠道：官方 Creators Forum https://creatorsforum.live2d.com 与 X 标签 `#cubism54_alpha`。
  - alpha 版手册直链：Editor / 外部 APP 集成 / Cubism Core / SDK 四个 manual（页面内 li.manual5_4_alpha_02_en 等）。
  - 提到的新功能关键词：**Parameter Controller**（该页只有名字，具体形态未在此页展开）。
- 实用性：**落地**（作为「知道有这个 + 知道别踩坑」）—— 对学生做 Ren'Py 立绘的人，这条的价值是**反向的**：
  5.4 再香，**在这个阶段做出来的模型不能进你的游戏**（许可证不覆盖 + SDK 迁移不保证），
  正确做法是等 release 版。省的是重装/重做的时间。
- 去重证据：`grep -iF "5.4 alpha"` 与 `grep -iF "cubism54_alpha"` 在 index.html / v25 / v23 / v22 均 **0 命中**。

### 3. Cubism Editor 5.3.00 正式版发布公告（当前稳定主线）
- 链接：https://www.live2d.com/en/information/cubism-editor-5-3-00-official-release/
- 出处：Live2D Inc. 官方 Product Info · Live2D Inc. · **日期冲突，需要留证**
  —— 官网首页新闻列表给这条标的日期是 **2025.11.14**；该公告页 WebFetch 返回的时间戳是 **2026.01.20**。
  本轮未能从页面正文中取到发布日期原文（正文内容未完整返回），因此**不单方面断言**，两个数字一并记录。
- 核实方式：`WebFetch https://www.live2d.com/en/information/cubism-editor-5-3-00-official-release/`
- 一句话：5.3.00 是目前「正式存在且官网在推」的稳定版里程碑，它的前置节点是
  2025.02.04 的 5.3 alpha 先行版（同在首页时间轴上）。
- 可拓展性：下一步应该补这个：**把 5.3.00 的新功能清单和对应 SDK 版本要求核出来**（本轮 WebFetch 没取到正文，
  属未核实，不能凭印象写）。想看的话日文版入口是 https://www.live2d.com/cubism/update/ （官网更新履历页）。
- 实用性：**参考** —— 版本号本身对学生没用，但它是「我到底该装哪个版本」这个问题的**唯一官方答案**，
  避免照着网上三年前的教程装错版本。

### 4. ★ FREE 版 vs PRO 版功能对照表（官方，日文）——这条决定了「不花钱能做到哪一步」
- 链接：https://www.live2d.com/cubism/comparison/
- 出处：Live2D Inc. 官方对照页 · Live2D Inc. · 日期未标注（本轮取到的为日文版）
- 核实方式：`WebFetch https://www.live2d.com/cubism/comparison/`
- 一句话：官方把两版的每一处限制逐条列成表。**学生最该先看这张表再决定要不要买 PRO。**
- 可拓展性：实测逐条抄下来的限制，全部出自该页。
  - **质地数**：FREE 只能 **2048px 1 张**；PRO 无限制。
  - **ArtMesh 数**：FREE **100 以内**；PRO 无限制（PSD 层数 ≈ ArtMesh 数）。
  - **参数数**：FREE **30 以内**（含 blend shape 用参数）；PRO 无限制。
  - **Blend shape 参数**：FREE **3 以内**；PRO 无限制。
  - **Deformer 数**（warp + rotation 合计）：FREE **50 以内**；PRO 无限制。
  - **Parts 数**：FREE **30 以内**；PRO 无限制。
  - **ArtPath**（描线＋1）：FREE **3 条以内**；PRO 无限制。
  - **Warp deformer 分割数**：FREE **9×9**；PRO **100×100**。
  - **描画顺组**：FREE **2 个**；PRO 无限制。
  - **重复（repeat）次数**：FREE **2**；PRO 无限制。
  - **导出**：连续静止图 / GIF 动画 FREE 最大 **1280×720**；视频导出 FREE 最大 **1280×720 且「建议显示 logo」**，
    PRO 则到 **9.4 megapixels（macOS 上另有最大 4096×2304）**。
  - **带 AAC 音轨的视频导出**：FREE 版**音频会有哔哔声**且有限制；PRO 无限制。
  - 纯 PRO 才有的（FREE 完全没有）：形状的复制/粘贴/混合、**Solo 显示**、Multi-view、
    命令行「收集文件」、连番图片 track、ID/名称的 CSV 导出导入、网格自动生成的预设保存、默认形状锁定、
    旋转/warp deformer 连续创建、网格复制粘贴（做左右对称省事）、对象居中、快照当底图、模型缩放、
    把 deformer 应用到子对象、统一所选对象的参数结构、多关键帧只对 ArtMesh 生效的形态编辑、
    **乘算色/屏幕色**（FREE 完全没有；PRO 可以把颜色变化也做成关键帧）。
  - **兼容性**：PRO 做的数据可以在 FREE 打开，但用 FREE **保存**时必须改到限制以内才存得上。
- 实用性：**落地** —— 对学生做 Ren'Py 立绘，这张表直接告诉你：**一张正常画质的半身立绘你我肉眼觉得够用的情况下，
  最可能先撞到的墙是「参数 30 个上限」和「导出视频 1280×720 + 建议打 logo」**。
  而 30 个参数对「眨眼＋口形＋两个角度出发」这种入门需求是**够的** → **先用 FREE 验证流程，再决定买不买**。
- 去重证据：`grep -iF "comparison"` 在四份基线 0 命中；`grep -iF "ArtMesh"` → 0；`grep -iF "アートメッシュ"` → 0。

### 5. ★ Live2D Store 官方售价（本轮实测，含日元原价）
- 链接：https://store.live2d.com/en/
- 出处：Live2D Store（Live2D Inc. 官方商店） · 本轮 **2026-10-10** 实测取数（USD 数字随实时汇率浮动）
- 核实方式：`WebFetch https://store.live2d.com/en/`
- 一句话：**"Live2D Cubism PRO for indie"（限定：普通用户 / 小规模事业者，年营业额 1000 万日元未满）**四档价格实测如下：
  - **Annual Plan（可续订）**：第 1 年 **$90.20 USD［¥14,280］/年**；第 2 年 **$74.28 USD［¥11,760］/年**；
    第 3 年 **$67.46 USD［¥10,680］/年**（官方注明第 3 年的折扣适用于之后所有续订）。
  - **Monthly Plan（可续订，按月）**：**$13.14 USD［¥2,080］/月**。
  - **3-Year Plan（不可续订，一次性买三年）**：**$231.95 USD［¥36,720］/3年**（官方称已含 Annual Plan 的全部折扣）。
- 可拓展性：该页写明的规矩，别忘了。
  - Annual Plan **在订阅期内不能取消**；**不退款、不接受退货**。
  - 官方建议：**先装试用版确认能在你机器上跑**再下单（对 16GB 机器尤其对）。
  - 官方原话："Cubism **"for indie"** and **"for business"** do not differ in functionality." —— **两个版本功能完全一样，差别只在签给谁的（营业额门槛）**。
  - USD 数字是 currencylayer 实时汇率，会浮动；**日元才是原价基准**。→ 引用时请写日元，别写美元。
- 实用性：**落地** —— 这是本轮对学生的**第一决策依据**：最便宜的合法 path 是「月付 ¥2,080 / 约 $13」起步。
  但我没拿到 English Store 页上的 "for business" 与学生档（本页 guard fetch 时只返回了 indie 区块），
  那两档请见本文件下条 / 「授权与价格」节的专门核实。
- 去重证据：`grep -iF "store.live2d.com"` → 0；`grep -iF "36,720"` → 0；`grep -iF "14,280"` → 0。

### 6. ★ 学生折扣：2026 年从 76% OFF 提到 **80% OFF**，¥36,720 → ¥7,344（官方两处数字打架）
- 链接：https://student.live2d.com/en/student-discount/
- 出处：Live2D Inc. 官方学生折扣页 · Live2D Inc. · **活动截止 2027-03-31**
- 核实方式：`WebFetch https://student.live2d.com/en/student-discount/`
- 一句话：在校学生/教职员买「Cubism PRO for indie **3-Year Plan**」可以打到 **80% OFF**：
  原价 **$231 USD［¥36,720］/3yr** → 学生价 **$46 USD［¥7,344］**。
- 可拓展性：
  - 只有 **indie 3-Year Plan** 能用这个券；官方标的活动截止日为 "Offer ends March 31, 2027"。
  - 权益：功能和标准 PRO 版一致、**无功能限制**；**不会自动续订（一次性）**；3 年有效，**毕业后还能继续用**。
  - 官方文案给的理由很有意思："This 80% discount is our investment in the creators who will shape the **next 80 years** of this artform."
    → 指向 https://www.live2d.jp/20th-anniversary/en/student-discount.html （本轮未打开，待补）。
  - 申请要学生邮箱之类的在学证明；学校邮件域外的邮箱不接受；也接受 **ISIC**（国际学生证）。
- **⚠️ 本条最大的坑（也是本路最反直觉的事之一）**：同一个官方站上居然存在两个不同的折扣率 ——
  - **80% OFF（¥8,812→↯／实为 ¥36,720 → ¥7,344）**：来自上面这个专门的学生折扣页；
  - **76% OFF（¥36,720 → ¥8,812）**：来自 live2d.com **全站共通横幅**（在 https://www.live2d.com/en/sdk/license/ 、
    https://www.live2d.com/en/information/cubism-5_4-alpha/ 等众多页面上都是这一句
    "…receive a **76% OFF** coupon for a 3-year Live2D Cubism Editor PRO subscription."）。
  → **判断**：80% 是 2026 年新出的活动（挂在官方 student 子站 + 有明确截止日 2027-03-31），
  76% 是上一版文案，**全站横幅还没改干净**。**请以 student.live2d.com 的 80% 为准，但要留 URL 备查。**
- 实用性：**落地（优先级最高的一条）** —— 对学生，"三年 PRO 只要 ¥7,344（约 $46）" 和
  "月付 ¥2,080" 的经济画像完全反过来了：**如果你能拿到学生邮箱认证，直接上车最便宜**。
- 去重证据：`grep -iF "student-discount"` → 0；`grep -iF "7,344"` → 0；`grep -iF "80% OFF"` → 0。

### 7. Cubism SDK 全景：7 个分支 + MotionSync 插件，官方一句"免费下载"
- 链接：https://www.live2d.com/en/sdk/about/
- 出处：Live2D Inc. 官方 SDK 页 · Live2D Inc. · 日期未标注
- 核实方式：`WebFetch https://www.live2d.com/en/sdk/about/`
- 一句话：官方把 SDK 分成 **Unity / Native(C++) / Web / Java / Unreal Engine / Cocos Creator / Console（主机，仅注册开发者）**
  七支 + **MotionSync Plugin**（只有 Unity / Native / Web 有，Java 与 Cocos 没有）。
- 可拓展性：实测到的平台支持矩阵要点。
  - **for Unity**：Windows / macOS / Linux / Android / iOS / **WebGL** / **HarmonyOS NEXT** 全绿。
    注：HarmonyOS NEXT 需要中国版 Unity「团结引擎」，境外打包还需要「DevEco Studio」。
  - **for Native**：OpenGL 全平台；Metal 只有 iOS；DirectX 9.0c / 11 / Vulkan 只有 Windows；Cocos2d-x 有。
  - **for Web**：TypeScript 写的 Wasm/WebGL，**Safari 不支持 Windows/Linux/Android**（只支持 macOS + iOS）。
  - **for Java**：minSdk Android 5.0 (API 21)，targetSdk API 34（Android 14）；兼容 Kotlin。
  - **for Unreal**：**只有 Windows** 受支持（macOS/Android/iOS 都不是）。
  - **for Cocos Creator**：只支持 v3.7.0 以上，**v2 不支持**。
  - **for Console**：PS4 / PS5 / Nintendo Switch 都要注册开发者资格才能拿。
  - **⚠️ 最关键的一句（原文照抄）**："At Live2D Inc., we allow our users to download our SDK with **no initial cost**
    and start development right away. **It is only when the users are ready to publish their content**, they will need to
    enter into the **Publication License Agreement** and pay the applicable license fee.
    **Individuals and Small-Scale Enterprises are exempted from the license and payment (except Expandable Application).**"
- 实用性：**落地** —— 对学生来说这句话翻译过来就是：**写 Ren'Py / Godot / Unity demo 往 demo 里塞 Live2D 是完全免费、不需要通知 Live2D 的；
  钱的问题只在「你把它发出去卖」的那一刻才出现。**
- 去重证据：`grep -iF "sdk/about"` → 0；`grep -iF "MotionSync"` → 0；`grep -iF "HarmonyOS"` → 0。

### 8. ★ SDK Release License（官方名 Publication License Agreement）—— 到底什么时候要签、多少钱
- 链接：https://www.live2d.com/en/sdk/license/
- 出处：Live2D Inc. 官方 SDK 授权页 · Live2D Inc. · 日期未标注
- 核实方式：`WebFetch https://www.live2d.com/en/sdk/license/`
- 一句话：这是整个 Live2D 生态里**最重要的一页**，回答了「把 Live2D 塞进游戏要不要另签授权」这个问题。
- 可拓展性：本页核心结论，逐条。
  - **开发期不要钱、不要签字。发布前要。** 官方原话："License **only required upon releasing** your content. Not during trial or development."
    → 你可以先免费下载 SDK，做完整个 demo，确认能跑，再谈钱。
  - **时间要求**：官方写明「要求在 **发布至少一个月前** 完成授权手续」（License agreement must to be completed at least one month prior to the release.）。
    → **这是最容易迟到的一条**：不是上线当天补签，是**提前一个月**。
  - **谁免费**：**普通用户（个人/学生/社团，年营业额 < 1000 万日元）** 与 **小规模事业者（年营业额 < 1000 万日元）**
    **免除签约与费用** —— **但 Expandable Application（可扩展性应用）除外**。
  - **中型以上也有免费口子**："Medium or larger scale enterprises can also be exempt from the license agreement and fee
    if the usage is for **temporary and specific promotional purposes** pending a review from Live2D Inc."
    （见 https://www.live2d.com/en/business/slp/ ，本轮未打开）
  - **8 个 license plan 清单**（A~G + Others）：A 可扩展性应用 / B 非营利·非分发型 / C 持续royalty·视频 /
    D 非营利·分发型 / E 一次性买断内容·非主机非 PC / F 一次性买断内容·主机或 PC / G 持续royalty·游戏或应用 / Others（游艺机、活动、runtime 等）。
  - **VTuber 用他人追踪软件的那段原文**（页面上有一段加框声明）：若把该应用作为**事业主要元素**、
    且由该应用或用它产出的内容带来的**直接或间接年销售额超过 2000 万日元**，就必须签 PLA 并付费。
    → **2000 万日元是 VTuber 这条线的阈值**（注意它不是 1000 万的编辑版/SDK 版本阈值，别混）。
  - **做追踪软件给别人用 = Expandable Application**，必须审查 + 签专门的 PLA。
  - **BtoBtoX**（内容不是直接给终端用户、而是卖给其他公司）不算上面任何 plan，要单独联系。
- 实用性：**落地** —— 直接决定了本轮基准用户「能不能合法发行」：
  **一个 16GB Windows 学生，用自己的 Live2D 模型做 Ren'Py 视觉小说并在 Steam/iOS/Android 上发行**，
  只要内容是**买断制、固定一组模型** → 落到 **Plan E（一次性购买・非主机非 PC）**，
  而 Plan E 的普通用户/小规模事业者档是 **Free**（见第 10 条实测）。
- 去重证据：`grep -iF "Publication License"` → 0；`grep -iF "sdk/license"` → 0；`grep -iF "Expandable Application"` → 0。

### 9. ★ License Plan A「可扩展性应用」——个人和小规模也不豁免的唯一黑洞
- 链接：https://www.live2d.com/en/sdk/license/expandable/
- 出处：Live2D Inc. 官方授权计划页 · Live2D Inc. · 日期未标注
- 核实方式：`WebFetch https://www.live2d.com/en/sdk/license/expandable/`
- 一句话：**唯一连个人/小规模都不豁免的一种授权形态** —— 必须 **先过审查 + 再签专门的 PLA** 才能发。
- 可拓展性：
  - **定义（原文）**："Means any work having **significant expandability** among services or content utilizing SDK products."
    具体包括：通过添加或组合文件/数据来**生成或使用不定数量的模型**的派生作品（例：**avatar**）；
    一个标题里包含多个或其它作品、或能从这一个标题访问到那些作品（例：**相关作品的合集或 portal**）。
  - **审查条件（举例，官方原话）**：要有有效的变现模式（原则上**完全免费过不了审**）；
    同意提交销售报告与基于 revenue share 的付费；在出品的 EULA/条款里包含 Live2D 指定的声明（仅 streaming 类应用）；
    **展示 Live2D logo 并让我们把你的应用放进 Showcase**。
  - **费用表（general user / small-scale 全免）**：
    基本初期费用（不限发布地区）：个人/小规模 **免费**；中型 **$315.95［¥50,000］**；大型 **$1,895.70［¥300,000］**。
    基本年度费用（按平台计）：个人/小规模 **免费**；中型 **$1,516.56［¥240,000］**；大型 **$7,582.82［¥1,200,000］**。
    Revenue share：个人/小规模 **每售出一份 ¥300 或 销售额的 20%，取较高者**；中型/大型 **销售额的 5%**。
  - **"销售额"的定义**：派生作品的销售/使用产生的金额；经第三方或商店代收的，按**抽成和税之前**的金额算；
    **广告收入也算**。按季度提交报告。
  - **涨价/回溯条款**：营业额导致 business size 变化要在 **2 个月内**通知 Live2D，否则可被追溯到变更当月按新档补签。
- 实用性：**参考（但必须知道）** —— 对学生做单机 Ren'Py，大概率**不触发** Plan A（因为模型是固定一组、不能让用户加自己的）。
  但**一旦你想做「玩家可以导入自己的 Live2D 模型的立绘编辑器」「换装+换角色的通用 VN 引擎」**，就立刻变成 Plan A，
  **个人也不豁免**，而且要过审查。做功能规划时这条要提前知道，别做完才发现发行被卡。
- 去重证据：`grep -iF "expandable"` → 0；`grep -iF "revenue share"` → 0；`grep -iF "20% of Sales"` → 0。

### 10. ★ License Plan E「一次性买断内容·非主机非 PC」—— 学生发行独立游戏的落点，**实测为免费**
- 链接：https://www.live2d.com/en/sdk/license/purchase_plan02/
- 出处：Live2D Inc. 官方授权计划页 · Live2D Inc. · 日期未标注
- 核实方式：`WebFetch https://www.live2d.com/en/sdk/license/purchase_plan02/`
- 一句话：**这就是为什么独立学生作者能合法发 Live2D 游戏还不用给 Live2D 钱** —— Plan E 给普通用户和小规模事业者的价格是 **Free**。
- 可拓展性：该页实测。
  - 适用于「有一次性购买的收益模式、但不属于「主机或 PC 一次性购买的内容计划」的内容」。
  - **两种付款方式二选一，签完合同不能改**：
    - **Option (1) 一次性费用**：普通用户 / 小规模 **免费**；中型 **$631.66［¥100,000］**；大型 **$3,789.98［¥600,000］**。
    - **Option (2) 按出货量**：每生产一份 **¥40（$0.25）** —— 但普通用户/小规模这栏同样是 **Free**，只有中型/大型要出。
      可下载的内容：开卖时先按 **1000 份**开票，之后每多卖 1000 份再开票。
    - 两种都按**所有平台的合计**算；但若内容在主机或 PC 上发行，就转到 Plan F。
  - **「折扣价的前提」**：上述价格都是**同意在内容里显示 Live2D logo、并把作品登上 Live2D 的 Showcase 页面**
    之后的价格（指到 https://www.live2d.com/en/sdk/guidelines/ ）。
  - **规模升级规则**：营业额导致规模变动要在 **2 个月内**通知 Live2D；同一地区多家发行商各自要签各自付费。
- 实用性：**落地（本轮对学生最有利的一条）** —— 直接把「要不要给 Live2D 付钱」的问题答完了：
  **个人 / 小规模，买断制发行 → ¥0。** 需要注意的代价是「必须打 Live2D 的 logo + 提供 Showcase 素材」。
- 去重证据：`grep -iF "purchase_plan02"` → 0；`grep -iF "¥40"` → 0；`grep -iF "100,000"` → 0。

### 11. License Plan G「持续 royalty・游戏/应用」—— 抽卡 / 内购 / 广告变现的游戏走这条
- 链接：https://www.live2d.com/en/sdk/license/running_plan01/
- 出处：Live2D Inc. 官方授权计划页 · Live2D Inc. · 日期未标注
- 核实方式：`WebFetch https://www.live2d.com/en/sdk/license/running_plan01/`
- 一句话：适用于「终端用户直接使用 SDK 内容、且有**持续性收入模型**（订阅、内购、广告等）」的游戏/应用。
- 可拓展性：该页实测。
  - **6 个发布地区**：日本 / 中国大陆·香港·澳门·台湾 / 亚洲（除日本、中国、台湾）/ 北美 / 欧洲 / 其他。
  - **4 个平台**：iOS / Android / **Harmony OS** / Web（Web = 在网页上运行、用户用自己的浏览器就能用的内容）。
  - **费用表**：基本初期费用（**按发布地区数**计）：个人/小规模 **免费**；中型 **$315.85［¥50,000］**；大型 **$1,895.11［¥300,000］**。
    基本月费（**按平台数 × 发布地区数**计）：个人/小规模 **免费**；中型 **$126.34［¥20,000］**；大型 **$631.70［¥100,000］**。
  - 计价公式：初期费合计 = 基本初期费 × 地区数；月费合计 = 基本月费 × 平台数 × 地区数。
  - 初始费用和发布当月的月费**都按月计费整月份 ozong不管几号上线**。
  - 折扣价的前提同样是「显示 Live2D logo + 进 Showcase」。
- 实用性：**参考** —— 对学生做单机买断 VN 通常不触发；但只要你的 VN 里**加了广告位或内购解锁服装**，
  就从 Plan E 滑到 Plan G —— 好在 **个人/小规模这档依然是 Free**，只是**变成了「性质不同」的单位**，
  稀缺性来自要不要承认自己有 recurring revenue。**知道自己落在哪个 plan，比知道价格重要。**
- 去重证据：`grep -iF "running_plan01"` → 0；`grep -iF "Harmony OS"` → 0。

### 12. Live2D 商标与 Showcase 指南 —— 「免费」的真实代价是这三件事
- 链接：https://www.live2d.com/en/sdk/guidelines/
- 出处：Live2D Inc. 官方 guidelines 页 · Live2D Inc. · 日期未标注
- 核实方式：`WebFetch https://www.live2d.com/en/sdk/guidelines/`
- 一句话：页面上那句关键的话是 —— **官网展示的 PLA 价格，都是「配合显示 Live2D logo + 收录进 Showcase」之后的折扣价**。
  换句话说，**"免费"不是无条件免费**。
- 可拓展性：四项 Mandatory，逐条。
  1. **在内容里显示 Live2D logo**：启动画面 / 起始画面，**一处即可**；splash 至少要显示 **1 秒**（不含淡入淡出，可跳过）；
     可全屏、窗口内或与别的 logo 并列。官方提供多种配色的 logo 素材下载。
  2. **在各发行平台的商品页写上「Live2D」字样**（Apple store / Google Play 的介绍页），格式不限，
     官方示例："Powered by Live2D" / "This application was made using Live2D from Live2D Inc."。
  3. **提交进 Live2D Database**（官方维护的「采用 Live2D 的商业作品 + 参与创作者」数据库），需要给作品与制作信息。
  4. **填一份改进问卷**，由实际用 SDK 的负责人填写。
  - Voluntary：在 credits 里再标一次 logo/名字（可选，格式不限）。
  - **成人内容的例外**：作者ship, only #2 and #4 apply —— **#1（显示 logo）和 #3（进 Database）都免去**。
- 实用性：**落地** —— 对你的 Ren'Py 游戏，这意味着：一个启动 logo 画面 + 商店页一句话 + 交一次资料 + 一份问卷。
  这是「免费路径」的真实成本，**很便宜但不是零**，而且**必须提前 1 个月启动**（回到第 8 条）。
- 去重证据：`grep -iF "sdk/guidelines"` → 0；`grep -iF "Powered by Live2D"` → 0。

### 13. ★ 网上到处引用的 `CubismSdkForUnity` 已经 404 —— Live2D 官方 GitHub 仓库名全改过
- 链接：https://github.com/Live2D
- 出处：GitHub · Live2D Inc. 官方组织 · 本轮 **2026-10-10** 实测
- 核实方式：`gh api "orgs/Live2D/repos?per_page=100&sort=pushed"` +
  `gh api "repos/Live2D/CubismSdkForUnity"` 等逐个探测
- 一句话：**`github.com/Live2D/CubismSdkForUnity`、`CubismSdkForWeb`、`CubismSdk4`、`CubismSDKForJava`
  全部返回 404（Not Found）。** 现存的是**部件粒度**的仓库。
- 可拓展性：全部为本轮 `gh api` 实测，**star / 最后推送日期均为当场拉到的值**。

  | 仓库 | star | 最后推送 |
  |---|---|---|
  | `Live2D/CubismWebSamples` | **392** | 2026-04-02 |
  | `Live2D/CubismUnityComponents` | **263** | 2026-09-29 |
  | `Live2D/CubismNativeFramework` | **264** | 2026-06-26 |
  | `Live2D/CubismWebFramework` | **237** | 2026-04-02 |
  | `Live2D/CubismNativeSamples` | **239** | 2026-04-02 |
  | `Live2D/CubismUnrealEngineComponents` | **32** | 2026-09-29 |
  | `Live2D/CubismJavaSamples` | **31** | 2026-06-04 |
  | `Live2D/CubismSpecs` | **22** | 2026-08-05 |
  | `Live2D/CubismJavaFramework` | **16** | 2026-06-04 |
  | `Live2D/CubismWebMotionSyncComponents` | **11** | 2025-03-27 |
  | `Live2D/CubismCocosCreatorComponents` | **8** | 2023-09-28 |
  | `Live2D/CubismNativeMotionSyncComponents` | **5** | 2026-08-25 |
  | `Live2D/CubismUnityMotionSyncComponents` | **3** | 2026-08-25 |
  | `Live2D/CubismViewer` | **46** | 2018-04-20 |

  - 许可证字段几乎全是 **NOASSERTION**（GitHub 识别不出标准许可证），**这不是「随意用」的意思**，
    实际受 https://www.live2d.com/eula/live2d-proprietary-software-license-agreement_en.html 约束。
  - **Cubism Core 不在 GitHub 上**：官方文档明确写「Cubism Core is not published on GitHub」，
    必须下载 SDK 分发包才有。→ 意味着 **clone 仓库并不能构建出能跑的东西**，必须去官网 download。
- 实用性：**落地（省时间的一条）** —— 网上的 Live2D 教程/博客（含 2024–2025 年的）大量写着
  `git clone https://github.com/Live2D/CubismSdkForUnity`，**这些链接现在是死的**。照抄只会 404。
  正确入口是上面这张表 + 官网 https://www.live2d.com/en/download/cubism-sdk/ 。
- 去重证据：本索引已收 `live2d/cubismnativeframework`（脚注 [765]，档案记 262 star / 2026-06-26 /
  NOASSERTION，与本次实测 **264** 一致，仅 star 微增 → **判为同一仓库，不重复收录**）。
  其余 13 个仓库在 index.html / v25 / v23 / v22 的 grep 结果均为 **0**，属新收。

### 14. Cubism 5 SDK 各分支的真实发布节奏（GitHub Releases 实测）
- 链接：https://github.com/Live2D/CubismUnityComponents/releases
- 出处：GitHub Releases · Live2D Inc. · 本轮 **2026-10-10** 实测
- 核实方式：`gh api "repos/Live2D/<repo>/releases?per_page=10"` 跑了 Unity / Web / Native / Java / Unreal 五个仓库
- 一句话：**最新的正式版本号是 R5（统一在 2026 年春上线），Unreal 分支还停在 beta。**
- 可拓展性：实测到的 tag + 日期。
  - **for Unity**：`5-r.5` = **2026-04-02**；`5-r.4.2` = **2026-05-14**（在 R5 之后补的补丁线）；
    `5-r.5-beta.3` = 2026-01-08；`beta.2` = 2025-10-14；`beta.1` = 2025-08-26；`5-r.4.1` = 2025-07-17。
  - **for Web** / **for Native**：`5-r.5` 同为 **2026-04-02**；各自有 `5-r.5-beta.3.1` = 2026-02-19。
  - **for Java**：`5-r.5` = **2026-06-04**（比其他三个晚两个月）。
  - **for Unreal Engine**：最新是 `5-r.1-beta.2` = **2026-09-29**，前面 `beta.1` = 2025-05-29，
    再往前全是 alpha1~alpha5（2024-09 ~ 2025-01）。→ **Unreal 这条线一直没进正式版**。
  - **Unity R5 的 CHANGELOG 实测要点**（`5-r.5 - 2026-04-02` 段）：新增 ARM64 iOS Simulator 用的 Cubism Core；
    开发 Unity 版本升到 **6000.0.68f1**；改用 Input System 包；**修了 URP 下 Scene View 里点不中 / 不描边的 bug**；
    修了 Reversed Z 环境下 offscreen 渲染的问题；改了乘算色/屏幕色的属性名（**这是破坏性改名，见第 15 条**）；
    Importer 的处理顺序改成先读 motion3.json、再读 model3.json。
- 实用性：**参考** —— 对 Unity 用户，R5 是「换 URP + 一堆改名的坑」，不是无痛升级；
  对其他人，这张表的作用是在**提 issue / 搜答案前先知道自己用的到底是 R几点**。
- 去重证据：`grep -iF "5-r.5"` → 0；`grep -iF "6000.0.68f1"` → 0；`grep -iF "CubismUnityComponents"` → 0。

### 15. ★ 《与 Cubism 5 SDK R5 正式版的兼容性》官方专页 —— R5 是一次带破坏性改名的升级
- 链接：https://docs.live2d.com/en/cubism-sdk-manual/compatibility-with-cubism-5-3-official
- 出处：Live2D Inc. 官方 SDK 手册 · Live2D Inc. · R5 上线日 **2026-04-02**
- 核实方式：`WebSearch`（官方文档站全文被收录，内容逐条核对）
- 一句话：官方专门写了一页讲「从 R5 beta 升到 R5 正式版要改什么」。**有 API 改名，照抄旧代码编译不过。**
- 可拓展性：本页要点。
  - 两个破坏点：① **模型计算顺序的重排列功能**（for Unity 的执行顺序改成与 Native/Web 的 Original Workflow 一致，
    结果是**物理相关的参数更新结果和 R5 beta 不一样**）；② **乘算色/屏幕色的类结构 + API 改名**。
  - **Unity 端改名举例**：`CubismRenderController.OverrideFlagForModelMultiplyColors` → `MultiplyColorEnabled`；
    `CubismPartColorsEditor.OverrideColorForPartMultiplyColors` → `PartMultiplyColorEnabled`；
    `CubismRenderer.OverrideFlagForDrawObjectMultiplyColors` → `DrawObjectMultiplyColorEnabled`。
  - **Native/Web 端**：相关函数从 `CubismModel` 类迁到新的 `CubismModelMultiplyAndScreenColor` 类，
    例如 `SetMultiplyColor()` → `SetDrawableMultiplyColor()`、`SetOverrideFlagForPartMultiplyColors()` → `SetPartMultiplyColorEnabled()`。
  - **回滚办法**：想要 R5 beta 的旧计算顺序，官方给了具体操作 —— 去 GitHub 找 R5 beta3 或更早的
    `Assets/Live2D/Cubism/Framework/CubismUpdateExecutionOrder.cs`，把常量抄回来替换。
  - 官方 SDK 手册更新历史里，同一天（**2026-04-02**）一口气更新了 Native / Web / Unity 三个分支的乘算色章节。
- 实用性：**参考** —— 对学生，重点是**别在升级前不知道会炸**。
  如果你（或你抄的插件）用了 multiply/screen color 的 API，**升级到 R5 必须改代码**，且它给了明确回滚方法。
- 去重证据：`grep -iF "MultiplyColorEnabled"` → 0；`grep -iF "Compatibility with the Cubism 5 SDK"` → 0。

### 16. ★ Ren'Py 官方 Live2D 支持 —— 基准用户最直接的一条动手路径
- 链接：https://www.renpy.org/doc/html/live2d.html
- 出处：Ren'Py 官方文档 · Ren'Py (Tom Rothamel / 官方) · 页面日期未标注
- 核实方式：`WebFetch https://www.renpy.org/doc/html/live2d.html`
- 一句话：**Ren'Py 原生支持 Live2D Cubism 3 / 4 / 5 三种格式**，能播 motions 和 expressions，
  底层是把参数传给 **Cubism SDK for Native**，拿回 mesh 列表再渲染。
- 可拓展性：文档里逐条可用的东西。
  - **安装**：官网下载 Cubism SDK for Native，把 **`CubismSdkForNative-5-r.1.zip`** 放进 Ren'Py 的 SDK 目录
    （启动器右下角按钮可打开该目录），然后 启动器 → preferences → **Install libraries** → **Install Live2D Cubism SDK for Native**。
  - **⚠️ 注意版本号**：文档里指定的是 **5-r.1**，而当前 Native 最新是 **5-r.5（2026-04-02）**
    → 这个 zip 文件名大概率已经过期，实操时很可能要变通。这一点我没有实测，**标为「未核实」**。
  - **iOS 需要手工把静态库拷进 iOS 工程**；必须开启基于模型的渲染器（GL2）否则用不了。
  - **写法**：`image hiyori = Live2D("Resources/Hiyori", base=.6)`，`show natori exp_00 mtn_01` 直接当属性播。
  - **表情/动作命名规则**：名字从 Live2D 文件读出来、**强制小写**，且若以 model3.json 名 + 下划线开头则前缀被去掉
    （文档原文举例：`Hiyori_Motion01` → `motion01`）。
  - **两个特殊属性**：`null`（不套用任何 exclusive 表情，用默认脸）+ `still`（停动作）。
  - **降级写法（文档给的样板，强烈建议抄）**：`renpy.has_live2d()` 判 False 时返回 `Placeholder(text="no live2d")`，
    否则 `Live2D(...)`。**因为硬件不支持时，一次 `Live2D()` 会让整个项目加载失败**，
    而且 **web 版发行也不支持** → 所以这个 fallback 对「想在 itch.io 网页版放 demo」的人是刚需。
  - **官方文档自己提到了授权**：原文 "you may need to purchase a license to use Live2D if your business makes
    more than a certain amount of money a year" → 与第 8/10 条的官方口径互相印证。
- 实用性：**落地（本轮的 TOP 1）** —— 对「16GB Windows 学生做 Ren'Py 视觉小说」这个画像，
  这条就是**唯一需要照着做的实现路径**：官方原生支持、有稳定 API、有 fallback 写法。
  配合第 10 条（Plan E 个人免费）→ **合法、够用、不用给 Live2D 钱**。
- 去重证据：`grep -iF "renpy.org/doc/html/live2d"` → 0；`grep -iF "CubismSdkForNative"` → 0；`grep -iF "has_live2d"` → 0。
  补充说明：CC-BY 中文镜像 http://doc.renpy.cn/zh-CN/live2d.html 内容一致，本条以官方英文站为准。

### 17. Godot 唯一的非官方 Live2D 路线 `gd_cubism` —— 能用，但已经停更
- 链接：https://github.com/MizunagiKB/gd_cubism
- 出处：GitHub · MizunagiKB（个人开发者）· 本轮 **2026-10-10** 实测
- 核实方式：`gh api "repos/MizunagiKB/gd_cubism"` + `gh api "repos/MizunagiKB/gd_cubism/releases?per_page=5"`
- 一句话：Godot **没有**官方 Live2D 支持，`gd_cubism` 是社区事实标准 —— 号称 "Unofficial Live2D Player for Godot Engine"。
- 可拓展性：实测数据 + 中文实践文共同印证。
  - 实测：**301 star / 47 fork / license = NOASSERTION / 最后 push = 2025-04-01**。
  - 实测最新 release：**v0.9.1（2025-03-27）**，往前 v0.9.0（2025-03-25）、v0.8.2-godot4.1（2025-03-08）、v0.8.2（2025-03-04）。
  - **⚠️ 停更风险（本条重点）**：最后一次提交是 **2025-04**，而官方 SDK 在 **2026-04-02** 出了 R5。
    即 **gd_cubism 停在 R4 时代** → 想用 R5 要么等上游、要么自己接。
  - 版本兼容性坑（CSDN 实践文实测）：**v0.9+ 只支持 Godot 4.3 及以上**；Godot 4.1/4.2 要用 `v0.8.2-godot4.1`
    这个特定 tag，用错版本会在编辑器里直接报加载失败。
  - 它走的是 **GDExtension 包一层官方 Cubism Native Framework**（不是纯 GDScript 重实现），
    所以性能和功能完整性都比「GDScript 逆向解析器」那条路好得多。
- 实用性：**参考（有明确前提）** —— 我们的基准用户是 Ren'Py，**不需要这个**；
  但如果你以后想把 VN 换到 Godot，这条是「Godot 能不能做 Live2D」的答案：**能做，但你在用一个停更两年的绑定**。
- 去重证据：`grep -iF "gd_cubism"` → 0；`grep -iF "MizunagiKB"` → 0。

### 18. nizima LIVE：Live2D 官方自己的免费面捕软件（¥0 起步）
- 链接：https://nizimalive.com/en/
- 出处：Live2D Inc. 官方产品站 · Live2D Inc. · 最新版公告日期 **2026-08-12（2.7 大更新）**
- 核实方式：`WebFetch https://nizimalive.com/en/`
- 一句话：这是 **Live2D Inc. 自己做**的面捕/直播应用，有**真·¥0 的免费 plan**，
  不用 VTube Studio 也能让你的模型动起来。
- 可拓展性：本页实测。
  - **三档价格**：Free plan **¥0**；**for indie**（普通用户 / 小规模，年营业额 ≤ 1000 万日元）**¥550/月（约 $3.47）**；
    **for business**（中型以上）**¥3,300/月（约 $20.84）**。两档付费都是**年缴 8 折**。
  - 三个还在维护的证据：2.7 大更新 **2026-08-12**、2.6 大更新 **2026-03-31**、还有一条 2026-08-21 的维护公告。
  - 功能点：可用 iPhone app「nizima LIVE TRACKER」当摄像头做到比 webcam 更准；
    支持 **Perfect Sync**（鼓脸颊、左右动嘴这种高阶表情）；自带 **100 个以上**预设 item；
    **协作直播最多 8 人同屏**（房间里只要有一个付费用户，免费用户就不受时长限制）。
  - 需要注册一个 **nizima 账户（免费）**才能用。
- 实用性：**落地** —— 对学生做 VN，面捕软件本身**不是必需的**（VN 靠参数驱动，不靠摄像头）。
  但这条的价值是：**它是验证「你的模型 rig 得好不好」最快的免费工具** ——
  做完模型扔进 nizima LIVE，对着摄像头动一动，瑕疵立刻看得见。
- 去重证据：`grep -iF "nizimalive"` → 0；`grep -iF "nizima LIVE"` → 0；`grep -iF "Perfect Sync"` → 0。

### 19. Live2D 官方的免费学习资源：教程站 / 范例模型 / JUKU / LEAP 教育计划
- 链接：https://docs.live2d.com/cubism-editor-tutorials/top/ （教程站）·
  https://docs.live2d.com/cubism-editor-manual/top/ （手册）·
  https://student.live2d.com/en/education-aid-program/ （LEAP，教育机构免费借用 PRO）
- 出处：Live2D Inc. 官方 · Live2D Inc. · 教程站标注「最終更新: 2026年1月20日」
- 核实方式：`WebSearch`（官方 docs 站全文被收录）+ 首页属实
- 一句话：**官方把「完全免费就能学」的入口做得相当全**，包括视频教程分级（入门：10 分钟看懂「眨眼」/ 20 分钟看懂基础操作 / 6 讲基础课）、
  6 讲「嵌入用教程」（讲怎么把模型塞进游戏或应用），以及感知器 AK/参数控制器相关的新章节。
- 可拓展性：
  - 教程站更新记录里有 **[2026/01/20]「使用混合模式和离屏绘制增强表现力」新页面公开** —— 对应 Cubism 5.3 的新功能。
  - **范例模型很重要**：官方提供可下载的样例模型（含 Hiyori / Haru 等），
    第三方整理指出这些样例模型被分成**不同授权等级**（有的是 Free Material License 可商用，
    有的联动角色不能商用、不能改），**并且要求保留版权声明**。
    → 想拿官方样例往自己的 VN 里塞的话，**必须先看样例自带的授权文件**，不要默认「官方 = 免费用」。
  - **LEAP**：教育机构可**免费借用** Cubism Editor PRO license，官方称已支持超过 **200 所学校**。
  - Live2D JUKU 是付费在线课程（非本轮重点，未核实价格）。
- 实用性：**落地** —— 免费 + 官方 + 有中文版（docs.live2d.com/zh-CHS/）。这是学生站主应该**从这里开始**的地方。
- 去重证据：`grep -iF "LEAP"` → 0；`grep -iF "JUKU"` → 0；`grep -iF "cubism-editor-tutorials"` → 0。

### 20. Booth（pixiv 旗下日本创作者市场）：Live2D 工程文件与素材的真实价格带
- 链接：https://booth.pm/zh-tw/items/4709134 （示例：`0x4682B4's Shop`）
- 出处：BOOTH / pixiv · 第三方创作者 0x4682B4 · 本轮通过 `WebSearch` 取到的商品页内容
- 核实方式：`WebSearch "Booth.pm Live2D プラグイン 素材 Cubism 販売"`
- 一句话：Booth 是日本 Live2D 生态里**买现成工程文件/模板**的地方，价格从几百到几千日元，
  比「定制角色（搜索引擎到的市场价 ¥500 起）」便宜得多。
- 可拓展性：示例店铺的实测价格带。模板类 **¥2,200**；chibi 模型底座 **¥2,800~¥7,100**；
  成品模型 **¥1,500~¥5,600**；item 小物件 **¥500**；教学例子（眼睛物理）**¥2,400**。
  → **几百日元就能买到「别人做了一半的工程」**，这是「花钱买时间」的最低价入口。
- **⚠️ 授权比价格更要紧**：同一个示例商品页的 TERM OF USE 写着 ——
  ❌ 不得转售/再分发工程与源文件、**不得把参数设置或工程结构公开**、不得声称自己是作者、
  **不得用于 NFT / 加密货币 / AI 生成艺术相关活动**；
  ✔️ 可以用于学习/研究、可以在自己的工程里用它的参数设置。
  → **「能不能改」「能不能进自己的商业游戏」由每个商品页各自规定**，没有统一答案，必须逐条读。
- 实用性：**落地（但要看清楚条款）** —— 对学生做 Ren'Py VN，花 ¥2,000 左右买个**含 cmo3 工程的结构范例**
  比看 20 小时视频更快。**但如果你想用 AI 图生成角色，上面那条「禁止 AI 生成艺术」可能直接否掉你的用法。**
- 去重证据：`grep -iF "booth.pm"` → 0；`grep -iF "0x4682B4"` → 0。

### 21. 日本侧初学者实录（note.com）：一位上班族从零学 Live2D 的血泪踩坑
- 链接：https://note.com/rosaria_v_score/n/n75e2690ba874
- 出处：note.com · 个人创作者 rosaria（日文）· 日期未核实（页面 direct fetch 失败，内容取自检索摘要）
- 核实方式：`WebSearch`（note.com 全文被收录）+ 直接 WebFetch **失败已记录**
- 一句话：一篇日文手写实录，讲一个没有美术背景的成年人怎么一步步做出自己的 Live2D 模型。
- 可拓展性：本用的三条教训。
  - **⚠️ 图层模式踩坑**：作者用 iPad 版 Clip Studio + Apple Pencil 画画，**大量使用「乘算（multiply）图层」画阴影**，
    结果**图层数超过 100 后性能急剧下降并开始报警**；改成普通图层能解决但**颜色会变，修色修了很久**。
    → **这是做得最多的 pipeline 级坑：绘制阶段就要决定图层合成模式。**
  - **教程不要挑「可动范围大」的**：标着「高可动范围」的视频是给进阶者看的，parts（=图层）数量会很恐怖，容易劝退。
    作者的建议是**不要一上来追求完美，先歪着做完一遍**。
  - **学习顺序**：先用第三方（Deep Blizzard 三部曲）做出**会动的东西**获得信心 →
    再用官方 Live2D JUKU 视频回来**整理 deformer 的层级结构**。作者说整理完数据后「模型不再莫名其妙坏掉」。
  - 另提到 Cubism **有 42 天 PRO 免费试用**，但作者提醒「不要指望免费版能拿来做 Live2D 正事」。
- 实用性：**落地** —— 这条的价值是**预期管理**：告诉你「做完一遍再打磨」比「一遍做好」更可行，
  以及最贵的成本不是软件钱而是**画 PSD 时的图层规划**。
- 去重证据：`grep -iF "note.com"` → 0；`grep -iF "rosaria"` → 0。

### 22. Cubism Editor 的系统需求与 42 天 PRO 试用（第三方下载站佐证）
- 链接：https://www.softpedia.com/get/Multimedia/Graphic/Graphic-Editors/Live2D-Cubism.shtml
- 出处：Softpedia（第三方下载站，非官方）· Softpedia 编辑团队 · 页标注 **Updated: Jul 14, 2026**
- 核实方式：`WebSearch`（Softpedia 页面被收录；**本轮未直接 WebFetch 该页，间接核实**）
- 一句话：一个第三方下载站给出的版本与硬件需求，可作为「官方没明确写」时的旁证 ——
  但**价格类信息一律不要采信这类站点**。
- 可拓展性：该页给出的信息。
  - **版本号**：Latest version **5.3.03 / 5.4 Alpha**（5.3.x 系列里还有个小版本 .03，官方首页只强调 5.3.00）。
  - **未注册版的限制**：**42 天 PRO 试用**；之后落到功能受限版（texture 数 / artmesh 数 / motion 参数数等限制）。
  - **系统需求**：Intel Core i5 以上（推荐 i7）、**内存 4GB 以上（推荐 8GB）**、约 400MB 硬盘、
    **OpenGL 3.3 以上**、屏幕 1440×900 以上（推荐 1920×1080）、需要联网。
  - 5.4 Alpha 的变更举例：修了 `csmGetParameterValues` 的返回类型，补了参数控制相关描述。
- 实用性：**参考（但带标签）** —— 对「16GB Windows 学生」这条直接回答了：**你的机器绰绰有余**
  （官方推荐才 8GB）。版本号 5.3.03 这个数字**建议下次去官网再核一次**，本条仅为旁证。
- 去重证据：`grep -iF "softpedia"` → 0；`grep -iF "5.3.03"` → 0。

### 23. ★ Bunraku（arXiv 2607.27348）：第一个「一张图 → 完整可编辑 Live2D  rig」的系统
- 链接：https://pith.science/paper/2607.27348 （含 AI 审稿 ；原始论文编号 **arXiv 2607.27348**）
- 出处：arXiv 预印本 2607.27348 · Junhao Chen、Jingjia Mao、Dayong Li 等 · AI 审稿读论文日期 **2026-08-01**
- 核实方式：`WebFetch https://pith.science/paper/2607.27348`
- 一句话：**目前最接近「AI 全自动做 Live2D」的工作**：输入一张插图，输出有层序的 RGBA 图层 +
  每层网格 + 关键姿势顶点位移，即一个完整可编辑、可驱动的 Live2D 资源。
- 可拓展性：
  - **两阶段**：Stage 1 用「Live2D 感知的 8 类 / 32 子类器官分类法」做**分层扩散**，输出带遮挡补全的 RGBA 层叠；
    Stage 2 把**每个网格顶点当成一个 token**、所有层的顶点拼成一个序列做**跨层 unmasked self-attention**，
    一次性回归所有层的 keypose 位移。位移被分解成「有界方向（tanh）+ log 幅值」以适应 Live2D 的重尾分布。
  - **核心实验结论**：**跨层联合预测才是最大收益（0.736 vs 0.693）**，单独把模型放大 **112 倍是没用的**（明确的负结果）；
    在 50 个留出角色上做到 per-vertex direction cosine **0.7676（中位数 0.8278）**。
  - **顺手放出来的东西**：**Live2D-Bench**（首个该任务的标准 benchmark）+
    **8,884 个带图层与动画监督的 Live2D 模型语料库**。
  - **⚠️ 踩坑/质疑（最值得看的部分）**：审稿指出**头条分数是在「画师手作网格」上测的**，
    而实际部署用的是 Stage 1 生成的 alpha 推导自动网格 —— **论文从没在全流水线上报这个指标**，
    只给了 3 个角色的渲染 PSNR。而**该指标对网格密度敏感**：自动网格更密（约 83 顶点/层 vs 47.5），
    单纯重新网格化就要掉 0.063 cosine → **端到端的真实分数可能远低于 0.7676，0.7676 更像上界**。
  - 论文自陈的局限：**不产出 .moc3**、只做线性插值、长尾参数会失效。
- 实用性：**参考** —— 目前**不能直接拿来插入你的 Ren'Py**（不出 .moc3），别被标题骗。
  但 **Live2D-Bench + 8,884 模型语料**是至今为止做这个方向最有价值的公开资产，值得进索引的「数据集」侧。
- 去重证据：`grep -iF "2607.27348"` → 0；`grep -iF "Bunraku"` → 0；`grep -iF "Live2D-Bench"` → 0。

### 24. ★ return.moe：非动画背景的人，一天内拼出全自动 Live2D 流水线 —— 以及「Live2D 会死」的预言
- 链接：https://blog.return.moe/en/2026/07/19/towards-fully-automated-live2d-style-animation
- 出处：个人博客 blog.return.moe · **Rodrigo Laneth（@rlaneth）** · **2026-07-19**
- 核实方式：`WebFetch https://blog.return.moe/en/2026/07/19/towards-fully-automated-live2d-style-animation`
- 一句话：一个完全没学过动画/绘画的人，用现成 AI 工具**在一天之内**拼出了「画画 → 分层 → rig → 自写引擎渲染」的全链路，
  并且给出了一个很凶的产业判断。
- 可拓展性：本文最有价值的是**流程与失败点**。
  - **流程五步**：① ChatGPT Images 2.0 生成底图 → ② **人工修图**（原生成里手上的包被裁掉了，做动画不能用）
    + 用 WAI-Illustrious-SDXL 系模型跑几轮 diffusion 让风格统一 → ③ 用 **See-through** 切成分层 PSD →
    ④ **再人工细修 PSD**（把模型合并在一起的部件拆开，比如两只手臂，并重排图层）→
    ⑤ 让 **GPT-5.6 Sol Ultra 从头写一个 OpenGL 引擎**，用文字反复迭代到满意。
  - **失败/局限（原文承认）**：作者自述标题刻意用了 "towards"，**流水线还不是全自动**，
    上面第 ②④ 两处人工介入**现在仍必需**。
  - **一个已验证的失败点**：作者早先試圖用 Claude Desktop 直接操纵 Live2D 软件界面，结果不好 ——
    他的结论是 **"LLMs struggle to drive complex GUI through screenshots"（让 LLM 靠截图驱动复杂 GUI 很难）**。
  - **作者的产业判断（争议点）**："Live2D itself … might effectively **die as a product**. …
    The engine itself is no longer a business moat: anyone can produce one with modern LLMs." ——
    它认为 Live2D 剩下的护城河是**集成生态**（VTube Studio、游戏引擎、直播工作流），不是技术。
  - 作者给社区的建议是**做标准化**（通用格式 + 参考实现 + 让 LLM 能照规范 rig 的 skills/connector），
    否则会碎成千百互相不兼容的实现。
- 实用性：**参考（含反面教材）** —— 对我们的基准用户，这篇文章的可操作部分是**工具链清单**
  （见第 25 条的 See-through），而不是它的预言。
  **它的预言本身是本辑最该留档的「反直觉观点」**，但请当作观点而非结论。
- 去重证据：`grep -iF "return.moe"` → 0；`grep -iF "rlaneth"` → 0；`grep -iF "see-through"` → 0。

### 25. ★ See-through：日本 Shitagaki Lab 的单图分层，SIGGRAPH 2026 论文 + Apache-2.0 开源
- 链接：https://github.com/shitagaki-lab/see-through
- 出处：GitHub · **Shitagaki Lab（日本研究组）** · 本轮 **2026-10-10** 实测
- 核实方式：`gh api "repos/shitagaki-lab/see-through"` +
  `gh api "repos/returnmoe/see-through"`（第 24 条作者做的 fork）
- 一句话：把一张平面角色插图切成**分层 PSD**，并且**把被遮挡的部分补画（inpainting）出来** ——
  这正好是 Live2D 流水线里「AI 还不擅长」的那一步。
- 可拓展性：实测数据。
  - **4,496 star / 409 fork**，许可证 **Apache-2.0**，仓库描述写明是
    **"Single-image Layer Decomposition for Anime Characters"（SIGGRAPH 2026 Conference Paper）**。
  - 创建于 **2026-03-31**，最近推送 **2026-10-05** → **仍在活跃维护**（这点比 gd_cubism 强太多）。
  - **return.moe 版本**（https://github.com/returnmoe/see-through，实测 **3 star / Apache-2.0** / push 2026-07-18）
    加了一个 Astro 写的 Web UI + 给 RunPod 这类云 GPU 用的 Docker 镜像 ——
    因为**官方的 Hugging Face Spaces 免费额度不够**（跑不到能用的分辨率），这是第 24 条讲的那个踩坑。
- 实用性：**落地（本轮 AI 方向最值得真的去跑的一条）** —— **Apache-2.0 是真宽松**，
  对「画完一张立绘后，还得花几小时手工拆图层」这个痛点，它是免费的解决方案。
  唯一门槛是需要 GPU（本地跑或用云的容器）。**这是我们索引里少见「License 明确 + star 体量大 + 仍在维护」三条都成立的项目。**
- 去重证据：`grep -iF "shitagaki"` → 0；`grep -iF "Shitagaki Lab"` → 0；`grep -iF "SIGGRAPH 2026"` → 0。

### 26. 海外 Godot 侧的「AI 写移植计划」：redot-cubism 与它的 preflight report
- 链接：https://github.com/dominicbytes/redot-cubism/blob/main/redot_live2d_cubism_importer_codex_plan.md
- 出处：GitHub · dominicbytes（个人）· 快照日期 **2026-09-07**，仓库重命名记录 **2026-09-16**
- 核实方式：`WebSearch`（公开仓库文档全文被收录）
- 一句话：一个把第 17 条的 `gd_cubism` 移植到 **Redot Engine LTS 26.2** 的计划文档 +
  一份「事后复盘」式的 preflight report，目标是给视觉小说/对话/立绘类项目用。
- 可拓展性：这里最有意思的是它的**方法论，而不是代码**。
  - 文档明确把 GDCubism **v0.9.1 定为 baseline**，理由是「它的源码和 native 集成路径是可辨认的」，
    并排除了把 TrueGDCubism 当新 baseline —— 因为后者自称 Godot 4.3+ fork，但**没有可验证的 R5 兼容优势**。
  - **它反复强调「我没验证过就不能说」**：多处写着 "Source licenses do not confer proprietary Core/model
    redistribution rights."、「No marketplace support claim made.」、「No fee/classification conclusion invented.」
    → **一份把「未知」显式登记出来的移植文档**，这比绝大多数 plan 文档干净。
  - 它也确认了 Live2D 官方有一个 community 集成目录，但那边**明确区分「社区维护」与「Live2D 维护」**，
    旧的 Godot 条目**不能当作当前兼容性证据**。
- 实用性：**不采用（理由是：本体不可用，但方法论值得抄）** ——
  这是个人移植计划、不是成品，我们没有 Redot 需求。
  **但它的「先写 preflight report 划分已验证/未验证」这个做法，可以直接抄进本索引的技术选型文档模板。**
- 去重证据：`grep -iF "redot-cubism"` → 0；`grep -iF "TrueGDCubism"` → 0；`grep -iF "GDCubism"` → 0。

---

## 授权与价格（务必核实到官方原文）

> 本节**每一句结论都带官方 URL**，全部为本轮（2026-10-10）`WebFetch` / `WebSearch` 打开过的页面。
> 核不到的地方明确写「未核实」，**不写推测值**。
> ⚠️ **两个提醒**：① 页面上所有 **USD 数字都是 currencylayer 实时汇率换算**，只有 **JPY 是原价基准** → 引用请写日元。
> ② 本节同时存在 **编辑器的钱** 和 **SDK 发布的钱** 两套完全不同的体系，**别混着看**。

### A. 编辑器（Cubism Editor PRO）：只有订阅，没有买断
- **没有 perpetual / 买断制。** 官方商店 `https://store.live2d.com/en/` 实测只列出三种 plan：
  **Annual Plan（可续订）/ Monthly Plan（可续订）/ 3-Year Plan（不可续订）** ——
  「3-Year Plan」是**一次性付三年**，不是永久授权。（来源：https://store.live2d.com/en/ ）
- **PRO for indie**（限定对象：普通用户 / 小规模事业者，**年营业额 1000 万日元未满**）实测价格：
  - 第 1 年 **¥14,280/年**；第 2 年 **¥11,760/年**；第 3 年 **¥10,680/年**（第 3 年折扣适用于之后所有续订）
  - 月付 **¥2,080/月**
  - 3 年 **¥36,720**
  （来源：https://store.live2d.com/en/ ）
- **PRO for business**（年营业额 1000 万日元以上）：本轮**直接打开 store.live2d.com 时只返回了 indie 区块**，
  business 档价格**未核实** —— 检索快照里曾出现 ¥66,000 / ¥59,760 / ¥54,960（年）与 ¥180,720（3 年），
  但**那不是本轮实测**，此处**不采用**。需要请在 https://store.live2d.com/en/ 自行确认。
- **indie 与 business 功能完全一样**：官方原话 "Cubism "for indie" and "for business" do not differ in functionality."
  → 两档的区别**只在签给谁的**（营业额门槛），不是功能多少。（来源：https://store.live2d.com/en/ ）
- 不退款规则：**不退款、不接受退货；Annual Plan 订阅期内不能取消**；官方建议你**先装试用版**确认能跑再买。
  （来源：https://store.live2d.com/en/ ）
- **PRO 有 42 天免费试用**（第三方下载站佐证，非官方原文）：https://www.softpedia.com/get/Multimedia/Graphic/Graphic-Editors/Live2D-Cubism.shtml

### B. 学生 / 教育：¥36,720 → ¥7,344
- **学生折扣：3 年 PRO 打 80% OFF，¥36,720 → ¥7,344（约 $46）**，一次性、不自动续订、毕业后仍可用，
  活动截止 **2027-03-31**。（来源：https://student.live2d.com/en/student-discount/ ）
- **⚠️ 官方站上有第二个数字**：live2d.com **全站共通横幅**在几乎所有页面（如 https://www.live2d.com/en/sdk/license/ 、
  https://www.live2d.com/en/information/cubism-5_4-alpha/ ）上写着 **76% OFF**（对应 ¥8,812）。
  判断：76% 是旧活动文案没改干净，**以 student 子站的 80% / ¥7,344 为准**，但两者都留 URL 备查。
- 申请需要**在学证明**（学校邮箱域，域外邮箱不接受），也接受 **ISIC**（审核约 5~6 天）。
  （来源：https://student.live2d.com/en/student-discount/ 、https://www.live2d.com/en/sdk/license/ ）
- **教育机构免费借用**：LEAP 计划把 Cubism Editor PRO license **免费租给教育机构**，
  官方称已支持**超过 200 所学校**。（来源：https://student.live2d.com/en/education-aid-program/ 、https://www.live2d.com/en/ ）

### C. FREE 版能做什么、不能做什么
- **FREE 版的商业/营利使用是「允许但有门槛」的**：官方原文 —— FREE 版的商用・营利目的利用
  **仅限于「普通用户」以及「小规模事业者（年营业额 1000 万日元未满）」**；除此之外的人只能用 FREE 版做
  **非营利目的或监修（supervision）目的**，输出文件也只能用于内部或非营利或监修目的。
  （来源：https://www.live2d.com/cubism/comparison/ ）
- **FREE 版的硬限制**（同一来源，逐条）：**纹理 2048px 1 张**、**ArtMesh 100**、
  **参数 30**（含 blend shape 参数）、**blend shape 参数 3**、**deformer 50**、**parts 30**、
  **ArtPath 3 条**、**warp deformer 分割 9×9**、**描画顺组 2**、**repeat 2**；
  **视频/连续静止图/GIF 导出最大 1280×720 且会建议带上 Live2D logo**；带 AAC 音轨导出**音频会有哔哔声**。
  超过限制就**存不了**。
- **FREE 与 PRO 的数据可以互通**：PRO 做的文件能用 FREE 打开，但用 FREE **保存**时必须改到限制内。
  （来源：https://www.live2d.com/cubism/comparison/ ）

### D. ★ 把 Live2D 塞进游戏发行：要不要另签授权？（本轮最重要的一组结论）
- **开发期完全不用管钱。** 官方原话：「**License only required upon releasing your content. Not during trial or development.**」
  你可以免费下载 SDK、验证、开发，一分钱不用。（来源：https://www.live2d.com/en/sdk/license/ ）
- **发布时必须签「Publication License Agreement（PLA，正式名：掲載許諾契約 / SDK Release License）」**
  —— **而且官方要求在发布至少 1 个月前完成手续**（License agreement must to be completed at least
  one month prior to the release.）。这不是上线当天补签。
  （来源：https://www.live2d.com/en/sdk/license/ ）
- **但普通用户和小规模事业者是「免除签约 + 免付费」的**，原文：
  "**Individuals and Small-Scale Enterprises are exempted from the license and payment (except Expandable Application).**"
  （来源：https://www.live2d.com/en/sdk/license/ 、https://www.live2d.com/en/sdk/about/ ）
  - 「普通用户」的官方定义：**个人、学生、社团或其他团体，年营业额低于 1000 万日元**。
  - 「小规模事业者」：同样是年营业额低于 1000 万日元。（来源：https://www.live2d.com/en/sdk/license/expandable/ ）
- **具体落到哪个 plan，费用分别是多少**（每个链接都是本轮打开过的官方页）：
  - **买断发行的游戏落在 Plan E（一次性购买内容・非主机非 PC）**：
    普通用户 / 小规模 = **Free**；中型 = **¥100,000**；大型 = **¥600,000**。
    另一种按份计费：每份 **¥40**（普通用户/小规模仍是 Free）；可下载内容按**开卖时先 1000 份**开票，之后每多 1000 份再开票。
    → **这就是「学生发买断制 VN 不用给 Live2D 钱」的落点。**
    （来源：https://www.live2d.com/en/sdk/license/purchase_plan02/ ）
  - **有订阅/内购/广告等持续性收入的游戏落在 Plan G（running royalty・游戏/应用）**：
    基本初期费用（**按发布地区数**计）：个人/小规模 **免费**；中型 **¥50,000**；大型 **¥300,000**。
    基本月费（**按平台数 × 发布地区数**计）：个人/小规模 **免费**；中型 **¥20,000**；大型 **¥100,000**。
    6 个发布地区 = 日本 / 中国大陆·港澳台 / 亚洲（除日本中国台湾）/ 北美 / 欧洲 / 其他；
    4 个平台 = iOS / Android / Harmony OS / Web。（来源：https://www.live2d.com/en/sdk/license/running_plan01/ ）
  - **Plan A「可扩展性应用」是唯一连个人也不豁免的**：
    基本初期费用：个人/小规模 **免费**；中型 **¥50,000**；大型 **¥300,000**。
    基本年度费用（按平台）：个人/小规模 **免费**；中型 **¥240,000**；大型 **¥1,200,000**。
    Revenue share：个人/小规模 **每份 ¥300 或 销售额的 20%，取较高者**；中型/大型 **销售额的 5%**。
    而且必须**过审查**、签字才能发。**原则上「完全免费的应用」审查不通过。**
    （来源：https://www.live2d.com/en/sdk/license/expandable/ ）
- **「可扩展性应用」的官方定义（决定你会不会掉进这个坑）**："Means any work having significant expandability
  among services or content utilizing SDK products." 具体包含：通过添加/组合文件或数据来
  **生成或使用不定数量模型**的派生作品（例：**avatar**）；或一个标题内含多个/其它作品、或能从该标题访问到那些作品
  （例：**相关作品合集或 portal**）。（来源：https://www.live2d.com/en/sdk/license/expandable/ ）
  → **做追踪软件给别人用 = Plan A**；**做单机固定角色 VN = 不是 Plan A**。
- **规模变了要主动报告**：营业额让 business size 变化，须在 **2 个月内**通知 Live2D，
  可被追溯到变更当月按新价表补签。（来源：https://www.live2d.com/en/sdk/license/running_plan01/ 、
  https://www.live2d.com/en/sdk/license/expandable/ ）
- **BtoBtoX（内容不直接给终端用户而是卖给其他公司）不属于以上任何 plan，要单独联系。**
  （来源：https://www.live2d.com/en/sdk/license/ ）
- 8 个 plan 的完整清单入口：https://www.live2d.com/en/sdk/license/ （A/B/C/D/E/F/G/Others）。
  本轮**未打开**的有：license plan B https://www.live2d.com/en/sdk/license/non-profit_plan02/ 、
  plan C https://www.live2d.com/en/sdk/license/running_plan02/ 、plan D https://www.live2d.com/en/sdk/license/non-profit_plan01/ 、
  plan F https://www.live2d.com/en/sdk/license/purchase_plan01/ → **这些的价格本轮一律写「未核实」。**

### E. 「免费」的真实代价：三件必须做的事
- **官网展示的 PLA 价格全部是「折后价」**，折扣的前提是**同意显示 Live2D logo、
  并把作品收进 Live2D 的 Showcase / Database**。
  （来源：https://www.live2d.com/en/sdk/guidelines/ 、https://www.live2d.com/en/sdk/license/running_plan01/ ）
- 四项 **Mandatory**（来源：https://www.live2d.com/en/sdk/guidelines/ ）：
  1. **在启动/起始画面显示 Live2D logo**（一处即可，splash 至少显示 **1 秒**，不含淡入淡出，可跳过）；
  2. **在各发行平台的商品介绍页写上「Live2D」字样**（如 App Store / Google Play），格式不限，
     官方示例 "Powered by Live2D"；
  3. **把作品提交进 Live2D Database**（官方维护的商业作品 + 创作者数据库）；
  4. **填一份改进问卷**（由实际用 SDK 的负责人填）。
  - Voluntary：credits 里再标一次（可选）。
  - **成人内容的例外**：只适用第 2 和第 4 项，**第 1（显示 logo）和第 3（进 Database）不需要**。
- Showcase / Database 入口：https://www.live2d.jp/showcase/ （该页面本轮**未打开**，仅从 guidelines 页的链接摘得）。

### F. VTuber / 直播场景的授权条款（单独一条，别和上面的混）
- **官方备案过一段给「面捕/追踪软件」的声明**，要点：若把该软件作为**事业的主要元素**，
  且由该软件或用该软件产出的内容带来的**直接或间接年销售额超过 2000 万日元**，
  就必须签 PLA 并付费，并须立即通知 Live2D。
  （来源：https://www.live2d.com/en/sdk/license/ ，原文为整段引用；注意 **2000 万**这个阈值与编辑器的 1000 万不是同一个）
- 这种情况下对应的 license plan 是 **Plan A（Expandable Applications）**。
  （来源：https://www.live2d.com/en/sdk/license/ ）
- **你自己发行面捕软件给别人用本身就属于 Plan A**，要先过审查再签专门的 PLA。
  （来源：https://www.live2d.com/en/sdk/license/ ）
- Live2D 官方自己的面捕软件 **nizima LIVE** 三档价：Free **¥0** / for indie **¥550 每月** /
  for business **¥3,300 每月**（后两者年缴 8 折）。（来源：https://nizimalive.com/en/ ）

### G. 第三方调用 Live2D 引擎时的条款（Ren'Py 官方的口径，可与上面互相印证）
- Ren'Py 官方文档明确写：「…you may need to purchase a license to use Live2D if your business makes
  more than a certain amount of money a year.」
  （来源：https://www.renpy.org/doc/html/live2d.html ）
- 它与 D 节官方口径一致：不是「用了就给钱」，而是「**营业额到某个门槛才需要」。
  具体的门槛请以官方 plan 表（D 节）为准，**不要采信任何转述的具体金额**。

### H. 本轮明确「未核实」的清单（避免下次误以为已核）
- PRO for business 的官方现行价格
- license plan B / C / D / F 的价格表
- 3-Year Plan 到期后如何续、是否有 renewal 价格
- 学生优惠的 Perpetual 与否之外的细节（条款页未打开）
- Cubism Editor 5.3.00 的确切发布日（存在 2025-11-14 与 2026-01-20 两说）
- Live2D JUKU 的订阅价格

