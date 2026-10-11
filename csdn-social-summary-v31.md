# 跨平台游戏制作 × AI 开发资源梳理（2026-10-11 · 第三十一辑 · **不买 Cubism Editor 的那条路，第一次有了完整栈**）

> 本辑三路：gh 路 37 条（20+ 组查询，双时间窗）· cn 路 8 条（采纳 3）· official 路 29 条。
> 落索引 **22 卡**（`index.html` 1257 → **1279 项**）。
> 上一辑原文存档：`csdn-social-summary-v30.md`（不改，append-only）。原始产出在 `_r31/`。
> ⚠️ **本辑与上一辑只隔 22 分钟**（上轮 12:57–13:14 跑完但**未提交未推送**）——
> 本轮开工先补收尾：核对闸门 → 提交 `eb967c3` → 推送 `main -> 08c1940`（179 blob / 13.8 MB）。

---

## 一、上轮待办检查（12 条 → 闭环 0 条 + 抓到 1 条上轮不在账上的问题）

| # | 上轮待办 | 结果 |
|---|---|---|
| 1 | 实测 `moeru-ai/airi` | ⏸ 顺延（本轮主线被「开源替代栈」占了，见 §三） |
| 2 | 走学生优惠 80% OFF | 🔶 **口径已核实到位**（英文首页新旧文案 80%/76% 并存，权威值 80%）—— 但**仍是「没下单」** |
| 3 | 把「三问」真用一次 | ✅ **本辑用上了**：拿它去核 `live2d-auto-pipeline` 与 `J621111/live2d-automation`（都声称单图→模型），见 §三.5 |
| 4 | **房规压缩**（连续第五轮欠账） | ⏸ **第六轮仍未做** —— 现 200/200 行贴顶，见 §八 |
| 5 | 补读 Cubism 5.3.01–5.3.04 | 🔶 部分：核到 **5.3.01 = 2026-02-24**、**5.3.02 = 2026-04-02**、**5.3.03 = 2026-06-16**、**5.3.04 = 2026-09-03**（含各自 beta1 日），**但「各自更新了什么」仍未读** |
| 6–12 | `/skill-doctor`（第十轮）· ollama-vscode · consolidation · 索引加复核日期 · rpycdec · Codex 离线 · `_tools` 版本控制 | ⏸ 顺延 |

**本辑额外抓到一条上轮不在账上的问题**：

- **`insert_guard_probe.py --base-block` 的入参格式是个陷阱**：它默认值是 `aee9fa3:index.html`（**带 `:index.html`**），
  但传裸 sha（如 `--base-block eb967c3`）**不报错**，只是拿到的是 `git show <sha>` 的 **diff 文本**而非文件 →
  锚点计数全部翻倍 → 报出一堆「出现 2 次」的假警。**本轮实测撞了一次**。
  → 归入 **M-0024 家族**（只认了部分表述 = 看不见其余情形）；已写进 §十待办。

---

## 二、本辑一句话

**前五辑一直在 Live2D 上「找工具」，这一辑第一次出现了「一整套不买 Editor 的替代栈」** ——
① 开源替代从「只有个编辑器」补齐成 **SDK 本体 + 绑定界面 + 自动化 CLI**；
②「单图/PSD → 可用模型」这条线**分叉成两条**：一条只在网格层动手（天然绕开 Core ABI 那道墙），
一条直接对 moc3（但导出的是 mock）；
③ 官方两处**口径冲突被定位**（76%/80% 的真相、LEAP 校数 200+ vs 450+），
外加一个**必读的破坏性变更**（`live2d-py` 1.0.0 移除了两个模块）。

---

## 三、主线一：不买 Editor 的路，第一次有了完整栈

### 1. 补齐了「根」：SDK 本体此前一直是漏的

| 项目 | 数字 | 是什么 |
|---|---|---|
| **`Inochi2D/inochi2d`** | **★1811** · BSD-2-Clause · **D** · 推送 2026-10-03 | 开源 2D 木偶（puppet）**动画 SDK 本体**，定位就是 Live2D Cubism 的开源替代 |
| **`nijigenerate/nijigenerate`** | ★314 · BSD-2-Clause · D · 推送 2026-10-10 | 配套的**绑定编辑器**（面向从 Inochi2D v0.8 派生的 nijilive 格式） |
| **`CheshireMew/PuppetLoom`** | ★245 · **AGPL-3.0** · TypeScript · 推送 2026-10-05 | 分层 PSD → **可自动制作、可验证、可校准**的角色；Electron + CLI + **Codex skill**；topics 直接标 `windows` |

> **上一辑的账**：index 里只有 `inochi-creator`（编辑器），**`inochi2d` 这个 SDK 本体一直没被收录** ——
> 等于只记了「有把螺丝刀」没记「有个电动工具台」。本辑补上，这条路才算**从库变成流水线**。
> ⚠️ 代价要写明：**D 语言 + 生态小 + 不能开 `.moc3`**。它不是 Cubism 的替代品，是另一条平行路。

### 2. 「单图/PSD → 可用模型」开始分叉

**分叉点 = 动不动 `.moc3`。**

| 路线 | 项目 | 数字 | 取巧之处 |
|---|---|---|---|
| **只在网格层动手**（不碰 moc3） | `shinshin86/mesh-avatar-studio` | **★597** · MIT · **建仓 7 天** | 一张插画 + 编码 agent → 可动 2D 网格；**因为根本不产 moc3，天然绕开前几辑反复撞的 Cubism Core ABI 那道墙** |
| 同上 | `marukun712/kokoro` | ★42 · MIT | 纯「2D 角色网格变形」库 —— 上面那条的地基 |
| 同上 | `zeikar/iki` | ★15 · MIT | Web 侧开放木偶引擎 + **AI 自动绑骨** + **自带 Claude Code 插件** |
| **双格式输出** | `codewayco/Inkinesis` | ★6 · Apache-2.0 | 文本/图片 → **Inochi2D 与 Live2D 两种 rig**，并拿官方运行时校验 |
| **直接对 moc3** | `J621111/live2d-automation` | ★77 · **无许可证** | 单图 → Live2D 的 **MCP Server**（工具面最全）；但导出的是 **mock `.moc3`** |
| 同上 | `mw2wbyys6t-sudo/live2d-auto-pipeline` | ★10 · Apache-2.0 | Python 全流程（拆分/绑定/导出），目标「全自动产出可部署模型」 |

> ⚠️ **本辑最需要打问号的一句**：「全自动产出可部署模型」。请对照上一辑立的**三问**：
> ① 主指标测的是**美术手作网格**还是**部署用的 auto-mesh**？② 与 baseline 是否**同协议**？
> ③ **眨眼（`ParamEyeLOpen/R`）**这类关键参数在自动分层上成没成？
> → 这两条（`live2d-auto-pipeline` / `live2d-automation`）**三问一条都没答**，且一个 10★、一个导出 mock。
> **结论：登记，不当能力已证实的工具。** 这正是上一辑那把「尺子」第一次真的被拿来用。

### 3. 把 Editor 本身自动化：`cubism-api-bridge`

`sayaka-aiart/cubism-api-bridge` · ★11 · MIT · 推送 2026-09-12 · 作者自评 **Experimental**

- Cubism Editor 官方 **External API** 的非官方 TS/Python 桥 + **本地 HTTP 服务**，附 StandRig 集成。
- **价值**：前几辑的结论是「Editor 授权买的是**绑骨**，渲染用的 Core 免费」——
  这条正面回答「那**绑骨这步能不能自动化**」。
- ⚠️ 两个前提：External API 是**付费版功能**；非官方桥意味着官方一改 API 就可能断。

### 4. Godot 侧出现了第二个 Cubism 集成

`pakholeung37/gd_cubism` · **★0** · 许可证不明 · C++ · 推送 2026-09-16

- Godot 的 Cubism 集成，带**批渲染与屏幕空间遮罩图集**。此前这条路只有 `MizunagiKB/gd_cubism`（已在库）。
- ⚠️ **0★、许可证不明、建仓不足月 → 仅 README 级核实，不要当依赖**；
  更关键的是**它没说吃哪一版 Cubism Core** —— 而这正是前几辑判定「能不能用」的那个数字。

### 5. 桌宠 / agent 形象这一簇：主干之下开始分层

| 项目 | 数字 | 判定 |
|---|---|---|
| `morettt/my-neuro` | ★1389 · MIT · JS · 推送 2026-10-05 | ✅ **第二梯队里最成熟的**（长期记忆 / 视觉 / 声音克隆），拿它当对照能画出「主干 vs 玩具」的分界线 |
| `Playa-Cyrene/Cyrene-Agent` | ★697 · MIT · TS | ✅ 带虚拟形象的桌面 agent，与上一条同赛道但侧重「agent 本体」 |
| `cqzaaa/AgentPet` | ★262 · **无许可证** · TS | 🔶 **功能面最全之一**（Live2D 外观 + ACP 多 agent 调度 + Computer Use + SSH）→ 但**无许可 + 权限面大**，只读参考 |
| `AOrbitron/Eridanus` | ★206 · **许可不明** · Python | 🔶 OneBot 框架，但支持「**不接 IM 的纯 Live2D 桌宠模式**」——反过来把平台层剥掉，对只想摆桌宠的人反而干净 |
| `Xinrea/JPet` | ★105 · MIT · **C++** | ✅ **「低占用」这个维度目前只有它值得看** —— 前面那些桌宠全是 Electron/Python/TS，启动就吃几百 MB；但它用的 Live2D 栈版本要自己核 |
| `MacchaPafe/D_sakiko` | ★96 · GPL-3.0 · Python | ✅ 形象 + agent + **GPT-SoVITS 声音克隆**，补上「音色一致性」这块 |
| `moonrailgun/vtubeleaf` | ★13 · MIT · Tauri | ✅ **会议场景**的本地 Live2D 面捕；Tauri 栈比 Electron 轻得多 |
| `NekoUnix/A.R.I.A` | ★10 · MIT · Rust | 🔶 Alpha；野心是「一个工作室管 Live2D/PNG/VRM/GLB 所有形象格式 + 多形象 OBS 输出」，方向没成熟品 |
| `StudioRaming/warudo-agent-bridge` | ★9 · MIT · C# | 🔶 **MCP server + CLI 让 agent「看到并驱动」WARUDO** —— 思路（把别人的演播软件变成 agent 的手脚）比工具本身值钱；但底座 WARUDO 要钱 |
| `Jelosus2/BD2-L2D-Viewer` | ★540 · MIT · Vue | ✅ Web 端 Live2D + Spine 查看器 —— 前几辑遇到的 viewer 都是 0★ 个人件，这条是**可抄的成熟参考** |
| `DasterProkio/awesome-ai-companion` | ★914 · CC0-1.0 | 🔶 **不是代码是清单**，可直接当下几轮的选题地图 |

---

## 四、主线二：官方口径——两处冲突被定位，一个破坏性变更

### 1. ⚠️「76% vs 80%」的真相：**不是两站打架，是同一张英文首页自己没统一**

`live2d.com/en/` · 2026-10-11 逐段读到

| 位置（**同一张英文首页**） | 写的是 |
|---|---|
| Student Discount 卡片（可见区） | **80% OFF** the Cubism PRO 3-Year Plan |
| 下方「How-to Guide」段落 | receive a **76% OFF** coupon for a 3-year PRO subscription |

> **上一辑记的「英文站 76% vs 简中站 80%」，根因说错了** —— 不是区域差异，是英文首页**新旧文案并存**。
> **权威取值 = 80%**（学生专页 + `store.live2d.com/en` 结算页 + 简中页三处一致）：
> 原价 $231【¥36,720】/3yr → **学生价 $46【¥7,344】**，**截止 2027-03-31**，属 20 周年「Shape the Future」企划。
> → **结论升级：不是「以区域为准」，是「以结算页为准」，且同一站内也可能自相矛盾。**

### 2. ⚠️ 第二处冲突：LEAP 覆盖校数「200+」vs「450+」

- `live2d.com/en/` 首页：「has now supported **over 200 schools**」
- LEAP 中/英文专页：「**more than 450** educational institutions … approximately **48,000** student users（*As of March 2025*）」

> 同一计划、两个数、**差一倍以上**。索引中应以 **LEAP 专页的「450+ / 截至 2025-03」**为准。

### 3. SDK 版本：上一辑「全线 5-r.5」的说法要修正为「**分线各自版本**」

| 线 | 版本 | 日期 |
|---|---|---|
| **Unreal** | **R1 beta2** | **2026-09-29** ← **全线最近一次更新** |
| MotionSync（Unity / Native） | **R2_1** | 2026-08-25（**Web 端仍停在 R2**，2025-03-27） |
| Java | R5 | 2026-06-04 |
| Unity | **R5（2026-04-02）与 R4_2（2026-05-14）并存** | ⚠️ **R4_2 晚于 R5 不是倒退**，是 R4 线的维护版 → 别误判「R4_2 是最新的」 |
| Native / Web | R5 | 2026-04-02 |
| **AE Plugin** | **R7 正式版** | 2026-05-21（前序 R7 beta1 = 2026-03-26） |

- **仍无 5-r.6、无 6.0**；Editor 仍 **5.3.04**（2026-09-03）；**5.4 只有 Editor alpha，无配套 SDK**。
- 5.3 系列 patch 日期补齐：**5.3.00 = 01-20 · 5.3.01 = 02-24 · 5.3.02 = 04-02 · 5.3.03 = 06-16 · 5.3.04 = 09-03**。
- 产品页 `Latest Updates` 仍只列 **5.3.00** vs docs 表 **5.3.04** —— **这条冲突挂了两辑，官方仍未修**。

### 4. ⚠️ 必读的破坏性变更：`live2d-py` 升到 1.0.0

`pypi.org/project/live2d-py` + GitHub Releases · **v1.0.0 = 2026-09-30** · 仓库 ★576、当日仍在更新

- 变更：v2/v3 模型统一用 `live2d.Model` 加载（**部分接口名变更**）、**移除 `live2d.v3` 与 `live2d.v2cpp` 模块**、减少默认日志。
- **影响面**：任何写过 `from live2d.v3 import ...` 的 Python 代码**升级后会直接报错**。
- 版本线：0.6.1(01-16) → 0.7.0(05-20) → 0.8.0(09-24) → 0.8.1(09-26) → **1.0.0(09-30)**。

### 5. 两条官方新动向（非 SDK）

- **`live2d.jp/news/live2d-chapters/`（2026-05-22）**：官方启动 **『Live2D Chapters』**，正式支援全球各地用户社区。
- **`live2d.jp/news/simple-license-nizimalive/`（2026-04-30）**：把 **nizima LIVE 纳入「著作物简易授权方案」** → 授权面变化。
- 另：**live2d.com 英文新闻自 2026-07-17 起近 3 个月无新增**（5.3.01~5.3.04 四个 patch 都没发新闻稿）→ **别把「新闻停更」误读成「项目停摆」**。

---

## 五、中文侧：终于有可执行的「接单 / 验收」口径（不是教程）

> ⚠️ 如实记：本轮 **CSDN 零采纳**（抽到的 `weixin_*` 帖几乎全是 AI 模板农场，且 WebFetch 普遍被「安全验证」页拦，**无法核首发日**）；
> **`zhihu.com` / `bilibili.com` 正文全被登录墙拦**；`live2dhub.com` 本轮零命中。

### 1. ✅《【LIVE2D-Vtuber】拆圖解說分享》——妄想販售屋（繁中接单工作室）

`mosouriya.com` · 页面仅标「已更新：9月5日」· **年份未核实**

**本辑最贴合「立绘拆分可执行」的一条**，全部是可照抄的判据：

- 身躯拆**上半身 / 下半身**两块（让呼吸、前后倾、左右转体各自独立）；**背面图层不能省**（否则转身空洞发扁）；
- 手拆**手臂 + 手掌**，且**手背与手心/侧面必须分开**（翻转时才不出透视错）；
- 脚拆**大腿 / 小腿 / 脚掌**，且接缝要留足「**出血范围**」；
- **所有投影阴影必须独立图层并设「乘算」模式**（底层换色阴影仍对）；
- 同系列「頭部」篇：头发拆前发 / 侧发 / 长侧发（**长侧发还要再分子件**）/ 后发 / 头饰 / 亮部 / 阴影。

→ **「阴影独立层 + 乘算」「手背/手心分件」「出血范围」这三条可以直接落进立绘规格书。**

### 2. ✅ 两份报价单，互为「个人 vs 商业」「简版 vs 一条龍」两种口径

| | 米画师「且明」橱窗 | Clibo 凌零依 |
|---|---|---|
| URL | `mihuashi.com/stalls/912393` | `clibo.tw/commissions/NmVzvW` |
| 日期 | 截稿 2026-09-30（发布日未显示） | **刊登 2026-09-25 / 更新 09-26**（已核实） |
| 底价 | ¥18,000（加塞 ×1.5） | NT$15,000+ |
| 授权 | **默认商用使用权**，但**不可买断 / 不可二改 / 不可量贩转卖 / 严禁公皮** | **含商业使用权、永久保固、修改不限次数** |
| 分期 | **10% 定金 → 30% 线草 → 50% 色草 → 70% 精草 → 100% 成稿** | 确认拆分档后先付 **50%** → 尾款 |

**Clibo 那条给的是「合格模型」的最低共识（可直接当自检线）**：
**头部 X 轴 ≈30° / Y 轴 ≈15° / Z 轴 ≈10° + 果冻眼 + 呼吸 + 一般头发物理 + 一般服装物理 + 赠 3 个静态表情**；
加购明码：加表情 200NT、动画面部表情 300NT、服装穿脱 1000NT、加发型/衣装 1000NT、**VBridger 口型 2000NT**（吐舌/歪嘴/鼓嘴/嘟嘴/抿嘴/咀嚼）。

### 3. 🔶《图形引擎实战：Live2D 项目应用及落地》的姊妹信息 + 两条排查法

- **《物理演算页面中未反映身体的 Y 轴》**（`creatorsforum.live2d.com/t/topic/3958/2`，**403 未读到正文，仅摘要级**）：
  「头发会动但身体 Y 轴不动」多半**不是物理没生效**，而是**「光标跟随设置」没包含「身体旋转 Y」** →
  三步：① 预览→光标跟随设置是否含目标参数 → ② 该参数是否也在「输入设置」里 → ③ 「输出设置」是否含要摆动的参数。
  > ⚠️ 该站被 discourse **403（IP 临时限制）**，下轮建议改人工浏览器取帖。
- **ABOUTCG 课程大纲**（`aboutcg.org/courseDetails/2400`，无日期、售课页）：
  把业内标准工序顺序给全了 —— **九轴制作**（布点→参数→变形器→X 轴→Y 轴→四角合成→身体 XY）→
  **五官与口型**（**胶水(glue)权重**→眼眉→嘴→物理链）→ 表情动作 + **VBridger 口型** → 导出与面捕。

---

## 六、⚠️ 编造专区：中文 AI 教程在骗你什么（本辑新增留痕 3 例 + 1 例复现）

> 共同特征未变：**教你垂直软件的具体功能名，但给不出官方出处**。

| 例 | 原文声称 | 真相 |
|---|---|---|
| `hnnews.cc`（怀宁新闻网）《AI生成2D骨骼动画的工具指南》 | 「**Live2D AI 智能交互引擎**」「语义分割自动拆分准确率 **98% 以上**」「**自适应骨骼绑定**」「某团队 **3 小时**完成原需 **2 周**的 **20 个 NPC**」「成本降低 **90%**」 | **Cubism 没有这些功能**；98% / 90% 全无出处。**编造功能 + 编造精确百分比**，本辑最典型 |
| `weixin_31458015/164005931` | AI 能「**自动生成可动的 Live2D 模型参数**」「**绕过最繁琐的拆分与绑定两步**」 | 现役图像/LLM **无法自动产出可用的 `.moc3` 与绑定** |
| `elser.ai` 厂商博客 | 「直接用 AI 生成**完整 Live2D 素材，完全跳过绑定流程**」 | 厂商卖点话术，当前不成立 |
| **复现** `weixin_30843121/164972177` + `bryh.cn` / `tzjp.cn` 镜像 | Cubism 5.3「**新增 6 种混合模式**」「**Motion Trail**」 | 上一辑已判；**本轮再次浮出并带同文镜像** → 该批镜像仍在持续分发，见到直接剔 |

**红牌术语表（下轮直接比对，不必重新论证）**：
`.pmx` 导出（那是 MMD 格式）· `MeshFitting` · `ParameterMixer` · `AI 面部自动生成` ·
物理参数写成「摩擦力/反弹力」（真实术语是**质量 / 移动 / 阻力 / 弹性 / 重力方向**）·
`config.live2d_fps`（不存在，真正开关是 `config.gl2`）· 「Motion Trail」。

---

## 七、索引与文档维护（本轮落盘）

- `index.html` **1257 → 1279 项**（卡片 1246 → **1268**，**第三十六版增补 22 卡**，脚注 [1257]-[1278]）
  - 新建 `insert_v36_cards.py`；跑前过 `insert_guard_probe.py` **6/6**
    （⚠️ 本轮实测：`--base-block` **必须写成 `<sha>:index.html`**，传裸 sha 会静默读成 diff → 假警）
  - 跑后 `index_metrics.py` 全绿，并 `--update` 重封 **306** 个分组
- 恒等式：**页头 1279 == 最大脚注 1278 + 1** ✅ · div **10999 / 10999** ✅
- 上新存档 `csdn-social-summary-v30.md`
- **补收尾上一辑**：上一轮（第三十辑，12:57–13:14）跑完**未提交未推送** →
  本轮核对闸门全绿后提交 `eb967c3`、推送 **`main -> 08c1940`**（179 blob / 13.8 MB）
- **查重基线**：`_r31/_dedupe_gh.txt` = 从 `index.html` **现场生成**（1230 条）+ `_r31/_dedupe_urls.txt`（475 条）
  — 沿用上一辑的治标修复（M-0031）
  - gh 路另做了**二次兜底**：直接对 `index.html` 现取链接再比一遍，抓到 `stevenjoezhang/live2d-widget`、`A8Chann/dsh-pet-live2d` **两条基线漏收**（已在 index 里）
  - 本辑 22 条候选**逐条 grep 命中 0**

---

## 八、自测：收集到的 AI/资源，哪些能直接改（只落地有信号的）

**✅ 已落地 1：破坏性变更进「版本钉子」** —— `live2d-py` **1.0.0（2026-09-30）**、移除 `live2d.v3` / `live2d.v2cpp`。
属于「写死过 import 的地方会断」那一类 → 与 `AGENTS.md` §十 的钉子表同构。

**✅ 已落地 2：「同站内也可能自相矛盾」补进口径纪律** —— 上一辑写的是「核对版本/价格必须写清**哪一站哪一页**」；
本辑把根因纠正为**同一张英文首页内部新旧文案并存** → 纪律升级为
**「以结算页为准，且同一站内跨区块也要交叉验证」**。

**🔶 观察**：`Inochi2D/inochi2d` + `nijigenerate` 这对组合是**唯一不买 Editor 的完整开源栈**，
但入口语言是 **D**，与本机 Python/JS 主线不搭 —— **先记录，不投入**（真要试，先确认 Windows 上 dub 工具链能装）。

**❌ 不采纳**：`khinson-lin` 式 0★ 占位仓；`pixi-live2d-display`（**三年未更新**，dist-tags 停在 2023-12-07）；
`easy-live2d` / `live2d-motion3`（**在 npm / crates.io / PyPI 均查无此包** → 上一辑的记载应改为「以该名不存在」）。

---

## 九、下一辑待办

**本辑新出**

1. **实测 `moeru-ai/airi`**（连续两轮顺延，本辑最高分）—— 只跑 Windows 桌面端，
   核一件事：它自带的 Live2D 运行时**吃哪个 Cubism Core 版本**
2. **核 `Inochi2D` 栈在 Windows 上到底能不能装起来**（D 语言 + dub 工具链），
   这是「不买 Editor」这条路能不能走通的唯一前置
3. **补读 Cubism 5.3.01–5.3.04「各自更新了什么」**（本辑只核到日期）
4. **修 `insert_guard_probe.py` 的 `--base-block` 入参陷阱**：传裸 sha 应报错或自动补 `:index.html`
5. **房规压缩** —— **连续第六轮欠账，200/200 行贴顶**。下一辑第一件事就干，
   按既有倾向的方案 ②：把「调研方法」类条款整体拆进 `game-production-pipeline.md`

**承接老账（顺延）**

6. `/skill-doctor`（**连续第十轮**）· 7. 装 `ollama-vscode` + 跑 `agnix` · 8. 做一次 `consolidation`
9. **索引条目加「最后复核日期 + 是否作废」**（本辑「英文首页 76%/80% 并存」「R4_2 晚于 R5」都是同一类问题）
10. `rpycdec` 反编译自查（**欠十四轮**）· 11. Codex 离线 / 词表 / 模型分档 · 12. `_tools/` 与 `AGENTS.md` 版本控制

---

## 十、搜索覆盖与去重报告（摘要）

| 路 | 覆盖 | 结果 |
|---|---|---|
| gh | **20+ 组查询**（live2d / cubism / moc3 / motion3 / vtuber / godot / unity / web / psd / mcp / agent / desktop pet / renpy / alternative / in:name / in:readme），双时间窗 `pushed:>2026-09-25` + `created:>2026-09-01`；约 90 次单仓库 `gh api` 核实 | 立条 37（✅23 / 🔶9 / ❌5）；剔除已收录 25 |
| cn | 21 组检索式（**不用 `site:`**，站名当普通关键词） | 采纳 3 / 观察 5；剔除 25+（`hqwc.cn` / `mhpq.cn` / `bryh.cn` / `tzjp.cn` / `cr173.com` / `smzdm` 聚合稿等） |
| official | live2d.com 首页+Information / live2d.jp / docs Release History / SDK 下载页 / **10 个 GitHub Releases 仓库** / npm·PyPI·crates.io registry API / arXiv·pith / HN Algolia / dev.to / store·student 结算页 | 29 条（含 8 条负结论），**0 重复** |

**负结论（别下轮再单独投入）**：

- **`live2d+renpy` 两个时间窗都是 0 结果** —— Ren'Py 侧已无新料，下轮不必再投。
- **`in:readme live2d` 命中 1487 条、噪声率 ~95%**（博客 / awesome 列表 / AI 百宝箱里提一句就算命中）→ 改用 **`in:name live2d`**（117 条，质量明显更高）。
- **`vtube` / `vtuber` 两个词信息量极低**：绝大多数是索引站、粉丝页、播放量追踪、日程工具，与「制作 / moc3 / 桌宠」无关 → **必须带 `live2d` 或 `moc3` 限定**。
- **`cubism` 有大量同名噪音**（立体主义画派、图书馆座位管理 `Cubismart`、设计系统）→ 同理需限定。
- **`motion3` 几乎全是噪声**（"motion 3d" / 物理作业 / 隐私政策），本轮唯一沾边的 `arkrolin/VLive` 0★无许可，不采。
- **DSH（DeepSeek Harness）桌宠是当前最密集的增量簇**（`dsh-whale-girl-live2d` / `dsh-pet-live2d` / `dsh-live2d-avatar` / `dsh-pet` / `dsh-live2d-widget`…），但**重复率极高**，且多条已收录 → 下轮可专门按 `dsh` + `live2d` 一次性收口。
- **HN / dev.to 在 Live2D 上仍是无料源**（HN `live2d` 近一年无相关 story，唯一高相关旧帖是 2023 年的 "Live2D Is a Security Trainwreck"；dev.to tag 最新 2026-06-08）。
- **退役源复测不变**：`gamemale.com` 未再投入（上轮已判 Cloudflare Turnstile 结构性退役）；Reddit / Medium / YouTube / itch.io / note.com 全部 **HTTP 000**。
- **英文 SEO 榜单站一律不采**：`statpit.com` / `sigmadax.com` / `tech-insider.org` / `streamer.guide` / `magicmotionstudio.com` / `betuber.com` / `sorceress.games` / `aiparabellum.com`（自带 affiliate 声明的「Top 10 工具榜」）。

---

*本辑三路候选：gh 37 条 · cn 8 条 · official 29 条；落索引 **22 卡**；*
*累计经验帖约 1440 → **约 1465 条**；索引 **1279 项**；房规 23 条 / 200 行（贴顶）；决策原则 23 条 / 224 行；mistakes **32 条**；*
*新建脚本：`insert_v36_cards.py`；新存档：`csdn-social-summary-v30.md`；补收尾：第三十辑已推送 `08c1940`。*
