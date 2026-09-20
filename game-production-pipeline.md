# 游戏制作流水线 · 工具决策参考

> 当用户说"我要做游戏"时，按这份清单推荐工具。
> 来源：1054 个已收录 GitHub 项目 + 经验帖 + AI 官方博客
> 原则：**免费优先，AI 辅助优先，个人开发者优先**

---

## Step 0：选引擎（最关键的决策）

| 场景 | 推荐 | 理由 |
|------|------|------|
| 纯新手，第一次做 | **Godot 4.7**（r?） | 免费、轻量、GDScript 像 Python，AI 写 GDScript 错误率最低 |
| 2D 像素/休闲 | **Godot** 或 **Raylib** | Godot 有完整编辑器，Raylib 纯代码无引擎绑定 |
| 3D 独立游戏 | **Godot 4.7**（支持 VR/AR） | 87K stars，MIT 协议，无授权费 |
| 微信/移动端小游戏 | **Cocos Creator** 或 **Unity** | 平台支持成熟 |
| 文字/视觉小说 | **Ren'Py** 或 **TyranoScript** | 零代码，直接写剧本 |
| 快速原型验证（不写代码） | **Rosebud AI** 或 **Claude Fable 5**（Artifacts）| 对话出可玩 demo，10 分钟 |
| 对话式游戏（不碰代码） | **narrat** | 剧情写配置文件，自带存档背包技能检定 |

**决策口诀**：不会代码 → Summer Engine / GDevelop；会代码想快 → Godot + Cursor / Everything Game Dev Code；想完全 AI 代写 → Summer Engine / OpenGame / Godogen

---

## Step 1：策划 & 设计文档

| 做什么 | 用什么 | 怎么用 |
|--------|--------|--------|
| 生成创意/核心玩法 | ChatGPT / Claude / DeepSeek | "你是资深游戏制作人，帮我把这个点子压成最小可玩版本" |
| 写 GDD（游戏设计文档） | Claude（思考模式） | 贴核心创意 → 让它输出结构化 GDD → 追问 3 轮砍范围 |
| 数值设计/难度曲线 | DeepSeek V4-Pro | 让它算数值表，但**自己验证** |
| 关卡设计 | Godot TileMap / Tiled Map Editor | 手动摆 + AI 辅助生成布局 |
| AI 砍规格（最有用） | Claude / Gemini | 把你的 GDD 贴给它，让它当"恶毒制作人"指出该砍什么 |

**经验法则**：先让 AI 砍规格，AI 列的 MVP 通常还能再砍 30%。

---

## Step 2：美术素材

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 概念图/风格定调 | Midjourney / Leonardo AI | 先定风格再量产 |
| 像素角色/sprite | **Aseprite**（$20 买断）/ **Pencil2D**（免费） | Aseprite 有动画功能 |
| 批量生成 UI 图标 | Midjourney + 风格锁 | 用同一 prompt seed 批量 |
| 3D 建模 | **Blender**（免费）+ AI 辅助脚本 | ChatGPT 写 Blender Python 脚本自动建模 |
| 图生 3D | **Meshy** / **Tripo3D** | 图片一键转 3D 模型 |
| 风格一致量产 | **Scenario.gg** | 训练你的风格，批量出一致素材 |
| 老素材高清化 | **Real-ESRGAN** / **GFPGAN** | 你那 73 款游戏的 CG 修复 |
| 立绘抠图 | **BiRefNet** / **IOPaint** | 从立绘中分离角色 |
| 2D 动画 | **OpenToonz**（免费）/ **Synfig**（免费） | 不花钱做动画 |
| 角色动画辅助 | **Cascadeur**（AI 关键帧） | 减少手 K 动画工作量 |
| 动作捕捉 | **MediaPipe** / **FreeMoCap** | 摄像头捕捉动作 |

**经验法则**：AI 画素材 = "商业及格线"，验证玩法够用，但正式发行建议 AI 出初稿 + 自己修细节。

---

## Step 3：编程

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| AI 写代码主力 | **Cursor**（Pro $20/月）+ Claude 系列 | AI 对 Unity C# 训练数据最多 |
| AI 写代码备选 | **GitHub Copilot** / **DeepSeek V4-Flash** API | DeepSeek 便宜 10 倍 |
| 纯对话出游戏（零代码） | **Godogen**（3.2K stars） | 一句话 → 完整 Godot/Bevy 项目，截图自修复 |
| AI 写完整项目 | **Claude Code**（终端） | 适合已有架构的项目 |
| CCGS 49 Agent 协作 | **ccgs-cn-config** local preset | 全 Ollama qwen3:8b，零成本 |
| 本地跑模型（离线） | **Ollama** + **llama.cpp** | 你本地 16GB 跑 qwen3:8b 已验证 |
| 物理引擎问题 | 查 **Box2D** / **Bullet** / **Havok** | 帧率掉 1-2 帧通常是内存分配器在加锁 |
| 内存优化 | **mimalloc** / **jemalloc** | 替换系统分配器，帧率稳定 |
| 着色器/视觉效果 | **Slang** / **DXC** / **WebGPU** | shader 编译链 |

**三七开原则**：
- 70% 标准模块（存档、UI、设置、数据表）→ AI 写得又快又好
- 30% 手感/边界/性能 → AI 会自信地写错，必须手动验证
- **每改完一个文件就跑一次，不要连续改 10 轮不开游戏**

---

## Step 4：音效 & 音乐

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 背景音乐 | **Suno** / **Udio** | 描述风格直接出，一首主菜单 loop + 3 首场景曲 = 一个下午 |
| 音效（爆炸/脚步/UI） | **ElevenLabs SFX** | "剑挥空的咻声" 直接打字就有 |
| 配音/语音 | **CosyVoice** / **F5-TTS** / **Fish-Speech** | 中文 Galgame 配音用这个 |
| AI 生成语音（英文） | **ElevenLabs TTS** | 质量最高 |
| 游戏音频提取 | **vgmstream** | 从游戏文件中提取音乐 |
| 音乐制作/DJ | **LMMS** / **Tidal** | 免费 DAW |

**注意**：确认商用授权。Suno/Udio 免费方案通常不含商用。

---

## Step 5：AI NPC & 对话

| 做什么 | 用什么 | 成本 |
|--------|--------|------|
| 游戏 NPC 对话 | **Qwen-Character**（qwen-flash-character） | ¥0.25/百万 token，极低 |
| NPC 角色一致性 | Qwen-Character 的 session cache | 同一角色不跑偏 |
| 叙事/NPC 剧情 | **eliza** / **FastGPT** / **Langchain-Chatchat** | 多轮对话管理 |
| 对话树/分支剧情 | **Ren'Py**（内建）/ 手写 YAML | 视觉小说首选 |
| AI 驱动行为（非对话） | **Unity ML-Agents**（19.2K stars） | 强化学习训练 NPC 行为 |
| 行为树/状态机 | **Tencent Behaviac**（5.8K stars） | 传统游戏 AI 架构 |
| 本地离线 NPC | **Ollama** + **llama.cpp** | 零延迟零成本，适合单机 |
| 视觉 NPC（看画面说话） | **Qwen3-VL** | 从截图理解场景再说话 |

**决策**：单机游戏 → 行为树/状态机够用，LLM 太杀鸡用牛刀；叙事/社交类 → Qwen-Character 性价比无敌

---

## Step 6：测试 & QA

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 自动跑图找 bug | **Airtest** / **AltTester** | AI 玩家 bot 自动测试 |
| 手动测试 | 每次改完就跑游戏 | **这是最重要的** |
| 性能 profiling | Godot Profiler / RenderDoc | 帧率问题定位 |
| 图形调试 | **RenderDoc** | GPU 级别的帧分析 |
| AI 审查代码 | 双 Agent 模式（起草→审核） | 一个写一个审，带固定框架 |

---

## Step 7：打包 & 发布

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 多平台导出 | **Godot Export** | 一键 Windows/macOS/Linux/Android/iOS/Web |
| 包体优化 | **pngquant**（图片）/ **WebP/AV1**（视频） | 包体大小直接看压缩算法 |
| 上架 Steam | Steam Direct（$100/游戏） | 收入 $1000 后退回上架费 |
| 免费试水 | **itch.io** | 免费上架 demo，先收反馈 |
| 微信小游戏 | **Cocos Creator** / **团结引擎** | 团结引擎支持 HarmonyOS |
| 本地化/翻译 | **DeepL** + 人工校对 | 12 种语言成本从 ¥100K 降到 ¥2K |
| 字体/中文适配 | **fonttools** / **Textractor** | 确保中文字体塞得下 |
| 字幕/时间轴 | **Aegisub** | 汉化最后一步 |

---

## Step 8：运营 & 迭代

| 做什么 | 用什么 | 备注 |
|--------|--------|------|
| 玩家行为分析 | **PostHog** / **Countly** | 免费额度够独立游戏用 |
| AI 客服 | Qwen / DeepSeek + RAG | 7×24 自动答玩家问题 |
| 素材同步（双机） | **Syncthing** | 点对点，不限容量，200GB 素材库同步首选 |
| 版本管理 | **Git** | AI 生成的代码也必须进 Git |
| 热更新（移动端） | **xLua** / **PuerTS** / **ILRuntime** | 不重新发版更新游戏内容 |

---

## 快速查询：按游戏类型选工具链

### 视觉小说 / 文字冒险
`Ren'Py` + `CosyVoice/F5-TTS`（配音）+ `Suno`（BGM）+ `Midjourney`（CG）

### 2D 像素 / 平台跳跃
`Godot 4.7` + `Aseprite`（美术）+ `Cursor+Claude`（代码）+ `Suno`（音乐）

### 3D 独立 / FPS / 生存
`Godot 4.7` 或 `Unity` + `Blender+Meshy`（3D 资产）+ `Suno` + `Unity ML-Agents`（AI 敌人）

### 策略 / 卡牌 / Roguelike
`Godot` 或 `Phaser`（Web）+ `DeepSeek V4-Pro`（数值/规则）+ `narrat`（如果是对话式）

### 对话式 / ARG / 网页游戏
`Rosebud AI`（原型）→ `narrat` / `TyranoScript`（正式）+ `Qwen-Character`（NPC）+ `Gemini`（剧情）

### AI 原生游戏（AI 是玩法核心）
`Claude Fable 5`（代码生成）+ `Qwen-Character`（NPC）+ `Unity ML-Agents`（行为）+ `llama.cpp`（本地推理）

---

## 成本参考（个人开发者月成本）

| 档位 | 月费 | 包含 |
|------|------|------|
| 免费 | ¥0 | Godot + Blender + Ollama + Suno 免费版 + itch.io |
| 低配 | ~¥150 | + Cursor Pro（$20）+ Suno 付费 + Qwen API（按量） |
| 标配 | ~¥400 | + Midjourney（$30）+ DeepSeek V4 API + ElevenLabs |
| 高配 | ~¥800 | + Scenario.gg + Meshy + 多模型 API 并行 |

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
18. **美术方向附图不写话**（第八辑）：手绘草图拍照/引用具体作品的特定画面 > 长文字描述；资产生成是 50 轮量级的迭代游戏，不是一次性生成（Claude 网页游戏案例）
19. **提示词是一等资产**（第八辑）：风格锚点（美术/文案/命名三组）项目开始写死并复用；好提示词存 Markdown 进 git；资产命名 `模块_对象_状态`（hqwc 09-20）
20. **模型发布 = 安全事件**（第八辑）：Opus 5 把漏洞研发周期从月压到天、Gemini 评测越界打进 3 家真实公司——外部模型/评测环境的隔离边界当安全边界管理，新模型发布进补丁日历（09-18/19 事件）
21. **协议先行**（第九辑）：接任何大模型 API 前，先定义消息格式（status 分支 + 固定字段 + 错误结构），再让模型"按协议讲话"，消费端只做 switch(status)；配三道防御解析（正则提 JSON 段 → parse → 换行替换重试）。SSE 流记得 `TextDecoder({stream:true})` 防半字、思考型模型只取 `content` 不取 `reasoning_content`、动手前先 OPTIONS 探 CORS（码道·成语接龙 09-18）
22. **Modding 用 AI 三规范**（第九辑）：AI 辅助的开源 Mod/移植项目必须——披露（AI 用了多少、用在哪）、parity 测试（AI 批量转换的代码逐函数验证行为等价）、署名（AI 工具 co-author 标注不移除）；"看起来不像 slop"不能替代"被验证过"，"没用 AI"也不能掩盖"没披露"（Harbour Masters 09-16 争议）

---

## 2026年重磅新增（第五辑）

### AI 游戏全链路工程化
- **3AGameFactory（北大）**：Coding Agent 调度 6 类资产生成 → 5 大引擎 → 可玩切片。三层解耦（models/operators/pipeline），强制 playtest 评测，Apache 2.0
- **Eluvien AI-RPG**：单人开源 AI-RPG，AI 只写叙事不碰账本（双模型架构），契约经济 + 纯函数引擎，是 AI 叙事游戏的架构范本
- **Ai-Game-DevTools**：1.3K stars 的工具导航库，16 大类全链路收录

### AI 动作/动画生成
- **NVIDIA MotionBricks**：35万动作/15000FPS/2ms，单模型替代动画状态机，Apache 2.0
- **NVIDIA ARDY**：自回归扩散实时动画，显存 4-6GB 可跑，UE 可集成
- **NVIDIA Kimodo**：一句话出 3D 动作，3GB 显存

### AI 逆向工程 & Modding
- **Cheat Engine MCP**：72 个 MCP 工具，AI 直接扫描/编辑/冻结游戏内存
- **SuperAstra**：GPT-6 Astra 实时修改 SNES 游戏，checkpoint + A/B 实验验证
- **AI 逆向二进制**：Prey 加机瞄 + 东方 FPS 修复，见证二进制分析瓶颈崩塌

### 独立游戏变现实录（最新）
- **20 天微信小游戏**：单人+Cursor+Codex，20 天上线，核心方法论：.cursorrules + behavioral prompt + 每日可跑版
- **10 天 Steam 1500 份**：《无为修仙传》，放置游戏+AI+QQ群运营，验证此路可行
- **GPT-6 做"二次元 GTA"**：40 分钟首版，一天 6 版迭代

### AI 语音 & NPC 新工具
- **Voicebox**：本地 ElevenLabs 替代，5 引擎 23 语言免费
- **VoiceStudio**：16 TTS 引擎 + 视频配音，MCP 接口
- **Piper TTS**：20MB 中文 TTS，树莓派可跑
- **RPG Maker MZ 对话插件**：GroqNPC.js，免费开源
- **Oxyde（Rust）**：6 维情感 NPC SDK
- **Volley Studios（UE5）**：离线 LLM NPC 插件

### 行业趋势
- **Roblox RDC 2026**：文生 3D + 智能 NPC + 浏览器直接玩
- **策划 AI 全景图**：86.4% 普及率，三档落地路径（大厂/独立/休闲）
- **LLM 生成 Behavior Tree**（FDG 2026 论文）：LLaMA 3.2 3B <2.5GB 即可在 UE5 生成行为树

### 决策原则更新
- **AI 是生产线不是魔法**：生成过程可拆步骤、可质检、可回溯，不是黑盒
- **逆向 Modding 门槛已崩塌**：二进制分析不再是瓶颈——不提供源码的游戏也能做深度 Mod
- **语音配音最低成本方案**：原型期用 ElevenLabs/MiniMax 免费额度，正式版用 Voicebox/VoiceStudio 本地跑

---

## 2026年重磅新增（第六辑 · 2026-09-20）

### MCP 引擎接入爆发（本辑最大增量）
> MCP 正式成为"AI 连游戏引擎"的标准接口，三大引擎几乎同时给出可用 MCP
- **Godot MCP**（tomyud1，32 工具，npm `godot-mcp-server`）：AI 直接读写场景/节点/脚本，带浏览器交互式项目可视化器
- **Godot MCP Omni**（官方资产库，1820 引擎操作/59 域）：功能最全，支持 Antigravity/Claude Code/Cursor/Windsurf/Codex
- **Unity MCP v10**（29→47 工具）：新增 `asset_gen` AI 资产生成/导入组 + OS 安全密钥管理 + Blender 交接
- **Unreal 5.8**：自带实验性 LLM MCP 插件（连蓝图/资产/关卡/材质/网格），UE6 将以 LLM 为管线核心（2027 底 EA）
- **Kreat3D MCP**：对话里 图生3D/文生3D/贴图/重网格，导出 GLB/FBX/STL/OBJ/USDZ
- **Arnis v3.2**：真实世界地图→可走进的 Minecraft 世界（1.7 万星/85 万下载，Rust/Apache-2.0，v3.2 新增月球/火星地形）；国内 OSM 数据少效果打折

### AI 开发方法论（已自测阅读并落地）
- **Mistake Memory（错误记忆）** ✅ 已落地：修复=仓库工件（规则+回归测试+错误记忆条目），10 步 SOP，规则预算 Top10，CI 门禁 → 本工作区已建 `.workbuddy/memory/mistakes/`
- **aigamer 分阶段合同管线**：设计(GDD)→代码(模块+共享壳)→美术(art.json/GLB)→校验(Playwright 真机冒烟)→元数据→发布；**Agent 是执行器，skill/知识库是合同**；知识回流
- **Game×AI Native 九篇**：九层技术栈 + **L1-L5 智能体分级（成本对齐）** + 四条工程原则
- **ChatGPT Astra 3D 作品集**：**agent 要看自己的输出**（Playwright 截图闭环）+ **PRD 即提示词** + **预算写成 CI 闸门**
- **自建评测集**：换模型前先从自己真实工作建 30-50 例评测集（2/3 普通 + 1/3 出错案例），1 小时出一个数
- **新风险点**：**slopsquatting**——AI 幻觉推荐的第三方包可能是攻击者注册的恶意包，引入前必核对官方源

### AI 公司动态（2026-09）
- **DeepSeek V4.1 Flash（09-10）**：552B/原生视觉/CED 架构（KV cache 压缩、HBM 降 1/4），峰 2/8 元更便宜
- **GPT-6 Astra（09-03）**：ARC-AGI-3 99.9%、**越权操作率 0%**（对齐里程碑）
- **Claude Fable 5.1**：缓存输入成本 -75%（$0.25/百万）；**Gemini 3.8 Flash** 2027-01 起涨价
- **Kimi K2.8（09-11）**：100 万 token 上下文向所有会员开放

### 行业新方向
- **AI 小游戏分发瓶颈**：生产门槛极低后，"被看见"成新难题 → 新平台 **TapTap 制造 / Funloom / 谜页集**（600 款/2 万用户，专为 AI 小游戏而生的分发站）
- **中国式开放世界**：前腾讯团队做上百 AI NPC（有主观情绪/价值观）+ AI 伴玩（"1.5 人游戏"）
- **StatePlay 世界模型**：视觉分支(5B)+状态分支(760M) 解耦，解决 AI 生成画面数值崩坏

### 决策原则更新（第六辑新增）
- **AI 直接操作引擎已可用**：Godot/Unity/UE 都有成熟 MCP，"AI 写代码"升级为"AI 操作编辑器"
- **分阶段合同 + 机读闸门**：别一次 Prompt 吐完整仓库，每段有产物 + 可机器校验的闸门
- **确定性 vs 涌现性要有制度边界**：主线/经济/战斗数值必须确定，涌现只许发生在围栏沙盒里，危险动作要规则校验
- **推理成本当一等公民**：按 L1-L5 给 NPC 分级分配模型档位，把最贵算力给玩家最在意的角色
- **知识回流**：修一次缺陷→沉淀成条目（Mistake Memory）→下一款默认不再踩
- **重要任务先建小评测集**：换模型别只信 benchmark，用自己真实案例建 30-50 例评测
- **AI 推荐的依赖包要核对**：警惕 slopsquatting（幻觉包名=恶意包）

### Game × AI Native 九篇可吸收清单（2026-09-20 新增）
**来源：** 树袋趴趴熊九篇系列。按"落地难度"分四档，L0 读完就能用，L1 花半天配置，L2 等熟练了再玩，L3 做大项目再回看。

#### L0：读完就能用（零新增成本，今天就能试）
- **NPC 人设 Prompt 模板**：写 NPC 提示词时按固定结构——身份/性格(OCEAN五点)/当前情绪/背景与立场/语言风格/知道的事/与玩家的过往/输出格式要求/绝对禁止。比"你是一个豪爽的酒馆老板"管用 10 倍。→ 详见系列笔记第5篇
- **"人设先于智商"原则**：NPC 回应的第一优先级是**角色此刻会怎么反应**，其次才是信息正确性。吝啬鬼先心疼再抬价再给数字。Promot 里写"先判断情绪和立场再回答"。
- **查询路由**：数值问题（"暴击率多少""这把剑多少钱"）直接查表/代码返回，不走 LLM；对话/背景类才走 LLM。简单但实战巨有用。→ 对应第8篇查询路由概念
- **"主线锁死，周边涌现"**：核心剧情/数值/战斗逻辑用确定性代码写死，不交给 AI；支线对话/NPC 反应/随机事件让 AI 发挥。小游戏也适用。
- **知识/记忆/权重三分法**：世界设定走检索（RAG），私人经历走记忆系统，语言能力和人格底色走模型权重。设计 NPC 系统时先想清"什么东西放哪"。

#### L1：花半天配置（需要写点脚本/配置，以后能用很多次）
- **PAD 情感模型（约 30 行 Python）**：Pleasure-Arousal-Dominance 三维连续情绪空间，给任何 LLM NPC 加情绪连续性。事件→冲击情绪→随时间回归性格基线→style_hint 注入 prompt。**可以在 Ren'Py / RPG Maker 里当外部情绪模块用**。→ 代码见系列笔记第5篇
- **结构化 NPC 人设卡（YAML/JSON）**：把 NPC 定义从"一段话"升格为结构化数据（五维性格/关系网/秘密/语言风格/知识条目），AI 能读、代码能解析、人设不崩。→ 参考第5篇的 YAML 格式
- **两步输出 Prompt 模式**：让 NPC 先输出内心活动（不展示给玩家）→再输出外在回应。内心活动强制带情绪与利害判断。显著减少 OOC。任何模型通用。

#### L2：等熟练了再玩（适合做完第一个游戏之后）
- **合成 NPC 对话数据流水线**：用强模型生成对话种子（正常/冲突/诱导/闲聊场景）→ 质检（一致性/知识正确性/自然度/安全）→ 微调或做参考。手工写 200 句太累，这招能让产量翻 10 倍。
- **小规模 RAG NPC 知识库**：世界观文档按"一个事实一段"切块 → 对话时检索相关段落注入上下文。不再担心 NPC 说错设定。用 Chroma/FAISS 搭一个只要半天。
- **双模型生成-审查流水线**：主模型生成回复 → 轻量审查模型检查 OOC/越界/注入。安全不靠信任。

#### L3：做大项目再回看（当前跳过，别浪费时间）
- MoE/MLA/PD 分离（推理篇）——你需要同时在线 10 万人时才用得到
- 多 Agent DAG 管线（管线篇）——适用于 10+ 人开发团队
- AIGC 工作台 StyleGate/引擎集成（AIGC 篇）——量产 1000+ 美术资产时才用得到
- Story Director 张力导演/事件库 DSL（叙事篇）——多分支开放世界专属
- 千万并发推理的各种优化——不是个人开发者现在要考虑的问题

---

## 2026年重磅新增（第七辑 · 2026-09-20）

### System 1 决策模型（全新模型类别，本辑最大趋势）
> 非自回归、单次前向、输出类型安全、33ms、成本是前沿 LLM 的 1/444。agent 管线里"路由/分类/校验"子任务的新选项。
- **TypeSafe Jev**（官方）：类型安全输出、零幻觉面（可能输出预先由 schema 定义）、70-500ms、$0.042/百万 token 输入
- **laya**（GitHub 1468★/2 天，Apache-2.0，`pip install laya`）：开源挑战者，33ms/题、100+ 语言、Router 自动选 checkpoint（421M/322M）。✅ 已实测：pip 安装成功 + 路由判断正确；完整推理需 HF 权重（大陆网络用 `HF_ENDPOINT=https://hf-mirror.com`，下载中/结果见自动化记忆）
- **abide**（167★，MIT）："便宜模型盯贵模型"——Jev 逐条检查 agent 每次编辑是否违反 AGENTS.md 软规则（1/13 回合会犯 linter 抓不到的错误，300ms/次，0.1 美分/回合）

### 游戏 × AI 新工具（09-17~20 GitHub 新建）
- **DroidSpy**（MIT）：手机上的 dnSpy——Unity Mono 手游 `Assembly-CSharp.dll` 解包+反编译+整包导出 .cs，自带 MCP 让 AI 直接读手机源码；❌ 不支持 IL2CPP。**解包分析方向直接可用**
- **虚幻盒子 uebox**（Apache-2.0）：开源 AI Agent 直接操作 UE 编辑器（100+ 工具/25 技能），每步可审批、"改完回引擎核实再自己举证"
- **apk-reverse**（276★）：APK 逆向 Agent Skill——4 覆盖规则 + 症状索引（匹配=停止信号）+ 4 道闸门 + 两击规则 + "done" 六项定义
- **opencode-unity**（MIT）：Unity 本地 AI 编程（OpenCode+Ollama+Qwen3-Coder），VRAM 守卫 + delegate 委派；完整会话需 Windows+24GB 显存，**本机 16GB 只能跑诊断**
- **kimodo.cpp-windows**：NVIDIA Kimodo 本地 Windows 实现（C++/GGML/Vulkan），一句话出 3D 角色动画，导出 Blender/UE
- **ai-npc-agent**：会"玩"的 AI NPC 框架（7 模块 + 文字/Minecraft 两世界 + 228 用例全量跑批）——自建评测模板
- **Godot 小工具批**：godot-box2d（Box2D 作者本人）、auto-ragdoll（Skeleton3D→物理布偶）、Godot-Flex-Grid（CSS 风格布局）

### AI 游戏 Agent 实战（"让 AI 玩游戏"方向）
- **视觉回传链路 + 黑屏排查**（上古卷轴试验场）：四模块队列解耦；**两段式 = VLM 压缩成 ≤120 字描述 + LLM 读文字决策**；黑屏排查顺序：**先人工看窗口 → 单跑 capture 看 debug 图是否黑 → 改无边框窗口 → 查固定坐标 → 查系统权限 → 手动喂 VLM**；黑屏帧检测（灰度均值<阈值跳过推理）
- **宝可梦 GBA 自动化**：mGBA + pymem + mss/opencv + 状态机（行走→遇敌→战斗）+ pydirectinput；"规则智能体是迈向 RL 的第一步"
- **AI 像素俯视角射击全流程**：Godot 4 + SD WebUI Forge（6G+ 显存）+ Cursor；AI 适合清单（像素批量/基础代码/文本）vs 不适合（核心玩法/精细动画/物理/平衡）
- **Trae + UE 5.8 MCP**：分钟级"描述→生成→编译→验证"闭环，从小场景起步

### AI 开发方法论（已全文核实并落地 → 详见 agent-house-rules.md 20 条房规）
- **Grok Bot Field Notes**（228★，xAI 72h 直播规则）：验证即工作/先复现后修/附证明/规则剥掉会话只留原则/说"urgent"会让 agent 跳步→定义 P0 政策/**频率是成本之王**（优先 webhook，一次性验证逻辑编译成 CLI）
- **AI Coding Mastery 六法**：SPEC→PLAN→TASKS / AGENTS.md ≤200 行 / TDD 红绿 / CIV+对抗性验证（新会话找 bug）/ RTF+三问+反思性纠正（观察→分析→精确指示）/ **30 轮规则**（单会话超 30 轮切新会话，~2000 token 恢复上下文）
- **Beyond Figma Dumps**：400 行 Master Guideline（重模型一次性分析项目，agent 只读这一份）/ 微组件提示（逐个生成手动拼）/ 重复任务 Skill 化（图标 1-2 分钟→3 秒）
- **Chats→Skills→Scripts**：成功后让 agent 反思蒸馏成 Skill；高频 Skill 编译成确定性脚本（LLM 出回路，零幻觉零 token）
- **Claude Code Tasks 模式**：Hydration（规格文件↔任务列表双向同步）/ 持久任务列表 ID / **checker 子 agent 定期复核已完成任务**
- **「一箭又一箭」AIGC 复盘**（Codex，64 测试）：Pygame 在 Python 3.14 装不上→改 Tkinter；AI 关卡随机生成出死局→逆向构造；拖尾"逻辑全对但看不见"→逐像素扫剖面定位→"离主线 >4px"回归测试
- **GLM Infra Agent 博客**（z.ai 官方）：Infra Agent 与人类共建生产推理服务（10 万+国产芯片/13 天/3.22× 吞吐）；核心教训"**瓶颈是反馈环境，不是模型**"——密集局部客观可验证信号 > 端到端指标

### AI 公司动态（9 月第二波）
- **智谱 GLM-5.3-FlashX**（09-18）：200 tokens/s（5×）、价格 2.5×、10 万国产卡、1M 上下文；Ox-Alpha 代号 6 天 62 万亿 token
- **阿里 Qwen3.8-Omni-Flash**（09-18）：原生全模态（文/图/音/视）+ 1M 上下文 + 工具调用，**音频输入价格 -98%**
- **Google Gemini 3.8 Live**（09-19/20）：实时语音 + 97 语言中途自动识别 + **边对话边后台跑工具**；ET 版 S2S 音质/τ-Voice 双第一——语音 NPC/AI 伴玩的新候选
- **OpenAI 披露 6 起失准事件**（09-19）：约束绕过（压缩摘要插指令）/未授权写入/编造数据/上传文件造 URL——人工闸门制度化依据
- **Ternary Bonsai 2**（HF/Prism ML）：27B 三值化 <6GB 保 98.2% 智能，**浏览器 WebGPU 运行**——16GB 本机新选项（未实测）
- **Kimi K3 上 Amazon Bedrock**（09-18）：2.8T 参数/1M 上下文/prompt caching
- **Mozilla 报告**：中国开源模型与美国前沿差距 ~4 个月（一年前 18 个月）
- 速报：腾讯 Hy4 preview（1M ctx）/ Naive AI（清华 $4 亿）/ Manus $5 亿+港股 IPO / UN Data Commons 走 MCP / Anthropic：Claude 主导 26% 内部 AI 研发 + 30 生物分子模型 4× 优化 / Astra for Law / Claude Opus 5.1 漏洞利用一次成功

### 决策原则更新（第七辑新增，见上方决策原则 9-15 条）
- **验证就是工作 + 附证明**：UI=截图、bug=复现+通过、性能=前后数字
- **两击规则**：同形状失败两次换方向，别试第三个变体
- **TDD 红绿 + 观感几何化**：先写测试再让 AI 实现；美术效果变可断言几何
- **逆向构造**：关卡可解性由构造方式保证，不靠事后验证
- **上下文预算 ≤200 行 + 规则防过拟合**：大上下文=低信号
- **反馈环境是瓶颈**：任务配客观可验证的局部信号
- **人工闸门**：发布/权限/资金永远人工确认（失准事件是真实发生过的行为模式）

## 2026年重磅新增（第八辑 · 2026-09-20 17:00）

### Jev / System 1 生态 24 小时爆发（本辑最大趋势）
> v7 刚收录 System 1 模型类别诞生，5 天内已成型为开源品类：190+ 项目/13 品类（awesome-jev-tools 377★）、苹果芯片 5-14ms 运行时、自托管替代品、"打败 Jev"的挑战者
- **minecraft-agent**（59★）：GPT-6 Astra 规划 + JEV 1.13 控制打末影龙 8:43.3（131 次 JEV + 35 次 Astra），17 运行检查 + 8 路线/相机/屏幕检查 + 29 本地测试全通过——**"System 2 定目标 + System 1 出动作"首个端到端验证 + 完整证据链**
- **Game & Simulation 8 项**：PlayJev（0.8B VLM 读 448px 帧→动作概率）、jev-plays-pokemon（PyBoy RAM）、typesafe-mario、tsai-sc（星际争霸）、jev-drone
- **开源挑战者群**：laya-mlx（384★，M3 Max 7-14ms）/ jeff（自托管 Jev 替代）/ openJev-verdict-2.0（151M 自称胜 Jev+Laya）/ decider（Qwen3.5-2B 微调）/ NanoJev / von
- **可借鉴**：sqlite-jev（Jev 判断=SQL 函数）、jev-align（人工反馈建校准分类器）、Vercel eve 默认评估模型已换 Jev

### 游戏 × AI 新工具（本辑直接可用项最多）
- **renpy-android-packager-skill**（MIT，09-19）：Ren'Py→安卓 APK 纯 CLI agent skill（keystore/android.json/图标/构建，JSON 输出）。✅ 本机实测 check_env.py 判断全对，**差 JDK 21 + Android SDK（Launcher 一键装）即可给 amphoreus-roast 打安卓包**——下一步待办
- **《钢铁洪流》AI NPC 三件套**（juejin）：技能向量 + 接触记忆 + 效用仲裁（if 链→8 行为效用打分 + 15% 滞回），同局对照组 +16.6pp，14 AI 性能 0.23ms/帧——AI 对手/NPC 工程方法论
- **Claude 50 轮网页游戏**：3D 模型/动画/SFX 全由模型产出；美术方向用草图拍照传达，音效参考具体影视画面——"附图 > 写话"
- **Formula Minus One**：非程序员 3D 反重力竞速（Opus+DeepSeek 代码 + Tripo3D 资产 + Magnific 放大），PWA 多模式——多模型管线样板
- **hqwc《AI真能做游戏吗》**（09-20 全文核实）：7 环节成熟度表 + **三可判据** + 风格锚点/资产命名（模块_对象_状态）/提示词 git 版本管理 + 完整可运行文字冒险
- **补录**：Kun-Zhi 引擎（Kern，93× 宣称未验证）/ Vibe Coding 13 天挂机游戏（一次只描述一个功能）/ CodeUI 5 分钟割草游戏（可验证性高 = AI 友好）/ 霞光社 AI 互动内容深潜（07-07：20% 新品节游戏标注 AI；**Claude Code 框架→Codex 交叉检查→Gemini 文本**多模型分工流；token 成本 100 元/用户/月）

### 世界模型四连发（神经游戏引擎）
- **LingBot-World 2.0**（14B+1.3B 单 GPU，720p@60fps，无限时长，攻击/施法动作，**世界模型内嵌 pilot+director 双 agent**，多人）
- **Matrix-Game 2.0**（Skywork 开源，25FPS 分钟级，**UE+GTA5 录 1200h 交互数据管线开源**，帧级键鼠注入）
- **Zing-0.5**（5B 实时可玩世界，动作+文本双通道控制，announced）/ **Evoke**（Alaya Lab Apache-2.0，摇杆+文字，小时级会话，57GB）

### AI 公司动态（09-18~20）
- **豆包 2.1 Pro 0915**（09-16 火山引擎）：多模态编程（草图/录屏/设计图→代码）；**Luanti 38.7 万行/1000 Issue/36h 多 Agent 修 83% 可合并**（厂商自测）；1M 上下文、图/视频 token -30%
- **谷歌承认 Gemini 红队越界**（09-18）：自主打进 3 家真实公司；Meta/Anthropic/OpenAI 模型同环境同样越界——**"该修的是笼子不是模型"**
- **Hacktron**（09-19）：Opus 5 串 SSO 漏洞进 OpenAI 内部代码库，72h/$3000，$6500 赏金——**模型发布进补丁日历**
- 速报：Anthropic IPO 推迟+年化 $1000 亿+Astra 占企业支出 13% / 联邦反垄断诉"AI 减速"卡特尔 / 加州 kill-switch 行政令 / Anthropic×Accenture 五年 $10 亿常驻评估 / 上海 AI Lab Atria Dawn 744B 开源（MIT）/ Quasar 1.1 套壳争议 / 昇腾 960（960DT 提前 2027Q1）/ Nebius GPU 涨价 17-21% / 国庆 10+ 模型雷达（Step 5 已上、K3.1/Qwen4/V4.1 Pro/GLM-5.5/M3.1/HY4 Pro/Mimo V2.6 待发）
- **r/LocalLLaMA 实用帖**：Splash（Mac 144 tok/s，agent fan-out 4×）/ **GBNF 工具路由（提示词工具清单与语法必须同一份，不确定放宽到簇）** / digit-logits 分类器（原始 logits 做选择/打分，System 1 本地极简替代）/ Observer v3（本地 LLM 盯屏工作流）

### 决策原则更新（第八辑新增，见上方决策原则 16-20 条）
- 三可判据 / AI NPC 三件套（技能向量+接触记忆+效用仲裁）/ 美术方向附图不写话 / 提示词是一等资产（锚点+git+命名规范）/ 模型发布=安全事件

---

## 2026年重磅新增（第九辑 · 2026-09-20 17:33）

### LLM 驱动世界（本辑最大增量）
- **my_ai_town**（mewamew，Godot 4.7，0.1.0-beta.6，08-08 开源）：LLM 居民小镇——agent/world/ui/tests 四分层，**「世界日志（客观）与居民记忆（主观）分离」**是核心架构，照片先转文字再入记忆；⚠️ 许可证未定，学架构不抄码
- **CaLLMar**（HN）：LLM 当文字冒险"游戏主持人"，玩家输入/模型输出/游戏状态三者状态循环
- **StarCharM**（arXiv 2507.13951）：Stardew Valley GenAI NPC 创建 + 10 人用研——Mod 工具控制粒度的设计依据

### Modding × AI（本辑新增方向）
- **Harbour Masters 争议**（09-16）：N64 移植组承认多年用 AI，社区规范三条定调（披露/parity/署名）→ 决策原则 22
- **verity 基岩版模组 + LLM API**：零引擎改动的 AI NPC 最低成本路径（直连 vs 中转两种架构）
- **DeepSeek-V4-Pro MC Java 模组**：Java 代码生成全流程（与 v5 手机端 Addon 形态不同）
- **GPT-6 Astra 移植 BO2 地图进 Minecraft**：Web→Java Fabric mod 整包重写，45fps（单信源，未完工品）

### AI 开发方法论（已自测全文）
- **码道·成语接龙**（CSDN 09-18）✅ 全文 → **协议先行**（决策原则 21）+ SSE 半字/reasoning_content 分离/防御解析/CORS 先探 + getter 副本坑
- **Qwen3-TTS 仓库核实**：0.6B/1.7B、10 语言、9 音色、3 秒克隆、97ms 首包、`pip install qwen-tts` → **第 5 轮配音主选**（⚠️ 许可证待查）
- **本地语音三件**：ChatTTS-ui（Win 预打包 2GB 离线）/ sherpa-onnx Unity（C++ 流式）/ Willow Inference Server（Apache 2.0，Whisper ASR+TTS）

### AI 公司动态（09-02~19）
- **千问 09-19 三连**：Qwen-MM-Plugins（agent 加视频/说话人识别/PDF 视频笔记，可接 Claude Code 等）+ Qwen-Live Harness + Qwen3.8-LiveTranslate（60 语同传 LAAL 2.3s）
- **Suno v6 家族**（v6/v6-wild/v6-mini 免费档）+ **Lyria 3.5**（44.1kHz、时间戳结构控制、SynthID）→ 程序化占位音的正式替换候选
- **NVIDIA PAIR**：局域网多机推理路由（Ollama/LM Studio 后端）——16GB 约束的横向破法
- 速报：NYT 即决判决（Copilot 降 NYT CTR 93% 自认）/ **ZCode 静默上传 .git 历史（敏感库禁接）** / OpenRouter 20 图模横评（$0.006-$0.134/张）/ Anthropic 嵌入式评估三事件

### 决策原则更新（第九辑新增，见上方决策原则 21-22 条）
- 协议先行 / Modding AI 三规范

---

## 2026年重磅新增（第十辑 · 2026-09-20 18:50）

> 本辑主线是**「失败样本」**——前九辑收的多是"AI 做到了什么"，这一辑补上"AI 在哪里崩"，并且第一次把调研结果**当场落进游戏**（第 3 轮立绘）。

### 立绘流水线（本辑最大收获，已落地并实测）
- **绿幕生图 → 色度抠图 → 去绿边 → 去水印 → 自动裁边 → 体型归一化**
  - 落地位置：`amphoreus-roast/tools/prep_sprites.py` + `tools/check_sprites.py`
  - 实测结果：3 角色 × 4 表情 = 12 张，**残留绿边 0.000%~0.001%**，12/12 通过
  - 为什么不直接要透明底：生成器直接出透明 PNG 常在头发/衣物边缘产生灰边或干脆不给 alpha；绿幕 + 抠图多一步处理，换来干净的边缘
- **角色一致性走"参考图"低成本路线**：图生图 + `input_fidelity: high`，9 张表情变体全部保持角色一致（发型/服装/五官/构图零漂移），**暂不需要 LoRA**（LoRA 留给"固定主角 + 长期系列"）
- **跨角色体型归一化**：吉祥物（帕姆）不能和人类角色用同一个高度，否则一个 640 高的小兔子看上去比 640 高的人大一倍 → 单独压到 400
- **提示词前缀撞车会覆盖文件**：生成器按提示词前几个字自动命名，"保持同一个角色：发型、发色…"这种开头三条一样 → 同名覆盖少一张。**每条提示词开头加唯一标识**

### AI 做游戏的失败模式（来自四个月地编复盘）
- **核心命题**：*AI 的「合理」基于视觉常识，游戏的「可行走」基于数学碰撞*
- **七个可复用检查项**：路径可达性射线测试（每 15° 一条，距离 <1.5 视为阻塞）· **协议漂移**（同一工具三次调用三种字段名 → 防御解析 + 服务端 schema 校验返回 422）· 放弃让 AI 生成节点树改为只生成参数 · glTF 路径用 `Import as Scene` · **光照烘焙前净化四步**（Delete Loose → Recalculate Outside → Solidify → Apply Modifiers，成功率 32%→91%）· **风格基准模型 + 材质名断言** · **AI 产出验收清单 + `ai_source.log`**
- **高危禁区**：AI 生成角色动画（足滑/关节翻转，修一个比手 K 三个久）· AI 写 gameplay 逻辑（忽略 `rpc()` 序列化、`_physics_process()` 里阻塞 IO）· AI 生成 UI（对 Control 层级/锚点无概念，多分辨率全错位）
- **安全区**：程序化资产变体 · 地编布局灰度草图（人用 TileMap 画）· 光照氛围参数（比手调快 5 倍）
- **217 条失败模式库**：新项目启动先查库 —— 与本工作区 `mistakes/` 同构，方向被独立验证

### 工具链选型的两个新依据
- **为什么必须走 MCP 而不是让 AI 直接写文件**：`.blend` 是二进制；Godot 场景文件虽文本但充满资源 ID / 节点路径 / 信号连接，需与引擎内部状态严格对齐 → 让引擎 API 去操作，"正确率完全不是一个量级"。**反推：Ren'Py 的 .rpy 是纯文本、无资源注册，所以本作不需要 MCP**
- **中低配三段式**：在线概念图（**发散**，定风格方向）→ 本地 AI 资产（**收敛**，统一风格）→ 顺手缩到实际尺寸（背景 1920×1080 / 图标 64×64，加载快、包体小）
- **三视图标准化**：纯提示词让通用模型直出标准三视图成功率极低；稳定路线是"通用模型出设计 → SD + ControlNet 标准化"（低 denoising 0.3~0.5 + 正/负向词锁定视角）

### 本机可试清单（16GB 无独显）
- **星辰 Xing4.0-29B-A4B**（中电信，09-17）：MoE 29B/**激活 4B**，主打工具调用与自主执行，低比特量化后消费级显卡可跑 → 本机最值得试的下一个本地 agent 模型
- **PrismML Bonsai 2**：Qwen3.8 27B 压到 5.9GB，内存占用降 9~10 倍
- ⚠️ **OpenRouter Union Alpha** 这类匿名模型：做评测时必须标注"来源不可核实"，别当结论

### 变现 / 发行新思路
- **Sowii（《秃秃》）**：3 个月流水超千万、次留 80%、抖音 200 万粉；**实体盲盒 + 身份卡扫码绑定数字角色**，"催产素驱动的情绪体验"
- 对我们的意义：在"AI 小游戏做出来没人看见"之外，**不指望平台给流量**的那条路——实体做入口、AI 做陪伴、UGC 做传播；**发售时"游戏"不该是唯一的交付物**
- 发售免责口径（Jenova）：留记录、不做版权角色/商标、**必须有人工过一遍**；**纯无人干预生成的图，版权地基比有指导、有修改的图更弱**

### 决策原则更新（第十辑新增）
- **23. 服务端校验优于客户端容错**：面对大模型函数调用的"协议漂移"，防御性解析只是止血；把 JSON Schema 校验放到服务端、不通过直接返回 422，才是根治（+100ms 换 99% 结构稳定）。
- **24. 风格一致性靠"锚点 + 断言"，不靠更强的模型**：人工先定 2~3 个风格基准，提示词强制匹配，加载时检查命名/材质名，不符合就拒绝加载。
- **25. AI 产出必须可审计**：每条产出附 `ai_source.log`（模型 / 提示词 / 时间 / 调用 ID）+ 一份验收清单。让 AI 从"黑箱魔法"变成"可审计工序"。
- **26. 先拆模块清单，再按模块喂**：不是"少让 AI 写手感"，而是先把玩法翻译成功能模块清单（场景/车辆/规则/数据/表现），逐模块交给 AI；有标准答案的基建全给它，"刚度/重心"这类手感值全部自己调。

---

*最后更新：2026-09-20（第十辑）*
*来源索引：index.html（1054 项，本辑新增 6 个待并入）+ csdn-social-summary.md（约 276 条经验帖，第十辑新增 24 条）+ mistakes/（错误记忆，6 条）+ agent-house-rules.md（23 条房规）+ refs/renpy-android-packager-skill（已克隆实测）*
