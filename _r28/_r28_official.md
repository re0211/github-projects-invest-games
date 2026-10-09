# 第二十八辑 · Live2D 全链路（建模→绑骨→动画→引擎集成→驱动→商用变现）

> 调研日期：2026-10-10 · 范围：live2d.com / docs.live2d.com / GitHub Live2D 官方仓 / Unity Discussions / Godot Forum / dev.to / Stack Overflow / 官方 creators forum / nizima 政策 / itch·Steam·Booth
> 去重基线：`_r28/_dedupe_urls.txt`（1316）+ `_r28/_dedupe_gh.txt`（1189）+ `_r27/_r27_official.md`（524 行，已通读逐条比对）+ `csdn-social-summary.md`(v27) + `csdn-social-summary-v26.md`(v26)
> 纪律：**任何日期都写明第二独立入口**；取不到的一律写「未核实」。M-0029（列表页按位置取日期会错配）已生效——本轮**不从任何 HTML 列表按位置取值**，一律取对象自身字段（GitHub API `published_at` / Vanilla `DateInserted` / 文章 `published_at` / 页面 revision 记录）。
> 本轮 Cubism 版本号：**没有任何 5.4 正式版、没有 SDK 5-r.6**；主线结论仍是「继续用 5.3.00」。新东西全在**政策/授权、替代运行时、无 Editor 工作流**这三条线上。

---

## 一、官方上新

### A. Cubism 5.4 alpha：本轮唯一在有效期内的重大新信息（**8 天后失效**）

- [Cubism 5.4 Alpha Release Announcement](https://www.live2d.com/en/information/cubism-5_4-alpha/) — Live2D Inc. 官方公告 · **2026.07.14**（交叉：`?info_cat=product` 分类页同日 + 公告页 `发布时间` 字段，两处一致）· **alpha 可用到 2026-10-18，到期后不再提供**；alpha1 已于 2026-09-14 停用，现存的是 alpha2；官方 FAQ 原话：**「请勿销售或分发」**用 alpha 做出的数据，只能个人使用 · **有用**——这条直接的商业判断：别把 5.4 写进你的第一款商业 VN 制作链；想尝 Parameter Controller 就这周抓，别用它的产出发版。
- [同上公告页 FAQ：「是否需要付费 license？」](https://www.live2d.com/en/information/cubism-5_4-alpha/) — 同上 · 2026.07.14（两处互证同上）· 官方回答 No：**没有付费 license 也能装 alpha 试用 5.4 新功能**，但 FREE 版只能试「cubism 5.3 为止的既有功能」，新功能要能把 5.4 装上才行 · **有用**——学生/零预算可以零成本评估 5.4，但「免费试用」≠「可以商用」。
- [同上公告页关于 SDK 的注意事项](https://www.live2d.com/en/information/cubism-5_4-alpha/) — 同上 · 2026.07.14 · 官方明确：**alpha → beta/release 的 SDK 迁移不作保证，用 alpha 产出的数据不做任何质量保证、不提供支持**，建议先备份 · **有用**——这条把「等正式版」钉死了：正式版出来前，你的模型工程一律用 5.3.x 产出。
- [5.4 alpha 的 External App Integration Manual（官方 External API）](https://cubism.live2d.com/link/manual5_4_alpha_external-api-intergration_en) → 实跳 `https://cubism.live2d.com/editor-alpha/doc/manual/alpha1/en/external-api-intergration/index.html` — Live2D Inc. 官方 alpha 手册 · 日期**未核实**（页面本体无发布日；所属 alpha 版发布日期 2026.07.14 已两处互证）· **官方第一次提供了「从外部程序操作 Cubism Editor」的正式 API 面**，5.4 alpha 起才有 · **参考**——这是未来「脚本/AI 驱动 Editor」的官方入口，但目前挂在 alpha 上，今天不能作为商业工程的依赖。

### B. 官方 SDK：全线无 5-r.6，但有几条之前没记过的

- [Cubism 5 SDK MotionSync Plugin for Unity R2_1](https://github.com/Live2D/CubismUnityMotionSyncComponents/releases/tag/5-r.2.1) — GitHub Live2D 官方仓 · **2026-08-25**（交叉：release `published_at` 与 commit「Update to ... R2_1」同一天，两个独立对象）· **口型同步插件 6 年来的第一次更新**（上一版 R2 是 2024-11-28）；许可证字段 **NOASSERTION** · **参考**——做 VN 用不上它的 Unity 侧，但它说明「官方口型同步（MotionSync）」这条线还活着（`docs.live2d.com` 有 MotionSync 专区）。
- [Cubism 5 SDK MotionSync Plugin for Native R2_1](https://github.com/Live2D/CubismNativeMotionSyncComponents/releases/tag/5-r.2.1) — GitHub Live2D 官方仓 · **2026-08-25**（交叉同上）· Native 与 Unity 两个分支同一天发布；Native 分支理论上离 Ren'Py 更近，但 **Ren'Py 官方 Live2D 文档未提及 MotionSync**，集成需自行验证 · **参考（未实测）**——想要「音频驱动的口型」而不是参数驱动的 mouth open，这是唯一的官方路径，但**Ren'Py 侧支持情况本轮未核实**。
- [CubismUnityComponents 修复 Unity 6.6 编译错误（PR #96）](https://github.com/Live2D/CubismUnityComponents/commit/2026-09-29) — GitHub · **2026-09-29**（commit `author.date`；⚠️ **只到 commit 层面，未发 release**）· 修复 `GetInstanceID` 过时导致的 Unity **6.6** 编译失败，同时做了 `birp/develop` 分支 · **有用（条件）**——如果你打算用 Unity 做 VN 封面动画/预览，Unity 6.6 上要用这个 commit，别直接用 `master` 的最新 release（`5-r.4.2`，[见](https://github.com/Live2D/CubismUnityComponents/releases/tag/5-r.4.2)，**2026-05-14**，GitHub release `published_at`）。
- [SDK 现状复核（本轮）](https://github.com/Live2D/CubismWebFramework/releases) — GitHub API · Unity R5 **2026-04-02** / Native R5 **2026-04-02** / Web R5 **2026-04-02** / Java R5 **2026-06-04** / Unreal `5-r.1-beta.2` **2026-09-29**（均为各 release 自身的 `published_at`）· **五个仓都没有 `5-r.6`，也没有任何 5.4 命名的 tag 或分支** · **参考**——对 v27 §1.2 的复核，结论不变，可作为下次查版本号的底稿。

### C. 官方规格与数据格式：首次拿到两条「动过」的证据

- [CubismSpecs：给 exp3.json / pose3.json 加可选 Version 字段（PR #7，已合并）](https://github.com/Live2D/CubismSpecs/pull/7) — Live2D 官方规格仓 · **2026-08-05**（交叉：PR `merged_at` + 该仓同一天 commit「Add Version info as an optional field」）· 官方第一次给 **exp3/pose3 加版本号字段**，这是官方仓 2017 年以来**第二次有人改**（上次是 2024-04）· **有用**——第三方工具（含 v27 收录的 `live2d-motion3`）写出的表情/姿态文件今后有了标版本的地方；反过来读别人的文件时要考虑多一个可选字段。
- [CubismSpecs：CDI3 规格加入 Drawables（PR #5，仍 open）](https://github.com/Live2D/CubismSpecs/pull/5) — Live2D 官方规格仓 · **2026-07-20**（交叉：PR `created_at` **+ 官方创作者论坛同题帖 DateInserted = 2026-07-20**，两个不同平台独立一致）· 提议让 `cdi3.json` 可选地带上 Drawable 列表；动机是第三方工具/引擎现在拿不到 drawable 级信息 · **参考**——论坛帖 0 评论、PR 至今未合并，**提案阶段，不是可用功能**。
- [官方创作者论坛：要求 CDI3 加 Drawables（Azxiana）](https://community.live2d.com/discussion/2376/add-drawables-as-an-optional-part-of-the-cdi3-specification) — Live2D 官方 Creators Forum · **2026-07-20**（帖子 JSON 的 `DateInserted` 字段）· 提出者就是上面 PR #5 的作者 · **参考**——同一议题的第二个入口，用于凑足交叉验证。

### D. 官方样本模型：清单变长了，且**授权的分档和后果**首次说清

- [Live2D Sample Data Collection（免费）](https://www.live2d.com/en/download/sample-data/) — Live2D Inc. · 日期**未核实**（列表页无日期）· 本比 v27 时多出/需注意的四个：**Ren Foster**（学 Cubism 5.3 的新绘制功能）、**Niziiro Mao**（Blend Shape / multiply-screen color 示例）、**Kei**（MotionSync 真实口型同步示例）、**Sample for Parameter Controller**（5.4 alpha 新功能）；部分模型同时提供 **SDK5.3/Cubism5.3** 版本 · **有用**——要验证「Cubism 5.3 的 moc3 到底能不能在我的引擎里动」，**Ren Foster 是官方给的免费靶子**（`/learn/sample/ren-foster/`）。
- [Live2D Cubism サンプルデータ利用条件（样本数据使用条款）](https://www.live2d.com/learn/sample/model-terms/) — Live2D Inc. 官方 · 日期**未核实**（页面无修订日）· 把样本分成三类：**Live2D オリジナル / コラボレーション / 社外ライセンス**；**每类适用的利用条件不同**；其中 **コラボレーションキャラクター（名執 尽、春傘 つみき）明确「営利目的での利用や改変・配布はできません」** · **有用（决定生死的一条）**——这两个角色无论怎么做都没有商用这条路，做商业 VN 直接排除。
- [同页：按角色的个别限制 + 必须标注的著作权表示](https://www.live2d.com/learn/sample/model-terms/) — 同上 · 未核实 · ミアラ/桃瀬ひより（含动画版）**一切设计上的改动都被禁止**；にと 必须保持二头身；マークくん 必须保持卡通调（不能描成美男子/剧画调）；しずく 必须保留名字与设定。用到作品上必须标：「本作品のキャラクターには株式会社Live2Dの著作物…」，游戏/アプリ的**说明栏**属于允许放长文的那档 · **有用**——「用拿来主义的样本模型发商业 VN」这一点上，**选人时有硬约束**（例如不能改设计、不能改比例、必须保留命名与设定）。
- [無償提供マテリアルの使用許諾契約書（Free Material License Agreement，英文）](https://www.live2d.com/eula/live2d-free-material-license-agreement_en.html) — Live2D Inc. 官方契约 · 日期**未核实** · **§2.1.3.1：一般用户/小规模事业者的使用目的 = 「irrespective of commercial or Non-commercial purposes」（商用非商用均可）**；**§1.23 小规模事业者 = 最近年度营业额不足 1000 万日元的事业者（含个人）**；**§2.1.4 コラボ角色：一般用户 = 非商用限定**；§2.1.5 要求标注著作权；§4.1.3 禁止反向工程 · **★★ 本轮最值钱的一条**——详见文末「三到五条」第 1 条。

### E. 官方活动/促销：2026 下半年**没有任何新东西**（负结论）

- [官方全站 News / Event 分类](https://www.live2d.com/en/information/) — Live2D Inc. · 最近一条 Campaign = **2026.07.17** 夏季促销；最近一条 Product Info = **2026.07.14** 5.4 alpha；最近一条 Event = **2025.10.14** Live2D Game Jam Winners · **2026-07-17 至今天之间官方零公告** · **参考**——「等打折」这条线上，秋冬场还没有影子，春夏两场都过期了。
- [官方创作者论坛另一入口 creatorsforum.live2d.com（区别于 community.live2d.com）](https://creatorsforum.live2d.com/) — Live2D Inc. · 日期未核实 · 5.4 alpha 公告页指定的反馈区是这个新域名（注册后可收 alpha 更新通知），而排错问答的老域 `community.live2d.com` 仍在用 · **参考**——下轮搜官方答复时两个域名都要查，v27 只用了 `community` 一个。

---

## 二、实战测评

- [Open-LLM-VTuber Review: Offline AI Companion with Live2D](https://dev.to/andrew-ooo/open-llm-vtuber-review-offline-ai-companion-with-live2d-327m)（原刊 [andrew.ooo](https://andrew.ooo/posts/open-llm-vtuber-offline-ai-companion-review/)）— dev.to · **2026-06-08**（API `published_at`；canonical 原文站本轮未打开）· **本轮唯一一份带着可复核数字的真评测**：作者在 M2 Pro 上连跑 3 天（`qwen2.5:7b` + Ollama + sherpa-onnx ASR/TTS），给出延迟拆解 **ASR ~200ms + LLM TTFT ~600ms + TTS 首块 ~400ms ≈ 1.2s**；FAQ 里给出 **16GB M1 Air 跑 `qwen2.5:7b`：往返 ~1.5s、常驻内存 ~6GB**；缺点写得很实——**v1.0.0 没有长期记忆**、macOS 上部分 TTS 仍走 CPU、v2.0 重写期（无发布日期）· **有用（作为 AI × Live2D 的成本/延迟基准）**——它是「本地 LLM 驱动 Live2D」这条路上少数给值的测评，其中「在流式输出里内联情感标签、用正则抽出后映射到 expression index」的做法很小而且能直接抄；但 ⚠️ 该文声称 `MIT`，而 GitHub API 给的 license 字段是 **NOASSERTION**，且本文声称「样本模型商用需要 Cubism Pro license」，**与本轮核到的官方 EULA（§2.1.3.1，个人/小规模商用不必）冲突，以官方契约为准**。
- [Unity Discussions：导入 Live2D 只见蓝色轮廓不见纹理（2026-05-24 提问 / 2026-07-13 解出）](https://discussions.unity.com/t/imported-live2d-models-not-appearing-on-screen-using-cubism-sdk/1720986) — Unity 官方 Discussions · **2026-05-24**（提问帖 `created_at`）/ **2026-07-13**（答复帖 `created_at`，两个独立帖对象）· 解法四步：Project Settings → Quality 设 Render Pipeline Asset 为 **UniversalRP** → Player → Other Settings 把 **Color Space 设为 Gamma** → 再导入 Cubism SDK → 在 UniversalRP asset 的 Renderer List 里加 **CubismURPRenderer** 并设为 Default · **★★ 有用**——与 v27 §3.1 的 Zenn 帖构成互证，但**多出两个 Zenn 那篇没写的点**：① 颜色空间必须 **Gamma**（Zenn 那篇没写）；② 答案是先在 Live2D 官方 Discord 找到、再回写论坛的——说明**官方 Discord 比论坛快**。
- [pixi-live2d5（pixi-live2d-display 的 Cubism 5 fork）](https://github.com/omniwaifu/pixi-live2d5) — GitHub · 创建 2025-08-21 / 最近推送 **2026-10-05**（repo 自身字段）· **专门为了解决「Cubism 5 的 moc3 第三方网页库不吃」而分叉**：README 明确要求 **PixiJS 8.19+ / Cubism SDK for Web R5（Core 6.0.1）/ WebGL2**，`bun run setup` 会自己下载 Core 与 13 个 GLSL shader；保留原高层 API，去掉了 cubism2/4 子路径；附 `checkMocConsistency` 选项与**「模型是不可信输入」的安全告示** · **★★ 有用**——这是本轮对 v26/v27 那条已知坑的**正面解法**：要做网页版试玩/宣传页，优先这条，不再纠结 pixi-live2d-display。
- [easy-live2d v1.0.0](https://github.com/Panzer-Jack/easy-live2d/releases/tag/v1.0.0) — GitHub · **2026-09-24**（release `published_at`；上一版 v0.4.4 是 2026-04-15）· v27 §4.4 记的是 v0.4.0，**现在已经是 1.0.0**，README 第 44 行写明用的是 **Cubism 5 SDK for Web R5 的官方 Core** · **有用**——pixi-live2d5 之外的第二个「Cubism 5 网页」选项，MIT、活跃、有中文 README；**Star 数（213）低不代表不成熟**，1.0.0 才是判断依据。
- [untitled-pixi-live2d-engine](https://github.com/Untitled-Story/untitled-pixi-live2d-engine) — GitHub · 创建 2026-01-23 / 推送 **2026-09-20**；★78 · MIT · 自述 「PixiJS v8 Live2D Engine | **Cubism 2–5 SDK** | Native Render Pipe & Lip-sync」 · **参考**——声称横跨 2/3/4/5 四代 SDK，若你需要同时兼容老模型和新模型可以考虑；**本轮未读源码，兼容性只按 README 声称，未实测**。
- [Purism Core（Cubism Core 的开源 C99 重实现）](https://github.com/SakuraMotion/PurismCore) — GitHub · 创建 2026-06-03 / 推送 **2026-08-21**；★40 · **MIT** · 纯 C99、单头文件 bundle（`PurismCoreBundle.h`）、覆盖 Win/macOS/Linux/iOS/Android/Emscripten；**明确写了「should be compatible with … Ren'Py」** · **★★ 有用**——见它 `docs/COMPAT.md` 给出的 ABI 对照表，这是本轮**对「为什么第三方吃不吃 Cubism 5」最好的机理说明**（详见文末「三到五条」第 2 条）。
- [Purism Core 的 v5 / v6 ABI 兼容表](https://github.com/SakuraMotion/PurismCore/blob/master/docs/COMPAT.md) — 同上仓 · 日期未核实（文档无发布日期）· **v5 ABI = Cubism Core 5.1**（Cubism Editor 5.1 引入），**v6 ABI = Cubism Core 6.0**（Cubism Editor 5.3 引入，「引入了多个破坏性变更」）；文内举例：**VTube Studio 用 v5 ABI、老版 Ren'Py 用 v5、最新版 Ren'Py 用 v6、gd_cubism 用 v5**；可用 `make ABI=v5` 切 · **★★ 有用**——把过去三轮反复出现的「不兼容」还原成了「ABI 版本」，从此不用猜。
- [MOC3ingbird：一份能让读取方崩溃的 .moc3（CVE-2023-27566）](https://github.com/OpenL2D/moc3ingbird) — GitHub · 创建 2023-03-03 / 推送 **2026-06-06**；★98（`undeleted.ronsor.com` 那篇 HN 文 v27 已引，但**这个 PoC 仓本身不在去重基线中**）· 作者判断：Cubism Core 是 C 库，**对 MOC3 内的偏移不做边界检查，读写可越界**；作者自称**尚未实现纯 Core 下的代码执行**，但可能存在；仓内含 `src/moc3.hexpat`（ImHex 样式，自称能看所有 MOC3）· **★★ 有用（按「别踩」记）**——第一款商业 VN 若只加载自己做的模型、不接受外部 .moc3，本条与你无关；但一旦计划「支持玩家导入模型 + UGC」，这是一个真实的攻击面——**这一点在这两年的中文/日文 Live2D 制作贴里几乎没人提**。
- [Pixi live2d 方案的安全告示（pixi-live2d5 README 的 Model asset trust 节）](https://github.com/omniwaifu/pixi-live2d5) — GitHub · 2026-10-05（repo 推送日）· 该库**不做沙箱、不限制资源数量/体积、不限制压缩包展开**，作者要求开发者自己建立信任、下载、归档与资源预算控制 · **参考**——与上一条是同一个问题的两面：网页端一旦接受第三方模型，信任与安全责任在你自己。

---

## 三、经验分享

### A. 不买 Editor 也能做/改动作（本轮最实的一条主线）

- [live2d-add-motion-sample-web-ui](https://github.com/shinshin86/live2d-add-motion-sample-web-ui) — GitHub · 创建 **2026-07-13** / 推送 **2026-10-08**；★194 · **MIT** · **只在 JSON 层面给现有模型加新动作，完全不需要 Cubism Editor**：`.motion3.json` 就是每个参数的几条关键帧曲线，在模型已有参数范围内改动即可，不涉及网格/骨骼。给官方样本 Hiyori 加了 7 个动作（Happy/Wink/Nod/Thinking/Surprised/Shy/Head shake），并且这些动作**不是手写的**，而是由生成脚本 → 独立校验器 → headless Chrome 验证三件套产出；**只依赖 Python 3 标准库** · **★★★ 有用**——对 16GB Windows 上的第一款 VN 这是本轮首选工具之一：你可以给自己角色的模型加上「害羞/点头/惊讶」这类表情动作而**一分钱 Editor 钱都不用花**；详见文末 AI 建议 §2。
- [同上：WebUI 的交互/预览能力](https://github.com/shinshin86/live2d-add-motion-sample-web-ui) — 同上 · 同上 · 本地起服务后（`tools/serve.py`，默认 8765）可拖动/缩放模型、区分一次性动作与循环动作、支持四种口型同步模式（关闭/模拟/跟随音频文件/跟随麦克风）、另有摄像头面捕与 OBS 直播模式；还带 `?freeze=`、`&cycles=`、`&record=` 等调试参数 · **有用**——可以把它当成「免费的动作预览器」用：在这边调好 → 把 `.motion3.json` 拷回你的游戏工程。
- [同上：如何给自己的模型（而不是样本 Hiyori）加动作](https://github.com/shinshin86/live2d-add-motion-sample-web-ui) — 同上 · 同上 · 官方三步：`tools/analyze_model.py` 先看有哪些参数、安全值域、**哪些参数是物理驱动的（不能直接动画）** → 在 `motion-defs/<model>.py` 里写关键帧 → `gen_motions.py` → `validate_motions.py`（应打印 OK）→ `verify_browser.sh`（需要 Chrome 截峰值姿势）· **有用**——这套「先分析再写」的顺序，比手工猜参数 ID 稳得多。

### B. AI / MCP 直接改模型（另一条不买 Editor 的路）

- [StandRig：MCP 可编辑的 2D 建模内核 + 可嵌入运行时](https://github.com/sayaka-aiart/StandRig) — GitHub · 创建 **2026-09-09** / 推送 **2026-09-13**；★82 · **Apache-2.0** · 读入**已分部件的 PSD**，让 MCP 客户端（Claude Code / Codex 等）通过 MCP 或 HTTP 编辑 mesh/deformer/keyform，再用数值参数驱动；自带浏览器播放页（透明、可作 OBS 浏览器源）；开发者初期版 **0.2.0**；README 明说：**「只读 PSD 不会自动有完整动作，需要向 AI 下指示」**，且**本体不做 cmo3/moc3 的生成、转换、播放** · **参考（有限有用）**——优点是完全绕开 moc3 二进制因此**没有反向工程的法务问题**；缺点是对本场景**不能直接产出 Ren'Py 能吃的 moc3**，只能做前期原型。环境要求：Node.js 22.12+ 或 24+，作者在 Windows / Node 24 上验证过。
- [StandRig Connect：摄像头追踪 + Windows 独立播放](https://github.com/sayaka-aiart/StandRig) — 同上仓 README 表 · 同上 · 另一个独立 app，做脸/眼/视点/口的追踪与校准、**可脱离浏览器和本体在 Windows 上单独绘制**、`ローカル HTTP` 的外部参数 API（可查看清单/值域、临时覆写、解除）、model slot 保存 · **参考**——这套生态看着完整，但产出仍是自有 JSON，进不了 Ren'Py。
- [Cubism API Bridge：Cubism Editor External API 的非官方桥](https://github.com/sayaka-aiart/cubism-api-bridge) — GitHub · 创建 **2026-09-10** / 推送 **2026-09-12**；★11 · **MIT** · 把官方 **External API** 暴露给 TypeScript / Python / 本地 HTTP（可与 StandRig 联动，也可独立用）；README 标明**验证对象是 Cubism Editor 5.4 alpha2 / External API 1.1.0**；共调查了 56 个 API，HTTP/Python 侧公开 47 个常规操作，并**诚实声明「全部项目的实机验证尚未完成」**（另附 `docs/alpha2-api-matrix.md` 验证矩阵）· **参考**——目前依赖 5.4 alpha（不可商用），且官方 External API 还是 alpha，两份 alpha 叠着，今天不能用于商业工程；但它证明「用外部程序读/写 Editor 的参数」这条路是通的。

### C. 直接从画切片一路到模型（含法务红线）

- [image2live2d：从分层画到可以动的 rig（自动绑这里）](https://github.com/Wzhang3912/image2live2d) — GitHub · 创建 **2026-07-10** / 推送 **2026-09-07**；★43 · **Apache-2.0** · Python 3.10+；输入**已分层的画**（`{order}_{role}.png` 目录/zip，或 PSD），全自动出 mesh、deformer、物理、动作，可导出三种标的：**nijilive `.inp`（主力，完全验证）/ Live2D `.moc3` 全套（moc3+model3+physics3+motion3+cdi3）/ `.cmo3`（可在 Editor 里改的工程）**；仓内有 `moc3_binary.py` `moc3_emit.py` `cmo3/caff.py` `cmo3/model_xml.py` 与对应测试，以及 `tools/moc3_render.py` 用于渲染校验 · **⚠️ 有用但有硬红线**——技术上是本轮最有冲击力的一个（真能不装 Editor 产出 moc3），**但作者自己写了那句话：「剩下的门槛是法务（Live2D 的 SDK license），不是技术」**；且官方 Free Material License Agreement §4.1.3 禁止反向工程。第一款商业作品**不建议**把产线建在这上面；做原型/做 nijilive 靶子则没问题。详见文末 §1。
- [live2d-from-art：artwork → Live2D 的 Agent Skill（含第三方 MIT `py-moc3` 序列化器）](https://github.com/fifteen42/live2d-from-art) — GitHub · 创建 **2026-09-15** / 推送 **2026-09-15**；★11 · **仓库本身没有声明开源许可证（NOASSERTION）**，内含的 `py-moc3` 是第三方 MIT · 一套分阶段 skill（`SKILL.md` + references + scripts），做 faithful layer separation、隐藏区域修补、**代码直接写 MOC3**、浏览器预览、音频驱动嘴部；`scripts/check_runtime.py` 只做 manifest 检查（「不校验二进制有效性与美观」）· **⚠️ 参考，不建议商用**——优点是它把失败边界写得很清楚（包含`.cmo3` 不生成、只支持浅转角不支持完整侧面、嘴部只跟音频振幅不跟音素、浏览器验证**不代表 VTube Studio 兼容**）；缺点是仓库无许可证、流程完全依赖 coding agent 执行、且项目很新（创建即最后推送，2026-09-15）。
- [官方创作者论坛：anysplit 团队问「拆图你最痛哪一步」](https://community.live2d.com/discussion/2381/quick-question-on-layer-prep-workflows) — Live2D 官方 Creators Forum · **2026-08-25**（帖子 JSON `DateInserted`）· 给出两个候选方向让建模者选：A = 细粒度边界识别（发丝/服饰/配件切成干净图层），B = 填充透明区与延伸遮挡区以便建 mesh · **参考**——体感上这就是目前 AI 拆图两条实际路线；两帖均 0 评论，说明**这条工具刚放出时社区反应很冷淡**，别据此调整自己的制作顺序。
- [同上团队的产品帖 anysplit](https://community.live2d.com/discussion/2379/seeking-feedback-on-layer-prep-tool-for-live2d-setup) — 同上 · **2026-08-06**（同法取得）· 明说目标是「帮 Live2D 画师省下**拆图层与补隐藏区域**的时间」，宣称 Smart Cutout + Inpainting 两个能力；0 评论、54 浏览 · **参考**——是 see-through 之外又一个同类的拆图/补画工具，但**无任何第三方验证**，别当结论。

### D. 排错 / 规范化（补一条交叉证据）

- [Unity URP 见轮廓不见纹理：官方 Discord 那边的答案回写到论坛（见 §二）](https://discussions.unity.com/t/imported-live2d-models-not-appearing-on-screen-using-cubism-sdk/1720986) — 已列于实战测评，强调它的**可复用排查顺序**——遇到「0 报错但渲染不对」时按：：确认 SRP、确认颜色空间、确认 Renderer Feature/List 已注册 · **有用**。
- [给 `exp3.json/pose3.json` 加 Version 字段（交叉引用）](https://github.com/Live2D/CubismSpecs/pull/7) — 已列于 §一 C；对写动作/表情工具的人来说，这条的意思是：**你生成的文件现在可以在官方格式里带上版本**，将来被旧工具吃掉时能自证清白。

### E. 本轮的「取不到 / 不采信」（诚实登记，下轮省时间）

- Reddit（r/Live2D、r/vtubertech、r/vtubers、r/gamedev）— 日期未核实（整站不可达）· `curl` 报 `Recv failure: Connection was reset` + `schannel TLS handshake failed`，**两条网络路径（curl 与 WebFetch）都失败**；搜索引擎 `site:` 定向也零结果 · **无效源**——v27 已记「抓取失败」，本轮换了三个入口（www JSON / old.reddit JSON / 带 `allowed_domains` 的 WebSearch）**依然不可达**，建议下一轮起把它当成结构性不可取（与 gamemale 同档），不再单独投入。
- itch.io — 不可用 · `curl` 超时（HTTP 000），两次不同 UA 重试均失败 · **本轮无效**——想找 Live2D 游戏的 devlog 只能另寻入口。
- Steam（steamcommunity 搜索接口 / 商店）— 不可用 · `HTTP 000` · **本轮无效**。
- note.com / Medium / YouTube — 不可用 · 三个域名 curl 均 `HTTP 000`，note.com 的 WebFetch 也返回 fetch failed · **本轮无效**——这意味着 v27 §3.6 留下的那批 note/Zenn 未读条目本轮仍无法打开。
- [Stack Overflow：`live2d` 标签](https://api.stackexchange.com/2.3/search/advanced?q=live2d&site=stackoverflow) — 官方 API · 本轮实跑 · **`live2d` 标签本身不存在**；`search/advanced?q=live2d` 返回 6 条，其中唯一相关的是 2013 年的《How does live2d work?》 · **负结论（比 v27 更进一步）**——v27 只试了 tag 页，本轮用了 advanced search，**可以下结论：SO 不是 Live2D 的排错源**。
- [Godot 官方论坛](https://forum.godotengine.org/search.json?q=live2d) — Discourse JSON · 本轮实跑 · `live2d` 命中 3 个主题（最新的 2026-05-15 讲的是网格 UV，非 Live2D 专有）+ `cubism` 命中 1 个 2018 年的 · **负结论**——Godot 论坛对 Live2D 近乎真空；要找 Godot 侧排错应围着 `gd_cubism` 本身的 issue 区，不在论坛。

---

## 三到五条最值钱的发现

**1. 「官方样本模型能不能用于商业作品」——本轮从官方契约文本拿到了硬答案，并籍此更正一条广为流传的错误说法。**
Free Material License Agreement §2.1.3.1 写得很直白：一般用户 / 小规模事业者使用 Live2D Original Character 的目的「**无论商用还是非商用**」都行；§1.23 定义小规模事业者 = **最近年度营业额不足 1000 万日元的事业者，含个人**。契约全文**没有出现任何「必须持有 Cubism PRO license 才能商用样本模型」的条款**（本轮逐条读过）。反例也很明确：コラボレーションキャラクター（名執 尽、春傘 つみき）§2.1.4.1 写着一般用户仅限非商用。→ 对第一款商业 VN：**可以用 Haru / Epsilon / Kei 这类「Live2D 原创角色」做练习与早期验证，甚至直接发商业版**，只要 ① 遵守该角色的个别限制（ミアラ / 桃瀬ひより 完全不许改设计；にと 必须保持二头身等）② 在游戏说明栏标注官方要求的那个长句。**但这也解释了一件事**：多个二手教程（含本轮那份 dev.to 评测）说的「样本模型商用需要 Cubism Pro」是以讹传讹，请以官方契约为准。⚠️ 注意边界：这条只对**从 live2d.com 官方下载页取得的样本数据**成立；nizima LIVE / nizima ACTION 渠道发布的角色走各自的使用许可。

**2. 「Cubism 5 的 moc3 第三方库不吃」这个困扰了三轮的问题，现在有机理、有解法、有时间线了。**
机理来自 Purism Core 的 `COMPAT.md`：**不是 moc3 版本号在作怪，是 Core 的 ABI 版本**。v5 ABI 对应 Core 5.1（Editor 5.1 引入），v6 ABI 对应 Core 6.0（Editor 5.3 引入，官方承认「引入多个破坏性变更」）。VTube Studio / 老版 Ren'Py / gd_cubism 停在 v5，最新的 Ren'Py 已经是 v6。这也就解释了为什么 v27 §3.2 那个「看 moc3 第 5 字节」的技巧能work——字节版本与 ABI 阶段是同泵的。解法不再是朴素的「降到 Cubism 4.2 导出」，而是**选一个明确支持 R5/Core 6 的运行时**：网页端有 `pixi-live2d5`（要求 Core 6.0.1 + Pixi 8.19+，2026-10-05 仍在推）与 `easy-live2d v1.0.0`（2026-09-24，README 明写用 Web R5 官方 Core）两条 MIT 路径；本地 C API 端有 MIT 的 Purism Core 可选 v5/v6 ABI 构建。时间线也因此定下来：**5.4 仍是 alpha，alpha 到期日 2026-10-18，SDK 全线无 5-r.6 —— 现在唯一该用的编辑器版本还是 5.3.00（2026-01-20）。**

**3. 这个 tuber AI 政策终于核到了（v27 列为高优先级欠账），而且它对「AI 图做 Live2D」是有条件放行。**
nizima 的 AI 政策正文：禁止投稿/销售/交付「制作过程的全部或一部分使用了画像生成 AI 或类似技术的插画，**以及用这些插画做成的 Live2D 作品**」，**加笔修正、描摹、AI 补画物体**同样在禁止列。但例外条款明确写了两类不算：① 对原画中**已存在**的物体使用绘制工具内的自动上色/背景铺色等局部辅助功能；② **「Live2D Cubism Editor」中辅助 Live2D 制作的功能**——原文特别点名包括「動きの自動生成機能」，理由是与画像生成 AI 的「学习目的、学习过程、目的均不同」。→ 结论：**放在商业出版这个前提下，Safe 的做法还是「人画 + 官方 PS 插件/自动补间辅助」；「AI 生成立绘 → 模型 → 上架」这条线在 nizima 一票否决**（别的平台上架规则不同，本轮未核）。顺带把 v27 的第二个欠账也结了：官方 AI 研究政策最后一次更新是 **2022-04-25**，研究范围明确包含「AI 辅助面部动作自动生成（XY 与四个角）」「辅助素材分け的线延长/涂广」「提升 mesh 自动生成精度」，并明确写「**不做从零生成插画、不做从插画全自动建模**」。

**4. 「不买 Editor 也能改动作」在 2026 年从尝鲜变成了可用工程：feature-complete 程度超出预期。**
`live2d-add-motion-sample-web-ui`（★194，MIT，仅依赖 Python 3 标准库，2026-10-08 仍在推）把这件事做成了流水线：分析模型的可用参数与值域 → 写关键帧定义 → 生成 → **独立校验器** → headless Chrome 截图验证。它写死了一条重要的经验规则：**物理驱动的参数不要直接给关键帧**。更关键的是它自带 `AGENTS.md`，让 Claude Code/Codex 这类 agent 能按规矩自动加动作——「不可用时不要硬来，要提出替代方案」这种约束被写进了流程。加上 v27 收的 `live2d-motion3`（Python 动作编辑器），**现在自己给自己角色加表情动作这件事，不需要五位数去买 Editor**。

**5. 被忽略的那条成本：模型文件是不可信输入。**
`moc3ingbird`（CVE-2023-27566，★98，2026-06-06 仍在推）说明 Cubism Core 对 MOC3 内的偏移不做边界检查，能越界读写；作者自称尚未实现纯 Core 下的 RCE，但明确说「几乎可以确定可行」。`pixi-live2d5` README 也专门加了「Model asset trust」一节：不沙箱、不限制资源规模、不控制压缩包展开。→ **第一款商业 VN 若只加载自己做的模型，这条与你无关；但只要计划支持玩家导入/UGC，这就是一个必须做预算与校验的工程项**（至少用上 `checkMocConsistency` + 自己的资源上限）。

---

## AI 相关的可直接落地的改动建议

> 判定原则：每一条我都读了原文（README / EULA 正文 / dev.to 全文），只采纳能当场验证的改动；不能直接用的写清为什么。

**✅ 采纳 1：给自己角色的模型加表情动作，走 `live2d-add-motion-sample-web-ui`，不要买家 Engine Editor。**
- 改什么：用这个仓库替换掉「打算为了做几个表情去买 Cubism PRO」这一步。它对已有模型**只在 `.motion3.json` 层面加动作**，产出的是纯 JSON + 既定参数，与 moc3 读者无关——所以**它天然绕开了 v27 那条「Cubism 5 的 moc3 第三方不吃」的坑**，这一点是本它与 v27 收的 `live2d-motion3` 共同的优势。
- 怎么改：① 官方样本页下载一个urfaces model 放到仓要求的目录（注意上文 D 段的个别限制，样本角色仅供流程验证，上线换成你自己的角色模型）；② `python3 tools/analyze_model.py` 导出可用参数、安全值域、**并看清楚哪些参数是物理驱动的（这些不要写关键帧）**；③ 在 `motion-defs/<model>.py` 里写高兴/点头/惊讶/害羞等关键帧；④ `gen_motions.py` → `validate_motions.py`（必须打印 OK）→ 浏览器看结果；⑤ 把生成的 `.motion3.json` 挂进你的游戏工程。
- 怎么验证：`validate_motions.py` 输出 OK 只是第一步，**真正的验证是 `tools/verify_browser.sh`（需本机 Chrome）截出的峰值姿势与你的预期一致**；再加第三步——把同一份 `.motion3.json` 拷回你的实际运行环境播一遍，确认参数 ID 完全对标。若你的运行环境读不动该文件，问题一定出在参数 ID 或 lied the line 版本，而不是这份 JSON 本身。

**✅ 采纳 2：如果做网页版试玩页，把运行时换成 `pixi-live2d5`（或 easy-live2d v1.0.0），并把「Core + 13 个 GLSL」纳入构建步骤。**
- 改什么：`pixi-live2d5` 的 README 要求 **Core 6.0.1 + `public/cubism5/shaders/` 下 13 个 GLSL 在运行时被serve**，且安装顺序是 `bun install --ignore-scripts` → `bun run setup`（下载 Core）→ `bun run prepare`（`prepare` 依赖 Core 先到位）。**不要照搬 pixi-live2d-display 的旧习惯按 `--scripts` 正常装**——那是它唯一容易踩的安装坑，README 专门解释了原因。
- 怎么验证：起它的 playground，用 **Ren Foster**（官方样本页明确标注为「学习 Cubism 5.3 新绘制功能」的模型）而不是 Hiyori——因为这个 map 就是要验证 5.3/6.0 路径；模型能动 + 头部能转 + 头发物理生效 = Core/Web SDK/shader 三者版本统一，此时才有意义去谈性能。

**✅ 采纳 3（小规模）：抄 Open-LLM-VTuber 的「情感标签 → 表情索引」模式，但不要抄它整个项目。**
- 改什么：该评测文给出的做法很小但很实用——让 LLM 在输出里内联情感标签（`[joy]` `[neutral]` `[surprise]`…），用一个正则在流式输出里抽出来，通过 WebSocket 推到 Live2D 的表情参数；`model_dict.json` 里一张 `emotionMap` 把标签映射到模型的 expression index。这个模式**与是否用 Open-LLM-VTuber 完全无关**，几十行就能复制。
- 怎么验证：先用固定文本（不接 LLM）触发一次，确认某标签确实把expression index 推对了，再接真正的流式输出。
- **为什么不建议直接上 Open-LLM-VTuber**-reason the 是聊天/伴侣形态，不是 VN 形态；而且仓库最近推送停在 **2026-05-15**、**GitHub license 字段是 NOASSERTION（与评测文声称的 MIT 不符）**、v2 重写期的风控也没有时间表。第一款商业作品不适合堆在它上面。

**❌ 不采纳：`image2live2d` 的 moc3 直写 —— 技术可行，但第一款商业 VN 不该建在这上面。**
- 读到的原文：它的输出表确实写着 `.moc3` 全套可用、`.moc3` codec 是「完全逆向生成，与 5 个官方 v3 模型 byte-for-byte 验证」，同时 `--live2d` **默认只写开放的 JSON 兄弟文件**，作者原话：写封闭的 `.moc3` 二进制是显式 opt-in，**「剩下的门槛是法务（Live2D 的 SDK license），不是技术」**。
- 为什么否：你需要发的是商业作品，上线后没法回滚。官方 Free Material License Agreement §4.1.3 明确禁止反向工程；而这个 « less-than-two-month-old » 项目（创建 2026-07-10）没有成为行业共识，也没有 License-level 的背书。**给「原型/评估」用可以（比如先出 `.inp` 看），给要上架的心服产品用不行。**

**❌ 不采纳：`StandRig` / `Cubism API Bridge` 作为当前产线。**
- 读到的原文：StandRig 0.2.0 是开发者初期版，**本体明确「不做 cmo3/moc3 的生成、转换、播放」**，产出是自有 JSON + 自有浏览器运行时，走不进 Ren'Py；`Cubism API Bridge` 的依赖明确写着 **Cubism Editor 5.4 alpha2 / External API 1.1.0**，而 5.4 alpha 官方原话是「请勿销售或分发」、「不保证向 beta/release 迁移」。两份 alpha 叠加。
- 为什么不推荐：它们代表的是「未来的形状」（脚本化/agent 化建模），但今天**既不能产出可上架的模型，也不被alpha 条款允许用于商业产出**。值得按季度复看一次，不作为本轮改动。

**⚠️ 顺带修正一条二手说法（见「最值钱发现」第 1 条）**：多份教程（含本轮那份 dev.to 评测）称「样本模型商用需要 Cubism Pro license」。官方 EULA 全文里没有这条要求；§2.1.3.1 反而明确允许一般用户/小规模事业者商用 Live2D 原创角色。**以官方契约为准**，二手说法不要直接写进索引或采购决策。
