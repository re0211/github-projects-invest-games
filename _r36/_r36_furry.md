# 第三十六辑 · Furry / Kemono 领域的 Live2D 技巧（专项调研）

> 触发：用户提问「我听说很多的 live2d 技巧都是 furry 领域大神开发出来的，可以找一找相关内容吗」
> 去重基线：`index.html`（1379 项 / 1362 卡）+ `csdn-social-summary.md` + 最近两版存档 + `_r35/_dedupe_gh.txt`
> **去重结果**：`furry` / `kemono` / `muzzle` / `兽人` / `兽耳` / `ケモノ` / `ケモミミ` / `しっぽ` / `尻尾` **全部 0 命中**
> → 该领域此前**完全未覆盖**，本轮全部为可新增内容。
> （`anthro` 5 处命中经查全是 `anthropics` 误报；`vtuber` 18 处命中属通用 VTuber 内容，非 furry 专属。）
> 数据抓取：2026-10-11

---

## 一句话结论

**「furry 大神开发了 Live2D 技巧」这个说法要打个折**：furry/kemono 圈**没有发明 Cubism 的底层机制**
（变形器、物理摆锤、四角合成都是官方功能），但它**确实率先把「非人类面部结构」逼成了一整套专用做法**，
并把其中一部分做成了**可以反哺人类模型**的通用技巧 —— 最典型的是**背层法（Back-Layer Method）**。

---

## §1 核心人物 / 系统性连载（本辑最重的收获）

### 1.1 Mimisuke（Mimi-Seam）「Kemono Live2D 从零」——最完整的一条线

| 篇 | 标题 | URL | 要点 |
|---|---|---|---|
| 核心 | **How to Create a Muzzle for Kemono/Animal Live2D Models [Part 1]** | https://note.com/mikischine/n/n0c96cc780405 | ⭐ **背层法**详解；「人类模型技巧做不了长吻部」 |
| P1 | How to Make a Kemono Live2D Model (For Beginners) Part 1 — 角色设计/分层/脸 | https://note.com/mikischine/n/n5ade353559e5 | 吻部下必须垫一个**同形稍小的黑色层**；嘴要多拆十几片；PSD 免费下载 |
| P4 | Part 4 — 手臂与手 | https://note.com/mikischine/n/nd7dc931e4c4b | 肉垫（paw pad）怎么贴到人手形上；「没有唯一正确答案」 |
| P7 | Part 7 — 张嘴 / 闭嘴 | https://note.com/mikischine/n/n183a4af27671 | 吻部上下层**同时**做；**下唇(fill)必须手动布点** |
| P8 | Part 8 — 脸左右转 | https://note.com/mikischine/n/nd739263ad37e | 截图+**Flip Motion** 一次性镜像；列出可 flip 的 7 项 |
| P11 | Part 11 — 歪头与耳朵摇动 | https://note.com/mikischine/n/n33e0a74ea6ab | 耳朵/毛用 **warp path 移动部件本身**；耳朵物理**单独建组**，否则和头毛摆动一模一样 |

**背层法（Back-Layer Method）原文提炼** ——
数字绘画的习惯顺序是「线稿层 → 上色层」，背层法**把两者反过来**：

1. 正常画好线稿层与上色层；
2. 把**上色层移到线稿层之上**；
3. 用线稿层建立选区 → 删掉上色层里压住线的部分；
4. 保险起见，把线稿层用线稿色填满。

**效果**：交叉/重叠部件的**线稿会连成一条**，不再互相打架。
**作者明确说：这个技巧「对其他模型也有用」（useful for other models too）** —— 这就是
「furry 圈技巧反哺通用模型」的直接证据。作者用它来解决**有角度的吻部**。

**其他来自本连载的 kemono 专属要点**：
- 「**有人类+兽耳的不算 kemono，那基本是人**」（作者原话，代表圈子自我定义）；
- **长吻部（狗/狼/狐/龙）不能套人类模型的面部做法**；
- 建议**先做「人头 + 吻部/耳朵/毛」**，整兽头是高难度；
- 嘴内画全黑 → **可以不做「犬齿橡胶垫」部件**（省事）；
- 对称部件（眼、犬齿、耳）只需画一侧，另一侧在 Cubism 里复制翻转（**对称的做两份最后会删掉**）；
- 吻部在**上白层**下面垫 **下黑层**（解释了「白吻部下面那块黑形状」的用途）；
- **下唇(fill)是整个流程里唯一必须手动布点的部件**，自动布点会穿帮（张嘴时露出本该藏住的嘴内）。

⚠️ **可达性**：`note.com` 本机 **直连 000 / 代理 000**（与第三十五辑复测口径一致），但**检索正文快照完整可读**。
→ 按 M-0033 记「**本机未命中**」，不写「不存在」。

### 1.2 palkaloid.com（作者 Barutofu / バルトフ）「免費版 Live2D 做兽人模型」——日文侧最系统

**可直接访问（200）**。两条并行连载，全部围绕一只兽人角色「**Fennec-kun（フェネック君）**」，
且**用免费版 Cubism 完成**（免费版参数数量受限，作者专门研究绕过方法）。

**A 线「Live2D で動かす獣人の描き方」（如何画能被 Live2D 驱动的兽人）4 篇：**
- ① https://palkaloid.com/82/live2d-how-to-draw1-1/ — 画兽人时要预先考虑什么
- ② https://palkaloid.com/145/live2d-how-to-draw1-2/ — **上半身（颈→头）重点**
- ③ https://palkaloid.com/167/live2d-how-to-draw1-3/ — **下半身重点**
- ④ https://palkaloid.com/209/live2d-how-to-draw1-4/ — 站姿立绘

**B 线「無料版 Live2D (N)」建模连载（至少 19 篇）**，与兽人直接相关的关键篇：
- (9) 吻部变形（muzzle deformation）——明确说「**这不是人形模型**」
- (10) 双耳设置 —— 镜像复制另一只耳 + **让耳朵随情绪/眼神摆动的物理**
- (11) 视线联动
- (12) 头部 Z 轴（用旋转变形器）
- (13) 脖子左右倾斜
- (15) 头部 X 轴（注明「部件多或嘴形复杂时会很难」）
- (16) 头部**四角形状合成**
- (17) 手臂旋转变形器 + 呼吸 ／ (18) 腿 ／ (19) 呼吸
- 另有「**手动 vs 自动布点的小差异与大差异**」（https://palkaloid.com/872/live2d-artmesh-tips/），
  作者原话承认「以前以为**因为有耳朵和吻部，自动布点用不了**」→ 这是兽人模型布点的常见痛点。

⭐ **该站有「Live2D distribution data (FREE)」** —— 兽人立绘数据免费公开，可直接拿来练手。

### 1.3 虎课网 huke88（中文侧，可直连 200）——兽耳/尾巴的图文步骤

- **《LIVE2D-模型制作-动物耳朵和尾巴的制作图文教程》** https://huke88.com/baike/a55193
  （Cubism 4.0.02，初级）核心步骤：
  1. **尾巴放在所有身体部件的最后**；**耳朵放到头发层的后面**；
  2. 耳朵全部加**自动网格** + **弯曲变形器**；
  3. 用 **角度X / 角度Y** 让耳朵跟随头部；
  4. **四角形状合成**；
  5. 耳朵抖动：新建参数，范围 **-1 / 1**，在**已调好的 XY 轴外面再套一个新变形器**；
     左耳2 幅度比左耳1 小 → 再做四角形状合成；
  6. 物理：把左耳**挂到「左眼」的输入上**、调高**影响度**、调**摆锤设定** → **复制**到右耳；
  7. 新建参数「耳朵抖动」min **0** max **1**，**不绑任何参数**，**把「眨眼」勾在它上面**。
- **《Live2D-简易Q版小人制作-DuangDuang的兽耳制作方法》** https://huke88.com/baike/list/p170
  核心知识点（原文）：「**左耳绑在左边的眼睛开闭上、右耳绑在右边的眼睛开闭上**；
  **耳朵 x 轴调整耳后的露出面积、耳朵 y 轴调整耳尖的上下位置**」；左右耳分别套变形器后**四角形状合成**。

### 1.4 moonku44.com（繁中，可直连 200）——唯一给出「兽耳六件套」拆法的中文源

**《(2025年更新版) 如何畫出一個標準 VTuber Live2D 立繪+拆圖教學》** https://moonku44.com/live2d-psd/
（站长本人兼绘师+模型师，2025-04-14 大更新，示范模型换成自己的 3.0）

- ⭐ **兽耳拆法（原文）**：「**獸耳：左外耳、右外耳、左內耳、右內耳、左毛毛、右毛毛**」——
  即「**外耳/内耳/耳毛 × 左右**」= 6 件。这是中文侧**最具体**的兽耳图层清单。
- 其他可迁移条目：「耳朵: 左耳、右耳」；「尾巴」需单独拆；「**後面（被遮住的地方）也要描繪出來**」；
  「**脖子请延长到嘴巴的高度**」（抬头时需要）；
  「**眼睛反轉要注意眼睛的反光位置，看起来可能会有点脱窗**」（对 furry 的竖瞳/异色瞳尤其相关）。

### 1.5 Mika ——「Snout Layering Guide」（本辑找到的**最直接的 furry 专属教程**）

收录于 `VTResources`（见 §2），条目原文：
> **Snout Layering Guide — Mika — Live2D: Rigging —**
> *"Visual breakdown of how to separate layers for doing snouts for animal or furry models"*

### 1.6 ko-fi 上的免费 furry 吻部工程文件（本辑**唯一可下载的一手素材**）

- **Live2D Furry Snout Example Asset** https://ko-fi.com/s/0007462429
  - **免费**的 **.cmo3 工程文件**，含**两种吻部风格**：**kemono（日系兽人）vs toony（卡通兽）**
  - 头部 **XYZ 角度**已做好，供学习
  - 作者原话要点：「**吻部比人的鼻子更往外突出**，所以 XY 移动时要**把鼻子推得更远**，
    并且要**为吻部加额外的部件**」；「我的**第一个教程视频就是讲 furry 吻部的**」
  - 使用规则：**仅供学习，不得再分发**
  - ⚠️ 本机直连 **403**（内容经检索快照取到）
- 参考（商业模型，非教程）：**Kemono Chibi Vtuber** https://ko-fi.com/s/a3c3b8d217 （Clouddle Atelier，交付 cmo3+json，**不给 PSD**）

---

## §2 ⭐ 关键枢纽：VTResources（人工策展的 VTuber 资源总表）

**http://vtresources.carrd.co/**（carrd 托管；本机直连 000，经检索快照取到）

这是本轮**价值最高的单点发现** —— 它把散落在 Twitter / Discord / YouTube 上的 rigger 技巧
**按主题编了目**，其中**明确包含 furry 专属条目**。摘录与本主题相关的：

**技巧类**
| 条目 | 作者 | 说明 |
|---|---|---|
| ⭐ **Snout Layering Guide** | Mika | **为动物/furry 模型做吻部的图层拆分可视化分解** |
| **nonon.'s Live2D Tips** | nonon.（ののん） | Tips 合集 —— 与 `letsplayindex` 那条「**预设基于 ののん 的推特示例**」**互相印证** |
| Himono's Head Turn Technique / 英译文章 | Himono | 转头技巧（知名 rigger，Patreon） |
| Live2D Project Optimization | Mika | 工程文件瘦身 |
| Shadow Layers on Multiply | ARHDian | 多个正片叠底阴影层互不干扰 |
| Skirt Physics Guide | Giratora / kujamori / アネシア | 裙摆物理 |
| Live2D Basics Class（5 小时 VOD + 练习 PSD） | Karrot | 入门课 |
| Live2D Tech Tips | Kira Omori | 嘴/眼绑定等 |
| Live2D Tutorial 2020 | Brian Tsui | 工具与概念入门 |
| Merry's Text Guide | Merry | 纯文字工作流 |

**可下载的学习素材 / 工程文件**（对本项目「先做小」路线直接可用）
- **Arch Chan** — RavioliMavioli，**CC 许可**的 Live2D 工程文件
- **Cillia's Live2D Resources** — 含**身体弹跳 & 头发物理**示例工程
- **Novaj's Live2D Resources** — ⭐ **嘴部绑定深入资源**：简单嘴 / 详细嘴 / **VBridger 测试嘴**
- **Kvxart's（KevinXu）** — 含**高度实验性绑定**的工程文件
- **Official Inochi2D Example Models**（seagetch）— 官方 Inochi2D 示例，**含 PSD**，也可用于 Live2D 练手
- **Official Live2D Sample Models** — 官方示例，部分含工程+PSD 可拆解
- **Laprio's Free Model**（Arcaena）— 旧模型免费用于 VTubing/学习（需 credit @uwutaa / @pepement_vt）
- **Base by SpoiledChestnut / Chibi Base** — 可自由改造的 base，**个人+商用**皆可
- ⭐ **Cat's Avatar Bases — catboymech** — **免费 Live2D VTuber 头像 base**（描摹/学习/自用）
- **MONDZECKE's Avatar Base** — 免费 base
- **Chibituber Rigging Practice Model**（Selco）／**Karrot's Chibi PSD**／**Test-Chan PSD**（Em）／
  **Annie VTuber Model**（xunidraws）／**Akari-chan Tori ver.**（Toriidoki）／**Asteli**／**Ariru**（.clip）

> 素材使用纪律：这批素材**大多明确写了「仅学习/参考，不得当自己的模型或转卖」**，
> 少数（SpoiledChestnut / catboymech / MONDZECKE）允许商用。**用之前必须逐条读许可**。

---

## §3 其他一手/半一手来源

### 3.1 学生项目实录（有真实踩坑记录）
**Courtney Stockman — [MP] Live2D Cubism Rigging**
https://courtneystockmanart.wixsite.com/home/post/mp-live2d-cubism-rigging
（本机直连 000，内容经检索快照取到）
- **Glue（粘连）**：把两个独立网格的多边形合起来，让它们**一起拉伸移动**而不是分别绑 ——
  作者用它做 **Hip Sway**，并说「**真希望早点学会 Glue，它救了我一命**」；
- **Skinning（蒙皮）**：让 Live2D **自动生成旋转变形器和参数** —— 作者用它做 **Tail Sway**，
  引用 **Moki 的 YouTube 教程**，并说「**尾巴尽量保持笔直**」，能让尾巴更 fluid，
  且**大幅缩短绑定时长**；
- 该模型的物理清单里有：**Ear Jiggle（挂在 Head XY + Eye Blink）**、**Wings Sway（挂呼吸）**、
  **Tail Sway（挂呼吸）**、Hair XYZ、Ribbon、Jewellery、Breast、Belt、Constellation Wiggle、Body/Arms/Leg Bounce、Breath。

### 3.2 NGA 模型师长帖（中文一手经验，本机 403）
**《[模型氵] 从 VTuber 到 Live2D——现今虚拟主播模型制作过程、质量评估与疑难解答》**
https://bbs.nga.cn/read.php?tid=24067275
- 画师交原画时「**尾巴等需要弯曲摆动的部分，为了方便一般会提供竖直状态的整体**」；
- 「**对于脑后、手肘等一般情况下看不到的地方也应该正常描绘**，因为看不见的地方也会出现在镜头前」；
- 作者自述踩坑：「**我刚开始做模型的时候为了把一根猫尾巴掰直，直接把它拆成了十几段**」——
  这是「尾巴要竖着画」这条规矩的**代价说明**；
- 物理提醒：「**Live2D 里模拟的物理场景与 FaceRig 里实际效果并不一致，请多加调试**」。

### 3.3 Furry VTuber 委托/商业侧（说明这条线的「产业面」）
- **MyFurryRefSheet — VTuber Rigger: Complete Guide for 2026**
  https://myfurryrefsheet.com/vtuber-rigger/ （本机 200）
  - **2D(Live2D) vs 3D 对比表**：Live2D 便宜快速（$300–2,000 / 2–6 周），3D 贵慢（$500–5,000 / 4–12 周）；
  - 「**furry 在 2D Live2D 极度流行，3D 在 2026 增长很快**」；
  - ⭐ 「**furry 模型有独特元素 —— muzzles、ears、tails、非人比例 —— 需要专门的绑定知识。
    接活前要问清对方有没有绑过 anthro 角色**」；
  - 找 rigger 的地方：**#VTuberRigger / #Live2DRigger / #VTuberCommissions**（X）、
    VTuber Discord 的 #rigger-search、Reddit **r/VirtualYoutubers / r/Live2D**；
  - 常见错误：**只拿一张平铺 PNG 去找 rigger，绑不了**（必须有分层 PSD）。
- **Coloso / online-courses.club — Meiyu《Create Cute Avatars in Live2D》**
  https://online-courses.club/create-cute-avatars-in-live2d-from-basic-to-commercial （本机 200）
  - 作者 **Meiyu**，中国人，自由职业 rigger 五年，**做过 200+ VTuber 模型**（含 Kira、Rurumi、Akugaki Koa、MOYO）；
  - 大纲里**明确含「Rig animal ears, tails, hats, and arm switching」**；
  - 配套练习包含 **cat ears 预设**、五套嘴型方案、头 XY 的完整 cmo3。
  - 工具链：Cubism 5.2.03（也允许 5.0）+ VTube Studio + **VBridger** + SAI Ver.2。16 小时 41 分（实际 33 小时 20 分）。
- **Booster / 通用教程（价值较低，仅作背景）**：
  - catvtuber.com《How to Become a Cat VTuber》https://catvtuber.com/how-to-become-a-cat-vtuber/ （200）
  - voxbooster.com《How to Make a VTuber Model: Complete 2026 Guide》 https://voxbooster.com/blog/how-to-make-a-vtuber-model
  - streamskins.net《How to Make a VTuber Model》 https://streamskins.net/how-to-make-a-vtuber-model ／
    繁中版 https://streamskins.net/zh/how-to-make-a-vtuber-model
  - aboutcg.org《二次元直播用 Live2d 制作教程》 https://www.aboutcg.org/courseDetails/1125/introduce （480 分钟，付费，非 furry）
  - GitHub **nanshaws/Live2DTutorial** https://github.com/nanshaws/Live2DTutorial （200，中文 Live2D 教学文档，通用）

### 3.4 视频转录站（内容可用，本体需另找）
- **tubesum.app**（把俄语/英语 YouTube 教程转录成英文文本 + 章节 + 闪卡）
  - 《Live2D Model Creation: Full Breakdown》 https://tubesum.app/v/kak-ia-delaiu-2d-modeli-dlia-strimingalive-2d-tutorial
  - 《Live2D Vtuber Rigging Guide》 https://tubesum.app/v/how-to-rig-your-vtuber-model-with-live2d
  - 《Separate VTuber Art for Live2D》 https://tubesum.app/v/how-to-separate-vtuber-art-for-live-2d-cubism
    ⭐ 这条明确写：「**Extras: Expressions and Accessories —— 把 animal ears/tails 放进各自的文件夹**」
- **letsplayindex.com**（CraftyKaname《How to Rig Wiggly Cat/Animal Ears (with physics setup)》）
  https://letsplayindex.com/video/live2d-tutorialhow-to-rig-wiggly-catanimal-ears-with-physics-okcExB3gkUM
  - 关键技：**不用旋转变形器**；**旋转变形器不能夹在 warp 层级中间**（会改变两侧 warp 行为）；
    Y1+Y2 基础耳抖（根+尖）参数分开；预设**基于 ののん 的推特示例** ← 与 §2 的 nonon. 互相印证。

---

## §4 结论：furry 圈到底「贡献」了什么？

把本轮材料摊平后，可以清楚地把「furry 圈的 Live2D 贡献」分成三层：

### 层 1 — **没有发明底层机制**（去掉神话）
变形器（Warp / Rotation / Deform Path）、物理摆锤、四角形状合成、剪切蒙版、Glue、Skinning
—— **全部是 Cubism 官方功能**，不是 furry 圈造的。

### 层 2 — **为「非人类结构」逼出了一整套专用做法**（真正的贡献）
| 问题 | furry/kemono 的解法 | 出处 |
|---|---|---|
| 吻部投影出脸外，人类面部技巧失效 | **背层法** + 白吻部/黑垫层 双层结构 + 鼻子在 XY 上推更远 | Mimisuke / Mika / ko-fi 素材 |
| 嘴要张得比人大 | **嘴部拆成十几片**（人只有上下唇两片）；嘴内画全黑可省掉橡胶垫部件 | Mimisuke |
| 耳/尾要独立于头发摆动 | **尾巴放最底层、耳朵放头发层之后**；耳/尾**各建独立物理组** | 虎课网 / Mimisuke P11 |
| 耳抖要「活」 | 耳朵绑在**同侧眼睛开闭**上 + 影响度调高；或新建 0–1「耳朵抖动」参数不绑、把眨眼勾上去 | 虎课网（两条） |
| 耳朵形状要跟头 | 角度X/Y + 弯曲变形器 + **四角形状合成** | 虎课网 |
| 兽耳要拆几层 | **外耳/内耳/耳毛 × 左右 = 6 件** | moonku44 |
| 尾巴摆动不自然 | **画的时候就画成竖直整体**，再做 **Skinning**（蒙皮）让 Cubism 自动生成变形器 | NGA / Courtney |
| 面捕对眼睛微笑不敏感 | 把微笑绑到「**嘴巴抿起 + 眼睛闭上**」的**前提条件**上 | cloudymount789（通用技巧，与耳抖同一思路） |

### 层 3 — **其中一部分确实反哺了通用模型**（用户直觉成立的部分）
- ⭐ **背层法（Back-Layer Method）** —— 作者本人说「**对其他模型也有用**」，用于任何**交叉重叠的部件**；
- ⭐ **「把 X 绑在 Y 的前提条件上」** 这套「参数优先级/前提条件」玩法，
  furry 用它做耳抖，人类模型用它做微笑 —— **同一个机制**；
- ⭐ **靠眼睛开闭驱动耳朵** 这个「借道捆绑」思路，本质和「靠呼吸驱动尾巴/翅膀」同源；
- ⭐ **Skinning / Glue** 这类高级技法，被 furry rigger 大量用于**尾巴与身体衔接**，
  反过来正好是尾部/裙摆这类通用问题的最优解。

> **一句话**：furry 圈不是「发明家」，是「**最难的那批客户**」——
> 因为要做的东西（长吻、大嘴、会动的耳和尾）**把人类模型的偷懒做法全堵死了**，
> 于是被逼出了一批**更鲁棒、可迁移**的解法。

---

## §5 可达性实测（2026-10-11，本机）

| 源 | 状态 | 备注 |
|---|---|---|
| palkaloid.com | **200** | 日文，兽人免费版连载 |
| huke88.com | **200** | 虎课网，中文图文 |
| moonku44.com | **200** | 繁中，拆图教学 |
| myfurryrefsheet.com | **200** | furry 委托指南 |
| online-courses.club | **200** | Coloso 课程页 |
| aboutcg.org | **200** | ABOUTCG 课程页 |
| github.com/nanshaws/Live2DTutorial | **200** | 通用教学文档 |
| catvtuber.com | **200** | 背景 |
| **note.com** | **000**（直连+代理） | 与第三十五辑一致；**内容经检索快照可读** |
| **vtresources.carrd.co** | **000** | ⚠️ 高价值枢纽，本机不通 |
| **courtneystockmanart.wixsite.com** | **000** | wix 不通 |
| **ko-fi.com** | **403** | 直连被挡 |
| **bbs.nga.cn** | **403** | 反爬 |

⚠️ **M-0033 纪律**：以上 000/403 **只表示「本机这条通道没拿到」**，不表示页面不存在或已下线。
`note.com` 连续两辑 000，但正文快照两次都完整 → **记为「本机未命中」，不记为「退役」**。

---

## §6 待办（留给下一辑）

1. **背层法实操**：用 Mimisuke 免费公开的 `こいぬ.psd`（或 palkaloid 的免费兽人数据）走一遍背层法，
   验证「线稿层→上色层反转」在 5.3 正式版上的实际手感。
   ⚠️ Mimisuke 的 PSD 授权**明确禁止「用于 AI 训练」**，但允许「下载/学习练习/改造/发视频截图/进作品集」。
2. **下载 ko-fi 的 Furry Snout `.cmo3`**（需绕过 403，或让用户手动下）→ 拆解两种吻部风格的结构差异。
3. **给 vtresources 建一份离线副本**（carrd 本机不通，但内容价值极高）—— 需要用户在浏览器里取一次。
4. **「Glue / Skinning」单独成条**：这两个是**通用**且能显著省时的技巧，属「有用就改」范畴，
   考虑写进 `game-production-pipeline.md` 的 Ren'Py/Live2D 相关章节。
5. **核实 `letsplayindex` 与 `tubesum` 是否属同一批转录站**（正文风格高度相似，疑似同源或同技术栈）。
6. **中文侧补检**：B 站/知乎/小红书上以「兽人 Live2D」为关键词的 UP 主教程（本机需人工浏览器）。

---

## 统计

- 检索轮次：**6 次 WebSearch + 1 次 WebFetch + 2 批 curl 可达性**
- 有效候选：**30+ 条**，去重后**全部为新增**（furry 域在索引中 0 命中）
- 可直连：8 个源；不可直连但内容可取：note.com / vtresources / ko-fi / NGA / wix
- 落盘：`_r36/_r36_furry.md`（本文件）
