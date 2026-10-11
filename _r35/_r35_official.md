# 第三十五辑 · official 路（官方文档 / 官方论坛 / 海外社区）

> 采集时间：2026-10-11 19:0x–19:2x
> 本路负责：`live2d.com` 官方站点与文档 · `community.live2d.com` 官方论坛 · 海外社区（zenn / note / HN / DEV）
> 去重基线：`index.html`（1317 个 owner/repo + 1472 URL）+ `csdn-social-summary.md` + `v34` / `v33` 存档

---

## 一、官方论坛（community.live2d.com）—— 本轮新帖

> ⚠️ **路由体系变了**：前几辑记录的是 `/t/<4 位帖号>`（如 /t/3979），本辑抓到的分类页给出的全是
> `/discussion/<4 位帖号>`（如 /discussion/2389）。**两套编号不互通**，本辑按 `/discussion/` 记录。

### ① 物理运算完全不动，`Maximum Output` 卡在 0 且改不了
- 链接：https://community.live2d.com/discussion/2389/why-won-t-my-live2d-physics-move-maximum-output-is-stuck-at-0
- 作者 / 日期：kimuhaye · **2026-10-06**（分类：Help）
- 事实（正文已读）：用户用 **Cubism 5.3**。给 `Hair Front` 参数做了 keyform，在物理设置里指定
  `Inputs: Angle X / Angle Z / Body rotation X / Body rotation Z`，`Output: Hair Front`。
  结果：**鼠标移动时摆锤（pendulum）完全不动，头发也不动**；且 `Hair Front` 这个输出的
  **`Maximum Output` 值显示为 0，用户改不动**。
- 状态：**截至采集时没有回复**。
- 可复用性：`⚠️ 参考` —— 没有官方解答，但它把「物理设置看起来配对了却一动不动」这个症状
  和「Maximum Output = 0 且不可编辑」这个**可观察量**绑在一起，排查时可以直接对照。
  **对做模型的人**比「去看物理教程」有用：先查输出参数的 `Maximum Output` 是不是 0。

### ② 社区请求「Live2D Cubism 原生支持 Linux」，官方回「已转交开发组」
- 链接：https://community.live2d.com/discussion/2386/live2d-cubism-linux-support
- 作者 / 日期：Qryosity · **2026-09-17**；官方 `ookubo(staff)` 回复 **2026-09-18**
- 事实（正文与回复均已读）：
  - 用户论证：Cubism 是 **Java 应用跑在 JVM 上**，改到 Linux 的代码量「应该很小」；
    他自己和若干 rigger 已迁到 Linux，现在只能靠 **Wine** 跑，「重型模型上性能损失更严重」。
  - 官方回复全文意思：**「已把您的请求共享给开发团队」**（标准套话，**没有承诺版本或时间**）。
- 另一个同题材帖：https://community.live2d.com/discussion/2382（韩语，`ookubo(staff)` 于 **2026-09-11**
  发在同一 Feature Requests 区）—— 说明 Linux 诉求这一个月内被提了不止一次。
- 可复用性：`⚠️ 参考` —— 「官方已回复但未承诺」这一定性，比「社区在要 Linux 版」这句传闻有用：
  **短期不要指望原生 Linux 版**，现阶段正解仍是 Wine + DXVK（论坛 2023 年那篇
  https://community.live2d.com/discussion/1360/running-live2d-cubism-on-linux-ft-wine-dxvk 仍是唯一实操帖）。

### ③ 图层准备（layer prep）工作流提问
- 链接：https://community.live2d.com/discussion/2381/quick-question-on-layer-prep-workflows
- 作者 / 日期：anysplit · **2026-08-25**（分类：General Discussions）
- 核实深度：**仅标题 / 作者 / 日期级**（正文未取）。
- 可复用性：`⚠️ 参考`（待取正文后升级判定）。

### ④ SDK 5 R5 + URP：`TransparentPicking` 材质在初始化后仍被挂住
- 链接：https://community.live2d.com/discussion/2374/cubism-sdk-5-r5-urp-transparentpicking-material-remains-assigned-after-initialization
- 作者 / 日期：`yasu.o@live2d`（**官方账号**）· **2026-07-06**
- 核实深度：**仅标题 / 作者 / 日期级**（正文未取）。
- 为什么值得留：**这是官方账号自己开的帖**，且题材与上一辑的「Unity 6.6 + URP3D 运行时黑屏」
  （/t/3986）同属 **SDK 5 R5 × URP** 组合。→ 结论倾向：**R5 的 URP 通路还有未清的材质侧问题**，
  用 Unity + URP 的先把 SDK 版本钉住，别顺手升 URP。
- 可复用性：`⚠️ 参考`（待取正文后升级判定）。

---

## 二、官方站 / 文档（本轮复测）

| 项 | 本轮实测 | 说明 |
|---|---|---|
| Cubism Editor 下载页 `live2d.com/en/cubism/download/editor/` | 页面可达，但**正文由 JS 渲染 + 非桌面 UA 检测**，抓不到版本号 | 版本号仍只能从 `docs.live2d.com` 的 Release History 表拿（见下） |
| `community.live2d.com/discussions` | **HTTP 200** | 可用，但**分类页正文是 JS 渲染**，`WebFetch` 取不到列表 → 本轮改用 `/categories` 页（服务端渲染，可读） |
| `docs.live2d.com/en/cubism-editor-manual/release-history/` | **404** | 这个 URL 形状是错的；实际 Release History 在 docs 站内另一路径，**下轮待办** |
| 版本口径 | **未变**：正式版 5.3.04 / 5.4 alpha2（**10-18 到期**倒计时 7 天） | 本轮**未能取到比上辑更新的 patch 号** —— `docs` 站路径没找到，**不是「没有新版本」**（负结论只写「本轮未命中」，见 M-0033） |

---

## 三、海外社区复测（退役源纪律：每条带复测）

| 源 | 本轮实测 | 处置 |
|---|---|---|
| `store.steampowered.com` | **200** | **延续上辑回滚结论**（上辑 000 → 200 已回滚），本轮仍可读 |
| `community.live2d.com` | **200** | 可读 |
| `note.com` | **000**（超时） | **维持退役**（本轮未命中，非「不存在」） |
| `zenn.dev` | 未单独复测 | 上辑有产出（`zenn.dev/shakebenn`、`zenn.dev/zeur` 已在索引里） |

---

## 四、⚠️ 本轮剔除：内容农场站群在 Live2D 题材上已经成规模

搜索本轮命中 5 个「文章」，其中 **4 个是同一种洗稿站**：

| 域名 | 样本 URL | 特征 |
|---|---|---|
| `hqwc.cn` | http://www.hqwc.cn/a/1465472.html · http://www.hqwc.cn/a/1073099.html | 「Live2D动画制作全流程」「Python 后端 + Live2D 参数同步」 |
| `bryh.cn` | http://www.bryh.cn/a/316392.html | 「Cubism Editor 5.3 新特性与优化解析」 |
| `tzjp.cn` | http://www.tzjp.cn/news/73233 | 「Live2D Cubism 5.3 混合模式与离屏绘制技术解析」 |
| `mtrt.cn` | http://www.mtrt.cn/news/28320 | 尧图网络「Live2D 集成架构」 |

**统一识别特征（本轮新总结，可直接用于下一轮过滤）**：
1. 开头是「作为一名使用 Live2D 技术**五年**的创作者 / 从业五年的技术美术」这类**匿名资历自述**；
2. **百分比数字密集但全部无法核实**（「参数调节范围扩大约 40%」「效率提升 25%」「内存占用降低 18-22%」
   「权重调整工作量减少约 60%」）；
3. URL 形状固定为 `<域名>/a/<7 位数>.html` 或 `<域名>/news/<5 位数>`；
4. **没有任何信源、没有截图、没有可复现的工程文件**；
5. 同一批域名互相之间内容结构高度同构（都分 1.1 / 1.2 / 2.1 小节，都用「关键技巧：」引出**编造的具体数值**）。

→ **全部剔除**。**注意这些数字是编的**：`Ctrl+D 直接复制图层`、`Alt+双击快速重置参数` 这类
在 Cubism 里就不是这个快捷键（`Ctrl+D` 在 Cubism 里不是「复制图层」），被写进索引会**当成事实传播**。

---

## 五、本路去重报告

- 剔除：上表 4 条内容农场文章（`hqwc.cn` ×2 / `bryh.cn` / `tzjp.cn` / `mtrt.cn`）
- 剔除：`docs.openwebgal.com/en/live2D.html`（WebGAL 引擎的 Live2D 接入说明）——
  WebGAL 已在索引里，且该页只是既有卡片的补充说明，不构成新条目
- 剔除：`handwiki.org` 的 2D 动画软件列表（聚合页，非 Live2D 专项，且内容为 Wikipedia 镜像）
- 保留待取正文（下轮）：`/discussion/2381`、`/discussion/2374`
- 与既有索引的帖号交叉检查：`2389` / `2386` / `2381` / `2374` 在 `csdn-social-summary.md` 与
  `index.html` 中**命中数均为 0** → 全部为新增
