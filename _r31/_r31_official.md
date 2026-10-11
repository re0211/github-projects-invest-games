# R31 · Live2D / Cubism 官方动态增量调研（官方与海外信源索引）

- 轮次：第 31 轮
- 调研日期：2026-10-11
- 对照基线：第 30 轮（20 分钟前）——官方 SDK 全线 5-r.5、Editor 5.3.04、学生优惠简中站 80% OFF
- 本轮目标：**只记「有没有新变化」**，不重述旧结论
- 查重基线：`_r31\_dedupe_urls.txt`（475 行）

---

## 一、官网新闻 / 公告（live2d.com 首页时间轴 + live2d.jp）

### 1. 首页新闻时间轴最新条目定格在 2026.07.17（无新公告）
- URL: https://www.live2d.com/en/information/
- 来源/日期: live2d.com 英文站「Information」全列表 · 抓取于 2026-10-11
- 事实：英文站新闻列表按日期倒序，**最新一条 = 2026.07.17**，其下依次 2026.07.14 / 2026.03.20 / 2026.02.13 / 2026.01.20 / 2025.11.14 ……。即**官网新闻自 2026-07-17 起已近 3 个月无新增条目**（Editor 5.3.01~5.3.04 四个 patch 均未发新闻）。
- 判定：✅采纳（作为「无新变化 / 新闻停更」的证据）

### 2. Cubism PRO 2026 夏季特惠 20% OFF（新 URL，未收录）
- URL: https://www.live2d.com/en/information/summersale-2026/
- 来源/日期: live2d.com 英文站 · 公告日期 **2026.07.17**，活动截止 2026-07-27（已结束）
- 事实：标题「Get 20% OFF Live2D Cubism PRO! Ends Monday, July 27, 2026」。为常规促销（非学生优惠），力度 **20% OFF**。详情页内嵌日期 2026.07.17，与首页时间轴一致（交叉核验通过）。
- 判定：🔶观察（官方新闻，但为已过期促销；与基线里的 springsale-2026 是两次不同活动）

### 3. 交叉验证方法：首页日期无错位
- URL: https://www.live2d.com/en/information/cubism-5_4-alpha/ 等 4 个详情页
- 来源/日期: live2d.com 各公告详情页 · 2026-10-11
- 事实：逐个打开详情页核对内嵌日期 —— 5.4 Alpha 页 = 2026.07.14、夏季特惠页 = 2026.07.17、5.3.00 发布页 = 2026.01.20、西语站点页 = 2026.02.13，**与首页时间轴「日期＋标题」配对完全一致**。本轮未复现「日期错位一位」的坑（原始 HTML 解析 `日期→紧随标题→紧随 href` 自洽）。
- 判定：✅采纳（方法留证，避免上几轮的误读）

### 4. live2d.jp 公司站新闻：『Live2D Chapters』启动（新）
- URL: https://www.live2d.jp/news/live2d-chapters/
- 来源/日期: live2d.jp 新闻列表 · **2026.05.22**
- 事实：标题「【Live2D】世界各地のユーザーコミュニティを公式支援する『Live2D Chapters』始動」——官方开始正式支援全球各地用户社区（Chapters 计划）。产品/社区层面新动作。
- 判定：✅采纳（新官方口径，基线无任何 live2d.jp 链接）

### 5. live2d.jp 公司站新闻：著作物「シンプルライセンスプラン」加入 nizima LIVE（新）
- URL: https://www.live2d.jp/news/simple-license-nizimalive/
- 来源/日期: live2d.jp 新闻列表 · **2026.04.30**
- 事实：「『著作物シンプルライセンスプラン』に nizima LIVEを追加」——把 nizima LIVE 纳入「著作物简易授权方案」，属**授权条款变更**。
- 判定：✅采纳（授权面新变化）

### 6. live2d.jp：20 周年纪念企划「Shape the Future」启动 + 主题曲英语版
- URL: https://www.live2d.jp/news/20thprojectstart/
- 来源/日期: live2d.jp 新闻列表 · 企划启动 **2025.12.03**；主题曲英语版演唱者公布 **2026.01.20**（Nerissa Ravencroft / hololive English）
- 事实：2025.12.03 起一年内滚动展开 20 周年联动企划；2026.01.20 公布英语版主题曲演唱者。学优 80% 即挂靠此企划（见第 12 条）。
- 判定：🔶观察（品牌事件，非 SDK/授权硬信息）

### 7. live2d.jp 其余新闻均为招聘说明会（无料）
- URL: https://www.live2d.jp/news/
- 来源/日期: live2d.jp · 2026-10-11
- 事实：2026.10.7 / 2026.8.3 / 2026.6.2 / 2026.4.3 / 2026.2.18 / 2026.1.7 / 2025.10.30 等条目**全部是「開発チーム オンライン採用説明会」招聘线上说明会**，与产品/技术无关。最新一条 2026.10.7（面向 10 月 19 日场次）。
- 判定：❌否决（招聘信息，无索引价值）

---

## 二、Cubism Editor 版本（docs Release History 表）

### 8. docs 英文版 Release History 表（新入口，patch 号唯一来源）
- URL: https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title/
- 来源/日期: docs.live2d.com 英文 Editor Manual · 页面含「5.4 alpha Now Available」横幅，抓取于 2026-10-11
- 事实：Release History 表（MM/DD/YYYY）最新数行：
  - **09/03/2026 Cubism 5.3.04**（最新正式版）
  - 07/30/2026 Cubism 5.3.04 beta1
  - 06/16/2026 Cubism 5.3.03 ／ 05/14/2026 5.3.03 beta1
  - 04/02/2026 Cubism 5.3.02 ／ 03/03/2026 5.3.02 beta1
  - 02/24/2026 Cubism 5.3.01
  - 01/20/2026 Cubism 5.3.00
- 判定：✅采纳（与 R30 一致：Editor 仍为 **5.3.04**，无新 patch；此表为 patch 号唯一来源）

### 9. 产品页「Latest Updates」与 docs 表口径冲突（持续）
- URL: https://www.live2d.com/en/cubism/update/
- 来源/日期: live2d.com 产品页 · 2026-10-11
- 事实：产品页「Latest Updates」最新条目仍只写 **Cubism Editor 5.3.00 released!**（大版本），**未列 5.3.01~5.3.04 patch**；docs 表为 5.3.04。**产品页 5.3.00 vs docs 表 5.3.04** 的官方口径冲突在 R31 依旧存在且未修。
- 判定：✅采纳（口径冲突，需在索引中标注「以 docs 表为准」）

---

## 三、SDK 版本（下载页 / GitHub Releases / docs 手册）

### 10. **Cubism 5 SDK for Unreal Engine R1 beta2**（最新 SDK 事件，新）
- URL: https://github.com/Live2D/CubismUnrealEngineComponents/releases/tag/5-r.1-beta.2
- 来源/日期: GitHub live2d 组织 Releases ＋ docs `cubism-sdk-manual/top` 公告 · **2026-09-29**（公告日 09/29/2026）
- 事实：tag `5-r.1-beta.2`，发布 2026-09-29T03:34Z。新增支持 macOS / iOS / Android 平台构建运行；新增 Koharu 模型与全部模型源工程；新增 `CubismStoredSourcePath`、参数 repeat；修复移动端预览稳定性、Android 遮罩渲染、UE 5.3 资产兼容等。docs 同日批量放出 SDK for Unreal Engine 教程（Motion/LookAt/Expression/Raycast 等 Sample）。
- 判定：✅采纳（**这是全线 SDK 最近一次更新**；R30「全线 5-r.5」的说法对 Unreal 不成立——Unreal 是独立 R1 线，且为 beta2，见负结论）

### 11. **Cubism 5 SDK MotionSync Plugin R2_1**（新）
- URL: https://www.live2d.com/en/sdk/download/motionsync/
- 来源/日期: live2d.com MotionSync 下载页 ＋ docs 公告 · **2026-08-25**（Unity 与 Native 同日）
- 事实：[2026/08/25] MotionSync Plugin **for Unity R2_1**；[2026/08/25] **for Native R2_1**；**Web 端仍停在 [2025/03/27] R2**（无 R2_1）。上一版 R2 为 2025-03-27（Native/Web）/ 2024-11-28（Unity）。
- 判定：✅采纳（MotionSync Unity/Native 升到 R2_1，Web 滞后）

### 12. Cubism 5 SDK for Java R5
- URL: https://www.live2d.com/en/sdk/download/java/
- 来源/日期: live2d.com Java 下载页 ＋ GitHub CubismJavaFramework · **2026-06-04**
- 事实：[2026-06-04] Cubism 5 SDK for Java R5；GitHub tag `5-r.5` 同期发布。较旧的 `5-r.5-beta.1.1`(2026-02-19)。
- 判定：✅采纳（R30 已知 R5，此处补日期 2026-06-04）

### 13. Cubism 5 SDK for Unity —— R5 与 R4_2 并存
- URL: https://www.live2d.com/en/sdk/download/unity/
- 来源/日期: live2d.com Unity 下载页 · 2026-10-11
- 事实：页面同时列两条更新史：**[2026-04-02] Cubism 5 SDK for Unity R5** 与 **[2026-05-14] Cubism 5 SDK for Unity R4_2**。GitHub Releases 同序（R4_2 2026-05-14，R5 2026-04-02）。**注意 R4_2 晚于 R5，是 R4 线的维护版，不是版本倒退**。repo 最新提交 2026-09-29（修 Unity 6.6 `GetInstanceID` 过时编译错误）。
- 判定：✅采纳（Unity 双线并存需在索引中说明，避免误判「R4_2 是最新」）

### 14. Cubism 5 SDK for Native / Web R5（无变化）
- URL: https://www.live2d.com/en/sdk/download/native/ · https://www.live2d.com/en/sdk/download/web/
- 来源/日期: live2d.com 下载页 · 均 **[2026-04-02] Cubism 5 SDK R5**
- 事实：Native R5、Web R5 均停在 2026-04-02；无 R6、无 5-r.6。
- 判定：✅采纳（无变化，作基线锚点）

### 15. Cubism 5 AE Plugin R7（新，正式版）
- URL: https://docs.live2d.com/en/cubism-editor-manual/cubism-ae-plugin-download/
- 来源/日期: docs.live2d.com Editor Manual · 页面 Updated 2026-05-21
- 事实：**[05/21/2026] Live2D Cubism 5 AE Plugin R7**（正式版），仅「Updated SDK：Native R5 / Web R5」。前序 **[03/26/2026] R7 beta1** 才引入混合模式与离屏渲染支持（更新至 Native R5 beta3_1 / Web R5 beta3_1）、遮罩 [Hide] 菜单混合模式与绘制顺序。再往前 R6 = 2025-05-29。
- 判定：✅采纳（AE 插件正式版跳到 R7，基线未含）

### 16. docs SDK 手册公告时间线（核验用）
- URL: https://docs.live2d.com/en/cubism-sdk-manual/top/
- 来源/日期: docs.live2d.com SDK Manual · 2026-10-11
- 事实：公告倒序 —— 09/29/2026 SDK R1 beta2（UE）；08/25/2026 MotionSync R2_1；06/04/2026 SDK R5（Java）；05/14/2026 SDK R4_2（Unity）；04/02/2026 SDK R5（Native/Web/Unity）；03/27/2025 MotionSync R2。**全部页面顶部挂「5.4 alpha Now Available」横幅，但 5.4 目前只有 Editor alpha，未配套新 SDK**。
- 判定：✅采纳（SDK 全量交叉核验基准）

---

## 四、开源包版本（pypi / npm / crates.io）

### 17. **live2d-py 升到 1.0.0**（新，重大版本）
- URL: https://pypi.org/project/live2d-py/ · https://github.com/Arkueid/live2d-py
- 来源/日期: PyPI JSON ＋ GitHub Releases · **v1.0.0 = 2026-09-30T11:50Z**
- 事实：`live2d-py` 最新 **1.0.0**（requires_python >=3.11）。版本时间线：0.6.1(2026-01-16) → 0.7.0(2026-05-20) → **0.8.0(2026-09-24)** → 0.8.0.7/.9 alpha(2026-09-24) → 0.8.1(2026-09-26) → **1.0.0(2026-09-30)**。1.0.0 变更：v2/v3 模型统一用 `live2d.Model` 类加载（部分接口名变更）、减少默认日志、**移除 `live2d.v3` 与 `live2d.v2cpp` 模块**、Viewer 同时支持 v2/v3、修 v2cpp 遗留问题。仓库 pushed 2026-10-11（今日仍在更新），星标 576。
- 判定：✅采纳（**破坏性 API 变更，Python 侧集成方必读**）

### 18. `pixi-live2d-display` 长期停更（无变化）
- URL: https://www.npmjs.com/package/pixi-live2d-display
- 来源/日期: npm registry · latest 0.4.0（2022-09-04）／beta 0.5.0-beta（2023-12-07，dist-tags 未变）
- 事实：dist-tags = {latest: 0.4.0, beta: 0.5.0-beta}；末次发布 **2023-12-07**，registry modified 同为 2023-12-07。无新版本。
- 判定：❌否决（三年无更新）

### 19. `easy-live2d` / `live2d-motion3` —— 包名不存在（负结论）
- URL: https://www.npmjs.com/package/live2d-motion3 · https://crates.io/crates/live2d-motion3 · https://pypi.org/pypi/easy-live2d/json
- 来源/日期: npm / crates.io / PyPI API · 2026-10-11
- 事实：npm `live2d-motion3` 无此包（dist-tags 返回空）；crates.io `live2d-motion3` / `easy-live2d` 均查无（crates.io 仅存一个无关的 `live2d` 0.0.0 / 2018-02-10）。PyPI `easy-live2d`、`easy_live2d` 均 404。
- 判定：❌否决（以当前包名在各 registry 不存在，勿追）

---

## 五、论文（arXiv / pith；arXiv 官方 API 本轮被限流）

### 20. **Bunraku：单张插图 → 可编辑 Live2D 角色（含 Live2D-Bench 评测）**
- URL: https://arxiv.org/abs/2607.27348
- 来源/日期: arXiv cs.CV · 首发 **2026-07-29**，v1 发布 2026-07-31；作者 Junhao Chen 等（清华 / 南洋理工 / SparcAI 系）
- 事实：**首个「单图 → 端到端 Live2D 资产」系统**（分层扩散拆 RGBA 图层＋遮挡补全；再逐层建三角网格并**联合**预测全角色关键姿势顶点位移）。关键评测数字：50 个未见角色、真生成无 teacher forcing 下**每顶点方向余弦 0.768（中位 0.828）**；网络中参数从 5.1M 放大 **112×**（至 571.6M）**无提升**（结论：瓶颈是跨层协同而非容量）。附带 **Live2D-Bench**（首个该任务标准基准，120 对分层 PSD）与 **8,884 个模型的 Live2D 语料库**（7,773 人形 + 1,111 非人形）。项目页 https://bunraku-live2d.github.io/ 。
- 判定：✅采纳（正式 arXiv 页为本轮新 URL；注意 `https://pith.science/paper/2607.27348` 已在基线，属同篇，见剔除表）

### 21. CartoonAlive：单张人像 → 表情 Live2D（旧，非本轮新论文）
- URL: https://arxiv.org/abs/2507.17327
- 来源/日期: arXiv cs.CV · **2025-07-23**（技术报告）
- 事实：单张人像 → Live2D，用 shape basis 构造面部 blendshape，据关键点回归权重，**<30 秒**生成、支持 **52 个表情控制**；MLP 训练集为 10 万对合成渲染。作者 Chao He / Jianqiang Ren / Jianjing Xiang / Xiejie Shen。项目页 human3daigc.github.io/CartoonAlive_webpage/ 。新出现的只是它的 pith 综述页（pith.science/paper/G4NR4YK3，综述时间 2026-09-23）。
- 判定：🔶观察（论文本身 2025 年，非新；作「单图→Live2D」谱系对照）

### 22. Textoon：文本 → Live2D 卡通角色（旧）
- URL: https://arxiv.org/abs/2501.10020
- 来源/日期: arXiv cs.CV · 首发 **2025-01-17**（v2 2025-02-05），阿里通义实验室
- 事实：文本描述 → Live2D 格式 2D 角色，**<1 分钟**；Qwen2.5-1.5B 解析属性（准确率 >90%）、SDXL+ControlNet 生成、遮挡补全、接入 ARKit 52 blendshape + Wav2Vec-XLSR 口型。项目页 human3daigc.github.io/Textoon_webpage/ 。
- 判定：❌否决（2025 年初旧作，本轮无更新）

---

## 六、社区源（HN / dev.to）

### 23. HN Algolia：live2d 无相关新帖（负结论）
- URL: https://hn.algolia.com/api/v1/search?query=live2d&tags=story
- 来源/日期: HN Algolia API · 2026-10-11
- 事实：`live2d` 命中 463 条但**近一年内无 Live2D 主题 story**；按日期过滤 2026 年命中项全是同名误召（"live diff"、个人项目等）。唯一高相关旧帖是 2023 年的「Live2D Is a Security Trainwreck」（100 pts）。`cubism` 查询同样无相关新帖。
- 判定：❌否决（无料，HN 对本主题已无产出）

### 24. dev.to：live2d 标签无新料
- URL: https://dev.to/api/articles?tag=live2d
- 来源/日期: dev.to API · 2026-10-11
- 事实：最新一篇为 2026-06-08 的「Open-LLM-VTuber Review」（第三方评测，非官方）；此后无新文章。与往轮判断一致。
- 判定：❌否决（顺手扫，无新料）

---

## 七、商用授权 / 定价 / 学生优惠

### 25. 官方商店定价（英文结算店）——未改版
- URL: https://store.live2d.com/en/
- 来源/日期: Live2D Store/EN 结算页 · 2026-10-11
- 事实（**以结算页为准**）：indie 年度方案 Year1 **$90.22 USD [¥14,280]/yr**、Year2 **$74.30 [¥11,760]**、Year3 **$67.47 [¥10,680]**；月付 **$13.14 [¥2,080]/mo**；3 年一次付 **$231.99 [¥36,720]/3yr**。business 年度 Year1 **$416.97 [¥66,000]**、Year2 $377.55 [¥59,760]。**JPY 基准价与历史完全一致**（¥14,280/¥11,760/¥10,680），**未改版**。
- 判定：✅采纳（定价锚点：无变化）

### 26. **学生优惠：英文店已改显 80% OFF（20 周年特价，截止 2027-03-31）**
- URL: https://student.live2d.com/en/student-discount/ · https://store.live2d.com/en/
- 来源/日期: Live2D Student 英文页 ＋ Store/EN · 2026-10-11
- 事实：英文学生页现写「**For this academic year only, grab the Cubism PRO 3-Year Plan at a massive 80% OFF**」；原价 $231 [¥36,720]/3yr → **学生价 $46 USD [¥7,344]**（= 80% off，与 Store/EN 结算页 `3yr $46.40 [¥7,344]` 一致）。**优惠截止 2027 年 3 月 31 日**。中文学生页同步：原价 RMB1,552/¥36,720 → **学生价 RMB310/¥7,344**，截止「2027 年 3 月 31 日」，且注明优惠券**仅限 Live2D Store/CN 使用**。该 80% 被官方定义为 20 周年特别企划（"Shape the Future"）。
- 判定：✅采纳（**R30 记的「英文站 76%」现已不成立**——英文学生页/英文结算店均为 80%，见下条冲突）

### 27. ⚠️ 官方口径冲突①：同一英文首页并存「80% OFF」与「76% OFF」
- URL: https://www.live2d.com/en/
- 来源/日期: live2d.com 英文首页 · 2026-10-11
- 事实：**同一张英文首页 HTML 内**同时存在两句互斥文案——Student Discount 卡片（可见区）：「**80% OFF** the Live2D Cubism PRO 3-Year Plan for students and faculty」；而「The Live2D Student Discount Program How-to Guide」段落（另一区块）：「receive a **76% OFF** coupon for a 3-year Live2D Cubism Editor PRO subscription」。**这正是 R30「英文站 76% vs 简中站 80%」的根源：不是两站冲突，而是英文首页自身新旧文案未统一**。权威取值应为 **80%**（学生专页＋结算页一致）。
- 判定：✅采纳（**新定位的官方口径冲突，高价值**）

### 28. ⚠️ 官方口径冲突②：LEAP 覆盖校数「200+」vs「450+」
- URL: https://www.live2d.com/en/ · https://student.live2d.com/en/education-aid-program/ · https://student.live2d.com/zh-chs/education-aid-program/
- 来源/日期: live2d.com 首页 ＋ Live2D Student 中英文页 · 2026-10-11
- 事实：**首页**写「The program has now supported **over 200 schools**」；**LEAP 中/英文页**均写「**more than 450 educational institutions and programs and approximately 48,000 student users**（*As of March 2025*）／逾 450 个教育机构与项目、约 48,000 名学生用户（截至 2025 年 3 月）」。**同属 LEAP 计划，校数口径 200 与 450+ 相差一倍以上**。
- 判定：✅采纳（第二个官方口径冲突；索引中应以 LEAP 专页「450+ / 截至 2025-03」为准）

### 29. Cubism SDK 授权框架（无版本变更迹象）
- URL: https://www.live2d.com/en/sdk/license/ · https://www.live2d.com/en/sdk/about
- 来源/日期: live2d.com SDK 授权页 / 产品页 · 2026-10-11
- 事实：SDK 仍为「下载无初始费用；发布内容时须签 Publication License Agreement 并付费；个人与小规模企业豁免（Expandable Application 除外）」。MotionSync Plugin 免版税、无需 CRIWARE logo。**未检测到 SDK 授权协议改版**（与授权相关的最新变更为第 5 条 nizima LIVE 加入简易授权方案）。
- 判定：🔶观察（无变化，留作基线）

---

## 已收录（剔除）

以下 URL 命中 `_r31\_dedupe_urls.txt`，本轮不再重复收录：

- https://www.live2d.com/en/information/cubism-5_4-alpha/ （5.4 Alpha，基线 line 425）
- https://www.live2d.com/en/information/cubism-editor-5-3-00-official-release/ （基线 line 426）
- https://www.live2d.com/information/springsale-2026/ （基线 line 432；注意与第 2 条 summersale-2026 是两次活动）
- https://www.live2d.com/en/cubism/comparison/ 、https://www.live2d.com/zh-chs/cubism/comparison （基线 line 423/434）
- https://www.live2d.com/en/sdk/guidelines/ 、/en/sdk/license/ 、/en/sdk/license/expandable/ 、/purchase_plan02/ 、/running_plan01/ （基线 line 427–431）
- https://www.live2d.com/zh-chs/community/ （基线 line 433）
- https://store.live2d.com/en/ （基线 line 367）
- https://student.live2d.com/en/student-discount/ 、https://student.live2d.com/zh-chs/education-aid-program/ （基线 line 368/369）
- https://docs.live2d.com/en/cubism-sdk-manual/compatibility-with-cubism-5-3-official （基线 line 129）
- https://docs.live2d.com/zh-chs/cubism-editor-manual/new-function5-3/ （基线 line 130）
- https://docs.live2d.com/cubism-editor-tutorials/top/ 、/en/cubism-editor-manual/divide-the-material/ （基线 line 127/128）
- https://github.com/live2d 、https://github.com/live2d/cubismunitycomponents （基线 line 207/208）
- https://pith.science/paper/2607.27348 （Bunraku 同篇，基线 line 352）
- https://blog.return.moe/en/2026/07/19/towards-fully-automated-live2d-style-animation （基线 line 101）
- https://cloudymount789.github.io/blog/live2d_note/ （基线 line 110）
- https://doc.renpy.cn/zh-tw/live2d.html 、https://www.renpy.org/doc/html/live2d.html （基线 line 125/441）

---

## 负结论

1. **无 5-r.6，无 6.0**：Native/Web/Unity/Java 全线最新仍为 **R5**（Unity 另有 R4_2 维护版），Unreal 为 **R1 beta2**，MotionSync 为 **R2_1**。未发现任何 5-r.6 或 6.0 字样。
2. **Editor 无新 patch**：仍为 **5.3.04**（2026-09-03），与 R30 一致。5.4 仅 Editor alpha，**无配套 5.4 SDK**（docs 全站横幅「5.4 alpha Now Available」但 SDK 公告线仍以 R1 beta2 为最新）。
3. **官网新闻停更**：live2d.com 英文新闻最新为 2026-07-17，之后近 3 个月无新增；5.3.01~5.3.04 未发新闻稿。
4. **HN Algolia 无料**：`live2d` / `cubism` 近一年无相关 story。
5. **dev.to 无料**：tag=live2d 最新 2026-06-08，之后再无。
6. **包荒**：`easy-live2d`、`live2d-motion3` 在 npm/crates.io/PyPI **不存在**（勿再追）；`pixi-live2d-display` 三年未更新。
7. **Reddit / Medium / YouTube / itch.io 不可达**（HTTP 000），本轮未耗时间。
8. **arXiv 官方 API（export.arxiv.org）本轮被网络策略拒绝**，改用 WebSearch + 聚合页（arxiv.gg / pith / deeppaper）取得论文信息，未直连 arXiv API。

---

## 搜索覆盖

| 类别 | 入口 / 方法 | 结果 |
|---|---|---|
| live2d.com 首页时间轴 | curl 原始 HTML + 逐公告详情页交叉核验 | ✅ 有（最新 2026.07.17） |
| live2d.com Information 全列表 | curl `/en/information/` | ✅ 有 |
| live2d.jp 公司站 | curl 首页 + `/news/` | ✅ 有（Chapters / 授权 / 20 周年） |
| docs Release History 表 | WebFetch `new-feature-introduction-title` | ✅ 有（5.3.04） |
| docs SDK 手册公告线 | WebFetch/搜索 `cubism-sdk-manual/top` | ✅ 有 |
| SDK 下载页（Native/Web/Unity/Java/MotionSync/AE） | WebFetch + curl | ✅ 有 |
| GitHub Releases（10 个 Cubism* 仓库） | `gh api` releases/tags/commits | ✅ 有 |
| npm / PyPI / crates.io | curl registry API | ✅ 有 |
| arXiv / pith / 聚合站 | WebSearch（官方 API 被拒） | ✅ 有（Bunraku） |
| HN Algolia API | curl JSON | ✅ 空 |
| dev.to API | curl JSON | ✅ 空 |
| store / student 定价 | curl + WebFetch 结算页 | ✅ 有 |
| Reddit / Medium / YouTube / itch.io | — | ❌ HTTP 000，跳过 |

**本轮相对 R30 的变化（速览）**：
1. 学生优惠口径：英文首页新旧文案并存（**80% vs 76%**），权威=**80%**，且明确「截止 2027-03-31」；R30 的「英文站 76%」已过时。
2. 新出现官方页面：20 周年「Shape the Future」学优页、Summer Sale 2026、Live2D Chapters、著作物简易授权方案并入 nizima LIVE。
3. SDK 日期补全：Unreal **R1 beta2（2026-09-29）**、MotionSync **R2_1（2026-08-25）**、Java R5（2026-06-04）、Unity R4_2（2026-05-14）——R30「全线 5-r.5」需修正为「分线各自版本」。
4. 新版本号：**live2d-py 1.0.0（2026-09-30，破坏性变更）**、**AE Plugin R7（2026-05-21）**。
5. Editor 与 SDK 主版本无变化（仍 5.3.04 / R5 系）。
