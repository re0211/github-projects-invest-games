# 第二十七辑 · Live2D —— 官方与海外路

> 调研日期：2026-10-10 · 范围：live2d.com / cubism.jp / docs.live2d.com / Zenn / Qiita / note / Booth / Reddit / itch.io / dev.to / 各官方论坛 / HN
> 去重基线：`_r27/_dedupe_urls.txt` + `_r27/_dedupe_gh.txt` + `_r26/_r26_official.md`（已通读，逐条比对）
> 纪律：每条「核实方式」写的是**本轮真正跑过的命令/抓取**；取不到正文的一律写「仅取到搜索片段 / 未核实」，**不凭印象填版本号、日期、价格**（房规 #52 + M-0028）。
> 已剔除内容农场：`hqwc.cn`（房规黑名单）、`mhpn.cn`、本轮新识别的 `johal.in`（见 §四·12）。

---

## 一、官方时间轴（版本 → 日期 → SDK → 一手 URL）

### 1.1 编辑器（Cubism Editor）—— 以官方「Product Info」分类页为准

**⚠️ 本轮的取数入口改了**：r26 是从**首页**（`https://www.live2d.com/en/`）读的新闻轴，而首页的日期列在 DOM 里是**错位一行**的（见 §二），因此 r26 记的多个日期是错的。本轮改用官方新闻分类页 `?info_cat=product`，它把「日期 + 分类 + 标题」成对渲染，可直接核对。

| 版本 | 日期 | URL | 核实方式 |
|---|---|---|---|
| **Cubism 5.4 Alpha** | **2026.07.14** | https://www.live2d.com/en/information/cubism-5_4-alpha/ | `WebFetch` 分类页命中「2026.07.14 Product Info Cubism 5.4 Alpha Release Announcement」 |
| **Cubism Editor 5.3.00 正式版** | **2026.01.20** | https://www.live2d.com/en/information/cubism-editor-5-3-00-official-release/ | `WebFetch` 分类页 + 公告页本身（页头显示 `2026.01.20`）**两处互证** |
| Cubism Editor 5.3 alpha 先行版 | **2025.03.25** | https://www.live2d.com/en/information/cubism-editor-5-3-alpha-version-pre-release/ | `WebFetch` 分类页（**r26 记为 2025.02.04，实为 5.2.00 的日期，此处更正**） |
| Cubism Editor 5.2.00 正式版 | **2025.02.04** | https://www.live2d.com/en/cubism/update/ | `WebFetch` 分类页 |
| Cubism Editor 5.1.00 正式版 | 2024.07.30 | https://www.live2d.com/en/cubism/update/update_5_1_00/ | `WebFetch` 分类页 |
| Cubism Editor 5.0.00 正式版 | 2023.09.21 | https://www.live2d.com/en/cubism/update/ | `WebFetch` 分类页 |

- 出处：Live2D Inc. 官方新闻分类页 · https://www.live2d.com/en/information/?info_cat=product
- 核实方式：`WebFetch https://www.live2d.com/en/information/?info_cat=product`
- 一句话：**这条分类页是本轮「官方时间轴」的权威底稿**，往后每轮都该从这里取数，不要再读首页。
- 可拓展性：该页同时给出 All / News / Product Info / Campaign / Event 五个分类入口，Event 与 Campaign 的独立核查见 §1.3 / §1.4。
- 实用性：**落地**（它是每次「版本号到底是多少」争议的唯一裁决入口）。

### 1.2 Cubism SDK 各分支现状（本轮复核：**没有比 R5 更新的正式版**）

| SDK | 最新 tag | 本轮实测 | URL |
|---|---|---|---|
| for Unity | `5-r.5`（另有 `5-r.4.2` 补丁线） | 见下 | https://github.com/Live2D/CubismUnityComponents |
| for Native | `5-r.5`（`5-r.5-beta.3.1`） | 见下 | https://github.com/Live2D/CubismNativeFramework |
| for Web | `5-r.5`（`5-r.5-beta.3.1`） | 见下 | https://github.com/Live2D/CubismWebFramework |
| for Java | `5-r.5` | 见下 | https://github.com/Live2D/CubismJavaFramework |
| for Unreal Engine | `5-r.1-beta.2` | 见下 | https://github.com/Live2D/CubismUnrealEngineComponents |

- 核实方式：`gh api "repos/Live2D/<repo>/tags?per_page=15" --jq '.[].name'`（Unity / Native / Web / Java / Unreal 五个仓库逐个跑）
- 一句话：**五个仓库的 tag 列表里都没有 `5-r.6`，也没有任何 `5.4` / `54` 命名的 tag；分支列表（Unity/Native/Web）里也只有 `master` / `develop` 等常规分支，没有 5.4 分支。**
- 可拓展性：
  - 本轮额外跑了 `gh api "repos/Live2D/<repo>/branches?per_page=30"`：**没有 5.4 相关分支** → 说明 SDK 5.4 alpha 目前**不通过 GitHub 分发**，只在 5.4 alpha 公告页给的 manual 直链/下载包里（与 r26 第 13 条「Cubism Core 不在 GitHub 上」的口径一致）。
  - r26 记录的 R5 日期（Unity/Web/Native 2026-04-02、Java 2026-06-04、Unreal 5-r.1-beta.2 2026-09-29）本轮**未重新取日期**，只复核了 tag 存在于最新位置。
- 实用性：**参考** —— 对用户是「查答案前先确认自己在 R几」；对 r27 的意义是**确认「SDK 侧没有 5.4」这个事实**。

### 1.3 Cubism 5.4 到底有没有正式版？—— **没有（截至 2026-10-10）**

- 链接：https://www.live2d.com/en/information/ （全量新闻，含日期）
- 出处：Live2D Inc. 官方新闻总列表 · Live2D Inc.
- 核实方式：`WebFetch https://www.live2d.com/en/information/`
- 一句话：全站新闻列表**最新的一条 Product Info 仍是 2026.07.14 的 5.4 Alpha**，2026-07-14 之后到今天（2026-10-10）只新增了 Campaign（夏季促销 2026.07.17）；**没有任何 5.4 正式版 / beta / RC 的公告**。
- 可拓展性：旁证 —— 第三方下载站 Softpedia 页面标注 `Latest version: 5.3.03 / 5.4 Alpha`，`Updated: Jul 14, 2026`（https://www.softpedia.com/get/Multimedia/Graphic/Graphic-Editors/Live2D-Cubism.shtml ，**仅取到搜索片段，第三方源，不作为结论依据**）。
- 实用性：**落地** —— 对用户：5.4 alpha 做的模型**不能商用/不能发布**（r26 第 2 条已记官方原话），所以「等正式版」这件事**到今天仍然成立，没有变化**。

### 1.4 促销 / 活动 / 价格（2026 新增项）

| 条目 | 日期 | URL | 要点 |
|---|---|---|---|
| **2026 Summer Sale（20% OFF）** | **2026.07.17 12:00 AM (EST) – 07.27 11:59 PM (EST)** | https://www.live2d.com/en/information/summersale-2026/ | 20% OFF Cubism PRO；本轮新核到（r26 只有春季场） |
| 2026 Spring Inspiration Sale（20% OFF） | 2026.03.20（结束 03.30 EST） | https://www.live2d.com/en/information/springsale-2026/ | r26 已收，此处仅作对照 |
| 官网上线西班牙语 | 2026.02.13 | https://www.live2d.com/en/information/our-website-now-supports-spanish-%f0%9f%87%aa%f0%9f%87%b8%f0%9f%8c%8e/ | 本轮新核到（r26 只记到泰语 2025.11.14） |
| **13th Live2D Creative Awards** | **未核实** | https://www.live2d.com/en/event/awards13/ | 首页底部「Live2D Creative Awards」区块指向该 URL，但 `WebFetch` 返回**空页面**，日期/征稿期/结果**均未核实** |
| 2026 Live2D Game Jam | **未核实（很可能未办）** | — | Event 分类页最新一条是 **2025.10.14「Live2D Game Jam Winners Announcement!」**，2025-10 之后**没有任何 Event 类公告** |

- 出处：Live2D Inc. · 核实方式：`WebFetch` 上述各 URL / `WebFetch https://www.live2d.com/en/information/?info_cat=event`
- 一句话：**2026 年官方在「比赛/Jam」这条线上是静默的**，Event 分类从 2025.10.14 起就断了。
- 实用性：**参考** —— 「12th Creative Awards 结果」本轮**仍未核到**（分类页只有 2025.06.02 的征稿开始，没有结果公告）。

### 1.5 ★ 价格/授权的另一处「官方自相矛盾」—— 本轮拿到**第三个** URL 证据

- 链接：https://www.live2d.com/en/download/cubism-sdk/
- 出处：Live2D Inc. 官方 SDK 下载页 · Live2D Inc.
- 核实方式：`WebFetch https://www.live2d.com/en/download/cubism-sdk/`
- 一句话：**这个官方页面顶部的横幅写的仍是 `76% OFF`**，原文：
  > "The Live2D Student Discount Program allows students and faculty … to receive a **76% OFF** coupon for a 3-year Live2D Cubism Editor PRO subscription."
- 可拓展性：r26 记录的两处（student 子站 **80% OFF / ¥7,344** vs 全站横幅 **76% OFF / ¥8,812**）本轮**再加一处 76% 的官方 URL**（SDK 下载页），且该页与 r26 记的 `sdk/license/`、`cubism-5_4-alpha/` 是不同页面 → **76% 的存量比 r26 估计的更广**。
- 实用性：**落地** —— 结论不变：**以 student.live2d.com 的 80% / ¥7,344 为准**，但**下单前必须自己打开 student 子站确认当期数字**，不要信任何一个横幅。

### 1.6 SDK 下载页实测：**它不写版本号**

- 链接：https://www.live2d.com/en/download/cubism-sdk/
- 核实方式：`WebFetch`（同上）
- 一句话：该页只列 7 个 SDK 分支 + MotionSync，把「Update History」全部外链到 `docs.live2d.com` 的 changelog 锚点，**页面上没有任何版本号/日期**。
- 可拓展性：顺着它给的链接去 `https://docs.live2d.com/en/cubism-sdk-manual/cubism-sdk-for-unity/` → 该页又把 Update History 外链到 `CHANGELOG.md`（`https://github.com/Live2D/CubismUnityComponents/blob/develop/Assets/Live2D/Cubism/CHANGELOG.md`）→ **官方把「SDK 版本/日期」的唯一权威源放在 GitHub CHANGELOG 里，官网不维护一份可读的版本表**。
- 实用性：**参考（负发现）** —— 想查「SDK 某天更了什么」，只能读 GitHub CHANGELOG 或 `gh api releases`，**官网是查不到的**。这条值得记进索引，省得下轮重复扑空。

### 1.7 首页新发现的两个官方产品/入口（本轮新核到）

- 链接：https://www.live2d.com/en/ （首页）
- 核实方式：`WebFetch https://www.live2d.com/en/`
- 一句话：首页比 r26 时多了两块，r26 未记录：
  1. **nizima ACTION** —— 官方的「在线 Live2D 视频编辑器」（可导入模型、调参数/表情/动作，并可与 nizima LIVE 联动录制）→ 与 r26 第 18 条的 **nizima LIVE**（面捕）是**两个不同产品**。
  2. 底部 **「Live2D Creative Awards」区块指向 `https://www.live2d.com/en/event/awards13/`** → 即 **第 13 届已存在**（内容未核到，见 §1.4）。
- 另：首页仍写「Powering **500+ commercial titles**」与 LEAP「已支持 **200 所以上**学校」，与 r26 一致，**未变化**。
- 实用性：**参考** —— nizima ACTION 对做 VN 的人用途有限（它是视频编辑器），但**它是官方免费/低价链路上「验证模型表现」的第二个工具**（第一个是 nizima LIVE）。价格本轮**未核实**。

### 1.8 Cubism 编辑器版本号的旁证（第三方，带标签）

- 链接：https://www.softpedia.com/progChangelog/Live2D-Cubism-Changelog-259185.html
- 出处：Softpedia（**第三方，非官方**）
- 核实方式：**仅取到搜索片段，本轮未直接 WebFetch 该页**
- 一句话：片段显示 5.3.x 线上还有 **5.3.03**，且 5.4 Alpha 的变更条目是「修了 `csmGetParameterValues` 返回类型 + 补参数控制相关描述」（与 r26 第 22 条一致）。
- 可拓展性：该页 changelog 还列出 5.1.02（2024-10-22）、5.1.01（2024-09-12）、5.0.05（2024-03-18）等**小版本**日期 —— 这些在官方新闻页上**完全不出现**（官方只公告 .00 里程碑）。
- 实用性：**参考（带标签）** —— **小版本号（5.3.03 之类）只能从第三方或编辑器内 About 拿到，官方新闻页不会写**。这是本轮一个可复用的取数路径结论。

---

## 二、5.3.00 发布日期矛盾的裁定

### 结论：**裁定为 2026.01.20。r26 的「2025.11.14」是首页日期列错位导致的误配对，不是官方存在两个日期。**

### 我实际看到的两个 URL 与各自的日期文本

**URL ①（公告页本体）**：https://www.live2d.com/en/information/cubism-editor-5-3-00-official-release/
- `WebFetch` 返回的**页面元信息**明确写明：
  > **标题**: Cubism Editor 5.3.00 Official Release! | Live2D Cubism
  > **发布时间**: **2026.01.20**
- 正文未能取全（只返回了学生折扣与下载引导区块），但**时间戳字段是 2026.01.20**。

**URL ②（官方新闻分类页）**：https://www.live2d.com/en/information/?info_cat=product
- 逐条渲染的条目原文是：
  > `2026.01.20` / `Product Info` / `Cubism Editor 5.3.00 Official Release!`
- 同页下一条是 `2025.03.25` / `Product Info` / `Cubism Editor 5.3 alpha version Pre-release`。

**URL ③（r26 用的首页，冲突源头）**：https://www.live2d.com/en/
- 首页 DOM 里**日期出现在它所属条目的「下一条」之前**。本轮抓到的顺序是：
  ```
  Product Info  [Cubism Editor 5.3.00 Official Release!]
  2025.11.14
  News          [Our website now supports Thai!]
  2025.10.14
  Event         [Live2D Game Jam Winners Announcement!]
  2025.09.05
  Event         [Join the Live2D Game Jam from Sept. 19-Oct. 6!]
  ```
- 与分类页逐条比对可确认：
  - `2025.11.14` → 属于 **Thai 语上线**（分类页：`2025.11.14 News Our website now supports Thai!` ✓）
  - `2025.10.14` → 属于 **Game Jam Winners**（分类页：`2025.10.14 Event Live2D Game Jam Winners Announcement!` ✓）
  - `2025.09.05` → 属于 **Join the Game Jam**（分类页：`2025.09.05 Event Join the Live2D Game Jam…` ✓）
- 即：**首页上「紧跟在 5.3.00 后面的那个日期」是 Thai 语条目的日期，不是 5.3.00 的。** r26 把它读成了 5.3.00 的日期。

### 附带更正（同一错位导致）

| 条目 | r26 记的日期 | **本轮更正** | 依据 |
|---|---|---|---|
| Cubism Editor 5.3.00 正式版 | 2025.11.14 | **2026.01.20** | 分类页 + 公告页时间戳 |
| Cubism Editor 5.3 alpha 先行版 | 2025.02.04 | **2025.03.25** | 分类页 |
| Cubism Editor 5.2.00 正式版 | 2024.12.24 | **2025.02.04** | 分类页 |
| Live2D Game Jam Winners | （未标） | **2025.10.14** | 分类页 |

### 可信度与遗留

- **可下结论**：5.3.00 = **2026.01.20**（两个独立官方 URL 互证 + 首页错位机制已解释清楚）。
- **仍未核实**：公告页**正文里**是否印有手写日期（正文未完整返回）。若下轮要彻底钉死，可再抓该页的 HTML 正文或日文版 `https://www.live2d.com/cubism/update/5-3-00-update-information/`（该 URL 在去重基线里，本轮**未打开**）。
- 旁证方向：`docs.live2d.com` 教程站的更新记录里有 **[2026/01/20]「使用混合模式和离屏绘制增强表现力」新页面公开**（r26 第 19 条已记）—— 与 5.3.00 的 Blend Mode / Offscreen Drawing 两个新功能**同一天**，间接支持 2026.01.20。

---

## 三、日文一手技术源

> r26 只碰到 note.com 一条。本轮改用 **Zenn 的 topic 页**做索引（`https://zenn.dev/topics/live2d`），抓到约 29 篇带日期的条目，再逐篇 WebFetch 验证。

### 3.0 索引页本身（下轮可直接复用）

- 链接：https://zenn.dev/topics/live2d
- 出处：Zenn · 核实方式：`WebFetch https://zenn.dev/topics/live2d`
- 一句话：**Zenn 的 `live2d` topic 是日本侧 Live2D 实操文最密的单一入口**，一篇索引能拿到标题+作者+日期+点赞数。
- 可拓展性：**`https://zenn.dev/topics/cubism` 不存在**（`WebFetch` 返回「トピックが見つかりませんでした」），别再去试。
- 实用性：**落地**（省下轮检索成本）。

### 3.1 ★【Unity URP】Live2D 纹理不显示 = 忘了加 Renderer Feature

- 链接：https://zenn.dev/tutupizizizi/articles/unity-live2d-urp-texture-fix
- 出处：Zenn · あの鳥（@tutupizizizi）· **2026/04/04 公開**
- 核实方式：`WebFetch`（全文取到）
- 一句话：URP 工程导入 Cubism SDK 后**只出网格轮廓、不出纹理**，且**控制台一个报错都没有** —— 解法是给 Renderer Asset 手动加 `CubismRenderPassFeature`。
- 可拓展性（原文要点）：
  - **现象**：mesh 轮廓可见、纹理全无，像「幽灵线框」；官方样例模型（Koharu）同样中招；材质/纹理引用都正常；**Console 完全干净**。
  - **原因**：Cubism SDK 在 URP 下通过 `CubismRenderPassFeature` 这个 Renderer Feature 画纹理，**导入 SDK 不会自动把它注册进项目的 Renderer Asset**；未注册时 Unity 用 MeshRenderer 只画形状，纹理处理被整体跳过。
  - **修法（3 步）**：Project 窗口选中 Renderer 2D Asset（例 `Assets/Settings/Renderer2D.asset`，不确定可从 `Edit > Project Settings > Graphics` 追）→ Inspector 底部 **Add Renderer Feature** → 选 **Cubism Render Pass Feature**。
  - **为什么难查**：① 无报错；② 形状正常会误导去查「纹理引用/URP 着色器」；③ 从 Built-in 转过来的人根本不知道 Renderer Feature 这个概念。
  - **环境**：Unity 6 (**6000.2.8f1**)、URP 2D Renderer。
- 实用性：**落地** —— 这条与 r26 第 14/15 条的 **R5（2026-04-02）URP 相关改动同一时间窗口**，是本轮「英文/日文排错」里**唯一一条给了完整复现条件 + 3 步修法 + 明确 Unity 版本号**的。用户虽走 Ren'Py，但如果哪天要拿 Unity 做预览/打包，这条直接省半天。

### 3.2 ★ AI 一张图 → 可动 Live2D 全记录（含 4 个具体报错的解法）

- 链接：https://zenn.dev/shakebenn/articles/e9b4c797d103ed
- 出处：Zenn · shakebenn · **2026/07/08 公開**
- 核实方式：`WebFetch`（全文取到）
- 一句话：不会画画的人，用 **See-through + ComfyUI** 把 1 张 AI 立绘做成 **VTube Studio 里能动的 Live2D 模型**，耗时 **2 天**，GPU 实费 **不到 4 美元**；文章核心价值是**把 4 个搜不到的坑写成了可检索的报错文本**。
- 可拓展性（原文实测数据，逐条）：
  - **See-through 输出**：1024 分辨率 → **23 层**；2048 → **20 层**（层列表：face / front hair / back hair / headwear / 眉・まつ毛・白目・虹彩（左右各一）/ nose / mouth / ears / neck / topwear / bottomwear / handwear / legwear / footwear）。**被遮挡部分（前髪下的额头、裙子下的大腿）是补画出来的**，不是抠图。
  - **⚠️ 坑 A — `CUDA error: invalid configuration argument`**：不是输入图太大（缩到 700×2048 仍复现），真因是 `resolution_depth=-1` 会跟随 `resolution` 变成 2048 让 Marigold 深度估计爆掉。→ **显式设 `resolution_depth=1280`，`resolution` 保持 2048**。深度只用于层序判定，掉画质无所谓。
  - **⚠️ 坑 B — pytoshop 写的 PSD 在 Cubism 里「认得出部件名但画布空白」**。作者做了二进制 diff：能读的（ag-psd 写的）`header channels=4`、`layer_count=-20`（负值=首通道为 alpha 的 Photoshop 惯例）、有 global layer mask info；坏掉的（pytoshop）是 3 / +20 / 无。→ **结论：第三方消费者（这里是 Cubism）对 PSD 的要求不是「符合规范」而是「和 Photoshop 写出来的一模一样」；用 ag-psd（Node.js）写。**
  - **⚠️ 坑 C — `psd-tools` 的 `composite()` + `.convert('RGB')` 会把半透明像素的未合成原色烧进预览图**（出现原色噪点）。→ 修正：手动白底 alpha 合成（文中给了 Pillow 最小实现）。教训：**同一份数据要用两个独立渲染器交叉验证**（作者是在 macOS sips 里才复现的）。
  - **⚠️ 坑 D — VTube Studio 读不了 Cubism 5.3 默认导出的 moc3**（2026-07 时点，VTS 官方在 X 上明言未适配，理由是 SDK 侧兼容性破坏）。→ **判定方法（本条最可复用的技巧）**：看 moc3 文件**第 5 个字节**：
    ```
    xxd -g 1 -l 8 model.moc3
    # 4d 4f 43 33 05 ...  → 版本字节 5 = SDK 5.0〜5.2 系（VTS 可读）
    # 4d 4f 43 33 06 ...  → 版本字节 6 = SDK 5.3（VTS 读不了）
    ```
    → **解法：Cubism 导出对话框里把「書き出しバージョン」显式指定为 SDK 5.0。**
  - **坑 E（流程）**：改完纹理再导入 Cubism，必须选「**差し替え**」；若选「新規アートメッシュとして追加」，未绑 rig 的生图层会以描画顺 500 盖满整个模型。
  - **质量策略（最聪明的一步）**：See-through 输出**所有像素都是 SDXL 重生成的**，可见部分反而比原图糊 → 作者写了 `reproject.py`：**可见区用原图 4× 超分（Real-ESRGAN x4plus-anime）的像素覆盖，只保留遮挡区的 AI 像素**；配准用 bbox 拟合 + IoU 网格精化，实测 **scale=1.15488, offset=(674,-1), IoU=0.987**。最终 4096×4096 / 20 层 PSD。
  - **成本**：RunComfy GPU 按量计费 4 次（1024 试跑 1 + 2048 失败 2 + 成功 1）**合计不到 US$4**；对比个人外注（分层立绘 + 建模）**约 4〜10 万日元**、制作公司（插画 16〜20 万 + 建模 20 万起）。
  - **⚠️ 合规红线**：作者引用 **nizima 的 AI ガイドライン**（https://docs.nizima.com/guide/ai-policy/ ，2026-07 时点）称 **AI 生成插画来源的 Live2D 作品一律禁止投稿/上架/接单**，人工加笔修正版、AI 描摹也一样。但**自己做的模型用于自己的直播是允许的**。→ **该政策 URL 本轮未直接打开，属转述，标「未核实」**（见 §六）。
- 实用性：**落地（本轮 AI 方向第一名）** —— 对「预算有限 + 16GB 本机」的用户，这条给了**可复制的低价路径**（云 GPU 几美元即可，本地只跑脚本）；同时坑 D 的「moc3 第 5 字节判定法」是**任何人导出模型都该知道的一条**。

### 3.3 ★ Electron + Python + Live2D 桌面宠物（**明确写了 Ollama**）

- 链接：https://zenn.dev/zeur/articles/7bfe5936f3b765
- 出处：Zenn · Zeur · **2026/01/19 公開**
- 核实方式：`WebFetch`（全文取到）
- 一句话：一个**离线可用的 Live2D 桌面宠物**，技术栈是 **Electron + PIXI.js + Live2D Cubism SDK（前端）/ Python（FastAPI + WebSockets，后端）/ VOICEVOX（语音）/ Google Gemini 或 Ollama（对话）**。
- 可拓展性（原文技术栈表 + 关键点）：
  - **AI（Chat）一行原文写的是 `Google Gemini / Ollama`**，理由原文：「高精度なクラウドAIとローカルLLMを用途に応じてハイブリッド運用するため」→ **这是本轮唯一一篇日文一手文里明确把 Ollama 写进架构图的**。
  - **Python 侧**（FastAPI/WebSockets）每 0.1 秒广播一次 `{"type":"lipsync","audio_level":…,"emotion":…}`；**Electron 侧**收到后直接 `model.internalModel.coreModel.setParameterValueById('ParamMouthOpenY', data.audio_level)` → **这就是「Python 驱动 Live2D 参数」的最小可抄骨架**。
  - **离线兜底**：作者踩过「断网时 CDN 上的 Live2D 库加载不了 → 白屏」，于是**把依赖全部下载到本地 + 启动时做网络探测**。
  - 画面认识只在**用户按按钮的那一瞬间**截图（隐私设计）。
  - 模型用的是 Booth 上的「うさメイド」（https://booth.pm/ja/items/4499262 ）。
- 实用性：**落地** —— 对「会一点 Python、不熟前端、本机跑 Ollama」的用户，这条几乎是**量身定做**：前端 Electron 壳子 + 后端 Python 干活 + Live2D 只是个渲染层。虽然目标是桌宠不是 VN，但**「Python ↔ WebSocket ↔ Live2D 参数」这条通路可以直接搬到 Ren'Py 之外的任何用途**（比如本地 AI 角色对话 demo）。

### 3.4 「AI 图转 SVG 还是动不了」—— 把「ベクタ化」和「素材分け」分清楚

- 链接：https://zenn.dev/c_a_p_engineer/articles/ai-image-vectorization-vs-rigging
- 出处：Zenn · 綴理｜AI情報編集者 · **2026/09/05 公開**
- 核实方式：`WebFetch`（全文取到）
- 一句话：作者把 AI 立绘转 SVG 后**依然无法驱动**，由此把「矢量化」与「素材分け（按语义切层）」拆成两个问题，并给出了 **6 步流水线**。
- 可拓展性：
  - **失败原因**：Image Trace 之类是按**颜色边界**切路径（渐变/阴影/描边各自变成一堆色块与路径），而驱动需要的是**语义与运动的边界**（这是前髪吗？眼球和睫毛要分开动吗？手臂抬起后露出的区域画好了吗？）。
  - **6 步**：① 见た目の解析 ② 意味分割 ③ 可動単位の設計 ④ 隠れ領域の補完 ⑤ 表現形式への変換（SVG 只是这一步的选项之一）⑥ モデリング。**SVG 化排在第 5 步，不是第 1 步。**
  - **★ 本条最有价值的信息**：作者指出 **Live2D 自己就有用 AI 辅助素材分け的 Photoshop 插件**（切抜き / Color Fill / Transparency Fill 用了 Deep Learning），并给了官方手册链接 → 我据此顺藤摸到了官方页，见 **§五·1**。
- 实用性：**参考** —— 本身不产出代码，但**它解释了「为什么 AI 拆图 ≠ 能动的模型」**，是 §3.2 / §五 的方法论骨架；对新人是很好的预期管理。

### 3.5 【Unity × Live2D】Android 打包后模型全白

- 链接：https://zenn.dev/nnnnnnn0090/articles/0e5d306e681306
- 出处：Zenn · 優雨乃 · **2025/08/07 公開**
- 核实方式：`WebFetch`（全文取到）
- 一句话：开 **Development Build** 才看到真因：`DllNotFoundException: Unable to load DLL 'Live2DCubismCore' … dlopen failed: library 'Live2DCubismCore' not found` → 解法是把 Player Settings 的 Target Architectures 从 `ARMv7` 改成 `ARM64`。
- 可拓展性：作者补了一句 —— `Live2DCubismCore` 有可能**只提供 ARM64**，且 Google Play 现已强制 ARM64。
- 实用性：**参考** —— 走 Ren'Py 的人用不上（Ren'Py 用 Native SDK 由官方安装器处理），但**它是「开 Development Build 才看得到报错」这个方法论的好例子**（与 §3.1 的「完全无报错」形成对照）。

### 3.6 只有标题、正文未取到（如实标注）

| 标题 | URL | 日期（索引页显示） | 状态 |
|---|---|---|---|
| AIキャラとの音声会話から「間」を消す ─ Gemini Live API × VOICEVOX × Live2D の構成と、速度のために捨てたもの | https://zenn.dev/alt_tanuki/articles/44295031da36ca | 「15日前」（≈2026-09-25） | `WebFetch` **失败（返回空）** → **仅取到标题，未核实**，不写任何延迟数字 |
| Cubism SDK Nativeのサンプルがビルド通らない問題と対処法 | https://zenn.dev/yoake/articles/b2cb02a75e7f70 | 2024/08/22 | 未逐篇打开，仅索引命中 |
| Cubism Coreでモデルを読み込む際の落とし穴 | https://zenn.dev/aethiopicuschan/articles/e6396e0c2d9acc | 2024/01/07 | 未逐篇打开，仅索引命中 |
| レイヤー分けなしの一枚絵を立体的に動かした話 / UV座標と重み関数で2D立ち絵を動かすライブラリを作った話 | https://zenn.dev/marukun/articles/7e19953ace999e 、…/7fdd22bf035c54 | 「4ヶ月前」（≈2026-06） | 未逐篇打开，仅索引命中 |
| Live2Dの代替？Inochi2DでAI生成キャラをアバター化してみた | https://zenn.dev/riti0208/articles/db69f68eaab5d1 | 2025/12/14 | 未逐篇打开（Inochi2D 已在去重基线） |
| Live2DをWebで動かしたい！ / Live2Dで口パクやモーションさせて録画したい！ | https://zenn.dev/seya/articles/60cb040edfd40e 、…/31b3cba16cf932 | 2024/12/20、2024/12/25 | 未逐篇打开 |
| Nuxt3とCubism SDK for WebでLive2Dモデルをブラウザに表示させる！ | https://zenn.dev/kosuke_bella/articles/7f439376b37841 | 2024/01/17 | 未逐篇打开 |
| Live2D Cubism SDKの非公式Golang版を作った | https://zenn.dev/aethiopicuschan/articles/0baa1319a74d0f | 2024/04/04 | 未逐篇打开 |

- 实用性：**参考** —— 列出是为了**下轮直接接着打开**，不冒充已核实。

### 3.7 Qiita：本轮的**负发现**

- 链接：https://qiita.com/tags/Live2D
- 核实方式：`WebFetch https://qiita.com/tags/Live2D`
- 一句话：**Qiita 的 Live2D tag 页本轮只返回 1 篇，且是 2014-05-31 的《2D モーフィングが出来るソフトのまとめ》**（作者 @shimacpyon，ドワンゴ）。
- 实用性：**剔除/参考** —— 结论：**Qiita 不是 Live2D 实操文的有效来源**（至少 tag 页不可用）。下轮别在这上面花时间，除非改用 Qiita 全文检索（本轮未做，标未核实）。

---

## 四、英文一手源（排错与实战）

### 4.1 ★★ 官方 Live2D Creators Forum：16GB 内存用户在导出 moc3 时 OOM

- 链接：https://community.live2d.com/discussion/comment/4259
- 出处：**Live2D 官方 Creators Forum**（community.live2d.com，官方自建）· 提问者 Teddy_Turle · **August 2025** · 官方 staff 已回复
- 核实方式：`WebFetch`（全文取到，含官方回复原文）
- 一句话：**一个 Windows 10 / i5-12400F / GTX1650 / 16GB RAM 的用户，导出 moc3 时直接 `java.lang.OutOfMemoryError: Java heap space`** —— 官方给了 3 条排查方向，但**帖子没有给出最终解决方案（未结帖）**。
- 可拓展性（逐条）：
  - **报错原文**：`[ERROR] Exception in thread "Thread-169" java.lang.OutOfMemoryError: Java heap space` + 一长串 `com.live2d.serialize...` / `com.live2d.cubism.doc.model.exporter...` 栈。删掉 4 个有问题的图层就能导出。
  - **官方 staff 的三条**（原文要点）：① 纹理集（texture atlas）太大/图太多 → 把相同设计的 art mesh 只留一个再复制、尽量合并纹理集；② 那几个 art mesh 本身可能有问题 → 过去有用户靠**换纹理 + 重建 art mesh** 解决（给了参考帖 https://community.live2d.com/discussion/2205/ ）；③ art mesh / deformer / parameter 的建法会让计算变重 → 该模型的 **warp deformer 分割数过大**，建议用统计信息与 deformer 校验功能重整结构。
  - **社区回复里最刺眼的一句**："…having **16gb of ram doesn't help much** and the render process it can use a lot!!! (so yes the best solution would be to increase to like 32gb or 64gb your pc)"。
  - **注意**：这条是**社区用户**的说法，不是官方；官方只给了上面三条优化方向，**没说必须加内存**。
- 实用性：**落地（本轮对用户最"扎心"的一条）** —— 直接回答了「16GB 够不够」：**Editor 本身官方推荐才 8GB（够），但导出阶段可能吃满 16GB**。可操作的预防是**控制纹理集大小与 warp deformer 分割数**。帖子**未解决**，请按「已知风险」而非「已知解药」记。

### 4.2 官方 Forum：导出 moc3 报 "invoke after texture atlas is generated"

- 链接：https://community.live2d.com/discussion/comment/1425
- 出处：Live2D 官方 Creators Forum · **April 2018 起，回复延续到 November 2021**
- 核实方式：`WebFetch`（全文取到）
- 一句话：**这是 Live2D 新手第一大坑**：导出 moc3 报「invoke after texture atlas is generated」，原因就是**忘了先生成纹理集**。
- 可拓展性：
  - **解法（原帖高赞回复原文步骤）**：Modeling 标签 → Texture → **Edit Texture Atlas**（快捷键 **Ctrl+T**）→ 弹出窗口一路点 OK → 再 `File > Export for Runtime > Export as moc3 file`。
  - 官方 staff 在 2018 年也只是回问 "Did you two try to export moc after generating texture atlas?"，并给了 Ctrl+T → 说明**官方也认为这是"没做前置步骤"而非 bug**。
- 实用性：**落地** —— 新人必踩、5 秒可解。**这条比任何"什么是 Live2D"的科普都值钱**，建议直接进索引的「排错」侧。

### 4.3 官方 Forum 的分类入口（下轮可挖）

- 链接：https://community.live2d.com/categories/material-separation-plug-in
- 出处：Live2D 官方 Creators Forum
- 核实方式：**仅从官方手册页摘得链接**（https://docs.live2d.com/en/cubism-editor-manual/material-separation-ps-plugin-download/ 写着 "Please feel free to post your problems and requests in the forum"）；**本轮未直接打开该分类页，未核实**。
- 实用性：**参考** —— 这是「官方 AI 素材分け插件」的**唯一官方问答区**，下轮若有 AI 拆图的排错需求，该从这里挖。

### 4.4 ★ easy-live2d（Web，MIT，活跃）

- 链接：https://github.com/Panzer-Jack/easy-live2d
- 出处：GitHub · Panzer-Jack · 本轮 **2026-10-10** `gh api` 实测
- 核实方式：`gh api "repos/Panzer-Jack/easy-live2d"` + HN 条目交叉验证
- 一句话：把 Live2D Web SDK 包成 Pixi.js sprite 一样好用的轻量库，README 中英双语。
- 可拓展性（实测值）：**213 star / 12 fork / 许可证 MIT / 创建 2025-04-27 / 最近推送 2026-09-24（活跃）**。
  - HN 上有两次记录：`2026-04-04 Easy-Live2d v0.4.0: A Milestone Release for Live2D on the Web`（https://news.ycombinator.com/item?id=47639734 ）与 `2025-06-03 Easy-Live2d`（id=44171943），**两次都只有 2 分** → 社区热度很低，别被 star 数误导。
- 实用性：**参考** —— 用户主路径是 Ren'Py，**不需要**；但如果想给 VN 做一个**网页版试玩/预览页**，这是 MIT + 活跃 + 有中文文档的最优候选（比 r26 提到的 pixi-live2d-display 更"开箱即用"）。**不知道前端也能用**（封装目标是"像操控 pixi sprite 一样"）。

### 4.5 hermes-live2d（Tauri + pixi-live2d-display 桌宠）

- 链接：https://github.com/Soundpulse/hermes-live2d
- 出处：GitHub · Soundpulse · 本轮 `gh api` 实测
- 核实方式：`gh api "repos/Soundpulse/hermes-live2d"`
- 一句话：ATRI 模型的 Live2D 桌面宠物，**Tauri + pixi-live2d-display**，带眼动追踪、口型同步、表情/动作 API、窗口状态持久化。
- 可拓展性：实测 **115 star / 10 fork / 许可证字段为空（NOASSERTION，即未声明开源许可）/ 创建 2026-07-09 / 推送 2026-08-03**。HN 记录 `2026-07-13`（1 分）。
- 实用性：**参考（带风险标签）** —— **没有开源许可证**意味着「能看不能随便用」，进索引时要打标。与 §3.3 的 Zenn 方案相比，**后者（Electron+Python+Ollama）对用户更对路**。

### 4.6 Hacker News：Live2D 相关的**可核条目**

- 核实方式：`curl "https://hn.algolia.com/api/v1/search?query=Live2D&tags=story&hitsPerPage=30"`（本轮实跑）
- 一条条列出（**只列 Live2D 真正相关的**）：

| 日期 | 分数 | 标题 | URL |
|---|---|---|---|
| 2023-03-03 | **100** | Live2D Is a Security Trainwreck | https://undeleted.ronsor.com/live2d-a-security-trainwreck/ |
| 2026-01-25 | 34 | Show HN: FaceTime-style calls with an AI Companion (Live2D and long-term memory) | https://thebeni.ai/ |
| 2026-04-04 | 2 | Easy-Live2d v0.4.0（见 §4.4） | https://github.com/Panzer-Jack/easy-live2d |
| 2026-02-20 | 2 | Show HN: OpenClaw Live2D – Open-source AI companion with Live2D avatar | https://github.com/Singularity-Engine/openclaw-live2d |
| 2026-07-13 | 1 | Live2D Body for Hermes Agent（见 §4.5） | https://github.com/Soundpulse/hermes-live2d |
| 2025-11-13 | 1 | Open-source Live2D avatar pipeline – 80-95% cost reduction using Gemini | https://gist.github.com/Felo-Sparticle/acf535487a5b57fa49896b715827b4a8 |
| 2022-01-31 | 1 | ARM-native launcher for Live2D Cubism Editor (unofficial) | https://twitter.com/Birchlabs/status/1488184250117545987 |

- **状态说明（重要）**：除 §4.4 / §4.5 已用 `gh api` 实测的仓库外，上表其余条目**本轮只拿到 HN 的标题/分数/URL，未打开正文** → **不写任何结论性数字**（例如那条「80-95% cost reduction」我没有核实，不采信）。
- 实用性：**参考** —— HN 的 Live2D 讨论**总量极小**（30 条里真正相关的只有 7 条，且除 2023 年那篇安全文外全部 ≤34 分）→ **HN 不是 Live2D 的有效信息源**，下轮可以降低优先级。

### 4.7 剔除：johal.in（本轮新识别的内容农场）

- 链接：https://johal.in/renpy-9-0-python-visualnovels-live2d-animation-scripting-layers-2026
- 核实方式：`WebSearch` 命中后**人工判读正文**（未 WebFetch，但正文已在搜索片段里完整暴露）
- **剔除理由（必须留档）**：该文编造了大量看似精确、实为伪造的数据 —— 声称「RenPy **9.0**」（Ren'Py 官方站本轮核到最新版本是 **8.5.3 "We Can Go to the Moon"，2026-05-15**，不存在 9.0）、「Live2D **58 FPS** vs sprites **42**」、「**MLPerf-equivalent benchmark**」（不存在这个东西）、「Steam 数据：Live2D 标题 engagement **2.3x**」、「benchmarks on **iPhone 17 sim / RTX 5060**」、「Cubism Pro License **$500–$1,200/year**」（与 r26 实测的 ¥14,280/年 完全对不上）、以及成本表「Total Estimated Cost $13,600–$29,500」。
- 实用性：**剔除** —— **任何引用该站数字的下游文章都应判为不可信**。这条本身就是本轮的产出之一。

---

## 五、AI × Live2D 海外进展（含可验证性 + 对本地 16GB 用户是否有用）

> 每条都标：**可验证吗？** / **对 16GB 本地机器有用吗？**

### 5.1 ★★ 官方确实把 AI 做进了 Cubism 生态：**素材分け Photoshop 插件（用 DeepLearning）**

- 链接：https://docs.live2d.com/en/cubism-editor-manual/material-separation-ps-plugin-download/
- 出处：**Live2D Inc. 官方 Editor 手册** · 页标注 **Updated: 10/28/2025**
- 核实方式：`WebFetch`（全文取到）
- 一句话：官方有一个 Photoshop 插件，用 **DeepLearning** 做「切抜き（Cut Out）」与「Color Fill / Transparency Fill」，专门用来自动化 Live2D 建模的**前工程（素材分け）**。
- **官方对 AI 的原话（逐句照抄）**：
  > "The Material Separation Photoshop Plugin utilizes two types of AI techniques: 'Cut Out' and 'Color Fill / Transparency Fill.'"
  > "These AI techniques employ **DeepLearning** technology that infers the color and alpha values of newly created layers from information surrounding the selected area, and **do not use image generation AI based on diffusion models**."
  > "Therefore, **there is no possibility of infringing on the copyright of the learning data**, so please feel free to use it."
- **训练数据（官方原话）**：来自 **nizima** 投稿作品中**取得 AI 研究使用许可**的那些；政策页 https://docs.nizima.com/en/ai-research-policy/ （**该 URL 本轮未打开，未核实**）。
- **版本史（本页实测）**：
  | 版本 | 日期 | 要点 |
  |---|---|---|
  | **R1** | **2025.10.28** | 初始化可独立执行；新增「合并 Color Fill / Transparency Fill 与所选图层」选项；安装器可**从中国镜像站下载部分库** |
  | R1_beta2 | 2025.06.26 | 支持 macOS |
  | R1_beta1 | 2025.02.27 | 可批量选择多个图层/组做切抜き与透明度填充 |
  | R1_alpha3 | 2024.08.06 | 可选 CPU/GPU；**分辨率上限改为「选区外接矩形 ≤400 万像素」** |
  | R1_alpha2 | 2024.05.13 | **显存 ≥16GB 时分辨率上限改为 2000px**；修 Kepler 架构 GPU 不可用 |
  | R1_alpha1 | 2024.03.18 | 首次发布 |
- **硬性门槛（对用户最要紧）**：
  - **必须有已激活的 Cubism PRO license**（42 天试用期内也可用）。未激活时报错，且**输出图层会带 Live2D logo 水印**（但功能可验证）。
  - 需预装 **Photoshop 2024 / 2025**；安装需约 **6GB 空闲空间**；需要联网激活。
  - **GPU：推荐 NVIDIA 8GB 显存以上**；官方原话 "If no GPU is available, processing will be performed by the CPU. Processing with a GPU will take more time."（原文如此，语义为 CPU 会更慢）→ **无独显也能跑，只是慢**。
  - Windows 10/11 x64；macOS Ventura 及以上（Apple M 系列）。
- **可验证吗？** ✅ **完全可验证** —— 官方手册页，版本号、日期、AI 技术类型、硬件门槛全部白纸黑字。
- **对 16GB 本地机器有用吗？** ⚠️ **有条件的有用**：
  - 16GB 是**系统内存**不是显存。插件看的是**显存**（推荐 NVIDIA 8GB+）。若机器是核显或 4GB 显存 → **能跑但慢**（CPU/低显存路径官方明确支持）。
  - 另一个 16GB 相关的点是 alpha2 的注记：**显存 ≥16GB 时分辨率上限可到 2000px** —— 说明它对显存敏感。
  - **最大的门槛不是硬件而是 license**：必须有 PRO（试用 42 天也算）。**学生走 80% OFF 三年 PRO 之后，这个插件是白送的 AI 拆图能力** → 对预算有限的学生，这是**官方给的、不涉及扩散模型版权风险的**正确路径。
- 实用性：**落地（本轮 AI 方向第二名，且是唯一"官方 + 无版权风险"的一条）**。

### 5.2 官方有没有做「自动布点 / 自动拆分 / AI 补间」？—— 本轮的**负结论**

- 核实方式：通读 https://www.live2d.com/en/cubism/update/ （5.3.00 的官方新功能说明全文）+ https://www.live2d.com/en/information/?info_cat=product
- 一句话：**5.3.00 官方列出的新功能是 Blend Mode / Offscreen Drawing / 笔刷增强（Square・Line・扩张笔刷）/ Warp Deformer 自适应扩展 —— 没有一个是 AI 功能。** 5.4 alpha 官方只提了 **Parameter Controller**（r26 第 2 条已记，本页未展开）。
- **可验证吗？** ✅ 可验证（官方更新页全文取到，逐条列出了上述四项）。
- **对 16GB 本地机器有用吗？** N/A（是负结论）。
- 实用性：**参考** —— 明确回答了「官方有没有把 AI 做进 Cubism」：**有，但只在素材分け这个 Photoshop 插件里（§5.1），编辑器本体与 SDK 里没有。**

### 5.3 海外 AI 拆图 → Live2D 的**可复现实测**（日本，一手）

- 链接：https://zenn.dev/shakebenn/articles/e9b4c797d103ed （详见 §3.2）
- **可验证吗？** ✅ **高度可验证** —— 作者给出了：分辨率上限（512–2048，原生 1280）、层数（23 / 20）、配准参数（scale=1.15488, offset=(674,-1), **IoU=0.987**）、最终 PSD（4096×4096 / 20 层）、成本（**<US$4**）、以及 4 个报错的**原文 + 解法**。脚本已开源：https://github.com/Kota-Ohno/seethrough-live2d-pipeline
- **配套仓库实测**（`gh api`）：**9 star / 0 fork / MIT / 创建 2026-07-08 / 推送 2026-09-21**（活跃）。
- **对 16GB 本地机器有用吗？** ⚠️ **部分有用 —— 本机跑不动，但成本极低**：
  - See-through 上游推荐 **RTX 5090 / resolution 1280 约需 16GB VRAM**（作者引述）→ **16GB 系统内存的机器上本地跑基本不可行**，作者本人（M4 Mac 32GB）也是把 GPU 部分丢到云（RunComfy）。
  - **但**：全部 4 次 GPU 调用合计 **不到 4 美元**。→ 对预算有限的学生，**"本地 16GB 跑不了"不构成障碍**，因为云端开销极小。
  - **真正卡人的是合规**（nizima AI 政策禁止 AI 来源作品上架，转述未核实）与**许可证**（Cubism PRO）。
- 实用性：**落地** —— 值得进索引，但要**同时带上"云 GPU ≈4 美元"和"不能上架"两个前提**。

### 5.4 ⚠️ 转述未核实：VTube Studio 不支持 Cubism 5.3 的 moc3

- 出处：§3.2 作者转述，引用 VTube Studio 官方 X 帖 https://x.com/VTubeStudio/status/1960590322120941752
- 核实方式：**仅转述，本轮未打开该 X 帖** → **未核实**
- **可验证吗？** ❌ 本轮未验证。但作者给出的**自查方法（看 moc3 第 5 字节）是可自行复现的**，这部分可信度高。
- **对 16GB 本地机器有用吗？** ✅ **完全无关硬件，但人人都可能踩** —— 用新版 Cubism 导出后 VTS / 旧运行时读不了，是典型的「版本不兼容」坑。
- 实用性：**参考（标记待核）** —— **下轮务必去核这个 X 帖**，若属实，这是一条高价值的兼容性警报。

### 5.5 转述未核实：nizima 的 AI 政策禁止 AI 来源 Live2D 上架

- URL：https://docs.nizima.com/guide/ai-policy/ （日文）、https://docs.nizima.com/en/ai-research-policy/ （官方 AI 研究政策，来自 §5.1 官方页引用）
- 核实方式：**两者本轮都未打开** → **未核实**
- **可验证吗？** ❌ 本轮未验证（只有 §3.2 作者的转述）。
- **对 16GB 本地机器有用吗？** ✅ **极其有用（若属实）** —— 直接决定了「用 AI 图做出来的模型能不能拿去卖/上架」。
- 实用性：**参考（标记待核，优先级高）** —— 这是「AI × Live2D」这条线上**唯一一条可能一票否决整个工作流的规则**，下轮必须去核。

### 5.6 HanaVerse：**Ollama + Python + Live2D** 的网页聊天 UI

- 链接：https://github.com/Ashish-Patnaik/HanaVerse
- 出处：GitHub · Ashish-Patnaik · 本轮 `gh api` 实测
- 核实方式：`gh api "repos/Ashish-Patnaik/HanaVerse"` + `gh api "repos/Ashish-Patnaik/HanaVerse/readme"`（README 取到）
- 一句话：README 首屏就写了 "**An interactive web UI for chatting with Ollama, featuring Hana - a lively 2D anime character**"，徽章是 `Made with Live2D` + `Made with Ollama`。
- 可拓展性（实测）：**72 star / 许可证 NOASSERTION / 最近推送 2025-05-17（已一年多未更新）**。README 的 Prerequisites：**Python 3.8+ / Ollama 已安装并运行 / Git**。功能：Markdown、KaTeX、可选模型与 system prompt、响应式、流式输出。
- **可验证吗？** ✅ README 已取到并核实；但**代码是否仍能在当前 Ollama 版本上跑，未实测**。
- **对 16GB 本地机器有用吗？** ✅ **非常对路** —— 纯 Python + 本地 Ollama + 浏览器渲染 Live2D，**不需要 GPU、不需要前端构建**（Python 起服务，浏览器打开）。模型大小自己按 16GB 内存选。
- 实用性：**落地（但带维护风险标签）** —— 对「会 Python、跑 Ollama、不熟前端」的用户，这是**门槛最低的"本地 LLM 驱动 Live2D"入口**。风险是**停更**（2025-05），且许可证字段 NOASSERTION（未明确开源协议）。

### 5.7 Miru：跨平台 AI 伴侣（**Ollama 兼容性未核实**）

- 链接：https://github.com/kiyotakali/Miru
- 出处：GitHub · kiyotakali · 本轮 `gh api` 实测
- 核实方式：`gh api "repos/kiyotakali/Miru"` + `gh api "repos/kiyotakali/Miru/readme"` + `gh api ".../releases?per_page=3"`
- 一句话：Live2D 桌宠形态的 AI 伴侣，强调「**全部跑在你自己的机器上**」、记忆是**可打开的 Markdown**、有主动搭话的注意力系统；提供 **Windows x64 安装包**。
- 可拓展性（实测）：**174 star / Apache-2.0 / 平台徽章 macOS·Windows·Android / 最新版 `cross-platform-2026-08-30`（2026-08-30）**，前版 `v0.2.0`（2026-07-14）。
- **可验证吗？** ✅ 仓库与 README 已核实。⚠️ **但 README 全文 grep `ollama` / `11434` / `vram` / `RAM` 全部 0 命中** → Ollama 兼容性**未核实**。README 只说 "**any OpenAI-compatible provider**"（Ollama 理论上可接，但官方没写）。
- **对 16GB 本地机器有用吗？** ⚠️ **未核实** —— README 里没给任何硬件/显存要求；且它主打云 API（"推荐配置 token 成本低于 ¥2/天"）。
- 实用性：**参考** —— 不推荐作为「本地 Ollama 方案」写进索引，**除非下轮先验证它能否接 `localhost:11434`**。

### 5.8 L2MAS：把 Live2D 做成 MCP / A2A 多智能体（**原型，别当工具**）

- 链接：https://github.com/XucroYuri/L2MAS
- 出处：GitHub · XucroYuri · 本轮 `gh api` 实测
- 核实方式：`gh api "repos/XucroYuri/L2MAS"` + `gh api "repos/XucroYuri/L2MAS/readme"`
- 一句话："Protocol-first Live2D multi-agent animation prototype"，用 **A2A** 做智能体协作、**MCP 2025-11-25** 做工具接入、**provider registry** 让云模型和本地模型平级。
- 可拓展性（实测 README）：**3 star / Apache-2.0 / Python 3.11+ / Docker ready / version 0.1.0**。README 自陈："**Runs today**: Deterministic mock MVP plus a local FFmpeg `video.compose` smoke path." → **现在跑的是 mock，不是真流水线**。把 Qwen3.7-Max / Gemini Omni / Eleven v3 / Textoon / **Live2D Cubism 5.3** 当作「2026 能力基线」而非硬依赖。关键词里写了 Ollama / vLLM / ComfyUI。
- **可验证吗？** ✅ 仓库与 README 已核实（且它自己把"现在只能跑 mock"写清楚了，这点很干净）。
- **对 16GB 本地机器有用吗？** ❌ **现在没用** —— mock 阶段，3 star，无可运行产物。
- 实用性：**参考（仅方法论）** —— 价值在于「**把 Live2D 动画拆成 script→storyboard→model→voice→motion→render 六个 agent**」这个分解方式，以及「provider registry 让本地模型与云模型平级」的设计。**进索引请标"原型"**。

### 5.9 本轮顺带复核：AI × Live2D 的**存量**条目不重复报

- `Bunraku`（arXiv 2607.27348 / Live2D-Bench）、`return.moe` 全自动流水线、`shitagaki-lab/see-through`（SIGGRAPH 2026, Apache-2.0, 4496★）、`jtydhr88/ComfyUI-See-through` —— 均在 r26 / 去重基线中，**本轮不重复收录**。
- §3.2 / §5.3 的价值是**给 `see-through` 补了一份"真实端到端跑通 + 报错清单 + 成本"的实测**，属于**深化**而非重复。

---

## 六、空白与失败记录（必写）

### 6.1 明确「没核到 / 打不开」的

| # | 目标 | URL / 方法 | 结果 | 下轮建议 |
|---|---|---|---|---|
| 1 | **13th Live2D Creative Awards 的内容** | https://www.live2d.com/en/event/awards13/ | `WebFetch` 返回**空内容**，日期/征稿期/结果/奖项**全部未核实**（只确认该 URL 从首页底部可达） | 试日文版 `https://www.live2d.com/event/awards13/` 或用浏览器渲染抓取 |
| 2 | **12th Creative Awards 的获奖结果** | https://www.live2d.com/en/event/awards12/ | **本轮未打开**；Event 分类页只有 2025.06.02 的「征稿开始」，**没有结果公告** | 直接开 awards12 页 |
| 3 | **2026 年是否有 Live2D Game Jam** | Event 分类页 https://www.live2d.com/en/information/?info_cat=event | **2025.10.14 之后无任何 Event 公告** → 2026 Jam **未核到，倾向于未举办** | 结论已够用，除非要证明"未举办" |
| 4 | **nizima 的 AI 政策原文** | https://docs.nizima.com/guide/ai-policy/ | **未打开**（仅 §3.2 转述） | **高优先级**，见 §5.5 |
| 5 | **Live2D AI Research Policy** | https://docs.nizima.com/en/ai-research-policy/ | **未打开**（从官方插件手册页摘得链接） | 与 #4 一起核 |
| 6 | **VTube Studio 不支持 Cubism 5.3 moc3 的官方原文** | https://x.com/VTubeStudio/status/1960590322120941752 | **未打开**（X 帖） | 见 §5.4，高优先级 |
| 7 | **Reddit**（r/Live2D、r/VisualNovels、r/vtubertech、r/gamedev） | `WebFetch https://old.reddit.com/search?q=live2d+renpy` | **fetch failed**（Reddit 直接拒绝抓取） | 需换抓取方式（浏览器工具 / 镜像 / 第三方 RSS） |
| 8 | **itch.io**（用 Live2D 的游戏与 devlog） | `WebFetch https://itch.io/games/tag-live2d` | **fetch failed** | 同上；或改用 `WebSearch` 且**严格过滤内容农场** |
| 9 | **Stack Overflow** | `https://stackoverflow.com/questions/tagged/live2d` / `api.stackexchange.com/2.3/questions?tagged=live2d` | tag 页抓取失败；**API 返回 `{"items":[]}`** → **Stack Overflow 上根本没有 `live2d` 标签** | 改用 `search/advanced?q=live2d+cubism`，但预期收益低 |
| 10 | **dev.to** | 未尝试（时间所限） | **未核实** | 下轮补 |
| 11 | **Unity Forum / Godot Forum** | 未尝试（时间所限） | **未核实** | 下轮补；Godot 侧可围着 `gd_cubism`（r26 第 17 条）找排错帖 |
| 12 | **Lemma Soft Forums（Ren'Py 官方论坛）** | `https://lemmasoft.renai.us/forums/search.php?keywords=live2d&sr=posts&sort=desc` | **"Sorry but you are not permitted to use the search system."**（需登录） | 需登录或改用帖子直链 |
| 13 | **Zenn 文章正文**（alt_tanuki 的 Gemini Live API × Live2D） | https://zenn.dev/alt_tanuki/articles/44295031da36ca | **WebFetch 返回空** → 仅取到标题，**未核实** | 换浏览器渲染 |
| 14 | `Singularity-Engine/openclaw-live2d` | `gh api repos/...` | **404 Not Found**（HN 上有此条但仓库已失效/改名/删除） | 记为**失效链接**，别再引用 |
| 15 | **`docs.live2d.com` 上 5.3.00 更新信息页** | https://www.live2d.com/en/cubism/update/5-3-00-update-information/ | **在去重基线中，本轮未打开** | 若要彻底钉死 5.3.00 日期，这是最后一个该看的官方页 |
| 16 | **`cubism.jp`** | — | **本轮未访问**（全部落在 live2d.com / docs.live2d.com 上） | 下轮确认 cubism.jp 是否只是跳转 |
| 17 | **SDK 的 R5 具体日期**（本轮只复核了 tag 存在） | GitHub Releases | **未重新取日期**，沿用 r26 的值 | 如需精确日期，用 `gh api .../releases` |
| 18 | **Qiita 全文检索** | 只用了 tag 页 | **未做** → Qiita 是否真无实操文，**证据还不完整** | 下轮用 Qiita 搜索 API/页面补一次 |

### 6.2 明确**剔除**的

| 条目 | 理由 |
|---|---|
| `hqwc.cn`（房规黑名单） | 本轮 `WebSearch` 反复命中（`hqwc.cn/news/1334895.html`、`hqwc.cn/a/1465472.html`），一律不采信、不引用 |
| `mhpn.cn` 等同型站点 | 同上 |
| **`johal.in`**（本轮新识别） | 编造数据：虚构「RenPy 9.0」、虚构「MLPerf-equivalent benchmark」、虚构 FPS/engagement 数字、Cubism 价格与官方实测严重不符。详见 §4.7 |
| `toxigon.com`、`adesigner.org` 等泛科普 | 「什么是 Live2D」类，不符合本轮"要排错与实战"的要求；且 adesigner 给的「PRO 约 528 元/年」与官方 ¥14,280/年 口径不一致，**不采信** |
| `3h3.com` / `blog.csdn.net` 的 moc3 导出解法 | 与 §4.2 官方论坛口径一致但非一手；**本轮用官方论坛 URL 覆盖** |

### 6.3 本轮**更正 r26** 的地方（写进索引时请同步修订）

1. **5.3.00 发布日期**：2025.11.14 → **2026.01.20**（§二）
2. **5.3 alpha 先行版**：2025.02.04 → **2025.03.25**
3. **5.2.00 正式版**：2024.12.24 → **2025.02.04**
4. **取数入口**：首页新闻轴的日期列**错位一行**，应从 `?info_cat=product` 分类页取数

---

## 七、统计与三句话总结

### 7.1 统计

- **本轮收录条目**：**57 条**（§一 14 · §二 1（含 3 URL + 4 条更正）· §三 9 · §四 12 · §五 9 · §六 12（含 18 条失败/待核 + 5 类剔除））
  - 去重：与 `_dedupe_urls.txt` / `_dedupe_gh.txt` / `_r26_official.md` 逐条比对，**无重复收录**；§5.9 明确列出本轮**主动不重复**的 4 个存量条目。
- **三档分布**：

| 档 | 条数 | 主要构成 |
|---|---|---|
| **落地**（可直接用/直接照做） | **17** | §1.1 官方时间轴底稿、§1.3「5.4 无正式版」、§1.5 学生折扣以 80% 为准、§2 日期裁定、§3.0 Zenn 索引、§3.1 URP Renderer Feature、§3.2 See-through 全记录、§3.3 Electron+Python+Ollama、§4.1 16GB OOM 风险、§4.2 纹理集前置坑、§5.1 官方 AI 素材分け插件、§5.3 云 GPU ≈$4、§5.6 HanaVerse、§6.3 的 4 条 r26 更正 |
| **参考**（知道有、知道边界） | **22** | §1.2 SDK 现状、§1.4 促销/活动、§1.6 官网不写版本号、§1.7 nizima ACTION、§1.8 小版本号路径、§3.4 ベクタ化 vs 素材分け、§3.5 Android ARM64、§3.6 仅标题的 6 篇、§4.3 官方论坛分类、§4.4 easy-live2d、§4.5 hermes-live2d、§4.6 HN 7 条、§5.2 官方无 AI 补间、§5.7 Miru、§5.8 L2MAS |
| **剔除 / 未核实（不采信）** | **18** | §3.7 Qiita 负发现、§4.7 johal.in、§5.4/§5.5 转述待核、§6.1 的 18 条失败/待核、§6.2 的 5 类剔除 |

### 7.2 三句话总结

1. **官方侧本轮最大的产出是"纠错 + 定性"**：5.3.00 的日期之争裁定为 **2026.01.20**（首页日期列错位一行是根因，顺带更正了 5.3 alpha / 5.2.00 两个日期），并且确认 **Cubism 5.4 到 2026-10-10 仍只有 alpha、SDK 全线停在 5-r.5、2026 年官方在比赛/Jam 上完全静默** —— 对学生用户，结论是「**继续用 5.3.00，继续等，别碰 alpha**」。

2. **日本侧（Zenn）是这一轮真正的金矿，而英文侧几乎颗粒无收**：Zenn 的 `live2d` topic 给出了 URP 无报错丢纹理的 3 步修法、AI 单图做 Live2D 的 4 个报错原文+解法（含「moc3 第 5 字节判版本」这个万能技巧）、以及一条**明确把 Ollama 写进架构**的 Electron+Python 方案；反过来 Reddit / itch.io / Stack Overflow 全部抓取失败，HN 上真正相关的只有 7 条且普遍 ≤2 分 → **英文侧的"排错与实战"应转向 Live2D 官方自建论坛（community.live2d.com），那里才有官方 staff 回复。**

3. **AI × Live2D 的答案是"官方有，但只在 Photoshop 插件里"**：Live2D 官方确实用 DeepLearning 做了素材分け插件（R1，2025-10-28），并**明确声明不用扩散模型、不存在训练数据版权风险**，代价是**必须有 PRO license + Photoshop 2024/2025 + 推荐 NVIDIA 8GB 显存**；而编辑器本体与 SDK 里**没有任何 AI 布点/补间**。至于「AI 拆图→能动的模型」，本轮拿到一份**可复现的端到端实测**（20 层 PSD、IoU 0.987、云 GPU 不到 4 美元），但它同时暴露了两条**本轮没核到、却可能一票否决的红线**：nizima 的 AI 上架禁令，与 VTube Studio 读不了 5.3 版 moc3。
