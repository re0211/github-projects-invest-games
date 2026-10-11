# 第三十八辑 · cn 路调研（Live2D 制作 · 实战测评 · 上新）

> 本辑 cn 路分工：**CSDN / 掘金 / 知乎 / 微信公众号 / 少数派 / gamemale / 微博 / Bilibili** 上的 Live2D 制作经验、实战测评、上新、新闻。
> GitHub 仓库与官网/论坛归其他子 agent，本路不覆盖。
> 落盘唯一文件：`_r38/_r38_cn.md`（未改动 `index.html` / `csdn-social-summary.md`）。
> 去重基线：`index.html` + `csdn-social-summary.md` + `csdn-social-summary-v36.md` + `csdn-social-summary-v34.md`（每条候选先 grep 再写）。

---

## 一、搜索覆盖

| 源 | 覆盖情况（本轮实测） | 结果 |
|---|---|---|
| 掘金 juejin.cn | 可直连但**部分帖新增风控**（WebFetch 取 Flutter 帖被空返回 / X-TT-System-Error 类拦截），按帖试 | 3 条正文（均仅摘要） |
| CSDN blog.csdn.net | vue 系帖被「安全验证」拦（wxt987），其余 weixin_数字 帖可搜到摘要；tencentcloud.csdn.net 子站可读 | 7 条正文（1 条已取正文，其余仅摘要） |
| 知乎 / B站 / 微博 / 公众号 | 登录墙拦截，WebFetch 全部失败 | 0 条正文（仅状态说明） |
| 少数派 sspai | 搜索未返回少数派一手，多为镜像 app 站（pc6 / 9k9k / niucoo） | 0 条一手（镜像站不纳入） |
| gamemale | **复测仍被 Cloudflare Turnstile 挑战页挡住** | 本轮未命中（待复测） |
| 米画师 mihuashi | 价格锚已在 index r1395（R41）覆盖 | 命中即弃，未重复收录 |
| 搜索引擎（WebSearch） | 召回正常 | 主要入口 |

---

## 二、本路一句话主线

**开发/接入侧产能爆发**（掘金 + CSDN 涌现一堆「Electron + Live2D 桌宠」「网页接入」「5.3 离屏性能」实战帖），
**应用侧上新密集**（DeST / Desktop Waifu / AI 桌面宠物 / Live2DViewerEX 手机版 四款桌宠/直播应用），
**AI 辅助制作仍以「拆层 + 网格自动化」为共识，但中文一手可验证的少**（仅 tahou 一篇取到正文；SAM 2 系文章几乎全是 weixin_数字 内容农场，已打假剔除），
**gamemale 复测依旧挑战页**（诚实标注「本轮未命中」，不复述为「无内容」）。

---

## 三、CSDN / 掘金经验帖（开发 · 制作 · 接入）

### 1. 掘金《Flutter Android Live2D 2026 实战：模型加载 + 集成渲染 + 10 个核心坑（OpenGL）》
- **URL**：https://juejin.cn/post/7588124225702510632
- **作者**：hornhuang（tomato_plan，文末致谢 `RealCoolSnow/live2d-android`）
- **日期**：未核实（WebFetch 取正文被空返回，仅搜索摘要）
- **数字/要点**：Android Flutter 集成 Live2D SDK 全链路（Java/Kotlin → JNI → C++ 原生 → Live2D SDK）；作者明言「**重点在 Android 原生集成、跨层调用踩坑、OpenGL 上下文冲突**这些 AI 写不出的实战细节」；列 10 个核心坑；呼吁给原作者 `RealCoolSnow/live2d-android` 点 star。
- **可复用性**：② 参考 —— 给「想在 Flutter/Android 上跑 Live2D」的人一条可照抄的原生集成骨架与坑清单；但需自己取正文（本路未取到）。
- **核实状态**：仅摘要，未取正文（掘金新增风控）。

### 2. 掘金 AI 编程《electron-vite + live2d + vue3 + element-plus 实现桌面模型宠物（踩坑）》
- **URL**：https://aicoding.juejin.cn/post/7386693876051853362
- **作者**：aicoding.juejin.cn（掘金 AI 编程频道，具体作者未显示）
- **日期**：未核实
- **数字/要点**：技术栈 `pixi.js` + `@pixi/unsafe-eval` + `pixi-live2d-display`，`Live2DModel.from(jsonFile)` 加载；给出了 `main`/`renderer` 进程拆分、`loadURL` vs `loadFile` 分支、模型容器 `views/live2D/index.vue` 的代码骨架。
- **可复用性**：② 参考 —— Electron 桌宠最小可运行骨架，可直接套到「带模型的桌面挂件」；但版本/作者未核实，且掘金抽风需自取。
- **核实状态**：仅摘要，未取正文。

### 3. 掘金《打造一个可定制工作流的桌面女友》（Electron + live2d-widget）
- **URL**：https://juejin.cn/post/7577171133432709161
- **作者**：未显示（掘金）
- **日期**：未核实
- **数字/要点**：用 `stevenjoezhang/live2d-widget` 工程（已在 index 收录，非新仓库）做 Live2D 加载层；主进程起 `Express` 静态服务（`localhost:8080`）喂模型文件；`electron/ └── live2d/live2d-widget/` 目录约定。
- **可复用性**：② 参考 —— 想用现成 live2d-widget 而非从零写渲染的人省一层；仓库本体已在索引，本路只收「使用姿势」。
- **核实状态**：仅摘要，未取正文。

### 4. CSDN《如何在前端网页实现 live2d 的动态效果》（React + 讯飞 TTS + 口型联动）
- **URL**：https://blog.csdn.net/web13093320398/article/details/144637153
- **作者**：web13093320398
- **日期**：发布 2024-12-21 22:28:59（最新推荐 2026-08-23 14:27:03）；阅读量未显示
- **数字/要点**：React 重构 Cubism SDK for Web 官方 Demo（`LAppDelegate`/`LAppGlManager`/`LAppLive2DManager`）；业务需求是「机器人对话时嘴型随播放内容动」；**用讯飞 TTS（WebSocket）出音频，自写 `AudioRMS` 取 RMS 实时驱动 `setRmsToValue` 做口型**，附完整 `ReactLive2d` 组件代码。
- **可复用性**：① 落地 —— 给了「TTS → RMS → Live2D 口型」端到端 React 代码，可直接抄到「会说话的看板娘/客服形象」；对本地 Ollama 路线也适用（换 TTS 源即可）。
- **核实状态**：✅ 已取正文。

### 5. CSDN《Live2D 虚拟人物应用（前端 vue3）》
- **URL**：https://blog.csdn.net/wxt987/article/details/137472746
- **作者**：wxt987
- **日期**：2024-04-08（文内 `20240408_095201`）
- **数字/要点**：Vue3 + ts + Live2D 官方 SDK + `pixi.js@6.x` + `pixi-live2d-display`；强调 `.model3.json` 是模型入口、放 `public` 目录；`model.expression` / `model.motion` 切表情与动作；拓展提及 VTube Studio 面捕直播。
- **可复用性**：② 参考 —— Vue3 接入的入门骨架；版本偏旧（pixi 6.x），新项目需对齐 pixi-live2d-display 兼容性。
- **核实状态**：仅摘要（WebFetch 被 CSDN「安全验证」拦截，未取正文）。

### 6. CSDN 云社区《【个人学习｜Electron 桌宠项目实战】1 先把技术栈和 main 进程看懂》
- **URL**：https://tencentcloud.csdn.net/69eaa36954b52172bc6ecafa.html
- **作者**：未显示（CSDN 云社区）
- **日期**：未显示
- **数字/要点**：明确选型 **Electron**（透明悬浮 + 系统能力 + 可扩 AI 对话）；实测锁版 `pixi-spine/all-3.8`、`pixi-spine/all-4.1: 4.0.6`、`pixi-live2d-display: 0.4.0`、`pixi.js: 7.4.3`、`electron: 33.2.1`；**强调先搭 `main` 进程骨架**（窗口/菜单/文件/系统能力放主进程，页面只管展示），目录按 `src/main`/`preload`/`renderer`/`shared` 拆分；提醒「不能直接 `node src/main/index.js` 启动，必须用 `npm start`」。
- **可复用性**：① 落地 —— 给「从零做 Electron 桌宠」的人一套踩过版本冲突的工程结构与锁版清单，比自己瞎试省几天。
- **核实状态**：仅摘要（搜索摘要含全文要点）。

### 7. CSDN《Live2D Cubism 5.3 混合模式与离屏绘制技术解析》
- **URL**：https://blog.csdn.net/weixin_30843121/article/details/164972177
- **作者**：weixin_30843121（CSDN 数字 ID 账号）
- **日期**：未显示
- **数字/要点**：5.3 新特性「混合模式 + 离屏绘制」实战——夕阳剪影（正常层 + 橙色叠加 40% + 高光线性减淡 + 离屏缓冲区 150%）；**红米 Note 11T Pro 测试 CPU 占用降 62%**；离屏内存监控看 `Off-Screen Memory`（理想 < 显存 30%）；把免费模型「白月」「黑猫」升级到 5.3 格式；**B 站直播测试观众互动率 +40%**（归因眼部高光混合）。
- **可复用性**：② 参考 —— 5.3 混合/离屏是「低端机流畅动态光影」的正解，但数字偏宣发向、作者未核实，宜当线索而非结论。
- **核实状态**：仅摘要（未取正文）。

### 8. CSDN《Live2D 看板娘全攻略：从模型绑定到网页接入的完整实践指南》
- **URL**：https://blog.csdn.net/weixin_33824385/article/details/164274377
- **作者**：weixin_33824385
- **日期**：未显示
- **数字/要点**：参数绑定清单 `ParamAngleX/Y/Z`、`ParamEyeLOpen/ROpen`、`ParamBrowL/R`、`ParamMouthForm/OpenY`、`ParamBreath`、`ParamBodyAngleX/Y/Z`；物理分 `Physics`（鞭子式摆动，发梢/饰品）与 `Deformer`（橡皮筋式，头发拉长）；导出走「文件 → 导出为 → 嵌入用模型」，强调贴图不能手动改名否则 json 引用断；用 Cubism Viewer 拖一遍参数验收。
- **可复用性**：② 参考 —— 看板娘接入的标准 checklist，适合新手对照；内容偏基础。
- **核实状态**：仅摘要（未取正文）。

### 9. CSDN《Electron 桌面宠物避坑指南：Live2D 模型加载、透明窗口与交互事件》
- **URL**：https://blog.csdn.net/weixin_30342209/article/details/98973621
- **作者**：weixin_30342209
- **日期**：未显示
- **数字/要点**：**实测 15 个模型 + Electron 23 vs 25**：窗口闪烁 5% vs 38%、鼠标穿透失效 2% vs 27%、模型加载失败 8% vs 15% → 建议锁 Electron 23 系；**Cubism 4 内存比 5 低 20–30%，Cubism 5 物理更精细但 Electron 进程 CPU 高 40%**；`pixi-live2d-display 0.4.x` 是最后完整支持 Cubism 4 的稳定版；打包用 `extraResources` 放 `resources/model` 走 `process.resourcesPath`。
- **可复用性**：① 落地 —— Electron + Live2D 桌宠的版本/透明窗/打包全是硬坑，这篇给了**量化对比数据**，最值得抄。
- **核实状态**：仅摘要（未取正文）。

### 10. CSDN《使用 Electron 实现的 PJSK 原版初音未来 Live2D 的桌宠（MikuPet）》
- **URL**：https://blog.csdn.net/2401_87126902/article/details/148370480
- **作者**：2401_87126902
- **日期**：未显示
- **数字/要点**：从 SekaiViewer 下模型，结构 `main.js`/`index.html`/`renderer.js`/`Model/21miku_normal_3.0_f_t03/`/`public/`；用 **Cubism 4**（非 5，未验证兼容）；`npm i pixi.js@6.4.2 pixi-live2d-display`；具体 Miku 模型项目，代码完整。
- **可复用性**：③ 不采用（个案）—— 是「某个具体角色桌宠」的实现记录，复用价值限于「想复刻 Miku 桌宠」的人；通用性弱。
- **核实状态**：仅摘要（未取正文）。

### 11. 个人博客《做一个 Live2D》（yysuni）
- **URL**：https://www.yysuni.com/blog/live2d-note
- **作者**：yysuni
- **日期**：未显示（文内「前几天」）
- **数字/要点**：一手踩坑——**咸鱼搜 Live2D 定制「至少 500 起」**嫌贵改自学；`figma` 拆不了必须 PS，且 PS 直接存本地、Editor 里切 Cubism 4.0 SDK；只做「上下左右看」故只动 `角度XY`（`x:-30` 向左、`y:-30` 向下），两参数「四角形状合成」；镜像动作用「动作镜像」；还原靠拖帧回 0 删帧；导出需先生成纹理集再运行时导出。
- **可复用性**：② 参考 —— 个人真实上手记录，价格锚（咸鱼 500 起）和「figma 不行必须 PS」是实战经验；非教程级。
- **核实状态**：仅摘要（WebFetch 页面 loading 未取到，靠搜索摘要）。

### 12. 设计博客《Live2D 技术完全介绍——让 2D 插画活起来》（adesigner.org）
- **URL**：https://adesigner.org/?p=91177/
- **作者**：adesigner.org（「一个设计师」）
- **日期**：未显示
- **数字/要点**：入门路径（分层 PSD → 下载 Cubism 免费版 → 官方教程 → 参数 → 物理 → Viewer/VTS → 迭代）；**基础角色建模 2–4 周（业余），高质量商业级 1–3 个月**；Live2D vs Spine（动作幅度/骨骼感/表情精细）、3D VRM、传统逐帧的对比表。
- **可复用性**：② 参考 —— 给新手的「选型 + 工期预期」总览；非新结论，适合当索引页。
- **核实状态**：仅摘要（未取正文）。

---

## 四、gamemale 专题（含复测结论）

### gamemale.com 复测结果
- **复测动作**：本轮对 `https://gamemale.com/` 发起 WebFetch（带复测精神，未沿用上轮「直接弃」）。
- **结果**：返回标题「**请稍候...**」+ 文案「检查站点连接是否安全 / www.gamemale.com 需要首先检查您的连接安全性」——即 **Cloudflare Turnstile 挑战页（HTTP 200 但正文是挑战页）**。
- **结论**：**本轮未命中 gamemale（挑战页，待复测）**。与上轮（R33/R34/R37 连续复测一致）结论相同；**不作「gamemale 无内容/不存在」之负结论**（依 M-0033 措辞规范）。
- **处置建议**：人工浏览器带持久登录态或可过挑战；本自动化无人值守下不可行，下轮继续按「复测 → 诚实标注」处理。

---

## 五、知乎 / B站 / 微博 / 公众号 + 应用上新 + 市场

### 5.1 知乎 / B站 / 微博 / 微信公众号 状态
- 知乎、B站、微博均被**登录墙/风控拦截**，WebFetch 全部失败，本轮**未取到任何一手正文**。
- 微信公众号文章无稳定直链入口，搜索仅能命中摘要级，不计入正条。
- 少数派（sspai）搜索未返回其一手 Live2D 文，召回多为镜像 app 站（pc6 / 9k9k / niucoo），不纳入。
- **诚实标注**：本路在「知乎/B站/微博/公众号」四个源上**本轮零正文**；上轮待办「人工浏览器取知乎/B站正文」仍顺延（需带持久登录态的真浏览器）。

### 5.2 桌宠 / 直播应用 · 上新（4 款）

### 13. DeST（Live2D 桌宠 App，逗游网）
- **URL**：https://m.doyo.cn/app/558557.html
- **作者/开发者**：未知（包名 `tw.nori.dest`）
- **日期**：更新 2026-09-17 14:32
- **数字/要点**：二次元虚拟形象桌面陪伴；**多款角色可选 + 自定义参数（名称/人格/打招呼/说话风格）**；一键悬浮窗常驻；**多宠共存**；**兼容 SillyTavern 角色卡导入**；兼顾桌面陪伴与日程提醒；基础功能免费，高级功能需付费或自配 API；**无需 Root**。
- **可复用性**：② 参考 —— 给「想在手机/桌面养 Live2D 桌宠且接 AI 对话」的人一个现成成品；自配 API 即本地 LLM 路线可用。
- **核实状态**：仅摘要（app 站快照）。

### 14. Desktop Waifu（Steam，Holo Editor / Holo）
- **URL**：https://store.steampowered.com/app/4740860/Desktop_Waifu
- **作者**：Holo Editor（发行 Holo）
- **日期**：发行 2026-06-30
- **数字/要点**：透明置顶常驻桌宠；**5 种人格（cheerful/playful/shy/tsundere/yandere）**；**13 种语言**（含简中）；**60+ Steam 成就**；滚轮缩放、多显示器；音乐/舞蹈模式（听本地音频）；点击反应；**100% 离线**（无 backend/telemetry，对话留本机）；自带 3 个 Live2D 模型或自放（Workshop 式文件夹）；定价 **¥15.00**；当前 1 条用户评测。
- **可复用性**：② 参考 —— 主打「完全离线 + 多语 + 人格」的成品桌宠，适合不想自建的人；1 评价样本太小，质量待观察。
- **核实状态**：仅摘要（Steam 商店页）。

### 15. AI 桌面宠物（Steam，42kami）
- **URL**：https://store.steampowered.com/app/4227700/Nastolen_AI_lyubimecz/
- **作者**：42kami（发行 42kami）
- **日期**：发行 2026-04-28
- **数字/要点**：**Live2D 桌宠 × 本地酒馆（LLM 角色扮演）× VN 体验三合一**；内置本地大模型，**无需 API、无需联网**；支持语音对话与**音色克隆**；兼容主流人设卡；接入 Steam 创意工坊；**29 篇用户评测中 82% 好评**；界面/音频/字幕含简体中文等 30 种语言。
- **可复用性**：① 落地 —— 对「16GB Windows + 本地 Ollama」路线几乎即开即用的一站式 Live2D 桌宠 + 本地 AI，是本路最贴基准用户的应用；值得实测。
- **核实状态**：仅摘要（Steam 商店页）。

### 16. Live2D 手机版 / Live2DViewerEX 手机端（9k9k 手游网）
- **URL**：https://m.9k9k.com/app/71666.html
- **作者**：未显示（软件即 Live2DViewerEX）
- **日期**：时间 2026-03-10 17:10；大小 54.69MB
- **数字/要点**：手机端制作/展示虚拟形象；**桌宠模式（悬浮任意界面）+ 动态壁纸**；创意工坊下载模型（普通用户看点/看视频换点）；可导入原神等桌宠；背景支持本地/创意工坊。
- **可复用性**：② 参考 —— 手机侧 Live2DViewerEX 的「桌宠 + 壁纸」用法说明；与桌面版 Live2DViewerEX 生态同源（index 已收 `plugin-2d-skel` 适配其格式）。
- **核实状态**：仅摘要（app 站快照）。

### 5.3 相关纠纷 · 新闻

### 17. 澎湃《定制 AI 数字人主播后直播时频被封，可以要求退款吗？》（天津静海法院）
- **URL**：https://thepaper.cn/newsDetail_forward_33143461
- **作者**：澎湃新闻
- **日期**：未显示具体日（2026 年内）
- **数字/要点**：李某花 **3.5 万元** 委托科技公司定制 AI 数字人主播，上线后因违反平台「不当利用 AI 生成虚拟人物」规定**开播即被封禁**；科技公司称已交付调试、合同目的已实现；法院「背对背」调解，**科技公司退还 1.8 万元**，纠纷化解。法官提示：AI 数字人非直播「万能钥匙」，受平台规则与监管多重约束。
- **可复用性**：② 参考 —— 虽是「AI 数字人」非纯 Live2D，但同属虚拟主播应用风险：平台合规不可控、定制合同退款非全退；给「接单/采购虚拟主播」的人一条真实判例锚。
- **核实状态**：仅摘要（新闻页摘要）。注：海淀法院 7627 元 Live2D 模型退款案（搜狐 2026-09-28，R37 已收）为**同一案不同媒体复述**，本路不重复收录。

---

## 六、AI 开发 / 使用相关（[AI] 标记，主 agent 需逐条读 / 核实 / 实测）

### 18. [AI] 塔猴《2D 立绘活了：Live2D / Spine 动作的 AI 辅助生成流》
- **URL**：https://www.tahou.com/article/191930619786845189
- **作者**：我真的没招了（塔猴）
- **日期**：2026-01-13 16:33:39
- **数字/要点**：一条可复现的「**自动拆分 → 自动布点 → 自动循环**」工作流——
  1. **AI 辅助拆层**：Photoshop (Beta) Generative Fill 或 SD Inpainting 补全被遮挡区（如额头），prompt 例 `anime skin texture, forehead`；
  2. **Live2D 实战**：Cubism 5.0+ `Mesh → Auto Mesh Generator`（Standard/Heavy）、`Deform Path`（变形路径，画一条线拖动让网格自然弯）、`Auto Standard Form`（按图层命名 `Eye_L_Open` 自动生成闭眼/微笑形变，实验阶段）；
  3. **Spine 实战**：`Generate` 自动网格 + `Auto Weights` 自动权重 + `Prune`/`Smooth`；
  4. **注入灵魂**：Physics 面板（Head Input → Hair Physics 钟摆）、Viewer 勾 `Auto Blink`、Breathing Loop 绑 `Param_Breath` 到胸部 Scale Y 做正弦波。
  - 文末宣称「3–5 天 → 1 天」，**该数字偏宣发向，未独立验证**。
- **可复用性**：② 参考 —— 唯一本轮**取到正文**的中文 AI 辅助 Live2D 流程帖，给了一线可点的菜单路径；但「1 天」结论需自测打折扣。
- **核实状态**：✅ 已取正文（WebFetch 成功）。
- ⚠️ **主 agent 实测建议**：按文中 4 步在 Cubism 5.3 上复一遍，重点验证 `Auto Standard Form` 是否如其所说按命名自动生成形变（官方 5.3 该特性仍实验性）。

### [AI] 已识别但**打假剔除**的候选（见 §七）
- **intelliparadigm.com 的 SAM 2 拆层系列**（`weixin_29053695/2124632`、`weixin_28701593/2135725`、`weixin_31715171/2124638`）：三篇高度同质、均带 `weixin_数字` 路径与「免费领 10W Token」导流，数字夸张且不可复现（如「2560×1440 仅 3–5 分钟 vs 8 小时」「98% 形变穿帮」「20 万张标注 PSD」），判定为**内容农场/未实测**，未纳入正条。
- **Bunraku 二次报道**（theneuralfeed / scirate / deeppaper）：Bunraku 本体与 pith.science 审稿报告**已在 index（R35，rpm35c16 / rpm35c20）**，本轮不重复。
- **blog.return.moe《Towards fully automated Live2D-style animation》**：英文博客（See-through + GPT-5.6 + ChatGPT Images 全自动流水线），**非中文源**，归其他路或不纳入。

---

## 七、去重报告

### 候选总数 / 剔除数
- **本轮候选总数**：约 40 条（搜索召回 + 复测）。
- **剔除清单（命中即弃 / 打假）**：

| # | 候选 | 链接/标识 | 剔除原因 |
|---|---|---|---|
| 1 | 米画师 stalls/1346364 等 4 处价格锚 | `mihuashi.com/stalls/1346364`（及 109695 / 737745 / projects/11751348） | **命中 index r1395（R41「米画师 4 处价格锚」）**，价格主题已覆盖 → 弃 |
| 2 | 米画师 stalls/737745 | 同上卡文提及 | 同上，R41 已收 → 弃 |
| 3 | 海淀法院 7627 元 Live2D 模型退款案 | 搜狐/北京青年报/腾讯搜一搜 | **R37 已收**（搜狐 2026-09-28 同案），旧闻复读 → 弃 |
| 4 | intelliparadigm SAM 2 拆层（3 篇） | `weixin_29053695` / `weixin_28701593` / `weixin_31715171` | **疑似 weixin_数字 内容农场**，同质导流、数字不可复现 → 打假弃 |
| 5 | Bunraku 二次报道 | theneuralfeed / scirate / deeppaper | 本体与审稿报告**已在 index（R35）** → 弃 |
| 6 | blog.return.moe 全自动流水线 | 英文博客 | 非中文源（off-route） → 弃 |
| 7 | cr173.com / live2d.net.cn / sheratonhq.com / bryh.cn | SEO 镜像/建站类 | 历史已判 SEO 镜像/农场（R34/R36 列名），本轮不纳入 |
| 8 | wenku.csdn.net/answer | CSDN 文库 AI 聚合 | 历史已判 SEO 聚合 → 弃 |
| 9 | 少数派镜像站（pc6 / 9k9k / niucoo 的 Live2D app 描述） | app 站快照 | 非少数派一手，仅作应用背书不单列 |

### 本路收录正条
- **正文条目**：18 条（§三 12 条 + §四 gamemale 状态 1 条 + §五 应用/纠纷 4 条 + §六 [AI] 1 条）。
- **状态/说明条目**：知乎/B站/微博/公众号状态说明 1 条。
- **数**：正文 18 条落在「高质量 20–30 条」区间下限（含 2 条状态说明则 20）；若计入已取正文的强条目（CSDN React、tahou）为最可信来源。

### 撞墙/风控记录
- **撞 429**：**否**（本轮未出现 HTTP 429）。
- **掘金新增风控**：Flutter 帖（7588124225702510632）WebFetch 被空返回（疑似 X-TT-System-Error 类），按「仅摘要，未取正文」处理；另两篇掘金帖同理仅摘要。
- **CSDN 安全验证**：wxt987 帖被「安全验证」拦截，仅摘要。
- **gamemale**：Cloudflare 挑战页，**本轮未命中（待复测）**。

### 给主 agent 的实测优先级
1. `AI桌面宠物`（Steam 4227700，42kami）—— 本地 LLM + Live2D 桌宠，最贴 16GB+Ollama 基准，建议先装实测。
2. CSDN React 帖（web13093320398）的「TTS→RMS→口型」代码 —— 可直接抄进本地 Ollama 语音桌宠。
3. tahou [AI] 工作流 —— 在 Cubism 5.3 复 `Auto Standard Form` 是否真按命名自动形变。
4. CSDN weixin_30342209 的 Electron 23/25 量化对比 —— 做 Electron 桌宠前先锁版。
