# 游戏制作流水线 · 工具决策参考

> 当用户说"我要做游戏"时，按这份清单推荐工具。
> 来源：1300+ 已收录 GitHub 项目 + 经验帖 + AI 官方博客 · 原则：**免费优先，AI 辅助优先，个人开发者优先**
> ⚠️ 本文件自带上限 **200 行**；超了**压正文、不撤条款**（条款 = 下面的《决策原则》）。

---

## Step 0：选引擎（最关键的决策）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 纯新手，第一次做 | **Godot 4.7**（r?） | 免费、轻量、GDScript 像 Python，AI 写 GDScript 错误率最低 |
| 2D 像素/休闲；3D 独立（含 VR/AR） | **Godot** / **Raylib**（2D 纯代码） | Godot MIT 无授权费、有完整编辑器；Raylib 无引擎绑定 |
| 微信/移动端小游戏 | **Cocos Creator** 或 **Unity** | 平台支持成熟 |
| 文字/视觉小说 | **Ren'Py** 或 **TyranoScript** | 零代码，直接写剧本 |
| 快速原型（不写代码） | **Rosebud AI** 或 **Claude Fable 5**（Artifacts） | 对话出可玩 demo，10 分钟 |
| 对话式游戏（不碰代码） | **narrat** | 剧情写配置文件，自带存档背包技能检定 |

**决策口诀**：不会代码 → Summer Engine / GDevelop；会代码想快 → Godot + Cursor / Everything Game Dev Code；想完全 AI 代写 → Summer Engine / OpenGame / Godogen

---

## Step 1：策划 & 设计文档

| 做什么 | 用什么 | 怎么用 |
|--------|--------|--------|
| 生成创意/核心玩法 | ChatGPT / Claude / DeepSeek | "你是资深游戏制作人，帮我把这个点子压成最小可玩版本" |
| 写 GDD（游戏设计文档） | Claude（思考模式） | 贴核心创意 → 输出结构化 GDD → 追问 3 轮砍范围 |
| 数值设计/难度曲线 | DeepSeek V4-Pro | 让它算数值表，但**自己验证** |
| 关卡设计 | Godot TileMap / Tiled Map Editor | 手动摆 + AI 辅助生成布局 |
| **AI 砍规格（最有用）** | Claude / Gemini | 把 GDD 贴给它，让它当"恶毒制作人"指出该砍什么 |

**经验法则**：先让 AI 砍规格，AI 列的 MVP 通常还能再砍 30%。

---

## Step 2：美术素材

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 概念图/风格定调 | Midjourney / Leonardo AI | 先定风格再量产 |
| 像素角色/sprite | **Aseprite**（$20 买断）/ **Pencil2D**（免费） | Aseprite 有动画功能 |
| 批量生成 UI 图标 | Midjourney + 风格锁 | 用同一 prompt seed 批量 |
| 3D 建模 / 图生 3D | **Blender**（免费）+ AI 脚本；**Meshy** / **Tripo3D** | ChatGPT 写 Blender Python 脚本自动建模；图片一键转 3D |
| 风格一致量产 / 风格迁移 | **Scenario.gg** | 训练你的风格，批量出一致素材 |
| 老素材高清化 / 立绘抠图 | **Real-ESRGAN** / **GFPGAN**；**BiRefNet** / **IOPaint** | 你那 73 款游戏的 CG 修复；从立绘中分离角色 |
| 2D 动画 / 角色动画 / 动捕 | **OpenToonz**、**Synfig**（免费）/ **Cascadeur**（AI 关键帧）/ **MediaPipe**、**FreeMoCap** | 不花钱做动画；减少手 K 工作量；摄像头捕捉动作 |

**经验法则**：AI 画素材 = "商业及格线"，验证玩法够用，但正式发行建议 AI 出初稿 + 自己修细节。

---

## Step 3：编程

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| AI 写代码主力 / 备选 | **Cursor**（Pro $20/月）+ Claude 系列；**GitHub Copilot** / **DeepSeek V4-Flash** API | AI 对 Unity C# 训练数据最多；DeepSeek 便宜 10 倍 |
| 纯对话出游戏（零代码） | **Godogen**（3.2K stars） | 一句话 → 完整 Godot/Bevy 项目，截图自修复 |
| AI 写完整项目 | **Claude Code**（终端） | 适合已有架构的项目 |
| 本地跑模型 / 多 Agent | **Ollama** + **llama.cpp**；**ccgs-cn-config** local preset | 本地 16GB 跑 qwen3:8b 已验证；CCGS 49 Agent 全 Ollama 零成本 |
| 物理引擎 / 内存 / 着色器 | **Box2D**、**Bullet**、**Havok**；**mimalloc** / **jemalloc**；**Slang** / **DXC** / **WebGPU** | 帧率掉 1-2 帧通常是内存分配器在加锁；替换系统分配器帧率稳定 |

**三七开原则**：70% 标准模块（存档、UI、设置、数据表）→ AI 写得又快又好；30% 手感/边界/性能 → AI 会自信地写错，必须手动验证；**每改完一个文件就跑一次，不要连续改 10 轮不开游戏**。

---

## Step 4：音效 & 音乐

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 背景音乐 / 音效 | **Suno** / **Udio**；**ElevenLabs SFX** | 一首主菜单 loop + 3 首场景曲 = 一个下午；"剑挥空的咻声"直接打字就有 |
| 配音/语音 | **CosyVoice** / **F5-TTS** / **Fish-Speech**（中文 Galgame）；**ElevenLabs TTS**（英文，质量最高） | — |
| 音频提取 / 制作 | **vgmstream**；**LMMS** / **Tidal**（免费 DAW） | 从游戏文件中提取音乐 |

**注意**：确认商用授权。Suno/Udio 免费方案通常不含商用。

---

## Step 5：AI NPC & 对话

| 做什么 | 用什么 | 成本 |
|--------|--------|------|
| 游戏 NPC 对话 / 角色一致性 | **Qwen-Character**（qwen-flash-character） | ¥0.25/百万 token，极低；session cache 让角色不跑偏 |
| 叙事/NPC 剧情 | **eliza** / **FastGPT** / **Langchain-Chatchat** | 多轮对话管理 |
| 对话树/分支剧情 | **Ren'Py**（内建）/ 手写 YAML | 视觉小说首选 |
| AI 驱动行为 / 行为树 | **Unity ML-Agents**（19.2K★）；**Tencent Behaviac**（5.8K★） | 强化学习训练 NPC；传统游戏 AI 架构 |
| 本地离线 NPC / 视觉 NPC | **Ollama** + **llama.cpp**；**Qwen3-VL** | 零延迟零成本适合单机；从截图理解场景再说话 |

**决策**：单机游戏 → 行为树/状态机够用，LLM 太杀鸡用牛刀；叙事/社交类 → Qwen-Character 性价比无敌

---

## Step 6：测试 & QA

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 自动跑图找 bug | **Airtest** / **AltTester** | AI 玩家 bot 自动测试 |
| 手动测试 | 每次改完就跑游戏 | **这是最重要的** |
| 性能/图形 profiling | Godot Profiler / **RenderDoc** | 帧率问题定位；GPU 级别的帧分析 |
| AI 审查代码 | 双 Agent 模式（起草→审核） | 一个写一个审，带固定框架 |

---

## Step 7：打包 & 发布

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 多平台导出 | **Godot Export** | 一键 Windows/macOS/Linux/Android/iOS/Web |
| 包体优化 | **pngquant**（图片）/ **WebP/AV1**（视频） | 包体大小直接看压缩算法 |
| 上架 Steam / 免费试水 | Steam Direct（$100/游戏）；**itch.io** | 收入 $1000 后退回上架费；免费上架 demo 先收反馈 |
| 微信小游戏 | **Cocos Creator** / **团结引擎** | 团结引擎支持 HarmonyOS |
| 本地化/翻译 / 字体 | **DeepL** + 人工校对；**fonttools** / **Textractor** | 12 种语言成本从 ¥100K 降到 ¥2K；确保中文字体塞得下 |
| 字幕/时间轴 | **Aegisub** | 汉化最后一步 |

---

## Step 8：运营 & 迭代

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 玩家行为分析 | **PostHog** / **Countly** | 免费额度够独立游戏用 |
| AI 客服 | Qwen / DeepSeek + RAG | 7×24 自动答玩家问题 |
| 素材同步（双机）/ 版本管理 | **Syncthing**；**Git** | 点对点不限容量，200GB 素材库同步首选；AI 生成的代码也必须进 Git |
| 热更新（移动端） | **xLua** / **PuerTS** / **ILRuntime** | 不重新发版更新游戏内容 |

---

## 快速查询：按游戏类型选工具链

- **视觉小说 / 文字冒险**：`Ren'Py` + `CosyVoice/F5-TTS`（配音）+ `Suno`（BGM）+ `Midjourney`（CG）
- **2D 像素 / 平台跳跃**：`Godot 4.7` + `Aseprite` + `Cursor+Claude` + `Suno`
- **3D 独立 / FPS / 生存**：`Godot 4.7` 或 `Unity` + `Blender+Meshy` + `Suno` + `Unity ML-Agents`
- **策略 / 卡牌 / Roguelike**：`Godot` 或 `Phaser`（Web）+ `DeepSeek V4-Pro`（数值/规则）+ `narrat`
- **对话式 / ARG / 网页游戏**：`Rosebud AI`（原型）→ `narrat` / `TyranoScript`（正式）+ `Qwen-Character` + `Gemini`
- **AI 原生游戏（AI 是玩法核心）**：`Claude Fable 5` + `Qwen-Character` + `Unity ML-Agents` + `llama.cpp`

## 成本参考（个人开发者月成本）

| 免费 ¥0 | 低配 ~¥150 | 标配 ~¥400 | 高配 ~¥800 |
|---|---|---|---|
| Godot + Blender + Ollama + Suno 免费版 + itch.io | + Cursor Pro（$20）+ Suno 付费 + Qwen API | + Midjourney（$30）+ DeepSeek V4 API + ElevenLabs | + Scenario.gg + Meshy + 多模型 API 并行 |

---

## 决策原则（从经验帖提取）

1. **先砍规格**：第一款游戏要"小到让你不好意思"
2. **三七开**：AI 写标准模块你 review，写手感/状态机你亲手验
3. **每改完跑一次**：连续让 AI 改 10 轮不开游戏 = 积累技术债
4. **锁文件锁范围**：prompt 里写"只改 X 文件，不动其他"
5. **成熟品类 + 1 个微创新**：别一上来就卷 3A
6. **不开公司**：Steam 个人就能上，保持轻盈
7. **AI 是及格线不是天花板**：验证玩法够用，正式发行要打磨
8. **版本控制**：AI 生成的代码也必须 Git，记录每次 prompt 和输出
9. **验证就是工作**（第七辑）：不能演示"改动有效"就没完工——UI 附截图、修复附复现+通过步骤、性能附前后数字；改计划比改代码便宜 10 倍
10. **先复现后修复 + 两击规则**（第七辑）：修 bug 先跑出来；同一形状失败两次 = 方向错了不是参数错了，别试第三个变体
11. **TDD 红绿**（第七辑）：代码类任务先写红色测试（定义行为）再让 AI 写绿色实现；动画/几何类把观感变成可断言的几何（距离/包围盒/颜色剖面）
12. **逆向构造保证可解**（第七辑）：关卡别随机生成（AI 撒点会出死局且肉眼看不出）——按消除顺序倒序摆放、每步校验畅通，可解性由构造方式保证
13. **数据没错 ≠ 看起来对**（第七辑）：数据层面校验全对，截图里仍可能"歪"——观感问题要追问到几何约束
14. **上下文预算 ≤200 行**（第七辑）：大上下文 = 低信号；每个项目维护一份 Master Guideline，agent 只读它；规则要剥掉会话只留原则（防过拟合）
15. **发布/权限/资金 = 人工闸门**（第七辑）：agent 约束绕过/未授权写入/编造数据都是真实发生过的事件模式，生产动作永远留人工确认点
16. **三可判据**（第八辑）：环节能否委托 AI = 需求可描述 + 结果可验收（机器可校验）+ 失败可重复；缺一即人主导（hqwc 09-20）
17. **AI NPC 三件套**（第八辑）：技能向量（每角色抽 10+ 参数分布，难度=构成比例+个体噪声）+ 接触记忆（最后位置+记忆时长）+ 效用打分仲裁（替 if 链，现任行为加滞回分）；效果用同局对照组量化，性能预算精确到 0.1ms（钢铁洪流）
18. **美术方向附图不写话**（第八辑）：手绘草图拍照/引用具体作品的特定画面 > 长文字描述；资产生成是 50 轮量级的迭代游戏，不是一次性生成
19. **提示词是一等资产**（第八辑）：风格锚点（美术/文案/命名三组）项目开始写死并复用；好提示词存 Markdown 进 git；资产命名 `模块_对象_状态`
20. **模型发布 = 安全事件**（第八辑）：Opus 5 把漏洞研发周期从月压到天、Gemini 评测越界打进 3 家真实公司——外部模型/评测环境的隔离边界当安全边界管理，新模型发布进补丁日历
21. **协议先行**（第九辑）：接任何大模型 API 前，先定义消息格式（status 分支 + 固定字段 + 错误结构），再让模型"按协议讲话"，消费端只做 switch(status)；配三道防御解析（正则提 JSON 段 → parse → 换行替换重试）。SSE 流记得 `TextDecoder({stream:true})` 防半字、思考型模型只取 `content` 不取 `reasoning_content`、动手前先 OPTIONS 探 CORS
22. **Modding 用 AI 三规范**（第九辑）：AI 辅助的开源 Mod/移植项目必须——披露（AI 用了多少、用在哪）、parity 测试（AI 批量转换的代码逐函数验证行为等价）、署名（AI 工具 co-author 标注不移除）；"看起来不像 slop"不能替代"被验证过"，"没用 AI"也不能掩盖"没披露"（Harbour Masters 09-16 争议）
23. **「一键生成」三问**（第三十辑）：看到任何「单图/一键生成 Live2D」的论文、产品或教程，先过三问 —— ① 主指标测的是**美术手作网格**还是**部署用的 auto-mesh**？② 与 baseline 的比较是否**在同一协议下**？③ **眨眼（`ParamEyeLOpen/R`）** 这类关键参数在自动分解层上成没成？**三问有一不过，就当营销读**。（来源：Bunraku arXiv 2607.27348 + `pith.science` 公开审稿报告——后者用论文自己的数据指出 0.768 测的是手作网格、部署网格从未被测、眨眼参数直接失效）

---

## 各辑增补（已归档）

每辑调研增补全文见 **[`game-production-pipeline-archive.md`](game-production-pipeline-archive.md)**（第六辑 ~ 第二十二辑逐字保留）；
经验帖汇总见 `csdn-social-summary.md` 与存档 `csdn-social-summary-vN.md`。
**为什么拆开**：主件是「查工具链时读的」，归档是「追溯某条结论从哪来时读的」——放一个文件里前者要为后者付 token。
归档里每辑「决策原则更新」小节的结论**已合并进上面的《决策原则》**，归档只留推导过程与原始链接。
