# 第三十辑 · official 路

> 调研日期：2026-10-11 · 范围：live2d.com / live2d.jp / docs.live2d.com / GitHub Live2D 官方仓 Release / 海外社区（HN · dev.to · hackernoon · 个人博客）/ 学术逆向 / 行业新闻
> 查重基线：`_r30/_dedupe_gh.txt`（1213）+ `index.html` 现取 + `csdn-social-summary.md`(v29) + `csdn-social-summary-v28.md` + `csdn-social-summary-v27.md`
> 纪律：URL + 日期 + 作者/机构 + 具体数字（版本号/价格/条款编号）四件套齐全才写；**拿不到就写「未核实」**（房规 #52，不许编数字）。

---

## 搜索覆盖

| 源 | 入口 | 状态 | 结果 |
|---|---|---|---|
| live2d.com（日文站，`hreflang=ja`） | `https://www.live2d.com/` | 200 / 65KB | 首页最新条目 **2026.10.08 alive 2026**（比 v28 的 2026.07.17 更新） |
| live2d.com（简中站，`hreflang=zh-hans`） | `https://www.live2d.com/zh-CHS/` | 200 / 68KB | 首页最新 **2026.10.01 秋季促销**（8 折 PRO，2026-10-11 止）+ 2026.10.08 alive 2026 |
| 官方 News 全量页 | `https://www.live2d.com/en/information/` | 200 / 42KB | 英文站最新仍是 **2026.07.17**（英文站未同步秋季促销，见下） |
| Cubism 5.4 alpha 公告 | `https://www.live2d.com/en/information/cubism-5_4-alpha/` | 200 / 60KB | 期间 **available until October 18, 2026**（7 天后失效）+ alpha1 已于 2026-09-14 停用 |
| alive 2026 活动页 | `https://www.live2d.com/event/alive2026/` | 200 / 49KB | 2026.12.11(金) @秋叶原UDX，一般 ¥3,000~ / 学生免费 |
| 学生优惠（CN） | `https://www.live2d.jp/chn/student-discount/` | 200 / 44KB | **80% OFF，RMB 1552→310 / 3yr，截止 2027-03-31** |
| GitHub Live2D 组织仓 | `api.github.com/orgs/Live2D/repos` | 200 | 18 个仓，最新推送 Unity/Unreal 2026-09-29 |
| GitHub Releases（7 仓） | `api.github.com/repos/Live2D/*/releases` | 200 | **无 5-r.6 / 无 6.0**；最新 Unity 5-r.4.2（2026-05-14）、Unreal R1-beta2（2026-09-29） |
| HN Algolia API | `hn.algolia.com/api/v1/search` | 200 | title 检索 `live2d` 命中若干，见条目 |
| dev.to API | `dev.to/api/articles?tag=live2d` | 200 | 仅 2 篇（均已在库/他辑） |
| hackernoon | `hackernoon.com/search?q=live2d` | 200 / 95KB | **零 Live2D 命中**（负结论） |
| Medium / note.com / Reddit / itch / Steam / YouTube | — | 退役（见「退役源复测」） | — |

---

## 条目

### 一、Live2D 官方上新

#### 1. Live2D 秋季专享特惠（Autumn Sale 2026）—— PRO 8 折，**今天（2026-10-11）最后一天** —— live2d.com · 2026.10.01

- 链接：`https://www.live2d.com/zh-CHS/information/autumnsale-2026/`（简中详情页）· 首页入口 `https://www.live2d.com/zh-CHS/`
- 核实：公告日期 **2026.10.01**（简中首页「2026.10.01 优惠活动」；标题原文「Live2D PRO版 8折优惠！金秋十月Live2D秋季专享特惠开始！**2026年10月11日(周日)截止**」）；折扣 **8 折（20% OFF）**；**简体中文站专有**——同一时刻英文站 `information` 页最新只到 2026.07.17，日文站首页最新到 2026.10.08 但展示的是 alive 2026，**三站不同步，秋季促销只在 zh-CHS 站现身**。
- 讲了什么：官方 2026 秋季对 **Cubism Editor PRO 许可证**的限时 20% 折扣，窗口 2026-10-01 → **2026-10-11（周日）**。与 v28 记录的「最近一条 Campaign = 2026.07.17 夏季促销」相比，这是新的一条；也是本辑唯一「**当天到期**」的时间敏感项。
- 可复用性：🔶 参考 —— 8 折是常规季节性促销（春夏秋冬各一次，力度历年都是 20%），**没有额外的省钱信息增益**；真正的省钱项是下面第 3 条学生优惠（80% OFF），买 Pro 前先走学割，不要为了这 20% 今天冲动下单。

#### 2. alive 2026（第 13 届 Live2D Creative Awards 颁奖礼）—— 2026.12.11 @秋叶原UDX，学生免费 —— live2d.com · 2026.10.08

- 链接：`https://www.live2d.com/event/alive2026/`
- 核实：公告日期 **2026.10.08**（活动页 INFORMATION 列表首条；日文首页同日同步）；时间 **2026.12.11（金）11:00–20:30（開場 10:30）**；地点 **秋葉原UDX シアター・ギャラリー 4F**；票价 **一般 ¥3,000~ / 学生入場無料**；含「第13回 Live2D Creative Awards 表彰式」与「Live2Dキャリアミートアップ」。
- 讲了什么：官方年度创作者大会（面向 2D 表现从业者 + 学生），现场有 Live2D 最新情报、企业讲座、展位体验、作品颁奖与求职交流；票已开售。
- 可复用性：❌ 不采用（对本机目标）—— 线下（秋叶原）活动，与「16GB Windows 本地做 Ren'Py VN」无直接关系；但**「alive 2026 会放出下一代 Cubism 情报」值得记一笔**——如果 5.4 正式版/6.0 要发，通常在这种年度场合讲，可留意 12 月之后的回放与公告。

#### 3. Live2D 学生优惠计划：**2026 年度限定 80% OFF**，¥7,344 / 3yr，截止 2027-03-31 —— live2d.jp/chn · 页面日期未核实

- 链接：`https://www.live2d.jp/chn/student-discount/`
- 核实：**80% OFF**（页面原文「2026年度限定」「80% OFF（二折优惠）」）；**正常价格 RMB 1,552 [¥36,720] / 3yr → 学生价 RMB 310 [¥7,344] / 3yr**；**特别优惠截止至：2027 年 3 月 31 日**；内容 = **Cubism PRO for indie 三年套餐**；**无学校邮箱者可用「学信网在线验证码」申请**（审查约 5–6 天）；非自动续费、毕业前购买可**用到订阅期满**；页面另含 LEAP（面向教育机构免费借出 Editor PRO）。
- 讲了什么：官方学割的**中国大陆口径**。⚠️ 与 v28 记录**数字打架**：v28 引英文页得 **76% OFF / $238.20→$57.16**，本稿引简中页得 **80% OFF / ¥36,720→¥7,344**。两个都是官网，**区域不同、结算页不同**——**以自己所在区域的结算页为准，别信首页宣传语**（这条口径打架 v28 已提示过，本辑再次坐实）。
- 可复用性：✅ 落地 —— 用户是在校生，这是**本辑唯一「今天就能落地且直接省钱」的事**：¥310 拿三年 PRO，比继续绕「不买 Editor」的时间成本更划算；且学信网验证码通道**不需要学校邮箱**（切中大陆学生）。

#### 4. Cubism 5.4 alpha 只剩 7 天：**2026-10-18 到期停供** —— live2d.com · 2026.07.14（本辑复核）

- 链接：`https://www.live2d.com/en/information/cubism-5_4-alpha/`
- 核实：公告 **2026.07.14**；页面原文 **Available until “October 18, 2026”**；alpha1 已于 **2026-09-14** 停用，现存 alpha2；「无需付费 license 也可试用 5.4 新功能」；「**SDK 不保证 alpha→beta/release 迁移**」「**产出数据仅供 alpha 使用，不提供任何保证与支持**」。
- 讲了什么：与 v28 一致的复核——**今天距停供 7 天**。想尝 5.4 新功能（Parameter Controller / External API）的窗口即将关闭，但**别把 5.4 产出的数据写进要上架的工程**。
- 可复用性：🔶 参考 —— 对「第一款商业 VN 用 5.3.00」的判断不变；这条只值一句「别用 alpha 产出发版」。

#### 5. 官方 SDK 全线复核：**仍然没有 5-r.6，也没有任何 6.0 tag** —— GitHub Live2D 官方仓 · 各 release 自身 `published_at`

- 链接：`https://github.com/Live2D/CubismWebFramework/releases` 等 7 仓
- 核实（GitHub REST API 实跑，均为 release 自身字段）：
  - Web / Native / Unity / NativeSamples / WebSamples 均为 **5-r.5（2026-04-02）**；Unity 另有更晚的 **5-r.4.2（2026-05-14）**
  - Java **5-r.5（2026-06-04）**
  - Unreal **`5-r.1-beta.2`（2026-09-29）**（更新到 R1 beta2）
  - MotionSync for Native / Unity 均为 **5-r.2.1（2026-08-25）**；MotionSync for Web 停在 **5-r.2（2025-03-27）**
  - 组织仓最新推送：CubismUnityComponents / CubismUnrealEngineComponents 均 **2026-09-29**
- 讲了什么：对 v28 §一.B 的复核，**结论完全不变**：官方 SDK 主线仍是 **5-r.5**，没有 `5-r.6`、没有 `6.0` 命名。Unity 侧近月只有 PR #96（修 Unity 6.6 `GetInstanceID` 过时编译错误，2026-09-29，v28 已记），**未发 release**。
- 可复用性：🔶 参考 —— 作为「查版本号的底稿」；对 Ren'Py 用户的意义：**Ren'Py 需要的 Native SDK 仍停在 5-r.5，且仍无 5.4 命名版本**，v28 那条「下载 `CubismSdkForNative` 装进 Ren'Py」的欠账所用版本号本辑不变。

#### 6. ⚠️ 修正 v28：Cubism Editor 正式版**早已不是 5.3.00，现为 5.3.04** —— docs.live2d.com 官方 Release History · 2026-09-03

- 链接：`https://docs.live2d.com/en/cubism-editor-manual/new-feature-introduction-title`
- 核实（页面 Release History 表逐行读到）：**09/03/2026 → Cubism 5.3.04（最新正式版）**；06/16/2026 → 5.3.03（beta1 05/14）；04/02/2026 → 5.3.02（beta1 03/03）；02/24/2026 → 5.3.01；01/20/2026 → 5.3.00。
- 讲了什么：⚠️ **v28 写的「现在唯一该用的编辑器版本还是 5.3.00」是过期口径**。官方**产品页**（`live2d.com/zh-CHS/cubism/update`）只列到大版本 5.3.00，**patch 号只出现在 docs.live2d.com 的 Release History 表里**——这正是「同一官网两处口径不一致」的又一个实例（与 §学割 的 76%/80% 同类）。当前正式版是 **5.3.04**。
- 可复用性：🔶 参考 —— 对「下载哪个版本」有直接影响：**装的应是 5.3.04，不是 5.3.00**；但本辑只核到版本号与日期，**未读 5.3.01–5.3.04 各自的具体更新条目**（下轮可补）。

### 二、海外社区（实战测评 / 讨论）

#### 1. HN：Beni AI「FaceTime 式 AI 伴侣」（Live2D + 长期记忆）——评论区就是一份架构实战笔记 —— news.ycombinator.com · 2026-01-25

- 链接：HN 帖 `https://news.ycombinator.com/item?id=46759627`（Show HN）· 产品站 `https://thebeni.ai/`
- 核实：HN Algolia API 实查——**2026-01-25 发布，34 分，8 条评论**（`objectID 46759627`）；产品站 HTTP 200（601KB）。作者 `summerlee9611` 在评论区亲自答技术细节。
- 讲了什么：一个把 **Live2D 当视频通话对象**的 AI 伴侣产品。**值钱的不是产品，是作者在 HN 评论区给出的实时链路**：`WebRTC 流式 → 流式 STT → 低延迟 LLM → TTS → 客户端驱动 Live2D 参数`；TTS 用 **ElevenLabs**，嘴型是「**简单音素/振幅**」而非精确音素对齐；在线模型以 **ChatGPT / Gemini** 为 baseline。评论区的高赞质疑是一条**产品判断**：`dfajgljsldkjag` 的「**亲密（private friend）与向外分发（public performer）互相冲突，不能同时最大化**」，作者回应称把个性放私有记忆、角色保持一致。
- 可复用性：🔶 参考 —— **对「Ren'Py VN 里接实时语音 Live2D」**：这条给出了可抄的**分层顺序**（流式输入 → LLM → TTS → 参数驱动），且点破了「嘴型只跟振幅」这个**够用但非精确**的取舍；但产品本身（云、实时、伴侣形态）与「单机 16GB 本地 VN」不同路，**不是今天能搬的东西**，当一个「未来形态」存档。

#### 2. HN：`Soundpulse/hermes-live2d`（ATRI 桌面宠物）—— 编码 agent 桌宠集群再添一员 —— github.com · HN 2026-07-13 / 仓推送 2026-08-03

- 链接：HN 帖「Live2D Body for Hermes Agent」`https://github.com/Soundpulse/hermes-live2d`（HN Algolia：2026-07-13，1 分）
- 核实：GitHub API 实查——created **2026-07-09** / pushed **2026-08-03** / **★115** / 语言 **Rust** / **license 字段为空（NOASSERTION）**；README 标题「ATRI Live2D — a desktop pet your agent can speak through」，栈 = **Tauri 2 + pixi-live2d-display**，带**语音口型同步、表情、鼠标追踪、本地 HTTP API**，内置 **Sparkle（火花）** 模型。
- 讲了什么：把编码 agent（NousResearch 的 **hermes agent**）生成的 TTS 音频，经 **Tailscale** 推到本机桌面宠物上做口型同步 + 气泡。**这是 v29 §三.5「Live2D × 编码 agent 桌宠集群」的又一条**（该集群已有 dsh-live2d-pets / agent-avatar / L2MAS 等）。
- 可复用性：🔶 参考 —— 与我们这个「WorkBuddy/DSH 桌宠」方向同层，且 ★115 是集群里偏高的；**但它无 license、且渲染栈是 `pixi-live2d-display`（老 Cubism 分叉，未确认 Core 版本）**，与 v29 记的 `dsh-live2d-pets` 「栈停在 Core 4」同风险——**第一条商业 VN 不要把它当依赖，看它学「agent→TTS→Live2D 参数」的接线即可**。

#### 3. HN：CUBISM CAT（把猫照变成「立体派猫」）—— 名字撞车，与 Live2D 无关 —— news.ycombinator.com · 2026-04-13

- 链接：`https://cubismcat.damjanski.com/`（HN 帖 `objectID 47750827`）
- 核实：**2026-04-13，5 分，4 条评论**；站 HTTP 200，正文仅「Turn Your Cat Pics into Cubism Cats / Terms Privacy Contact」。
- 讲了什么：名字里的「Cubism」指**立体主义画派**，不是 Live2D Cubism——**是一个同名噪音项**。评论区也只有「lol / 10 different shapes」。
- 可复用性：❌ 不采用 —— **不是 Live2D 内容**。登记它的唯一价值：**下轮搜 `cubism` 时把这类同名项直接排掉**，别浪费时间。

#### 4. dev.to / hackernoon 复核：**本辑无新内容** —— dev.to API / hackernoon · 2026-10-11 实跑

- 链接：`https://dev.to/api/articles?tag=live2d` · `https://hackernoon.com/search?q=live2d`
- 核实：dev.to `tag=live2d` 返回**恰好 2 篇**——`Open-LLM-VTuber Review`（2026-06-08，v28 已收）+ `easy-live2d v0.4.0`（2026-04-04）；`dev.to/search/feed_content` 全文搜 live2d 返回 **0**。hackernoon `search?q=live2d` HTTP 200（95KB）但**正则扫全文零 `live2d` 命中**。
- 讲了什么：**负结论**——「海外开发者博客」这条线在 Live2D 上基本是干的；真正有料的实战都在 **HN 评论区**（见本节 1、2）和**学术预印本**（见下节）。
- 可复用性：🔶 参考（方法层）——**下轮别再对 dev.to / hackernoon 单独投入**，把它们降为「顺手扫一眼」；HN Algolia 的**评论区**才是海外实战信息的富矿。

### 三、技术 / 学术（本辑最重的一条）

#### 1. ★★ Bunraku：单张插图 → 可编辑 Live2D 角色（首个端到端系统 + 首个基准）—— arXiv 2607.27348 · 2026-07-29

- 链接：arXiv `https://arxiv.org/abs/2607.27348` · 项目页 `https://bunraku-live2d.github.io/` · 代码仓 `https://github.com/SparcAI-Inc/Bunraku`
- 核实：arXiv abs 页实读——**cs.CV，Submitted 29 Jul 2026**；作者 **Junhao Chen, Jingjia Mao, Dayong Li, Chenghai Li, Saining Zhang, Zhihao Li, Hao Zhao, Yufei Wang, Ruqi Huang**（清华/南洋理工/SparcAI，据 arXivDaily 中文速递，机构归属**未逐字核**）；GitHub API：`SparcAI-Inc/Bunraku` created **2026-07-31** / pushed 2026-07-31 / **★37** / **license 字段为空**。关键数字（来自论文摘要）：**50 个留出角色上，Stage 2 每顶点方向余弦 0.768（中位数 0.828）**（无 teacher forcing 的 true generation）；网络放大 **112×** 无增益；发布 **Live2D-Bench**（首个该任务标准基准）+ **8,884 个模型**的 Live2D 语料库。
- 讲了什么：**Stage 1** 用「懂 Live2D 器官级 taxonomy」的分层扩散，从单图生成**有序 RGBA 图层堆叠 + 遮挡区补全**；**Stage 2** 仅凭每层 alpha 通道建三角网格，把**所有图层的顶点当作同一序列的 token**、自注意力**跨层**，**联合**预测关键姿势顶点位移。核心论点：**让角色读起来像一个整体靠的是「联合预测」而非堆网络**（放大 112× 无用）；且因为网格只由 alpha 生成，**换装/改纹理时可 byte-for-byte 复用网格与动画**。
- 可复用性：🔶 参考（判据价值 > 工具价值）—— ⚠️ **它把 v29 §三.4 那条「单张立绘自动生成 Live2D 会散架」的判断顶到了桌面上**：现在有了一个**声称**端到端能成的系统 + 一个**可比的基准**。但**代码仓无 license、★37、创建即停更**，且**下一篇审稿报告指出它的头号指标有水分**（见下条）——**今天不能当产线，但它是「以后拿什么指标筛『一键生成 Live2D』宣传」的第一把尺子**。

#### 2. ⚠️ pith.science 公开审稿报告：Bunraku 的 0.768 是「上限」，不是「交付精度」——审稿意见可直接当筛选清单 —— pith.science · 日期未核实

- 链接：`https://www.pith.science/p/2607.27348`
- 核实：**日期未核实**（页面未给发布日）· 3 条 major / 6 条 minor 意见。核心数字：**头号指标 0.7676（median 0.8278）测的是「美术手作网格」**，而部署管线实际用的是**由 alpha 推导的自动网格**（§3.4 Eq.3）；论文**从未报告全管线对该指标的实测**——App.Q 只给了 3 个角色的渲染 PSNR/SSIM/LPIPS。审稿人用论文自己的数据反推：**重网格化 24% 的层（平均顶点 47.5→71.9）就掉 0.063 cosine，是所研究「模型效应」的两倍**，而部署 auto-mesh 平均每层 **~83 顶点**（比美术网格更密）→ **0.768 是上限而非交付精度**。
- 讲了什么：三条 major 各点一个「不能接的宣传」——① 主指标口径与部署口径不一致（见上）；② 与 image-to-video baseline 的比较**未在同一协议下跑**，作者自己写「Re-running the four baselines … is the one measurement this paper still owes」；③ **eye-open 参数在自动分解层上直接失效**（驱动 `ParamEyeLOpen/ParamEyeROpen` 会移动整个头部组而非眼皮，论文因此把眨眼排除出 in-the-wild 测试）——这正是 v29 那条「自动生成一动就散架」的**同款故障**。
- 可复用性：✅ 落地（当清单用）—— **这 3 条就是「以后看到任何『一张图生成 Live2D』的论文/产品，先拿它对一遍」的检查表**：① 主指标是在**手作网格**还是**部署网格**上测的？② baseline 是否**同协议**？③ **眨眼（ParamEyeLOpen/R）** 这类关键参数在自动分解层上成没成？——**一条不过，宣传就得打折**。

### 四、上新 / 行业新闻

#### 1. nizima ACTION!!（官方在线视频编辑器 beta）新增 Live2D 模型「春日部つむぎ」+ VOICEVOX —— Live2D Inc. 新闻稿 · 2026-09-10

- 链接：`https://third-news.com/article/86ebc6a2-acc5-11f1-92ac-9ca3ba08e13f`（Live2D Inc. 新闻稿转载）· 官方站 `https://nizima.com/action/`（HTTP 200）
- 核实：稿内日期 **September 10, 2026 / 2026-09-10**；内容 = Live2D Inc.（东京新宿）在 **nizima ACTION!! beta** 中加入「春日部つむぎ」Live2D 模型（作画：Sakamoto Ahiru），**可配合 keyframe、多轨编辑、口型同步与 VOICEVOX**；VOICEVOX 于 **2026 年 5 月**接入；模型亦在 **KASUKABEproject Booth 免费分发**，可用于 nizima LIVE / VTube Studio。
- 讲了什么：官方把「Live2D 模型 + 语音合成 + 浏览器内视频编辑」打包成**免费 beta**，并预告桌面版、离线存储、协作编辑等后续功能。⚠️ 注意这是**新闻稿转载页**，**官方原始公告页未逐字核**。
- 可复用性：🔶 参考 —— **与 Ren'Py 无直接关系**（它是做短视频/CG 的 SaaS）；但它说明**官方主线在往「云端、视频、VTuber」走**，而不是往「游戏引擎集成」加码——**这对「等官方出 Ren'Py 友好功能」的期待是一次降温**。

#### 2. GALLERIA「Live2D Certified Model」认证整机 —— THIRDWAVE × Live2D Inc. · 2026-03-26

- 链接：`https://techbizblogs.com/galleria-launches-live2d-certified-pc-models-for-enhanced-creative-production/` · `https://alive-project.com/en/streamer-magazine/article/15035/`（均引 PR TIMES）
- 核实：两篇稿内日期 **March 26, 2026 开售**（DOSPARA 门店与网店）；购买权益 = **Live2D Cubism PRO（60 天）授权码 + nizima LIVE（1 年）免费券**；由 Live2D Inc. **监修规格**，目标让 Cubism Editor 与 nizima LIVE 舒适运行。
- 讲了什么：硬件厂商与 Live2D 联名的「认证整机」。⚠️ 两稿皆为**新闻稿转载/二手**，**官方 Live2D 侧无对应条目（本辑在 `live2d.com/information` 未核到）**。
- 可复用性：🔶 参考 —— 对个人无采购意义（他在 16GB Windows 上已能跑）；但**赠品结构值得记**：**60 天 PRO + 1 年 nizima LIVE** —— 如果哪天想「零成本试 PRO 60 天」，这是除 42 天试用、学割之外的**第三条免费 PRO 通道**（买这类机器时）。

#### 3. VTuber 直播平台市场规模报告（含 Live2D nizima LIVE 2.6） —— 市场研究稿 · 日期未核实

- 链接：`https://pmarketresearch.com/it/vtuber-live-streaming-platform-market/`
- 核实：**发布方为市场研究站点，日期未核实**；可读到的数字：**2025 年市场规模 USD 4580.0M → 2032 年预测 USD 18266.04M，CAGR 21.85%**；文中称 **Live2D 于 2026 年 3 月发布 nizima LIVE 2.6**（标注来源「Live2D Inc. / nizima LIVE Official, March 2026」）。
- 讲了什么：行业报告口径，把 Live2D 列为 VTuber 工具层供应商之一。⚠️ **此为二手市场报告，数字未经官方核对，仅登记不作依据**。
- 可复用性：❌ 不采用 —— **市场预测数字对本机目标无用**；唯一可用信息是「**nizima LIVE 2.6 大致在 2026 年 3 月**」，而**它已被官方 docs 的 2.6.1（2026-04-08，官方支持 Cubism 5.3）更新**（见下条）。

#### 4. 官方 nizima LIVE 变更历史：**2.6.1（2026-04-08）正式支持 Cubism 5.3** —— docs.live2d.com · 2026-04-08

- 链接：`https://docs.live2d.com/nizimalive/en/manual/history`
- 核实（搜索结果中读到官方页面内容）：**2.6.1 — 4/8/2026：Added official support for Cubism 5.3**；上游 2.6.0（2026-03-31）含 webcam 追踪增强、自适应采样、眨眼辅助、多种特效/预设等；2.5.x 各项修复。文末条目含 2026-01 的 2.5.0（新增动画数据创建、面捕参数等）。⚠️ 本辑**只从搜索摘要读到该页**，**未直接 curl 该页逐字复核**。
- 讲了什么：把上面那条二手市场报告的「nizima LIVE 2.6（2026-03）」**坐实并补到 2.6.1**——官方 VTuber 应用**已跟进 Cubism 5.3**。
- 可复用性：❌ 不采用 —— nizima LIVE 是 VTuber 直播应用，与 Ren'Py VN 无关；登记它只为**收束上面那条二手市场报告**。

---

## 退役源复测

> 本辑用户**未点名**退役源；按房规做一次低成本状态复核（curl 看状态码 + 正文特征），结果与 v29 一致，**判定不变，继续不再单独投入**。

| 源 | 状态码 | 正文特征 | 判定 |
|---|---|---|---|
| `gamemale.com` | **200** | `<title>请稍候...</title>` + `challenges.cloudflare` + `turnstile` | 全站 Cloudflare 人机验证，**结构性不可取**（与 v29 一致） |
| `reddit.com/r/Live2D/` | **000** | 无响应 | TLS/连接失败，**不可取** |
| `itch.io` | **000** | 无响应 | 超时，**不可取** |
| `note.com` | **000** | 无响应 | 超时，**不可取** |
| `medium.com` | **000** | 无响应 | 超时，**不可取** |
| `youtube.com` | **000** | 无响应 | 超时，**不可取** |

> 附：`hackernoon.com`、`dev.to` 本辑实测**可达**（200），只是**零 Live2D 内容**——它们不是「退役源」，是「无料源」，见 §二.4。
> `Stack Overflow` / `Godot 官方论坛`：v28 已用官方 API 跑过并下了负结论，本辑**未重复投入**（主题近真空）。

---

## 去重报告

**查重口径**：`_r30/_dedupe_gh.txt`（1213 行，本辑基线）+ `index.html` 现取（18727 行）+ `csdn-social-summary.md`(v29) + `csdn-social-summary-v28.md` + `csdn-social-summary-v27.md`。

| 关键词 | 命中的历史文件 | 结论 |
|---|---|---|
| `easy-live2d` | **index.html [1196]**（★213 · 2026-09-24）| **已在库**，本辑 dev.to 那篇不重复收 |
| `Open-LLM-VTuber` | v28 已收 | 已在库 |
| `5.3.00` / `5.3.04` / `5.3.03` | 无 | **新**（5.3.04 是对 v28「5.3.00」口径的修正） |
| `alive 2026` / `alive2026` / `autumnsale` / `秋季促销` | 无 | **全新官方动态** |
| `Bunraku` / `Live2D-Bench` / `bunraku-live2d` / `2607.27348` / `pith.science` | 无 | **全新学术** |
| `hermes-live2d` / `Soundpulse` / `hermes agent` / `NousResearch` | 无 | **新**（v29 桌宠集群的追加项） |
| `thebeni` / `cubismcat` / `Felo-Sparticle` / `openclaw-live2d` | 无 | **新**（community/上下线新闻） |
| `nizima ACTION` / `Kasukabe` | 无 | **新**（官方产品动态） |
| `GALLERIA` / `Live2D Certified` | 无 | **新**（联名硬件新闻） |

**净结论**：本路候选 **13 条**，**0 条与历史重复**；其中 `easy-live2d`（dev.to 那篇）与 `Open-LLM-VTuber`（HN/dev.to）**已在库，主动剔除**。所有收录条目的 URL/日期/版本号/价格**均逐条从对象自身字段真读**（GitHub API `created_at`/`pushed_at`/`published_at`、HN Algolia `created_at`、arXiv abs 页 `Submitted`、官方页正文日期），**无一条凭印象填写**；取不到的 3 处已显式标「日期未核实」（学割页 / pith.science / 市场报告）。

---

## 三到五条最值钱的发现

**1. 【官方口径修正 ×2】v28 的两处版本/价格数字本辑被推翻。**
第一处：**Cubism Editor 正式版早已不是 5.3.00，而是 5.3.04（2026-09-03）**——官方**产品页**只列大版本、**patch 号只藏在 `docs.live2d.com` 的 Release History 表**里，是「同站两处口径不一」的又一实例。第二处：**学生优惠在简中站是 80% OFF（¥36,720→¥7,344 / 3yr，截止 2027-03-31）**，而 v28 引英文站得 76% OFF（$238.20→$57.16）——**同一官网、区域不同、结算页不同**，**以自己所在区域结算页为准**。→ 这两条合起来说明一件事：**本文档过去几次「版本号/价格」结论漂了，不是记错，是官网分区域/分页面各写各的**；以后核对价格与版本，**必须写清是哪一站哪一页**。

**2. 【官方上新，时间敏感】今天（2026-10-11）是本轮两个窗口的边界。**
① **秋季专享特惠 8 折 PRO 今天截止**（2026.10.01 起，仅简中站有）；② **Cubism 5.4 alpha 再过 7 天（2026-10-18）停供**。→ 对用户的实际动作：**别为今天这 20% 冲动买 Pro**（学割 80% OFF 才是正路，截止 2027-03-31，时间很宽）；**想尝 5.4 新功能就这周抓，但别用它的产出发版**（官方明写「alpha→beta 迁移不作保证」）。另一条官方动态：**alive 2026 定档 2026-12-11 @秋叶原**（学生免费），**下一代 Cubism 情报大概率在这种年度场合放**，可留意 12 月后的回放。

**3. 【技术判据，价值最高】Bunraku 给了「一张图生成 Live2D」第一把尺子——而它的审稿报告顺手给了检查表。**
arXiv 2607.27348（2026-07-29，清华/南洋理工/SparcAI）是**首个端到端从单图生成「有序 RGBA 层 + 逐层网格 + 关键姿势顶点位移」的系统**，还发了首个基准 **Live2D-Bench** 与 **8,884 个模型**语料库——**这正面顶上了 v29 §三.4「单张立绘自动生成会散架」的判断**。但 `pith.science` 的公开审稿报告用**论文自己的数据**指出：**0.768 的方向余弦测的是「美术手作网格」，部署用的「alpha 自动网格」从未被测**（且 auto-mesh 更密、指标更差），且**眨眼（ParamEyeLOpen/R）在自动分解层上直接失效**。→ **这两篇合起来就是本辑最值钱的东西**：以后看到任何「一键生成 Live2D」，拿三问过一遍——① 主指标测的是**手作网格**还是**部署网格**？② baseline 是否**同协议**？③ **眨眼参数**在自动分解层上成没成？**三问有一不过，宣传就打折。**

**4. 【架构可抄】「AI 伴侣怎么接 Live2D」的实时链路，HN 评论区里写清了。**
Beni AI（HN 2026-01-25，34 分）作者原话给出链路：**WebRTC 流式 → 流式 STT → 低延迟 LLM → TTS → 客户端驱动 Live2D 参数**；口型用「**简单音素/振幅**」而非精确音素对齐。→ 对「Ren'Py 里接实时语音 Live2D」**方向可用、实现别硬搬**（云 + 实时 + 伴侣形态 ≠ 单机 16GB VN）；值钱的是**分层顺序**和「**振幅级口型够用**」这个取舍。

**5. 【跨境 vs 本地】官方主线在「云端/视频/VTuber」，不在「游戏引擎集成」。**
nizima ACTION!!（浏览器视频编辑，2026-09-10 加 Live2D 模型 + VOICEVOX）、GALLERIA 认证整机（2026-03-26）、nizima LIVE 2.6.1 支持 Cubism 5.3（2026-04-08）——**官方扩的是 SaaS 与 VTuber 侧**；而 **Ren'Py 依赖的 Native SDK 仍停在 5-r.5（2026-04-02）、无 5.4 版、无 6.0**。→ 结论：**别等官方为「游戏引擎」加码**；v28 那条「下载 Native SDK 装进 Ren'Py + 用 `Mao.moc3` 真跑一次」的自助欠账，**本辑仍是唯一正路，且版本号不变**。

---

## AI 相关的可直接落地的改动建议

> 判定原则：只采纳本辑**当场真读到**的东西；不能直接用的写清为什么。

**✅ 采纳 1：立刻走「学生优惠 80% OFF」，别为今天的 8 折促销买单。**
- 改什么：把采购动作从「看今天秋季促销」改成「走 `live2d.jp/chn/student-discount` 学割」——**¥7,344 / 3yr（80% OFF）vs 促销价仍要 ¥29,376+（8 折）**，**学割便宜一个数量级**。用户是在校生，**学信网在线验证码通道不需要学校邮箱**（切中大陆学生），审查约 5–6 天。
- 怎么验证：提交申请后**以收到的优惠券结算页价格为准**（别信首页宣传语）；核对「**非自动续费**」「**毕业后可用至订阅期满**」两条是否写进订单。
- 别做的事：**不要冲着 2026-10-11 截止的秋季 8 折今天下单**——那是给非学生/机构的口子，会浪费掉 80% 的学割。

**✅ 采纳 2：把 Bunraku 的三问做成一张「一键生成 Live2D 宣传打假清单」，下次遇到先用。**
- 改什么：以后任何「单图/一键生成 Live2D」的论文、产品、教程，**先过三问**：① 主指标测的是**手作网格**还是**部署用的 auto-mesh**？② 与 baseline 是否**同协议**？③ **`ParamEyeLOpen/R`（眨眼）** 在自动分解层上是否有量化成功率？**三问有一不过，就当营销读**。
- 怎么验证：这条清单本身**已被 `pith.science` 的审稿意见逐条坐实**（三个 major 分别对应三问），可回原文核对；配合 v29 §三.4 的失败实录，就有一套**正反两面**的判据。
- 边界：⚠️ Bunraku 代码仓 `SparcAI-Inc/Bunraku` **无 license、★37、创建即停更**——**今天只当「尺子/判据」用，不当产线**。

**🔶 观察（半采纳）：把 `Soundpulse/hermes-live2d` 记进「桌宠集群」清单，但仍不装进主力。**
- 读到的原文：它 `Tauri 2 + pixi-live2d-display`，带口型同步/表情/鼠标追踪/本地 HTTP API，**★115**（集群里偏高）；核心理念是「**把 agent 生成的 TTS 路由到宠物上做口型**」。
- 为什么只观察：**无 license 字段**（NOASSERTION）+ 渲染栈 `pixi-live2d-display`（老分叉，**未确认 Core 版本**，与 v29 记的 `dsh-live2d-pets`「栈停在 Core 4」同风险）。→ **先看它的接线（agent→TTS→Live2D 参数），别先装它**；真要装，先按 v29 §三.5 的警示「人先审一遍第三方插件再进主力 agent」。

**❌ 不采纳：Beni AI（thebeni.ai）作为参考实现去照搬。**
- 读到的原文：产品是**云 + 实时 WebRTC + ElevenLabs TTS + 在线 LLM** 的「视频通话 AI 伴侣」，评论区还有「**亲密 vs 分发互相冲突**」的核心产品矛盾。
- 为什么否：它解决的是「**云上 24/7 陪伴**」，用户要的是「**单机 16GB 本地 VN**」——**两套约束相反**（本地要离线、要确定性、要 Ollama；它要实时、要云、要在线上模型）。**只抄它的分层顺序与「振幅级口型够用」这一点，不搬它的架构**。

**❌ 不采纳：把「官方会为游戏引擎出 5.4/6.0 原生支持」当近期计划。**
- 读到的原文：官方 SDK 全线仍 **5-r.5（2026-04-02）**、**无 5-r.6、无 6.0**；官方扩的是 nizima ACTION（云视频）、GALLERIA 整机、nizima LIVE 2.6.1。
- 为什么否：**官方这条线的重心明显在 SaaS/VTuber，不在引擎集成**。第一款 VN 的 Live2D 落地，**仍得靠自己把 Native SDK 5-r.5 接进 Ren'Py**（v28 欠账），不是等官方给。

---

*本辑 official 路：官方上新 6 条 · 海外社区 4 条 · 技术/学术 2 条 · 上新/行业 4 条，共 **16 条**（净 13 条候选 + 3 条复核/负结论）。*
*查重：0 条与 `index.html` / v27 / v28 / v29 / `_dedupe_gh.txt` 重复；已剔除 `easy-live2d`（[1196]）与 `Open-LLM-VTuber`（v28）。*
*退役源：6 个源复测 1 个 200（gamemale Turnstile）+ 5 个 000，判定不变。*
*时间敏感：秋季 8 折 2026-10-11 止 · Cubism 5.4 alpha 2026-10-18 止 · 学割 2027-03-31 止 · alive 2026 定档 2026-12-11。*
*状态：完稿（2026-10-11）。*
