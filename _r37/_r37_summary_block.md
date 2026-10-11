
---

# 第三十七辑（2026-10-11 · 第三十七次执行）

> 三路：**gh 32 条**（子 agent）+ **cn 24 条** + **official 8 条新增 / 17 条口径复核**；原始产出 `_r37/`。
> 落索引 **24 卡**（1379 → **1403** 项，卡片 1362 → 1386，脚注 [1379]–[1402]）。
> 去重基线**从 `index.html` 现取**：1337 个 `owner/repo` + **62 条「卡内正文反引号提及型」**（新增补的盲区修复）+ 1379 条 URL；
> **子 agent 报的 32 个候选仓库由主 agent 逐条 `gh api` 复验，零出入、零 404。**

## 本辑一句话

**上一辑在讲「给 AI 装一个身体」，这一辑它从主张变成了重复模式；与此同时，官方论坛一轮里认领了三处塌方。**

---

## 搜索覆盖

| 路 | 覆盖源 | 结果 |
|---|---|---|
| gh | GitHub REST / GraphQL、PyPI、crates.io、网页直取 | 正文 32 条 + 边缘登记 4 行 |
| cn | 掘金（主力）· CSDN · B站专栏 · NGA · 博客园 · AcFun · 搜狐 · 米画师 / B站工房 · 中国台湾一手博客 | 正文 24 条 |
| official | live2d.com 三站 · creatorsforum（Discourse）· community.live2d.com（Vanilla API）· Spine · Inochi2D · HN / dev.to / Reddit / Medium | **新增一手 8 条** + 主干口径 17 条逐条复核 |

---

## 一、本辑主线：AI 的「身体」从主张变成重复模式

上一辑的范式主张是「**你的桌宠不需要大脑**」。本辑出现的是**四个独立实现**，而且分成了两种姿态：

**姿态 A · 单向（状态 → 表情）**
- `Rosa134/daidai-live2d-pet`（★12 · MIT · Electron）—— **监听 Codex / Claude Code 会话状态**，角色头顶弹中文气泡，按「思考 / 运行工具 / 回复 / 完成」四态切动作。另带陪伴模式（OpenAI 兼容接口 + 火山引擎 TTS + RMS 口型）。本辑 gh 路唯一标「**落地**」的桌宠。
- `hacxy/dsh-live2d`（★0 · MIT）—— DSH 插件版，**走公开挂载点**（`window.ModuleLoader + ctx.slots + webServer SSE`），第三方沙箱评级 **L5 运行时通过**。价值是**协议样本**，不是代码。⚠️ 母本 `lrplrplrp/live2d` 最后推送 **2025-03-29**，比下游还旧。

**姿态 B · 双向（既是脸也是界面）**
- `kongweiguang/xiaoya`（★1 · MIT）—— 实时语音对话 + **自然打断** + Live2D 神态/口型 + **MCP 工具扩展**，口号「让 AI 从回答问题走向完成任务」。Live2D 不再只是状态灯，而是交互界面本身。

**同日还有两处旁证**：`fswolf/luna-local-agent`（★4，把「逐 token 置信度可视化」和 Live2D 形象并置）、`zhuang-HE/live2d-ai-pet`（★1，Ollama + 6 情绪状态机最小闭环，❌ 无 LICENSE 未收卡）。

---

## 二、桌宠宿主：Tauri / Rust 已成主流，且出现「低配退路」

| 项目 | ★ | 许可 | 一句话 |
|---|---|---|---|
| `liwenka1/bongo-cat-next` | 151 | MIT | **Tauri 2 + Next.js 15**，BongoCat 系最有维护的一支；hooks 拆成 `_useCore/_useModelLoader/_useMotionPlayer/_useMouseEvents` |
| `isHarryh/Ark-Pets` | **1124** | GPL-3.0 | 本辑唯一千星通用桌宠框架；**平面重力场物理**（干员能被丢出去、会站窗口边缘），**实测运行内存约 50–80MB** |
| `NekoHome-Studio/mea-pet-public` | 44 | MIT | **Live2D 与 PNG 差分双渲染引擎可热切**；180+ 立绘 / 18 表情 / 5 服装 |
| `NewComer00/Chobits` | 3 | MIT | 把 moc3 渲染**搬进终端复用器 Zellij 的窗格** —— 非 GUI 宿主这条路径独一份 |
| `CatStack-pixe/MochiPaw` | 49 | **混许可** | BongoCat 衍生（MIT）+ PolyForm Noncommercial + 第三方素材 → **商用需书面许可** |
| `TamKungZ/VLiva` | 10 | NOASSERTION | Linux 原生 VTuber 宿主（对标「Linux 上没有 VTube Studio」） |
| `SymphonyIceAttack/mac-avatar-layer` | 4 | **无 LICENSE** | macOS 原生层托 Live2D 的 Rust 原型 |

> **「宿主换代」这条线的落点**：Electron 明显减少，Tauri / Rust / 原生层变多；同时**「低成本退路」第一次被当成一等设计**（`mea-pet` 的 PNG 差分、`Ark-Pets` 的 50–80MB）。

---

## 三、格式线：终于有了「不做渲染」的纯 Python 读写器

- ⭐ `Ludentes/py-moc3`（★4 · MIT · **零依赖**）—— `.moc3` **能读能写**，PyPI 直装（`pip install py-moc3`，周下载约 131–145）。
  格式拆解写得很干净：**64B 头 + 640B 段偏移表（160 × uint32）+ 从第 1984 字节起约 100 个 64B 对齐的 typed array**；
  支持 **V3.00 / V3.03 / V4.00 / V4.02 / V5.00**，read→write **字节级 round-trip**（自带 `moc3 verify`）。
  → **本辑对「维护索引站的个人」最有用的一条**：批量扫模型、读参数范围、改 texture index 全部命令行化、零图形栈。
- `alksdesu/live2d-tools`（★4 · **无 LICENSE** · C++）—— **逆向**方向：每个 drawable 单渲一层导出 PSD（保留 Part 分组与命名），
  或从 moc3 恢复几何/变形器/参数/物理生成可编辑 `.cmo3`。救「工程丢了只剩运行时文件」的场景。
  ⚠️ 别名 `live2d2psd` 经 `gh api` 返回 **404（本机代理假阴性）**。
- `Lendic42/LumaStage`（★1 · GPL-3.0-only）—— **不是拿来跑的，是拿来抄的**：`compatibility.md` 是一张 VTS 兼容性验收矩阵
  （Cubism 3/4/5 模型发现、parameter mapping、表情/场景热键、插件 API 各自 Full / 兼容子集 / 尽力而为 / 计划中），
  并明确声明「不复制 VTS 代码、不解密受保护模型、不绕过作者限制」。
- `Eatgrapes/Live2D-JavaBinding`（★16 · MIT）—— Cubism Native 的 **JNI Java 绑定**，含 `makeGL()` / `makeVulkan(...)` **双后端**。
- 谱系补全：`DenchiSoft/VTubeStudio`（★1313）—— **不是 VTS 本体，是整个生态的 API 事实标准**（模型/表情/动作/物理覆盖/参数注入/事件订阅）。
- `Inochi2D/inochi-session`（★407 · BSD-2）—— 全开源替代路线的**播放端**。⚠️ **已停推约 11 个月**；
  但**核心库 `Inochi2D/inochi2d` 仍在推（2026-10-03，★1811）** → **创作端停、底层动**的分裂状态。

---

## 四、官方一手（本辑最硬，全部新增）

### O1 · 官方认领 bug：Unity 里模型压不过 Sprite（`/t/3991`）
用户把 `Order in Group` 与 `Order in Layer` 拉成 500 / -500、又拉 Z 坐标，**Scene 与 Game 视图里 Sprite 照样盖住模型**。
官方 2026-10-07：`Cubism 5 SDK for Unity R5 以降`要在网格之间夹对象需用 **「描画割り込み機能（Z-Interlocking）」**，且
**`ただし、描画割り込み機能は現在不具合がございます。こちらは次回のリリースで修正いたします`**。
→ **现阶段别把「模型与背景 Sprite 之间的图层穿插」当可交付项。**

### O2 · 官方认领 bug：同名 `motion3.json` 覆盖重导入崩（`/t/3978`）
Unity R4 / Win11 / Unity 2022.3.62f2，**参数/曲线数变多**的新 motion3 覆盖旧文件后抛
`System.IndexOutOfRangeException … CubismFadeMotionData.CreateInstance(...)`；官方 2026-09-30 定性
`こちらは Cubism SDK の不具合になります`。
→ **规避：覆盖前先删旧的 `.fade.asset`，或新建工程导入。**

### O3 · 官方否认 Unreal SDK 停摆，20 天后 beta2 闭环（`/t/3973`）
官方 2026-09-09：**`開発・サポートを停止する予定はございません。現在、次期アップデートのリリースに向けて開発を進めております`**
→ 次期更新 = **2026-09-29 的 `5-r.1-beta.2`**。**「停更 ≠ 停摆」** 得一例。

### O4 · 跨辑口径冲突**正式收口**：5.4 alpha 可用期 = **2026-10-18**（`/t/3976` + 官网公告页）
- 官网两处原话：`Available until "October 18, 2026." After this date, the alpha version will no longer be available.` → **整条 alpha 线 = 10-18**。
- 同页另一句：`Please note that alpha1 will no longer be available after September 14, 2026.` → **09-14 只是 `alpha1` 的下线日**。
- 官方 2026-09-17 复证：`alpha1 は「2026年9月14日」まで利用可能で…`
- **cn 路此前记的「可用期至 2026-09-14」= 把单个版本的下线日当成整条线的可用期** → 本辑采信 **10-18**。
- 附带同样重要：**alpha 版无「前方兼容」**（`前方互換には対応しておらず`）—— alpha2 存的工程 **5.3 打不开也编辑不了**，用 alpha 前必须先备份。

### O5–O8（登记）
`/t/3974`：5.3.02 里「模型数据消失」实为**只存了 `.can3`（动画）、没存 `.cmo3`（模型）** —— 两份文件；
`/t/1189`：**跑了 4 年的功能请求落地** —— blend shape 现可「删 deformer 并让子元素继承参数」；
`/t/3985`：**同一参数的往返无法分段自动化**（规格缺口），做循环特效要预留手工补 key 的工作量；
`community disc/2385`：**复杂 Warp Deformer 有性能放大**，用户实测根目录里放任何东西都能拖慢到 5 秒以上 → 官方 2026-10-01 转开发组。

### 官方主干口径逐条复核（**17 条全部未变**）
Editor **5.3.04**（09-03，无 5.3.05）· 5.4 **alpha2**（alpha1 07-14 / alpha2 09-07，无 alpha3）· SDK 术语 **R6 → R7 alpha1** ·
Unreal **R1 beta2**（09-29）· GitHub org 最近推送仍 **2026-09-29**、**仍无 R7 tag** · 产品页 `Ver.5.3.00` vs docs `5.3.04` **冲突持续（第 5 轮）** ·
学生页 `$46` vs Store `$46.40`（¥7,344 同）· 76% 遗留文案仍在 · 官网新闻首条仍 **2026-07-17** · Spine **4.3.26** · Inochi2D creator 停 `v0.8.6`。
**✅ 顺带解决上辑待办**：Release History 正确入口找到了 —— `/en/cubism-editor-manual/release-history/` **404 复现**，
正确路径 = **`updates-history/`（Hub）+ `new-feature-introduction-title/`（大版本表）+ `updates-history5-3/`（patch 明细）**。

---

## 五、中文侧：本辑最硬的不是教程，是「纠纷金额」

- ⭐ **搜狐 2026-09-28**：北京海淀法院 2026 年判 —— **7627 元**定制虚拟主播模型，原告以精度不达标要求退稿退款；
  法院依《民法典》787 条认定有任意解除权，但查明画师**已完成约八成工作量** → **判付报酬 4000 元、平台退 3627 元**（「不满意 ≠ 全额退款」）。
  米画师案例：**669 元**细化虚拟服装，画师拿不出草稿/过程文件 → **仲裁认定原创性不足，封号 + 全额退回**。
  **举证能力决定胜负**（另一案原告因未存提示词/参数/修改过程而败诉）。
- **7 个价格锚交叉验证**（米画师 4 + B站工房 3）→ 推出一个很少被公开的数字：
  **「工程文件约值 2500–2900 元」**（¥3666 / ¥3700 的橱窗**不给工程**；¥800–1100 的企划**必须给 `.cmo3`**）。
  「不对称」加成**跨平台口径不一**：米画师 **×1.2** vs B站工房 **×1.5**。
  「嘴型基础 44」是唯一量化口型条数的样本；「交稿后小改 30 / 大改 50–100」是唯一量化**售后成本**的橱窗。
- **NGA《从零开始的 Live2D 使用手册》** —— 中文侧最长手写总纲：纹理图集 2048²（上限 16834²）· 导出选 **SDK 3.3** ·
  **免版图层 ≤30** · **影响度每类总上限 100%** · 易晃度 0.7–0.99。**这些区间可当自动绑定的合法性断言用。**
- **博客园看板娘三条静默失败**：`fastly.jsdelivr.net` 被墙（页面不报错）· `live2d_path` 末尾 `/` 必须加 · `waifu-tips.json` 的 `paths` 格式。
- **掘金 `easy-live2d v0.4.0`** —— 「**5 行加载模型、1 行播放语音口型同步**」（`playVoice()` 自动 RMS），新增 Cubism 3/4/5 兼容、**Tauri 支持**、远程音频 URL；
  评论区内 MooreThreads 工程师称 `guansss/pixi-live2d-display` **长期不维护、issue 无人回**。
- 中国台湾一手两处：`moonku44` 拆图细则（**A4 / 300–350dpi / 最长边约 4000px / 拆分到上·下眼皮分立 / 交档六查**）；
  「游戏角落」盗卖事件（数万元定制模型被 **300 元**挂 Etsy、**约三个月 36 笔交易**，工作室称系合作建模师出走）。

---

## 六、方法学：本轮三个「教训型」发现

### 6.1 ⚠️ **`index.html` 的脚注区已从正文区「漂移」出去，且没有任何闸门能看见**（**本轮最重要**）
- 实测：脚注 **[1301]–[1378]（78 条）整块嵌在卡片 `div class="card"`（`rpm38c4`）内部** ——
  位置在该卡的 `<p class="plain">` 之后、`.analogy` 之前（`index.html` 第 14793 行之后、14873 行之前）。
- **为什么一直没人发现**：`index_metrics` 的 E1–E7 只审「**数量与平衡**」（页头 / 恒等式 / 脚注缺号 / div 平衡 / 分组对账），
  **没有任何一条审「脚注住哪儿」**；div 计数照样平衡，恒等式照样成立 → **全绿**。
  **这是「闸门最危险的失败模式不是假警，是沉默」（M-0024 家族）的又一例，而且这次沉默的是「位置」这一维。**
- 全貌：文档里脚注实际分布在**至少三簇**（约 14795–19xxx 的中段簇 238 条 + `<footer>` 内 20359 行之后的主簇）；
  中段簇是被历轮 `insert_vN_cards.py` 的「插在最后一条脚注之后」规则**一路继承**下来的。
- **本轮处置（保守）**：新脚注 [1379]–[1402] 仍按既有规则插在 `r1378` 之后（不改迁移 → 不会让下一次整体重排更难）；
  **仅记录为下轮第一优先待办**，需要「把散落簇整体搬到 `<footer>` 内 + 给 `index_metrics` 加一条『脚注不得出现在 card 容器内』的判据（**配负对照**）」。

### 6.2 去重盲区已修复并有实效：补抓「卡内正文反引号提及型」`owner/repo`
上辑闸门拦下 4 个重复收录，暴露 URL 型基线只抓 `github.com/…`。本辑基线**新增**第二条：把 `index.html` 里
**反引号包裹的 `owner/repo`** 也导出去重表 → **62 条**。
本轮实测：**`stevenjoezhang/live2d-widget`、`guansss/pixi-live2d-display`、`sparcai-inc/bunraku`、`Panzer-Jack/easy-live2d` 四个候选**
都是靠这条通道确认「本体已在索引，只收使用姿势/文章」的 —— **URL 型基线对这四个全部漏检**。

### 6.3 「同名 ⇒ 不同源」也要逐条查（本辑复核两条）
`Inochi2D/inochi-session` 与索引里已有的 `Inochi2D/inochi-creator` **同组织不同仓**（一个是播放端、一个是创作端），
`DenchiSoft/VTubeStudio` 与索引里已有的 `Hawkbat/VTubeStudioJS` **同名不同源**（一个是官方 API 仓、一个是第三方 JS 封装）。
→ 与上辑「两条同源疑点结论正好相反」互为印证：**同源 / 不同源都不该预设。**

---

## 七、退役源复测（每条带复测期）

| 源 | 本轮 | 处置 |
|---|---|---|
| `creatorsforum.live2d.com` | **200** | 可读（`/latest.json` 可用），本辑**主要一手来源** |
| `community.live2d.com` | **200** | 可读；⚠️ `/latest.json` **404**，须改走 Vanilla API `/api/v2/discussions` |
| `docs.live2d.com` / `cubism.live2d.com` | **200** | 可读（SDK alpha2 手册仍 **404**，第 4 次复现） |
| `store.steampowered.com` | **200** | **延续回滚结论**，仍可读 |
| `gamemale.com` | **200 但正文是 Cloudflare Turnstile 挑战页**（标题「请稍候...」） | **复测结论与上轮一致**（cn 路建议：后续不再逐轮复测，直接沿用） |
| `note.com` / `reddit.com` / `medium.com` | **000** | 维持退役（本轮均未命中） |
| `vroid.com` | **403（WAF）** | 本轮未命中 |
| `hn.algolia.com` | **200 但 2167 命中全误召** | 无料（复测条件：出现标题含 Live2D 的非误召条目） |
| `dev.to`（tag=live2d） | 2 篇，最新 **2026-06-08** | 无新帖 |
| `juejin.cn` | 部分帖**新增风控**（`Access Denied / X-TT-System-Error: 3`） | **口径修正：掘金不能整站乐观，要按帖试** |
| `bbs.nga.cn` | **浏览器 200 / curl 403** | **新发现可用源**：正文可取，但 curl 直连被拒 |
| 米画师 / B站工房 / 博客园 / AcFun / 搜狐 | **200** | 均可直连取正文 |

---

## 八、索引与文档维护

- **索引**：`index.html` **1379 → 1403**（`insert_v41_cards.py` 增补 **24 卡**，脚注 [1379]–[1402]，分组 311，div **13003 平衡**）。
  跑前 `insert_guard_probe` 对 v41 **6/6**（P0 语法 + 1 正 5 反，基准 `eef3e2b:index.html`）；跑后 `index_metrics --update` 重封。
- **✅ 完成上辑待办①**：**22 个改名仓库的链接腐化就地更正** —— `_r37_fix_renames.py` 精确替换 **44 处 href + 23 处脚注显示名 + 1 处卡面名**
  （例：`hiyouga/LLaMA-Factory → hiyouga/llamafactory`）；改前逐条断言「2 href + 1 脚注」、改后断言旧路径计数 **= 0**、页头与 div 计数不变；
  备份 `_r37/index.html.pre-rename.bak`。
- **存档**：`csdn-social-summary-v36.md`（含第三十四 / 三十五 / 三十六辑）。
- **口径修正**：`AGENTS.md` §七 索引项数指针 1379 → **1403**（卡片 1386 / 脚注 1402）。
- 未落盘（超上下文）→ 见下节待办，不含糊带过。

---

## 九、下一辑待办（**按顺序做**）

1. ⭐ **修「脚注区漂移」**（见 §6.1）：把散落在正文区的脚注簇整体搬回 `<footer>`，并给 `index_metrics` 补一条
   **「脚注 div 不得出现在 `class="card"` 容器内」** 的判据 —— **加判据后必须跑 `gate_recall_probe` + 造负对照**（新判据假警比没有判据更危险）。
2. ⭐ **实测 `py-moc3`**（本辑最有用的一条）：`pip install py-moc3` → 扫一遍手上的 moc3，导出参数范围/纹理索引清单，验证 `moc3 verify`。
3. **实测 `easy-live2d v0.4.0` 的 `playVoice()` 一行口型**（接本地 Ollama TTS 走远程音频 URL）。
4. `/skill-doctor` 第三轮：**新根因 = 检测器本身失真** —— `_r34_skill_use.py` 量的是「技能名是否出现在记忆里」，
   **不等于「技能被加载过」**（本自动化专用技能 `round-research-index` 本轮显式加载即为例）。**先修判据，再判技能。**
5. DSH 插件生态单独成辑（已集齐 4 个实现 + 本辑 dsh-live2d）。
6. `Agent-desktop-pet` GUI 试装（隔离装 CPython 3.12，不改 vendor）+ 把状态读取半边接进本自动化。
7. **Cubism 5.4 alpha 下线（2026-10-18）后的第一手** —— 10-18 之后复测 alpha 入口是否转 beta、SDK 手册是否补 alpha2。
8. `ayagami` 复查（**连续第三轮无推进**：★351→352，pushed 仍 2026-09-14，releases 0 / tags 0，crates.io 只有占名）。
9. 回填收尾：38 条 `gh api` 未命中换通道补 + 45 条 `创建 … · 最近推送 …` 特殊格式。
10. consolidation（记忆合并淘汰，蓝本在 cn 路）。
11. 超上下文顺延：`motion-mirror` 本机可行性 · `MemOS` 35.24% 宣称复现 · 人工浏览器取知乎/B站视频页正文。

---

## 统计页脚

- 检索：gh 32 条正文 + 4 行边缘 · cn 24 条正文 · official 8 条新增 + 17 条口径复核 + 12 项可达性复测。
- 去重：基线 1337 `owner/repo` + **62 反引号型（新）** + 1379 URL；本轮 24 卡命中 **0**；**主 agent 逐条复验 32 个候选仓库（零出入、零 404）**。
- 索引：**1379 → 1403** 项（卡片 1386 / 脚注 1402 / 页头 1403）；分组 311；div 13003 平衡。
- 文档：`csdn-social-summary.md` 本辑；存档 `csdn-social-summary-v36.md`；`AGENTS.md` 指针已更新。
- 工具：`_r37_fix_renames.py`（改名仓库就地更正，含改前改后双向断言）。
- 闸门：`insert_guard_probe` 6/6 · `index_metrics` E1–E7 + 恒等式全绿 · `gate_recall_probe` · `index_card_loss_probe` · `doc_ref_check` · `house_rules --check` · `skill_budget` · `memory_health`。
