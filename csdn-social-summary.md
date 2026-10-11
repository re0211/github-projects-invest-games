# 跨平台游戏制作 × AI 开发资源梳理（2026-10-11 · 第三十二辑 · **有人正面拆了 Cubism Core 那堵墙**）

> 本辑为 Live2D 连续第八轮。**主线不是「又找到几个工具」，而是「卡了六轮的那堵墙，第一次有人正面拆」。**
> 三路候选：gh 30 条 · cn 16 条 · official 21 条；落索引 **22 卡**（1257 → 1279 → **1301**）。
> 所有 ★ / 许可证 / 日期均走 `gh api repos/<r>` 实取，**主 agent 已把 22 条卡片逐条复验一遍**（见 §四）。

---

## 一、上轮待办检查（5 条 → **闭环 5 条**）

| # | 上轮待办 | 状态 | 结果一句话 |
|---|---|---|---|
| ① | 实测 `moeru-ai/airi`（连续两轮顺延） | ✅ | **它的 Cubism Core 版本定位到了硬编码 URL**：`CubismSdkForWeb-5-r.3.zip`（详见 §五） |
| ② | 核 Inochi2D 栈在 Windows 能否装起来 | ✅ | **假设部分不成立**：SDK **有 win32 预编译包**，不用 D 编译器；编辑器有 MSI 但**停更 1 年 4 个月** |
| ③ | 补读 Cubism 5.3.01–5.3.04 各更新了什么 | ✅ | **逐版读完**（规律：**beta1 写全套、正式版只写修补**）→ 见 §五 |
| ④ | 修 `insert_guard_probe.py --base-block` 裸 sha 陷阱 | ✅ | 自动补 `:index.html` + 非 HTML 直接 rc=2 报错 + 新增 `--selftest`（**7/7**） |
| ⑤ | 房规压缩（**连续第六轮欠账**） | ✅ | `agent-house-rules.md` **200 → 189 行**，**23 条一条没少**（做法改了：压正文，不撤条款） |

> ⑤ 这条拖了六轮，本辑换了个做法才推动：**问题不是「条款太多」，是「每条正文太啰嗦」**。
> 原纪律写的是「超 200 行先砍最通用的条款」—— 但砍条款要先归档、代价高，还会误伤元规则（#33 被砍过两轮）。
> 改成**压正文**（把来源叙事缩成一行）之后，一行没丢就腾出 11 行。新纪律已写进文件尾部。

**顺手抓到的**：`insert_guard_probe.py` 的修复本身**也暴露了一个可复用的教训** ——
闸门脚本自己的失败模式如果是「沉默」（不报错、只是判据悄悄翻倍），就必须**给自己配一组反例**（M-0020 / M-0024 家族）。

---

## 二、本辑一句话

**前六辑反复承认同一件事：「不买 Cubism Editor，就没有合法的 moc3 渲染器」。这一辑出现了两个正面拆墙的人 ——
一个（★351 的 Rust 库）已经把墙拆开了，另一个（★2 的 Rust 栈）刚把枪口对准；同时，官方自己把 Editor 的「编辑 API」放了出来，
第三方立刻围出一整簇工具。**

---

## 三、主线一：ayagami —— 第一条公开的「黑盒逆向 moc3」开源渲染器

### 1. `AyagamiDev/ayagami`（★351 · Rust · Apache-2.0）

| 项 | 值 |
|---|---|
| 地址 | https://github.com/AyagamiDev/ayagami （Demo: https://demo.ayagami.dev） |
| 创建 / 推送 | **2026-07-11 / 2026-09-14** |
| 星标 | **351**（3 个月） |
| 做的事 | **直接读 Live2D 的 `.moc3`**，用 wgpu 渲染（Vulkan / Metal / DX / OpenGL / WebGL / WebGPU 全后端） |
| 宣称支持 | MOC3 特性「up to **SDK 5.0**」：Parts、ArtMeshes、旋转/弯曲变形器、Glue、Blendshape 参数；**物理引擎已完成**；「**SDK 5.3 features（advanced blend & off screen rendering）**」也已打勾 |
| 法律姿态 | README 明写 **strictly using black-box reverse engineering**，并配了 contributor policy 保证 —— **从不反汇编/反编译专有软件** |

**为什么这是本辑最硬的一条**：索引里的「开源替代」此前要么**不碰 moc3**（Inochi2D 用自己的格式、`umamo` 只读 `.cmo3`），
要么**只做 JSON 不做网格**。ayagami 是第一条公开、活跃、**声称已实现 MOC3 加载 + 渲染**的开源库。
更关键的是它把两件事在法律上分开了：**「格式兼容」≠「破解软件」** —— 只看输入输出反推格式，不碰二进制本体。

**但别现在押它**（作者的自我披露，不是我的判断）：
① `API is pretty unstable … no documentation yet`，crates.io 还没发版；
② **表达式 / pose / 动作文件仍是 TODO** → 做得成挂件，做不成完整 VTuber；
③ 许可**双标**（README 写 MIT + Apache-2.0，GitHub 只识别出 Apache-2.0）→ **引用时以仓库内 LICENSE 原文为准**；
④ 「黑盒逆向合法」是**作者的法务主张**，各地对专有格式逆向的认定不同，商用前自行复核。

### 2. 两条配套：一条通引擎，一条当实验台

- **`ayagami-gd`（★39 · MIT · Rust · 推送 2026-09-15）** —— Ayagami 的 **Godot 绑定**。
  Godot 侧原本只有「官方 Cubism Native SDK」一条路（`gd_cubism`），这条是新增的「**Godot + 非官方 moc3 渲染器**」组合。
  ⚠️ 需 **Godot 4.7**，而 `gd_cubism` 的二进制仍 target **Godot 4.3 ABI** —— **两者版本要求不同，别混着装**。
- **`pakholeung37/manosaba-live2d`（★0 · C++ · 无 license · 推送 2026-09-16）** ——
  **同一 Godot 工程里把两条运行时并行跑**的对照实验台：一条 `gd_cubism v0.9.1 + Cubism Native 5-r.5`（官方），
  一条 Ayagami（Rust）。它的价值不是代码，是**「可比」** —— 想知道开源那套行不行，这是最快的一手信号源。
  ⚠️ 路径写死 macOS、无 license、只是 demo。

### 3. 还有一个刚对准枪口的：`ayatsuri_2d`（★2 · Rust · GPL-3.0）

宣称端到端支持 **moc3 v3 到 v6**，自带 C ABI 让 Unity / UE / Godot / Python / JS 都能嵌入，自创 `.aom` 保存格式。
但它 README 自标 **status: Early**、★2、宣称**无第三方验证**、项目名疑似新号 → **只登记「有人在做」，不采信能力**。

> **两家的意义**：「moc3 兼容层」已经从「某人的怪念头」变成**开源阵营公认的必争点**。
> 这条线值得**每辑复查一次进度** —— 它是「不买 Editor 也能用现成 moc3 资产」唯一的现实出口。

---

## 四、主线二：Cubism Editor 的 External API 被第三方围建出一整簇

**背景**：官方 Cubism Editor 有本机 External API（**默认端口 22033**），2026 起第三方开始围它做插件 / agent / 工程管理，
且 **5.4 alpha 首次放出「编辑 API」样例（`04_EditSample`）**。索引此前只有零散的 MCP，**这一辑成簇了**。

| 项目 | 星 | 关键点 | 可复用性 |
|---|---|---|---|
| `turboism/Turboism`（Java · AGPL-3.0-only · 2026-10-08） | ★3 | **Windows 优先的插件框架**；支持表列出 **5.2.03 / 5.3.02 / 5.3.03 各配「精确版本适配器」** ← 这是「5.3.x 内部接口在变」的**第三方硬证据** | 参考（AGPL + ★3，先观察） |
| `pakholeung37/cubism-editor-computer-use`（Python · MIT · 2026-09-16） | ★0 | **官方 5.4 alpha「编辑 API」样例** + 补齐 `cubism_async/`（session / dispatcher / identity / specs） | 参考（抄它的**握手分层**） |
| `sena-nana/NanaBetterCubism`（Rust · MIT · 2026-09-07） | ★0 | 对话驱动改工程，所有结构编辑走 **preview → 确认 → 后端事务 → 回读验证** | 参考（抄**可回滚的 AI 编辑**模式） |
| `RainTrap341/cubihub`（Rust · MIT · 2026-03-21） | ★0 | **多版本 Cubism 的工程管理器**：自动扫描本机版本、绑定启动版本开项目、读写 **Mesh Preset**、**日志→问题摘要** | 参考（思路可借） |

**两条值得抄进自己项目设计的**：
1. **「可回滚的 AI 编辑」**（NanaBetterCubism）—— 用 agent 改美术资产，所有人的第一反应都是「改坏了怎么办」。
   它的答案是 `preview → 确认 → 事务 → 回读验证`，且可取消。索引里**此前没有任何条目给出这种范式**。
2. **「GUI-only 的工具，可以在文件层绕过界面」**（呼应 `inochi2d-toolkit`）——
   `yanjingzhaisun/inochi2d-toolkit`（★0 · MIT）用 CLI + MCP 对 Inochi2D 的傀儡格式做**文件级**读写，
   而不是模拟点击 UI。**文件级稳定可测，UI 级一改版就碎。**

> ⚠️ 四条全部依赖**正版授权的 Cubism Editor**；Turboism 明确声明「不分发 Editor、也不绕过其许可」。别误读成「免费替代」。

---

## 五、主线三：官方口径 —— **两处被推翻，一处退役可回滚**，外加 5.3.x 逐版补齐

### 1. ⚠️ 推翻上一辑：「5.4 无配套 SDK」不成立

- **上一辑**记的是「5.4 只有 Editor、没有配套 SDK」→ **错**。
- **本轮实证**：`cubism.live2d.com/link/manual5_4_alpha_sdk_en`（页面日期 **2026/07/14**，标题 **Live2D Cubism 5 SDK R7 alpha1**）。
- **官方术语澄清**（照抄手册）：**Cubism 5 SDK = 截至 R6；Cubism 5.4 SDK = 自 R7 alpha1 起。**
- **两个破坏性变更**（这一条比版本号本身重要）：
  1. **Change in Model Calculation Order** —— Unity SDK 的计算顺序改为与 Native/Web 的 Original Workflow 一致，
     结果是**涉及物理模拟的参数更新结果会与 R5 Official SDK 不同**（官方给了回退办法：替换 `CubismUpdateExecutionOrder.cs` 的常量）。
  2. **Json Version Tag Identification** —— SDK 开始识别 json 里的 Version tag，
     **带 R7 alpha 不认识的 Version tag 的 json 会加载不了**：`.model3.json` 报错且**不创建 prefab**；
     motion / exp / pose / physio / userdata / paramctrl3 各自降级（不创建对应组件）。
- **alpha 定位**：**限时评估版，不保证向 beta/release 迁移**；Parameter Controller 在 5.4 SDK 里 **alpha1 只支持 Unity**，其他平台 beta1 起。
- **论坛实报**：**Cubism Editor 5.4.00 alpha2 启动崩溃**（Creators Forum 2026-09-25，官方回复「调查中」）→ 现在别上。

> **钉子要按线写**：**Editor 线 = 5.3.04（正式）/ 5.4 alpha**；**SDK 线 = 5.3 系 R6 / 5.4 系 R7 alpha1**。
> 写成一个数就会自相矛盾 —— 这也再次印证「SDK 是**分线各自版本**」。

### 2. ⚠️ 推翻上一辑：`easy-live2d` 确实存在，且已 1.0.0

上一辑记「`easy-live2d` 各 registry 不存在、勿再追」→ **错**。本轮 npm registry 实取：**真实存在，最新 v1.0.0（2026-09-24）**。
（`github.com/Panzer-Jack/easy-live2d` 已在索引 [1196]，是**包与仓库两条线**被混淆了。）

### 3. ⚠️ 退役名单可回滚：`creatorsforum.live2d.com` 本轮 **HTTP 200**

上一辑记为 **403** → 判退役。本轮实测 **200**，并成功取到单帖（`/t/3983.json`，即上面那条 alpha2 崩溃帖）。
→ **官方论坛可用，从退役名单移除。**（**退役名单不是永久判决，要定期复测** —— 这条本身就是一个教训。）

### 4. 5.3.01–5.3.04 逐版补齐（连续两轮欠账）

**入口**：`docs.live2d.com/en/cubism-editor-manual/updates-history5-3/`（上一辑只读了大版本表，**没进过这个 patch 明细页**）。
**官方口径规律**：**beta1 写全套改动，正式版只写 beta 之后新增的修补** → 某版的实质内容要看它的 **beta1**。

| 版本 | 日期 | 实质内容（一句话） | 正式版正文 |
|---|---|---|---|
| **5.3.01** | 2026-02-24 | 修项目面板多选失效；新建 PSD 模型可选「Cubism 5.2 及更早的混合模式」 | 本版**无 beta** |
| **5.3.02** | 2026-04-02 | 网格编辑新增 **[Reset mesh]**（重置回初始态）+ 重叠顶点自动合并 | 只修「多 ArtMesh 改网格无法粘贴」 |
| **5.3.03** | 2026-06-16 | 参数面板 **[Subject to move]/[Move here]** 拖拽排序 + **Set all parameter values as default** + 网格 **[Paste in copied shape]** | **仅一句「移除 beta、发布正式版」** |
| **5.3.04** | 2026-09-03 | 日志面板可开新窗口、**物理组 tooltip 显示影响值**、Glue 编辑加笔刷形状与角度、导出参数 **[Clear GUID]** | 只修「拖拽时部件面板高亮色异常」 |

**对建模小白最值钱的两条**：**5.3.02 的 `[Reset mesh]`**（手工分网格搞坏了可直接重置，不用重导 PSD）与
**5.3.03 的参数拖拽排序**（新手最容易把参数顺序搞乱）。
**负结论**：**没有 5.3.05**，5.3.04 仍是最新正式版；官网新闻停在 **2026.07.17**（近 3 个月无新增）。

### 5. 顺手实测的两个数（本辑自己跑的，不是二手）

- **`moeru-ai/airi`（★50,267 · MIT · TypeScript · 推送 2026-10-11T06:31Z），待办①的答案在这里**：
  它的 Windows 安装包 `AIRI-0.12.0-beta.5-windows-x64-setup.exe` **733 MB、下载 17,038 次**（同 release 最大单项）。
  **它吃哪个 Cubism Core** —— 构建脚本 `@proj-airi/unplugin-live2d-sdk`（独立仓库 `proj-airi/unplugin-live2d-sdk` ★2 · MIT）
  在 `src/vite/index.ts` 里**硬编码**：
  `https://cubism.live2d.com/sdk-web/bin/CubismSdkForWeb-5-r.3.zip` → 取 `Core/live2dcubismcore.min.js`。
  → **结论：吃的是 Cubism SDK for Web 5-r.3**（不是 Unity 线的 R5/R4_2 —— 又一次印证「分线各自版本」）。
  → **预编译安装包已内含 Core，用户零配置**；但 Core 的**重分发条款仍归 Live2D**（airi 的 MIT 只覆盖它自己的代码）。
  → 渲染栈 = pixi（`@pixi/*`）+ 自研 `stage-ui-live2d` + `model-driver-magic-live2d`；2025-10 从 Tauri **迁到 Electron**。
- **Inochi2D 在 Windows 的真实门槛（待办②）**：
  ✅ `inochi2d` release tag **`nightly`（2025-09-18）提供 `inochi2d-win32-release.tar`** →
  **用 SDK 本体不需要 D 编译器**（只有「从源码构建」才要 LDC2 + dub）；✅ `inochi-creator`（★1242 · BSD-2-Clause）
  release `v0.8.6`（2024-09-18）提供 **`inochi-creator-win32.msi`（下载 24,511 次）**。
  ⚠️ **但编辑器停更约 1 年 4 个月**（发布版 2024-09 / 仓库最后推送 2025-06-16）——
  **「不买 Editor」路线的真实短板不是装不上，是编辑器停更。**

---

## 六、中文侧：AI 陪伴进了监管射程 + 皮套价目表被摊成可抄的表

### 1. ✅《人工智能拟人化互动服务管理暂行办法》—— **本辑对所有做本地 LLM 数字人的人最该知道的一条**

**2026-04-10 五部门公布（网信办 / 发改委 / 工信部 / 公安部 / 市场监管总局），2026-07-15 施行。**
本辑**多源交叉核实**：`cac.gov.cn` 官方解读（2026-06-03）+ 深圳市司法局 + 福州市数管局（转央视）+ 中青网，
四处一致；我自己又跑了一轮 WebSearch 复核。

| 要点 | 内容 |
|---|---|
| 适用范围 | 模拟自然人人格特征 / 思维模式 / 沟通风格，**且持续性情感互动**的服务；**智能客服 / 知识问答 / 工作助手 / 学习教育 不适用** |
| 未成年人 | **不得向未成年人提供虚拟亲属、虚拟伴侣等虚拟亲密关系服务**；未满 14 周岁须监护人同意；建立未成年人模式 |
| 身份提醒 | 须**显著提示用户正在与 AI 而非自然人互动**；发现过度依赖须弹窗动态提醒；**连续使用每超 2 小时**须提醒 |
| 行为红线 | 不得**过度迎合、诱导情感依赖或沉迷**；不得用情感操纵诱导不合理决策；须提供**便捷退出**、不得阻碍退出 |
| 数据 | 交互数据**非经单独同意不得用于模型训练**；除法定/同意外不得向第三方提供 |
| 门槛 | **注册用户 100 万以上 或 月活 10 万以上** → 须安全评估并报省级网信部门；首次引入**监管沙箱** |
| 前瞻 | 明确将「**研究制定数字虚拟人、智能体等相关规定**」← 对 VTuber / 虚拟人行业的前置信号 |

**对我们意味着什么**：把自己的桌宠接上「会哄人、有记忆」的本地 LLM 并**对外发布**，就已进入射程。
**纯自用不发布**不在管理范围（但同一批技术栈迟早要过这道门）。三条可直接抄成检查项：
**2 小时提醒 / 不得诱导情感依赖 / 数据不得擅自训练**。

### 2. ✅ 两张「皮套多少钱」的价目表（合起来才完整）

- **smzdm《从45.9元到4.5万差出1000倍》**（2026-08-11）—— 从 20+ 真实交易帖整理出 **6 档价格**：
  免费公皮 / ≤100元（45.9 元"包商"小豆人、60 元客单）/ 100–600 元（128 元商断成品、299 元 Q 版、388 元含商断、599 元小电人一条龙）/
  600–3000 元（600 定制、2199–2499 高精仅售一人、3K 高精私皮）/ 3000–10000 元（3500 限时直售、7000 二手急出可分期）/
  ≥1 万元（五位数代挂拍卖、**4.5 万顶配**、万元模型 + 中之人招募）。
  建模师公开价目：**Q 版 599/1199/2299，正比 1999/4999/9999**。另列 **4 笔隐性开支**：软件（VTS 免费）/ 面捕设备 / 后续维护 / **版权登记**。
  → **判据价值**：看到低价模型先问「为什么便宜」。
- **米画师橱窗 `stalls/120410`**（¥3,157 橱窗价 / ¥3,000 起套餐）—— **补上 smzdm 缺的「拆分」口径**：
  它卖的是**拆分立绘**不是建模。**原子报价**可直接比价：静态表情 **¥35–70/个**、动态 ¥35–100/个、手部 ¥150/只、
  完整换装 **¥1300–1500/套**；姿势加价：纯正面 ¥3000 < 微侧 ¥3300–3500 < 侧身 ¥3600–3900 < 侧身坐立 ¥4000–4500；
  画布 8000×10000px、**单件工期 30–60 天**、建议提前 2–3 月预约。
  ⚠️ **同站 `stalls/51760` 上一辑已收录** → 本条是**不同建模师、不同价目**，不是重复。
- **繁中两站（参考级，来源为中介站）**：`clibo.tw/commissions/eXNMf0`（NT$40,000–100,000 / 收款后两个月交 / **定金 NT$5,000 才排单**）；
  `tyaward.com.tw` 的 5 档精度表 —— 其中最有信息量的一条是「**要 CMO3 工程档 = 原报价的 4 倍**」，
  这解释了「只买 `.moc3` 会锁死后续二改」，**与授权链直接相关**。

### 3. ✅ 虎嗅/学术趴：Live2D 二十周年的官方数字（信息量最大的一篇）

**市占率 95%（VTuber 虚拟形象领域）· 采用 Live2D 的游戏与应用市场每年 350 亿人民币 · 软件月活 10 万 ·
个人/自由职业者制作销售流通总额每年超 3 亿人民币**（来源：《Live2D 20 周年发展历程之现状》，Live2D × 角川联合）。
商业节点：**2018 年与 Aniplex 达成资本/业务合作**；**2024 年与 OLM 合作《殿下与狗》成为首部几乎全篇 Live2D 制作的动画**；
**2027 年 1 月《风之继承者》将在日本 28 家电视台开播**（可跟踪的官方节点）。
创作者案例（方法论价值）：**脑水回**用「旋转变形器」做纵深视错觉，B 站播放超 60 万；
**卡米雷特**「扒官方手册学底层」→ 用二维图层模拟三维投影实现 360° 旋转、手搓逻辑门做加法器，获第 12 届 Live2D Creative Awards 模型大奖。

### 4. 🔶 降级采用的两条（AI 生成物，只取思路）

- **掘金《把 3D，live2d 模型放桌面…一款开源 Tauri 应用》**（2026-09-08，介绍 `guipie/pingyou`「屏友」）：
  拆解 **Tauri 2 + Vue 3 + Rust** 桌宠，Live2D 用 **`easy-live2d` + PixiJS**、3D 用 three.js；
  鼠标 IPC **16ms 节流**；Ollama 子进程用 `OnceLock<Mutex<Option<Child>>>` 只 kill 自己拉起的进程。
  **核心踩坑（对上面对 easy-live2d 的纠正）**：`easy-live2d` **不含** Cubism Core SDK，直接 import 报
  `Live2DCubismCore is not defined` → 须**动态从 CDN 加载 `live2dcubismcore.min.js`（官方/jsdelivr/unpkg 三重兜底）**。
  → 这与 airi 的做法是**同一个问题的两种解法**（一个构建期下载、一个运行期动态加载），**归到「闭源 Core 怎么合法引入」这一个知识点**。
- **TrueSight《VTube Studio 模型部署 SOP》**（2026-05-24）：⚠️ **正文顶部印着生成模型签名 `gemma-4-26b-a4b-it`** → 判为 AI 生成站。
  可取的排错点：纹理 **2K 主流**；`model3.json` **路径含中文/非 ASCII 会加载失败（白模）**；
  首次导入后生成 `.vtube.json`，**迁移必须一起拷贝否则调优参数全丢**；**VBridger 默认端口 8001**；
  iPhone 面捕**严禁 2.4GHz Wi-Fi**；**CPU 负载 >80% 面捕出现"粘滞感"**。
- **51CTO《从零搭建 Live2D 虚拟主播》**（2026-05-13）：`live2d-py` + MediaPipe + PySide6 + OpenCV 思路成立，
  但正文列了 `pyLive2D` / `Live2D-for-Python` / `bbb-live2d-py-v4` 等**在 PyPI 查无此包**的名字（疑为模板名）→ **工具名以 `live2d-py` 为准**。

---

## 七、⚠️ 编造 / 内容农场专区（本轮密度创新高：候选里**约七成**是模板站）

### A. 红牌术语复现（沿用上一辑术语表，直接定罪，无需重新论证）

| 例 | 原文声称 | 真相 |
|---|---|---|
| 西西软件园《Live2D Cubism Editor 5.1.00 中文最新版》 | **`MeshFitting` 自动网格优化**、**`ParameterMixer` 面板**、「AI 面部自动生成」、「AI 自动生成变形器」 | **四个词全是上一辑已定罪的红牌术语**，Cubism 无这些命名 |
| CSDN `weixin_30325487`《…导出 .pmx 文件的完整流程》 | 「勾选**包含物理模型(.pmx)**」 | **`.pmx` 是 MMD 格式**，Live2D 根本不导出 `.pmx` |
| CSDN `weixin_30800987`《…呆毛和头发跟随摆动》 | 物理参数写成「**摩擦力 / 反弹力**」 | 真实术语是 **质量 / 移动 / 阻力 / 弹性 / 重力方向** |

### B. AI 生成 / 农场站清单（见到直接剔）

- **同源 SEO 镜像农场族**：`hqwc.cn`（页脚"编程知识"）、`mhpq.cn`、`kwkr.cn`、`sheratonhq.com`、`live2d.net.cn` → 形态 ⑤ **见域即疑**。
- **英文 SEO 榜单农场**（连续两辑复现）：`wifitalents.com` / `zipdo.co` / `gitnux.org` / `saashub.com` / `magicmotionstudio.com`（自带 affiliate 声明）。
- **下载站/聚合站**（版本日志常自相矛盾）：`cr173.com`、`289.com`、`mfunz.com`、`cooco.net.cn`、`4570885.com`、`3dmplay.com.cn`、`jxxy.net`。
- **CSDN `weixin_29xxxxx/30xxxxx` 簇（8 个 ID，同题材同日）** → 形态 ⑥ **内容农场**，同一模板结构长文。
- **AIGC 推广号**：CSDN `gitblog_*` 正文挂 `utm_source=gitcode_aigc_v1` → 是**搬运改写**，非原创实测。

### C. 一条重要的判定**反例**（别误杀）

`hqwc.cn` 上的《零基础一晚上用 Live2D 做出会动的头像》**内容其实基本正确**
（「轴多少 ≠ 灵活度」「参数控制在 15–25 个」「MVV 最小可行」）—— 但**站点属镜像农场族**。
→ **按站剔除，不逐句采信**；其中「参数 15–25 个」这条思路可留个印象（**来源不可采，结论可参考**）。
**判定依据永远是「发布节奏 / ID 模式 / 同题材同日」，不是「我没听过」** —— 知识缺口不是虚构的证据。

### D. 本辑新判一条：**同一版本号、三个互斥的更新日志 = 二手拼凑**

`cr173.com` 称 VTube Studio **v1.32.71 (2026-02-18)** 含「20 款樱花主题 / 低光识别率提升 35%」；
`289.com` 与 `mfunz.com` 又写 v1.32.71 是「**7 月 22 日更新：Live2D SDK 更新至 4.2 版**」。
→ **同一版本号三个互斥日志 + 无官方出处 → 判为二手拼凑，本辑不采纳任何一条 VTS 版本结论。**
（official 路已核官方值：**VTS 官方版本 1.35.10（2026-07-08），以官方 Trello 为准**。）

---

## 八、索引与文档维护（本轮落盘）

| 项目 | 变化 |
|---|---|
| `index.html` | **1279 → 1301 项**（v37 增补 **22 卡**，脚注 **[1279]–[1300]**，分组 306 → **307**；div 11375/11375 平衡） |
| 增补脚本 | 新建 `insert_v37_cards.py`；跑前 `insert_guard_probe` 对 **v37 本身 6/6** |
| 经验帖存档 | `csdn-social-summary.md` 上一辑 → **`csdn-social-summary-v31.md`** |
| 房规 | `agent-house-rules.md` **200 → 189 行**（23 条不变）；维护纪律改为**压正文、不撤条款** |
| 闸门工具 | `insert_guard_probe.py` 修裸 sha 陷阱 + 新增 `--selftest`（7/7） |
| `index_metrics --update` | 已重封分组快照（307 个分组） |

**本轮卡片选材与复验**：gh 路报 27 条 + 5 条边缘登记 → 取 **22 条**入索引。
**主 agent 用 `gh api` 把 22 条的 ★ / 许可 / 语言 / 推送日全部重跑一遍**，与子 agent 汇报**逐条一致，零编造**。
（子 agent 报告不能直接采信 —— 这是房规；本轮按规矩做了。）

---

## 九、自测：收集到的 AI / 资源，哪些能直接改（只落地有信号的）

| 条目 | 自测结论 | 落地动作 |
|---|---|---|
| `Agent-desktop-pet`（Agent 状态→表情，9 状态，Windows 原生、只读本地不联网） | ✅ **真有用** | 本辑**唯一「明天可试装」级**；它把「编码 agent 的工作状态」当表情信号源，对天天盯 agent 跑任务的人几乎量身定做 → 列入下轮待办「实际装一次」 |
| `illust2psd` 的 `layer_taxonomy.yaml` 图层命名表 | ✅ 真有用 | 已抄进本辑结论；**不依赖它跑得起来**（它是 Alpha）也能立刻用这张表 |
| `NanaBetterCubism` 的 **preview→确认→事务→回读验证** | ✅ 真有用（模式） | 落成一条**通用做法**记入本辑 §四；适用于任何「让 AI 改文件」的场景，**已与我们自己的「改前改后各跑闸门」纪律同向** |
| `inochi2d-autorig-claude` 那句「Cubism 不能自动绑骨」 | ✅ 真有用（认知） | 落成**认知边界**：以后遇到「全自动绑骨」的宣称，先按此打问号 |
| `inochi2d-toolkit` 的「**GUI-only 工具可在文件层绕过界面**」 | ✅ 真有用（做法） | 记为通用做法；与本工作区「闸门放在真实执行路径上」是同一思路的两个方向 |
| `insert_guard_probe` 的「沉默失败」教训 | ✅ 真有用 | 已修 + 已配反例；并推广成一条：**闸门脚本自己要能被反例验证**（呼应房规 #33 / M-0020） |
| 5.4 alpha 两个破坏性变更 | ⚠️ 现在别碰 | **不落地** —— alpha 不保证迁移 + 论坛已报 alpha2 启动崩溃 → 写成**钉子**（下轮复核） |
| smzdm / 米画师 / tyaward 的价格数字 | ⚠️ 来源分级 | 只有 smzdm 与米画师是**正文已读**；tyaward 明确是**中介整理值**，已降级标注 |
| `easy-live2d` 不含 Core、须动态加载 | ✅ 真有用 | 与 airi 的构建期下载**归并成一个知识点**：闭源 Core 的两种合法引入方式 |

---

## 十、下一辑待办

**最高优先**
1. **实际装一次 `Agent-desktop-pet`**（本辑评出的「明天可试装」级），并核它的 THIRD-PARTY.md 许可边界。
2. **复查 `ayagami` 进度**（是否发出 crates.io 版本 / 是否支持表情与动作文件）—— 这条线是「不买 Editor 也能用现成 moc3」的唯一现实出口。
3. **`/skill-doctor`** —— **连续第十一轮**（照 `darwin-skill` 形状：列出没被用过的 skill + 评估→测试→保留或回滚）。
4. **实装 `moeru-ai/airi` 的 Windows 包**（733 MB）核一遍：预编译包是否真的零配置、Electron 迁移后 Tauri 版是否还在维护。
5. **核 `Inochi2D` 编辑器停更的真实影响**：v0.8.6（2024-09）的 MSI 在 Windows 11 上还能不能正常跑。

**闸门与记忆**
6. **`creatorsforum.live2d.com` 从退役名单移除**并写进 `AGENTS.md` §八 —— 同时立一条规矩：**退役名单要每 N 轮复测一次**，别把「上次 403」当永久判决。
7. 索引条目加「最后复核日期 + 是否作废」（`mistakes/` 已有；**1290 张卡没有**）—— 承接多轮未动。
8. `insert_guard_probe.py` 的 `--selftest` 接进「改 index.html 前必跑」的清单（目前靠人记得）。
9. 「命令可跑性」检查（R7 只查路径在不在，不查命令跑不跑得起来）。

**承接老账**
10. `rpycdec` 反编译自查（**欠十四轮**）· Codex `config.yaml` 纯离线 · `check_rpy_branches.py` · 词表落地 · 模型分档旋钮 · **`_tools/` 未入版本控制**。
11. **DSH 插件二轮评估**：若跟 dsh **先走 `dsh-win32` 原生 Windows 路线**；⚠️ **Session V3 不可回退，升级前先备份**。
12. 未登记候选池仍约 17 个 + 本辑新增（`cubihub` / `Turboism` 等已在索引，另 `live2drust` / `interactive_assistent` / `Godot-Live2D` 等边缘条目可下轮择机单列）。
13. `_tools/` 与 `AGENTS.md` 不在版本控制里 → 闸门全部无历史，待决定。

---

## 十一、搜索覆盖与去重报告（摘要）

| 路 | 覆盖 | 结果 |
|---|---|---|
| gh | 7 个子方向（替代栈 / PSD 流水线 / moc3 逆向迁移 / 运行时集成 / AI-Agent 桌宠 / Cubism Editor 自动化 / 边缘登记）；约 40 次单仓库 `gh api` 核实 | 立条 **27**（+ 5 边缘登记）；剔除已收录 **25+** |
| cn | 10 组检索式（**不用 `site:`**，站名当普通关键词） | 采纳 **16**（✅ 正文已读 6 / 摘要 8 / 弱信源 2）；剔除 **30+** |
| official | docs Release History **patch 明细页** / live2d.com 各页 / **Creators Forum（含 `/latest.json` 与单帖）** / GitHub org / npm registry / dev.to API / HN Algolia / esotericsoftware changelog / denchisoft + Trello | **21 条**（含 4 条 changelog + 2 条上一辑口径纠正 + 1 条退役回滚），**0 重复** |

**去重执行**：三路每条先 `grep -iF` 对 `_r32/_dedupe_gh.txt`（**1252 owner/repo**）+ `_r32/_dedupe_urls.txt`（**1396 URL**）
+ `index.html` + `csdn-social-summary.md` + `-v30` + `-v31` 比对。
**基线从 `index.html` 现取**（不用历史快照 —— M-0031：历史快照会把上一轮成果当新发现）。
**主 agent 复跑**：cn 路 24 条 URL **零命中**；gh 路 21 条 owner/repo **零命中**（全部新）。

**疑似同源但不确定（提请下轮复核）**：
- `daoming07280/live2d-auto-pipeline` ↔ `mw2wbyys6t-sudo/live2d-auto-pipeline` —— **同名不同 owner**，
  描述都指向「See-through + psd2live 全自动流水线」，极可能是同一作者账号迁移 → **只收了 `whale-maid-svg-layers`**。
- `empty-sekai/nnnotes-standalone` ↔ `MetaSekaiLab/nnnotes` —— 后者 ★15 活跃、前者 ★0 描述几乎逐字相同 → **只收后者**。
- `Open-LLM-VTuber` **三条中文踪迹**（gh 卡 / CSDN `gitblog_00677` / gitcode 推广镜像）→ **同源，别再各算一条**。

**负结论（别下轮再单独投入）**：
- **音频驱动口型（Audio→LipSync）专项：GitHub 零独立命中** —— 多被并入「LLM 语音助手/桌宠」整体项目；已成主干的不再单列。
- **HuggingFace / Gitee：零新制作工具** —— HF 上 Live2D 资源被塞进 LLM 数据集（如 `NopePrime/Open-LLM-Dataset` 内含 `shizuku.moc3`），**没有独立的 Live2D 模型/绑定数据集**；Gitee 侧全是多年前的看板娘 widget 与教程镜像。
- **无独立「许可证清单仓库」命中** —— 各项目的许可信息是分散写的，没有汇总仓。
- **HN / dev.to 在 Live2D 上仍是无料源**（HN `search_by_date` 2167 命中近一年全为误召；dev.to 标签存量仅 2 篇，最新 2026-06-08）。
- **`zhihu.com` / `bilibili.com` 正文仍全被登录墙拦** → 本轮无一条正文级证据；下轮建议改人工浏览器取帖。
- **`gamemale.com` 未投入**（上一辑已判 Cloudflare Turnstile 结构性退役）；**`creatorsforum.live2d.com` 本轮 200，可回滚**。
- **新增探测失败**：`theaic.io`（The AI Changelog）**HTTP 000**；`warudo.app` 是 SPA、正文 JS 渲染，取不到静态日志。

---

*本辑三路候选：gh 30 条 · cn 16 条 · official 21 条；落索引 **22 卡**；*
*累计经验帖约 1465 → **约 1490 条**；索引 **1301 项**；房规 23 条 / **189 行**；决策原则 23 条 / 224 行；mistakes **32 条**；*
*新建脚本：`insert_v37_cards.py`；新存档：`csdn-social-summary-v31.md`；*
***本辑最硬的一条：卡了六轮的「不买 Editor 就没有 moc3 渲染器」，第一次有人正面拆墙 —— 而且要盯住它（每辑复查进度）。***
