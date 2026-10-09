# 跨平台游戏制作 × AI 开发资源梳理（2026-10-10 · 第二十六辑 · **Live2D 制作专题**）

> ## ⚠️ 勘误块（2026-10-10 第二十七辑追加，append-only —— 原文不动，只留痕）
>
> 本辑 §八「上新与新闻」里的三个日期**取数入口选错了**（从 live2d.com 首页新闻时间轴按位置读，
> 而该页 DOM 的日期排在它所属条目的**下一条之前**，系统性差一位）。
> 第二十七辑改用官方 Product Info 分类页（`?info_cat=product`，逐条渲染）复核后裁定：
>
> | 项 | 本辑写的 | **更正为** |
> |---|---|---|
> | Cubism Editor 5.3.00 正式版 | 2025-11-14 | **2026-01-20** |
> | Cubism Editor 5.3 alpha | 2025-02-04 | **2025-03-25** |
> | Cubism Editor 5.2.00 正式版 | 2024-12-24 | **2025-02-04** |
>
> 根因与教训已记为 **M-0029**（从列表页按位置取属性 → 相邻条目错配，必须配第二个入口）。
> ⚠️ 本辑当时其实留了一句「发布日期两说，已在原始稿留证，不单方面断言」—— 这句话救了它一半，
> 但**「两说」本身也是错的**（不是两说，是读错一位）。**留痕 ≠ 正确，只能保证错误可追溯。**

> 三路并行调研，原始产出：`_r26/_r26_gh.md`（GitHub 路 **32 条**）·
> `_r26/_r26_cn.md`（中文社媒路 **28 条**）· `_r26/_r26_official.md`（官方与海外路 **26 条 + 授权 8 小节**）。
> 候选池 **86 条**，三路交叉零重复；与 `index.html`（增补前 1168 项）及 `csdn-social-summary-v25/v23/v22`
> 机器比对 —— **历史库里 live2d 词频为 0（中文路）/ 4（全是已收的 `cubismnativeframework`）**，
> 也就是**这是一个全新主题，没有旧账可去重**。
>
> ⚠️ **编号说明**：本辑是**第二十六辑**（第二十四辑号被 2026-09-24 的房规交互轮占用，存档按内容编号，
> 故 `csdn-social-summary-v25.md` = 第二十五辑，`v24` 仍是有意缺口）。
>
> **本辑主线：Live2D 的钱不是花在软件上，是花在拆图上。**
> 我们原本的假设是「预算有限的学生做不了 Live2D」—— 查完发现这个假设是错的：
> 官方 **FREE 版**（30 参数 / 100 ArtMesh / 单张 2048 纹理）对「只播预设表情和动作」的视觉小说
> **本来就够用**；学生三年 PRO 折后约 **¥7,344 日元**（≈ 三百多人民币）。
> 真正的成本在人力：一位画师的实录是**立绘画 7 小时、拆分拆了 14 小时** —— 拆图比画画贵一倍。
> 所以本辑把票投给「**拆图 / 绑骨自动化**」和「**AI 补间**」，而不是更贵的编辑器插件。

---

## 一、搜索覆盖与去重

| 路 | 覆盖 | 条数 |
|---|---|---|
| gh | GitHub：运行时 / SDK / 编辑器替代 / PSD 转换 / 网页挂件 / 查看器 / 面捕 / AI 拆层 | 32 |
| cn | CSDN / 掘金 / B站 / 微信 / 虎课 / 虎嗅 / 微博 / gamemale / 模之屋 / 知乎 | 28 |
| official | live2d.com 官网与手册 / store / 学生计划 / GitHub Releases / note.com / Zenn / Booth / arXiv | 26 + 8 |

**剔除名单（本轮一条未收）**：`hqwc.cn`、`bryh.cn`（房规点名同源站）·
`live2d.net.cn`（普拉弗蒙代理商 SEO，页底挂电话咨询）·
CSDN `weixin_33824385/weixin_29061041/weixin_30846347`「看板娘全攻略」三连（ID 连续、同题材 = 同一 AI 稿批次）·
`intelliparadigm.com`（路径即 `/article/weixin_29053695/`，CSDN 镜像内容农场，其「98.7% 准确率 / 1080Ti 37 秒」无任何一手来源）·
百度文库 / 人人文库 / renrendoc（付费文档墙）· GitHub 侧：`zwa73/UnityLive2DExtractor-Unofficial`（换名派生）、
`NovaPlayzGames/model-reaper`（换名重发）、`xiazeyu/live2d-widget.js`（同功能撞车）、`P1kaj1uu/ChattyPlay-Agent`（关键词堆砌）。

**⚠️ 两个「本轮查不到」要记下来**（免得下轮以为漏了）：
**知乎在这一主题上零命中**；**gamemale 需登录**，本轮只登记了站点入口未取到具体页 —— 这两个是下辑的补缺方向。

---

## 二、先算清楚账：授权与价格（本辑最值钱的一节）

> 价格与条款**逐条来自官方页面**（下附 URL）；核不到的写「未核实」，**不填估计值**（房规 #52）。

| 问题 | 结论 | 出处 |
|---|---|---|
| 不花钱能做什么 | FREE 版：参数 30 个 / ArtMesh 100 个 / 导出 1280×720 | [官方对照表](https://www.live2d.com/cubism/comparison/)（[中文版](https://www.live2d.com/zh-CHS/cubism/comparison)） |
| PRO 多少钱 | PRO for indie：**¥14,280 首年 / ¥2,080 月 / ¥36,720 三年**，**没有买断制** | [Live2D Store](https://store.live2d.com/en/) |
| 学生 | **80% OFF → 三年 ¥7,344**，截止 **2027-03-31** | [学生折扣页](https://student.live2d.com/en/student-discount/) |
| 学校渠道 | LEAP 教育支援计划可申请**免费 PRO 授权** | [LEAP](https://student.live2d.com/zh-CHS/education-aid-program/) |
| 什么时候要签授权 | **开发和试做阶段一分钱不收**；「只在发布内容时需要」，且须**提前 1 个月**办完 | [SDK License](https://www.live2d.com/en/sdk/license/) |
| 个人把 Live2D 塞进游戏发行 | Plan E：**个人 / 小规模（年营业额 < 1000 万日元）免费**，中型 ¥100,000 / 大型 ¥600,000 | [Plan E](https://www.live2d.com/en/sdk/license/purchase_plan02/) |
| 唯一不豁免个人的 | **Plan A「可扩展性应用」**（avatar / 多作品 portal / 你发行的面捕软件）：必须过审查签专门 PLA，revenue share **每份 ¥300 或销售额 20% 取较高者** | [Plan A](https://www.live2d.com/en/sdk/license/expandable/) |
| 靠内购/抽卡/广告赚钱 | Plan G 持续 royalty | [Plan G](https://www.live2d.com/en/sdk/license/running_plan01/) |
| 「免费」的代价 | 三件事：启动 logo 显示 1 秒、商品页标注 Live2D、提交 Database + 一份问卷 | [Guidelines](https://www.live2d.com/en/sdk/guidelines/) |

**⚠️ 同官网挂着两个不同的折扣数字（本轮实测，不是核错）**：学生专页写 **80% OFF（¥7,344）**，
而 live2d.com 的**全站共通横幅**（SDK 授权页、5.4 alpha 公告页上都有）仍是 **76% OFF（¥8,812）**。
两个 URL 都打开过。判断是 2026 年改价后**旧文案没清干净** —— 签约/付款前以**结算页实际金额**为准，别信横幅。

**⚠️ 一个会造成事故的坑**：网上到处被引用的 `github.com/Live2D/CubismSdkForUnity` **现在是 404**。
官方早把 SDK 拆成 `CubismUnityComponents` 等部件仓库，而且 **Cubism Core 根本不在 GitHub 上**（必须去官网下载分发包）
—— 也就是说 **clone 仓库构建不出能跑的东西**。照老教程做的第一步就撞墙。官方仓库全景：[github.com/Live2D](https://github.com/Live2D)。

---

## 三、最贵的一环：拆图与分层

1. **官方素材拆分手册**（英文，图多，权威）— https://docs.live2d.com/en/cubism-editor-manual/divide-the-material/
2. **画师全栈避坑笔记**（个人博客，**本轮最有价值的一手材料**）— https://cloudymount789.github.io/blog/live2d_note/
   → **画 7 小时 / 拆 14 小时**的工时账单 + 一堆没人写的坑：先拆完再布点、做 Y 轴时 X 轴归中、别删关键帧、
   Procreate 导出的 PSD 每层都是整画布大小（要在 PS 里删掉背景层再导入）。
3. **B站《1 个小时从 0 基础到上手 Live2D》**（7 节连载，中文闭环到 VTS + OBS）— https://www.bilibili.com/read/cv20738750/
4. **卡米雷特**（中文互联网最专业的 Live2D 账号）：[5.3 新功能演示](https://bilibili.com/video/BV1PNkLBWEqi/) ·
   [眼球深度小妙招](https://bilibili.com/video/BV1z6ieBSEXy/)
5. **B站《live2d 制作全过程》附 PSD**（可跟着做）— https://bilibili.com/video/BV1vg4y1W7JC/
6. **官方教程站**（免费，含范例模型 JUKU）— https://docs.live2d.com/cubism-editor-tutorials/top/
7. **虎课网《虚拟主播原画基础拆分分层》**（视频课）— https://www.huke88.com/course/82442.html
8. **CSDN 分层原理**（图片分层 → 骨骼绑定）— https://bbs.csdn.net/weixin_30047059/article/details/100239327
9. **省钱做法**：`tsunehimatoi/psd2live`（★598，PSD → .cmo3 自动绑骨）https://github.com/tsunehimatoi/psd2live
   ⚠️ **GPL-3.0**，商用前想清楚传染性。

**一句话结论**：不要在画完之后再想 Live2D —— **画立绘的那一刻就按 Live2D 的图层结构分图层画**，
这比任何省钱技巧都省钱。

---

## 四、接出去：Ren'Py / Unity / Godot / Web / 直播

- **⭐ Ren'Py 官方原生支持 Live2D Cubism（3 / 4 / 5）** — https://www.renpy.org/doc/html/live2d.html
  （[中文译本](https://doc.renpy.cn/zh-TW/live2d.html)）
  → 三步装完；两个必记点：需要 `config.gl2 = True`；用 `renpy.has_live2d()` 做降级
  （不做的话没有 Live2D 支持的机器会**整体加载失败**，且 **web 版不支持**）。
  → **这条直接改写了待办**：社区模块 `asfdfdfd/renpy-live2d`（★89，**推送停在 2021-03-02**）已不值得装，
  本辑仍登记进索引，作为「旧项目迁移」的参考实现。
- **Unity**：官方部件仓库 https://github.com/Live2D/CubismUnityComponents （旧名已 404，见上）
- **Godot 4**：`MizunagiKB/gd_cubism`（★301，C++ GDExtension，推送 2025-04-01）https://github.com/MizunagiKB/gd_cubism
  ⚠️ NOASSERTION（许可证不明，商用前必须确认）
- **Web**：官方 `CubismWebFramework`（★237）+ 社区事实标准 `guansss/pixi-live2d-display`（★1507 / MIT）。
  想直接挂个看板娘：`hacxy/l2d-widget`（★639 / **MIT**）https://github.com/hacxy/l2d-widget
  —— 老牌 `stevenjoezhang/live2d-widget` 有 ★10986 但是 **GPL-3.0**，往商业站点挂有传染性。
  中文实战：[掘金口型同步](https://juejin.cn/post/7458066295867932723) ·
  [CSDN vue 引入保姆级](https://blog.csdn.net/qq_64595427/article/details/140717574)
- **直播 / VTuber**：官方自己的免费面捕 **nizima LIVE**（¥0 起步）https://nizimalive.com/en/ ·
  本地 AI 虚拟主播 **Open-LLM-VTuber**（★14025，可接本地 Ollama）https://github.com/Open-LLM-VTuber/Open-LLM-VTuber ·
  摄像头驱动表情 `adrianiainlam/facial-landmarks-for-cubism`（★75 / MIT）
- **模型检查器**：`guansss/live2d-viewer-web`（★175 / MIT，拖进去就看）https://github.com/guansss/live2d-viewer-web
- **开源平替**：`Inochi2D/inochi-creator`（★1240 / BSD-2-Clause）https://github.com/Inochi2D/inochi-creator
  —— 完全不想谈授权时的干净路线，代价是教程少、接 Ren'Py 要自己写一层。

---

## 五、AI × Live2D：哪一段真能用

| 环节 | 现在能不能交给 AI | 证据 |
|---|---|---|
| **拆图 / 补遮挡** | ✅ **能，这是刚需环节** | See-through（SIGGRAPH 2026，Apache-2.0）https://github.com/shitagaki-lab/see-through ；ComfyUI 封装 https://github.com/jtydhr88/ComfyUI-See-through |
| **整条流水线** | 🟡 有人跑通，但依赖闭源模型 | [return.moe 实录](https://blog.return.moe/en/2026/07/19/towards-fully-automated-live2d-style-animation)：出图 → See-through 分层 → 让 LLM 写引擎并绑骨，作者自称**无动画背景**也做出来了 |
| **端到端学术方案** | 🔵 有论文，短期不是工具 | Bunraku（arXiv 2607.27348）https://pith.science/paper/2607.27348 —— 单图 → 可编辑 rig，另发 Live2D-Bench + 8,884 个模型语料 |
| **让 AI 直接操作软件** | 🟡 刚起步，值得盯 | `nana7chi/CubismExternalEditMCP`（★33 / MIT）https://github.com/nana7chi/CubismExternalEditMCP —— 把 Cubism 操作暴露成 MCP，接本地 Ollama 就能用 |
| **问 AI 解决软件里的坑** | ❌ **不能，会持续编** | 见下节 M-0028 |

**Bunraku 论文里最反直觉的一条**：把 Stage 2 网络**放大 112 倍（到 5.7 亿参数），动画质量毫无提升**。
瓶颈是**跨层协调 / 任务歧义**，不是模型容量。→ 如果以后真要做 AI 辅助绑骨，别堆参数，**要让各层的顶点互相看见**。

---

## 六、AI 贴核实：我读了，决定改什么

本轮中文路单独标出 5 条 AI 相关贴，**我逐条读过后只采纳一条作为改动**：

- **采纳 → 新增 `M-0028`「让 LLM 回答小众垂直 GUI 软件的操作问题，它会持续编造选项」**。
  一手证据：作者卡在「重新导入 PSD 后图层与布点/变形器对不上」，问了很久 AI，
  原话是「**AI 老是编造软件的功能，实际上软件里没有这个选项**」「检索到的文章使用的软件版本不同」。
  → **这不是「AI 能不能帮我做 Live2D」的吹捧，是「AI 在这类软件上会幻觉」的实证。**
  我据此给房规 #52 补了**第二种形态（存在性）**：「软件里有没有这个按钮」也是结论，
  判据是**回答里有没有可核对的官方落点**（手册哪一页 + 版本号）；给不出 = 它在编。
  （与 #52 原本管的**数值类**是同一个病：拿不到工具结果时，模型用文体补事实。）
- **A1（SAM 2 五分钟自动拆分）→ 剔除**。内容农场，数字无一手来源，只当「这个方向有人在喊」的信号。
- **A5（虎嗅：AI 时代手搓动画更香）→ 只记观点不落地**。 https://www.huxiu.com/article/4862515.html
  它与 A4 恰好构成对照：AI 在**拆图/生成**侧有用，在**软件精细操作**侧会幻觉，在**审美与编排**侧不可替代。

---

## 七、资源与社区（含「要登录」预警）

- **模之屋 PlayBox**（模型社区，中文）https://www.aplaybox.com/model/model —— ⚠️ **下载需注册/实名**
- **gamemale**（二次元资源社区）https://www.gamemale.com/ —— ⚠️ **需登录**，本轮零命中 Live2D 专页
- **微博 #Live2D#** https://s.weibo.com/weibo?q=Live2D —— ⚠️ 搜索结果需登录；
  官方汇总的推荐标签页 https://www.live2d.com/zh-CHS/community/
- **Booth**（pixiv 旗下，日文创作者市场，看真实价格带）https://booth.pm/zh-tw/items/4709134
- **note.com 日本初学者实录** https://note.com/rosaria_v_score/n/n75e2690ba874
- **免费模型几种获取方式** https://blog.csdn.net/qq_36303853/article/details/142284330

## 八、上新与新闻（2026）

- **Cubism 5.3.00 正式版**：[官方公告](https://www.live2d.com/en/information/cubism-editor-5-3-00-official-release/)（页面标注 2026-01-20）·
  [新功能中文手册](https://docs.live2d.com/zh-CHS/cubism-editor-manual/new-function5-3/) ·
  [更新日志](https://www.live2d.com/en/cubism/update/5-3-00-update-information/)
  ⚠️ **发布日期两说**：官网新闻列表写 2025-11-14，公告页时间戳与教程站写 2026-01-20 —— 已在原始稿留证，不单方面断言。
- **Cubism 5.4 alpha**：官方免费放出的尝鲜版，但**明确禁止拿它做成品**（用 alpha 做的模型不能卖也不能发行，SDK 迁移不保证）
  → https://www.live2d.com/en/information/cubism-5_4-alpha/ → 结论：**别在这个阶段做东西**。
- **2026 春季促销 20% OFF**：仅 11 天（2026-03-19 ~ 03-30）https://www.live2d.com/information/springsale-2026/
- **R5 破坏性改名**：SDK 与 5.3 正式版的兼容性官方专页 https://docs.live2d.com/en/cubism-sdk-manual/compatibility-with-cubism-5-3-official

---

## 九、索引与文档维护（本轮落盘）

- `index.html` **1168 → 1183 项**（卡片 1157 → 1172，第三十一版增补 **15 卡**，脚注 [1168]-[1182]，
  新建 `insert_v31_cards.py`；跑前过了 `insert_guard_probe.py` **6/6**，跑后 `index_metrics --update` 重封 301 个分组快照）
- 新增错误记忆 **`M-0028`**（mistakes 27 → **28**），已 `mistakes_seal.py seal` + `check` 28/28 一致
- 房规 **#52 补第二种形态（存在性）**并指向 M-0028（不再新开条款，省预算）；主件行数 193 → **197 / 200**（⚠️ 只剩 3 行）
- 上一辑存档 `csdn-social-summary-v25.md`

---

## 十、下一辑待办

**本辑新出**
1. **房规只剩 3 行余量** —— 下一辑必须**压缩条款正文**（不是撤条款），否则 #52 之后没法再加东西
2. **真跑一次 Ren'Py 官方 Live2D**（`config.gl2 = True` + `has_live2d()` 降级），用最小工程验证，别只登记文档
3. **实测 `psd2live` + `ComfyUI-See-through`**（本辑两条最高分工具，都只有 API 级核实，没有本机跑过）
4. **`Open-LLM-VTuber` 跑一遍**（★14025 + 可接本地 Ollama，是「本地 LLM 驱动角色」最完整的现成参考）
5. **补两个空白**：知乎在这一主题零命中；gamemale 需登录 —— 下轮换入口（站内搜索镜像 / 站内话题页）

**承接老账（顺延）**
6. `/skill-doctor`（**连续第五轮**）· 7. 装 `ollama-vscode` + 跑 `agnix` · 8. 做一次 `consolidation`（记忆合并淘汰）
9. 索引条目加「最后复核日期 + 是否作废」· 10. `rpycdec` 反编译自查（**欠九轮**）· 11. Codex 离线 / 词表 / 模型分档
12. `_tools/` 与 `AGENTS.md` 纳入版本控制

---

*本辑新增 86 条候选（gh 32 / cn 28 / official 26）+ 授权 8 小节，落索引 15 卡；
累计经验帖约 995 → **约 1081 条**；索引 **1183 项**；房规 **22 条 / 197 行**；决策原则 22 条；mistakes **28 条**；
新建脚本：`insert_v31_cards.py`。*
