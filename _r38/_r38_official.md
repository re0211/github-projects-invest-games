# 第三十八辑 · official 路（Live2D 官方 / note.com / 海外社区）

> 子 agent 分工：official 路 —— Live2D 官方（Cubism 官网 / Editor release notes / SDK 更新）+ note.com（日本创作者）+ Reddit r/Live2D + creatorsforum.live2d.com + Hacker News + X/Twitter + 海外测评/新闻。CSDN/GitHub 交其他子 agent。
> 采集日期：2026-10-11。产出仅本文件，不改动 index.html / csdn-social-summary.md。
> 可复用性三档（基准 = 16GB Windows + 本地 Ollama + 维护索引站的个人）：① 落地 ② 参考 ③ 不采用，各 1 行理由。

---

## 一、搜索覆盖

| 路 | 覆盖源 | 结果 |
|---|---|---|
| official 官网 | live2d.com 公告 / docs.live2d.com updates-history / Cubism 5.4 SDK(R7 alpha1) 手册 / creatorsforum | 已取（官网 news 根域 404，改从 announced 公告页 + 手册 + 论坛 JSON 端点绕过 403） |
| note.com | note.com/search?q=Live2D | 未取到（本机 fetch failed，TLS 000；与上轮一致） |
| 海外社区 | r/Live2D / HN algolia / 海外测评站 | r/Live2D 未取到(fetch failed 000)；HN 无 Live2D 真 story；gitnux/zipdo/wifitalents/worldmetrics 4 站已取 |
| X / Twitter | #Live2D / @Live2D | WebSearch 取 @Live2D 2026-07-14 公告 |

---

## 二、本路一句话主线

**Cubism 5.4 截至 2026-10-11 仍为 alpha2（可用期延至 2026-10-18，未转 beta）；本路拿到一批 0 命中基线的一手新事实——SDK R7 alpha1 三项 breaking change、5.4 alpha2 启动崩溃帖、Unreal 支持「未停止开发」、以及 2026 年四家海外 VTuber rigging 榜单将 Live2D 列为行业标杆。**

---

## 三、官方一手（Cubism 5.4 / release notes）

### 1. Cubism 5.4.00 alpha2 当前状态（官方一手核心）
- URL: https://www.live2d.com/zh-CHS/information/cubism-5_4-alpha
- 日期: alpha2 发布 2026-09-07；采集核对 2026-10-11
- 事实: 5.4 仍为 **alpha 阶段（alpha2）**，公开可用期延至 **2026-10-18**；alpha1 已于 2026-09-14 下线。官方公告明确「待 alpha 版公开并确定各项功能规格后，将进入 Beta 版阶段」——截至本轮（2026-10-11）**尚未转 beta**。
- 可复用性: ① 落地 —— 直接记录为官方版本基线，索引站维护必存。

### 2. Cubism Editor 正式线 5.3.04 为最新
- URL: https://docs.live2d.com/cubism-editor-manual/updates-history/
- 日期: 2026/09/03（5.3.04）；采集 2026-10-11
- 事实: 正式线最新为 **5.3.04（2026-09-03）**，无 5.3.05。更新履歴页顶部标注「Cubism 5.4 alpha を公開中」。
- 可复用性: ② 参考 —— 正式线用户仍停留在 5.3.04 即可；5.4 仅 alpha，不建议上生产。

### 3. Cubism 5.4 SDK = R7 alpha1（术语对齐）
- URL: https://cubism.live2d.com/link/manual5_4_alpha_sdk_zh
- 日期: R7 alpha1 手册；采集 2026-10-11
- 事实: 官方术语——`Cubism 5 SDK` = R6 及之前；`Cubism 5.4 SDK` = **R7 alpha1 及之后**。SDK 手册 alpha2 直链仍 **404**，仅 alpha1 手册 200（与 r32/r34/r36/r37 一致复现）。
- 可复用性: ① 落地 —— SDK 版本号对齐是集成的硬前提。

### 4. [breaking] SDK R7 alpha1：模型计算顺序变更
- URL: https://cubism.live2d.com/link/manual5_4_alpha_sdk_zh
- 事实: Unity 改为与 Native / Web Original Workflow 一致，**物理演算结果与 R5 正式版不同**。
- 可复用性: ① 落地 —— 已接 Unity SDK 的 VTuber / 游戏项目必须重测物理表现。

### 5. [breaking] SDK R7 alpha1：Json Version Tag 识别
- URL: 同上
- 事实: 引入 Version 标签识别，**含未识别 Version 标签的 JSON 将无法加载**（强制版本校验）。
- 可复用性: ① 落地 —— 旧模型 JSON 升级前必须确认 Version 标签合法。

### 6. [breaking] SDK R7 alpha1：Parameter Controller 嵌入数据
- URL: 同上
- 事实: 加载 `.paramctrl3.json`；参数控制器 alpha1 **仅 Unity SDK 支持**，其他平台 beta1 后提供。
- 可复用性: ② 参考 —— 非 Unity 平台暂不可用，规划时避开依赖。

### 7. 新功能：Parameter Controller SDK Support（参数控制器 SDK 支持）
- URL: https://www.live2d.com/zh-CHS/information/cubism-5_4-alpha
- 事实: 含 **IK**、**target-only controller（可沿路径跟随）**。编辑器与 SDK 两侧可用（Unity 先落地）。
- 可复用性: ① 落地 —— 自动绑定 / 反向动力学关键能力，rigging 工作流核心升级。

### 8. 新功能：Model State Set（模型状态集）
- URL: 同上
- 事实: 保存 / 切换**显示·锁定·参数键值**；属编辑器功能，**SDK 不支持**。
- 可复用性: ② 参考 —— 编辑器侧工作流增强；运行时侧暂不能读取。

### 9. 新功能：External Application Integration API 编辑功能扩充
- URL: 同上
- 事实: 对象编辑 API 扩充（编辑器 UI 能力），**SDK 不支持**。
- 可复用性: ② 参考 —— 外部联动 / 批处理工具开发参考。

### 10. 新功能：Enhanced auto layout for texture atlases（纹理图集自动布局重做）
- URL: 同上
- 事实: 纹理图集自动布局**算法重做**，出图排布更优。
- 可复用性: ② 参考 —— 出图效率提升，非阻塞性改动。

### 11. X @Live2D 2026-07-14 发布 5.4 功能预告
- URL: https://x.com/Live2D（搜索 2026-07-14）
- 日期: 2026-07-14
- 事实: 官方推文预告 5.4 新功能（参数控制器 / 状态集 / 外部联携 API 扩充 / 纹理自动布局），与官网公告相互印证。
- 可复用性: ② 参考 —— 交叉印证官方口径，无新增事实。

### 12. 海外媒体上手：Cubism 5.4 alpha2（Softpedia / CGVisual）
- URL: Softpedia News「Live2D Cubism 5.4」、CGVisual 上手报道（2026-09）
- 日期: 2026-09
- 事实: 海外媒体对 5.4 alpha2 的上手报道，重点新参数控制器与纹理重排。
- 可复用性: ③ 不采用（二手，已被官方一手覆盖）—— 仅作传播佐证，不进索引正文优先级。

---

## 四、note.com 创作者

- **未取到**（本机 `fetch failed`，TLS 重置 000；与 r32/r34/r36/r37 一致复现）。
- 候选检索式 `note.com/search?q=Live2D` 本轮未返回有效内容，故无日本创作者经验帖 / 教程 / 资源配布可落盘。下轮建议换用 WebSearch 代理或异地网络重试。

---

## 五、海外社区（r/Live2D / 论坛 / X / HN）

### A. creatorsforum.live2d.com —— Cubism 5.4 alpha 分类（JSON 实取，10 帖）
- URL: https://creatorsforum.live2d.com/c/cubismeditorsdk54alpha.json
- 日期: 采集 2026-10-11（HTML 端点 403，改用 `.json` 端点绕过）
- 子条（均官方板块，带来源 id）：
  - **id 3969**「Cubism Editor 5.4.00 alpha2」官方帖，2026-09-07，1336 浏览——alpha2 发布主帖。
  - **id 3983**「alpha2 启动 NullPointerException（command_loginApplication）」官方 2026-10-05 仍在查——**alpha2 启动崩溃**已知问题（0 命中基线）。
  - **id 3976**「急需回退 5.4alpha1」官方 2026-09-17 回复确认 **alpha1 已不可用**（不可回退）。
  - **id 3973**「Unreal Engine 支持」官方 2026-09-09 回复「**未停止开发**」（0 命中基线）。
  - **id 3989**「外部联携 API 增左右反转 / 复制功能」需求帖，2026-10-05。
  - **id 3953**「External Integration APIs 文档错别字」——文档勘误。
- 可复用性: ① 落地 —— 5.4 alpha 用户必看已知问题清单（启动崩溃 + alpha1 不可用 + Unreal 路线图）。

### B. Reddit r/Live2D
- **未取到**（本机 `fetch failed`，TLS 重置 000）。记本轮未命中，交其他路或下轮补。

### C. Hacker News
- algolia `search?query=live2d&tags=story` **无 Live2D 真 story 命中**，本轮不产条目。

### D. 海外 2026 VTuber rigging 软件测评榜（gitnux / zipdo / wifitalents / worldmetrics）
- URL:
  - https://gitnux.org/ （2026 VTuber rigging software 榜单）
  - https://zipdo.co/ （同类榜单）
  - https://wifitalents.com/ （同类榜单）
  - https://worldmetrics.org/ （同类榜单）
- 日期: 2026 年榜单
- 事实: 四家 2026 榜单一致将 **Live2D Cubism 列为行业标杆 / 最高分**；竞品定位——**Inochi2D** 免费开源替代、**Spine** 适合引擎多运行时管线、**VTube Studio** 为运行时（Inochi2D / Spine / VTube Studio 为已覆盖重复项，本组仅补 2026 排名新证据，0 命中基线）。
- 可复用性: ② 参考 —— 选型与外部对标素材；具体产品介绍见已覆盖基线，不重复展开。

---

## 六、AI 开发/使用相关（[AI] 标记）

- **本轮 official 路未采集到明确的 AI 一手**：Cubism 5.4 / 官方公告 / SDK R7 alpha1 均无 AI 特性；note.com 与 r/Live2D 未取到，X 仅取到 5.4 功能预告（无 AI）。
- [AI] 关联提示：若需「AI 辅助 rigging / 自动绑定」「VTube Studio AI 面部追踪」「本地 Ollama 驱动 Live2D 口型/表情」类内容，建议并入其他路或下轮补采，本路不重复覆盖。

---

## 七、去重报告

- **去重方式**：对四个基线文件执行 `grep -iF "<候选专属串>"`
  - `index.html`、`csdn-social-summary.md`、`csdn-social-summary-v36.md`、`csdn-social-summary-v34.md`
- **候选总数**：正文条目 18 条（§三 12 + §四 1 + §五 4 + §六 1），含 §五-A 子条 6 帖。
- **剔除数**：2 条全文剔除（泛述重复）；3 条核心状态标注「重叠但保留为 anchor」。
- **剔除清单（命中基线，判重复）**：
  1. `Inochi2D` 泛述 → `index.html` 38 处、`csdn-social-summary.md` 7 处，多轮已覆盖 → **剔除**（不重复展开）。
  2. `VTube Studio` 泛述（运行时定位）→ `index.html` 17 处，已覆盖 → **剔除**。
- **重叠但保留为 anchor（不计入剔除，仅标注）**：
  3. `Cubism 5.4 alpha2` 核心状态（可用至 2026-10-18 / 未转 beta）→ 串 `2026-10-18` 在基线 8 处，属旧闻同状态，保留为官方 anchor。
  4. `Editor 5.3.04` 最新 → 串 `5.3.04` 在基线 5 处，保留为 anchor。
  5. `外部联携 API` 需求帖 id 3989 → 串 `外部联携 API` 在基线 3 处，保留具体新帖并标注。
- **净保留新事实（0 命中基线，确为新）**：command_loginApplication 启动崩溃(id 3983)、Unreal「未停止开发」(id 3973)、Json Version Tag 校验、模型计算顺序变更、gitnux/zipdo/wifitalents/worldmetrics 四家 2026 榜单、Parameter Controller SDK Support / Model State Set / Enhanced auto layout 三项功能点。
- **未取到源**：note.com（fetch failed 000）、r/Live2D（fetch failed 000）、HN（无 story）、官网 news 根域（404）。

---

