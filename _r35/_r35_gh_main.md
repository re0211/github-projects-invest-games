# 第三十五辑 · gh 路（GitHub / Gitee / HF：Live2D 制作相关新增与重大更新）

> 检索窗口：`pushed:>2026-09-01`（关键链条放宽到 08-01）
> 去重基线：`_r35/_dedupe_gh.txt`（1317 条已收 owner/repo）+ `csdn-social-summary.md` / `-v34.md` / `-v33.md`
> 可复用性基准：**16GB 内存 Windows、跑本地 Ollama、维护静态索引站的个人开发者**（非企业、无 GPU 集群）
> 数据来源：全部走 `gh api` / GraphQL **逐条实测**（★ / license / 主语言 / pushedAt / updatedAt / archived）

---

## A. ⭐ 本辑最重：AI「拆层 → 自动绑定」的完整流水线第一次成形

> 前几辑的主线是「绕开 Cubism 的格式线」（自己解 moc3）；**本辑变了**：出现了
> **「单张立绘 → See-Through 拆层 → psd2live 自动绑定 → moc3 → VTube Studio」**这条
> **端到端可跑、且有人贴出显存实测**的路径。四个仓库互相引用、构成同一条链。

### A1. `tsunehimatoi/psd2live` —— 把 PSD 自动绑成 Live2D 模型（★614 · Kotlin · NOASSERTION）
- URL：https://github.com/tsunehimatoi/psd2live
- 实测：★614 · Kotlin · NOASSERTION · **推送 2026-10-11**
- 事实：这一链条里的**核心件**（其余三条都在调用它）。把一个分层 PSD 自动变成可驱动的 Live2D 模型。
- 可复用性：**⚠️ 参考（不是 ✅，理由在下面）** —— 它是「自动绑定」这个环节目前★最高、最活跃的实现，
  **但这台机器上跑不了**：Kotlin + 极可能依赖 Cubism 官方链路；且它的**输出质量上限就是「首版」**——
  下面 A2/A3 的作者自己的结论也是「先出首版、后面还得手工修」。**当作流水线的「绑定段」来理解，不要当成品。**
- ⚠️ 待下轮补：**许可证写的是 NOASSERTION**（仓库里有 LICENSE 但 GitHub 认不出）→ **用于商业前必须人工读 LICENSE 原文**。

### A2. `flowingduskpro/jpg-to-live2d-workflow` —— 单张 JPG 到可动模型，**带 8GB 显存实测**（★4 · Python · MIT）
- URL：https://github.com/flowingduskpro/jpg-to-live2d-workflow
- 实测：★4 · Python · MIT · 推送 2026-09-14 · 更新 2026-10-07
- 事实（仓库自述）：**从单张 JPG 插画到可驱动的 Live2D 模型**：`See-Through 拆层 → 分层 PSD → psd2live 自动绑定 → moc3 → VTube Studio`；
  **并含「8GB 显存上的实测性能与精度结论」**。
- 可复用性：**✅ 落地** —— **这是本辑对你这台机器最直接有用的一条**。理由：① 它是**工作流说明 + 脚本**，不是要你装大 SDK；
  ② 显存门槛 **8GB**，你的机器（16GB RAM + 若有独显）大概率跨得过；③ MIT；④ 它把「精度结论」写出来了 ——
  即**它自己承认哪里做得不好**，这正是要抄工作流时最需要的部分。
- ⚠️ 注意：★ 只有 4 —— **不是「成熟工具」，是「一个人的实验记录」**。价值在路线与数字，不在代码质量。

### A3. `lvhaojie456/image-to-live2d` —— 一张立绘/一句 prompt → 首版 Live2D（★2 · Python · MIT）
- URL：https://github.com/lvhaojie456/image-to-live2d
- 实测：★2 · Python · MIT · 推送 2026-09-22 · 更新 2026-09-29
- 事实（自述）：`One portrait or prompt → a first-pass Live2D model (moc3 + Cubism project)`：
  **AI planning + See-through decomposition + measured expressions + psd2live rig**。
- 可复用性：**⚠️ 参考** —— 比 A2 更「自动化」（多了 AI planning 与 prompt 入口），但 ★ 更低、且更强调「首版」。
  与 A2 是**同一条链的两种封装**，读一份即可；两份一起读能看出**哪些步骤是被反复重写的**（那些步骤就是真正的瓶颈）。

### A4. `daoming07280/live2d-auto-pipeline` —— 同链路的 **RTX 4060 实测**记录（★0 · Python · MIT）
- URL：https://github.com/daoming07280/live2d-auto-pipeline
- 实测：★0 · Python · MIT · 推送 2026-09-18
- 事实（自述）：`Live2D auto pipeline: See-through 768/30 + psd2live workflow notes, scripts, and sample moc3 results (RTX 4060)`。
- 可复用性：**⚠️ 参考** —— **它与 `mw2wbyys6t-sudo/live2d-auto-pipeline`（已在索引里）是「同名不同 owner」**，
  上一辑已判「纯同名巧合」，本辑复现该结论：**两者内容不同，但都指向同一条 See-Through + psd2live 链路**。
  → **值得记的是「这条链路有多个人在各自跑」这件事本身**，说明它不是孤例。
- ⚠️ 注意：「`768/30`」是 See-Through 的分辨率/帧数或版本参数，**未在仓库外得到证实**，照录不自证。

### A5. `sweetcornna/OneClick2D` —— 「一键 2D」的**可行性优先**工具包 + 开放规范（★0 · Python · 无 license）
- URL：https://github.com/sweetcornna/OneClick2D
- 实测：★0 · Python · **无 license（licenseInfo 为空）** · 推送 2026-08-08（**早于窗口，属边缘收录**）
- 事实（自述）：`Feasibility-first, privacy-conscious toolkit and open specification for turning
  rights-cleared anime illustrations into inspectable, editable 2D avatars`。
- 可复用性：**⚠️ 参考** —— 唯一把**「版权已清（rights-cleared）」写进定位**的同链条项目，
  且强调「可检查、可编辑」（反「黑盒一键」）。**无 license = 默认保留全部权利**，**不能拿来直接用**，只能读它的规范思路。

---

## B. DSH / AI agent 桌宠的「身体」—— 本辑继续密集（承接上辑待办④「DSH 生态单独成辑」）

### B1. `A8Chann/dsh-pet-live2d` —— DSH Web GUI 的 Live2D 桌宠插件（★38 · JavaScript · NOASSERTION）
- URL：https://github.com/A8Chann/dsh-pet-live2d
- 实测：★38 · JavaScript · NOASSERTION · 推送 2026-10-10
- 事实（自述）：**DSH Web GUI 的 Live2D 桌宠插件**：可拖动、跟随鼠标、**跟着会话状态换动作与表情**、右键面板可换装。
- 可复用性：**✅ 落地** —— 与上辑 `duty-on`（Tauri，桌宠当 agent 状态灯）**是同一个设计思想的两条实现**：
  「**桌宠不承载智能，只做 agent 状态的显示器**」。你在用 DSH，这条是**可以当场装的**（JS 插件、40★ 量级、当天还在推）。
- ⚠️ license 为 NOASSERTION → 自用无碍，**再分发前读 LICENSE 原文**。

### B2. `mhmdalsaisi/ds-pet` —— 「看鲸鱼对 DSH 会话的反应」（★0 · JavaScript · NOASSERTION）
- URL：https://github.com/mhmdalsaisi/ds-pet
- 实测：★0 · JavaScript · NOASSERTION · 推送 2026-10-11
- 事实（自述）：`Watch a cartoon whale on your desktop react to DeepSeek Harness sessions in real time.`
- 可复用性：**⚠️ 参考** —— 和 B1 同题材（DSH 状态外显），但★0、且是**占位性的小玩物**。
  收录理由：**它是「DSH 桌宠」这个品类在两轮内出现的第 3~4 个实现**（上辑 duty-on / dsh-live2d-avatar，本辑 B1 / B2），
  这类项目的**增量已经足够单独成一辑**（见本辑待办）。

### B3. `Maboroshinatsu/maibot-deskpet-plugin` —— MaiBot 的 Live2D 桌面伴侣插件（★7 · TypeScript · **GPL-3.0**）
- URL：https://github.com/Maboroshinatsu/maibot-deskpet-plugin
- 实测：★7 · TypeScript · **GPL-3.0** · 推送 2026-10-11
- 事实（自述）：`基于 Electron + Vue3 + PixiJS + Live2D Cubism 4 的 MaiBot 桌面宠物插件`。
- 可复用性：**⚠️ 参考** —— 技术栈（**Electron + Vue3 + PixiJS + Cubism 4**）是「给已有聊天机器人挂身体」的**标准配方**，
  想复刻时可直接照这套选型；但 **GPL-3.0** —— 二次分发必须开源，做闭源产品会咬人。

---

## C. 桌面伴侣 / 桌宠（宿主技术栈在换代：Tauri / Rust / 原生 OpenGL 变多）

### C1. `ochiru520/Mio` —— Windows 本地优先的个人 AI Agent（★49 · Python · MIT）
- URL：https://github.com/ochiru520/Mio
- 实测：★49 · Python · MIT · 推送 2026-10-11
- 事实（自述）：`Windows 本地优先的个人 AI Agent —— conversations, memory, diary, voice, QQ, Live2D, and screen awareness`。
- 可复用性：**✅ 落地** —— **MIT + Python + Windows 本地优先**，与你的栈（本地 Ollama、Windows、Python）**逐条对得上**；
  且功能面是「对话 + 记忆 + 日记 + 语音 + QQ + Live2D + 屏幕感知」——**可当作「一个人怎么把 Live2D 塞进一个完整 agent 应用」的参考架构**。
- ⚠️ 注意：功能多 = 每个都浅。**当架构参考，别当全能工具**。

### C2. `chengyuZou/EmaAgent` —— Tauri + React + Fastify 的桌面伴侣，带「独立叙事 RAG」（★3 · TypeScript · MIT）
- URL：https://github.com/chengyuZou/EmaAgent
- 实测：★3 · TypeScript · MIT · 推送 2026-10-11
- 事实（自述）：`desktop-first AI companion agent built with Tauri + React + Fastify.
  Featuring a Live2D stage, local SQLite memory, and an independent Narrative RAG`。
- 可复用性：**⚠️ 参考** —— 亮点是 **「叙事 RAG」与「普通记忆」分开存**（local SQLite）这个设计；
  Tauri 栈比 Electron 轻，适合 16GB 机器。★ 很低，是早期项目。

### C3. `Hisakazu333/NekoPapa` —— Tauri + Rust + C++/OpenGL 原生舞台的跨平台 Live2D 伴侣（★0 · TypeScript · Apache-2.0）
- URL：https://github.com/Hisakazu333/NekoPapa
- 实测：★0 · TypeScript · Apache-2.0 · 推送 2026-10-10
- 事实（自述）：`基于 Tauri、React、Rust 与 C++/OpenGL Native Stage 构建的跨平台 Live2D 桌面伴侣`。
- 可复用性：**⚠️ 参考** —— **Apache-2.0（对商用最友好）+ 原生 OpenGL 舞台**；
  但★0、C++/OpenGL 那层意味着**编译门槛高**（你这台机器要过这一关不轻松）。价值在「许可证宽容度」这个维度。

### C4. `waifuai/waifu-companion` —— 纯浏览器的 Live2D 伴侣（★38 · JavaScript · **MIT-0**）
- URL：https://github.com/waifuai/waifu-companion
- 实测：★38 · JavaScript · **MIT-0** · 推送 2026-10-11
- 事实（自述）：`Browser-based AI companion with Live2D characters, voice chat and long-term memory`。
- 可复用性：**✅ 落地** —— **MIT-0 是本辑遇到最宽松的许可（≈公共领域，连署名都不要求）**，
  且**纯浏览器**（不需要装任何桌面运行时）→ 对「静态索引站想挂个会聊天的看板娘」这条需求最贴近。
- ⚠️ 注意：浏览器里跑，**模型与推理得外接**（自述没说是本地推理）。

### C5. `kongweiguang/xiaoya`（小芽）—— 中文数字人助手，MCP 工具扩展（★1 · TypeScript · MIT）
- URL：https://github.com/kongweiguang/xiaoya
- 实测：★1 · TypeScript · MIT · 推送 2026-10-11
- 事实（自述）：`小芽：会听、会说、会行动的中文数字人助手。实时语音对话与自然打断、Live2D 神态与口型同步、本地语音处理及 MCP 工具扩展`。
- 可复用性：**⚠️ 参考** —— **中文 + MCP + 本地语音**这三个关键词组合很少见；
  但★1，属刚起步。**「自然打断」是数字人里最难的交互点之一**，值得盯。

### C6. `fswolf/luna-local-agent` —— 全本地语音伴侣（Whisper 进 / Kokoro 出）（★4 · Python · MIT）
- URL：https://github.com/fswolf/luna-local-agent
- 实测：★4 · Python · MIT · 推送 2026-10-11
- 事实（自述）：`fully local, private AI voice companion you can see inside: Whisper speech in, Kokoro voice out, memory, tools, plugins and moods`。
- 可复用性：**✅ 参考** —— **「Whisper in + Kokoro out」是一套明确可替换的本地语音方案**，
  和你「本地 Ollama」的路子同源（全本地、隐私优先）。想给自己的东西加语音时的选型参考。

### C7. `loliRuriruri/HoloDori` —— 纯 Rust 的 Live2D Manager（导入/构建/预览/当桌宠）（★0 · Rust · 无 license）
- URL：https://github.com/loliRuriruri/HoloDori
- 实测：★0 · Rust · 无 license · 推送 2026-10-01
- 事实（自述）：`HoloDori Live2D Manager — import, build and preview Live2D models with motions,
  expressions and physics, then run them as desktop characters or Window...`
- 可复用性：**⚠️ 参考** —— 与 `MahouTechnologies/moc3-rs`（★6，已在索引）同属 **Rust 阵营**；
  **无 license → 不能直接用**。价值在「Rust 侧又添一个解析/预览实现」。

### C8. `An-d-u/ENE` / `celestial-sora/vivian` / `nyan-mikan/codex-live2d` —— 同品类的三个小实现（★1 / ★1 / ★0）
- `An-d-u/ENE`（★1 · Python）：桌面伴侣 + 笔记/情绪/语音/日历工作流 · 推送 2026-10-11
- `celestial-sora/vivian`（★1 · TypeScript）：`mobile-first Live2D AI companion`（Next.js + PixiJS + Cubism 4）· 推送 2026-10-07
- `nyan-mikan/codex-live2d`（★0 · JavaScript）：**给 Codex 桌面端**做的 Live2D 伴侣，`local model profiles, streamed speech` · 推送 2026-10-11
- 可复用性：**⚠️ 参考（合并登记）** —— 三条都是★1 以下的早期项目。**合并收在这里的理由**：
  它们印证了同一件事 —— **「给某个 AI 编码工具配一个 Live2D 身体」已经成了重复出现的模式**
  （Codex 有、DSH 有、MaiBot 有）。这是趋势信号，不是工具推荐。

### C9. `RifkyA911/mirunova-live` —— 纯客户端 Web Live2D/3D 视觉追踪（★0 · Svelte · 无 license）
- URL：https://github.com/RifkyA911/mirunova-live
- 实测：★0 · Svelte · 无 license · 推送 2026-10-11
- 事实（自述）：`Next-Gen Web Live2D & 3D Avatar Vision Tracker • 100% Client-Side • Powered by Bun & SvelteKit`。
- 可复用性：**⚠️ 参考** —— 「**100% 客户端**的视觉追踪」这个定位（摄像头数据不出本机）在隐私维度上有价值；
  但★0、无 license。

---

## D. 格式 / 渲染线（本辑增量较小）

### D1. `haneoka-gakuen/vega-plugin-cubism` —— 「Vega」插件宿主里的 Cubism 2–5 支持（★0 · TypeScript · MPL-2.0）
- URL：https://github.com/haneoka-gakuen/vega-plugin-cubism （同组织另有宿主 `haneoka-gakuen/vega` 等 5 个插件）
- 实测：★0 · TypeScript · MPL-2.0 · 推送 2026-10-11
- 事实（自述）：`Live2D Cubism 2–5 characters and lip sync for Vega`。同组织下有
  `vega`（宿主）/ `vega-plugin-cubism` / `vega-plugin-composite` / `vega-plugin-haneoka` / `altair-plugin-models`。
- 可复用性：**⚠️ 参考** —— **「插件宿主 + Cubism 插件」这种分层**在 Live2D 生态里不多见
  （别家基本是单体应用）。**MPL-2.0 是文件级 copyleft，比 GPL 温和**。★0、全部为 0，属早期。
- ⚠️ 同一组织的 5 个仓库**只收这 1 条**（其余是骨架/配置），避免灌水。

### D2. `Type010/live2d-web` —— moc3 做网站看板娘 + 面板控制（★0 · TypeScript · 无 license）
- URL：https://github.com/Type010/live2d-web
- 实测：★0 · TypeScript · 无 license · 推送 2026-09-30
- 事实（自述）：`将 moc3 模型用于网站看板娘，支持面板控制：切换背景、装饰、表情`。
- 可复用性：**⚠️ 参考** —— 与 CN 路的 A1/D5/F3（看板娘自托管）是同一需求的不同实现；**无 license**。

### D3. `rydanee/live2drust` —— 简易 .moc3 查看器（★0 · Rust · 无 license）
- URL：https://github.com/rydanee/live2drust
- 实测：★0 · Rust · 无 license · 推送 2026-09-23
- 可复用性：**❌ 不采用（本轮）** —— 自述就一句 `A simple .moc3 model viewer with more to come :)`，
  没有任何比 `MahouTechnologies/moc3-rs`（已在索引）更多的信息。**登记以免下轮重复发现**。

### D4. `julfed7/Cubism-2` —— GDScript 侧的空仓库（★0 · GDScript · 无 license · 无描述）
- URL：https://github.com/julfed7/Cubism-2
- 实测：★0 · GDScript · 无 license · **无 description** · 推送 2026-10-11
- 可复用性：**❌ 不采用** —— **无描述 + 无 license + ★0**，无法判定用途。登记以说明「搜到了但不收」。

### D5. `lilyco-42/ly_motion` —— Rust 动效/骨骼绑定引擎（★0 · Rust · MIT）
- URL：https://github.com/lilyco-42/ly_motion
- 实测：★0 · Rust · MIT · 推送 2026-10-11
- 事实（自述）：`Rust 动效/动画引擎：图片素材运动 · 高效骨骼绑定 · 类 PCL 的 UI 动效 · 类 manim 的声明式出片`。
- 可复用性：**⚠️ 参考** —— **注意：它自称要解决的是「2D 骨骼绑定」的通用问题，不是 Live2D 格式兼容**；
  与 `rig-c/core`（上辑，编译到 Spine 4.3）属**不同的绕开路线**（那条出 Spine，这条出自家的动效引擎）。

---

## E. 边缘登记（低价值 / 待复核）与剔除

- `P1kaj1uu/ChattyPlay-Agent`（★949 · TypeScript · Apache-2.0 · 推送 2026-10-11）：**仅边缘登记** ——
  自述是「多平台视频聚合 + 4K 解析下载」工具，**Live2D 只是附带标签**，与「Live2D 制作」无关 → **不单独成条**。
- `MetaSekaiLab/nnnotes`（★15、命中基线）：上辑已收，**本辑复现「双仓 fork 只收本体」的结论** → 不重复。
- `airisu-dev/experiment-rn-live2d`（★0 · TypeScript · MIT · 无描述 · 推送 2026-10-11）：RN 实验，无描述 → 仅登记。
- `julfed7/Cubism-2` / `rydanee/live2drust`：见 D3 / D4。
- **同名不同 owner（复现上辑结论）**：`mw2wbyys6t-sudo/live2d-auto-pipeline`（已收）× `daoming07280/live2d-auto-pipeline`（本辑新增）
  → **仍是巧合，但两条指向同一条 See-Through + psd2live 链路**（见 A4）。

---

## F. 本路去重报告

**去重方法**：检索得到的每个候选都跑
`grep -icF "<owner/repo>" _r35/_dedupe_gh.txt`（基线**从 `index.html` 现取**，非历史快照 —— 历史快照会把上一轮刚入库的
东西当新发现，M-0031）。

**结果**：48 个候选中 **26 个命中基线（已收，全部剔除）**，**22 个未命中（新增）**。

**命中即弃清单（部分）**：
`moeru-ai/airi`(★50276) · `DasterProkio/awesome-ai-companion` · `umamoorg/umamo` · `jianchengwang/live2d_models` ·
`KurisuMakise004/renderkit` · `MahouTechnologies/moc3-rs` · `SakuraMotion/PurismCore` · `Wzhang3912/image2live2d` ·
`fifteen42/live2d-from-art` · `funlin724/emote-to-cubism` · `canyueY/pyqt-live2d-bridge` · `Yoru-KenomoVT/ayatsuri_2d` ·
`henceketh/inochi2d-autorig-claude` · `turboism/Turboism` · `ptghb/virtual-person` · `Hera-Berg/open-avatar-creator` ·
`Andersen216/dsh-whale-girl-live2d` · `Hana-ame/moc3-json-viewer` 等。

**⚠️ 本路最重要的方法学发现（已写进待办）**：
**`gh api repos/<x>` 返回 404，不等于仓库不存在。** 本机实测 `kitao/pyxel`（★1.4 万级、当天仍在提交）
经 `gh api` / `curl api.github.com` 全部 404，而 WebSearch 证明它活跃存在（v2.9.9，2026-08-12 提交）。
同批 38 个「查不到」的仓库里包含 `block/goose` / `fabricmc/fabric` / `hiyouga/LLaMA-Factory` / `pytorch/torchtune`
等**一线项目** → 判定为**本机网络层（代理）对未缓存路径返回 404**。
→ **纪律**：查到 404 时，**不许写成「已死链/不存在」**，要写「**本轮 API 未命中，原因未定**」，
并换第二种通道（search API / WebSearch / 镜像页）交叉验证。**负结论只写「本轮未命中」（M-0033 家族）。**
