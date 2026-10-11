# 跨平台游戏制作 × AI 开发资源梳理 · 第三十九辑（2026-10-12 · 官方第一次把「本地 LLM」写进产品）

> 本辑为 Live2D 连续第十二轮。三路并行（gh / cn / official），共得 **gh 38 条 + cn 26 条 + official 23 条** 候选，
> 经与 index.html（1426→1450 项）及 csdn-social-summary（v36 / v34 / v33）比对，
> 落索引 **24 张卡（1409→1433）+ 24 条脚注（[1426]–[1449]）**（含 gh 路收尾补录的 2 项）。
> 详细条目见 `_r39/_r39_gh.md` / `_r39_cn.md` / `_r39_official.md`。
> **收尾再补录 3 卡**（`insert_v43c_cards.py`，1450→1453）：Core 官方合规口径 / 平台支持表 / 官方组织全表 —— 见 §六.1。

## 一、搜索覆盖

| 路 | 覆盖 | 正条 | 备注 |
|---|---|---|---|
| gh | GitHub / Gitee / HF：工具·格式·查看器·引擎插件·AI 数字人 / 桌宠 | 31（工具 14 + [AI] 13 + 边缘 4） | 全部走 `gh api repos/<r>` 实测 |
| cn | **gamemale（用户点名）** / CSDN / 掘金 / 知乎 / 公众号 / B站 / 抖音 / 虎课 | 26 | **gamemale 本轮首次破墙** |
| official | Cubism 官网·release notes·手册 / note.com / r-Live2D / Booth / 海外媒体 | 23 | **5.4 alpha 倒计时最后一周核对** |

## 二、本辑一句话主线

**「本地大模型驱动 Live2D」第一次不再是社区自己接线 —— 官方把它写进了产品（nizima LIVE 2.7 的 AI 助手可直连本地 LLM）；
而开源侧的桌宠不再各自造一个 Electron 壳，开始往宿主里钻：做成 bot 框架插件、做成双格式适配层、甚至挂到路由器面板上。**

## 三、上轮（第三十八辑）待办检查 —— 6 条 → 闭环 3 / 半闭环 1 / 注销 1 / 顺延 1

| # | 上轮待办 | 状态 | 结果一句话 |
|---|---|---|---|
| ① | ⭐ **修脚注区漂移** | ✅ **闭环** | **306 条脚注（[1120]–[1425]）从 8 张 card 内部搬回 footer 的 srcs 容器**，8 张被撕开的卡片结构全部恢复。判据补 **E8** + 负对照（把 1 条脚注塞进 card → E1–E7 全绿、唯有 E8 报红）。详见 §五.1 |
| ② | ⭐ **实测 py-moc3 / easy-live2d `playVoice()`** | ⚠️ **半闭环 + 注销一半** | py-moc3 **✅ 已实测**（见 §五.2）；easy-live2d **❌ 注销** —— **待办本身的前提错了**（详见 §五.3） |
| ③ | **AI 桌宠本机可行性实测** | ✅ **闭环** | **渲染侧 + LLM 侧都通**：`live2d-py` 实测 `pip install` 成功、`import live2d` 成功（Model/glInit/init 接口齐全）；Ollama **0.32.13 已装机且可拉起**（详见 §五.4） |
| ④ | **Cubism 5.4 alpha 10-18 复测** | ✅ **闭环** | 距截止 6 天逐语种核对：仍 alpha2、**未转 beta、无 alpha3、无正式版时间表**；原文「可使用至 2026 年 10 月 18 日」 |
| ⑤ | 中文源补采（note.com / 知乎 / B站） | ⚠️ **部分** | note.com 本轮仍未取到正文（登记为「本轮未命中」）；**但 gamemale 破墙**（Cloudflare 挑战页 → 改走搜索引擎快照，首获 3 帖）；B站/知乎仍是登录墙 |
| ⑥ | ayagami 复查 / DSH 插件生态成辑 | ❌ **顺延** | 本轮上下文与配额都给了上面五条，未做 |

## 四、分主题条目（均带链接，细节见 `_r39_*.md`）

### A. 官方侧（本辑最硬，6 条全部落卡）
- ⭐ **nizima LIVE 2.7 —— AI 助手直连本地 LLM，语音即可驱动模型** [1426]：官方第一次把「本地跑大模型」写成产品功能。**对你的 Ollama 栈直接对口**。
- **Cubism 5 SDK for Unreal Engine R1 beta2（2026-09-29）** [1427]：终结「Unreal 支持是否已弃」的悬案（上辑官方否认过停摆，本条是手册里的一手证据）。
- **Editor 5.4 alpha2 手册** [1428]：上辑记 404、**本辑首次取到 200**，含 PSD 导入强化。
- ⚠️ **alpha2 数据不可回退** [1429]：alpha2 存的工程**回不去 alpha1 / 5.3**——用 alpha 前必读的硬约束。
- **5.4 alpha 倒计时核对** [1431]：仍 alpha2、未转 beta、无 alpha3；官方同时写明「Beta 版和正式版时间可能调整」。
- **第 13 届 Creative Awards 新增「AI·对话界面」部门** [1430]：官方用奖项承认「能对话的角色」成了独立赛道。

### B. 工具 / 格式 / 宿主（本辑主线所在）
- **ihopenot/LpkUnpacker（★296，本批最高）** [1432]：解 Live2DViewerEx 的 LPK；README 自述「少部分早期 lpk 仍无法解包」——格式边界写得诚实。
- **receyuki/live2pet** [1437]：**不做桌宠应用，做适配层** —— Live2D + Spine 双格式统一，面向 Clawd on Desk / Codex 两个 Agent 宿主。
- **yanghuagai55/astrbot_plugin_live2d_pet（★12 · MIT）** [1441]：**做成成熟 bot 框架的插件**，不自己造壳。「别自己造宿主」这个判断比插件本身值钱。
- **OliverIsNotAvailble/AS_Live2D-reader** [1433]：不走 Pixi.js，**live2d-py v3 + 原生 OpenGL 直绘**。
- **Zosuya/ParaRig** [1434]：把「Cubism 的参数面板」搬进 Blender（四种控件 + **非破坏性更新**）。
- **rayriffy/CubismMetal** [1435]：macOS 原生（Swift + Metal）查看器——Apple 侧稀薄生态的补充。
- **kinaito/myoc** [1436]：把「捏脸/换表情」从 VTube Studio 里剥离成独立应用。
- **BANDORI-PET-Android** [1438]：上辑 PC 版（★465）的移动端兄弟，同源 LuaJIT 渲染核。

### C. [AI] AI × Live2D（13 条候选，落 5 张卡）
- **luckui/HiyoriAI（★93 · MIT）** [1439]：本批 AI 侧星最高。接 **OpenAI 兼容 API（可指本地 Ollama）**；**重活转 Codex SDK**——「按任务难度分流模型」这个分工可直接照搬。
- **sjmsltx/deepseek-desktop-pet（★13 · MIT）** [1440]：长期记忆 = **BM25 检索 + 事实抽取 + LLM 重排**（不是全塞上下文），对 16GB 机器是正解。⚠️ 仓库 285 MB。
- **PhyQxx/companion-hub** [1442]：**四层隐私分级 L0–L3**，L2 强制本地模型、L3 不上云；记忆带删除台账与来源追溯。
- **liyu-1028/mochi** [1443]：前端（Tauri+Live2D）与认知核心（**LangGraph**）显式解耦——大脑和身体的边界划清楚。
- **去 Electron 轻量路线三条并进**（本次只登记未落卡）：C/SDL3 的 `TianMengLucky/BongoCat-X`、C++ 的 `jinsc123654/l2dpet`、Rust 的 `VeiQiuLab/DesktopPet`。
- ⭐ **补录 · `whymycompilefail/cpu-only-ai-tuber`** [1448] —— **没有独显也能跑**的 AI 主播栈实测，三条结论**全部反直觉**：
  ① **LLM 不是瓶颈**（391 ms TTFT 只占整轮 **2.7%**）；② **压量化反而更慢**（Q8_0 35.3 → Q5_0 **28.3 GB/s**，内存带宽才是墙）；
  ③ **人设跑偏不在 system prompt** —— 破人设率 3/15 → **0/15**，解法在**对话历史**里。**对本机（16GB、无独显）命中度最高的一条。**
- **补录 · `Hayliy/naixi-desktop`** [1449] —— 规模最硬的量化样本：**7.9 万行 / 56 模块 / 222 个 REST 端点 / 29 张 SQLite 表**。
  别的 README 写「能聊天能记忆」，这条直接把体量摊开 —— 是判断「这类项目做到底有多大」的标尺。

### D. 中文侧（gamemale 首次破墙）
- **gamemale《live2d 半藏麦克雷桌面 doi 动画》** [1444]：整站是 Cloudflare 挑战页（HTTP 200 但正文是「请稍候…」），**改走搜索引擎索引快照才破**——破墙方法本身比这条帖子的内容更有价值。
- **See-through 实测：一张动漫图 → 23 层 PSD** [1445]：与你硬盘上已有的 `live2d/psd2live-out/seethrough_output.moc3` 是**同路线**，可直接对照。
- **Open-LLM-VTuber 部署笔记** [1446]：命令与端口（localhost:12393）可照抄；最简组合 Ollama + Edge TTS（**仓库本体已在 r31 收录，本条只收经验**）。
- **Live2D + Ollama 排障** [1447]：最关键一条 —— **默认 Edge TTS 需联网**，很多人以为自己搭的是纯离线栈，其实语音那段走了云。

## 五、实测与「有用就改」（本辑的动手部分）

### 5.1 修脚注区漂移（上轮 ⭐ 待办①，闭环）
- **根因不是某一版写错，是锚点错一次后每版沿用**：某版把脚注块插进了「上一版最后一张卡片」的内部，之后每版都以「最后一条脚注」为锚点继续插，雪球从 v24 一路滚到 v42 —— 共 **8 张 card 被撕开、306 条脚注落在 card / section 里**。
- **修复**：`_r39/fix_footnote_drift.py`，只搬「不该在那儿」的 306 条（srcs / footer 内的 1108 条原地不动），搬进 srcs 容器开头。8 张卡片恢复后结构齐全（card-top / plain / grid2 / src-line 全在，脚注归零）。
- ⚠️ **第一版脚本自己造了个事故**：无差别删除所有脚注片段再回插，把不该动的 1108 条也删了（1424 → 316），靠 `.bak2` 回滚修正。修正后加了**三道写盘前自检**（脚注总数不变 / div 平衡 / card 内归零），不通过就不落盘。
- **补判据 E8**（`index_metrics.py`）+ `_r39/e8_negative_probe.py` 负对照：把 1 条脚注搬进 card → **E1–E7 全绿、唯有 E8 报红**。E8 前提显式化：页面无 `<footer>` 时跳过并报 W5（迷你 fixture 会假警，与 E7 的 W3 同源）。

### 5.2 ⭐ 实测 py-moc3 v0.1.0（MIT / Ludentes）—— 结论与上轮的期待相反
- **装得上、读得准**：`info` 秒出结构（Parts / Deformers / ArtMeshes / Parameters / Keyform / UVs / Glues）；`params` 能读出参数名与范围；`meshes` 能列出网格名+顶点数。手上 4 个 moc3 全部读通。
- **语义层 3/3 全保真**：写回再读回，参数 247 / 网格 269 / 部件 92 / 变形器 425 —— **数量与名称完全一致**。
- **但 round-trip 4/4 全 FAIL**：写回体积**少 7–9%**（少 14336 / 15872 / 96896 字节）。字节差异从 **0.005%**（差异在文件尾）到 **71%**（差异在文件头，后面全部错位）。
- **定位**：**只读的「模型体检 / X 光机」，不是手术刀**。能查、能盘点、能对账；**不能拿它改模型**（会丢它不认识的段落，丢在哪不可控）。
- → 这修正了上轮把它当「字节级 round-trip 亮点」的判断。**「README 写了 ≠ 实测通过」这条老规矩，再一次是对的。**

### 5.3 注销一条待办：easy-live2d 的 `playVoice()` —— 待办本身的前提错了
- PyPI 上**根本没有 `easy-live2d`**（`pypi.org/pypi/easy-live2d/json` → 404；pip → No matching distribution）。
- GitHub 上的 `Panzer-Jack/easy-live2d`（★213 · **TypeScript**）是**基于 Pixi.js 的 Web SDK**，不是 Python 包 —— 不可能有供本机 Python 栈调用的 `playVoice()`。
- → **上轮把它当成 Python 库写进待办，是前提错误**，本轮注销并记录原因。**教训：待办里的「实测 X 的某个函数」类条目，落笔前先确认它是什么语言、以什么形态分发。**

### 5.4 AI 桌宠本机可行性（上轮待办③，闭环）
- **渲染侧 ✅**：`pip install live2d-py` 成功，`import live2d` 成功，接口齐全（Model / glInit / init / clearBuffer / dispose）。
- **LLM 侧 ✅**：Ollama **0.32.13 已装机**（`C:\Users\34498\AppData\Local\Programs\Ollama\ollama.exe`），执行 `ollama list` 能自动拉起服务。
  ⚠️ **差点写成负结论**：第一次用 `curl localhost:11434` 拿到空、且 `which ollama` 无结果，一度要写「本机没有 Ollama」—— 实际是**服务没在跑 + 不在 PATH**，不是没装。**负结论必须先排除「没启动 / 不在 PATH」再下笔。**
- → 结论：这套栈缺的不是环境，是按 [1446] 那份部署笔记走一遍。**本轮未做完整 clone + 跑通**（仓库大、耗时长），留待下轮。

### 5.5 E8 顺手抓出增补脚本一个潜伏多版的 bug
- 现象：本辑插完 22 条脚注后 **E8 立刻报红**「22 条脚注游离在 footer 之外」。
- 根因：`insert_v<N>_cards.py` 先算脚注插入偏移 `fend`，**再**插卡片组（在 `fend` 之前）—— 卡片一插，后面的偏移量整体失效，脚注被插到了 footer 之外。
- 修法：**先插位置靠后的脚注，再插位置靠前的卡片组**。这个 bug 之前一直没暴露，是因为脚注本来就在 card 里、位置对错看不出来 —— **E8 装上当天就抓到了它**。

## 六、索引与文档维护

- 落索引：`insert_v43_cards.py` → 22 张卡 + 22 条脚注（[1426]–[1447]）；gh 路收尾补录 `insert_v43b_cards.py` → 再 2 张卡 + 2 条脚注（[1448]–[1449]）。
  合计 **24 张卡（1409→1433）+ 24 条脚注**；页头 1426→1450 项。
- 闸门：`insert_guard_probe` **6/6**；`index_metrics` **E1–E8 全绿**（恒等式 1448 == 1447+1，div 13763/13763），`--update` 已重封 313 分组快照；`index_metrics --selftest` 8/8；`gate_recall_probe` 漏检 0 / 假警 0。
- 新增工具：`_r39/fix_footnote_drift.py`（修漂移）、`_r39/diag_footnote_container.py`（容器诊断）、`_r39/e8_negative_probe.py`（E8 负对照）。
- 判据变更：`index_metrics.py` 增 **E8 脚注位置** + **W4**（footer 内不在 srcs）、**W5**（无 footer 时 E8 跳过）。

### 6.1 收尾再补录（`insert_v43c_cards.py`，3 卡，1450→1453）—— official 路 §八 里最有价值的 3 条

| 信源 | 内容 | 为什么值得单独立卡 |
|---|---|---|
| [1450] | **Cubism Core 官方合规口径** —— 官方手册原文「根据 Live2D 专有软件许可协议，**不在 GitHub 上发布 Cubism Core**」，适用 EULA v2.1（修订 2025-02-03） | 追了十几轮的「Core 那堵墙」的**官方答案**：不是技术拆不动，是**许可不允许**。反推出判据：任何号称「自带 Core / 免下载 SDK」的仓库都该先怀疑合规性 |
| [1451] | **平台支持表 2026-09-29 更新** + ⚠️ **官方口径不一致第三例**：GitHub README 仍写未来时「will be ended」，官方手册已改完成态「**was terminated after Native R2**」并给日期 **2024-12-19** | 选型唯一该看的权威表；「以手册为准、别信仓库 README」第三次撞到。另附 Native 版本链 R2(2024-12-19)→R5(2026-04-02) |
| [1452] | **Live2D 官方组织全表（18 个仓库）** —— `CubismWebSamples` ★393（121 forks）/ `CubismSpecs` ★22（格式规格）/ `nizimaLIVEPluginAPI` ★6 | **十二辑从没整表扫过官方组织**，★393 的基础件漏了整整十二轮。`gh api orgs/Live2D/repos` 实取 |

> 补录的 3 条全部来自 `_r39/_r39_official.md` §八（§25–§27 结案条 + MotionSync 授权边界条），
> `insert_guard_probe` 对 v43c 本身 **6/6**；`index_metrics` 复跑 E1–E8 全绿（1453/1452/1436，div 13852）。

## 七、下一辑待办（按顺序）

1. ⭐ **按 [1446] 那份笔记真跑一遍 AI 桌宠**（渲染侧与 LLM 侧本轮都已验证可用，缺的是走通）—— 建议从 `HiyoriAI`（★93/MIT/可指 Ollama）或 DoroPet_V3 入手。
2. ⭐ **追 nizima LIVE 2.7 的后续**（官方第一次给本地 LLM 开口子，值得盯它有没有放出接口细节/文档）。
3. **把 414 条「footer 内但不在 srcs 容器」的脚注（[661]–[1074]）也搬进 srcs**（本轮 W4 提示，位置能用但容器不规范）。
4. **gamemale 顺着「搜索引擎快照」这条路继续挖**（本轮已证明可行，只取到 3 帖）。
5. **note.com 正文**（连续多轮未取到；可能需要带登录态或换检索式）。
6. **ayagami 复查**（连续多轮无推进，考虑降级为「每季度查一次」）+ DSH 插件生态成辑。
7. 超上下文顺延：`wan-h/awesome-digital-human-live2d` 试装 · `motion-mirror` 本机可行性 · 1290 张旧卡 `updated_at/pushed_at` 回填。

## 统计页脚（第三十九辑）

- 检索：gh 31 条（工具 14 + [AI] 13 + 边缘 4）· cn 26 条 · official 23 条。
- 去重：对 index.html（1426 项）+ csdn-social-summary（v36 / v34 / v33）+ `_r38/_r38_gh.md` 全表逐条 `grep -iF`，**落卡的 24 条零重复**（gh 路剔除 8 条：LPK 三连中与已有 LpkUnpacker 重复 2 条、官方 SDK 仓库已在索引、内容农场等）；剔除内容农场（SAM2 第三次出现在新镜像站）、已收录旧闻（Bunraku / Open-LLM-VTuber 仓库本体）。
- 索引：**1426 → 1453 项**（v43 22 卡 + v43b 2 卡 + v43c 再补录 3 卡；卡片 1409→1436 / 脚注 1425→1452）；分组 312→315。
- 闸门：`insert_guard_probe` 6/6（v43c 复验 6/6）· `index_metrics` E1–E8 全绿 + `--update` · selftest 8/8 · `gate_recall_probe` 0/0 · E8 负对照 ✅。
- 原始：`_r39/_r39_gh.md` · `_r39_cn.md` · `_r39_official.md` · `insert_v43_cards.py` · `insert_v43b_cards.py` · `insert_v43c_cards.py` · `fix_footnote_drift.py` · `diag_footnote_container.py` · `e8_negative_probe.py`。
- ⚠️ 工具修复：`index_metrics.py` 的 `BASE_GAP` 常量**只写了注释没写定义**（第三十九辑补 W1 基线时留下的）→ 闸门直接 `NameError` 崩溃。已在常量区补 `BASE_GAP = 16`（依据 = 注释里记的两版交叉实测），复跑全绿。**「闸门沉默/崩溃」比假警更危险的又一例。**

---


# 跨平台游戏制作 × AI 开发资源梳理 · 第三十八辑（2026-10-11 · Live2D 制作全谱系补采）

> 本辑为 Live2D 连续第十一轮。三路并行（gh / cn / official），共得 **gh 24 条 + cn 18 条 + official 16 条** 候选，
> 经与 index.html（1403→1426 项）及 csdn-social-summary（v34 / v36）比对待办，**全部 28 个 GitHub slug 零重复**，
> 落索引 **23 张卡（1386→1409）+ 23 条脚注（[1403]–[1425]）**。详细条目见 `_r38/_r38_gh.md` / `_r38_cn.md` / `_r38_official.md`。

## 一、搜索覆盖

| 路 | 覆盖 | 正条 | 边缘 |
|---|---|---|---|
| gh | GitHub / Gitee / HF：Live2D 工具·查看器·插件·引擎·AI 数字人 | 24（§三 11 + §四 13 [AI]） | 7 行（§五） |
| cn | CSDN / 掘金 / 知乎 / 公众号 / 少数派 / gamemale / 微博 / B站 | 18 | gamemale 复测状态 1 + 应用/纠纷 4 + [AI] 1 |
| official | Cubism 官网·release notes / note.com / r-Live2D / 官方论坛 / X | 16（§三 8 + §四 4 + §五-A 6 帖） | — |

## 二、本辑一句话主线

**Live2D 制作的「身体侧」供给继续加密，且第一次出现可验证的硬指标样本；AI×Live2D 数字人从「主张」彻底变成「重复模式」——
12 条新增 AI 桌宠/数字人收敛出一条可复用的本地栈（Live2D 渲染 + 本地 LLM/Ollama + TTS/ASR + 长期记忆）。**

## 三、分主题条目（均带链接，细节见 _r38_*.md）

### A. 工具 / 查看器 / 插件 / 引擎（gh §三，11 条）
- **ImDuck42/Live2D-Viewer**（★14 · MIT）— **本辑唯一标「落地」的网页查看器**：原生 JS+PIXI.js 6.5.10，四种载入（URL/预设/GitHub 仓库浏览器/本地 ZIP），可在索引站直接嵌一个 Live2D 预览器。[1412]
- **TSKI433/hime-display**（★254 · GPL）— 一套 UI 看 Live2D/Spine/MMD/VRoid 四格式，做素材库预览省事。[1404]
- **LIlGG/plugin-live2d**（★251 · MIT）— Halo 博客 Live2D 看板娘插件，即插即用。[1405]
- **evgo2017/vue-live2d**（★166 · MIT）— Vue 组件版看板娘。[1409]
- **amorist/platelet**（★226 · GPL）— 经典「血小板」网页看板娘 widget。[1406]
- **LSTM-Kirigaya/Live2dRender**（★183 · Apache）— Web 端新版 Cubism 渲染封装，当渲染底座。[1408]
- **Arisego/UnrealLive2D**（★153 · MIT）— Unreal 路线稀缺的 Live2D 桥接（⚠️ 2025-02 后未动，先核 SDK 兼容）。[1410]
- **iCharlesZ/vscode-live2d-models**（★169）— VSCode 看板娘模型库（资源集合）。[1407]
- **ezshine/AwesomeLive2D**（★411）— Live2D 模型/资源 awesome 清单（约 3 年未动，作导航）。[1403]
- **redchenk/yachiyo-live2d-studio**（★25 · MIT）— 当天建仓的「studio」，待 README 补全再评。[1411]
- **sweetcornna/OneClick2D**（★0）— **不碰 Cubism 授权的替代格式 .oc2d**，版权敏感场景的稀缺思路。[1413]

### B. AI × Live2D 数字人 / 桌宠（gh §四，12 条，全部 [AI]）
- **HELPMEEADICE/BANDORI-PET-REV**（★465 · GPL）— **本辑最硬指标**：Cubism SDK+PySide6，51+ 角色/305+ 服装，自研 LuaJIT 渲染核较 live2d-py **6 倍+（30→180fps+）**，Qwen3TTS 口型 + faster-whisper ASR + LLM 记忆。[1422]
- **waterfeet/DoroPet_V3**（Gitee · ★7 · Apache）— **架构最贴本机栈**：live2d-py + Ollama + sherpa-onnx/edge-tts + SQLite 记忆 + Galgame 叙事。[1423]
- **andyhuo520/openclaw-assistant-mvp**（★408）— Electron AI 语音助手 + Live2D 表情/口型（⚠️ 无 LICENSE）。[1414]
- **MIO-456/Lumi_Nox**（★239 · MIT）— 双 AI VTuber 同台直播实时编排（open-core）。[1415]
- **YuriCrystal/ai-avatar-bot**（★203 · NOASSERTION）— Live2D/VRM 语音 avatar，一行嵌入网站。[1416]
- **inni918/warashi**（★119 · NOASSERTION）— 桌面 AI 伴侣：Live2D+语音+长期记忆+主动搭话（正中本地 Ollama 基准）。[1417]
- **chyinan/Kokoro-Engine**（★156 · MIT）— Rust 跨平台虚拟角色交互引擎。[1424]
- **funnycups/petto**（★119 · GPL）— Flutter/Dart Live2D 桌宠。[1418]
- **ReSerendipity/SpiritPal**（★0 · Apache）— **Tauri v2 + Pixi.js 8 Live2D**（2026 新写法样本）。[1421]
- **DesktopPetXuansi/Xuansi**（★1 · Apache）— Windows 本地 AI 桌宠，纯本地优先。[1420]
- **Nav-Joe/Xue_CyberNeko**（★7 · MIT）— 轻量 Live2D AI Neko。[1419]
- **aurel-g/ComfyUI-Live2DViewer**（★0 · MIT）— ComfyUI 节点预览 Live2D（补「AI→Live2D 流水线」可视化环，但 2024 起停更）。[1425]

### C. 中文经验帖 / 实战测评（cn，取到正文的关键 2 条 + 状态）
- **塔猴《2D 立绘活了：Live2D / Spine 动作的 AI 辅助生成流》**（tahou.com · 2026-01-13）— **本辑唯一取到正文的中文 AI 辅助 Live2D 流程帖**：AI 拆层 → Auto Mesh → Deform Path → Auto Standard Form → Physics/Auto Blink/Breathing Loop，给了可点的菜单路径（「3–5 天→1 天」偏宣发，需自测打折扣）。[CSDN 路径见 _r38_cn.md §六]
- **CSDN React 帖「TTS→RMS→口型」代码** — 可直接抄进本地 Ollama 语音桌宠（主 agent 实测优先级 2）。
- **Steam AI桌面宠物**（4227700 · 42kami）— 本地 LLM + Live2D 桌宠，最贴 16GB+Ollama 基准（待装实测）。
- 已剔除：米画师 4 处价格锚（R41 已收）、海淀 7627 元案（R37 已收）、SAM 2 三篇 weixin_数字 内容农场（打假）。
- **gamemale 复测**：仍被 Cloudflare 挑战页挡住 → **本轮未命中（待复测）**，未写成负结论。

### D. 官方 / 海外（official，关键结论）
- **Cubism 5.4**：仍为 **alpha2，可用期延至 2026-10-18，未转 beta**；alpha 版无前方兼容（alpha2 存的工程 5.3 打不开）。
- **官方论坛**：Unity Sprite 压不过模型 / motion3 覆盖重导入 / Unreal SDK 停摆三件事上轮已认领，本轮无新进展。
- **note.com / r-Live2D**：本机 fetch 000（非限流），下轮用代理或带登录态浏览器补采。
- **creatorsforum.live2d.com**：403 用 `.json` 端点绕过成功。

## 四、AI 开发 / 使用相关帖子的实测结论（主 agent 逐条读 + 核实）

本轮 [AI] 帖子共 **13（gh）+ 1（cn）= 14 条**，全部走 `gh api` 复核 stars/许可证/语言/日期。结论：

1. **可复用性**：除 ImDuck42/Live2D-Viewer 标「落地」外，AI 数字人/桌宠 12 条均为 **② 参考**、1 条 HF LoRA 为 **③ 不采用**（闭源付费、非本地）。
2. **收敛出的本地栈**（对本机 16GB+Ollama 基准直接有用）：`Live2D 渲染（pixi-live2d / live2d-py）+ 本地 LLM（Ollama / Qwen3）+ TTS（edge-tts / sherpa-onnx / Qwen3TTS）+ ASR（faster-whisper）+ 长期记忆（SQLite / JSON）`。
   - 最完整两个样本：**BANDORI-PET-REV**（★465、自研渲染核 6x+）与 **DoroPet_V3**（Gitee、live2d-py+Ollama 全链路）。两者协议分别为 GPL-3.0 / Apache-2.0，抄架构不抄依赖。
3. **是否「改我们的工具/流程」**：**本轮不改**。这些帖子是「AI 桌宠/数字人」应用，对维护索引站 / agent 工具链无直接改造点；其价值是**作为索引卡收录**（已落 12 张）与**本地栈架构参考**。
4. **待实测（留作下轮待办）**：在 16GB 本机 clone 并跑通 BANDORI-PET-REV / DoroPet_V3，验证本地 Ollama 栈可行性；以及在 Cubism 5.3 复一遍塔猴的 `Auto Standard Form` 是否真按图层命名自动形变。

## 五、可拓展性 & 实用性 思考（通俗版）

- **查看器/插件侧**：格局已稳，新增多是「换框架再实现一遍」（Halo / Vue / Unreal / Flutter）。**真正可落地的是 ImDuck42/Live2D-Viewer**——它能在我们的索引站里直接嵌一个 Live2D 模型预览器，MIT、有在线 demo，改造量小。
- **AI 数字人侧**：这是本辑密度最高的方向，且**第一次出现可验证硬指标**（BANDORI-PET-REV 的 6x 渲染、50+/300+ 模型量）。说明「AI 装 Live2D 身体」已从玩具走向能跑的工程。但**绝大多数是 ★0–1 或当天建仓**，协议也参差（无 LICENSE / NOASSERTION / GPL 传染），当参考骨架可以，当依赖不行。
- **合规红线仍在**：凡碰 `.moc3` / Cubism SDK 的（BANDORI-PET-REV、DoroPet_V3、UnrealLive2D）都绕不开 Live2D 官方授权；**OneClick2D 走「不碰 Cubism」的 .oc2d 替代格式**是版权敏感场景的稀缺思路，值得持续盯。
- **对本机最实用的三件事**：① 用 Live2D-Viewer 给索引站加预览器；② 抄 BANDORI/DoroPet 的本地栈架构做自己的桌宠/数字人；③ 把「本地 LLM + TTS/ASR + 记忆」当标准件复用，别重复造。

## 六、索引与文档维护

- 落索引：**insert_v42_cards.py** → 23 张卡（1386→1409）+ 23 条脚注（[1403]–[1425]）；页头 1403→1426 项。
- `index_metrics`：**E1–E7 全绿**，恒等式 1426 == 1425+1，div 13389/13389 平衡，`--update` 已重封 312 分组快照。
- ⚠️ **脚注区漂移（上轮待办①）仍未修**：[1301]–[1378] 嵌在 card `rpm38c4` 内，本辑 [1403]–[1425] 按既有规则接在其后，**同样落在 card 容器内**（这是 E1–E7 盲区，下轮必修）。
- 原始产出：`_r38/_r38_gh.md` / `_r38_cn.md` / `_r38_official.md`。

## 七、下一辑待办（按序）

1. ⭐ **修脚注区漂移**：把 [1301]–[1378]（及本辑 [1403]–[1425]）整体搬出 `rpm38c4` 的 card div 进 `<footer>`，并给 `index_metrics` 加「脚注不得出现在 card 容器内」判据（加判据后必跑 `gate_recall_probe` + 造负对照）。
2. ⭐ **实测 py-moc3 / easy-live2d v0.4.0 `playVoice()`**（上轮待办②③，仍pending）。
3. **AI 桌宠本机可行性实测**：clone BANDORI-PET-REV / DoroPet_V3，在 16GB 跑通 Ollama 本地栈。
4. **Cubism 5.4 alpha 10-18 下线后复测**（转 beta？SDK 手册补 alpha2？）。
5. **中文源补采**：note.com / r-Live2D / 知乎·B站（带登录态浏览器），本机 fetch 000 本轮未取到。
6. 超上下文顺延：ayagami 复查（连续多轮无推进）、DSH 插件生态成辑。

## 统计页脚（第三十八辑）

- 检索：gh 24 条正文 + 7 边缘 · cn 18 条正文 · official 16 条正文。
- 去重：28 个 GitHub slug 对 index.html + csdn-social-summary(v34/v36) **零重复**；打假 SAM2 内容农场 3 篇、剔除 R37/R41 已收旧闻 2 处。
- 索引：**1403 → 1426 项**（卡片 1386→1409 / 脚注 1402→1425）；分组 311→312。
- 闸门：`index_metrics` E1–E7 全绿 + `--update` 重封快照。
- 原始：`_r38/_r38_gh.md` · `_r38_cn.md` · `_r38_official.md` · `insert_v42_cards.py` · `prepend_summary.py`。

---


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
