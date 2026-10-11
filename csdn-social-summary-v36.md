# 跨平台游戏制作 × AI 开发资源梳理（2026-10-11 · 第三十四辑 · **「身体」侧的供给第一次压过「格式」侧；官方一手给出了「模型越做越存不动」的根因**）

> 本辑为 Live2D 连续第十轮。**这一辑的看点从「墙」挪到了「墙两边的人」：**
> ① 「绕开 Cubism 的绑定」这条线第一次出现**可验证流水线** —— `rig-c/core` 把 rig spec 编译成 **Spine 4.3**，
> 先做命名断言 + round-trip 校验、**只输出通过校验的结果**，并以 agent skill 形式分发；
> ② 官方论坛 **4 条一手正文全是新增**，其中最有用的一条把「模型越做越存不动」的根因说穿了 ——
> **不是文件大（470MB），是参数数「相乘」爆炸**，解法 = **blend shape（加法）替代普通 key**；
> ③ 桌宠「身体」侧供给本辑最密集（N.E.K.O ★3044 / Soul-of-Waifu ★1386 / duty-on / dsh-live2d-avatar / WuziDesktopPet）。
> 三路候选：gh 路 34 条正文 + 26 行边缘登记 · cn 路 22 条 · official 路 25 条；落索引 **24 卡**（1325 → **1355**）。
> 所有 ★ / 许可证 / 日期均走 `gh api repos/<r>` 实取，**主 agent 已把 20 个候选仓库逐条复验，零出入**（见 §十）。

---

## 一、上轮待办检查（10 条 → **闭环 5 条 / 半闭环 1 条 / 顺延 4 条**）

| # | 上轮待办 | 状态 | 结果一句话 |
|---|---|---|---|
| ① | **`/skill-doctor`**（连续第十二轮，要求排在所有调研动作之前） | ✅ **闭环** | **本轮第一次真做**：21 个技能逐个体检（行数/token/description）+ 统计使用痕迹。**14/21 在全仓 93 万字记忆里零命中**；同时发现本自动化的专用技能 `round-research-index` 早已存在却未被显式加载 → 本轮开工即加载。详见 §五.1 |
| ② | `Agent-desktop-pet` 装/不装做决定（装 3.12 还是改 vendor） | ✅ **闭环（并推翻了上轮的结论）** | 上轮结论「装不上，因为要 CPython 3.12」**只对了一半**：`gh api repos/<r>/tarball` 拿到包后实测，**状态读取侧（`agent_state.py`，101KB）只依赖标准库，本机 3.13.12 直接跑通**，正确识别 codex / claude / dsh / workbuddy。**3.12 只是 GUI 侧（pythonnet + pywebview + `_cffi_backend.cp312-win_amd64.pyd`）的门槛**。详见 §五.2 |
| ③ | `updated_at` vs `pushed_at` 落进卡片模板 | ⚠️ **半闭环** | **新卡已落**（v39 起 src 行固定同时打印两个日期，差 >30 天标「⚠️ 假活」）；**1290 张旧卡未回填**（要动 1338 张卡，留下一轮）。且本轮**新发现一种反向异常**：`duty-on` 的 `updated_at` 比 `pushed_at` **还旧** → 规则必须**双向** |
| ④ | `wan-h/awesome-digital-human-live2d`（★2425）正面评一次 | ✅ **闭环** | **它不是制作工具，是「数字人 web 应用」的一站式脚手架**：Docker 部署、**配置要求低于 2 核 2G**、接 Dify/FastGPT/Coze、ASR/LLM/TTS 模块化。但有两条硬伤：**开源版最后推送 2026-05-18（5 个月）**，且功能在往官网 SaaS 收（个人应用管理 / 内置服务接入 / 分享 = 官网独有）。结论 **⚠️ 参考**。详见 §五.3 |
| ⑤ | DSH 插件生态单独成辑 | ❌ 顺延 | 但本辑已在 gh 路**独立成节**（13 条正文 + 15 行边缘），并落了 3 张卡（MemOS / petdex / awesome-dsh-plugin）→ **成辑留待下轮** |
| ⑥ | `ayagami` 进度复查（每辑一次） | ✅ **闭环** | **连续第二轮无推进**：GitHub releases **0**、tags **空**、最新 commit 仍是 **2026-09-14**（`driver: cargo fmt`）；crates.io 上仍只有占名。详见 §五.4 |
| ⑦ | 决策原则瘦身（224 行，压正文不撤条款） | ✅ **闭环** | `game-production-pipeline.md` **224 → 179 行**（进 200 内），**23 条决策原则一条未删**，归档指针保留；同步改 `AGENTS.md` §七 指针。详见 §五.5 |
| ⑧ | 上轮两条同源疑点收口 | ✅ **闭环（两条都收）** | ① `live2d-auto-pipeline` 双 owner = **纯同名巧合，不是同源**（`mw2wbyys6t-sudo` ★10 / Apache-2.0 / 508 文件 vs `daoming07280` ★0 / MIT / 38 文件，描述、许可证、体量全不同）；② `nnnotes` 双仓 = **`empty-sekai/nnnotes` 是 `MetaSekaiLab/nnnotes` 的 fork**（`fork:true`, parent 已确认）→ 只收本体。详见 §五.6 |
| ⑨ | 人工浏览器取知乎 / B站正文 | ❌ 顺延 | 本轮仍未做（需带持久登录态的真浏览器，无人值守下不可行）。**本辑实得一条替代结论**：中文技术社区里 **掘金可直连取正文**（WebFetch 成功），B站 / 知乎 / 微博均被登录墙拦 → **下轮把「掘金」提为主力 CN 源** |
| ⑩ | 工作区 `MEMORY.md` 回注预算超线（R8 4,782/3,000 token） | ⚠️ **部分** | 本辑已动手压缩（**4,782 → 约 2,9xx token**，做法照房规：压正文、不撤章节），复测见 §十 |

---

## 二、本辑一句话

**上一辑在看「墙两侧长出两丛轮子」，这一辑看到的是「人」——「身体」侧的供给第一次压过「格式」侧，
而官方论坛的一手正文第一次把「模型越做越存不动」的根因说穿了：不是文件大，是参数数在相乘。**

---

## 三、主线一：「身体」侧供给本辑最密集（桌宠 / AI 伴侣）

> 上一辑的范式主张是「**你的桌宠不需要大脑**」。本辑是**这条主张的供给爆发期** —— 一波「给已有 AI 装身体」的项目同时出现。

### 1. `Project-N-E-K-O/N.E.K.O`（★3044 · Apache-2.0 · Python）
**会主动找你玩的 AI 猫娘**：实时陪伴、**主动发起对话**、共享媒体，带「具身情绪引擎」，本地 LLM 驱动。
- 关键分岔：多数桌宠是「你点它才动」，**它反过来先动** —— 把桌宠从「宠物挂件」变成「有自己节奏的室友」。
- 当日仍在推送（2026-10-11），Python 栈 + Apache-2.0，与本地 Ollama 路线同源 → **桌宠侧最完整的参考实现**。

### 2. `jofizcd/Soul-of-Waifu`（★1386 · **GPL-3.0** · Python）
桌面角色扮演 & AI 伴侣，**同时支持 Live2D 与 VRM 头像**、语音、本地 LLM，从聊天演进到 RPG / 桌面陪伴。
- 价值在**功能面最全**；⚠️ **GPL-3.0 传染**，自用无碍、做产品要先想清楚。
- ⚠️ 已 1.5 个月未推送（`pushed_at` 2026-08-28 vs `updated_at` 2026-10-11）。

### 3. `marine841023/duty-on`（★3 · MIT · **Rust + Tauri 2**）—— 本辑「范式最贴题」
**桌宠当你的 AI 编码 agent 状态灯**：监听 Trae / Qoder 等编码 agent 的实时状态，agent 等你输入时用模型动作提醒你。
- 对「同时开好几个 agent 跑长任务」的人是**真实痛点**。
- ⚠️ **反向异常（本轮新形态）**：`updated_at` 2026-08-23 **比** `pushed_at` 2026-10-09 **还旧** —— 连 README 都没顺手更新。**别当依赖，当范式抄。**

### 4. `Lsc-91-69/dsh-live2d-avatar`（★1 · MIT · JavaScript）
DSH 插件：把 Live2D 变成桌宠，**展示 agent 实时状态与「内心想法」**。
- 价值不在代码（刚建 4 天），在**它证明这条接口是通的** —— DSH 插件协议 → Live2D 桌宠，一个 MIT 小插件就够。

### 5. `1704919/WuziDesktopPet`（★2 · MIT · **Godot 4.7 / GDScript**）
Windows 桌宠：随机动画、**离线对话**、桌面互动 + 图片转换与批量重命名。
- Godot 在 Windows 上**原生透明窗**，不用折腾 Electron 的窗口穿透 —— 这是它相对 Web 栈的真正卖点。

### 6. 其余「身体」侧（本辑一并复核，均为新增）
`efficiencyx/JunOS`（★5 · Apache-2.0）自托管 AI 伴侣，**关键词是「关系动力学」** —— 多数伴侣只记事实，它多记一层「你俩关系进展到哪了」；
`Hawkbat/VTubeStudioJS`（★68 · MIT）VTube Studio API 的 JS 实现，**「LLM 状态 → 表情/动作」最省事的通道**；
`o0Nomar0o/Motiv2D`（★45）同时吃 Spine2d 与 Live2D 的查看器（双格式抽象值得学）。

---

## 四、主线二：官方论坛 4 条一手正文（**本辑最硬，全部新增**）

> 入口：`creatorsforum.live2d.com`（上一辑实测 403 → 200 已回滚退役）；本辑 5 个单帖 JSON 全部读取。

### 1. ⭐ **5.3「保存失败（出力に失敗）」的根因 —— 不是文件大，是参数数「相乘」爆炸**（/t/3979，2026-09-22 → 官方 2026-10-09）
用户报「约 **470MB** 的模型，做新表情时保存一直失败」。官方 `enoko_staff` 的根因回复（照抄关键句）：
> `おそらく口周りのオブジェクトについているパラメータが多すぎることが原因である可能性が高い`
> `キーフォームはパラメータ数の掛け合わせで処理が増えていくので…保存できる範囲を超えてしまったものと思われます`
> `ファイルサイズが470MBであることが直接の原因ではありません`
> `問題が顕著な表情パラメータは、通常のキーではなくブレンドシェイプで作成することをおすすめいたします。掛け算ではなく足し算の計算になるので、少ない処理で変形させることができます`

**一句话**：模型越做越存不动时，**第一反应「文件太大，删点素材吧」是错的**；真正会爆炸的是**参数在末端网格上的组合数**。
解法两条：① **blend shape 替代普通 key**（加法≠乘法）；② **key 打在包住整个部件的 deformer 上**，而不是直接打在末端 ArtMesh 上。
⚠️ 官方另给了**应急处方**（本项目具体场景）：「先把上唇上新增的 key 删掉」—— 别把应急当通用解。

### 2. Unity **6.6 + URP3D + SDK for Unity R5**：Scene 能渲染、**运行时不渲染**（官方已复现认领）（/t/3986，2026-09-30 → 官方 2026-10-02）
> 用户：`Unity6.6 にて Universal 3D でプロジェクトを新規作成` + `CubismSdkForUnity-5-r.5.unitypackage`；现象 `シーンには描画されるけど実行すると描画されない`
> 官方 `ono-at-live2d-com`：`サポート環境にて現象の再現を確認いたしました。こちら調査いたします`

**前置坑（帖内给出）**：Unity 6.6 上 `GetInstanceID()` 过时导致编译错误 → 需打 **CubismUnityComponents PR #96** 补丁。
**一句话**：官方只认领调查、**未给修复时间**；**未修前别把 Unity 6.6 + URP3D 上生产**。这也是「为什么 2D 路线（如 Ren'Py）更稳」的旁证。

### 3. 外部联携 API **做不到的 4 件事**（用户向官方点名）（/t/3989，2026-10-05）
> 现在 API **能**：加参数 key、改对象属性与层级。**不能**：① 复制既有对象 ② 复制含 keyform 的对象 ③ 按指定轴左右镜像顶点/形状 ④ 在指定 key 之间复制形状。
> 后果：`この工程を外部ツールから完結できません` —— 「左右眼/左右部件镜像」**目前无法纯靠 API 完成**。

**一句话**：上一辑记了「第三方在 Cubism 的 External API（22033 端口）外围建了一整簇工具」；**这条给出了那条路的能力边界** —— 边界内（加参数、改层级）已能自动化，**边界外（镜像、复制）还得人点**。

### 4. 图集反转复制后显示 `NoArtMesh` —— 官方定性「**规格，不是 bug**」并给恢复法（/t/3975，2026-09-14 → 官方 09-24 / 10-01）
> 官方：`今回の現象は不具合ではなく、Cubism Editorの仕様の範囲で起きている`
> 恢复法：在部件/变形器面板里**右键源图（左眼）→「選択アートメッシュの入力画像として設定」**
> 官方（10-01）：`モデリング画面ではパーツが問題なく表示できているようですので、そのままモデリングを続けていただいて問題ございません`

**一句话**：做「左右镜像部件」时一定会撞上 —— **① 症状不是 bug，别删工程重来；② 恢复只要三步右键**。

### 5. 复核（**官方主干口径逐条未变**，这是「零变动」而非「没干活」）
- Editor 正式线仍 **5.3.04（09/03）**，`updates-history5-3/` **5.3.05 未命中**；Release History 大表**仍无 5.4**（5.4 只在页顶横幅）。
- 产品页 `cubism/update` 仍写 **Ver.5.3.00**，与 docs 表 5.3.04 冲突**未修**。
  ⚠️ **计数分歧照录不归一**：R33 自述「连续第 3 轮」，但按 `v31` 第 146 行「挂了两辑」推，**本轮应为第 4 轮** → 本辑记「**连续第 4 轮复现**，与 R33 自述存在 ±1 分歧」。
- 官网新闻首条仍 **2026.07.17**（且是一条**已过期**的 20% 折扣 Campaign）→ **至少连续 4 轮无新增**。专项搜 `anniversary|周年|20th` → **0 命中**（上辑记的「20 周年」在新闻页未命中）。
- 5.4 alpha2 手册修订记录**未新增**（仍停 09/07）；**可用期仍截至 2026-10-18**（距本辑 7 天）；**76% 遗留文案仍在**。
- ⭐ **alpha2 启动崩溃帖有官方进展**（/t/3983）：官方 10-05 仍在查，并**反问用户「是正常点 exe 启动，还是用 AI agent 等启动的？」** → 官方已把「**AI agent 启动**」列为可疑变量。**对「想用 agent 自动化 Cubism」的人这是官方警告信号。**
- SDK 口径：**`Cubism 5 SDK` = ≤R6；`Cubism 5.4 SDK` = ≥R7 alpha1**（未变）；两条破坏性变更未变；**5.4 SDK alpha2 手册仍 404**（Editor 有 alpha2、SDK 手册停在 alpha1，第 3 轮复现）。
- SDK 分线版本（**别写成一个数**）：Unreal **R1 beta2（09-29）**仍是全家族最新；Unity **R5 与 R4_2 并存**；Web / Native / Java = R5；MotionSync = R2_1。GitHub org `Live2D` 最近推送仍停 **2026-09-29**，**无 R7 tag**。
- 学生优惠**跨区块裂缝仍在**：学生页 **`$46`** vs Store 结算 **`$46.40`**（¥7,344 相同，80% OFF，截止 2027-03-31）→ **第 4 轮连续复现**。
- 竞品：Spine **4.3.26**（4.3.27 仍 Unreleased）；Inochi2D `inochi-creator` 最新仍 **v0.8.6（2024-09-18）**，**13 个月无稳定版**。

### 6. ⭐ 来源可读性翻转一：**Steam 商店本轮从 HTTP 000 变为 200**
上辑把 `store.steampowered.com` 列入「HTTP 000 超时·不再投入」；本轮实测搜索页 **200**、appdetails API **200**。
命中 2026 年三款**以 Live2D 为卖点的商业成品**：
- `Cursor for Live2D`（appid 4956950，2026-09-07，**¥42**）—— 生成式命名，实为**桌面跟随型 Live2D 播放器**；
- `Figryne Cast Studio Engine - Live2D Addon`（appid 5015260，2026-09-03，**¥77**）—— **单摄像头实时面捕**的 VTuber 工作室 Live2D 插件；
- `RPG Developer Bakin Live2D Toolkit`（appid 4753800，2026-06-17，**¥77**）—— 官方 DLC：把 Cubism 做的模型导入 Bakin 游戏。
→ **口径纪律**：「退役源」必须带复测，**不回滚就等于永久误判**（与上辑 `creatorsforum` 403→200 同一形态）。

---

## 五、上轮待办的实测（本辑的「动手」部分）

### 1. ✅ `/skill-doctor` 欠了十二轮的账，本轮结掉
- **判据**：`_tools/skill_budget.py`（21 技能 **0 超预算**）+ 自写 `_tools/_r34_skill_use.py`（在 93 万字记忆 + 项目文档里逐技能做命中统计）。
- **结果**：**14/21 技能全仓零命中**；有痕迹的只有 7 个（`github` 系 55 命中但属常用词误召、`renpy-visual-novel` 5、`round-research-index` 4、`dsh-session-log-repair` / `fullstack-dev` / `github-pages-auto-deploy` / `tencent-meeting-skill` 各 1）。
- **最重要的发现**：本自动化的**专用技能 `round-research-index` 早已存在于技能表**（描述与流程逐条对得上），但此前各轮是「凭记忆跑流程」而**未显式加载技能**。→ **本轮开工即加载**，流程中「零重复 / 先写骨架 / 主 agent 复验」三条正是从它里面读来的。
- **处置**：**不删任何技能**（删除需用户明确要求）；零命中 ≠ 无用（`krea-image` / `nano-banana-pro` / `ima-skills` / `tencent-meeting-skill` 都是面向具体场景的按需工具）。**留下一轮**：给零命中的技能逐个判定「触发条件写窄了」还是「真用不上」，前者改 description。

### 2. ✅ `Agent-desktop-pet` —— **上轮「装不上」的结论被推翻一半**（本辑最有价值的实测）
- **新通道**：`gh api repos/<r>/tarball` **可用**（本机 `git clone` 被代理挡死，这条是绕法）→ 拿到 6.6MB 压缩包。
- **实测**：`agent_state.py`（101KB）**非标准库 import 只有同目录的 `codex_state`**；用**本机 Python 3.13.12 直接跑 `--list` 成功**：
  ```
  codex      found=True  ~/.codex
  claude     found=True  最近更新 14182 分钟前
  dsh        found=True  最近更新 1298 分钟前
  workbuddy  found=True  刚刚更新
  （共 12 个 agent 支持；workbuddy / dsh 都在列）
  ```
- **真正的门槛只在 GUI 侧**：`vendor/` 是**预编译二进制**（`cffi` 的 `_cffi_backend.cp312-win_amd64.pyd` + `pythonnet` + `pywebview`），锁死 **CPython 3.12 ABI** → 「改 vendor」要重编译整条 .NET/Python 链，**不现实**；「装一个隔离的 3.12」才是正解。
- **结论**：**状态读取这半边今天就能用**（可当独立的 agent 活跃度探针接进自己的自动化）；**GUI 另装 3.12，留下一轮**。

### 3. ✅ `wan-h/awesome-digital-human-live2d`（★2425）正面评完
**它不是制作工具，是「数字人 web 应用」的一站式脚手架**（Docker / **<2 核 2G** / 接 Dify·FastGPT·Coze / ASR+LLM+TTS 模块化 / Live2D 模型扩展 / PC+移动 web / 沉浸式对话）。
- **优点**：部署门槛极低（比 airi 的 733MB 轻得多），架构分层清楚，中文文档齐（含 v2.0.0 B站部署教程）。
- **硬伤**：**开源版最后推送 2026-05-18（5 个月）**；功能在往官网 SaaS 收（个人应用管理 / 内置服务接入 / 分享 = 官网独有）→ **开源版是「引流版」**。
- **定位**：`⚠️ 参考` —— 做「AI 伴侣 web 应用」时可当**最低成本起点**；**它不帮你做 Live2D 模型**。

### 4. ✅ `ayagami` 复查 —— **连续第二轮无推进**
GitHub **releases = 0**、**tags 空**、最新 commit 仍 **2026-09-14**（`driver: cargo fmt`）；crates.io 无有效包。★351 未变。
→ 与上辑结论一致；**这条线每辑复查一次**（它是「不买 Editor 也能读 moc3」的唯一现实出口，但至今未兑现为可分发的软件）。

### 5. ✅ 决策原则瘦身：`game-production-pipeline.md` **224 → 179 行**
- **做法**：照房规本辑的改法 —— **压正文、不撤条款**。合并同类工具行、合并「快速查询 / 成本参考」的重复结构、删冗余分隔线；**23 条决策原则逐字保留**。
- **校验**：`wc -l` = 179（≤200）；条款计数 = **23**；归档指针 `game-production-pipeline-archive.md` 仍在。
- **同步**：`AGENTS.md` §七 指针 224 → **179**（先全仓 grep 引用点，只有 `AGENTS.md` 与 `MEMORY.md` 两处活的）。

### 6. ✅ 两条同源疑点收口（**结论相反**，这正是要逐条查的原因）
| 疑点 | 判定 | 依据 |
|---|---|---|
| `live2d-auto-pipeline` 双 owner | **不是同源（同名巧合）** | `mw2wbyys6t-sudo` ★10 · Apache-2.0 · 508 文件 · 创建 2026-05-14 · 推送 2026-10-11；`daoming07280` ★0 · MIT · 38 文件 · 创建 2026-09-16 · 推送 2026-09-18，描述是「See-through 768/30 + psd2live workflow notes (RTX 4060)」→ **项目、许可证、体量、描述全不同** |
| `nnnotes` 双仓 | **是同源（fork）** | `empty-sekai/nnnotes` 的 `fork=true`、`parent=MetaSekaiLab/nnnotes`、★0、创建 2026-09-25 → **只收本体**（index.html 已只收 `MetaSekaiLab/nnnotes`） |
> **教训**：「同名 ⇒ 同源」和「同名 ⇒ 不同源」**都不该预设** —— 本轮两个疑点结论**正好相反**，只能逐条查。

---

## 六、自测与「有用就改」（本辑落地的改动）

### 1. ✅ 新通道落成：`gh api repos/<r>/tarball` 可拿仓库快照
本机 `git clone` 被代理挡死（https 与本地代理两条路都失败）已记在 `AGENTS.md` §二。**本辑补上绕法**：`gh api repos/<owner>/<repo>/tarball > x.tar.gz`（@6.6MB 实测成功），配 `tar -xzf` 即可离线审仓库。
→ **本机事实更新**，已写进 §八 与 `AGENTS.md`。

### 2. ✅ Ollama 调参：**官方口径修正 + 补一条漏收的变量**（本辑唯一「改到自己身上」的）
cn 路给了一篇「Ollama 爆显存三步调参」。我读了，**核实后改了 `ccgs-cn-config/docs/SUFE-REMOTE-RUNBOOK.md`**：
- ⚠️ **口径修正**：原文说「`OLLAMA_FLASH_ATTENTION=1` 提速 20~40%」。查官方 FAQ 后修正 —— **新版 Ollama 在 backend/设备支持时会自动启用 Flash Attention**（上游 2026-07-02 commit 起），`=1` 是「**强制开**」、`=0` 是「**强制关去排查异常**」，**不是「不开就没有」**。旧口诀已过时。
- ➕ **补收一条 cn 路漏掉的**：**`OLLAMA_KV_CACHE_TYPE=q8_0`** —— 官方明确「启用 Flash Attention 后可以对 K/V cache 量化」，`q8_0` ≈ f16 的 **1/2** 内存、精度损失很小（**官方在不使用 f16 时推荐**），`q4_0` ≈ 1/4。**这比单纯砍 `OLLAMA_CONTEXT_LENGTH` 更精细**，且是**全局生效** → 写进 runbook 的环境变量块并标注了「高 GQA 模型（Qwen 系）对量化更敏感」。
- 落地位置：`ccgs-cn-config/docs/SUFE-REMOTE-RUNBOOK.md` §1.2 环境变量块（新增 2 个变量 + 1 段口径说明）。

### 3. ✅ 新技能体检工具（一次性，未进 `_tools/` 常驻）
`_tools/_r34_skill_use.py`（逐技能在记忆语料里做命中统计）。**未升级为常驻闸门** —— 理由：「技能是否被用过」**不等于**「技能有用」，把它做成闸门会诱导出一堆假警（M-0009）。**只作为一次性证据留档。**

### 4. ⚠️ 收集到但**本轮不改**（写清为什么）
- **`motion-mirror` 的本地可行性**：依赖 Wan2.1-VACE，16GB 内存能否跑**未实测** → 改不了，留下一轮。
- **`updated_at` 回填 1338 张旧卡**：要逐卡重取 API（rate limit + 时间），**超上下文** → 留下一轮。
- **`MemOS` 宣称的「省 35.24% token」**：单方宣称，**未独立复现** → 只按「宣称」记录，不落地。

---

## 七、中文侧（本辑可直连取的只剩掘金）

### 1. ✅ **可操作度最高的一条**：喵僕《Live2D 拆分準備與 PSD 圖層整理》
`https://www.nekomaido.com/blog/live2d-psd-preparation` —— **做模型前必须先定的图层规范**，两条硬结论别处少见：
- **图层效果支持边界（Cubism 5.3+）**：**支持** 一般图层 / 图层混合模式 / 剪贴蒙版（**需在 Live2D 内重新剪贴 ID**）；**不支持** 蒙版(Layer Mask) / 图层样式 / 调整图层 / 智慧型物件 / 文字图层 / 向量图层 —— **这些必须在 PS 里先转成一般图层再导入**。
- **命名硬规则**：**避免重名** —— 「導入時 Live2D 並不會報錯，但後續替換圖層時會出現同名替換錯誤」；建议格式 `[左/右_部位_物體1/2/3]`。
- 另两条判断：「**拆了合并简单，合并要拆很难**」「半透明/有纹理/滤镜特效的图层**完结后再补拆非常困难**」→ **画的时候就分好**。

### 2. ✅ 巴哈姆特《Live2D 教學、學習資源整理》（`forum.gamer.com.tw/Co.php?bsn=60608&sn=40198`）
中文圈**结构最完整的一份「指路 + 资源」楼**（GP 209，持续更新）：官方源 / **可回查的建模大佬名单**（其模型展示片常带**工程文件展示**，能直接看各参数单独运作）/ 拆圖專區 / nizima（官方商城，**可网页浏览模型的参数**）。
→ 对本机的意义：**「去哪看别人怎么调参数」比任何单篇教程更适合自学者**；⚠️ 是持续更新的楼，链接会漂移。

### 3. ✅ 掘金《vibecoding · 属于你的小耄》——桌宠**事件→动作绑定模型**
`https://juejin.cn/post/7650052991785287720` —— 技术栈 **Tauri 2 + Vue 3 + PixiJS/Live2D + Rust**（比 Electron 省内存）。
**最值得抄的是「事件 → 动作/表情」的绑定模型**：可绑定事件 = 出现/隐藏/被点击/被拖拽/被摸/投喂/聊天/开始干活/干活中/干活结束/开始散步/停止散步/开心/难过/生气/安心/得意/疲惫；并规定「**一个事件同一时间只能绑定到一个目标**」，绑新目标时旧目标自动排除。

### 4. ⚠️ gamemale（GM 论坛）—— **本轮仍未命中（Cloudflare 人机验证拦截）**
直连返回挑战页（标题「**请稍候…**」/ 正文「需要首先检查您的连接安全性」）。与 `v31/v32` 判定一致。
→ **负结论写法照纪律**：写「本轮未命中」+ 复测条件（站点改用可通行验证，或人工浏览器 + 持久会话）。相邻替代 `forum.gamer.com.tw` 本轮 200 可用（见上）。

### 5. 其余中文源，本轮命中但**全部剔除**（详见 §九）
`wenku.csdn.net/answer|column`（站内 AI 聚合）、`hqwc.cn` / `mhpq.cn` / `cr173.com` / `png5.com` / `game773.com`（SEO 镜像/农场）、`live2d.net.cn`、AI 生成器落地页（`goenhance.ai` / `arcloop.ai` —— 把「Live2D 风格动画」当营销词，与 Cubism 制作无关）。

---

## 八、AI 开发 / 使用侧（读后核实，标注「有用就改」）

> 本辑 AI 开发侧的中文材料质量**意外地高**（都是掘金/个人博客可直连）。三条**互相独立地为同一结论作证**：

### 1. ✅ 《2026 年 AI 辅助开发踩坑复盘与 SOP》（掘金，roc98）+ ✅ 《設計 CLAUDE.md》（vocus）+ ✅ 保哥《Claude Code 20 技巧》
- **三篇独立印证同一件事**：**规则塞太多 → 权重变平 → AI 反而忽略关键指令**。
  - roc98 有**量化**：把团队 **1.2 万字** Java 规约整体注入 → **Token 指数上升 / 上下文丢失 / 「智力降级」**（注意力被驼峰命名、注释格式分散）；破局 = 解耦成**每个微规则包 ≤1000 字**、按需加载。
  - vocus：**「CLAUDE.md 超过 200 行 → 資訊一多，權重就會變得很平」** → 原则改为「只放会影响决策的内容」。
  - 保哥：**`CLAUDE.md` 不是万能的**（「单文件不超过 800 行」这类经常控制不好）。
- **对我们自己的意义**：本工作区的 `AGENTS.md ≤150 行`、房规 `≤200 行`、决策原则 `≤200 行` **三条自定上限，第一次拿到外部独立实证**。→ **不改阈值**（已经很紧），但**记下这条旁证**。
- 保哥另两条可执行习惯：① **「已经修正 Claude 两次以上还是不对 → 上下文已被失败方案污染 → `/clear` 重开」**（与房规「两击规则」同源，但判据更早）；② **「如果 Claude 能看到自己代码的运行结果（报错/测试是否通过），代码质量能提升 2~3 倍」** —— 与决策原则「给 AI 一个能自验的手段」一致。

### 2. ✅ 《我是如何从零构建一个生产级 AI Agent 框架的》（掘金，争筝）——**长期记忆的双轨架构**
- **短期** = 框架内置 `SqliteSaver` 自动 checkpoint；**长期** = 对话结束后由**辅助模型异步提取结构化事实**（「我养了一只猫叫花花」→ `{宠物:猫, 宠物名:花花}`）→ **去重** → 存 SQLite → 下次会话注入 System Prompt。
- **理由写得清楚**：后台异步 = 不阻塞；**用轻量模型** = 信息提取不需要大模型；**去重是必须的，否则 memory 膨胀影响注入效率**。
- **其余**：Coordinator 用 LLM Structured Output 做意图分类 + 生成 **DAG 执行计划**（不靠关键词匹配）；Dispatcher 负责**节点失败重试而非整链崩溃**；工具全面接 MCP，命名空间 `{server}__{tool}`，**框架层「零意见」只透传**；重构后**代码量 -30% 而功能增强**。
- **对我们自己的意义**：这正是我们「**记忆只增不 merge，越滚越贵**」那个待办的**现成解法蓝本**（`consolidation` 待办）。

### 3. ⚠️ 参考级（登记但不落地）
- 《Vibe Coding 的尽头是 AI Agent 军团》（掘金，孟健）：每个 Agent 一份 `MEMORY.md`、`sessions_send` 跨 agent 通信、Cron 定时、浏览器自动化**明确「绝不用 headless，避免被风控」**；起步纪律「**一个 Agent 跑稳了再加第二个**」。⚠️ 营销向复盘，**成本/失败率未给**。
- 《基于 Harness + SDD + 多仓管理》（得物技术）：核心是「**给 AI 一个已有实现当参照，让它照着复刻**」—— 对比「请实现一个 CRUD 接口」vs「**请参照现有『场景欢迎语』功能（后端 `/api/v1/feature/list`，前端 `FeatureTable/index.tsx:53-58`）实现『结束语』**」，数据结构/分层/命名保持一致。⚠️ 企业级 Java 全栈流程，个人场景需大幅裁剪。
- 《用 AI 编程三个月踩坑》（掘金）：三个坑（一把梭大模块 / 上下文塞太满 / 无测试就合）+ 「**把它当杠杆，别当替身**」。⚠️ 阅读量仅 6，价值在印证不在新增。

---

## 九、负结论（**一律写「本轮未命中」，不写「不存在」**）

| 项 | 查法入口 | 本轮命中 | 复测条件 |
|---|---|---|---|
| Editor 5.3.05 | `docs.../updates-history5-3/` + `new-feature-introduction-title/` | **0**（最新仍 5.3.04 / 09-03） | 出现 `5.3.05` 行，或 5.4 进大版本表 |
| 5.4 进 Release History 大表 / 上官网新闻 | 同上 + `live2d.com/en/information/` | **0**（5.4 只出现在页顶横幅；新闻首条仍 07.17） | 5.4 beta 发布时 |
| 官网「20 周年 / anniversary」 | 对 `_p_news.html` grep `anniversary\|周年\|20th\|20 year` | **0** | 新闻页出现周年字样 |
| SDK 主公告线出现 R6/R7 | `docs.../cubism-sdk-manual/top/`（`Updated: 09/29/2026`） | **0**（R6/R7 仅存于 alpha 手册） | 主公告线出现新 `Notification` |
| GitHub org `Live2D` 十月动作 / R7 tag | `api.github.com/orgs/Live2D/repos?sort=pushed` + 5 仓 releases | **0**（推送仍停 2026-09-29） | 出现 10 月推送或 R7 tag |
| 5.4 SDK **alpha2** 手册 | `/sdk-unity-alpha/doc/manual/alpha2/en/index.html` | **404**（alpha1 → 200） | 返回 200 |
| HN 本主题 | `hn.algolia.com/api/v1/search_by_date?query=live2d&tags=story` | **2167 命中 / 真 story 0**（全误召：把 lived / live diff 算进来） | 出现标题含 Live2D 的非误召条目 |
| dev.to 新帖 | `dev.to/api/articles?tag=live2d` | **2 篇**，最新 2026-06-08 | count>2 或最新日期更晚 |
| Reddit | `reddit.com/r/Live2D/` | **HTTP 000**（本机 TLS 重置） | 返回 200 |
| note.com / itch.io | `note.com/search?q=live2d` / `itch.io/search?q=live2d` | **HTTP 000** | 返回 200 |
| Stack Overflow `live2d` 标签 | `stackoverflow.com/questions/tagged/live2d` | **HTTP 403（WAF）**（新探明，标签历史亦可能不存在） | 返回 200 或换 UA 后确认标签 |
| gamemale | `gamemale.com` | **Cloudflare 挑战页**（HTTP 200 但正文是「请稍候…」） | 验证方式变更，或人工浏览器持久会话 |
| **Steam**（口径翻转） | `store.steampowered.com/search/?term=live2d` | ✅ **200**（上轮记 000）→ **退役回滚** | 续监可达性，避免误判为永久退役源 |

---

## 十、索引与文档维护

### 1. `index.html`：**1325 → 1355 项**（`insert_v39_cards.py` 增补 **24 卡**，脚注 **[1325]-[1354]**，分组 309）
- **改前保险丝**：`insert_guard_probe.py --script insert_v39_cards.py --base-block 129a486:index.html` → **P1 正例 + 5 反例全过**（产物 div 平衡、末条脚注 r1354 x1）。
- **改后口径**：`index_metrics.py` → 页头 **1355** / 最大脚注 **1354** / 卡片 **1338** / div **12196 平衡**；**恒等式 1355 == 1354+1 ✅**；E1–E7 全过。
- **⚠️ W1 提示**：卡片数与脚注数差 **16**（历史值 10）—— 因为本辑 **24 卡对应 30 条脚注**（多 6 条是**只作引用、不单独成卡**的信源：cn 喵僕 / 巴哈姆特 / 保哥 / 掘金踩坑 / vocus CLAUDE.md / Steam Bakin）。**这是设计如此，不是漏脚注。**
- `index_metrics.py --update` 已重封快照（309 分组）。
- **新增约定（落地待办③）**：v39 起 `src` 行**固定同时打印 `推送` 与 `更新` 两个日期**，差 >30 天标「⚠️ 差 N 个月」，**反向（updated 更旧）也标** —— 本辑抓到 1 处反向异常（`duty-on`）。

### 2. 文档
- `game-production-pipeline.md` **224 → 179 行**（23 条条款一条未删）。
- `AGENTS.md` §七 指针同步（224 → 179）。
- `ccgs-cn-config/docs/SUFE-REMOTE-RUNBOOK.md`：新增 `OLLAMA_FLASH_ATTENTION`（含口径修正）+ `OLLAMA_KV_CACHE_TYPE=q8_0`。
- 归档：`csdn-social-summary.md`（第三十三辑）→ **`csdn-social-summary-v33.md`**。

### 3. 闸门全跑（改前改后）
| 闸门 | 结果 |
|---|---|
| `index_metrics.py` | ✅ E1–E7 全过，恒等式成立（1355/1354/1338，div 12196），分组 309 |
| `index_metrics.py --update` | ✅ 重封 309 分组快照 |
| `insert_guard_probe.py`（对 v39 本身） | ✅ **P1 + N1–N5 全过**；`--selftest` **7/7** |
| `gate_recall_probe.py` | ✅ 漏检 **0** / 假警 **0** |
| `index_card_loss_probe.py` | ✅ 通过（删一张卡 → E7 报红：「…16 → 15」） |
| `doc_ref_check.py` | ✅ `--selftest` **12/12** |
| `house_rules_enforcement.py --check` | ✅ 6/6（主件 **189 行**，在 200 内） |
| `skill_budget.py` | ✅ 21 技能 **0 超预算** |
| `memory_health.py --selftest` | ✅（R8 变化见 §一.⑩） |

### 4. 子 agent 产出核验（不信汇报，只信文件）
| 路 | 文件 | 条数（`grep -c '^### '`） | 空骨架 `（待填）` | 结论 |
|---|---|---|---|---|
| gh | `_r34/_r34_gh.md` | 34 正文 + 26 边缘 | 0 | ✅ 独立复算 `grep -cE '^### [0-9]+\. '` = **34**，一致 |
| cn | `_r34/_r34_cn.md` | 22 正文（+3 节标题） | 0 | ✅ 独立复算 = **22**，一致 |
| official | `_r34/_r34_official.md` | 25 | 0 | ✅ 含 5 条全新论坛一手 + 12 条负结论 |
| **主 agent 复验** | 20 个候选仓库逐个 `gh api` | — | — | ✅ **与子 agent 汇报零出入**；额外抓到 1 处 `updated_at` 反向异常 |

---

## 十一、下一辑待办（**按顺序做**）

1. **`updated_at` vs `pushed_at` 回填到底**（本辑只落新卡）—— 1338 张旧卡要一次性对齐，且规则已确定为**双向**（真·假活 + 反向异常）。**排在调研之前**（同上一辑把 `/skill-doctor` 排最前）。
2. **`Agent-desktop-pet` 的 GUI 试装**：装隔离的 **CPython 3.12**（不改 vendor —— 预编译二进制锁 ABI），只试 GUI 那半边；同时**把「状态读取」半边接进自己的自动化**（已被证明在 3.13 直接可跑，能识别 workbuddy / dsh）。
3. **`/skill-doctor` 第二轮**：给 **14 个零命中技能**逐个判定「触发条件写窄」还是「真用不上」，前者改 description（**不删技能**）。
4. **DSH 插件生态单独成辑**（连续两轮提到；本辑已独立成节但未成辑）。
5. **`consolidation`（记忆合并与淘汰）**：本轮 cn 路拿到了现成蓝本（**`deepseek-v4-flash` 异步提取结构化事实 → 去重 → SQLite → System Prompt 注入**），可照它给工作区记忆做「只增不 merge」的解法。
6. **人工浏览器取知乎 / B站正文**：用带持久登录态的浏览器（`agent-browser` 技能）；**同时把「掘金」提为 CN 路主力源**（本轮唯一可直连的）。
7. **`wan-h/awesome-digital-human-live2d` 试装**（Docker，<2核2G）—— 若要做「AI 伴侣 web」它是最低成本起点。
8. **`ayagami` 进度复查**（每辑一次）；**`creatorsforum` / **`Steam`** 两条回滚源**继续按轮复测。
9. **Cubism 5.4 alpha 下线（2026-10-18）后的第一手**：alpha 入口消失后，5.4 是否转 beta、SDK 手册是否补 alpha2 → 下辑必查。
10. **超上下文顺延的三条**：`motion-mirror` 本机可行性实测 / `MemOS` 35.24% 宣称复现 / `updated_at` 全量回填（见 §六.4）。

---

## 统计页脚

- 三路候选：**gh 34 条正文（+26 行边缘登记）· cn 22 条 · official 25 条**；原始产出 `_r34/`。
- 本辑落索引：**24 卡**（1301+…：1279 → 1301 → **1325 → 1355**）；脚注 [1325]-[1354]；分组 309。
- 累计经验帖：约 **1490 → 约 1540 条**。
- 房规 `agent-house-rules.md`：**23 条 / 189 行**（未动）；决策原则：**23 条 / 179 行**（本辑压完）；`mistakes/`：**33 条**（本辑未新增；两条同源疑点收口属「查证」不属「新错法」）。
- 新建工具：无常驻（一次性 `_tools/_r34_skill_use.py` 留档）。
- **口径纪律新增一条**：「**同名 ⇒ 同源」与「同名 ⇒ 不同源」都不该预设** —— 本轮两条同源疑点结论**正好相反**，只能逐条查。
- **来源可读性翻转**：Steam **000 → 200**（退役回滚）；`creatorsforum` 保持 200。**退役源必须带复测期**。

---

# 第三十五辑（2026-10-11 · 第三十六次执行）

> 原始产出：`_r35/_r35_gh.md`（子 agent）· `_r35/_r35_gh_main.md`（主 agent 直接检索补位）·
> `_r35/_r35_cn.md` · `_r35/_r35_official.md`
> 去重基线：**从 `index.html` 现取**（`_r35/_dedupe_gh.txt` 1317 个 owner/repo + `_dedupe_urls.txt` 1472 URL），
> 非历史快照（历史快照会把上一轮刚入库的东西当新发现，M-0031）。

## 本辑一句话

**上一辑还在看「墙两侧长出两丛轮子」；这一辑「轮子」自己长成了一条流水线 —— 「立绘 → AI 拆层 → 自动绑定 → moc3」第一次出现四个独立仓库互相引用的完整链路，
而且有人把显存实测贴了出来。同时，桌宠「身体」侧的宿主技术栈整体换代（Electron → Tauri/Rust/原生 OpenGL）。**

## 搜索覆盖

| 路 | 覆盖 | 产出 |
|---|---|---|
| gh | GitHub（`search/repositories` × 8 组关键词，窗口 `pushed:>2026-09-01`，关键链条放宽到 08-01） | **49 条**（子 agent）+ **22 条**（主 agent 直接检索补位），合并去重后见 §二 |
| cn | 掘金（**本轮提为主力源，实测可直连**）/ CSDN / 知乎 / B站专栏 / 网易云社区 / AcFun / 什么值得买 / CSP 官方中文 tips / CGVisual | **24 条**（独立价值约 23 条；E1/E2 同源只算 1 条） |
| official | `live2d.com` 官方站 / `community.live2d.com` 官方论坛 / Steam·note 复测 | **5 条 + 2 条复测**（4 条论坛帖 + 1 条站内路由变化；剔除 4 条内容农场） |

## 一、⭐ 本辑主线：AI「拆层 → 自动绑定」流水线第一次成形

前几辑的主线是「绕开 Cubism 格式线」（自己解 moc3）；**本辑变了** —— 出现了一条端到端可跑的路径：
**单张立绘 → See-Through 拆层 → 分层 PSD → `psd2live` 自动绑定 → moc3 → VTube Studio**。

- **`tsunehimatoi/psd2live`（★614 · Kotlin · NOASSERTION · 推送 2026-10-11）** —— 链条核心件：分层 PSD 自动变可驱动模型。
  ⚠️ 许可证为 NOASSERTION → 商业使用前必须人工读 LICENSE 原文。
- **`shinshin86/still2rig-psd`（★130 · MIT · JavaScript）** —— **绑定侧★最高**；静态图 → 结构化 PSD，闭环「拆层 + QA 自检 + 动作预演」。
- **`sayaka-aiart/StandRig`（★82 · Apache-2.0 · TypeScript）** —— 本辑最「另类」：**把绑定做成 MCP 工具调用**，
  即「agent 直接调绑定」。与上几辑「让 agent 写 Live2D」的尝试不同，这条是**把绑定能力暴露成 agent 的工具**。
- **`flowingduskpro/jpg-to-live2d-workflow`（★4 · MIT · Python）** —— **含 8GB 显存上的实测性能与精度结论**，
  是本辑对「16GB Windows 个人开发者」最直接有用的一条（门槛 8GB 跨得过；MIT；且**作者自己写了哪里做不好**）。
- `lvhaojie456/image-to-live2d`（★2 · MIT）· `daoming07280/live2d-auto-pipeline`（★0 · MIT，RTX 4060 实测）——
  同链条的另两种封装 / 实测记录。
- 拆层侧工具：`0ran/puppet-part-splitter`（★4）· `satoxpochi/PSLayerLRSplitter`（★1 · MIT）·
  `Bellpepperknuthamsun280/ComfyUI-See-through`（ComfyUI 节点，★0）· `bluewakame/live2d-psd-generator`（★1 · MIT）。
- ⚠️ **纪律**：这一链条**全部是「首版/实验」性质**（除 psd2live/still2rig/StandRig 外 ★ 均为个位数）。
  **不能当成品工具推**，价值在「路线已经跑通 + 有人贴了数字」。

## 二、桌宠「身体」侧：宿主技术栈换代

上辑的桌宠多是 Electron/Python；本辑**Tauri / Rust / 原生 OpenGL / 纯浏览器**明显变多：

- `A8Chann/dsh-pet-live2d`（★38 · JS）—— **DSH Web GUI 的 Live2D 桌宠插件**，跟着会话状态换动作表情；
- `ochiru520/Mio`（★49 · Python · MIT）—— Windows 本地优先 AI Agent（对话/记忆/日记/语音/QQ/Live2D/屏幕感知）；
- `waifuai/waifu-companion`（★38 · **MIT-0**）—— 纯浏览器，**本辑遇到最宽松许可**（连署名都不要求）；
- `zeikar/charivo`（★23 · MIT）· `FanyinLiu/Nexus`（★20 · MIT）· `sslbs09/suzuran-pet`（★17）；
- `chengyuZou/EmaAgent`（★3 · MIT · Tauri）—— 亮点是**「叙事 RAG」与普通记忆分开存**；
- `Hisakazu333/NekoPapa`（★0 · Apache-2.0 · Tauri + Rust + C++/OpenGL 原生舞台）；
- `Maboroshinatsu/maibot-deskpet-plugin`（★7 · **GPL-3.0** · Electron + Vue3 + PixiJS + Cubism 4）；
- `mhmdalsaisi/ds-pet`（★0）—— 看鲸鱼对 DSH 会话反应。

**趋势判断**：「**给某个 AI 编码工具配一个 Live2D 身体**」已经成了重复出现的模式 ——
Codex 有（`nyan-mikan/codex-live2d`）、DSH 有（A8Chann / dsh-whale-girl / ds-pet）、MaiBot 有（maibot 插件）。
**这类项目的增量已经够单独成一辑**（见待办④）。

## 三、格式 / 渲染线（本辑增量较小）

- `HELPMEEADICE/Neocari`（★0 · **GPL-3.0** · Rust）—— 纯 Rust 加载 Cubism V2，自带 Haru 六件套；
- `sdegfd/embedded-live2d`（★0 · MIT · C）—— **ESP32-P4 移植**（把 Live2D 塞进单片机，本辑最意外的一条）；
- `haneoka-gakuen/vega-plugin-cubism`（★0 · MPL-2.0）—— 「**插件宿主 + Cubism 插件**」的分层结构，生态里少见；
- `davidleonstr/live2dqt`（★1 · MIT）· `RealNath/wuwa-live2d-viewer`（★5）·
  `4163/pixijs-live2d-spine-viewer`（★2 · MIT）· `rydanee/live2drust`（★0，无 license，❌）· `julfed7/Cubism-2`（★0，无描述，❌）。

## 四、官方侧（official 路）

- **`/discussion/2389`（2026-10-06）** —— 物理完全不动 + **`Maximum Output` 卡在 0 且改不了**（Cubism 5.3）；
  **截至采集无回复**。价值在于把「配了却不动」的症状与一个**可观察量**绑在一起：先查输出参数的 `Maximum Output` 是不是 0。
- **`/discussion/2386`（2026-09-17，官方 09-18 回复）** —— 社区请求 **Live2D Cubism 原生支持 Linux**
  （论据：Cubism 是 **JVM 上的 Java 应用**，改造成本「应该很小」；现在只能 Wine，重模型性能损失大）；
  官方回复是套话「**已共享给开发团队**」，**无版本承诺** → **短期不要指望原生 Linux 版**。
- `/discussion/2381`（图层准备工作流，2026-08-25）· `/discussion/2374`（**官方账号**发的 SDK 5 R5 + URP
  `TransparentPicking` 材质残留，2026-07-06）—— 两条**仅到标题/作者/日期级核实**，正文待取。
- ⚠️ **论坛路由变了**：本辑抓到的是 `/discussion/<4 位>`，前几辑记录的是 `/t/<4 位>`，**两套编号不互通**。

## 五、⚠️ 方法学：本轮最重要的三个「教训型」发现

### 5.1 `gh api repos/<x>` 返回 404 ≠ 仓库不存在（**新增，影响所有后续回填**）
本机实测 `kitao/pyxel`（★1.4 万级、当天仍在提交）经 `gh api` 与 `curl api.github.com` **全部 404**，
而 WebSearch 证明它活跃存在（v2.9.9，2026-08-12 提交）。同批「查不到」的 38 个里包含
`block/goose` / `fabricmc/fabric` / `hiyouga/LLaMA-Factory` / `pytorch/torchtune` 等**一线项目**。
→ 判定为**本机网络层（本地代理）对未缓存路径返回 404**，**不是仓库消失**。
**纪律**：遇到 404 **不许写「已死链/不存在」**，要写「**本轮 API 未命中，原因未定**」，并换第二通道交叉验证（M-0033 家族）。

### 5.2 **22 个仓库改了 owner/name（链接腐化清单）** —— 靠 GraphQL 返回的 canonical 名抓到
| 索引里的旧路径 | 现在的路径 |
|---|---|
| `block/goose` | `aaif-goose/goose` |
| `Bin-Huang/chatbox` | `chatboxai/chatbox` |
| `hiyouga/LLaMA-Factory` | `hiyouga/llamafactory` |
| `pytorch/torchtune` | `meta-pytorch/torchtune` |
| `oobabooga/text-generation-webui` | `oobabooga/textgen` |
| `KwaiVGI/LivePortrait` | `klingairesearch/liveportrait` |
| `FunAudioLLM/CosyVoice` | `qwenaudio/cosyvoice` |
| `ltdrdata/ComfyUI-Manager` | `comfy-org/comfyui-manager` |
| `intel-analytics/ipex-llm` | `intel/ipex-llm` |
| `qodo-ai/pr-agent` | `the-pr-agent/pr-agent` |
| `sjtu-ipads/powerinfer` | `tiiny-ai/powerinfer` |
| `itzcrazykns/perplexica` | `itzcrazykns/vane` |
| `streetpea/chiaki-ng` | `chiaki-ng/chiaki-ng` |
| `RaiMan/SikuliX1` | `oculix-org/sikulix1` |
| `haosulab/maniskill` | `mani-skill/maniskill` |
| `kolbytn/mindcraft` | `mindcraft-bots/mindcraft` |
| `genesis-embodied-ai/genesis` | `genesis-embodied-ai/genesis-world` |
| `laude-institute/terminal-bench` | `harbor-framework/terminal-bench-1` |
| `riffusion/riffusion` | `riffusion/riffusion-hobby` |
| `RamiLego4Game/LIKO-12` | `liko-12/liko-12` |
| `Dryxio/auto-re-agent` | `dryxio/reagent` |
| `JakeSelby/agent-harness` | `jakeselby/model-citizen` |

**判读**：星数不是「项目还行」的信号；**owner/name 会变**。**卡片的 href 虽然重定向，但卡片上显示的仓库名已经过时** → 下轮待办。

### 5.3 内容农场站群在 Live2D 题材上成规模（**识别特征已成型**）
本轮搜索命中的「文章」里，`hqwc.cn` / `bryh.cn` / `tzjp.cn` / `mtrt.cn` 是同一批：
开头「作为从业五年的技术美术」+ **百分比数字密集但全部无法核实**（「参数调节范围扩大约 40%」「效率提升 25%」）
+ URL 形状固定（`/a/<7 位>.html`、`/news/<5 位>`）+ 无信源无截图。
⚠️ **这些数字是编的** —— 例如写出「`Ctrl+D` 直接复制图层」，而 Cubism 里 `Ctrl+D` 不是这个功能。**收录即传播错误。**

## 六、退役源复测（每条带复测期）

| 源 | 本轮 | 处置 |
|---|---|---|
| `store.steampowered.com` | **200** | 延续上辑回滚，维持可读 |
| `community.live2d.com` | **200** | 可读（但**分类页正文 JS 渲染**，要改用 `/categories` 页取） |
| `note.com` | **000** | 维持退役（本轮未命中） |
| B 站 | 视频页需登录**仍不可取正文**；**「专栏 `read/cv…`」页可直读** | **口径微调：只有视频详情页退役，专栏不算退役** |
| 掘金 `juejin.cn` | **实测可直连取正文**（A1–A3 均成功） | **本辑起确认为 CN 路主力源** |

## 七、自测（「有用就改」）

1. **待办① 已落地**：`pushed_at/updated_at` **回填 1212 处 src-line**（见 §八）；顺带得到
   **190 个「疑似僵尸」**（pushed 比 updated 早 1 年以上）、**28 处反向异常**（updated 比 pushed 还旧）。
   → 这条规则确认为**双向**（上辑结论复现）。
2. **`gh api` 404 假阴性**（§5.1）→ **已写入下轮纪律**；本轮**没有**把这 38 个仓库写成死链（守住 M-0033）。
3. **CN 路主力源切换成功**（掘金可直连）→ 下轮沿用；**B 站专栏页**同步解禁。
4. **内容农场判据成型**（§5.3）→ 下轮可直接过滤，省一轮检索。
5. 未落地（超上下文）→ 全部写进待办，不含糊带过。

## 八、索引与文档维护

- **`index.html` 旧卡回填**：`_tools/_r35_backfill.py` 一次改写 **1212 处** src-line，格式统一为
  `最近更新 <updatedAt>（推送 <pushedAt>）· …`；**38 条因 API 未命中而跳过**（不编数据）；
  45 条特殊格式（`创建 … · 最近推送 …`）留待办。备份 `_r35/index.html.pre-backfill.bak`。
- **第四十版增补**：`insert_v40_cards.py` 增补 **24 卡 + 24 条脚注（[1355]-[1378]）**；
  页头 **1355 → 1379 项**；卡片 **1338 → 1362**；分组 **309 → 310**；div **12606 / 12606**。
- **闸门（改前改后各跑一次）**：`insert_guard_probe` **6/6**（P0 语法 + P1 正例 + N1–N5 反例）·
  `index_metrics` E1–E7 全绿 + 恒等式 + `--update` 重封 310 组 ·
  `gate_recall_probe` 漏检 0 假警 0 · `index_card_loss_probe` ✅ · `doc_ref_check` 全部通过（C1/C2/C3/C4）·
  `house_rules_enforcement --check` 6/6（主件 189 行）· `skill_budget` 21 技能 0 超预算 · `memory_health` 跑通。

### ⚠️ 8.1 本轮闸门拦下一次「重复收录」—— 并暴露去重流程的一个盲区

**过程**：v40 初稿里我放了 4 个仓库：`tsunehimatoi/psd2live`、`flowingduskpro/jpg-to-live2d-workflow`、
`lvhaojie456/image-to-live2d`、`A8Chann/dsh-pet-live2d`。
`insert_guard_probe` 的**重复仓库检测（N5）直接把它们拦下**——4 个全部已在 `index.html` 里出现过。

**逐个查证结果**：
| 仓库 | 在 index.html 里的实际状态 |
|---|---|
| `tsunehimatoi/psd2live` | **已是独立卡片**（`rpm31c1`，第 31 版收的）。⚠️ 更严重的是：**我当时写的「许可证 NOASSERTION」与索引里记的「GPL-3.0」相反** —— 旧卡是读过 LICENSE 原文的 |
| `flowingduskpro/jpg-to-live2d-workflow` | 已作为**正文里的纯文本提及**（v38 卡 `rpm34c15`：「同类还有 … 都是同一条链的变体，别重复造」） |
| `lvhaojie456/image-to-live2d` | 同上，被同一句提及 |
| `A8Chann/dsh-pet-live2d` | 已在 v38 卡里写明「仓库还有 … 与 `A8Chann/dsh-pet-live2d`（★38）两个同题插件，**别装重**」 |

**→ 处置**：4 张卡全部撤下，换成 4 条真正的新条目
（`bluewakame/live2d-psd-generator` × `0ran/puppet-part-splitter` × `4163/pixijs-live2d-spine-viewer` × `hoardodile/plugin-2d-skel`）。

**暴露的盲区（本轮最该记住的一条）**：
> **我的去重基线 `_r35/_dedupe_gh.txt` 是用 `grep -oE 'github\.com/[owner]/[repo]'` 从 `index.html` 现取的 ——
> 它只能抓到「以 URL 形式出现的仓库」，抓不到「卡片正文里以 `owner/repo` 纯文本形式提及的仓库」。**
> 而我们的卡片**习惯在「注意」栏里写「同类还有 `x/y`」** —— 这些仓库**看起来是新的，实际已经被判过价值**。

**修法（下轮起）**：生成去重基线时**追加一条全文反引号抓取**：
```bash
grep -oE '`[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+`' index.html | tr -d '`' | tr 'A-Z' 'a-z' | sort -u >> _dedupe_gh.txt
```
并注意：**探针的判据（`slug in src.lower()`）比我的基线更严**——它连「正文提及」也算重复。
**这次不是探针过度保守，是探针比我严、且它是对的。**

### ⚠️ 8.2 同一个脚本连撞两次 P0/P1 —— 探针的另一次价值实证

- 第一次：中文串里混了 ASCII 双引号 → `SyntaxError: unterminated string literal`（P0 拦下）；
- 第二次：修语法时**多加了一个逗号**，把 `desc = ('a' 'b' …)` 变成了 tuple → `TypeError: can only concatenate str (not "tuple") to str`（P1 拦下）。
- **教训**：`desc = ('多行' '字符串' '隐式拼接')` 这种写法，**一个多余的逗号就静默改变类型**。
  两次都由探针在**未落盘**的状态下拦下 —— 若直接跑真脚本，会写坏 2.5MB 的 `index.html`。

## 九、下一辑待办（按序）

1. **把 22 个改名仓库的 href 与显示名更新**（§5.2 清单已备好）—— 卡片链接虽重定向，但**显示名已过期**。
2. **`updated_at` 回填的收尾**：38 条 API 未命中的需换通道补（提示：用 `search/repositories` 或镜像页）。
3. **AI 拆层→绑定链条的实操验证**：`psd2live` 系（★614）/ `still2rig-psd`（★130 MIT）—— 至少把
   **许可证与运行前置**读清楚，判断本机（16GB Windows）能不能真跑一次。
4. **DSH 插件生态单独成辑**（连续三轮提到，本辑已集齐 4 个实现）。
5. **`/skill-doctor` 第二轮**：11 个零命中技能（本辑实测口径）逐条判定「触发写窄 / 真用不上」，
   **本轮发现的新根因：技能之间职责重叠也会导致零命中**（`github-research-report-pages` 与
   `round-research-index` 争同一个场景 → 干脆凭记忆跑）。
6. **`Agent-desktop-pet` GUI 试装**（隔离 CPython 3.12；状态读取半边已被证明 3.13 直接可跑）。
7. **`awesome-digital-human-live2d` 试装** / `ayagami` 复查 / `creatorsforum`·`Steam` 按轮复测。
8. **Cubism 5.4 alpha 下线（2026-10-18）后的第一手**；⚠️ 本辑 **cn 路给出的是「可用期至 2026-09-14」**，
   与上辑记录的 **10-18** **冲突** → **照录不归一，下轮必须定一个**。
9. **`consolidation`（记忆合并与淘汰）** —— 蓝本已备（cn 路）。
10. 超上下文顺延：`motion-mirror` 本机可行性 / `MemOS` 35.24% 复现 / Cubism 官方 Release History 的**正确 URL**
    （本辑实测 `docs.live2d.com/en/cubism-editor-manual/release-history/` **404**，路径形状错了）。

## 统计页脚

- 三路候选：**gh 49（子 agent）+ 22（主 agent 补位）· cn 24 · official 5**；原始产出 `_r35/`。
- 本辑落索引：**24 卡**（1325 → 1355 是上辑；本辑 1355 → **1379**）；脚注 [1355]-[1378]。
- **旧卡回填**：**1212 处** src-line（另 38 条 API 未命中跳过、45 条特殊格式留待办）。
- 累计经验帖：约 **1540 → 约 1585 条**。
- `mistakes/`：**33 条**（本辑未新增；§5.1 先并入房规纪律，下轮视情况立条）。
- 新建工具：`_tools/_r35_extract_repos.py` · `_r35_fetch_pushed.py` · `_r35_backfill.py`（**均为一次性，留档**）。
- **口径纪律新增**：「**API 的失败返回不是事实**」—— 404/超时/空结果都只说明「**这条通道没拿到**」，
  不说明「东西不存在」；**换通道**是义务，不是加分项。

---

# 第三十六辑（专项）：Furry / Kemono 领域的 Live2D 技巧

> 触发：用户提问「我听说很多的 live2d 技巧都是 furry 领域大神开发出来的，可以找一找相关内容吗」
> 原始产出：`_r36/_r36_furry.md`（完整版）。数据抓取：2026-10-11。

## 零、去重结论（**该领域此前完全未覆盖**）

对 `index.html` + 本文件 + 最近两版存档 + `_r35/_dedupe_gh.txt` 做 `grep -i`：
`furry` / `kemono` / `muzzle` / `兽人` / `兽耳` / `ケモノ` / `ケモミミ` / `しっぽ` / `尻尾` —— **全部 0 命中**。
（`anthro` 5 处命中经查全是 `anthropics` 误报；`vtuber` 18 处属通用内容。）
→ **本轮 30+ 条候选全部为可新增**，无需剔除。

## 一、一句话结论

「furry 大神开发了 Live2D 技巧」**要打折**：圈里**没发明 Cubism 底层机制**（变形器/物理摆锤/四角合成
全是官方功能），但它**率先把「非人类面部结构」逼成了一整套专用做法**，其中一部分**能反哺人类模型** ——
最硬的一条是**背层法（Back-Layer Method）**，作者亲口说「**对其他模型也有用**」。

## 二、本辑最重的三个发现

1. ⭐ **Mimisuke（Mimi-Seam）「Kemono Live2D 从零」** —— `note.com/mikischine`，
   至少 **11 篇**（Illustration P1/P4 + Modeling P7/P8/P11 + Muzzle 专篇）。提出**背层法**。
   ⚠️ `note.com` 本机 **000**（直连+代理，与上辑一致），但**检索正文快照完整可读** → 按 M-0033 记「本机未命中」。
2. ⭐ **VTResources（`vtresources.carrd.co`）** —— 人工策展的 VTuber 资源总表，**本辑最高价值单点**。
   内含 **Mika《Snout Layering Guide》（furry 吻部分层，最直接的专属教程）**、
   **nonon.（ののん）Tips 合集**（与 `letsplayindex` 那条「基于 ののん 示例」**互相印证**）、
   Himono / Karrot / Kira Omori / Novaj（嘴部绑定）/ Inochi2D 官方示例 等。
   ⚠️ carrd 本机 **000** → 需人工浏览器取一次建离线副本。
3. ⭐ **palkaloid.com（200，日文）** —— 兽人角色 **Fennec-kun** 用**免费版** Cubism 的
   两条连载（「獸人的畫法」4 篇 + 「無料版 Live2D」19 篇，含 muzzle / 双耳物理 / 四角合成），
   且**免费公开兽人立绘数据**。

## 三、中文侧（可直连）

- **虎课网 huke88**（200）：`/baike/a55193` 动物耳朵和尾巴（尾巴放最底、耳朵放头发层后、
  角度X/Y 跟随、四角形状合成、**耳抖范围 -1/1 并把「眨眼」勾上去**）；
  `/baike/list/p170` DuangDuang 兽耳（**左耳绑左眼开闭、右耳绑右眼开闭**；耳 X≈耳后露出面积、耳 Y≈耳尖上下）。
- **moonku44**（200）：⭐ 唯一给出**兽耳六件套**——「**左外耳、右外耳、左内耳、右内耳、左毛毛、右毛毛**」。
- **NGA `tid=24067275`**（**403**，内容经快照取到）：「**尾巴要画成竖直整体**再绑」；
  作者自述「**为了把一根猫尾巴掰直，直接拆成十几段**」——这条规矩的代价说明；
  另提醒「**Cubism 里模拟的物理与 FaceRig 实际效果不一致**」。

## 四、furry 贡献的三层拆解（本辑的核心判断）

- **层 1 没有发明底层机制**：变形器 / 物理摆锤 / 四角合成 / 剪贴蒙版 / Glue / Skinning 全是官方功能。
- **层 2 为「非人类结构」逼出专用做法**：背层法+黑白双吻层 / 嘴拆十几片 / 尾放最底耳放发后 /
  耳绑同侧眼开闭 / 耳六件套 / 尾巴竖直+Skinning / 耳朵与头毛**必须分开建物理组**。
- **层 3 确实反哺通用模型**：**背层法**（任何交叉重叠部件）；「**把 X 绑在 Y 的前提条件上**」
  （furry 做耳抖、人类做微笑，**同一机制**）；**耳朵借道眼睛开闭** 与「呼吸驱动尾巴/翅膀」同源；
  **Skinning / Glue** 正好是尾部/裙摆衔接的最优解。

> 一句话：furry 圈不是发明家，是「**最难的那批客户**」——它把人类模型的偷懒做法全堵死了。

## 五、可达性实测（2026-10-11）

**200**：palkaloid · huke88 · moonku44 · myfurryrefsheet · online-courses.club · aboutcg · github/nanshaws · catvtuber
**000**：note.com（直连+代理）· vtresources.carrd.co · courtneystockmanart.wixsite.com
**403**：ko-fi.com · bbs.nga.cn

## 六、下一辑待办（本专题）

1. **背层法实操**：用 Mimisuke 免费公开的 `こいぬ.psd` 或 palkaloid 的免费兽人数据走一遍。
   ⚠️ Mimisuke 的 PSD **明确禁止「用于 AI 训练」**，但允许学习/改造/发截图/进作品集。
2. **下载 ko-fi 的 Furry Snout `.cmo3`**（需绕 403 或人工下）→ 拆两种吻部风格的结构差异。
3. **vtresources 建离线副本**（需人工浏览器）。
4. **「Glue / Skinning」写进 `game-production-pipeline.md`** —— 属「有用就改」，且是**通用**省时技巧。
5. 核实 `letsplayindex` 与 `tubesum` 是否同源（正文风格高度相似）。
6. B 站/知乎/小红书「兽人 Live2D」UP 主教程（需人工浏览器，本机不通）。

## 统计（本专题）

- 检索：**6 次 WebSearch + 1 次 WebFetch + 2 批 curl 可达性**；有效候选 **30+**，去重后**全部新增**。
- 索引：**本辑未落卡**（纯调研专项，用户未要求并入 `index.html`）；`furry` 域在索引中仍为 **0**。
- 落盘：`_r36/_r36_furry.md`。
