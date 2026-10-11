# 跨平台游戏制作 × AI 开发资源梳理（2026-10-11 · 第二十九辑 · **Live2D × Agent**）

> 本辑候选约 **413 条**（GitHub 8 组搜索去重后），关键词命中且未收录 296 条；中文站群 5 组；官方 2 组。
> 落索引 **18 卡**（`index.html` 1215 → **1233 项**）。
> 上一辑原文存档：`csdn-social-summary-v28.md`（不改，append-only）。

---

## 一、上轮待办检查（12 条 → 闭环 3 条）

| # | 上轮待办 | 结果 |
|---|---|---|
| 4 | **确认 psd2live 的 GPL-3.0 对 `.moc3` 有没有传染性** | ✅ **闭环**（§三.3）—— 找到了可引用的书面依据：**传染的是工具代码，不是产出的模型文件** |
| 1 | **拿一个 `.moc3` 真跑 Ren'Py Live2D** | 🔶 **一半闭环**（§四）—— 「拿不到模型」这个阻塞点解开了，剩「装 Core for Native」 |
| 2 | 实测 `live2d-add-motion-sample-web-ui` | 🔶 **改道** —— 本辑出了个更强的同层工具 `Rev2D`（§三.1），先跑它更划算 |
| 3 | 跑一次 see-through 的 HuggingFace 在线 demo | ⏸ 顺延 |
| 5 | **房规压缩**（连续三轮欠账） | ⏸ **第四轮仍未做** —— 现 200 行 / 上限 200，**已经贴着天花板**，见 §七 |
| 6 | `/skill-doctor` | ⏸ **连续第八轮** |
| 7–12 | `ollama-vscode` / consolidation / 索引加复核日期 / `rpycdec` / Codex 离线 / `_tools` 版本控制 | ⏸ 顺延 |

**本辑额外抓到一条上轮没在账上的问题**（→ §五.2）：**查重基线用的是「插入前」的快照**，
导致 `umamo` 被当成新发现、差点重复入库。是保险丝拦下来的，不是我自查出来的。

---

## 二、本辑主线：前三辑在答「不买 Editor 怎么凑合」，本辑账变了

### 1. 绑定这件事被做成了「一个 JSON」——agent 能写，也能自己证明它对

`RevStudio/Rev2D`（MIT，★7 但**分量很重**）：核心主张是 **一个绑定 = 一个 `*.r2d.json`** ——
参数、骨骼、warp 变形器、部件、关键形绑定、IK、物理、分层动画全在这一个文件里，按 id 寻址、
以画布像素为单位。于是它可以 **diff、可以 review、可以程序生成**。

配套的是一个**无 GPU、无浏览器的确定性渲染器**（同样的模型和输入永远出同样的像素），
加上 **35 条 CLI（全带 `--json`）** 和 **18 个 MCP 工具的 MCP server**，2600+ 测试。

它的工作流被写成一句话：**write the JSON → check it with renders and numbers → fix it with ops → check again**。

> 这句话和我们的房规 #33「规则要能被测」是同一件事，只不过它把它做进了工具里。
> 判据不是「看起来对」，是**渲染图 + `inspect`/`analyze` 的数字**。

**⚠️ 边界要写清楚**：`.moc3` **不支持**（专有未公开二进制）。它能搬的是
**motion3 / exp3 / physics3 / cdi3 / model3 这些 JSON**，美术网格和变形器搬不了。
→ 它不是「替代 Live2D」，是「**在 Live2D 旁边给 agent 一个可写的沙盘**」。

### 2. 「绕开 Editor」整件事的账，被官方学生优惠重算了

前三辑花了大力气研究怎么不买 Editor。本辑查到官方 **Live2D Student Discount Program**：

| 项 | 值 |
|---|---|
| 内容 | Cubism **PRO** · indie · **三年**计划 |
| 价格 | **$238.20 → $57.16**（76% OFF） |
| 性质 | 一次性买断、**不自动续费**、**功能与标准 PRO 相同** |
| 毕业后 | **可继续用到订阅期满** |
| 中国区 | `live2d.jp/chn/student-discount`，**没有学校邮箱也可用「学信网验证码」申请** |
| LEAP | 另有一个教育支援计划：向教育**机构**无偿提供 Editor PRO 授权（已 200+ 家） |

⚠️ **口径打架**：英文学生页写 **76% OFF**，日文官网首页写 **80% OFF**，中文二手教程写「2.4 折」
（= 76% off）。**以结算页为准，别信宣传语**。

> 这条不是「又一个工具」，它是把前三辑绕路的**时间成本**重新标了价。
> 三年约 ¥450 —— 对在校生来说，这可能比继续绕路便宜。

### 3. 上一辑收录的 umamo，本辑复核：进展是真的，但还不是能用的那天

`umamoorg/umamo` 上一辑（v33 / 信源 [1207]）已收录，当时 ★149。本辑复核 ★151，README 现在明确：

- **CMO3 与 MOC3 双向导入导出，兼容到 Cubism 5.4**（上一辑只说「读写 `.cmo3`」）
- 新增 CLI：`dump`（把模型内容打到 stdout）· `convert`（cmo3↔moc3，其中 cmo3→moc3 会一并产出
  model3.json / cdi3.json / 贴图）· `diff`（两个模型语义级对比）· `extract`（解包成明文 main.xml + 分层 PNG）
- 仍然 **alpha**（README 原话：请定期备份，拿副本去玩，别用原件）· **动画功能仍未实现**

⚠️ 一个必须说出口的点：**格式知识是「黑盒观察逆向」出来的**（README 原文
*reverse-engineered by black box observation*）。而官方免费素材 EULA §4.1.3 是**禁反向工程**的。
两者之间有没有张力、有多大，我不做裁断 —— **但商用前必须自己想清楚**，本辑只登记事实。

---

## 三、本辑最值钱的五条（按对这位用户的实际价值排序）

### 1. Rev2D（§二.1，已展开）· MIT · 推送 2026-10-06 · 索引 [1215]

### 2. 官方学生优惠（§二.2，已展开）· 索引 [1217]

### 3. live2d-agent-kit —— 上轮 #4 的法务答案在这里

`Ariakage/live2d-agent-kit`（★26，Python，带 `SKILL.md`）：帮 Codex 和其他 coding agent
把参考图 / 分层 PSD 做成能跑的 `.moc3`。真正值钱的是它的 `THIRD_PARTY_NOTICES.md`：

| 东西 | 许可 |
|---|---|
| kit 自己的代码与文档 | **MIT** |
| `integrations/psd2live/*.kt` 与 `patches/psd2live-agent-kit.patch` | **GPL-3.0-only**（因为和 GPL 引擎一起编译） |
| psd2live 本体 | 只下载到被忽略的本地缓存，**不随包分发**，保留原 LICENSE |
| 示例资产（Pink Sakura） | **CC BY 4.0**（与代码许可分开） |

→ **GPL 传染的是工具代码，不是它产出的模型文件。**
一句话总结它自己的说法：**licensing those assets does not relicense their tools**。

⚠️ 这**不是法律意见**，但终于有了一份**可引用的书面依据**，不再是「大家都这么觉得」。

它还摊开了一条很重要的顺序经验：**先修拆层和遮罩，再做超分** ——
混入发片的衣服像素会跟着头发动，提高分辨率只会让断口更明显。

### 4. 《一张立绘自动生成 Live2D，最后是怎么散架的》—— 不是工具，是判据

第一手失败实录（note.com/dn0288）。作者做了全自动流水线，**23 个测试全过、29 个部件齐全、
Cubism Viewer 里能加载**。然后插进真实立绘一动就散架：长发形状套不上短发、肩部冒出重复部件、
眼嘴位置对不上导致重叠或消失、脸/脖子/躯干接缝露缝。

作者的结论 —— **单张立绘里根本不包含「让它动起来」所需的那些信息**：
刘海挡住的眼睛、闭着的嘴里的牙齿舌头、被头发衣服挡住的脖子肩膀、正面图推不出的侧脸与后脑深度。

> **自动化能帮你把「文件生成」跑通，但跑通 ≠ 能上直播 / 能进游戏。**
> 缺的那部分不是 AI 精度问题，**是原图里就没有**。
> 生成式 AI 能「像那么回事地补全」，但**「像那么回事」≠「原作者想要的那个正确答案」**。

→ 上一辑我们有反证、本辑有正面证据；这条把两半合成**一句完整判断**。
**以后再看到「一张图自动生成 Live2D」的宣传，先拿它对一遍。**

### 5. Live2D × 编码 agent 的桌宠集群（2026-09/10 集中爆发）

这一个月 GitHub 上冒出一整片「把编码 agent 的状态接到 Live2D 上」的项目：

| 项目 | 支持的 agent | 备注 |
|---|---|---|
| `joyparkray/agent-avatar`（★1，MIT） | **Claude Code · Codex · Hermes · DeepSeek Harness · WorkBuddy** | 五个连接器，有文档化 Bridge Protocol |
| `cyanfish-x/dsh-live2d-pets`（★30，MIT） | **DSH** | `dsh plugin --profile web add` 一行装；渲染栈停在 **Core 4** |
| `ankesu/dsh-live2d-pet`（★4）· `A8Chann/dsh-pet-live2d`（★38） | DSH | 同题重复实现，别装重 |
| `XucroYuri/L2MAS`（★9） | MCP + A2A 多 agent | 更实验 |

⚠️ **两条都要小心**：
① **要不要往主力 agent（WorkBuddy / DSH）里装第三方插件，得人先审一遍再装** —— 别让 agent 自己装；
② `dsh-live2d-pets` 的栈停在 **Cubism Core 4**，按上一辑的 ABI 结论，
**它对 Cubism 5.3+ 导出的模型可能不吃**。

---

## 四、本机实测：`.moc3` 拿到了（上轮欠账 #1 的一半闭环）

上一辑卡在「`git clone` 被挡，拿不到模型文件」。本辑绕过去了：

```sh
# 官方样例模型其实就在官方仓库里
gh api "repos/Live2D/CubismUnityComponents/git/trees/HEAD?recursive=1" --jq '.tree[].path' | grep '\.moc3$'
#   → Clipping / Koharu / Mao / Natori / Ren / Rice  六个
gh api "repos/Live2D/CubismUnityComponents/contents/Assets/.../Mao/Mao.moc3" --jq .content | base64 -d > Mao.moc3
```

实测下载成功：`Mao.moc3` **879,680 字节**，文件头是 `M O C 3` + **版本字节 0x05**。

- ✅ **「拿不到模型」这一半闭环了**
- ⏸ **还剩一步**：Ren'Py 需要 `CubismSdkForNative-5-r.1.zip`（Core ≥ 5.3）放进 SDK 目录，
  再用 launcher 装一次。这一步要下官方 zip，**本辑未做**
- ⚠️ 版本字节 **5** 与上一辑 PurismCore COMPAT.md 的对照表（v5 ABI = Core 5.1）在数字上一致 ——
  但**Ren'Py 到底吃不吃没实测**，别当成结论

---

## 五、两个方法层面的落地

### 1. gamemale 复核：判定成立，不再单独投入

用户本辑再次点名 gamemale。复核结果：HTTP **200**，但返回的是
**Cloudflare Turnstile 挑战页**（`<title>请稍候...</title>` + `challenges.cloudflare.com/turnstile`）。

→ 这不是登录墙，是**全站人机验证**。上一辑「结构性不可取」的判定成立。
**本辑及以后不再单独投入**（与 Reddit / itch / Steam / note / Medium / YouTube 同源，见 `AGENTS.md` §八.7）。

### 2. ⚠️ 新坑：查重基线用了「插入前」的快照

本辑差点把 `umamo` 当新发现再入库一次。原因是我的查重清单一路用的是 `_r28/_dedupe_gh.txt` ——
那是**上一辑插入之前**生成的快照，**不含上一辑自己刚插进去的 16 张卡**。

拦住它的是 `insert_v34_cards.py` 里那句「仓库已存在就拒绝」，**不是我自查出来的**。

→ 已写进 `AGENTS.md` §八.3：**查重基线必须从 `index.html` 当前内容现取，不能用历史快照**。
（这已经是第三次「闸门救了我，而不是我救了闸门」，见 §七待办 #9。）

---

## 六、AI 贴核实：读了 7 条，采纳 3 条

| 贴 / 项目 | 判定 |
|---|---|
| `RevStudio/Rev2D` | ✅ **采纳**（§二.1）—— 本辑最高分：MIT、可 diff 的 JSON 格式、18 个 MCP 工具、2600+ 测试 |
| `Ariakage/live2d-agent-kit` | ✅ **采纳**（§三.3）—— 上轮法务欠账的答案，且带 `SKILL.md` |
| `cyanfish-x/dsh-live2d-pets` | ✅ **采纳**（§三.5）—— 本机在跑 DSH，现成可装；但先确认模型是 Core 4 还是 5 |
| `joyparkray/agent-avatar`（支持 WorkBuddy） | 🔶 **观察** —— 方向对，但 1★ / 创建 5 周 / 要重启 WorkBuddy；**今天不装进主力** |
| `myths-labs/prometheus-avatar`（LLM 驱动 Live2D） | ❌ **不采纳** —— 上一辑已判过：单机 VN 对话是写死的，Ren'Py 无法在运行时改单个参数 |
| note.com 全自动失败实录 | ✅ **采纳为判据**（§三.4）—— 不是工具，但以后用来筛「一键生成」的宣传 |
| `johal.in` 那篇「Ren'Py 9.0 Live2D Layers」 | ❌ **判为编造** —— 它写 `config.live2d_fps = 60`、还给了「2025 Ren'Py Community Benchmarks / Snapdragon 778G / Fluidity Score 96.2%」这类数字。
  **Ren'Py 真正的开关是 `config.gl2 = True`**（本机 `config.py:1050` 已核实），**没有 `config.live2d_fps`**。→ **M-0028 的又一个实例：LLM 在小众垂直软件上编造选项** |

**一条独立的真人佐证**：中文长篇实战帖《live2D 全栈制作教程/避坑》里作者写
「**问 AI 很难解决这类问题，他们会一直编造软件的功能**」——
这是**被坑的一方**写下来的，和我们从工具侧总结的 M-0028 对上了。

---

## 七、索引与文档维护（本轮落盘）

- `index.html` **1215 → 1233 项**（卡片 1204 → 1222，第三十四版增补 **18 卡**，脚注 [1215]-[1232]，
  新建 `insert_v34_cards.py`；跑前过 `insert_guard_probe.py` **6/6**，跑后 `index_metrics --update` 重封 **304** 个分组）
- 恒等式：页头 1233 == 最大脚注 1232 + 1 ✅ · div 10213 / 10213 ✅
- 上一辑存档 `csdn-social-summary-v28.md`
- `AGENTS.md` §八.3 补：**查重基线从 `index.html` 现取**；§八.7 补 gamemale 的 Turnstile 证据
- 本辑候选约 **413 条**（gh 8 组 / cn 5 组 / official 2 组），落索引 18 条
- 新增错误记忆 **M-0031**（查重基线过期）

---

## 八、下一辑待办

**本辑新出**

1. **实测 `Rev2D`**（本辑最高分，仍只有 README 级核实）：`npm install` → 跑 CLI → 导出一个
   `.motion3.json` → 拿回 Cubism Viewer 验一遍。Node ≥22 本机有
2. **装官方学生优惠**（§二.2）：用户是在校生，**学信网验证码**那条路不需要学校邮箱。
   这是本辑唯一一条「今天就能落地、且直接省钱」的事
3. **补完欠账 #1 的后一半**：下载 `CubismSdkForNative-5-r.1.zip` → 装进 Ren'Py → 用 `Mao.moc3` 真跑一次
4. **房规压缩** —— **连续第四轮欠账，且已经 200/200 贴顶**。下一辑**第一件事**就干，
   按上一辑倾向的方案 ②：把「调研方法」类条款整体拆进 `game-production-pipeline.md`
5. **给 `_r28/_dedupe_gh.txt` 这类历史快照加个「生成日期 / 来源 commit」标注**，
   或者在 `insert_vN_cards.py` 里改成**直接从 `index.html` 现取查重集合**（治本）

**承接老账（顺延）**

6. `/skill-doctor`（**连续第八轮**）· 7. 装 `ollama-vscode` + 跑 `agnix` · 8. 做一次 `consolidation`
9. **索引条目加「最后复核日期 + 是否作废」** —— 本辑 `umamo` 那次差点重复入库，
   如果卡上有复核日期就不会发生；这条从「欠了七轮」升级为**有具体事故驱动**
10. `rpycdec` 反编译自查（**欠十二轮**）· 11. Codex 离线 / 词表 / 模型分档 · 12. `_tools/` 纳入版本控制

---

*本辑新增约 413 条候选（GitHub 8 组搜索去重后；关键词命中且未收录 296 条），落索引 18 卡；*
*累计经验帖约 1283 → **约 1370 条**；索引 **1233 项**；房规 22 条 / 200 行（贴顶）；mistakes **31 条**；*
*新建脚本：`insert_v34_cards.py`；新存档：`csdn-social-summary-v28.md`。*
