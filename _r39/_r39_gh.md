# 第三十九辑 · gh 路（2026-10-12）

> 本路只覆盖 GitHub / Gitee / HuggingFace 上的 Live2D 相关仓库与项目。CSDN/官网/论坛由其他子 agent 覆盖，本路不重复。
> 取数方式：GitHub 走 `gh api repos/<r>`（取数日 2026-10-12）；Gitee 走 `gitee.com/api/v5/repos/<r>`；HF 走 WebSearch/WebFetch。限流或 404 均已标注（404 ≠ 不存在）。
> 去重基线：`index.html`（1426 项 / 1409 卡，含 **r38 已落 [1403]–[1425] 共 23 张**）+ `csdn-social-summary.md` + `-v36.md` + `-v34.md` + `-v33.md` + **\_r38/\_r38_gh.md 全表**。
> 去重操作：每条候选先 `grep -iF "<owner/repo 或标题关键词>" index.html csdn-social-summary.md csdn-social-summary-v36.md csdn-social-summary-v34.md`，命中即弃；再比对 _r38_gh.md。
> 本轮额外看点：① 有没有继 `Ludentes/py-moc3` 之后「不做渲染」的纯解析工具；② 有没有把绑定做成可复用流水线的第二例（继 `tsunehimatoi/psd2live`）。

## 一、搜索覆盖

- **GitHub（主力）**：`gh search repos` 共 **22 条查询式**，覆盖两类维度——
  - *广度*：`live2d`(按 stars 前 100) 、`moc3`、`cubism-sdk`、`cubism moc3 rust`、`live2d rigging`、`live2d cubism 4`、`live2d binding`、`moc3 parser`、`live2d editor`、`live2d sdk`、`live2d model viewer`、`live2d automation`、`live2d mesh`、`live2d psd`、`psd to live2d`、`live2d motion`、`rig spec`、`Bunraku`；
  - *新鲜度*：`live2d` / `moc3` / `cubism` / `live2d viewer` / `live2d pet` / `live2d ai` 六式各叠加 `pushed:>2026-09-15` 并按 updated 排序（每式 60 条）。
  - **官方组织整表扫描（补做，由 gp-2 的交叉核对反馈触发）**：`gh api orgs/Live2D/repos?per_page=100&sort=updated` 拉出官方组织**全部 20 个仓库**整表去重，发现此前各辑只零散收了 4 条，补收 Samples 系列与 MotionSync 三件套（见 §三 19–24）。另加 `nizima` / `nizima action` / `live2d nizima` / `cubism editor plugin` / `live2d video export` 五式查询。
  - 合计扫描约 **235 个不重复仓库**，对通过去重的候选**逐条 `gh api repos/<r>` 实取** stars / license / language / created_at / pushed_at / updated_at / forks / size（本文件每个数字均来自此，无一项凭记忆）。
- **README 实读**：对 12 个关键仓库额外 `gh api repos/<r>/readme` 取正文（AS_Live2d-reader、LpkUnpacker、HoloDori、ParaRig、CubismMetal、glitch-2d、cpu-only-ai-tuber、HiyoriAI、meidochan、companion-hub、Mana、ChatWaifu-NEXT、naixi-desktop、deepseek-desktop-pet），用于取版本号、性能倍数、文件数等具体数字。
- **Gitee**：WebSearch「Gitee Live2D 开源 2026 moc3 绑定 工具」→ 命中 5 条，**全部为已收录仓库的镜像/教程**（`live2d-py`→Arkueid/EasyLive2D、`gd_cubism`→MizunagiKB、`live2d-moc3`→Cubism 官方 Samples 的教学拷贝、`live2d-widget-v3`→letere-gzj），**本轮 Gitee 无原生新仓**。
- **HuggingFace**：WebSearch「HuggingFace Live2D dataset/avatar rigging」→ 命中的仍以 GitHub 镜像与 r38 已登记的 `Muapi/flux-live2d-...`（付费 API LoRA）为主；**本轮 HF 无原生新资产**。
- **官方手册站点（越界探测，非 gh）**：受 gp-2「官方手册从来没整表列过」的提示，用 `curl` 实拉 docs.live2d.com 的 WordPress sitemap，把官方手册整表结构量化成 3 套站点 / 526+43+59 条，并给出"根路径除 sitemap 外无入口"这个坑（详见 §六-K）。数据来自 HTTP 状态码实测，**非 `gh api`**。
- **限流**：`gh api` 全程**未撞 429**（已登录 re0211，额度充足）。

## 二、本路一句话主线

**本辑 gh 路的主线是「Live2D 制作的重心，从『能不能跑起来』转向『能测、能导出、能合规』」**：十二轮以来第一次出现**带完整实测数据、且结论全部反直觉**的本地栈（`cpu-only-ai-tuber`，无 GPU 的 Ultra 7 155H 上跑通整条主播链路，证明 LLM 只占一轮耗时 2.7%、压量化不提速、破人设的解法在对话历史而不在 system prompt）；第一次出现**可落地的导出件**（`AS_Live2D-reader` 把 Cubism 动作导出成 MP4/透明 WebP/PNG 序列）与**纯解析工具的补全**（`LpkUnpacker` ★296 补上"不做渲染"的容器解析这一格）；而**绑定自动化仍未出现第二例**（See-Through→psd2live 这条线上已卡 6 条同源仓），唯一的**新形态是跨路线的同类思路**（`ParaRig` 把"配置列表 → 一键生成控件+Driver"的绑定抽象落到 Blender）。

支撑这条主线的六个观察：

1. **"有尺子"的项目开始变多**：`cpu-only-ai-tuber` 给出 391 ms TTFT / 2.7% 占比 / 8 条每分钟 / 35.3→28.3 GB/s / 破人设 3/15→0/15；`naixi-desktop` 给出 7.9 万行 / 222 REST 端点 / 29 张 SQLite 表 / 633 提交；`HoloDori` 标 121 项测试通过；`glitch-2d` 把"手离开袖口 ≤4 px"写成第七条逐帧断言。**本轮最有价值的不是新工具，是可测量性本身。**
2. **导出/解析侧从空白到有件**：查看器已连续三轮涌现，但**"看完还能导出"**此前一直是缺口——`AS_Live2D-reader` 是本轮唯一填上的（且是 Windows + Python，正中基准）。
3. **绑定自动化：方向拥挤、形态未变**：`jpg-to-live2d-workflow` / `live2d-auto-pipeline`×2 / `seethrough-live2d-pipeline` / `image-to-live2d` / `rig-c/core`+`rig-c/parts` 全在索引里，本轮**第七例没有出现**。
4. **合规/隐私工程明显升级**：`Mana` 三层许可切分（代码 Apache-2.0 / 美术 LICENSE-ARTWORK / Cubism Core 安装时拉取）、`companion-hub` 四层隐私分级 L0–L3 + MCP 白名单只读边界、`ChatWaifu-NEXT` 独立 `LICENSES.md` 划资产边界——都是可直接抄进自己项目的模板。
5. **桌宠去 Electron 化**：本轮同时出现三条原生路线——C × SDL3（`BongoCat-X`）、C++（`l2dpet`）、Rust + Win32 + D3D11 + DirectComposition（`VeiQiuLab/DesktopPet`）。
6. **反面：AI 桌宠同质化海未退潮**。本轮扫描到的"本地 LLM + Live2D 桌宠"约 40 个，最终只选了 13 个有明确区分度的（纯 CPU / Ollama 必需 / MCP / LangGraph / 双格式宿主 / 隐私分级 / 三层许可），其余进 §五 或 §六-H。
7. **补做（受 gp-2 反馈触发）暴露出一个方法论漏洞**：把 `Live2D` 官方组织整表拉出来后才发现，此前十二辑**从来没整表扫过官方组织**，都是"搜索顺带命中一条收一条"——结果 `CubismSpecs`（唯一权威格式规格）和 `CubismWebFramework` 收了，而 ★393 / forks 121 的 **CubismWebSamples**、★239 的 **CubismNativeSamples** 和 **MotionSync 三件套**却漏了。同时澄清了 **nizima ACTION 是纯闭源在线服务、gh 路无仓库可收**（命中的 12 条全是另一个产品 nizima LIVE）。


---

## 三、工具 / 格式 / 渲染（建模·绑定·moc3·查看器·引擎插件）

### 1. OliverIsNotAvailble/AS_Live2D-reader（★0 · 无许可证文件 · Python · 建仓 2026-10-11 · pushed 2026-10-11）
**Windows 专用 Live2D Cubism 查看器 + 动作导出器**（AS Live2D Reader），初版 **v0.1.0**。
- 关键机制/数字：Python + PySide6 + **原生 live2d-py v3** + FFmpeg；预览走**原生 OpenGL 直绘**（要求 GPU **OpenGL 3.3+**），导出时才从 GPU 读回像素；支持 `.model3.json` 载入与同窗口安全换模型；可检视 motion group / expression / parameter / 引用文件（缺失依赖高亮）；**导出 MP4、动图 WebP、PNG 序列、MP4+WebP 四档**，透明或纯色/图片背景，导出分辨率与预览分辨率解耦；FFmpeg 跑独立编码线程，输出走 `.part.mp4` 原子重命名，取消导出不破坏上一次结果。
- 要求：Windows 10/11，**Python 3.10 或 3.11（64 位）**；不打包 Cubism 运行时，需自装 live2d-py。
- 可复用性：**① 落地**。四项同时命中本机基准——Windows、Python、本地跑、有导出（不是只渲染）；「把动作导出成透明 WebP」这一条对做索引站的动图素材是现成能力。⚠️ 无 LICENSE 文件、★0、作者自述「未做真实模型交互验证」，属"待验证但结构完整"。
- 证据：`gh api repos/OliverIsNotAvailble/AS_Live2D-reader` → ★0 / license=none / Python / created 2026-10-11 / pushed 2026-10-11 / size 74 KB（取数 2026-10-12）；README 实读 v0.1.0 与模块清单（`as_live2d/model.py`·`viewer.py`·`encoder.py`·`window.py`）。
- URL：https://github.com/OliverIsNotAvailble/AS_Live2D-reader

### 2. ihopenot/LpkUnpacker（★296 · 无许可证文件 · Python · pushed 2026-04-07 · updated 2026-10-10 · forks 46）
**Live2DViewerEx `.lpk` 打包格式解包器**——**本轮命中的「不做渲染」的纯解析工具第一例**（容器/格式解析方向，继 `Ludentes/py-moc3` 的二进制 moc3 读写之后的另一条支线）。
- 关键机制/数字：解包 Live2DViewerEx 的 LPK；**增加了 STD_1_0 及更早格式的支持**；README 自述「少部分早期 lpk 仍无法解包，推测存在未知的密钥生成或解密算法」——这是很具体的格式边界陈述。两种用法：`LpkUnpackerGUI.exe`（Releases 直接下）+ 源码 `LpkUnpacker.py <args>`；GUI 内还支持 **Steam 创意工坊文件批量查找/批量解包**，以及**软件渲染 + 网页渲染两种模型预览**。
- 可复用性：**① 落地**。★296、forks 46、Python、有编译好的 Windows EXE，是这批里最"能直接装上用"的解析工具；对"手上有一堆 lpk 想还原成 moc3/贴图"是唯一解。⚠️ 无 LICENSE 文件，且版权上要明确只处理自己有权的模型。
- 证据：`gh api repos/ihopenot/LpkUnpacker` → ★296 / license=none / Python / created 2022-03-29 / pushed 2026-04-07 / updated 2026-10-10 / forks 46 / open_issues 8（取数 2026-10-12）；README 实读。
- URL：https://github.com/ihopenot/LpkUnpacker

### 3. Arkueid/lpk2moc3（★18 · 无许可证文件 · Python · 建仓 2023-02-14 · pushed 2023-08-09 · forks 4）
**带 GUI 的 lpk → moc3 提取器**（"Extract moc3 live2d model from .lpk file with GUI"）——与 §三.2 同方向的**第二例**，但更聚焦"只取 moc3"。
- 可复用性：**② 参考**。与 LpkUnpacker 构成对照样本（通用解包 vs 定向提取 moc3）；⚠️ **最后推送 2023-08（约 3 年未动）**、无 LICENSE，属存档价值大于使用价值。
- 证据：`gh api repos/Arkueid/lpk2moc3` → ★18 / license=none / Python / pushed 2023-08-09 / updated 2026-04-13 / forks 4 / size 40.5 MB（取数 2026-10-12）。
- URL：https://github.com/Arkueid/lpk2moc3

### 4. yazelin/glitch-2d（★0 · MIT · JavaScript · 建仓 2026-09-05 · pushed 2026-09-24 · 仓库 114 MB）
**「格莉奇 2D」——一套**不依赖 Live2D/Cubism/Pixi 运行时**的原生 JS 2D 角色骨架**（README 首句："重新生成的角色部件由原生 JavaScript 组合，使用 WebGL 绘制、Web Audio 带动嘴型，没有 Live2D、Cubism 或 Pixi 的执行期依赖"），站点里还保留了**此前的 Live2D 版本**（`/legacy/`）作对照。
- 关键机制/数字（README 里的工程细节相当硬，是稀有的一手绑定经验）：① 2D 图翻不出掌心，**与 Live2D 同思路走"差分切部件"**：`hand-side`（侧手掌）与 `hand-open`（正面掌心）同挂 `leftHand` slot，`armFold > 0.55` 硬切，任一时刻只有一只手存在；② 手部件必须**共用袖子的校正矩阵**，否则差一个固定量；③ 掌心素材**预旋转 128.34°**（=`bend.elbow`+`bend.shoulder`）；④ 尺寸要烤进部件的 `rect`（形变前），不能放 `adjustment`（形变后）——放错位置导致"挥手中途手离开袖口最远 102 px"，且**七条 check-wave 全绿也没抓到**；⑤ 事后补第七条逐帧检查：比对袖子腕关节与当前手腕点，**超 4 px 即失败**，修复后全程 0.0；⑥ 现版本 v0.5.0，波浪动画改为 `deformPoint` 里两段骨蒙皮（肩/肘/腕 joints），`armRaise`×`bend.shoulder`、`armFold`×`bend.elbow`。
- 可复用性：**② 参考**（对"Live2D 制作"这一主题是**替代路线的一手方法论**）。MIT、文档写到了"检查项怎么加"的层级，对自建 2D 骨架或写自动校验极有参考价值；⚠️ ★0、单人项目、作者是繁体中文母语，素材不通用。
- 证据：`gh api repos/yazelin/glitch-2d` → ★0 / MIT / JavaScript / created 2026-09-05 / pushed 2026-09-24 / size 113.7 MB / homepage https://yazelin.github.io/glitch-2d/（取数 2026-10-12）；README 实读（含 0.5.0 变更与"走错的三次"复盘）。
- URL：https://github.com/yazelin/glitch-2d · https://yazelin.github.io/glitch-2d/?v=0.4.8&view=full

### 5. Zosuya/ParaRig（★0 · GPL-3.0 · Python(Blender 插件) · 建仓 2026-07-31 · pushed 2026-09-16）
**Blender 插件：把"绑定"做成可复用配置面板** —— 在 3D Viewport 里自动生成可拖拽滑块面板，滑块位置通过 Driver 映射到 **Shape Key / 自定义属性 / 骨骼位置**，README 明写对标 "Live2D Cubism-style" 的参数驱动思路。
- 关键机制/数字：**四种控件样式**（纵向滑块 / 横向滑块 / 双轴拖拽板 / 文本标签）；**非破坏性更新**（Update 原地改，手动调过的位置尺寸不被重置）；**分组 Group** 共享同一 Frame、整组可跟随骨骼或物体；棋盘格布局只管"谁挨着谁"，不用算间距；从 Releases 下 zip → Edit > Preferences > Add-ons > Install from Disk → N 面板 ParaRig 标签页。
- 可复用性：**② 参考**。这是本轮**唯一真正把「绑定」做成可复用流水线/工具形态**的新仓库（虽然落点在 Blender 而非 Cubism），"配置列表 → 一键生成控件+Frame+Driver"的抽象可平移到 2D 参数面板；⚠️ ★0、GPL-3.0、且对不做 Blender 的人无直接用。
- 证据：`gh api repos/Zosuya/ParaRig` → ★0 / GPL-3.0 / Python / created 2026-07-31 / pushed 2026-09-16 / size 4.4 MB（取数 2026-10-12）；README（中英双版）实读。
- URL：https://github.com/Zosuya/ParaRig

### 6. rayriffy/CubismMetal（★0 · 无许可证文件 · Swift · 建仓 2026-08-29 · pushed 2026-09-16）
**macOS 原生 Metal 高性能 Live2D Cubism 查看器**。
- 关键机制/数字：直接开 `.model3.json` 清单或 `.moc3`（需同级清单）；支持 Launch picker / Finder 打开 / Cmd-O；播放具名 `.motion3.json`（**默认循环**）；绘制 normal / additive / multiplicative 三类图层并渲染 Cubism **裁剪遮罩**；**默认 60 FPS，显示器与模型扛得住时可跑 120 FPS**；可平移/缩放/复位与显示实测 FPS 叠层。构建链：Xcode 27+ → `scripts/build-app.sh` → `scripts/build-dmg.sh`，`project.yml`（XcodeGen）为唯一事实源，CI 产出 ad-hoc 签名的 `CubismMetal.dmg`（**未 Developer ID 签名、未公证**）。
- 可复用性：**③ 不采用（对本机基准）**。质量很高且是"纯 Metal 渲染管线"的稀缺样本，但**是 macOS 专属**、需 Xcode 27，与 16GB Windows 基准不搭；仅登记思路（"60/120 FPS 双档 + 三类图层 + mask"可作为自己写渲染器的验收清单）。
- 证据：`gh api repos/rayriffy/CubismMetal` → ★0 / license=none / Swift / created 2026-08-29 / pushed 2026-09-16 / size 2.9 MB（取数 2026-10-12）；README 实读。
- URL：https://github.com/rayriffy/CubismMetal

### 7. loliRuriruri/HoloDori（★0 · 无许可证文件 · Rust · 建仓 2026-10-01 · pushed 2026-10-01）
**HoloDori Live2D Manager (HDM)** —— 面向 Steam 游戏 *hololive Dreams* 的**端到端本地导入/构建/预览管理器**，v1.0.0。
- 关键机制/数字：技术栈 **Rust + Tauri 2 + React + TypeScript + WebGL**；流水线为 Steam 自动探测 → **AES-128-CBC 加密资产目录 `octocacheevai` 解密** → 目录浏览（角色/服装/动作/表情）→ **严格体积 + MD5 校验**拉取并本地缓存 → 解 UnityFS 取纯 `.moc3` + Texture2D 图集 + 动画片段 → **构建 `.model3.json` 标准 Cubism 包** → 内嵌 WebGL 预览 / 桌面角色窗口 / **真 Windows 壁纸模式（挂进桌面窗口层级，位于图标之后）**。README 标 **121 项测试通过**，有 CI。明确不打包游戏资产与 Cubism Core。
- 可复用性：**② 参考**。把"解包 → 校验 → 重新打包成标准 model3.json"做成有测试的产品化管线，是**资产管线工程化的稀缺样本**（121 tests 是硬指标）；⚠️ ★0、无 LICENSE、绑死单一游戏（版权灰色，只可用于自有副本）。
- 证据：`gh api repos/loliRuriruri/HoloDori` → ★0 / license=none / Rust / created 2026-10-01 / pushed 2026-10-01 / size 2.8 MB（取数 2026-10-12）；README 实读（含 v1.0.0 badge、Tauri v2、121 passing）。
- URL：https://github.com/loliRuriruri/HoloDori

### 8. haneoka-gakuen/bangdream-live2d-viewer（★1 · MIT · JavaScript · 建仓 2025-05-10 · pushed 2026-10-04 · open_issues 5）
**BanG Dream! Live2D 查看器**，有正式主页 **https://live2d.haneoka.org**。
- 可复用性：**② 参考**。MIT + 已部署站点 + 2026-10 仍在推，是"游戏 Live2D 资源浏览器"里可直接克隆改造的样本；⚠️ ★1、涉及游戏资产版权。
- 证据：`gh api repos/haneoka-gakuen/bangdream-live2d-viewer` → ★1 / MIT / JavaScript / pushed 2026-10-04 / homepage https://live2d.haneoka.org / open_issues 5（取数 2026-10-12）。注：同 owner 另有 `vega`（视觉小说引擎 + `vega-plugin-cubism` / `vega-plugin-composite` / `altair-plugin-models` 一套 Live2D 插件），但 `haneoka-gakuen/vega` 在 index/csdn 基线已命中，本轮剔除（见 §六）。
- URL：https://github.com/haneoka-gakuen/bangdream-live2d-viewer · https://live2d.haneoka.org

### 9. TianMengLucky/BongoCat-X（★10 · AGPL-3.0 · C · 建仓 2026-09-19 · pushed 2026-10-11 · forks 1）
**BongoCat 的 X 分支 fork**：**C × SDL3 × OpenGL** 跨平台桌面宠物（fork 自 `vladelaina/BongoCat`）。
- 可复用性：**② 参考**。"用 C + SDL3 写桌宠"这条非 Electron/非 Web 的轻量路线稀缺（内存占用远低于 Electron 系），AGPL-3.0；⚠️ ★10、是 fork，且 BongoCat 本体已相当知名（撞车风险高，见 §六）。
- 证据：`gh api repos/TianMengLucky/BongoCat-X` → ★10 / AGPL-3.0 / C / created 2026-09-19 / pushed 2026-10-11 / forks 1 / size 13.2 MB（取数 2026-10-12）。
- URL：https://github.com/TianMengLucky/BongoCat-X

### 10. kinaito/myoc（★0 · 无许可证文件 · 语言未标注 · 建仓 2026-07-06 · pushed 2026-10-11 · 仓库 650 KB）
**MyOC —— 通用 Live2D 模型"捏脸"应用**：**不依赖 VTube Studio（VTS）即可独立完成** Live2D 角色的形象、表情创作与管理。
- 关键机制：把"换表情/捏脸"从 VTS 里剥离出来做独立应用——对应的是 Live2D 生态里长期"只能靠 VTS 或 Cubism Editor 收费版才能调"的空白。
- 可复用性：**② 参考**。切口稀缺（去 VTS 依赖的独立捏脸器），2026-10 仍活跃；⚠️ ★0、无 LICENSE、无语言标注、仓库仅 650 KB（很早期），先登记观察。
- 证据：`gh api repos/kinaito/myoc` → ★0 / license=none / language=null / created 2026-07-06 / pushed 2026-10-11 / size 650 KB（取数 2026-10-12）。
- URL：https://github.com/kinaito/myoc

### 11. receyuki/live2pet（★0 · Apache-2.0 · JavaScript · 建仓 2026-08-30 · pushed 2026-10-11）
**live2pet —— 把 Live2D / Spine 模型变成桌宠**（"Turn Live2D and Spine models into desktop pets for Clawd on Desk and Codex. Preview, customize, and build locally."）。
- 关键机制：**双格式（Live2D + Spine）统一转桌宠**，且面向的是两个具体的 Agent 宿主（Clawd on Desk、Codex）——即"桌宠作为 Agent 前端"的适配层；本地预览 + 定制 + 构建。
- 可复用性：**② 参考**。Apache-2.0 友好，"模型 → 桌宠"的通用转换层思路可直接借鉴到"给自家 Agent 挂形象"；⚠️ ★0、未验证构建产物。
- 证据：`gh api repos/receyuki/live2pet` → ★0 / Apache-2.0 / JavaScript / created 2026-08-30 / pushed 2026-10-11 / size 6.7 MB（取数 2026-10-12）。
- URL：https://github.com/receyuki/live2pet

### 12. sakura-builder1/luci-app-live2d（★0 · 无许可证文件 · JavaScript · 建仓 2026-09-30 · pushed 2026-10-10 · forks 1）
**OpenWrt LuCI 看板娘插件**：樱花主题 + **AI 对话 + 路由器管理**——把 Live2D 看板娘挂进路由器管理后台。
- 可复用性：**② 参考**。平台切口极其罕见（路由器 Web 后台跑 Live2D + AI 对话），对"任何 Web 面板都能挂"的思路是个极端证明；⚠️ ★0、无 LICENSE、10 天新仓。
- 证据：`gh api repos/sakura-builder1/luci-app-live2d` → ★0 / license=none / JavaScript / created 2026-09-30 / pushed 2026-10-10 / forks 1 / size 5.6 MB（取数 2026-10-12）。
- URL：https://github.com/sakura-builder1/luci-app-live2d

### 13. jinsc123654/l2dpet（★0 · NOASSERTION · C++ · 建仓 2026-10-10 · pushed 2026-10-11 · 仓库 21.4 MB）
**跨平台 Live2D 桌宠**（Windows / Linux / macOS），C++ 实现，含交互动作，可选 LLM 对话 + 记忆 + 人格（"optional LLM chat, memory, and personality"）。
- 可复用性：**② 参考**。**C++ 原生**而非 Electron/Python，在"桌宠内存占用"这条线上是与 TianMengLucky/BongoCat-X 并列的两个轻量样本；⚠️ ★0、NOASSERTION 许可证、两天新仓。
- 证据：`gh api repos/jinsc123654/l2dpet` → ★0 / NOASSERTION / C++ / created 2026-10-10 / pushed 2026-10-11 / size 21.4 MB（取数 2026-10-12）。
- URL：https://github.com/jinsc123654/l2dpet

### 14. HELPMEEADICE/BANDORI-PET-Android（★6 · GPL-3.0 · Kotlin · 建仓 2026-07-08 · pushed 2026-10-06 · forks 2）
**BandoriPet 安卓版**：BanG Dream! 角色的 Android 桌面宠物 / **动态壁纸**应用。
- 关键机制/数字：技术栈 **Kotlin Compose + OpenGL ES + LuaJIT + Live2D Lua 运行时**（与桌面版 BANDORI-PET-REV 同源的 LuaJIT 路线）；支持模型切换、触摸互动、**帧率调节**、动态壁纸模式。
- 可复用性：**② 参考**。给"LuaJIT + Lua Live2D 运行时"这条线补了移动端证据（桌面版 `HELPMEEADICE/BANDORI-PET-REV` ★465 已由 r38 收进索引）；⚠️ GPL-3.0、★6、依赖官方 Cubism SDK。
- 证据：`gh api repos/HELPMEEADICE/BANDORI-PET-Android` → ★6 / GPL-3.0 / Kotlin / created 2026-07-08 / pushed 2026-10-06 / forks 2（取数 2026-10-12）。
- URL：https://github.com/HELPMEEADICE/BANDORI-PET-Android

### 15. kiraio-moe/Revolt2D.Motion3 + Revolt2D.MotionSync3（各 ★0 · 无许可证文件 · C# · 建仓 2024-10-12 / 10-13 · 仓库 5 KB / 7 KB）
**两个"只做序列化、不做渲染"的托管格式读写库**：`.motion3.json` 与 `.motionsync3.json` 的 **(De)Serializer**（C# / .NET）。
- 关键机制：与 `Ludentes/py-moc3`（moc3 二进制读写）、`ihopenot/LpkUnpacker`（lpk 容器解包）构成**三个不同层次的"纯格式工具"**——前者管几何、中者管容器、这里管动作/口型同步配置。
- 可复用性：**② 参考**。★0、无 LICENSE、2024 年建仓即停（各仅一次推送）、仓库 5–7 KB（极小）。价值在"格式清单"而非"可用实现"：提醒 `.motionsync3.json`（Cubism 4 的口型同步设置）是独立于 `.motion3.json` 的一类文件，做工具链时容易漏。
- 证据：`gh api repos/kiraio-moe/Revolt2D.Motion3` → ★0 / license=none / C# / created 2024-10-12 / pushed 2024-10-12 / size 5 KB；`gh api repos/kiraio-moe/Revolt2D.MotionSync3` → ★0 / license=none / C# / created 2024-10-13 / pushed 2024-10-13 / size 7 KB（取数 2026-10-12）。
- URL：https://github.com/kiraio-moe/Revolt2D.Motion3 · https://github.com/kiraio-moe/Revolt2D.MotionSync3

### 16. Laughting455/live2d_toolkit-v2（★0 · 无许可证文件 · 语言未标注 · 建仓 2026-05-16 · pushed 2026-05-16 · size 0）
**AI Web 应用：把一张 PNG 角色插画精确拆成 Live2D 可直接打开的 PSD**，用于简化 Live2D 开发流程（"precisely splits a PNG character illustration into a PSD file that can be directly opened by Live2D"）。
- 可复用性：**③ 不采用（暂）**。切口正确（PNG → 分层 PSD 是 psd2live 上游那一环），但 **size 0（空仓库）、建仓即停、无 LICENSE、无语言**——只有一句描述，无代码可查。登记为"方向存在、实现未落"。
- 证据：`gh api repos/Laughting455/live2d_toolkit-v2` → ★0 / license=none / language=null / created 2026-05-16 / pushed 2026-05-16 / size 0（取数 2026-10-12）。**注：本轮 API 命中成功，非空仓判断来自 `size=0` 与单次推送，非 404。**
- URL：https://github.com/Laughting455/live2d_toolkit-v2

### 17. proj-airi/unplugin-live2d-sdk（★2 · MIT · TypeScript · 建仓 2025-03-15 · pushed 2026-08-04 · forks 2）
**帮你在构建工具里装 Live2D SDK 的 unplugin 插件**（"Helper plugin for helping installing Live2D SDK"）。
- 关键机制：把"手动下载 Cubism Core、手动复制到 public/、手动改路径"这串 Live2D Web 开发最烦的初始化步骤，做成 **Vite / Webpack / Rollup / esbuild 通用的 unplugin 插件**。
- 可复用性：**① 落地**。MIT、体积极小（529 KB）、切中的是**每个做 Live2D 网页的人都会踩的第一步坑**；对"在索引站里嵌 Live2D 预览"是最省事的入场件。⚠️ ★2、最后推送 2026-08。
- 证据：`gh api repos/proj-airi/unplugin-live2d-sdk` → ★2 / MIT / TypeScript / created 2025-03-15 / pushed 2026-08-04 / forks 2 / open_issues 1 / size 529 KB（取数 2026-10-12）。
- URL：https://github.com/proj-airi/unplugin-live2d-sdk

### 18. bunraku-live2d/Bunraku-live2d.github.io（★0 · 无许可证文件 · JavaScript · 建仓 2026-07-27 · pushed 2026-08-05 · 仓库 45.5 KB）
**Bunraku 项目的官方展示页仓库**（`bunraku-live2d` 组织下）。与主仓 `SparcAI-Inc/Bunraku`（★37，索引已卡 [1248]，arXiv 2607.27348，首个端到端"单图 → 可编辑 Live2D"系统 + 首个基准 Live2D-Bench）配套。
- 可复用性：**② 参考**。主仓已在索引 [1248]，本仓只作**生态配套登记**（有独立可访问的项目页，可看效果演示）；不单独作为工具收录。
- 证据：`gh api repos/bunraku-live2d/Bunraku-live2d.github.io` → ★0 / license=none / JavaScript / created 2026-07-27 / pushed 2026-08-05 / size 45.5 KB（取数 2026-10-12）；主仓 `SparcAI-Inc/Bunraku` 在 index.html 命中 [1248]，剔除。
- URL：https://github.com/bunraku-live2d/Bunraku-live2d.github.io

> **以下 19–24 为「Live2D 官方组织补漏组」**：接到 general-purpose-2 的交叉核对反馈后，我用 `gh api orgs/Live2D/repos?per_page=100` **把官方组织 20 个仓库整表拉了一遍**，发现此前各辑只零散收了 `CubismSpecs`[1202] / `CubismWebFramework`[1170] / `CubismUnityComponents`[1171] / `CubismNativeFramework` 四条，**Samples 系列与 MotionSync 三件套从未进索引**。逐条去重后补收如下（全部 `grep` 命中 0）。

### 19. Live2D/CubismWebSamples（★393 · NOASSERTION · 建仓 2018-08-29 · pushed 2026-04-02 · **forks 121** · 仓库 31.7 MB）
**官方 Web 端 Cubism 样例工程**（与已卡的 `Live2D/CubismWebFramework`[1170] 配套）。
- 可复用性：**① 落地**。★393 + **121 个 fork** 是官方组织里被抄得最多的仓库——它是"在网页里正确载入 moc3、接 WebGL/着色器、组织 resources 目录"的**权威实现模板**；对"在索引站里嵌 Live2D 预览"是比任何第三方封装都可靠的起点。⚠️ NOASSERTION（官方 SDK 自有条款）、无 description。
- 证据：`gh api repos/Live2D/CubismWebSamples` → ★393 / NOASSERTION / language=null / created 2018-08-29 / pushed 2026-04-02 / updated 2026-10-11 / forks 121 / open_issues 0 / size 31.7 MB（取数 2026-10-12）。
- URL：https://github.com/Live2D/CubismWebSamples

### 20. Live2D/CubismNativeSamples（★239 · NOASSERTION · 建仓 2018-04-25 · pushed 2026-04-02 · forks 44 · 仓库 36 MB）
**官方 Native（C++）Cubism 样例工程**。README 口径：**「Cubism 5 SDK for Native R2 发布后，将终止 Cocos2d-x 支持」**。
- 可复用性：**② 参考**。Native 路线上唯一官方完整样例；"终止 Cocos2d-x"这条官方口径对判断哪些老教程已过期有用（**注意：这是官方 README 自述，非本轮独立核实，需与 gp-3 的官方页取数对齐**）。⚠️ NOASSERTION。
- 证据：`gh api repos/Live2D/CubismNativeSamples` → ★239 / NOASSERTION / created 2018-04-25 / pushed 2026-04-02 / forks 44 / open_issues 1 / size 36 MB（取数 2026-10-12）。
- URL：https://github.com/Live2D/CubismNativeSamples

### 21. Live2D/CubismViewer（★46 · 无许可证文件 · C# · 建仓 2017-07-21 · **pushed 2018-04-20** · 仓库 11 KB）
**官方 Cubism Viewer —— 已明确停止维护**（description 原文：`[CAUTION] This repository is not actively maintained.`）。
- 可复用性：**③ 不采用**。★46 但**停更 8 年、仓库仅 11 KB**（疑似历史存档/重定向），无使用价值。收录理由只有一个：它是**"官方查看器已死，所以第三方查看器才会连续三轮涌现"这条主线的直接证据**，写卡时可作为对照。
- 证据：`gh api repos/Live2D/CubismViewer` → ★46 / license=none / C# / created 2017-07-21 / pushed 2018-04-20 / updated 2026-10-02 / forks 7 / size 11 KB（取数 2026-10-12）。
- URL：https://github.com/Live2D/CubismViewer

### 22. Live2D MotionSync 三件套（Cubism 5 的口型同步官方组件）
- `Live2D/CubismUnityMotionSyncComponents`（★3 · NOASSERTION · C# · 建仓 2023-08-10 · **pushed 2026-08-25** · 25.6 MB · forks 2）
- `Live2D/CubismNativeMotionSyncComponents`（★5 · NOASSERTION · C++ · 建仓 2023-10-16 · **pushed 2026-08-25** · 8.9 MB · forks 2）
- `Live2D/CubismWebMotionSyncComponents`（★11 · NOASSERTION · TypeScript · 建仓 2023-11-30 · pushed 2025-03-27 · 8.8 MB · forks 2）
- 关键机制：**MotionSync 是 Cubism 5 起的独立能力**——不靠手 K 口型关键帧，而是**直接从音频波形生成口型参数**，所以它单独占三个仓库（Unity / Native / Web），与主干 SDK 平行发布。Unity 与 Native 两仓 **同日推送 2026-08-25**。
- 可复用性：**② 参考**。★数极低（3/5/11）但**是官方的、且 2026-08 仍在推**——说明"音频驱动口型"这条口型同步的正路在官方侧是 2026 年才补齐的；此前所有第三方桌宠的口型都是手 K 或粗暴音量映射。⚠️ NOASSERTION、无 description、需配合 Cubism 5 SDK。
- 证据：三条均 `gh api repos/<r>` 实取（取数 2026-10-12）。
- **cn 路交叉印证（general-purpose-2 提供，2026-10-12）**：本条的"官方 2026 年才补齐"不是推测，已有反证实例——cn 路本轮收的虎课网古风立绘建模课，教的说话口型是**「在每一帧上详细调整」的纯手 K**，软件版本 **Cubism 4.0.02**。gp-2 据此给出了可直接复用的判据：**凡 2026 年之前的中文「口型同步」教程基本都是手 K 或粗暴音量映射（TTS → RMS → `ParamMouthOpenY`），下轮遇到不必当新方案收**。r38 收的那条 CSDN React 帖（TTS→RMS→口型）正是这一时代的产物，现在有了官方对照物，可直接标时代。
- URL：https://github.com/Live2D/CubismUnityMotionSyncComponents · https://github.com/Live2D/CubismNativeMotionSyncComponents · https://github.com/Live2D/CubismWebMotionSyncComponents

### 23. nizima LIVE 官方 API 组（回应 gp-2 关于 nizima 的提问）
- `Live2D/nizimaLIVEPluginAPI`（★6 · 无许可证 · 建仓 2024-01-09 · pushed 2026-03-31 · forks 2 · **size 17 KB**）
- `Live2D/nizimaLIVEScriptAPI`（★4 · 无许可证 · 建仓 2024-01-30 · pushed 2025-06-09 · forks 3 · size 464 KB）
- `Live2D-Garage/nizimaLIVESampleScript`（★0 · MIT · JavaScript · 建仓 2024-01-30 · pushed 2024-11-22 · forks 1 · size 52 KB）
- **关键区分（务必别混）**：gp-2 提到的 **nizima ACTION**（在线视频编辑器，`docs.live2d.com/nizimaaction/...`）与这里的 **nizima LIVE**（桌面直播/表演应用）**是两个不同产品**。本轮 `gh search repos "nizima action"` / `gh search repos "live2d nizima"` **均返回 0 条**，说明 **nizima ACTION 没有对应的开源仓库/导出脚本，是纯闭源在线服务**——gh 路在这条线上**确实没有漏网，漏的是产品形态本身**。
- 可复用性：**② 参考**。nizima LIVE 的插件 API 与脚本 API 是官方开放的**可编程入口**（第三方可用它给角色接语音/字幕/表情），`Live2D-Garage` 那份样例脚本是 MIT，可当模板。⚠️ 两个官方仓均**无 LICENSE 文件**、无 description、仓库极小（17 KB / 464 KB，应为文档+类型定义而非运行时）。
- 证据：三条均 `gh api repos/<r>` 实取（取数 2026-10-12）；`gh search repos "nizima action"` 返回空集。
- URL：https://github.com/Live2D/nizimaLIVEPluginAPI · https://github.com/Live2D/nizimaLIVEScriptAPI · https://github.com/Live2D-Garage/nizimaLIVESampleScript

### 24. jellydreams/pyNizima（★0 · MIT · Python · 建仓 2024-12-09 · pushed 2024-12-11 · PyPI 包 `pynizima`）
**通过 WebSocket 操作 NizimaLIVE API 的 Python 库**（"Python library for interacting with the NizimaLIVE API via WebSocket"），**已发布到 PyPI**（https://pypi.org/project/pynizima/）。
- 可复用性：**② 参考**。**本轮唯一一个"用 Python 脚本控制商业 Live2D 表演软件"的库**——对"本地 Ollama 出文本 → 驱动 nizima LIVE 里的角色"这条链路是现成的桥；MIT、有 PyPI 包（可直接 `pip install`）。⚠️ ★0、停更近 2 年、open_issues 1、仓库仅 12 KB。
- 证据：`gh api repos/jellydreams/pyNizima` → ★0 / MIT / Python / created 2024-12-09 / pushed 2024-12-11 / forks 1 / open_issues 1 / size 12 KB / homepage https://pypi.org/project/pynizima/（取数 2026-10-12）。
- URL：https://github.com/jellydreams/pyNizima


---

## 四、AI × Live2D（条名标 [AI]）

### [AI] 1. whymycompilefail/cpu-only-ai-tuber（★0 · MIT · C++ · 建仓 2026-10-11 · pushed 2026-10-11 · size 0）
**纯 CPU 跑通的完整本地 AI 主播栈**——B 站弹幕 / 麦克风 → **Qwen3.5-2B** → **Qwen3-TTS** → Live2D，附**自研 CPU 特化 llama.cpp fork 与全部实测数据**。参考机：**Intel Core Ultra 7 155H，22 线程，无 GPU**。
- 关键机制/数字（README 里三条"最值钱的结论"，全部可复现，且**全部反直觉**）：
  1. **LLM 不是端到端大头**：一轮健康回合 **15～32 秒，绝大部分是 TTS 合成**；LLM 侧 TTFT 优化到 **391 ms** 后只占一轮耗时的 **2.7%**；引擎侧单轮 ~7-8 秒 ⇒ 上限 **约 8 条回复/分钟**，而中型直播间产出 **10～50 条/分钟**。推论：**忙时硬丢弃弹幕而非排队是设计而非缺陷**（否则 AI 永远落后五分钟）。
  2. **不是带宽受限**：实得带宽随每元素字节数**下降**（Q8_0 的 **35.3 GB/s** → Q5_0 的 **28.3 GB/s**），瓶颈是每元素指令成本，压量化位宽换不来线性提速。
  3. **破人设的病灶是 RLHF 诚实性先验，不是模型太小**：换更大 Instruct 模型大概率**更糟**；去掉 persona 里的 "AI" 字样破人设率**一字未变**；**有效解是把示范写进对话历史而非 system prompt：破人设 3/15 → 0/15**。
  4. 附带踩坑：Qwen3.5 是思考模型，不关 thinking 则回复全进 `reasoning_content`、`content` 为空且**不报任何错**；须用环境变量 `LLAMA_ARG_CHAT_TEMPLATE_KWARGS='{"enable_thinking": false}'`（写成命令行参数会因 shell 吞花括号导致 llama-server 启动即崩）。
- 工程规模：相对上游 llama.cpp `5096f2a` 改了 **15 个文件 / +1121 −173 行**，完整 diff 在 `patches/`；Open-LLM-VTuber（MIT）上加了 ASR 延迟初始化一处魔改；`ctest/` 自研起停栈/弹幕桥接/破人设探针/隐私扫描；`specs/` 记录每次改动为什么，含被否决方案。
- 可复用性：**① 落地**。**这是本轮对本机基准命中度最高的一条**——无 GPU 纯 CPU 正是 16GB Windows 笔记本的常态，三条结论直接改写"该优化什么"的预算分配（别压 tok/s、别压量化、去改 persona 写法）；MIT、有可重放 patch。⚠️ ★0、当天建仓、`size 0`（llama.cpp 用 gitlink，作者自述 `.git` 被改名成 `.git.fork-backup/`，需 `mv` 回来否则 clone 到空目录）。
- 证据：`gh api repos/whymycompilefail/cpu-only-ai-tuber` → ★0 / MIT / C++ / created 2026-10-11 / pushed 2026-10-11（取数 2026-10-12）；README 实读（含 Ultra 7 155H、391 ms、2.7%、8 条/分钟、35.3→28.3 GB/s、3/15→0/15、15 文件 +1121/−173）。
- URL：https://github.com/whymycompilefail/cpu-only-ai-tuber

### [AI] 2. luckui/HiyoriAI（★93 · MIT · TypeScript · 建仓 2026-03-16 · pushed 2026-10-10 · forks 5）
**Hiyori（日和）—— 住在 Windows 桌面、也能从手机找到你的 Live2D AI 助手**。
- 关键机制：Electron + TypeScript + Live2D Cubism；接 **OpenAI 兼容 API**（可指本地 Ollama）；**需要认真写代码时把项目交给 Codex 官方 SDK，再把结果带回来**——"角色形象 × Agent 分工"的清晰切分；提供 Windows 安装包（Releases）。
- ⚠️ **上游改名核对**：README 的下载 badge 指向 `luckui/ai-live2d-go`，`gh api repos/luckui/ai-live2d-go` 返回的是 `luckui/HiyoriAI` 本体——**同一仓库的旧名，不是两个项目**。
- 可复用性：**① 落地**。★93、MIT、有 Windows 发行包、OpenAI 兼容（可接本地 Ollama），是这批里"装了就能用"且协议最干净的；"她把活派给 Codex"这条人机分工设计对做自己的本地 Agent 有直接借鉴。
- 证据：`gh api repos/luckui/HiyoriAI` → ★93 / MIT / TypeScript / created 2026-03-16 / pushed 2026-10-10 / forks 5 / open_issues 0 / size 13.9 MB（取数 2026-10-12）；README 实读（Windows 10/11、Codex Official SDK、OpenAI Compatible、有 B 站演示 BV1f6dWBBEQA）。
- URL：https://github.com/luckui/HiyoriAI

### [AI] 3. Hayliy/naixi-desktop（★0 · Apache-2.0 · Python · 建仓 2026-07-24 · pushed 2026-10-10 · 仓库 89.4 MB · v1.2.0）
**奶昔 · 桌面智能体（Naixi Desktop）**——本地优先的桌面 AI 智能体，把对话/桌宠/直播互动/工作流/自动化/本地搜索/知识库/记忆整合进一个常驻托盘的 Tauri 2 应用。
- 关键机制/数字（README 给的规模数字非常具体，是本批最硬的量化样本）：第一方代码约 **7.9 万行**（Python 43,083 / 前端 35,331 / Rust 571，含注释与空行）· **56** 个 Python 模块 · **37** 个前端组件 · **222** 个 REST 端点 · **29** 张 SQLite 表 · **633** 次提交 · 版本 **v1.2.0** · Apache-2.0。
- 技术栈：Tauri 2（Rust）+ 系统托盘常驻；前端 React 19 + Vite + Tailwind；**后端 Python sidecar（aiohttp，默认 `http://127.0.0.1:9845`）**；**桌宠走 PySide6（Qt）驱动 Live2D / VRM，支持摄像头面捕**；内置 **SearXNG 便携版**做本地搜索（可降级公共引擎）；可视化工作流 DAG **25 种节点**；**13 个平台连接器**（QQ/微信/飞书/企微/钉钉/Discord/Slack/Telegram/WhatsApp/邮件/GitHub/GitLab/自定义 HTTP）；分层记忆（短期上下文 + 长期画像 + 反思提炼）。
- 可复用性：**① 落地**。**Python sidecar + Qt 桌宠 + Live2D/VRM 双格式 + 本地 SearXNG** 这一组合几乎逐条对齐本机基准（Windows、Python、本地优先）；Apache-2.0 可商用可改。⚠️ ★0（知名度假是"星数滞后于工程量"的典型）、89 MB 仓库、Python 3.13 sidecar 需自配。
- 证据：`gh api repos/Hayliy/naixi-desktop` → ★0 / Apache-2.0 / Python / created 2026-07-24 / pushed 2026-10-10 / size 89.4 MB / homepage B 站空间 363346472（取数 2026-10-12）；README 实读（v1.2.0、633 commits、79k LOC、222 端点、29 表、25 节点、13 连接器）。
- URL：https://github.com/Hayliy/naixi-desktop

### [AI] 4. PhyQxx/companion-hub（★2 · 无许可证文件 · Python · 建仓 2026-08-17 · pushed 2026-10-10 · 仓库 17.1 MB）
**Aria · 伴侣中枢**——部署在自有设备上的 AI 伴侣，README 明写"人格与形象解耦，换形象不会丢失记忆和关系"，**Live2D Web 运行时按官方许可在本机安装，不随仓库分发 Cubism Core**（合规表述清晰）。
- 关键机制/数字：**四层隐私分级 L0~L3**（公开 → 原始高敏传感），**L2 敏感内容强制本地模型处理，L3 数据不进入通用持久化或云端**；长期记忆支持多主体（你/她/共同约定）、冲突纠错、删除台账与来源追溯、按时间线回查；语音支持 VAD 自动断句、**人声打断（barge-in）**、PTT、口型同步；**通用 MCP 客户端底座已接入官方 SDK v2**，提供 Streamable HTTP + 白名单工具目录 + 只读调用边界 + Admin 健康页（Context7 外部 Server 有 **2026-09-11** 真实联调记录）；地图/天气走高德真实数据源；多终端感知（电脑 + 浏览器扩展注册为感知终端）+ Home Assistant / MQTT 遥测 + 手机 PWA（**PWA Batch B/C 于 2026-09-11 完成真机验收**）；内置 Admin 面板配置模型路由、语音参数、人格草稿、记忆检索、设备配对。
- 可复用性：**② 参考**。**"四层隐私分级 + 记忆可删除台账 + MCP 白名单只读边界"是这批里最完整的合规/隐私工程样本**，对"本地 Ollama + 敏感数据分级"的索引站主人有直接抄的价值；⚠️ **无 LICENSE 文件**（最大问题）、★2、无 PDF/发行包。
- 证据：`gh api repos/PhyQxx/companion-hub` → ★2 / license=none / Python / created 2026-08-17 / pushed 2026-10-10 / size 17.1 MB（取数 2026-10-12）；README 实读（L0~L3、MCP SDK v2、2026-09-11 联调与真机验收）。
- URL：https://github.com/PhyQxx/companion-hub

### [AI] 5. bbmio/meidochan（★0 · MIT · Python · 建仓 2026-09-25 · pushed 2026-10-11 · v0.1 · 仓库 4.6 MB）
**妹抖酱 v0.1 —— 完全本地运行的 AI Agent 桌面应用**（Python + PySide6）：多工作空间 + 插件系统 + **向量知识库** + Live2D 立绘。
- 关键机制/数字：**接 DeepSeek 云端或本地 Ollama**，支持思考链、流式回复、工具调用；Live2D 立绘随对话状态换表情，能听懂「笑一个」「跳个舞」；**跨会话记住偏好与习惯**；**多工作空间隔离——工作/学习/娱乐各自独立的人设与记忆（"不串味"）**；三套主题（亮色/深色/初音）+ 色轮自定义。依赖：Python ≥ 3.11（用标准库 `tomllib`）、**Ollama（向量检索必需）**；装法明确到命令：`ollama pull bge-m3`（向量/历史检索必需）、`ollama pull qwen3.5:9b`（本地对话模型）。
- 可复用性：**① 落地**。**"Ollama 为必需依赖 + 明确给出 bge-m3 / qwen3.5:9b 两个具体模型"** 是本机基准（16GB + 本地 Ollama）最贴合的一条；"多工作空间记忆隔离"是可直接抄到索引站工作流的设计；MIT。⚠️ ★0、v0.1 早期。
- 证据：`gh api repos/bbmio/meidochan` → ★0 / MIT / Python / created 2026-09-25 / pushed 2026-10-11 / size 4.6 MB（取数 2026-10-12）；README 实读（Python≥3.11 / tomllib / bge-m3 / qwen3.5:9b / 多工作空间）。
- URL：https://github.com/bbmio/meidochan

### [AI] 6. sjmsltx/deepseek-desktop-pet（★13 · MIT · Python · 建仓 2026-08-02 · pushed 2026-10-11 · 仓库 285 MB）
**DeepSeek 桌宠助手**——PySide6 (Qt) + DeepSeek API 的 Windows 桌面 AI 陪伴助手，**有 Windows 免安装便携包**（解压即用，无需 Python 环境，需自备 API Key）。
- 关键机制/数字：**双角色（V4 Flash / V4 Pro）**各有人格、情绪状态与好感度成长；长期记忆 = **BM25 检索 + 自动事实抽取 + LLM 重排**；工具调用含时间/天气/提醒/待办/PowerShell 自动化/联网搜索/**MCP servers**/可安装插件；**主题系统 86 个 design tokens 单一事实源** + 可安装主题插件；插件系统五类（tool / menu / rules / theme / skill）+ 自编辑代码工具（带备份 + 语法闸门）。
- 版本说明（README 特别澄清）：**发布版本号走语义化 `2.x`**（见 CHANGELOG），源码注释里的 `v6.xx` 是**内部开发迭代号**（`v6.19` 为起点）**——两套编号不是同一串**，这个坑很容易被误记。
- 可复用性：**② 参考**。MIT + 免安装便携包 + 双角色好感度 + BM25 记忆，工程完成度在 ★13 这批里偏高；"两套版本号"的澄清对做索引卡很有用（避免把 v6.19 当发行版）。⚠️ 依赖 DeepSeek 云端 API（非本地 Ollama）、285 MB 仓库。
- 证据：`gh api repos/sjmsltx/deepseek-desktop-pet` → ★13 / MIT / Python / created 2026-08-02 / pushed 2026-10-11 / updated 2026-10-01 / size 285 MB（取数 2026-10-12）；README 实读（双角色、BM25+自动抽取+LLM 重排、86 tokens、2.x vs v6.xx 版本说明）。
- URL：https://github.com/sjmsltx/deepseek-desktop-pet

### [AI] 7. Yuuzulight/Mana（★7 · Apache-2.0（代码） · JavaScript · 建仓 2026-05-30 · pushed 2026-10-11 · forks 3 · open_issues 61）
**Mana —— Windows 本地优先 AI 伴侣**：本地语音转写（**whisper.cpp**）+ 本地 LLM（**llama.cpp**）+ 本地 TTS + 屏幕感知 + Live2D 形象。
- 关键机制：栈为 **.NET 10 WinForms（前端）+ Node.js（后端）+ llama.cpp + whisper.cpp**——WinForms 这条线在 2026 年的桌宠里极罕见；隐私主张写得很硬："works offline, doesn't meter you, nothing leaves the machine unless you explicitly turn that on"。
- 许可拆三层（值得单独记）：**代码 Apache-2.0（© 2026 Mashiron Labs）**；**美术资源（sprites/ 与所有 avatar 模型）单独 LICENSE-ARTWORK，保留所有权利，不得复用**；**Cubism Core 不随仓库分发，安装时按其自身条款拉取**。
- 可复用性：**② 参考**。"三层许可切分（代码/美术/Cubism 运行时）"是本批最规范的合规模板，值得抄进自己的项目；⚠️ **61 个 open issues**（远超 ★7 的体量，可能是作者自建任务池而非真 bug）、美术不可复用、WinForms 前端不易二开。
- 证据：`gh api repos/Yuuzulight/Mana` → ★7 / Apache-2.0 / JavaScript / created 2026-05-30 / pushed 2026-10-11 / forks 3 / open_issues 61 / size 109 MB（取数 2026-10-12）；README 实读（.NET 10 WinForms / Node.js / llama.cpp / whisper.cpp / LICENSE-ARTWORK / THIRD_PARTY.md）。
- URL：https://github.com/Yuuzulight/Mana

### [AI] 8. MuBai-He/ChatWaifu-NEXT（★9 · NOASSERTION · Python · 建仓 2026-08-25 · pushed 2026-10-09 · forks 1 · 仓库 42.3 MB）
**ChatWaifu NEXT（ChatWaifuV2）**：本地优先的实时 AI 角色运行时，语音 + Live2D + 记忆 + **Runtime Skills**。
- 关键机制：**Web 与桌宠同一项目维护、各自构建发布，共用同一套对话/记忆/语音能力**（"不必再各做一套"）；可打断；随相处改变语气/表情/动作；人格、声音、模型、Avatar 均可替换；有独立文档站 https://mubai-he.github.io/ChatWaifu-NEXT/ 与 `docs/implementation-status.yaml` 实现状态清单。桌面端目前只产出**未签名安装候选**。
- 血脉：脱胎于 `cjyaddone/ChatWaifu`（早年把聊天模型 + 角色语音 + Live2D 拼在一起的项目）。
- 合规边界写得很清楚：宁宁 Live2D、训练音色、checkpoint、Cubism Core 等 owner-only 资产不随源码分发，见 `LICENSES.md`。
- 可复用性：**② 参考**。"Web + 桌宠共用一套对话/记忆/语音内核、分别构建"的架构是少见的正解（多数项目是两套各写一遍）；有 `implementation-status.yaml` 做实现度自评是稀缺习惯。⚠️ **NOASSERTION + 发行许可证尚未选定**（README 明说），二开分发前必读 LICENSES.md。
- 证据：`gh api repos/MuBai-He/ChatWaifu-NEXT` → ★9 / NOASSERTION / Python / created 2026-08-25 / pushed 2026-10-09 / forks 1 / open_issues 4 / size 42.3 MB（取数 2026-10-12）；README 实读。
- URL：https://github.com/MuBai-He/ChatWaifu-NEXT

### [AI] 9. liyu-1028/mochi（★3 · NOASSERTION · Python · 建仓 2026-08-03 · pushed 2026-10-10 · 仓库 26 MB）
**Mochi —— 会成长的桌面智能伙伴**：**Tauri + Live2D 前端 × LangGraph 认知核心**，"捏出你的专属 AI 伙伴，让智能体拥有温暖的模样"。
- 关键机制：**前端（Tauri + Live2D）与认知核心（LangGraph）显式解耦**——把"智能体编排"交给 LangGraph 而不是自己撸状态机，这在桌宠里是相对少见的选型。
- 可复用性：**② 参考**。"Tauri + Live2D 壳 × LangGraph 内核"是可直接套用的分层模板（形象层与认知层各自替换）；⚠️ NOASSERTION 许可证、★3、open_issues 2。
- 证据：`gh api repos/liyu-1028/mochi` → ★3 / NOASSERTION / Python / created 2026-08-03 / pushed 2026-10-10 / open_issues 2 / size 26 MB（取数 2026-10-12）。
- URL：https://github.com/liyu-1028/mochi

### [AI] 10. throndir2/Martlet（★0 · NOASSERTION · C# · 建仓 2026-09-13 · pushed 2026-10-11 · 仓库 31.7 MB）
**Martlet —— Windows AI 伴侣**：会说话、会听、**会看你的屏幕**，以 **Live2D / VRM 双格式**角色形态常驻桌面。
- 关键机制：**Live2D 与 VRM 同一套宿主**（不是二选一），叠加屏幕感知——对应"桌宠看得见你在干什么"这条线。
- 可复用性：**② 参考**。C#/.NET 路线 + Live2D/VRM 双宿主，对不想碰 Electron 的人有参考价值；⚠️ NOASSERTION、★0、一月新仓。
- 证据：`gh api repos/throndir2/Martlet` → ★0 / NOASSERTION / C# / created 2026-09-13 / pushed 2026-10-11 / open_issues 2 / size 31.7 MB（取数 2026-10-12）。
- URL：https://github.com/throndir2/Martlet

### [AI] 11. VeiQiuLab/DesktopPet（★0 · MIT · Rust · 建仓 2026-08-13 · pushed 2026-09-19 · 仓库 6.7 MB）※桌宠底座本身无 AI 组件
**轻量 Windows Live2D 桌宠**：**Rust + Win32 + D3D11 + DirectComposition**（无 Electron、无 Python、无浏览器内核）。
- 可复用性：**② 参考**。与 §三.13 的 `jinsc123654/l2dpet`（C++）、§三.9 的 `TianMengLucky/BongoCat-X`（C/SDL3）共同构成**本轮"去 Electron 轻量桌宠"三条不同技术路线**的对照样本；MIT 最友好。⚠️ ★0、停更近一月。
- 证据：`gh api repos/VeiQiuLab/DesktopPet` → ★0 / MIT / Rust / created 2026-08-13 / pushed 2026-09-19 / size 6.7 MB（取数 2026-10-12）。注：索引里的 `1704919/WuziDesktopPet`、`ymhyyds/DesktopPet`、`DesktopPetXuansi/Xuansi` 均为**不同仓库**，已逐一核对。
- URL：https://github.com/VeiQiuLab/DesktopPet

### [AI] 12. 12sncaksh/AIssistant（★2 · MIT · Python · 建仓 2026-09-23 · pushed 2026-10-08）
**AIssistant —— Windows 桌面 AI 助手 + Live2D 桌宠**：**PyQt6** + 结构化工具调用的 LLM 对话 + **MCP 支持** + 语音唤醒/输入/输出 + 系统工具。
- 可复用性：**② 参考**。**PyQt6 + MCP** 这一组合与本机基准（Windows + Python）贴合，是把"MCP 工具生态"接进桌宠的最小样本；MIT。⚠️ ★2、半月新仓。
- 证据：`gh api repos/12sncaksh/AIssistant` → ★2 / MIT / Python / created 2026-09-23 / pushed 2026-10-08 / size 3.9 MB（取数 2026-10-12）。
- URL：https://github.com/12sncaksh/AIssistant

### [AI] 13. yanghuagai55/astrbot_plugin_live2d_pet（★12 · MIT · Python · 建仓 2026-01-22 · pushed 2026-09-27 · forks 2）
**AstrBot 的 Live2D 桌宠插件**——把 Live2D 形象做成 AstrBot（开源聊天机器人框架）的插件。
- 可复用性：**② 参考**。**"桌宠作为成熟 bot 框架的插件"而非独立应用**是更省力的接入路径；与下条 `llly712/tianyi-desktop-pet`（同样接 AstrBot）互为印证，说明 AstrBot 生态已形成 Live2D 形象接入的事实标准。MIT、★12（这批里星数偏高的）。
- 证据：`gh api repos/yanghuagai55/astrbot_plugin_live2d_pet` → ★12 / MIT / Python / created 2026-01-22 / pushed 2026-09-27 / forks 2 / open_issues 2 / size 122 KB（取数 2026-10-12）。注：仓库无 description，README 亦未取到，功能描述以仓库名与生态位置为准（**未做深度核实**）。
- URL：https://github.com/yanghuagai55/astrbot_plugin_live2d_pet


---

## 五、边缘登记

一行一条，均已过 `gh api` 取数（取数日 2026-10-12），仅因体量/成熟度/平台不符而不进正文。

- `Momoyeyu/momo`（★0 · NOASSERTION · HTML · 建仓&推送 2026-10-11 · **open_issues 59** · 主页 https://momoyeyu.github.io/momo/）—— 本地优先 AI 桌宠（Live2D + Tauri + 本地推理）。⚠️ 当天建仓却有 **59 个 open issues**（远超 ★0 体量，疑似批量建 issue 或 bot），登记待观察。URL https://github.com/Momoyeyu/momo
- `RifkyA911/mirunova-live`（★0 · 无许可证 · Svelte · 建仓 2026-10-08 · pushed 2026-10-11 · 64 MB）—— Web Live2D & 3D 头像**视觉追踪器**，**100% 客户端侧**、Bun + SvelteKit。URL https://github.com/RifkyA911/mirunova-live
- `NaviVoid/Rive2d`（★0 · MIT · TypeScript · 建仓 2026-02-28 · pushed 2026-09-18 · forks 1）—— **niri 合成器**上的 Live2D 查看器（Linux Wayland 滚动平铺 WM 生态）。URL https://github.com/NaviVoid/Rive2d
- `MorphTheMoth/Stella-Sora-Live2d`（★0 · 无许可证 · JavaScript · pushed 2026-09-29 · 已部署 https://morphthemoth.github.io/Stella-Sora-Live2d/）—— 游戏《Stella Sora》的 l2d 查看器。URL https://github.com/MorphTheMoth/Stella-Sora-Live2d
- `zhzhongshi/MOC3-Explorer`（★2 · 无许可证 · Java · 建仓&推送 2025-01-25 · 38 KB）—— 名字直指 moc3 解析，但**无描述、无 README、仅一次推送**，无法核实功能，只登记名字。URL https://github.com/zhzhongshi/MOC3-Explorer
- `potter-pixel/live2d-motion-animator`（★0 · 无许可证 · TypeScript · 建仓 2026-06-21 · pushed 2026-07-12 · 2.5 MB）—— Live2D 动作动画编辑器。URL https://github.com/potter-pixel/live2d-motion-animator
- `Up-to-code/edwardarwin`（★1 · NOASSERTION · TypeScript · 建仓&推送 2026-10-10 · 27 MB）—— Emma Darwin：macOS 本地 AI 伴侣，F4 语音 + Live2D + SQLite 记忆 + 桌面 MCP 工具，**混合许可源码发布**。URL https://github.com/Up-to-code/edwardarwin
- `llly712/tianyi-desktop-pet`（★3 · MIT · Python · 建仓 2026-08-18 · pushed 2026-09-19 · 614 KB）—— 洛天依桌面 AI 助手：**PMX/Live2D 双渲染** + TTS + 本地 Agent + **AstrBot 接入**（与 §四.13 同生态）。URL https://github.com/llly712/tianyi-desktop-pet
- `stenlysayd/avalon-avatar`（★1 · MIT · TypeScript · 建仓 2025-12-26 · pushed 2026-09-19 · 283 KB · 已部署 https://avalon-avatar.vercel.app）—— **Next.js 16** + Live2D Cubism 3/4 + **Web Audio 口型同步** + 多供应商 TTS 流式 + 结构化 LLM 输出。URL https://github.com/stenlysayd/avalon-avatar
- `juliandavid0610/AI-Chatting-Assistant`（★0 · NOASSERTION · TypeScript · 建仓&推送 2026-09-19 · 8.4 MB）—— 流式 LLM 接 Cubism rig，**句子说到一半表情就换**、嘴型跟真实音频波形。URL https://github.com/juliandavid0610/AI-Chatting-Assistant
- `Chenqiang-Zhang/airi-lite`（★1 · MIT · JavaScript · 建仓 2026-08-09 · pushed 2026-10-10 · 1.1 MB）—— 受 Project AIRI 启发的**自托管 Live2D 伴侣精简原型**。URL https://github.com/Chenqiang-Zhang/airi-lite
- `sorakee/itsumo-desk`（★0 · MIT · TypeScript · 建仓 2026-10-03 · pushed 2026-10-11 · 470 KB）—— 轻量常驻 Live2D 桌伴。URL https://github.com/sorakee/itsumo-desk
- `xiaochengzina/madoka-deskpet`（★0 · NOASSERTION · JavaScript · 建仓 2026-09-16 · pushed 2026-09-20）—— **Driftlet** 桌宠引擎的 Madoka 皮肤（鼠标追踪 + 自动眨眼 + 呼吸 + 点击发光）。URL https://github.com/xiaochengzina/madoka-deskpet
- `ranran486/deskpet-studio`（★1 · MIT · TypeScript · 建仓&推送 2026-10-10 · 38 MB）—— 可扩展 Windows 桌宠：动作模板、情绪互动、自定义台词 + DeepSeek。URL https://github.com/ranran486/deskpet-studio
- `x01n/petforge`（★0 · 无许可证 · Python · 建仓 2026-09-10 · pushed 2026-09-19 · 3.8 MB）—— 通用桌宠框架（流式模型/TTS/Live2D/MCP）。⚠️ 与 r38 登记的 `SDFA-BOOP/PetForge-A-modular-...`（404 未核实）**描述高度相似**，疑为同源重传，故只登记不进正文。URL https://github.com/x01n/petforge
- `bearman141/ds-whale-pet`（★2 · NOASSERTION · JavaScript · 建仓 2026-09-25 · pushed 2026-09-27）—— DS 鲸鱼娘桌宠，Electron + Cubism 4。URL https://github.com/bearman141/ds-whale-pet
- `windblown-directionalantenna594/2d-vtuber-vtube-studio-setup-toolkit`（★0 · 无许可证 · 无语言 · 建仓 2026-09-22 · pushed 2026-10-11 · 481 B）—— VTuber 开播配置工具箱（VTS + 表情 + 快捷键 + OBS 场景）。URL https://github.com/windblown-directionalantenna594/2d-vtuber-vtube-studio-setup-toolkit
- `YoKONCy/Peroperochat`（★14 · GPL-3.0 · Vue · pushed 2026-04-27 · forks 2 · 51.5 MB）—— Capacitor 构建的移动端应用，集成 Live2D SDK 渲染 + **离线记忆引擎**，iOS/Android/Web。URL https://github.com/YoKONCy/Peroperochat
- `sucv/HoloLive2dChatbot`（★43 · 无许可证 · C++ · pushed 2023-07-03 · forks 6）—— Qt + Live2D SDK 的 ChatGPT 全息聊天机器人（"DIY 版 Gatebox"），**2023 停更**。URL https://github.com/sucv/HoloLive2dChatbot
- `Chaoray/AzurLane-Live2D-Viewer`（★28 · 无许可证 · JavaScript · pushed 2024-05-26 · **仓库 2.1 GB** · 已部署 https://Chaoray.github.io/AzurLane-Live2D-Viewer/）—— 碧蓝航线 Live2D 查看器。★28 尚可但**停更两年 + 2.1 GB 仓库**（内含模型资产），不进正文。URL https://github.com/Chaoray/AzurLane-Live2D-Viewer

**官方组织补漏组的余下条目（`gh api orgs/Live2D/repos` 整表拉出，去重后 KEEP 但未进正文）：**

- `Live2D/CubismUnrealEngineComponents`（★32 · pushed 2026-09-29 · 2024-08-07 建仓）—— 官方 Unreal 组件，与 r38 已收的第三方 `Arisego/UnrealLive2D`(★153) 形成官方/社区对照。URL https://github.com/Live2D/CubismUnrealEngineComponents
- `Live2D/CubismJavaFramework`（★16 · NOASSERTION · Java · pushed 2026-06-04 · 350 KB · forks 6）+ `Live2D/CubismJavaSamples`（★31 · NOASSERTION · pushed 2026-06-04 · 51.7 MB · forks 7）—— 官方 Java 路线全套，2022 年才建仓（比 C++/Web/Unity 晚 4 年）。URL https://github.com/Live2D/CubismJavaFramework · https://github.com/Live2D/CubismJavaSamples
- `Live2D/CubismAndroidLiveWallpaper`（★45 · pushed 2021-09-02）—— 官方安卓动态壁纸样例，**已停更 5 年**（与本轮 §三.14 的社区版 `BANDORI-PET-Android` 正好互补）。URL https://github.com/Live2D/CubismAndroidLiveWallpaper
- `Live2D/CubismCocosCreatorComponents`（★8 · pushed 2023-09-28）—— 官方 Cocos Creator 组件，与"Native R2 后终止 Cocos2d-x"的口径相关（Cocos Creator ≠ Cocos2d-x）。URL https://github.com/Live2D/CubismCocosCreatorComponents
- `Live2D/CubismPhotographyApp`（★1 · pushed 2021-12-22）—— 官方拍照应用样例，停更。URL https://github.com/Live2D/CubismPhotographyApp

**nizima LIVE 生态余下条目：**

- `polisherm/nizima-live-speech-plugin`（★0 · NOASSERTION · TypeScript · 建仓 2026-08-17 · pushed 2026-08-30 · 406 KB）—— 用 **nizima LIVE Plugin API + VOICEVOX** 让 Live2D 模型带声音、口型、表情、字幕说话（日文项目）。URL https://github.com/polisherm/nizima-live-speech-plugin
- `KarakuriPolta/nLFaceController`（★0 · MIT · Python · 建仓&推送 2024-05-31 · 51 B）—— 用 nizima LIVE 参数模拟键盘输入的插件（**仓库仅 51 字节**，实为空壳/说明）。URL https://github.com/KarakuriPolta/nLFaceController
- `flat-yr/nizimaLIVE-Scripts`（★0 · MIT · JavaScript · 建仓 2025-05-29 · pushed 2025-07-10 · 10 KB）—— nizima LIVE 脚本集。URL https://github.com/flat-yr/nizimaLIVE-Scripts
- `bungaku-moe/Dump-Nizima-Live2D`（★1 · 无许可证 · 建仓&推送 2024-09-23 · homepage https://nizima.com）+ `bungaku-moe/Nizima-Live2D-Samples`（★0）—— 自述 "Messy ways to dump Nizima Live2D samples"，**资产爬取向，版权灰色**，只登记名字。URL https://github.com/bungaku-moe/Dump-Nizima-Live2D
- `dasilva333/live2d-nizima-index`（★0 · 无许可证 · HTML · 建仓 2026-07-27 · pushed 2026-08-02 · **220 MB**）—— 无描述的 nizima 索引站，220 MB 疑似含资产。URL https://github.com/dasilva333/live2d-nizima-index
- `jellydreams/VTS-Fullbody-Tracking`（★34 · 建仓 2024-04-10 · pushed 2025-03-05）—— 仅用摄像头做 Live2D **全身**追踪的 VTube Studio 插件（与 pyNizima 同作者）。URL https://github.com/jellydreams/VTS-Fullbody-Tracking


---

## 六、去重报告

**本路候选总数**：扫描约 **235 个不重复仓库**（GitHub 27 式查询 + 官方组织整表）+ Gitee 5 + HF 若干 → 经 `grep -iF` 比对七份基线 + 上下文复核后，最终 **KEEP 68 条**，其中 **37 条进正文**（§三 24 + §四 13）、**31 条进边缘**（§五）。

**剔除总数：约 167 条**（含已卡、r38 已收、上游改名、镜像、假命中澄清、内容农场、空壳）。

> **补做说明**：初稿交付后收到 general-purpose-2 的交叉核对反馈，追加了「Live2D 官方组织整表扫描」与「nizima 系列查询」，新增 §三 19–24（6 条）+ §五 追加（11 条）。上述数字已含这批。

### A. index.html 已卡（含 r38 的 [1403]–[1425] 共 23 张），命中即弃（代表性列举）

*A1. 老牌高星 Live2D 仓库（`live2d` 按 stars 前 60 必现，全数已在 index）：*
`moeru-ai/airi`(★50287)、`Open-LLM-VTuber`(★14044)、`stevenjoezhang/live2d-widget`(★10981)、`EYHN/hexo-helper-live2d`(★3872)、`Eikanya/Live2d-model`(★3439)、`wan-h/awesome-digital-human-live2d`(★2425)、`zenghongtu/PPet`(★2034)、`xiazeyu/live2d-widget.js`(★1578)、`guansss/pixi-live2d-display`(★1508)、`xiazeyu/live2d-widget-models`(★1468)、`fghrsh/live2d_demo`(★1467)、`Voine/ChatWaifu_Mobile`(★1430)、`morettt/my-neuro`(★1390)、`jofizcd/Soul-of-Waifu`(★1386)、`elevenyellow/handcrafted-persona-engine`(★1381)、`fghrsh/live2d_api`(★1323)、`imuncle/live2d`(★1156)、`galnetwen/Live2D`(★1063)、`timi-liuliang/echo`(★991)、`DasterProkio/awesome-ai-companion`(★920)、`Dreamer-Paul/Pio`(★899)、`JoeyBling/hexo-theme-yilia-plus`(★744)、`Navi-Studio/Virtual-Human-for-Chatting`(★707)、`avgjs/pixi-live2d`(★682)、`hacxy/l2d-widget`(★639)、`Perfare/UnityLive2DExtractor`(★634)、`EasyLive2D/live2d-py`(★576)、`mmmmmm44/VTuber-Python-Unity`(★558)、`wpydcr/LLM-Kit`(★554)、`vignetteapp/vignette`(★522)、`xb2016/poster-girl-l2d-2233`(★584)、`huihut/Facemoji`(★455)、`ezshine/AwesomeLive2D`(★411)、`lawsonsli/faceCapture`(★386)、`yeemachine/kalidoface-2d`(★381)、`summerscar/live2dDemo`(★363)、`fguby/live2D`(★328)、`fguby/Electron-elf`(★317)、`Perfare/AzurLaneLive2DExtract`(★303)、`QiShaoXuan/live2DModel`(★301)、`MizunagiKB/gd_cubism`(★301)、`yui540/satella.io`(★298)、`erodozer/open-vt`(★284)、`v3ucn/live2d-TTS-LLM-GPT-SoVITS-Vtuber`(★283)、`52cik/bilibili-haruna`(★283)、`rotejin/MotionPNGTuber`(★337)、`xb2016/33-live2d-wp`(★128)、`open-mmlab/Live2Diff`(★199)、`guansss/live2d-viewer-web`(★175)、`Arisego/UnrealLive2D`(★153)、`vtubing/moc3`(BASE 命中)、`kongbaiku/Live2D-M`(BASE 命中)、`stkrwork/UE-Live2D`(BASE 命中)。

*A2. r34–r38 期间已卡的 Live2D 新势力（本轮复现，再次剔除）：*
`jtydhr88/ComfyUI-See-through`(★835, index [1176])、`Jelosus2/BD2-L2D-Viewer`(★542)、`CheshireMew/PuppetLoom`(★245, [1260])、`umamoorg/umamo`(★151, [1207])、`Arcelyth/live-ascii`(★234, [1224])、`nanlingyin/soullink-emotion-sdk`(★148, [1223])、`lmmtrr/spive2d`(★138, [1225])、`Untitled-Story/untitled-pixi-live2d-engine`(★78, [1222])、`aethiopicuschan/cubism-go`(★32, [1218])、`Panzer-Jack/easy-live2d`(★213, [1196])、`cqzaaa/AgentPet`(★262, [1270])、`kiyotakali/Miru`(★175, [1308])、`momori777/Artemis`(★382, [1237])、`SparcAI-Inc/Bunraku`(★37, [1248]，arXiv 2607.27348)、`zeikar/iki`(★15)、`tsunehimatoi/psd2live`(★616)、`liwenka1/bongo-cat-next`(★151)、`kongweiguang/xiaoya`(★1)、`pakholeung37/gd_cubism`、`omniwaifu/pixi-live2d5`(★12)、`luomo66ccff/Amahane-Hikari-Live2D`(★113)、`ochiru520/Mio`(★49)、`moonrailgun/vtubeleaf`(★13)、`haneoka-gakuen/vega`(含 vega-plugin-cubism / vega-plugin-composite / altair-plugin-models 整套)、`Hera-Berg/open-avatar-creator`、`turboism/Turboism`(★3)、`HELPMEEADICE/Neocari`、`shinkuan/Waifuland`(★81)、`sdegfd/embedded-live2d`、`Eatgrapes/Live2D-JavaBinding`、`hoardodile/plugin-2d-skel`、`4163/pixijs-live2d-spine-viewer`、`fyisgod/live2d-desktop-pet-electron`、`shinshin86/live2d-add-motion-sample-web-ui`、`goodko/xiaozhi-ios`、`LitStronger/live2d-moc3`、`julfed7/Cubism-2`、`Hisakazu333/NekoPapa`、`A8Chann/dsh-pet-live2d`(★39)、`cyanfish-x/dsh-live2d-pets`(★31)、`SherlockYzz/anime-desktop-pet`(★9)、`shicheng5589-oss/Agent-desktop-pet`(★21)、`sslbs09/suzuran-pet`(★17)、`yuri-os/YuriOS`(★34)、`chengyuZou/EmaAgent`(★3)、`fswolf/luna-local-agent`(★4)、`nyan-mikan/codex-live2d`、`MetaSekaiLab/nnnotes`(★15)、`UlyssesWu/D2Evil`(★139)、`OpenL2D/moc3ingbird`(★98)、`goldimpact/Eviler`(★12)、`Yoru-KenomoVT/ayatsuri_2d`(★2)、`phoiex/AAAAGENT`(★149)、`AOrbitron/Eridanus`(★206)、`Maboroshinatsu/maibot-deskpet-plugin`(★7)、`impossibletea/liver`(BASE)、`SuomiKP31/GFLMotionConverter`(★10)、`ymhyyds/DesktopPet`(BASE)。

*A3. 「See-Through 拆层 → psd2live 绑定 → moc3」这条流水线上的已卡同源仓（本轮复现 4 条，全弃）：*
- `flowingduskpro/jpg-to-live2d-workflow`（★4，index 卡片 + csdn-social-summary.md:464 双重命中）
- `mw2wbyys6t-sudo/live2d-auto-pipeline`（★10，index [1264]）
- `daoming07280/live2d-auto-pipeline`（index [1360]）
- `Kota-Ohno/seethrough-live2d-pipeline`（★10，index [1187]）
- `lvhaojie456/image-to-live2d`（★2）
- `rig-c/core`（★12）+ `rig-c/parts`（★2）—— index 已卡（"AI 写的 2D 绑定，编译成 Spine 4.3 并用断言把关"）。
> **这构成 §二主线里对"绑定流水线第二例"这个问题的直接回答。**

### B. 上游改名 / 旧路径（README badge 常留旧名，须交叉核对）
- `luckui/ai-live2d-go` → `gh api` **返回的是 `luckui/HiyoriAI` 本体**（同一仓库旧名）。**不是两个项目**，已按新名收录（§四.2）。
- `Arkueid/live2d-py` → 现为 `EasyLive2D/live2d-py`（已在索引）；其 fork `kazari0kokonoe/live2d-py`（★0，支持 SDK 5 r.5）因 BASE 命中旧名剔除。
- `ymhyyds/DesktopPet`（Qt6 + Cubism SDK + DeepSeek）与 `VeiQiuLab/DesktopPet` **是不同仓库**，经上下文复核后者保留（§四.11）。

### C. 假命中澄清（短词/子串误伤，用 `grep -o ".\{40\}关键词.\{70\}"` 看上下文后判定为 KEEP）
| 候选 | 初次 BASE 命中的"元凶" | 结论 |
|---|---|---|
| `Momoyeyu/momo` | `momori777/Artemis` 里的子串 "momo" | **假命中**，但仅进边缘（另有 59 open issues 异常） |
| `liyu-1028/mochi` | `genmoai/mochi`（视频生成模型，★3722） | **假命中** → 收进 §四.9 |
| `Yuuzulight/Mana` | `Amethyst-Mod-Manager` / `KKManager` 里的 "Mana" | **假命中** → 收进 §四.7 |
| `VeiQiuLab/DesktopPet` | `1704919/WuziDesktopPet` / `DesktopPetXuansi/Xuansi` | **假命中** → 收进 §四.11 |
| `x01n/petforge` | r38 登记的 `SDFA-BOOP/PetForge-...`（404 未核实） | 描述高度相似，**疑同源重传** → 仅边缘登记 |

### D. 真同名但内容重复（判定剔除）
- `Midnight-Su-J/Live2D-Viewer`（★0，2026-09-25 建仓）vs r38 已收的 `ImDuck42/Live2D-Viewer`（★14）—— 同为"浏览器端 Live2D 查看器"，**内容农场式同名克隆**，剔除。
- `Hana-ame/live2d-viewer`（★0）vs `guansss/live2d-viewer-web`（已卡）—— 同功能同名，剔除。

### E. Gitee / 其他平台镜像（本轮无原生新仓）
WebSearch 命中 5 条全部是镜像或教学拷贝：`adong168/live2d-py`（= EasyLive2D/live2d-py）、`JokerPan12/live2d-moc3`（= Cubism 官方 Samples 的教学说明）、`xyzgy/cubism-sdk-for-web`（= Cubism Web SDK 修改版）、`MizunagiKB/gd_cubism`（CSDN 教程引用，已卡）、`letere-gzj/live2d-widget-v3`（GitHub 已卡）。

### F. 空壳 / 无法核实（一律写"未核实"，不写"不存在"）
- `Laughting455/live2d_toolkit-v2`（★0，建仓即停，**size=0**）—— 本轮 API **命中成功**，空仓判断来自 `size=0` + 单次推送，**非 404**；已按"方向存在、实现未落"登记（§三.16）。
- `whymycompilefail/cpu-only-ai-tuber`（MIT，size=0）—— 同属 `size=0`，但其 README **内容详实且有实测数据**，故照常进正文（§四.1）；作者已说明 llama.cpp 的 `.git` 被改名为 `.git.fork-backup/`（**不是删历史**）。
- `yanghuagai55/astrbot_plugin_live2d_pet`（★12）—— 无 description、README 未取到，功能描述以仓名与生态位置为准，**已标注"未做深度核实"**。

### G. 本轮额外两问的查证结论（写进 §二主线）
1. **「不做渲染」的纯解析工具（继 py-moc3）**：本轮**新增命中 4 条**，分属三个层次——`ihopenot/LpkUnpacker`（容器层：.lpk 解包，★296，§三.2）、`Arkueid/lpk2moc3`（定向提取层：lpk→moc3，★18，§三.3）、`kiraio-moe/Revolt2D.Motion3` + `.MotionSync3`（配置层：.motion3.json / .motionsync3.json 序列化，各 ★0，§三.15）。**但严格意义上的「moc3 二进制读写」仍无新增**：`vtubing/moc3`(★10) 已被 BASE 命中剔除；`zhzhongshi/MOC3-Explorer`(★2，Java，无描述无 README) 与 `Sachin-Dev55/MOC3_Library`(★1) 虽 `grep` 为 0，但**均无法核实是否真做解析**（前者仅 38 KB 单次推送），只进边缘；`QiE2035/moc3-reader-re`(★17，2022 停更) 亦同。结论：`Ludentes/py-moc3` 在「moc3 二进制读写」上仍是索引里唯一一条。
2. **「绑定做成可复用流水线」的第二例**：r35–r38 期间**已卡至少 6 条同源仓**（见 A3），本轮**没有出现第七例**；唯一的新形态是 `Zosuya/ParaRig`（§三.5）——**它不在 moc3 路线上，而是把"配置列表 → 一键生成控件 + Frame + Driver"这套绑定抽象落到了 Blender**，属"跨路线的同类思路"而非追加一例。

### H. `grep` 通过（KEEP）但本轮未入选正文——去重上**不算重复**，只因体量/成熟度/主题贴合度而暂不收

这一档请**不要**在下辑当作"已剔除"处理；它们是合法新仓，本轮只是没位置写。每条均已过 `grep -iF` 七份基线比对，命中 0：

- 格式/工具向：`QiE2035/moc3-reader-re`(★17 · 2022 停更 · 逆向 moc3 reader)、`Sachin-Dev55/MOC3_Library`(★1)、`Veykril/cubism-rs`(★47 · 2020 停更 · Rust 封装)、`qinyonghang/Live2D-Python`(★21 · PyLive2D 封装)、`HCLonely/Live2dV3`(★61 · 网页 moc3)、`letere-gzj/live2d-widget-v3`(★41)、`DenchiSoft/Live2DLighting`(★155 · 2019 停更 · Live2D 打光/后处理)、`yttbz/ciallo-for-desktop`(★1)、`s1fx/UnityLive2DCubismPoser`(★4)、`IsaacBell/awesome-vtuber`(★0 · awesome 清单)
- 素材/模型库向（非工具）：`xiaoski/live2d_models_collection`(★195)、`xiarimangguo/aLive2D`(★185)、`Pelom777/DestinyChildLive2D`(★128)、`mzyy94/ARKit-Live2D`(★174)
- AI 桌宠向（同质化海，本轮已收 13 条，余下不再铺开）：`chinokikiss/Live2D-Virtual-Girlfriend`(★233)、`JimHans/live2d-kanban-desktop`(★336)、`DD-MASTER/AI-Girlfriend-Desktop-Pet`(★238)、`KennardWang/VTuber-MomoseHiyori`(★200)、`LikeNeko/L2dPetForMac`(★125)、`Yancheng-s/mate-human`(★11)

---

### I. 官方组织整表扫描（补做）的结果

`gh api orgs/Live2D/repos` 拉出 **20 个仓库**，逐条过 `grep -iF` 七份基线：

- **已卡（4 条，剔除）**：`Live2D/CubismSpecs`[1202]（**官方文件格式规格——自己写解析器的唯一权威**，r33 已收）、`Live2D/CubismWebFramework`[1170]、`Live2D/CubismUnityComponents`[1171]、`Live2D/CubismNativeFramework`。
- **未卡（16 条，KEEP）**：其中 **6 条进正文**（§三 19–24 的 8 个仓库合并计）、**10 条进边缘**（§五"官方组织补漏组"）。
- **结论**：官方组织此前**从未被整表扫过**，各辑都是"搜索时顺带命中一条收一条"，导致 Samples 系列（★393 / ★239）这种高星基础件反而漏了。建议下辑起把 `gh api orgs/<vendor>/repos` 作为固定动作，覆盖 `Live2D`、`Live2D-Garage`、`EasyLive2D`、`Open-LLM-VTuber` 等组织。

### J. nizima 线的产品形态澄清（回应 gp-2）

`gh search repos "nizima action"` 与 `"live2d nizima"` **均返回 0 条**，`"nizima"` 命中的 12 条**全部属于 nizima LIVE**（桌面表演/直播应用），无一条关于 nizima ACTION。
**判断**：**nizima ACTION 是纯闭源在线视频编辑器，没有开源仓库、没有第三方导出脚本**，gh 路在这条线上不存在漏网。索引若想覆盖它，只能走 gp-2 的官方文档路线（`docs.live2d.com/nizimaaction/...`）。

### K. 官方手册站点的整表结构（gh 路越界做的一次探测，供官方路/下辑复用）

gp-2 指出"docs.live2d.com 下除了 Cubism Editor 手册，还有 nizima LIVE / nizima ACTION / SDK / Viewer 四套独立手册，此前也从来没被整表列过"。我用 `curl` 把站点地图实拉了一遍，结论如下（取数 2026-10-12，`HTTP 200` 实测）：

**官方手册实际是 3 套独立 WordPress 站点（各有 `/en/` 英文镜像）：**

| 站点 | sitemap 入口 | 子表条目数（JA） |
|---|---|---|
| 主站（Editor + SDK） | `docs.live2d.com/sitemap.xml` | editor_manual **241** / editor_tutorials **28** / sdk_manual **179** / sdk_tutorials **77** / page 1 → 合计 **526 条** |
| nizima ACTION | `docs.live2d.com/nizimaaction/wp-sitemap.xml` | page 1 / manual **30** / tutorials **12** → 合计 **43 条** |
| nizima LIVE | `docs.live2d.com/nizimalive/wp-sitemap.xml` | page 1 / manual **33** / tutorials **25** → 合计 **59 条** |

**几个可直接用的结论：**
1. **主站根路径没有 sitemap 之外的入口**：`/cubismviewer`、`/cubismeditor`、`/sdk`、`/viewer` 全部 **404**——手册是按 WordPress 自定义文章类型分的（`editor_manual` / `sdk_manual` 等），不是按路径分。
2. **gp-2 提到的第 4 套「Viewer 手册」本轮未定位到**：主站 sitemap 里没有 viewer 类型，`/cubismviewer*` 路径全 404。结合 §三.21（官方 `CubismViewer` 仓库 **2018 年停更、仓库仅 11 KB**），合理推测是**官方 Viewer 手册已随产品下架**，而不只是没被扫到。建议官方路按此结论处理，别再花时间找。
3. **两个 nizima 子站加起来才 ~102 条**，扫完成本极低；主站 526 条是主要工作量。
4. **这印证了 §六-I 的同一个方法论漏洞**：官方侧的"整表扫描"动作此前也没做过。下辑官方路建议直接按上表三行入口扫一遍，与 gh 路的 `gh api orgs/Live2D/repos` 成对做。

（本小节数据来自 `curl` 实测 HTTP 状态码与 sitemap 条目计数，**非 `gh api`**，特此标明来源。）

---

## 七、取证纪律自述

1. **未撞 429**：`gh api` / `gh search` 全程正常，无速率限制。
2. **404 说明**：本轮 `gh api` **未出现任何 404**（全部 68 条 KEEP + 抽样 DROP 均取数成功），因此本文件**不含任何基于 404 的"不存在"判断**。
3. **"0 条结果"≠"不存在"**：nizima ACTION 的 0 条来自 `gh search repos` 空集，与 404 性质不同——已在 §三.23 与 §六-J 注明是"产品闭源"而非"仓库消失"。
4. **空壳判定依据**：`Laughting455/live2d_toolkit-v2` 的"空仓"判断来自 API 成功返回后的 `size=0` + 单次推送，**不是 404**。
5. **star 数零凭记忆**：本文件每一个 ★ / license / language / 日期 / forks / size 均取自 `gh api repos/<r>` 实返（68 条），或 §六-K 中明确标注的 `curl` 实测。
