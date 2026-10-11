# 跨平台游戏制作 × AI 开发资源梳理 · 第三十九辑（2026-10-12 · 官方第一次把「本地 LLM」写进产品）

> 本辑为 Live2D 连续第十二轮。三路并行（gh / cn / official），共得 **gh 38 条 + cn 26 条 + official 23 条** 候选，
> 经与 index.html（1426→1448 项）及 csdn-social-summary（v36 / v34 / v33）比对，落索引 **22 张卡（1409→1431）+ 22 条脚注（[1426]–[1447]）**。
> 详细条目见 `_r39/_r39_gh.md` / `_r39_cn.md` / `_r39_official.md`。

## 一、搜索覆盖

| 路 | 覆盖 | 正条 | 备注 |
|---|---|---|---|
| gh | GitHub / Gitee / HF：工具·格式·查看器·引擎插件·AI 数字人 / 桌宠 | 38（工具 14 + [AI] 13 + 边缘 11） | 全部走 `gh api repos/<r>` 实测 |
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

- 落索引：`insert_v43_cards.py` → 22 张卡（1409→1431）+ 22 条脚注（[1426]–[1447]）；页头 1426→1448 项。
- 闸门：`insert_guard_probe` **6/6**；`index_metrics` **E1–E8 全绿**（恒等式 1448 == 1447+1，div 13763/13763），`--update` 已重封 313 分组快照；`index_metrics --selftest` 8/8；`gate_recall_probe` 漏检 0 / 假警 0。
- 新增工具：`_r39/fix_footnote_drift.py`（修漂移）、`_r39/diag_footnote_container.py`（容器诊断）、`_r39/e8_negative_probe.py`（E8 负对照）。
- 判据变更：`index_metrics.py` 增 **E8 脚注位置** + **W4**（footer 内不在 srcs）、**W5**（无 footer 时 E8 跳过）。

## 七、下一辑待办（按顺序）

1. ⭐ **按 [1446] 那份笔记真跑一遍 AI 桌宠**（渲染侧与 LLM 侧本轮都已验证可用，缺的是走通）—— 建议从 `HiyoriAI`（★93/MIT/可指 Ollama）或 DoroPet_V3 入手。
2. ⭐ **追 nizima LIVE 2.7 的后续**（官方第一次给本地 LLM 开口子，值得盯它有没有放出接口细节/文档）。
3. **把 414 条「footer 内但不在 srcs 容器」的脚注（[661]–[1074]）也搬进 srcs**（本轮 W4 提示，位置能用但容器不规范）。
4. **gamemale 顺着「搜索引擎快照」这条路继续挖**（本轮已证明可行，只取到 3 帖）。
5. **note.com 正文**（连续多轮未取到；可能需要带登录态或换检索式）。
6. **ayagami 复查**（连续多轮无推进，考虑降级为「每季度查一次」）+ DSH 插件生态成辑。
7. 超上下文顺延：`wan-h/awesome-digital-human-live2d` 试装 · `motion-mirror` 本机可行性 · 1290 张旧卡 `updated_at/pushed_at` 回填。

## 统计页脚（第三十九辑）

- 检索：gh 38 条正文 + 11 边缘 · cn 26 条 · official 23 条。
- 去重：对 index.html（1426 项）+ csdn-social-summary（v36 / v34 / v33）+ `_r38/_r38_gh.md` 全表逐条 `grep -iF`，**落卡的 22 条零重复**；剔除内容农场（SAM2 第三次出现在新镜像站）、已收录旧闻（Bunraku / Open-LLM-VTuber 仓库本体）。
- 索引：**1426 → 1448 项**（卡片 1409→1431 / 脚注 1425→1447）；分组 312→313。
- 闸门：`insert_guard_probe` 6/6 · `index_metrics` E1–E8 全绿 + `--update` · selftest 8/8 · `gate_recall_probe` 0/0 · E8 负对照 ✅。
- 原始：`_r39/_r39_gh.md` · `_r39_cn.md` · `_r39_official.md` · `insert_v43_cards.py` · `fix_footnote_drift.py` · `diag_footnote_container.py` · `e8_negative_probe.py`。

---

