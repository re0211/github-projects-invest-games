# 第三十九辑 · official 路（Live2D 官方 / note.com / 海外社区）

> 子 agent 分工：official 路 —— Cubism 官方（官网 / Editor release notes / SDK 手册 / creatorsforum）+ note.com（日本创作者）+ Reddit r/Live2D / r/LocalLLaMA + DEV.to + X/Twitter + Booth.pm + YouTube 测评 + 海外上新新闻。CSDN/GitHub 交其他子 agent。
> 采集日期：2026-10-12。产出仅本文件，不改动 index.html / csdn-social-summary.md。
> 可复用性三档（基准 = 16GB Windows + 本地 Ollama + 维护索引站的个人）：① 落地 ② 参考 ③ 不采用，各 1 行理由。
> **本轮最高优先级：Cubism 5.4 alpha 可用期 2026-10-18 截止，倒计时最后一周。**

---

## 一、搜索覆盖

| 路 | 覆盖源 | 结果 |
|---|---|---|
| 官网公告 | live2d.com/en/information/cubism-5_4-alpha、cubism.live2d.com/link/announcement_5_4_alpha_zh | 已取（全文，含开发日程/FAQ/手册直链） |
| Editor 手册 | docs.live2d.com 更新履歴、**cubism.live2d.com/link/manual5_4_alpha_02_zh（alpha2 手册）** | 已取，**alpha2 手册本轮首次拿到**（r38 记为 404，本轮 200） |
| SDK 手册 | docs.live2d.com/en/cubism-sdk-manual/top | 已取（更新历史全量，含 09/29 Unreal 条目） |
| SDK 下载页 | live2d.com/zh-CHS?p=8720（Unreal Engine 更新履历） | 已取 |
| 官方论坛 | creatorsforum.live2d.com/c/cubismeditorsdk54alpha.json | **未取到（403，IP 被限流）**，见 §六 |
| 官网 news 首页 | live2d.com/en/?p=2121 | 已取（最新条目仍为 2026.07.14） |
| note.com | site: 检索 + WebSearch 多组日文检索式 | 未取到有效 note.com 正文，见 §六 |
| Reddit / DEV.to / HN | r/Live2D、r/LocalLLaMA | 检索未返回有效结果，见 §六 |
| 海外媒体 | Softpedia changelog、CGVisual | 已取 |
| GitHub 官方仓库（旁证） | Live2D/CubismUnrealEngineComponents releases | 已取（仅用于交叉印证 Unreal beta2，正文归 gh 路） |

---

## 二、本路一句话主线

**截至 2026-10-12（距 5.4 alpha 可用期 10-18 截止仅剩 6 天），官方口径零变化——仍为 alpha2、未转 beta、无 alpha3、无正式版时间表；但本路首次拿到三条新一手：Editor 5.4 alpha2 手册（含 PSD 导入强化 + alpha2 数据不可回退 alpha1/5.3 的兼容性硬约束），以及 2026-09-29 发布的 Cubism 5 SDK for Unreal Engine R1 beta2（终结了「Unreal 支持是否已弃」的悬案）。**

---

## 三、官方一手（Cubism 5.4 / release notes / SDK）

### 1. 【本轮最高优先级】5.4 alpha 倒计时状态核对：仍 alpha2，未转 beta，无 alpha3
- URL: https://www.live2d.com/zh-CHS/information/cubism-5_4-alpha （英：https://www.live2d.com/en/information/cubism-5_4-alpha/ ；镜像 https://cubism.live2d.com/link/announcement_5_4_alpha_zh ）
- 日期: 公告原发 2026-07-14；**核对时间 2026-10-12**（各语言版本均同步核对）
- 事实（原文）: 「**可使用至2026年10月18日。超过期限后，alpha版将无法继续使用。**」；「※随着alpha2的发布，使用期限已延长。请注意，alpha1在2026年9月14日之后将无法使用。」；「※ alpha版开放期间，以及**Beta版和正式版的发布时间，可能会根据收到的反馈数量进行调整**。」
- 三项关键核对结论：
  1. **未转 beta** —— 页面「开发流程」段仍为「待alpha版公开并确定各项功能规格后，将进入Beta版阶段」，无 beta 已启动字样。
  2. **无 alpha3** —— 全部官方页面仍只提 alpha1 / alpha2 两档，无 alpha3 下载或公告。
  3. **正式版时间表：本轮未取到** —— 官方全文未给出 beta/正式版的具体日期，仅声明可能随反馈量调整。**不得臆测。**
- 可复用性: ① 落地 —— 倒计时窗口的权威基线，索引站需在下轮（10-18 后）立刻复核是否已转 beta。

### 2. 【0 命中新事实】Editor 5.4 alpha2 手册上线，alpha2 修订记录首次可读
- URL: https://cubism.live2d.com/link/manual5_4_alpha_02_zh （官网公告页「alpha版使用手册」首条直链即为该 `_02` 版）
- 日期: 手册页标注 **2026/09/07**；采集 2026-10-12
- 事实: 修订记录表明确两档——`alpha1 / 2026/07/14 第一版创建`、`alpha2 / 2026/09/07 新增了以下内容`（含「数据兼容性的注意事项」「版本不一致时的覆盖保存警告」「更新历史记录『关于alpha版本的到期日期』」「更新历史记录『PSD导入功能的强化』」）。
- 对比价值: **r38 记录「SDK 手册 alpha2 直链仍 404」，本轮 Editor 手册 alpha2 直链 200 可用**——alpha2 文档此前被认为缺失，实际已补齐（SDK 手册仍仅 alpha1，见 §三-8）。
- 可复用性: ① 落地 —— 手册链路由 r38 的「404」更新为「alpha2 可用」，直接修正索引站既有条目。

### 3. 【0 命中新事实】alpha2 数据兼容性硬约束：不可回退 alpha1 / 5.3
- URL: https://cubism.live2d.com/link/manual5_4_alpha_02_zh
- 日期: 2026/09/07（alpha2）；采集 2026-10-12
- 事实（原文）: 「**使用 5.4.00 alpha2 保存的模型无法在 5.4.00 alpha1 或 5.3 及更早版本的 Editor 中打开。**另外，由于这是 alpha 版本，**无法保证未来发布的 5.4.00 beta 及后续版本的 Editor 也能正常读取该版本保存的数据**。如果用旧版本 Editor 打开后直接覆盖保存了模型文件，可能会导致该数据只能在 alpha2 中使用。」
- 配套机制: 「当您尝试覆盖保存不同版本的模型时，系统将自动弹出警告提示」（alpha2 新增的「版本不一致时的覆盖保存警告」）。
- 可复用性: ① 落地 —— 10-18 截止前**必须**提醒 alpha2 用户先导出/备份，否则数据锁死在过期 alpha2 内。

### 4. 【0 命中新事实】alpha2 新增 PSD 导入功能强化 + 导入交互简化
- URL: https://cubism.live2d.com/link/manual5_4_alpha_02_zh
- 日期: 2026/09/07（alpha2）；采集 2026-10-12
- 事实（原文）: 更新历史「PSD导入功能的增强 / alpha2 / 2026/09/07 /《新增功能》● **PSD导入功能的强化**」；通用类《其他改进项目》「**在导入PSD时，不再显示用于选择模型图像显示质量的对话框，默认设置为原始尺寸**」。
- 可复用性: ② 参考 —— 建模入口流程变更（少一步弹窗，默认原始尺寸），影响批量导入脚本/教程的操作步骤描述。

### 5. 【0 命中新事实 · 本轮最大发现】Cubism 5 SDK for Unreal Engine R1 beta2 发布（2026-09-29）
- URL: https://docs.live2d.com/en/cubism-sdk-manual/top/ ；下载页 https://www.live2d.com/zh-CHS?p=8720
- 日期: **2026-09-29**
- 事实（SDK 手册更新历史，同日 11 条 Unreal 条目一次性上线）:
  - 发布公告: 「Notification of Cubism 5 SDK R1 beta2 release (09/29/2026) —— Cubism 5 SDK for Unreal Engine R1 beta2」
  - 下载页更新履历: 「[2026-09-29] Cubism 5 SDK for Unreal Engine R1 beta2」
  - 新增手册章节: *How to use the model parameters in UE*、*Update components in editor mode*、*CubismUpdateController*、*ExpressionSample*、*HUDSample*、*LookAtSample*、*MotionSample*、*RaycastSample*
  - 更新章节: *Notes Specific to the Unreal Engine Version*、*Json (UE)*、「Platform Comparison」*Platform support status*
- beta2 具体变更（官方仓库 release notes 交叉印证，正文归 gh 路）: 新增 **macOS / iOS / Android 构建与运行支持**、新增 Koharu 模型、新增全部模型的 Cubism 源文件；修复渲染低效、Mobile Preview 稳定性、Android 遮罩渲染错误、非 Cubism Actor 添加组件崩溃、HarmonicMotion TimeScale 参数间不独立、**Unreal Engine 5.3 资源兼容性**、普通/循环动作的淡入淡出计算。
- 开发环境（官方 README）: Unreal Editor **5.7.4 / 5.6.1 / 5.5.4 / 5.4.4 / 5.3.2**；VS2022 17.14.40；测试平台 iOS/iPadOS 26.4、macOS 26.6、**Windows 11 25H2**、Android 16（Pixel 7a）。
- 战略结论: **终结 r38 悬案**——r38 只有论坛口头的「Unreal 支持未停止开发」（id 3973），本轮有**实锤发布物**：Unreal SDK 已从 alpha5 → beta1（2025-05-29）→ **beta2（2026-09-29）**，平台支持从 Windows 单一扩到 macOS/iOS/Android 四端。
- 可复用性: ① 落地 —— Unreal 集成路线图的关键节点，做 UE×Live2D 的必须以此为基线。

### 6. Cubism 5 SDK MotionSync Plugin R2_1 发布（2026-08-25）
- URL: https://docs.live2d.com/en/cubism-sdk-manual/top/
- 日期: **2026-08-25**
- 事实: 「Notification of Cubism 5 SDK MotionSync Plugin R2_1 release (08/25/2026)」——**for Native R2_1** 与 **for Unity R2_1** 双平台同步发布。（对齐：R2 为 2025-03-27，R2_1 为小版本迭代。）
- 可复用性: ② 参考 —— 口型同步（音频驱动）插件的版本基线；若项目用 MotionSync 应核到 R2_1。

### 7. 官方术语与 SDK 支持矩阵（alpha1 口径未变）
- URL: https://cubism.live2d.com/link/manual5_4_alpha_sdk_en （中文 https://cubism.live2d.com/link/manual5_4_alpha_sdk_zh ）
- 日期: R7 alpha1；采集 2026-10-12
- 事实（原文）: 「**Cubism 5 SDK refers to SDK versions up to and including Cubism 5 SDK R6. Cubism 5.4 SDK refers to SDK versions from Cubism 5 SDK R7 alpha1 onward.**」；支持表——Parameter Controller: Cubism 5 SDK ✕ / Cubism 5.4 SDK △（**alpha1 仅 Unity，其他平台计划自 beta1 起**）；Model State Set: 编辑器专属、**SDK 不支持**；外部联携 API 编辑扩充: 编辑器 UI 功能、**SDK 不支持**。
- 可复用性: ① 落地 —— 版本术语对齐是集成硬前提。

### 8. 【状态复核】SDK alpha2 手册仍缺失，仅 alpha1
- URL: https://cubism.live2d.com/link/manual5_4_alpha_sdk_zh （及 _en）
- 日期: 采集 2026-10-12
- 事实: SDK 手册仍为 **alpha1（2026/07/14）** 口径，未见 alpha2 修订记录；与 r32/r34/r36/r37/r38 一致复现。**即：Editor 手册已补 alpha2（§三-2），SDK 手册未补** —— 不对称状态本轮再次确认。
- 可复用性: ② 参考 —— 做 SDK 集成的只能依赖 alpha1 手册，需自行验证 alpha2 行为差异。

---

## 四、海外社区与上新新闻

### 9. 【0 命中 · 本轮 AI 关联最强】nizima LIVE 2.7：AI 助手直连本地 LLM，语音即可驱动模型（官方一手）
- URL: https://nizimalive.com/topics/product/270release （官方发布页）；日文原报道 https://prtimes.jp/main/html/rd/p/000000159.000024818.html ；MoguraVR https://www.moguravr.com?p=340311/
- 日期: **2026-08-12** 发布
- 事实（官方原文要点）:
  - **AI 助手**: 「You can have conversations with any Live2D model you like by **linking with the chat AI including ChatGPT, Gemini, or a local LLM**（可与 ChatGPT / Gemini / **本地 LLM** 联动）」；朗读用 **VOICEVOX 31 角色 82 种语音**（含 Zundamon、Shikoku Metan）；支持语音输入；口型与全身随朗读同步，**表情按对话推断的情绪变化**；可把回答作为字幕输出到 OBS。
  - 官方明确保留: 「**Live2D model data is not sent to the chat AI and will not be used for training**（模型数据不会发送给聊天 AI，也不用于训练）」。
  - 限制: 「The AI assistant feature is currently **available in Japanese only**（仅日语）」。
  - **语音追踪（Voice Tracking）**: 无需摄像头，纯语音输入即可驱动眨眼、口型、面部上下左右、全身动作。路径: Camera Settings > Audio Tracking。
  - **时间参数**: 可将「一天内从 0 单调推进到 1」的时间量绑定 Live2D 参数，支持 **24 小时 / 12 小时**两种周期（可做随时间变化的窗外景物等）。
  - macOS 全模型口型同步（此前仅 MotionSync 兼容模型）；鼠标左/右/中键及侧键可绑定表情与动作快捷键；Google 账号登录；新增 Mirror Ball / Comic / Pixel Art 特效。
- 可复用性: ① 落地 —— **与本索引基准（本地 Ollama）直接对口**：官方已原生支持「本地 LLM 驱动 Live2D」，是 AI×Live2D 从社区 hack 变成官方能力的标志节点。

### 10. 【0 命中】第 13 届 Live2D Creative Awards：新增「AI·对话界面」部门，2026-09-30 已截稿
- URL: https://www.live2d.com/en/event/awards13/ （中: https://www.live2d.com/zh-CHS?p=12989 ）
- 日期: 征稿 **2026-06-05 → 2026-09-30 23:59 JST**；**结果公布: 2026 年 12 月，于 alive 会场**
- 事实:
  - **本轮征稿已于 2026-09-30 结束** —— 对 10-12 这一时点是「评审中」状态。
  - 奖项与金额: 金奖 1 名 **30 万日元**+奖杯；影像表现力奖 / 创意互动奖（游戏·App）/ **创意互动奖（AI·对话界面）/ Live2D 模型奖 / 特别表彰奖** 各 1 名 **10 万日元**+奖杯；学生奖（大学·职校 / 高中及以下）各 1–3 名 **5 万日元**；创作者灵感奖 1–3 作品。
  - **「创意互动奖（AI・对话界面部门）」为第 13 届新增**（官方英文: *Interactive Award (AI / Talk interfaces)*），定位「体现 Live2D 作为 AI 对话引擎等界面潜力的作品」。
  - 投稿要求: 作品 ≤5 分钟；须在 YouTube / X / bilibili 公开上传并挂 **#Live2DAwards13**；须保持公开至 2027 年 1 月底。
  - 学生部门扩容: 自第 12 届（2025）起学生奖名额增至大学/职校 3 名 + 高中及以下 3 名。
- 可复用性: ② 参考 —— AI×Live2D 的官方风向标（新增 AI 部门 + 12 月 alive 公布，下轮可跟进获奖作品）。

### 11. 【0 命中】Live2D 20 周年（2026）官方企划：主题曲 + 学生折扣提至 80% + 与 KADOKAWA 的产业调研
- URL: https://www.live2d.jp/20th-anniversary/en/
- 日期: 企划跨 2025-12 → 2027-03
- 事实:
  - 2026 年为 Live2D **20 周年**，官方制作原创主题曲 **「Shape the Future」**（日文版: Machita Chiima；英文版: **Nerissa Ravencroft（hololive EN）**；作词作曲 Tabuchi Tomoya，编曲 Horie Shota；音乐制作人 Yamanouchi Masaharu（ANIPLEX）+ Suda Shugo（Live2D））。角色设计 seica，Live2D 建模与动画导演 **cillia**。允许翻唱/二次创作。
  - 核心项目 ①: **Cubism Editor「2026 限定，学生折扣上调至 80%」**（2026-03-02 → 2027-03-31，仅 2026 学年）。
  - 核心项目 ②: **调研报告「Live2D: 20 Years of Creative Impact」**（2025-12-03），与 **KADOKAWA ASCII 研究实验室**合作。
  - 协同项目: Coloso. 课程折扣（2025-09-25 起）；**组合折扣提至减 ¥2,000**（2025-12 起，搭配 JUKU / nizima LIVE）；「Future Shapers」新人创作者访谈（2025-11-21 起，首期韩国独立开发商 HIGH-END Games）；**2025-12-12 秋叶原 UDX「alive」邀请 200 名学生免费入场**。
  - 官网多语种扩展: 泰语（2025-11-14，泰语为第 5 大用户社群）、西班牙语（2026-02-13）、印尼语（2026-04-02）。
- 可复用性: ② 参考 —— 官方生态/商业化口径的一手汇总；学生 80% 折扣对预算敏感读者有直接价值。

### 12. 【0 命中】Unreal 手册新增页：Cubism Model Parameter Controller 编辑器扩展（含明确限制）
- URL: https://docs.live2d.com/en/cubism-sdk-manual/cubism-sdk-for-ue-model-parameter
- 日期: 随 R1 beta2 上线，2026-09-29；采集 2026-10-12
- 事实（原文）: 在装有 Cubism SDK for Unreal Engine 的项目中导入 Live2D 模型，由 `.model3.json` 生成 uasset 放入 View 并生成 actor 后，**右键 Outliner 或该 actor → 选「Cubism Model Parameter Controller」**，即可用 Inspector 里的滑杆预览参数操作。
- **关键限制（原文）**: 「**Only parameter changes made with the 'Cubism Model Parameter Controller' while 'Play in Editor' is off are applied.** Note that if 'Play in Editor' is on, any changes you make ... will not be applied.」（PIE 开启时改的参数**不生效**）
- 可复用性: ① 落地 —— UE 内调参的必踩坑：必须先关 PIE，否则改了白改。

### 13. Softpedia 收录 5.4 Alpha 变更条目（Core 层）
- URL: https://www.softpedia.com/progChangelog/Live2D-Cubism-Changelog-259185.html
- 日期: 条目标注 **Jul 14, 2026**；采集 2026-10-12
- 事实: 「What's new in Live2D Cubism 5.4 Alpha: **Fixed the return value type of `csmGetParameterValues`. Added description related to parameter control.**」；Softpedia 页同时标注最新正式版为 **5.3.03**，5.4 列为 Alpha，安装包 236 MB。
- 可复用性: ② 参考 —— Cubism Core C API 层面的一处签名修正（`csmGetParameterValues` 返回值类型），直连 Core 的项目需核对该签名。

### 14. 海外媒体报道：CGVisual（5.4 alpha + Summer Sale 2026 捆绑）
- URL: https://new.cgvisual.com/cgnews/live2d-cubism-5-4-alpha-released-alongside-summer-sale-2026-with-20-off-pro-licenses
- 日期: 2026-07（与 Summer Sale 同期）
- 事实: 报道 5.4 alpha 重点为**参数控制器 SDK 支持（可在 SDK 通过指定 Target 坐标实时控制模型动态）**与**模型状态集**；同期的 Summer Sale 2026 在 **7 月 27 日前**对新购 Cubism PRO（年费/三年）及 **nizima LIVE** 提供 **20% 折扣**，并与在线课程平台 **Coloso.** 联动。
- 可复用性: ③ 不采用（二手，已被官方一手覆盖）—— 仅作传播佐证。

### 15. DEV.to 评测：Open-LLM-VTuber —— 离线 AI 伴侣 + Live2D（社区侧，本地 LLM 路线）
- URL: https://www.libhunt.com/posts/1513864-open-llm-vtuber-review-offline-ai-companion-with-live2d （dev.to 原文转载索引）
- 日期: 转载索引 2026 年；项目本体持续更新
- 事实: 官方定位「Talk to any LLM with hands-free voice interaction, voice interruption, and **Live2D taking face running locally** across platforms」；安装链路 `uv sync` + `ollama pull qwen2.5:7b` + `uv run run_server.py`。第三方评测记录其 **10,000+ GitHub stars**、v1.x 稳定版、**v2.0 正在完全重写**、**v1.0.0 缺长期记忆**、示例 Live2D 模型限非商用。
- 去重注: `Open-LLM-VTuber` 在 `index.html` 有 4 处（已覆盖），本条仅补「DEV.to 评测 + 本地安装命令 + v2.0 重写状态」新证据。
- 可复用性: ② 参考 —— 与 §四-9 的官方 nizima AI 助手互为对照：一条官方路线、一条开源路线，都指向本地 LLM 驱动 Live2D。

### 16. Live2D Game Jam（itch.io 官方赛事）
- URL: https://itch.io/jam/live2d-game-jam
- 日期: 赛程 **9 月 19 日 00:00 → 10 月 6 日 23:59 JST**（对应 2025 年首届；官网 news 记为 2025-09-05 启动、2025-10-14 公布获奖）
- 事实: 无引擎限制，Cubism SDK 使用可选但被鼓励（官方明确 SDK 支持 **Web / Native / Unity / Unreal Engine (beta) / Java**）；队伍上限 4 人；奖品为 1 年 Cubism PRO 授权（每队至多 4 份，约 $100/份）+ 官方 X 展示 + 官网作品库收录；评委含 Momoiro Kohi、Ran（PIXELVERTICE）、Tom Farro、Cat Athenya。**规则明确禁止使用生成式 AI 产出的图像/音频/音乐素材**（允许用于编码辅助）。
- 去重注: `itch.io` / `Game Jam` 在 `index.html` 有 6 处（已覆盖），本条补「Unreal (beta) 官方口径 + AI 素材禁令」新证据。
- 可复用性: ② 参考 —— 官方对 SDK 各平台支持状态的口语化表述（Unreal 标 beta）可作旁证。

---

## 五、note.com 等日本侧制作经验

> **note.com 本轮仍未取到**（详见 §六）。以下为**实际取到的日本侧一手/准一手来源**：Live2D 自家产品 nizima 系列发布页 + 日本科技媒体（MoguraVR / PR TIMES / alive-project / Third News）对官方发布的报道。

### 17. 【0 命中】nizima ACTION!! 追加「春日部つむぎ」Live2D 模型（2026-09-10）
- URL: https://third-news.com/article/86ebc6a2-acc5-11f1-92ac-9ca3ba08e13f ；时间线索引 https://yomimono.id/tag/nizima-action
- 日期: **2026-09-10**（Live2D 官方发布）
- 事实: 浏览器端在线视频编辑器「**nizima ACTION!! β版**」新增春日部つむぎ Live2D 模型（插画: 坂本アヒル）。该模型含 **40 种以上表情与动作**，**免费使用**，**支持手部追踪（hand tracking）**，可通过 **nizima LIVE / VTube Studio** 等追踪应用实时驱动；与 5 月已集成的 **VOICEVOX** 联动，可在编辑器内一次完成「文本输入 → 语音合成 → 口型同步」。同一模型也在 **KASUKABEproject 的 Booth** 免费配布。使用时须遵守角色使用条款并标注 Credit（如「VOICEVOX:春日部つむぎ」）。
- 编辑器状态: 有 nizima 账号即可**免费**使用；官方称**桌面版（离线）与协作编辑功能正在开发中**。
- 可复用性: ① 落地 —— 免费可商用素材 + 浏览器端零安装工作流，对不想装 Cubism 的读者是低门槛入口。

### 18. 【0 命中】nizima ACTION!! 集成 VOICEVOX：字幕与语音合成（2026-05-27）
- URL: https://yomimono.id/tag/live2d （时间线条目，源自 PANORA 等日本媒体）
- 日期: **2026-05-27**
- 事实: 「字幕与语音合成」功能集成 **VOICEVOX**（当时支持 **37 个角色**）；可输入文本生成角色语音（含 Zundamon），**可调语速 / 音高 / 音量 / 语调**，一键把音频放到时间轴。同次更新还追加了坂本アヒル绘制的 **Zundamon Live2D 模型**，以及东北 Zunko・Zundamon 项目的**另外 8 个模型**（含东北ずん子、東北きりたん、四国めたん等）。
- 可复用性: ② 参考 —— 日文 TTS + Live2D 的官方闭环方案；VOICEVOX 角色数从 5 月的 37 增至 8 月 nizima LIVE 2.7 的 31 角色 82 语音口径（口径不同，需注意统计维度）。

### 19. 【0 命中】nizima ACTION!! 追加四国めたん / アンコモン模型（2026-08-04）
- URL: https://yomimono.id/tag/nizima-action
- 日期: **2026-08-04**
- 事实: Live2D 发布四国めたん与アンコモン的 Live2D 模型（插画: 坂本アヒル），**各含 50 种以上表情与动作**，**支持手部追踪**，可经 nizima LIVE / VTube Studio 实时驱动；同时作为样例素材内置，并在项目官网免费配布。官方同时预告将追加**东北三姐妹（东北ずん子・東北きりたん・東北イタコ）**模型。
- 可复用性: ② 参考 —— 免费模型素材池的扩充节奏（5 月 → 8 月 → 9 月，每月一批）。

### 20. 【0 命中】日本科技媒体侧：MoguraVR / PR TIMES 对 nizima LIVE 2.7 的报道（2026-08-12/13）
- URL: https://www.moguravr.com?p=340311/ ；PR TIMES 原文 https://prtimes.jp/main/html/rd/p/000000159.000024818.html
- 日期: 发布 2026-08-12，报道 2026-08-13
- 事实: MoguraVR 给出的规格表——**最新版本 2.7 / 发布日期 2026 年 8 月 12 日 / 主要新功能: AI 助手・语音追踪・时间参数 / AI 联动: ChatGPT、Gemini、local LLM 等 / 语音合成: VOICEVOX 系列 31 角色共 82 种 / 支持 OS: Windows、macOS，另有 iOS 应用 nizima LIVE TRACKER**。
- 可复用性: ② 参考 —— 日本主流 VR/VTuber 媒体的规格确认，可作 §四-9 的日文侧互证。

### 21. 【0 命中】日本侧媒体 alive-project：nizima LIVE 2.7 六项新功能盘点 + 趋势评论
- URL: https://alive-project.com/en/streamer-magazine/article/18748/
- 日期: 2026-08（2.7 发布同期）
- 事实: 归纳 2.7 的**六项新功能**——AI 助手、语音追踪、时间参数、**macOS 全模型口型同步**、**鼠标点击绑定快捷键**、**Google 登录**；另加 **Mirror Ball / Comic / Pixel Art** 三种新特效。评论观点: AI 助手集成是「VTuber 工具的里程碑式更新」，使「单人直播也能实现角色间对话」这一新直播形态成为可能；语音追踪则解决了「绘画直播低头导致摄像头追踪失效」的长期痛点。
- 可复用性: ② 参考 —— 日本侧对「AI×Live2D」落地场景的具体判断，可作索引站趋势段落的引述来源。

### 22. 【0 命中】日本侧媒体 Third News：第 13 届 Live2D Creative Awards 征稿报道
- URL: https://third-news.com/article/ed11f04c-6093-11f1-86b1-9ca3ba08e13f
- 日期: 2026-06（征稿开始时）
- 事实: 征稿期 **2026-06-05 → 2026-09-30（JST 23:59）**；评审标准两条——① 是否传达了 Live2D / 2D 作品的特性与可能性；② Live2D 动画质量是否达到高水准。**结果公布: 2026 年 12 月，于 alive 会场**。
- 可复用性: ② 参考 —— 与 §四-10 官方页互为印证，补评审标准细节。

### 23. note.com（日本创作者经验帖）—— 本轮未取到
- 检索式: `note.com/search?q=Live2D`、`note.com/hashtag/Live2D`、多组日文 WebSearch 检索式
- 结果: **均未取到**。WebFetch 直连返回 `fetch failed`（TLS/连接层失败）；WebSearch 的 `site:note.com` 检索式未返回任何 note.com 域名结果（返回的是无关中文/日文站点）。
- **说明: 这不代表 note.com 上不存在 Live2D 制作经验帖**，而是本轮本机网络对其不可达。与 r32/r34/r36/r37/r38 一致复现（连续 6 轮未取到）。下轮建议: 换用可访问日本站点的网络出口，或经由 Bing/Google 缓存、note.com 的 RSS/API 端点尝试。

---

## 六、本轮取源失败登记

| 源 | 端点/检索式 | 失败表现 | 性质判断 |
|---|---|---|---|
| **note.com** | `note.com/search?q=Live2D`、`note.com/hashtag/Live2D` | WebFetch `fetch failed`（连接层失败，非 404）；WebSearch 日文检索式无 note.com 结果 | **网络不可达 / 反爬**。非「不存在」 |
| **creatorsforum.live2d.com** | `/c/cubismeditorsdk54alpha.json` | HTTP **403**，`Your IP has been temporarily restricted`（Discourse 限流，错误码 `d/t/44262`） | **IP 限流**。**r38 曾用 `.json` 端点成功，本轮被封**。非「不存在」 |
| **Reddit** | r/Live2D、r/LocalLLaMA | 多组检索式均未返回 reddit.com 正文结果 | **未取到**。非「无内容」 |
| **DEV.to** | 站内直接检索 | 仅取到 libhunt 转载索引，未取到 dev.to 原页 | **部分取到**（已标注为转载索引） |
| **Booth.pm** | `Live2D モデル 配布 Booth 2026年10月` | 检索结果全部为无关日本活动/周边页面 | **未取到** |
| **YouTube 官方测评** | Live2D 官方 YouTube playlist | 未直接取到视频页正文 | **未取到**（客观存在，公告页有直链） |
| **X / Twitter** | `#cubism54_alpha`、`@Live2D`、@live2d_dev | 未取到 2026-09/10 新推文；仅取到 2026-07-14 历史推文（经第三方镜像） | **未取到本轮新推文** |
| **5.4 beta / 正式版时间表** | 官网公告、手册、SDK 页全量核对 | 官方全文未给出任何 beta/正式版日期 | **官方未公布**（非取源失败，是客观上不存在） |
| **5.4 alpha3** | 同上 | 全部官方页面无 alpha3 字样 | **官方未发布**（非取源失败） |

---

## 七、去重报告

### 去重方式
对五个基线文件执行 `grep -iF "<候选专属串>"`:
`index.html`、`csdn-social-summary.md`、`csdn-social-summary-v36.md`、`csdn-social-summary-v34.md`、`csdn-social-summary-v33.md`

### 候选总数
正文条目 **33 条**（§三 8 + §四 8 + §五 7 + §八 10）。

### 0 命中基线、确认为全新的串（本轮净增事实）
`Unreal Engine R1 beta2`(0/0/0/0/0)、`manual5_4_alpha_02`(0)、`PSD导入`(0)、`Cubism Model Parameter Controller`(0)、`Koharu`(0)、`csmGetParameterValues`(0)、`Creative Awards 13th`(0)、`20th anniversary`(0)、`Proprietary Software License`(0)、`Platform support status`(0)、`HarmonyOS`(0)、`Tuanjie`(0)、`MotionSync Core`(0)、`5-r.2`(0)、`CRIWARE`(0)、`CRI Lipsync`(0)、`DOVA-SYNDROME`(0)、`Poly Haven`(0)、`0.55.3`(0)、`0.55.0`(0)、`Intel Mac`(0)、`GTX 1060`(0)、`wp-sitemap`(0)、`nizimaaction`(0)、`Cocos Creator`(index 3 处，但本轮为「与 Cocos2d-x 区分」的新用法)、`Shape the Future`(0)、`KADOKAWA`(0)、`nizima LIVE`(0)、`nizima ACTION`(0)、`Kasukabe`(0)、`Zundamon`(0)、`Ankomon`(0)、`Shikoku Metan`(0)、`MoguraVR`(0)、`alive-project`(0)、`PANORA`(0)、`prtimes`(0)、`Coloso`(0)、`VOICEVOX`(index 3 处，正文描述不同，保留标注)

### 命中基线、但作为 anchor / 补新证据保留（不计剔除）
1. `Unreal` —— index 33 处 / summary 7 处。泛述已覆盖，**但 `R1 beta2` 具体版本 0 命中**，按新事实保留。
2. `MotionSync` —— index 1 / summary 1 / v36 1 / v34 1。`R2_1` 串 0 命中于 index，保留为版本基线更新。
3. `Open-LLM-VTuber` —— index 4 处。已覆盖，本条仅补 DEV.to 评测 + v2.0 重写状态，标注后保留。
4. `itch.io` / `Game Jam` —— index 6 处。已覆盖，本条补「Unreal (beta) 官方口径 + 生成式 AI 素材禁令」，标注后保留。
5. `nizima` —— index 4 / summary 1。泛述已覆盖，`nizima ACTION`/`nizima LIVE` 具体产品串 0 命中，保留。
6. `VOICEVOX` —— index 3 处。保留但标注：本轮补「31 角色 82 语音 / 37 角色」具体数字与 nizima ACTION 集成日期。
7. `2026-10-18` / `5.4 alpha2` 核心状态 —— 基线多处，属旧闻同状态，**保留为官方 anchor**（本轮为倒计时最后一次核对，价值在「确认未变」）。
8. `Cocos2d-x` —— index 3 处。已覆盖，但本轮补的是「**官方手册已由未来时改为完成态 + 确切日期 2024-12-19**」这一口径变更事实，属新证据，保留。
9. `MotionSync` —— index 1 / summary 1 / v36 1 / v34 1。已覆盖，本轮补的是「**双协议授权 + royalty-free + Core 不上 GitHub**」这一授权边界（gh 路原标 NOASSERTION），属新证据，保留。
10. `MediaPipe` —— index 6 处。已覆盖，本轮补的是「**nizima LIVE 面部追踪确用 MediaPipe SDK**」这一官方技术栈声明，属新证据，保留。
11. `nizimalive` —— index 5 处。已覆盖，本轮补的是官方手册子站结构与运行环境一手规格，属新证据，保留。

### 剔除清单（判重复，全文不收）
- **无**。本轮所有 23 条候选均通过去重或经标注后保留。
- 主动放弃的候选（未写成条目）:
  1. Live2D Cubism 基础操作教程类中文站点（cr173 / live2d.net.cn / adesigner）—— 内容无一手信息且与索引站定位不符。
  2. Booth.pm 上新 —— 检索未返回有效结果，无法形成条目（已登记 §六）。
  3. 中文站「Live2D 技术完全介绍」类泛述 —— 无新增事实。

### 「旧闻换日期」专项核对
对以下高危候选逐条核对发布日期，确认**非**旧帖换日期:
- 5.4 alpha 公告页: 页面正文 `2026.07.14` 发布，10-18 期限自 alpha2（2026-09-07）起生效，**非**近期新发的旧内容。
- Editor 更新履歴: 最新仍为 `5.3.04 (2026/09/03)`，与 r38 一致，**未**被换成新日期。
- SDK Unreal R1 beta2: 手册更新历史与下载页均为 `09/29/2026`，且与 GitHub release 时间戳 `2026-09-29T03:20:01Z` 三方一致，确认真实新发布。
- nizima LIVE 2.7: 官方页、MoguraVR、PR TIMES 三方均为 2026-08-12/13，一致。

---

## 八、应 gh 路请求补核的官方口径（r39 追加）

> 由 general-purpose-1 提出三点交叉核对要求，均属 official 路范围，本轮补核如下。

### 24. 【官方口径已变 · 值得单独记一笔】Cocos2d-x 支持：README 是陈旧文案，官方手册已改为「R2 后已终止」
- URL: https://docs.live2d.com/en/cubism-sdk-manual/platform/ （中: https://docs.live2d.com/zh-CHS/cubism-sdk-manual/platform/ ）
- 日期: 平台支持表 **Updated: 09/29/2026**；Cocos2d-x 条目更新于 **2024/12/19**
- 事实（三方口径对比）:
  - **GitHub README（陈旧，未来时）**: `[Notice of End of Support for Cocos2d-x] With the **upcoming release** of Cubism 5 SDK for Native R2, support for Cocos2d-x **will be ended**.` —— 至今仍挂在 `Live2D/CubismNativeFramework`、`Live2D/CubismNativeSamples` 仓库描述上。
  - **官方手册表格注释（现在时/完成态）**: 表注 `*4`: 「**Support was terminated after Cubism 5 SDK for Native R2.**」
  - **官方手册更新历史（明确日期）**: `12/19/2024 | Cocos2d-x | Support was terminated after Cubism 5 SDK for Native R2`；中文版对应「2024/12/19 / Cocos2d-x / **仅支持到Cubism 5 SDK for Native R2**」。
- **结论**: 官方口径**已从事前预告改为事后确认**，并给出确切日期 2024-12-19。**README 文案未同步更新，属陈旧文案**——Cubism 5 SDK for Native 早已发布到 R5（R5 beta1 见 2025-08-26），R2 是过去式。
- **易混淆点警告**: 官方手册 Cubism Core 页列出的官方 SDK 清单中是 **「Cubism SDK for Cocos Creator」**，与 **Cocos2d-x 是两个不同东西**（Cocos Creator ≠ Cocos2d-x）。且官方注明「目前 Cubism SDK for Cocos Creator 的 GitHub 存储库中没有 CHANGELOG」。索引站引用时务必区分，勿混为一谈。
- 可复用性: ① 落地 —— 索引站此前已有一轮推翻过官方两处口径，此为**第三次口径不一致**，建议统一以「官方手册平台支持表」为准、README 为次。

### 25. 【0 命中 · 权威合规说法】Cubism Core 不得在 GitHub 发布，须从官方包获取
- URL: https://docs.live2d.com/zh-CHS/cubism-sdk-manual/cubism-core （英: https://docs.live2d.com/en/cubism-sdk-manual/cubism-sdk-for-unreal-engine 同款表述）
- 日期: 采集 2026-10-12
- 事实（官方原文）: 「**根据Live2D 专有软件许可协议，不在GitHub上发布Cubism Core。** Cubism Core已包含在软件包中，如果需要，请从Live2D官网下载软件包。」（英: *In accordance with the Live2D Proprietary Software License Agreement, Cubism Core is not published on GitHub.*）
- 官方 SDK 包含关系（原文）: 「**每个公开的Cubism SDK包中都包含了最新的Cubism Core。**」官方 SDK 清单一共 6 个: Native / Web / Unity / Java / **Cocos Creator** / Unreal Engine。
- 适用 EULA: **Live2D Proprietary Software License Agreement, Version 2.1, Revised: February 3rd, 2025**；対象ソフトウェア明确为 **Live2D Cubism Core** 与 **Live2D Cubism MotionSync Core** 两项。URL: https://www.live2d.com/eula/live2d-proprietary-software-license-agreement_en.html
- **对 gh 路三个仓库的合规判定**: `rayriffy/CubismMetal`、`Yuuzulight/Mana`、`loliRuriruri/HoloDori` 均声明「不打包 Cubism Core，需用户按官方条款自行获取」——**与官方口径完全一致，属正确合规做法**。三者差异仅在表述粒度（Mana 用三层许可切分，另两家仅为一句声明），**不构成合规冲突**。
- 可复用性: ① 落地 —— 这是「Core 能否随仓库分发」的**唯一权威答案：不能**。下辑可据此统一各仓库的合规表述。

### 26. 【0 命中】平台支持表 2026-09-29 更新：Unreal Engine 一行新增 macOS / Android / iOS
- URL: https://docs.live2d.com/en/cubism-sdk-manual/platform/
- 日期: **2026-09-29**（与 R1 beta2 同日）
- 事实: 更新历史最新条目 `[09/29/2026] Unreal Engine / Added new item`。Unreal Engine SDK 行现为 **Windows ✓ / macOS ✓ / Android ✓ / iOS ✓**（注 *1: 仅 64 位架构）。
- **对比价值**: 该表在 beta2 之前 Unreal 行仅有 Windows。**macOS / Android / iOS 三格正是 R1 beta2 的新增**，与 §三-5 的 release notes（新增 macOS/iOS/Android 构建与运行支持）**互相印证**。
- 同表其他 0 命中细节: Native 行含 **HarmonyOS ✓**（渲染引擎列）；Unity 行含 **WebGL ✓** 与 **HarmonyOS ✓**（注 *3: 需 **Tuanjie / 团结引擎**，即 Unity 中国版）；Java 行 **Android 5.0(API 21) – Android 14.0(API 34)**。
- 可复用性: ② 参考 —— 平台选型的一手依据；**Tuanjie（团结引擎）为中国版 Unity** 这一点对国内读者有直接价值。

### 27. 【0 命中 · 结案】Cubism 5 SDK for Native R2 已发布 → Cocos2d-x 终止支持为既成事实
- URL: https://github.com/Live2D/CubismNativeSamples/releases/tag/5-r.2 （官方仓库 tag `5-r.2`）
- 日期: **R2 发布日期 2024-12-19**（release assets 时间戳 `2024-12-19T02:19:54Z`）
- 事实（R2 release notes 原文，Removed 段）: 「**Remove the Cocos2d-x sample project.**」——**同一次发布就把 Cocos2d-x 示例工程直接删除**。
- **判定（回应 gh 路提问）**: R2 **已发布**，故 Cocos2d-x 支持终止**不是预告，是既成事实**。与 §八-24 官方手册「terminated after Cubism 5 SDK for Native R2」+ 更新历史 `12/19/2024` **三方时间戳完全吻合**（手册日期 = release 日期 = 2024-12-19）。
- **对老教程时效性的直接影响**: 凡依赖 Cubism Native + Cocos2d-x 的教程，其示例代码在 **R2（2024-12-19）之后官方仓库已无对应 sample**，读者按教程操作会找不到工程。索引站对这类老教程建议加时效标注。
- **Native 版本演进链（供版本判定参考）**: R2(2024-12-19) → R3(2025-02-18) → R4(2025-05-29) → R4_1(2025-07-17) → R5 beta1(2025-08-26) → R5 beta2(2025-10-30) → R5 beta3(2026-01-29) → **R5(2026-04-02)**。
- 可复用性: ① 落地 —— 给「Cocos 相关老教程是否已失效」一个硬日期分界线：2024-12-19。

### 28. 【0 命中 · 结案】MotionSync 授权边界：非单独授权，走双协议，且免版税
- URL: https://docs.live2d.com/en/cubism-sdk-manual/cubism-sdk-motionsync-plugin-for-native/ （Web 版中文: https://docs.live2d.com/zh-CHS/cubism-sdk-manual/cubism-sdk-motionsync-plugin-for-web ）
- 日期: 采集 2026-10-12
- 事实（官方原文，逐条）:
  - **授权归属**: 「Cubism SDK MotionSync Plugin 许可证**适用 Live2D Proprietary Software 软件许可协议和 Live2D Open Software 软件许可协议**。」→ **不是单独授权**，与主体 SDK 同一套双协议。
  - **第三方组件与费用**: 本软件使用 CRI Middleware Co., Ltd. 的「**CRIWARE (R)**」；但「MotionSync Plugin 中使用的 **CRI Lipsync 已获得 Live2D 许可**，因此 MotionSync Plugin **可以免版税（royalty-free）使用**，并且**无需显示 CRIWARE 徽标**」。
  - **Core 可否分发**: 「根据 Live2D Proprietary Software 软件许可协议，**MotionSync Core 未在 GitHub 上发布**。软件包中包含 MotionSync Core，因此如果需要，请下载该软件包。」→ 与 §八-25 的 Cubism Core 同一规定。
  - **前置依赖**: 「使用时需要 **Cubism SDK for Native / for Web**（对应平台）」——插件不能独立使用。
- **对 gh 路 NOASSERTION 的建议（回应提问）**: 三个 MotionSync Components 仓库（`CubismUnityMotionSyncComponents` / `CubismNativeMotionSyncComponents` / `CubismWebMotionSyncComponents`）无 LICENSE 文件是**符合官方结构的**——仓库只是开源的「Components」外壳，Core 专有不随仓。建议卡片标注改为 **「Live2D Open Software License（Components 部分）+ Proprietary（MotionSync Core，不随仓分发）」**，比纯 NOASSERTION 更准确。
- **MotionSync Plugin 平台支持矩阵**（官方 SDK 页 https://www.live2d.com/zh-CHS/sdk/about ）: **Unity ✓ / Native ✓ / Web ✓；Java ✗ / Cocos Creator ✗**。与 gh 路观察到的三个仓库（Unity / Native / Web）完全一致。
- 同页 0 命中细节: **Cubism SDK for Cocos Creator 支持 Cocos Creator v3.7.0 或以上，不支持 v2**。
- 可复用性: ① 落地 —— 解决 gh 路的 NOASSERTION 硬伤；「免版税 + 无需 CRIWARE 徽标」对商用评估是直接结论。

### 29. 【0 命中】nizima ACTION!! 官方站：闭源在线服务，官方页是索引覆盖它的唯一入口
- URL: https://site.nizima-action.com/en （官方站）
- 日期: 采集 2026-10-12；站内 NEWS 最新条目 `3/18/26 nizima ACTION!! [0.48.0] has been released!`
- **产品定位（回应 gh 路提问）**: 官方定位「**Live2D's Official Online Video Editor**」，浏览器内运行。与 **nizima LIVE**（桌面/移动端的**追踪·直播应用**）**确为两个不同产品**——gp-1 的判断正确。
- 关键事实（官方原文）:
  - **定价**: 「Currently, the beta version is available **completely free of charge**! In the future, we plan to charge for some functions and materials, but you will be able to continue to use the service for free.」
  - **商用**: 「Commercial use of the beta version is available **for free to both individuals and corporations**（**个人与企业均可免费商用**）」。
  - **素材规模**: 「**Over 10,000 assets and templates**」；含 **DOVA-SYNDROME** BGM、**irasutoya（いらすとや）动画化模型**、Pixabay、Pexels、**Poly Haven（3D 素材站）**。
  - 功能: 导入自有 Live2D 模型、参数调整、表情/动作套用；**基于语音输入自动生成口型同步与动作**；经 **nizima LIVE / VTube Studio** 做动作追踪；「**Live2D ACTION Frames**」（把模型放进气泡、胶片盘等特效框）；**7 种导出格式**。
  - 版本: beta 首发 **2025-07-09**（alive-project 报道）；当前 **0.48.0（2026-03-18）**；**桌面版与协作编辑功能开发中**。
  - 官方角色: 「**Dōrō Act**（どろあくと）」，可免费使用。
- **对 gh 路的结论**: nizima ACTION 是**纯闭源在线服务，无开源仓库**，gh 搜索 0 条是**正确结果**（非漏采）。索引要覆盖它只能走官方站这一入口——本条即为该入口。
- 可复用性: ① 落地 —— 「个人+企业免费商用」是索引站上少见的强商用授权信号，值得单独标出。

### 30. 【0 命中 · 本轮最新一手】nizima ACTION!! 更新履历：当前 0.55.3（2026-10-07），官方预告 10-14 数据保存机制刷新
- URL: https://docs.live2d.com/nizimaaction/manual/updates-history/
- 日期: 手册页 lastmod 2026-06-17；**最新条目 [0.55.3] 2026-10-07**（采集 2026-10-12，**仅 5 天前**）
- 事实（官方原文）:
  - **[0.55.3] 2026-10-07**: 适配 nizima 缩略图新规定尺寸，视频尺寸预设「nizima 動くサムネイル用」由 **400×288 改为 700×504**。旧尺寸项目可通过「プロジェクト」面板 >「編集中のシーン設定」>「サイズ変更」>「解像度」改。
  - **[0.55.0] 2026-09-16**: 限时搭载「**データ保存チェック**」功能——官方原文「**10 月 14 日以降に予定しているデータ保存の仕組みの刷新**に向けて、既存データのチェックと再保存のためのツールを期間限定で搭載」。即检查「只存在浏览器缓存、未保存到服务器」的数据并重新保存。
  - **[0.54.0] 2026-08-31**: 新增**裁切编辑（トリミング）**；播放/编辑 seek **迁移到 WebCodecs 方式**（帧级精度与响应速度提升，可从时间线右上菜单退回旧方式）；引入**低分辨率预览**（可选「自动 / 品质优先 / 速度优先 / 不使用」，**不影响导出画质**）；打开项目时自动检查不支持字体。
  - 版本节奏: 0.49.0(2026-04-15) → 0.50.0(2026-05-27) → 0.50.1(2026-05-28) → 0.51.0(2026-06-17) → 0.52.0(2026-07-09) → 0.53.0(2026-08-05) → 0.54.0(2026-08-31) → 0.55.0(2026-09-16) → **0.55.3(2026-10-07)**。约 **每 3–4 周一个小版本**。
- **重要更正**: 官方站 NEWS 区显示的最新条目是 `[0.48.0] 3/18/26`（见 §八-29），**落后于手册更新履历近 7 个月**。手册 changelog 才是可靠版本源——与 §八-24「README 陈旧」同类问题，**官网营销页与手册不同步**。
- **时效提示**: 官方承诺的「数据保存机制刷新」在 **2026-10-14**，距本轮采集仅 2 天，下轮应复核是否已上线。
- 可复用性: ① 落地 —— 浏览器端 Live2D 视频工作流的版本基线；700×504 缩略图尺寸是做 nizima 投稿的硬指标。

### 31. 【0 命中】nizima LIVE 运行环境一手规格 + Intel Mac 生命周期终点
- URL: https://docs.live2d.com/nizimalive/manual/operating-environment/ （lastmod 2026-03-31）
- 日期: 采集 2026-10-12
- 事实（官方规格表原文）:
  - **Windows**: OS **Windows 11（64 位、仅桌面模式）**；CPU 最大频率 **2.5GHz 以上且 2 核以上**的 Intel/AMD；内存 **4GB 以上（推荐 8GB 以上）**；硬盘 **约 500MB**；GPU 推荐 **NVIDIA GeForce GTX 1060 相当或以上**；显示 1440×900 以上（推荐 1920×1080）；**需联网（许可认证）**。
  - **macOS**: **macOS v14 / v15 / v26**；**Apple Silicon（M1 以降）**；内存 4GB（推荐 8GB）；硬盘 **约 1.3GB**；需 **Metal**。
  - **关键生命周期信息（原文）**: 「**Intel Macには nizima LIVE 2.5.2 まで対応しております**」——**Intel Mac 仅支持到 2.5.2**，即 Apple Silicon 之后 Intel Mac 被放弃。
  - **移动端**: nizima LIVE TRACKER 推荐 **iPhone X 以降 / iOS 14.0 以降 / 存储 500MB**。
  - **技术栈（原文）**: 「nizima LIVEは、フェイストラッキングと分析に **MediaPipe** のSDKを使用しています」——面部追踪用 **MediaPipe SDK**。
  - **macOS 缺失功能（官方明示）**: **虚拟摄像头输出**、**口型同步 LipSync（但 MotionSync 可用）**、**自动更新**、**录制功能** 四项在 macOS 上不支持。
  - **协作（コラボ）版本兼容性**: 1.5.0 及以后版本之间可协作（切换区域需 2.1.0+）；**1.5.0 之前与 1.5.0+ 不可协作**；**1.3.0 之前与 1.3.0+ 不可协作**。
  - 开发方: 株式会社Live2D（nizima チーム）。
- 可复用性: ① 落地 —— **Intel Mac 止于 2.5.2** 是选型硬约束；macOS 缺 LipSync 但对标 MotionSync 可用，是跨平台方案设计的关键取舍。

### 32. 【0 命中 · 更正 gh 路结论】官方手册实为 3 套 WordPress 站，但 **nizima 两个子站没有英文镜像**
- URL: 主站 https://docs.live2d.com/sitemap.xml ；ACTION https://docs.live2d.com/nizimaaction/wp-sitemap.xml ；LIVE https://docs.live2d.com/nizimalive/wp-sitemap.xml
- 日期: 采集 2026-10-12（本轮实拉验证）
- 事实（本轮实测）:
  - 三套站点结构确认: 主站 526 条（editor_manual 241 / editor_tutorials 28 / sdk_manual 179 / sdk_tutorials 77 / page 1）；**nizima ACTION 43 条**（manual 30 / tutorials 12 / page 1）；**nizima LIVE 59 条**（manual 33 / tutorials 25 / page 1）。与 gh 路统计一致。
  - **更正**: gh 路称「各有 `/en/` 英文镜像」——本轮实测 **`/en/nizimalive/...` 与 `/en/nizimaaction/...` 均返回 404**（页面导航中 nizima 两个手册的链接也只指向无 `/en/` 的日文路径）。**即：主站（Editor/SDK）有 en/zh-CHS/ko 多语镜像，nizima 两个子站仅日文**。
  - 主站根路径确无 sitemap 外入口（`/cubismviewer`、`/sdk`、`/viewer` 等均 404），gh 路判断正确。
- **本轮实拉的两个子 sitemap 关键 lastmod（供下轮按日期挑新内容）**:
  - ACTION: `live2d-tracking` 2026-06-24、`browser_app_permission_settings` 2026-06-25、`updates-history` 2026-06-17、`top` / `project-and-scene` 2026-06-22、`export` 2026-06-18、`subtitle-and-voice` 2026-06-22、`audio` 2026-06-08。
  - LIVE: `livetracker_features` **2026-07-06**、`history` 2026-06-19、`samplemodel-terms` 2026-06-03、`operating-environment` 2026-03-31、`livetracker_top` 2026-04-02、`app_menu` 2026-04-07。
- 可复用性: ① 落地 —— 索引站若要把 nizima 手册做成固定扫描项，必须知道**只有日文**，英文读者需走官网营销页。

### 33. 【负结论 · 已核实】Cubism Viewer 官方手册确已下架，非漏扫
- URL: 主站 sitemap（无 viewer 类型）；`/cubismviewer*` 全 404
- 日期: 采集 2026-10-12
- 事实: 主站 sitemap 的 5 个子表（`editor_manual` / `editor_tutorials` / `sdk_manual` / `sdk_tutorials` / `page`）**不含任何 viewer 类型**；`/cubismviewer`、`/viewer` 路径均 404。
- **旁证（gh 路提供，本路认可）**: 官方仓库 `Live2D/CubismViewer` **2018-04-20 停更**、仓库仅 **11 KB**、README 写明「not actively maintained」。
- **判定**: 采纳 gh 路推断——**官方 Cubism Viewer 手册随产品一起下架**，不是本轮漏扫。**但须注明这是推断，官方未发布任何「下架公告」**。
- 可复用性: ② 参考 —— 负结论本身有价值：告诉索引站不要再为 Viewer 手册留扫描位；同时提醒引用 Viewer 教程的读者其官方依据已失效。
