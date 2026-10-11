# 第三十一辑 · cn 路

> 调研主题：中文互联网上 Live2D **制作 / 绑定 / 物理 / 实战测评 / 上新** 的经验分享贴。
> 这是第 31 轮，与第 30 轮相隔约 20 分钟，增量稀薄，**宁可少而真**。
> 起始时间：2026-10-11。逐条追加，不攒稿。
> 方法沿用房规：**不用 `site:` 算子**，把站名当普通关键词丢进 WebSearch，命中后用 WebFetch 直取正文核实。
> **搜索覆盖表见文末**；去重基线为 `_r31/_dedupe_urls.txt`（475 条）+ `_r31/_dedupe_gh.txt`（1230 条）。

## 条目

### 1. 【LIVE2D-Vtuber】拆圖解說分享 · 身軀（含四肢）—— 妄想販售屋（mosouriya.com）/ 作者 sandy62407 / 日期未核实
- URL: https://www.mosouriya.com/post/live2d-vtuber-%E6%8B%86%E5%9C%96%E8%A7%A3%E8%AA%AA%E5%88%86%E4%BA%AB-%E8%BA%AB%E8%BB%80 （同系列「頭部」篇：https://www.mosouriya.com/post/%E3%80%90live2d-vtuber%E3%80%91%E9%A0%AD%E9%83%A8%E6%8B%86%E5%9C%96%E8%A7%A3%E8%AA%AA）
- 来源/日期: 妄想販售屋（繁中 VTuber 模型工作室博客）· 页面仅标「已更新：9月5日」，**未给年份 → 日期未核实**
- 一句话内容: 台湾模型工作室把「立绘怎么拆件」按部位写成可照抄清单——身躯拆**上半身/下半身**两块（让呼吸、前后倾、左右转体各自独立）、**背面图层不能省**（否则转身空洞发扁）、手拆**手臂+手掌**且**手背与手心/侧面必须分开**（翻转时才不出透视错）、脚拆**大腿/小腿/脚掌**且接缝要留足「出血范围」；所有**投影阴影必须独立图层并设「乘算」模式**（底层换色阴影仍对，建模时可整层绑到对应部件）；同系列「頭部」篇把头发拆成前发/侧发/长侧发（长侧发还要再分子件）/后发/头饰/亮部/阴影。
- 判定: ✅采纳。（**本轮最贴合「立绘拆分可执行教程」目标的一条**，且是少见的繁中、由接单工作室写的实操口径；「阴影独立层+乘算」「手背/手心分件」「出血范围」都是能直接落进你立绘规格书的判据。）

### 2. 米画师橱窗「（加塞）live2d立绘定制」—— 画师「且明」—— 米画师 / 截稿 2026-09-30
- URL: https://www.mihuashi.com/stalls/912393
- 来源/日期: 米画师（mihuashi.com）· 页面显示**截稿 2026-09-30 23:59**，未显示发布日（核实：WebFetch 成功取回正文）
- 一句话内容: 一份**可直接当接单/验收口径范本**的橱窗——底价 ¥18,000（加塞 ×1.5，标价 ¥18,950），**默认「商用使用权」，但明确「不可买断 / 不可二改 / 不可量贩转卖 / 严禁公皮售贩」**；加价项全部明码：头发换色 800~1500、换发型 1000~3000、兽耳 200~600、角 200~400、翅膀/尾巴 100~500、加手势 400~600、表情加 50/个（附赠 3 个）、整套换服 1000~8000、服装换色 800~1500、跟宠 1000~4000；并对「脚部姿势对称就只画一只鞋」这类细节给了计费口径；分阶段付款 **10% 定金→30% 线草→50% 色草→70% 精草→100% 成稿**。
- 判定: ✅采纳。（**你若不接单，价值在「授权边界 + 加价项 + 分期节点」这套可复制模板**；画师本人好评数 440、完成率 99%、准时率 97%，是一条可核实的真实橱窗而非行情截图。）

### 3. 「一般Live2D委託15000新台幣起，可接一條龍」—— 凌零依001 / Clibo 同人委託平台 / 刊登 2026-09-25、更新 2026-09-26
- URL: https://clibo.tw/commissions/NmVzvW
- 来源/日期: Clibo（台湾接案平台）· **刊登 2026-09-25 18:37，更新 2026-09-26 17:27**（核实：WebFetch 成功取回正文）
- 一句话内容: 把「一个基础 Live2D 模型到底包含什么」写成了验收清单——一般方案 NT$15,000+ 内含：**头部 X 轴约 30° / Y 轴约 15° / Z 轴约 10°、果冻眼、呼吸、一般头发物理、一般服装装饰物理、赠 3 个静态表情**；加购项明码：加表情 200NT、动画面部表情 300NT、服装穿脱 1000NT、加发型/加衣装 1000NT、加动作 500NT、吉祥物 2000NT、大小变 2000NT、**VBridger 口型 2000NT（吐舌/歪嘴/鼓嘴/嘟嘴/抿嘴/咀嚼）**；交付含 **VTube Studio 运作档 + 去背 PNG**，**含商业使用权、永久保固、修改不限次数**，付款分 5 段（确认拆分档后先付 50% 定金）；制作节点：确认拆分档→五官建模预览→头部预览→身体预览→交付并付尾款。
- 判定: ✅采纳。（与第 2 条互为「个人 vs 商业」「简版 vs 一条龍」两种报价口径；**「X轴30°/Y轴15°/Z轴10°」这组角度正是圈内判定「合格模型」的最低共识**，可以当你自检或外包验收的达标线。）

### 4. 米画师企划「live2d立绘精拆分用于建模」—— 米画师 / 发布于 2026-08-18、截稿 2026-08-28
- URL: https://www.mihuashi.com/projects/11730022
- 来源/日期: 米画师 · **搜索片段显示「发布于 2026-08-18 09:56:31 / 截稿 2026-08-28」**；⚠️ WebFetch 两次均**未取回正文（返回空）**，以下为检索片段，属**仅摘要级**
- 一句话内容: 从**甲方一侧**给出的「拆分需求书」样例——一张少女 Live2D 立绘，明确要拆：**一套衣服；三个表情；三个手势（拿扇子/拿话筒/捧着脸），其中「扇子」小物需拆、话筒不用；两种发型（刘海与头顶不变，只变双马尾/单马尾后发）**；单张稿酬 ¥150~250、平台手续费 5%、商业用途、按「草稿 20%→线稿 30%→上色 60%→确认收稿 100%」付保证金节点。
- 判定: 🔶观察。（**「哪些小物要拆、哪些不拆」「发型只变后发」这类需求描述模板很有参照价值**；但因正文未能亲手打开，日期与金额按房规降级为待核，只当线索不当结论。）

### 5. ABOUTCG 课程「从立绘到直播—零基础 live2d 虚拟主播实战案例教学」—— aboutcg.org / 讲师「李大文青」/ 日期未核实
- URL: https://www.aboutcg.org/courseDetails/2400/introduce
- 来源/日期: ABOUTCG 学院 · 页面**未显示开课日期 → 日期未核实**（核实：WebFetch 成功取回正文；页面标注总时长约 6.5 小时 / 390 分钟，学习热度 905）
- 一句话内容: 一份**可当自学路线图**的课程大纲（本身就是制作流程的分步结构）：第一章下载/拆分检查；**第二章「九轴制作」= 布点→参数→变形器→X 轴→Y 轴→四角合成→身体 XY**；第三章「五官与口型」= **胶水**(glue 权重)→眼眉→嘴→物理→头发物理→衣服物理→手臂物理→扭屁股物理；第四章表情动作 + **VBridger 口型** + 导出与面捕；第五章经验杂谈。
- 判定: 🔶观察。（无价格、无日期、是售课页不是经验复盘，**但章节目录把「九轴/胶水/VBridger 口型」这条业内标准工序顺序给全了**，可作你的学习顺序参照；不采信其具体操作细节。）

### 6. AI 绘画给虚拟主播做立绘：先出静帧再进 Live2D —— FlowPix（flowpixai.com）/ FlowPix Team / 2026-09-16
- URL: https://www.flowpixai.com/ai-art/ai-huihua-b8b149.html
- 来源/日期: FlowPix（AI 绘画品牌博客）· **发布时间 2026-09-16**（核实：WebFetch 成功取回正文，页面标 2,729 字）
- 一句话内容: 一条「先静帧、后拆件」的 AI 立绘→Live2D 顺序论，附自称实测数字：**直接产出会动的图 = 拆不出来（每帧重算、发丝对不上前后帧），必须先把定稿全身像 + 正/侧/背三视图 + 表情差分钉死再交拆件**；一致性靠「提示词模板 < 参考图垫图 < 角色 LoRA」三档，**垫图权重 0.4 起、每 0.05 一档，0.55~0.6 是甜点区、超 0.7 构图被参考图焊死**；三视图三大翻车点（侧面瞳色漂移/背面发型崩/服装纹样对不齐）各有修法；交给 Live2D 前的自查：**图层能分层、线条闭合、色块纯色化、长边 3000px 起步**；表情差分 8~10 张够开工。
- 判定: 🔶观察。（**「静帧先行、三视图钉死再拆件」这条顺序判断是对的、也是圈内共识**；但它是**品牌 SEO 博客**，那些具体权重/命中率数字**无第三方出处**，当「待验证经验」用，别当标定值。）

### 7. 物理演算页面中未反映身体的 Y 轴（官方中文创作者论坛求助帖）—— Live2D Creators Forum / 楼主与回帖者未署名 / 日期未核实
- URL: https://creatorsforum.live2d.com/t/topic/3958/2
- 来源/日期: Live2D 官方创作者论坛（中文区）· 页面显示「8月 9 日」发帖、「8月 10 日」「8月 14 日」回帖，**未给年份 → 日期未核实**；⚠️ WebFetch **返回 403（IP 被 discourse 临时限制）**，读不到正文，以下为检索片段，属**仅摘要级**
- 一句话内容: 一个真实卡点与解法——楼主用 5.3 版做物理演算时「头发会动但身体 Y 轴完全不动」，回帖指出这多半**不是物理没生效，而是「光标跟随设置」里没包含「身体旋转 Y」**；给了三步确认顺序：①「预览→光标跟随设置」是否含想动的参数 → ②该参数是否也在「输入设置」里 → ③「输出设置」是否含要摆动的参数；并提醒**即使不开光标跟随，也可直接在物理设置右侧参数列表里调值验证摆动**。
- 判定: 🔶观察。（**「物理不动先查光标跟随/输入/输出三段、而非先怀疑引擎」是个具体可用的排查法**；但页面 403 未能亲手核对原帖文字与年份，按房规降级为仅摘要级、待人工浏览器复核。）

### 8. Live2D PRO 版八折 · 秋季专享特惠（10月1日~11日）—— B站专栏 / 发布者未核实 / 活动期 2026-10-01~11
- URL: https://www.bilibili.com/read/cv53247923
- 来源/日期: 哔哩哔哩专栏 · 正文标**活动期 2026年10月1日(周四)~11日(周日)**，文章发布日未核实；**bilibili 正文有登录/反爬墙，WebFetch 未取回，仅检索片段 → 摘要级**
- 一句话内容: 一条**中文侧的「上新/促销」信号**：Live2D PRO（indie/business，含包年续订、1 年合约、3 年合约）在国庆档给**八折优惠券**（文中给出优惠券代码 `92YNUJXUVM`，购买入口 store.live2d.com/cn，仅限新购、不可与其它优惠叠加），并提到武汉 Live2D WuhanChapter 看板娘联动；同时提醒**首次可享 PRO 版 42 天免费试用**。
- 判定: 🔶观察。（本质是官方促销文案，**价值仅在「中文侧上新/促销时间线」这一记录**；因正文未亲手打开、无法确认发布者是否为官方号，仅留痕，不当教程用。）

## 已收录（剔除）

> 凡命中 `_r31/_dedupe_urls.txt` / `_r31/_dedupe_gh.txt`，或命中房规点名的内容农场/下载站/SEO 镜像，一律不另计条。逐条 `grep -iF` 结果如下。

| 命中 | 判定 | 理由 |
|---|---|---|
| `wenku.csdn.net/answer/bm4kadon54pv`《把一张立绘图做成Live2D动起来…关键步骤?》 | **弃（已在库）** | 第 30 辑已判定为 **CSDN 文库 AI 生成答案**；本轮搜索反复命中，续剔 |
| `github.com/EasyLive2D/live2d-py`（含其 wiki「参数控制」页） | **弃（已在库·gh）** | 仓库主干已在 `_dedupe_gh.txt`（`github.com/easylive2d/live2d-py`，另有 `live2d-motion3`）；**wiki 页是它的附属**，不另计条 |
| `renpy.org/doc/html/live2d.html` · `doc.renpy.cn/zh-TW/live2d.html` | **不另计条** | Ren'Py 官方文档（中/英），非「经验贴」；关键事实（`config.gl2=True`、`CubismSdkForNative-5-r.1.zip`、`renpy.has_live2d()`）前辑已消费 |
| `lemmasoft.renai.us/forums/viewtopic.php?p=577834`（RenpyLive2DTraceSample） | **弃（已在库 + 英文）** | 附属仓库 `github.com/kojimio/RenpyLive2DTraceSample` 已在 `_dedupe_gh.txt`；英文社区，非中文路 |
| `store.live2d.com/cn/` · `www.live2d.com/zh-CHS/business/` | **不另计条** | 官方商店/商用页，非经验贴（`store.live2d.com/en/` 已在 `_dedupe_urls.txt`） |
| `blog.csdn.net/weixin_30843121/article/details/164972177`《Live2D Cubism 5.3混合模式与离屏绘制技术解析》 | **弃（同源批次 + 编造）** | 第 30 辑「疑似编造专区」同款（5.3「新增 6 种混合模式」「Motion Trail」「降67%/减42%」）；本轮再命中 `bryh.cn`/`tzjp.cn` 同文镜像，**续剔** |
| `blog.csdn.net/weixin_29967445/article/details/164234054`《Unity集成Live2D 2.1 SDK…》 | **弃（内容农场）** | 第 30 辑已判定（`weixin_` 高号、模板化）；本轮续命中 |
| `blog.csdn.net/weixin_30846347/article/details/164182620`《Live2D看板娘资源文件全指南》 | **弃（未核实·不采纳）** | `weixin_` 号 + 内容形态为 AI 生成；**WebFetch 两次均被「安全验证」拦，无法核对正文与首发日** → 不采 |
| `blog.csdn.net/weixin_42593549/article/details/164342611`《Live2D模型ZIP解包与修复实战指南》 | **弃（内容农场）** | `weixin_` 高号（164342611 = 新批次），未取回正文；典型模板贴 |
| `blog.csdn.net/cuixun7780/article/details/100345805`《从PSD到可编程Live2D模型》 | **弃（旧文·2019）** | 号段 `100345805` ≈ 2019 年，内容为通用科普，时效与原创性不足 |
| `www.cr173.com/soft/1669159.html`、`/soft/1700676.html`、`/html/392921_1.html` | **续弃（下载站 SEO）** | 房规点名 `cr173.com`；正文含「AI 功能自动生成变形器」等编造界面名，第 30 辑已入专区 |
| `www.hqwc.cn/*`、`www.mhpq.cn/*`（多篇：1630559 / 1465472 / 1468640 / 1334895 / 643291 / 1085143 / 1081724 / 1030246 / 965215 / 615157 / 1001721 / 1337676 / 1465472…） | **续弃（SEO 镜像站）** | 房规点名同源站；正文互抄、同题材多站换域名分发，本轮搜索**命中密度最高**的一批 |
| `www.tzjp.cn/news/87686` | **续弃（SEO 镜像站）** | 房规点名；与上列同源文本 |
| `wap.cisis.com.cn/rjxz/1407.html` · `www.gameyj.com/down/15268.html` · `market.goapk.com/pkg/vtubestudio` | **弃（下载站/应用市场 SEO）** | VTube Studio 下载页，参数（灵敏度 70~85 等）与第 30 辑 `weixin_32705179` 同源话术，无官方出处 |
| `www.haremeta.com/xs/562/562999/522161` | **弃（软件园 SEO）** | 「联盟软件园」功能罗列页，拼凑软件简介 |
| `www.zhanghuanan.com/xiangqing/111151659707.html`《虚拟主播素材怎么使用》 | **弃（SEO 农场）** | 「楠楠博客」，模板化 AI 文案，无具体可核实经验 |
| `post.smzdm.com/p/aggdgn8m/`《Live2D约稿避坑…一篇全讲清》 | **弃（AI 聚合，非个人经验）** | 什么值得买社区帖，正文自曝**「源自627位全网作者」**并逐段挂外部引用（央视财经/北青报等）= 机器聚合稿；内容为通用的约稿合同常识，无 Live2D 专属可核实细节 |
| `www.guhive.com/…立绘类型有多少坑…` | **续弃（存疑不采）** | 第 30 辑已判定「42 个可动参数/35 工时」等数字无出处；本轮同页再命中，续剔 |
| `www.sohu.com/a/1073839438_121267581`（Live2D 虚拟主播全流程视频教程） | **弃（课程搬运）** | 搜狐号转帖的**课程介绍**，非经验贴，正文为教程目录与卖点罗列 |

## 负结论

- **本土平台现状（如实记）**：
  - `blog.csdn.net` 上**凡 `weixin_` 号段 + 高文章号**的 Live2D 帖，本轮抽查到的几乎全是 AI 生成/模板农场（`weixin_30846347` / `29061041` / `42593549` / `31458015` / `29274969` / `30843121` / `29967445`…），且 WebFetch 多被「安全验证」拦，**无法核首发日**——本轮**未从 CSDN 采纳任何一条**。
  - `zhihu.com` / `bilibili.com` 正文受登录/反爬墙，本轮**未能产出任何一条已核实的知乎/B站正文**（第 8 条 B站帖为摘要级）。
  - `creatorsforum.live2d.com`（官方中文创作者论坛）**质量高但被 discourse 403（IP 临时限制）**，本轮只能拿到摘要级内容，**建议下一轮改由浏览器人工取帖**。
  - `live2dhub.com` 本轮**搜索零命中**（未再浮出新的中文论坛帖）；`gamemale.com` 未参与本轮检索，上轮已判「Cloudflare Turnstile 结构性退役」，未再投入时间。
- **上新情报的语种错位**：本轮「上新」类信息（**nizima LIVE 2.7 = 8/12/2026**，新增 AI 助手 + 纯语音追踪 + 时间参数；**nizima ACTION!! 新模型 Shikoku Metan/Ankomon/Kasukabe Tsumugi**；**Cubism 5.4 alpha 开放体验**；**Cubism 5 SDK R5 / R1 beta2 / MotionSync R2_1**）**只有英文/日文源**（yomimono.id、alive-project.com、moguravr.com、third-news.com、docs.live2d.com/en），**中文非官方解读本轮未找到可核实者** → 归入 official/en 路，不入 cn 条。另 `Live2D 13th Creative Awards` 征稿（6/5 起、9/30 截止）亦仅见英文源。
- **英文 SEO 榜单站一律不采**：`statpit.com` / `sigmadax.com` / `tech-insider.org` / `streamer.guide` / `magicmotionstudio.com` / `psewdg.com` / `betuber.com` / `sorceress.games` / `aiparabellum.com` —— 均为英文「Top 10 工具榜 / 指南」并自带 affiliate 声明。
- **新抓到的「疑似编造」例子（只留痕不采纳）**：
  1. `www.hnnews.cc/sczx/202608/t20260812_9491695.html`（怀宁新闻网·地方站 SEO）《AI生成2D骨骼动画的热门工具指南》—— 文中「**Live2D AI 智能交互引擎**」声称「语义分割自动拆分准确率 **98% 以上**」「**自适应骨骼绑定**」，「某团队 **3 小时**完成原需 **2 周**的 **20 个 NPC**」「成本降低 **90%**」「iPhone 12 上 **60FPS**、CPU 占用 **<15%**、内存仅 **30MB**」。⚠️ **Cubism 没有「AI 智能拆分 / 自适应骨骼绑定」这类功能，98%/90%/15% 全无出处** —— 典型「编造软件功能 + 编造精确百分比」。
  2. `blog.csdn.net/weixin_31458015/article/details/164005931`《AI驱动Live2D动画生成：基于 Stable Diffusion 的快速角色动态化方案》—— 声称某项目能用 AI「**自动为其生成可动的 Live2D 模型参数**」「**绕过最繁琐的拆分与绑定两步**」。⚠️ **现役图像/LLM 无法自动产出可用的 `.moc3` 与绑定**，与第 30 辑判定的「AI 面部自动生成」同属一类，**存疑不采**。
  3. `www.elser.ai/zh-TW/blog/best-ai-oc-maker-in-2026…`（厂商博客）—— 称「部分创作者甚至**直接使用 Elser AI 生成完整的 Live2D 素材，完全绕过了传统的角色绑定流程**」。⚠️ 厂商卖点话术，**「生成完整 Live2D 素材并跳过绑定」当前不成立**，留痕。
- **本轮「编造」复现**：`weixin_30843121/164972177`（Cubism 5.3「新增 6 种混合模式 / Motion Trail」）**再次浮出并带 `bryh.cn` / `tzjp.cn` 同文镜像**；提示这批镜像仍在持续分发，后续轮次见到直接剔。

## 搜索覆盖

> 方法：**不用 `site:` 算子**（会掐死中文站群），把 `csdn.net` / `zhihu.com` / `bilibili.com` / `juejin.cn` / `live2dhub` / `小红书` / `抖音` 等**当普通关键词**丢进 WebSearch，再对命中 URL 用 WebFetch 直取正文核实日期/作者。

| # | 搜索式 | 主要命中 | 处理 |
|---|---|---|---|
| 1 | CSDN Live2D 立绘 绑定 教程 参数 2026 | wenku.csdn bm4kadon54pv / weixin_30846347 / weixin_29061041 / cr173 | 全弃（已在库/农场/下载站） |
| 2 | Live2D Cubism 物理演算 头发 摆动 参数 设置 踩坑 | hqwc / mhpq / **creatorsforum.live2d.com/t/topic/3958** | **采 1**（摘要级）、其余 SEO |
| 3 | live2dhub.com 论坛 Live2D 教程 求助 避坑 | hqwc / weixin_30846347 / github nanshaws / cuixun7780 | 全弃（live2dhub 本轮零命中） |
| 4 | Live2D Ren'Py 集成 教程 立绘 踩坑 2026 | renpy.org 官方 / doc.renpy.cn / lemmasoft / sorceress.games | 官方不另计；英文不采 |
| 5 | 掘金 Live2D 集成 踩坑 教程 前端 pixi | mhpq / hqwc / tzjp / gitcode_00078 | 全弃（SEO 镜像） |
| 6 | Live2D Cubism 5.4 新功能 更新 中文 解读 | docs.live2d.com 官方 / blog.gitcode / docs 手册 | 官方占位；gitcode 被 WAF 拦 |
| 7 | Godot Live2D 集成 教程 插件 踩坑 2026 | hqwc / blog.gitcode(AIRI) / weixin_42593549 / github MizunagiKB/gd_cubism | 全弃（SEO/gitcode 被拦/农场；gd_cubism 已在库） |
| 8 | 小红书 Live2D 立绘 接单 教程 经验分享 | guhive / sohu / **mihuashi.com/stalls/912393** / smzdm / flowpixai | **采 2**、弃 3 |
| 9 | 抖音 Live2D 教程 拆分 绑定 教学 2026 | hqwc 多篇 / sohu / zhanghuanan / mhpq | 全弃（SEO 农场） |
| 10 | Live2D 商用授权 定价 Cubism PRO 区别 2026 中文 | store.live2d.com/cn / live2d.com 商用页 / bilibili cv53247923 / 英文 tech-insider 等 | **采 1**（摘要级 B站促销）、官方不另计、英文不采 |
| 11 | Live2D 模型 上新 2026 新功能 新版本 测评 | yomimono.id / alive-project / moguravr / third-news（均英文） | 非中文，归 official/en，负结论留痕 |
| 12 | Live2D 拆图 分层 蒙版 教程 步骤 部位 布点 | mhpq / hqwc / docs.live2d.com 中文官方 | 官方不另计、其余 SEO |
| 13 | nizima LIVE 2.7 AI助手 语音追踪 中文 更新 | third-news / alive-project / moguravr / nizimalive.com / docs 手册 | 全英文/日文，非中文，不采 |
| 14 | 知乎 Live2D 绑骨 建模 教程 经验 | hqwc / cr173 / github nanshaws | 知乎正文取不到；其余弃 |
| 15 | Live2D 接单 报价 经验 拆分 价目表 2026 | **mihuashi.com/stalls/912393** / **mihuashi.com/projects/11730022** / **clibo.tw/NmVzvW** / 英文 magicmotion/psewdg | **采 3**、英文不采 |
| 16 | Live2D Cubism 表情 参数 差分 教程 2026 csdn 实战 | weixin_29967445 / hqwc / weixin_30843121 / github EasyLive2D wiki | 全弃（农场/编造/已在库） |
| 17 | VTube Studio 新手 教程 中文 表情 快捷键 2026 | note.com（英）/ betuber（英）/ cisis / gameyj / goapk | 中文全部为下载站 SEO，全弃 |
| 18 | Live2D Cubism 5.4 alpha 中文 新功能 | docs.live2d.com 中/英官方 / blog.gitcode / haremeta | 官方占位、其余弃 |
| 19 | Live2D 避坑 经验 教程 绑定 穿模 修复 2026 | hqwc / mhpq / live2d.net.cn / weixin_29274969 | 全弃（SEO/农场） |
| 20 | Live2D 公众号 拆分 物理 实战 教程 经验 | **mosouriya.com 拆圖系列** / **aboutcg.org/2400** / hqwc | **采 2**、弃 1 |
| 21 | AI 一键生成 Live2D 模型 自动绑定 2026 工具 | weixin_31458015 / **hnnews.cc** / elser.ai / sigmadax 等 | 全弃并**新增 3 条疑似编造留痕** |

**搜不到 / 空白的部分（如实记）**：① **`zhihu.com`、`bilibili.com` 正文均被登录墙/反爬拦**，本轮唯一 B站条目（促销）只到摘要级；② **`creatorsforum.live2d.com` 被 discourse 403（IP 临时限制）**，官方中文论坛帖只能取摘要；③ **`live2dhub.com` 本轮零命中**，未见新的高质量中文论坛帖；④ CSDN 上 `weixin_*` 农场贴的 WebFetch **普遍被「安全检测」页拦截**，无法核首发日期，故本轮 CSDN **零采纳**；⑤ **「上新」类信息中文源缺席**——nizima LIVE 2.7 / nizima ACTION!! 新模型 / Cubism 5.4 alpha 均无中文非官方解读可核。

**本轮结论：8 条入表（✅ 采纳 3 条 / 🔶 观察 5 条），逐条 `grep -iF` 命中 0 条重复；剔除 25+ 条、留痕 3 条新增疑似编造。**
