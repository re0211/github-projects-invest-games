# 跨平台游戏制作 × AI 开发资源梳理（2026-09-20 · 第十三辑）

> 搜索覆盖：GitHub（2 个新仓库全部用 REST API 实测 stars / 语言 / 协议 / 推送日期，无一估算）/ CSDN / 独立开发者博客（test-n-tell）/ arXiv 论文原文 / r/LocalLLaMA（经 AGI Hunt 转述）/ 大模型公司与行业日报（Pondero、The AI Changelog、On The Wire、央广网）/ Dev Community / 工具官网
> 上一辑的主线是**「拆开看」**。这一辑顺着往前推一步：**拆开之后，把"验证"单独拿出来看**——几乎每一篇高价值文章都在说同一件事：AI 把"做出来"变便宜了，"验对不对"成了新的瓶颈。
> 本辑主线 = **「验证侧」**。
> 已有索引：`index.html`（1071 项 GitHub 项目，本辑新增 2 张卡 → 第十八版增补）+ 前十二辑经验帖（累计约 332 条）+ `game-production-pipeline.md`（工具链 + 决策原则 37 条）+ `agent-house-rules.md`（29 条房规）+ `mistakes/`（错误记忆 11 条）
> 上一辑存档：`csdn-social-summary-v12.md`

---

## 本辑一句话

**AI 让"生成"的成本趋近于零之后，所有文章的焦点不约而同挪到了"怎么证明它对"**：游戏 agent QA 用截图闭环、视觉回归区分"有意义的差异"和"无关差异"、游戏原型用状态机当"测试用例的索引"、多 agent 团队用"可运行"当唯一硬验收——**谁先把验证侧搭起来，谁才能真正吃到生成侧的倍数**。

---

## 一、世界模型新路线：程序管状态，视频只渲染（1 条）

### 1. Programmable World Model（Alaya Lab，arXiv:2609.10540，09-09）

视频世界模型玩久了会"变糊"：还剩几个敌人？东西被用掉没有？这些状态只存在于生成的像素里，靠概率模型记逻辑账必然漂。这篇的路线很决绝：**别让像素管状态，让程序管**。

- agent 把自然语言规则翻译成可执行程序，轻量引擎维护**显式、持久的全局世界状态**（含屏幕外实体和背包这类非视觉属性）
- 预训练视频模型只当"渲染器"：状态通过状态增强 3D OBB 编译成时空条件信号喂给它
- CombatStateBench 上自报 94% 计数准确率 / 98% 状态准确率（**自报数字，等独立复现**）
- GitHub：`AlayaLab/pwm`（REST API 实测 **183★**，推送 09-10，已登记 index.html）

> **和第十辑地编失败复盘是同一个命题的另一面**：「AI 的『合理』基于视觉常识，游戏的『可行走』基于数学碰撞」——状态也一样。已经写进决策原则 #23（服务端校验优于客户端容错）的那套思路，在世界模型尺度上再次被验证。

---

## 二、游戏 × AI 新项目（5 条）

### 2. AI-Sandbox（CrazyDashTool/AI-sandbox，Gemma 4 挑战赛参赛作）

Godot 4 沙盒 + 一个"住在世界里"的 AI NPC：每次思考都把世界状态、玩家近期行为、对话记忆、天气，**加一张 NPC 自己视角的 1280×720 截图**发给 Gemma 4 31B，换回一个 JSON 决策（`speech/action/emotion`），解析成真实游戏行为。**"截图进提示词"是我们第十辑从 @op7418 学来的"附图>写话"，在 NPC 感知上是同一个道理。**（API 实测：0★，GDScript，MIT，推送 2026-05-20——项目比文章老，挑战赛贴是补的宣传）

### 3. Godot 4 + AI Agent + MCP：AI 自动回归测试雏形（CSDN weixin_30542979）

让 AI 按固定路径操作场景，`capture_screenshot` 截每一帧关键画面对比，改完物理参数自己验一次而不是把"有没有改坏"抛回给人脑。作者自评"还很粗糙"，但方向和我们 `testcases.rpy` + `_shots/` 的闭环完全一致。文末那句值得抄在墙上：**"AI 生成的代码再流畅，手感上的微妙差距也只有人的输入神经能感知"**——对应我们的决策原则"写手感边界性能必须亲手验"。

### 4. AI 原生 Godot 二十天踩坑：场景树撑爆上下文（CSDN weixin_29015899）

最有价值的一条：Agent 每次改动前都 `get_scene_tree` 拉全树，一棵几十节点的场景序列化就是几千 token，连拉几次之后 agent 开始"遗忘"早期需求。对策是写进项目文档的工具调用规范：**全树只在"开新任务"和"报错且信息不明"两种情况下读，平时只读目标节点的局部属性**。这和第十二辑论文的结论（上下文管理的价值=防溢出）在实践侧完全对上了。

### 5. Ren'Py 视觉小说网页化实战（CSDN weixin_33507732）

一个 GPLv3 同人项目把 Ren'Py 游戏打成 **index.html + wasm 零安装网页版**（155 张立绘 / 4 个 .rpy / 2 个音效，46MB）。对本作的启示：**网页发行是 Ren'Py 成品最低门槛的"试玩版"渠道**——以后做 demo 分发可以考虑，不用任何人下载 exe。（注意：作者强调叙事重构不是"把文字塞进引擎"，那部分是水文；有用的就是 web 打包结构本身）

### 6. Ren'Py Visual Programming Editor（fvn.li，$ 预售中）—— 反面教材

 itch.io 上的付费可视化编程编辑器，9 月评论翻车："connectors aren't logical"、"AI created tool 卖太贵"。**价值在评论区：纯 AI 复刻已有工具功能、没有真实使用打磨就收费，社区会直接点名。**对应我们的原则：AI 写标准模块可信，但"产品"要人用出来。

---

## 三、验证侧方法论（本辑最厚的一节，7 条）

### 7. 《Early game dev: one leap forward, four steps back》（test-n-tell，09 月）

两周实测复盘，两个结论值得永久保留：

1. **"AI 让前 70% 快得惊人，但产品不在 70% 发布。"**核心机制几天就通了，从"能跑的软件"到"看起来、摸起来像个真游戏"花了数倍时间——这正是本工作区第 5/6/8 轮在补的东西（闸门、配音、特写都是"后 30%"）。
2. **"对 LLM 描述你要的价值，比描述要建什么、更比描述怎么建，结果更好。"**作者让 Codex 照自己的方案实现 Crazy Balls 模式，吃掉了大头开发时间；事后意识到应该先让模型模拟几个方案再锁定义。

### 8. 一人 + 49 个 AI 员工（CSDN weixin_29061509 + weixin_32899685，同系列两篇）

六个坑里三条直接可抄：

| 坑 | 对策 | 对应本工作区 |
|---|---|---|
| 设定漂移（角色名"阿岚"变"阿兰"、暴击上限 100% 变 200%） | **单一事实源**：全项目角色名/系统名/数值上限写在一个 constants 文件里，任何 agent 开工前必读，"有疑问查总纲，不要猜" | 我们没有——**待落地**（见自测） |
| AI 追求"正确"不追求"高效"（寻路单测全过、实机帧率个位数） | 程序类交付必须附**复杂度说明和潜在瓶颈分析** | 决策原则"性能边界亲手验"的补充 |
| 验收模糊（"做个攻击特效"交了个没接进攻击事件的粒子文件） | 需求强制**"条件 + 动作 + 可观测结果"三段式**（日志输出 spawn_fx 关键词） | 决策原则 #25"AI 产出必须可审计"的同义强化 |

另有**体验评分卡**（视觉模型按"UI 有没有重叠/按钮醒不醒目"逐项打分）和**短会话工作制**（每次任务只加载需要的文档片段，交付完立刻结束会话、留下结构化摘要）——后者就是房规 #28"可回收上下文是纯负担"的工程化版本。

### 9. Claude Teammate 中医游戏开发心法（hqwc.cn/a/1334002）

项目没做完，但复盘比成功帖诚实：长对话里设计原则会被淹没 → **"项目宪法"**（核心规范条目化固定）+ 开新模块前**主动复述确认** + 按模块拆对话。我们的 `agent-house-rules.md` + `pipeline.md` 就是"项目宪法"的实物形态，这条算验证了现有做法。

### 10. GPT-6 Astra 做游戏实践：状态机是给模型的，也是给测试的（seeles.ai）

原型最容易出的 bug 是**状态互相穿透**（胜利了还能移动、重置后旧监听器触发两次）。解法是把状态转移表写清楚（当前状态/事件/下一状态/必须发生/必须禁止）——**"状态转移表既是给模型的上下文，也是测试用例的索引"**。还有一条"验证闭环五步"：生成→运行→观察（六维度）→记录（失败归类）→**只改一件事重跑同一条测试路径**，每轮留一份短 receipt。**这就是我们"一个 diff 一个关切"的通用版。**

### 11. AI agents in mobile games: QA on real devices（mobilerun.ai）

厂商博文，但分界线画得清楚："传统设备农场脚本在 UI 移动 10 像素时就崩；agent 像玩家一样读屏，按钮美术改了也认识"。可测的：新手漏斗、分地区 live-ops 检查、沙盒 IPI 全流程、真机 nightly soak，结构化结果 + 截图进 webhook。**明确不做代练/多开**。对我们：单机 VN 用不上真机矩阵，但"结构化结果 + 截图"的产出格式值得抄——`testcases.rpy` 已经是这么干的。

### 12. AI 驱动测试工具 2026（hqwc.cn/a/78237）

把视觉回归的核心难题讲清楚了：**Applitools 类工具的价值不是"找不同"，是区分"有意义的差异"（按钮移位）和"无关差异"（字体渲染微差、动态内容）**。这正好解释了我们 `check_font_coverage.py` 的两次误报教训（M-0009：闸门范围过宽会假警，比没有更差）——**一个会喊狼来的闸门迟早被无视**。

### 13. LumeValley 游戏测试 AI（lumevalley.com，厂商软文，降权收录）

唯一值得记的一条：**根因定位不是让 AI 下结论，是让 AI 缩小排查范围**（把缺陷单、日志、代码变更连起来给方向）。软文，方法通用。

---

## 四、AI 美术：角色一致性三条（第 8 轮直接用上了）

### 14. Consistent Characters 2026 Guide（text2img.pro，两篇同站）

把"一致性不是模型特性，是你搭的工作流"讲得最系统的一篇。可抄的三件套：

- **12 点角色卡**：年龄/脸型/眼眉鼻嘴/肤色瑕疵/发色发质/体型/默认服装+标志物/性格形容词/招牌表情——每条写成**固定的短语**
- **Anchor Phrase 方法**：25~80 词的"身份块"逐字复用、永远不改动、永远放在提示词**最前面**（前面的 token 权重高）；场景/表情/光线只写在后面，可自由变
- **三大漂移源**：提示词改写（同义词换词=换人）、seed 变化、镜头距离（全身比特写需要模型编更多细节）

> **第 8 轮实际用法**：灰毛特写没有走"改提示词重新生成"，而是按同一套角色特征生成独立头肩构图——就是这篇"身份块不动、只变镜头距离"的实操版。成品零漂移。

### 15. 独立游戏 AI 美术流水线（hqwc.cn/a/434115）

经验密度一般的合集帖，两条有用：**负面提示词库**（建一个自己的通用负面词文件，每次调用）和**把生成参数写进文件名**（`Barrel_[Model_RPGV5][Seed_12345].png`，复现时直接找回配置）。后者我们没有做——SOURCES.md 记了提示词但没记 seed，因为平台没暴露；如果以后换平台，这条是硬要求。

### 16. 2D 游戏立绘 ComfyUI 工作流（xxmr.cn 转载，源头不明，降权收录）

给了可执行的经验区间：Steps 25-30 / CFG 6-7 / LoRA 权重 0.6-0.9；**CFG 太高边缘过锐，太低"AI 味"重得像糊了雾**；"CLIP 对特征词组的抓取比长句稳定"。转载站，参数方向可信、数值需自测。

---

## 五、本地模型（16GB 机器直接相关，3 条）

### 17. 16GB 显存跑 Qwen3.8-27B 做村庄模拟游戏（r/LocalLLaMA via AGI Hunt）

RTX 5070 Ti 16GB，Qwen3.8-27B **UD-Q3_K_XL** 量化，tg 75 t/s、上下文 96K，做出有昼夜季节/资源/御寒/饥饿死亡的村庄模拟 POC。核心经验：**与其用高量化+部分卸载 CPU 掉到 5-20 t/s，不如低量化换全 GPU 高速，出问题靠 prompt 修**；开发方式是增量 feature prompt + handover 文档管理上下文。**对 16GB 内存（无独显）的我们：跑不动 27B，但"低量化全量进显存 > 高量化半卸载"的判据是通用的，未来换机器直接用。**

### 18. Best Local LLMs September 2026（ai-master.dev）

档位表：8GB→9B Q4；**16GB→MoE 35B-A3B / DeepSeek V4 Flash Q4（20-40 t/s）**；24GB→122B-A10B 部分卸载。结论跟我们此前一致：16GB 是 MoE 的甜点档。聚合站，数字方向可信。

### 19. 你到底需要多少显存（Dev Community）

最实用的只有那个 napkin 公式：**VRAM ≈ 参数量 × 每权重字节数 + 余量**（Q4_K_M=0.5B/param，Q8=1.0，F16=2.0；余量给 KV cache 留 2GB+）。以及一条反直觉的：**模型装不下时，第一动作不是换小模型，是降量化**——同一颗脑子四分之一的价格。

---

## 六、AI 公司 / 行业（8 条）

### 20. Grok 4.7（09-12，xAI）

参数 2.1 万亿（较 4.6 的 1.5 万亿 +40%）。马斯克宣称全面超越——**按惯例等第三方评测再定**（M-0002）。

### 21. K2 Horizon（MBZUAI 基础模型研究所，09-04 上旬）

**0.9B~375B 六个模型全部 Apache-2.0，权重、代码、训练数据全开**——目前开源最彻底的前沿模型舰队。和闭源 GPT-6 Astra 形成两个极端赌注。对小团队：0.9B~9B 档可能出好用的离线 NPC/分类小模型，**待观察是否有社区微调版**。

### 22. UMG × ElevenLabs 多年授权协议（09-10）—— 对我们 BGM 替换路线有影响

ElevenLabs 第一份大厂牌授权：粉丝可用参与艺人曲目做 remix/mashup。**信号：AI 音乐平台的版权合规化在加速，"训练数据合法性"正在从风险变成卖点。**本作 BGM 替换候选（Suno v6-mini / Lyria 3.5）商用条款仍要逐条读，但时间站在合规这边。

### 23. Microsoft MAI-Transcribe-2（09-06 当周）

自研语音转文本：多语种榜第一，**$0.10/小时音频**，直接打 OpenAI/Google/ElevenLabs 的转写业务。对做游戏本地化字幕后处理的人是价格锚点。

### 24. Anthropic：Claude Docs + Claude Slides（09-16）

Claude 内置两个编辑器（文档可导 Word/Google Docs；幻灯片可放映可导 PPT/PDF），Pro/Max beta。**"对话产出 → 可交付文档"的最后一公里在被平台补齐。**

### 25. Cursor Projects（09-10）

IDE 升级成云原生项目执行环境：一个 Project 持有上下文数月，协调 agent 派活给**数千个并行云端 subagent**，合盖不停机。与 OpenAI Agents API 同日发布——**"长时程 agent 平台"成了新的正面战场**，和我们无关但值得知道：单人 + 平台型 harness 的产能天花板又被抬高了。

### 26. ABC-Bench（ACL Findings）

面向 agentic 后端编码的基准：规划/工具使用/测试/恢复四维度可复现指标。选型时比"排行榜总分"更贴近真实 agent 工作质量，**记入评测工具箱**。

### 27. 九月发布密度盘点（央广网 09-16）

三季度国内外厂商 9 月集中发旗舰：09-01 Fable 5.1 → 09-03 GPT-6 Astra → 09-10 DeepSeek V4.1-Flash → 09-12 Grok 4.7。行业解读：Scaling law 未破，但**"每提升一个百分点换同等能力，成本指数上升"**。对我们的实操含义不变：**追新模型没有意义，追"单位成本的任务完成率"才有**（DeepSeek V4 Flash 路线继续有效）。

---

## 七、AI Dev 自测结论（本辑）

- **test-n-tell "后 30%" 命题** ✅ 真有用 → 直接命中本工作区现状：第 0-4 轮做的是"前 70%"，第 5-8 轮全是"后 30%"。**写成决策原则 #38。**
- **单一事实源 constants** ✅ 真有用，**待落地** → 下轮给 amphoreus-roast 建 `game/00_canon.rpy`（角色名表、成就条件、结局表已散在 00_memory 里，收敛成一处）。**不新开原则**——它是决策原则 #24"风格一致性靠锚点"在数据侧的实例。
- **"描述价值 > 描述怎么建"** ✅ 真有用 → 写成决策原则 **#39**（给 AI 指令先说"要什么效果"，方案让模型提）。
- **复杂度说明/三段式验收** ✅ 真有用 → 并入决策原则 #25（AI 产出必须可审计）。
- **text2img 身份块方法** ✅ 已在第 8 轮实操验证（特写零漂移）。
- **PWM 世界模型 / AI-Sandbox / ABC-Bench / K2 Horizon** ⚠️ 信号记录，未落地（世界模型要 GPU；ABC-Bench 是选型工具）。
- **UMG×ElevenLabs / MAI-Transcribe / Cursor Projects** ⚠️ 行业信号，影响的是未来路线不是本周动作。
- **本辑主动剔除的重复项（M-0011 纪律）**：Eluvien AI-RPG（第五辑已收）、banjtheman/renpy_mcp_server（第十一辑已实测收录）、LingBot-World 2.0（第八辑）、Jev / GPT-6 Astra / DeepSeek V4.1 / Anthropic Projects 并行线程（第七/十一/十二辑）、Jenova 立绘生成器（第十辑）、gaugius/aitooldiscovery 等纯 SEO 榜单 3 条。

---

## 八、落进游戏的（同期完成 · 第 8 轮）

本辑调研当轮落进了游戏一轮：**立绘头部特写差分**（详见 `amphoreus-roast/ROADMAP.md` 第 8 轮交付）。

- 灰毛 snark / flat 两档头肩特写，脸放大约 4 倍，剧本 6 处情绪重音点接入
- 用到的本辑资料：#14 text2img 的"身份块不动、只变镜头距离"（特写按同一套角色特征单独生成，零漂移）
- 踩的坑（已记 mistakes）：**水印压在人物身上时，全身那套"右下角无差别清零"会把人挖个洞** → 先裁底部 9.5% 再抠图（M-0012）；**`git add -A` 扫进上轮遗留临时文件** → 提交前先 `git status`（M-0013）
- 验收：lint 0 警告 / test PASSED（17 截图）/ check_sprites **14/14** / 台词+字体+音频三闸门 PASS

---

## 九、索引更新

- `index.html` **第十八版增补 2 张卡**（卡片 1071 → **1073**，脚注 [1071]-[1072]）：
  - `AlayaLab/pwm`（183★，程序管状态+视频渲染，方向信号）
  - `CrazyDashTool/AI-sandbox`（0★，Gemma 4 NPC 沙盒，附图提示词实证）
- ⭐ 本辑卡片少的原因：新项目要么是论文代码（还没到"工具"阶段），要么是挑战赛作业（0★）。**价值在方向信号不在成熟度，评分口径不变。**

---

## 十、下一辑搜索缺口（给第十四辑）

1. **Ren'Py 8.5.3 web 发行实测**：第 5 条只有二手信息，`renpy.sh launcher build_web` 的 wasm 包体积/加载时长没人给数据——对本作的"网页试玩版"路线是前置条件
2. **K2 Horizon 小模型微调实测**：0.9B~9B 档有没有人做中文角色扮演微调（对"其余 12 角色配音的语气分类"有用）
3. **Kokoro 之外的本地中文 TTS 新版本**：第十二辑收的 sherpa-onnx 路线有没有出新（帕姆口癖的语速/音调变体）
4. **"单一事实源"在 Ren'Py 的现成实现**：constants/canon 文件模式有没有社区模板（我们可能要自己写）
5. **AI 音乐商用条款横向对比**：Suno v6-mini vs Lyria 3.5 的商用授权原文（BGM 替换前的必答题）
6. **UE 5.8 官方 MCP 插件的真实使用复盘**（第十一辑只收了发布消息，缺一手体验）
7. **中国平台 AI 披露规则**：TapTap/好游快爆有没有跟进 Steam 式披露要求（出海+国内双渠道都需要）

---

## 附录 A · 补充批 26 条（并发实例产出，方向互不重叠）

> ⚠️ **本批的来源**：本次定时任务被**重复触发**，两个实例并发执行同一任务。
> 另一实例产出了上面第一至十节（27 条，主线"验证侧方法论 + 世界模型 + AI 公司动态"）；
> 本批是另一实例搜到的、与上面**零重叠**的 26 条，主线是**「把游戏交出去时会撞上什么」**：
> 引擎官方下一版 · 两个分发平台实操 · 披露与本地化的真实成本 · 中文 TTS 横评 · 游戏×AI 新项目。
> 两边各自做了去重比对（v1-v12 + index.html），合并后累计约 **385 条**。
> **教训已记入工作区：定时任务重复触发会造成并发写同一文件，需先查文件 mtime / 是否已有本日产出。**

### A1 官方引擎的"下一版"（Ren'Py，2 条）

1. **当前正式版仍是 8.5.3（2026-05-15「We Can Go to the Moon」），官方主线是 SDL3 移植**
   https://www.renpy.org/ ｜ https://patreon.renpy.org/dev-2026-02.html
   —— 2 月月报：`renpy.pygame` 与声音系统已迁完，桌面三平台可构建，之后 HTML5 → Android → iOS。
   本作就跑在 8.5.3，现在升级没有收益。
2. **master（8.6.0）不兼容变更清单（官方原文）**
   https://github.com/renpy/renpy/blob/master/sphinx/source/incompatible.rst
   —— 三条要紧的：**① 8.6.0 用 SDL3，`get_sdl_dll()` 需传 version=3**；
   **② voice 语句默认不再参与翻译标识符**（`config.tlid_only_considers_say=False` 可退回）
   → **直接关系第 6 轮 159 句配音与将来的英文版，翻译 ID 会漂**；
   **③ late audio scan**：自动音频定义改到 late init。另：8.7 移除 zsync；8.5.4 Live2D 贝塞尔语义变更。
   ✅ **已落地**：写进 `ROADMAP.md` 技术债——**升级 8.6 前必须先确认这三条**。
   ❌ **未采用**：CSDN 文库称"官方 Roadmap 已确认 9.x 重构 transform 调度"，官方仓库无 9.x 痕迹（M-0002）。

### A2 两个分发平台的完整实操（5 条）

3. **Steam 首发 23 步清单（中文，作者踩过一遍）**
   https://ima.qq.com/wiki/?shareId=37edeee193a4807f7262f8b06584d1cd4567c3d41f5f68ea13791260e43b9f42
   —— $100 应用费 + 强制等待期；注册 1-5 天 / 商店页 2-3 天 / 包体 3-5 天（**周末不上班**）；
   商店页通过后到发行**至少隔 14 天**；新品节需"报名截止前注册满 30 天 + 包体过审 + 活动后不发正式版"。
4. **soonlab《Publish on Steam 2026》** https://www.soonlab.ai/blog/how-to-publish-a-game-on-steam
   —— ⚠️ 等待期写 **30 天**，与第 3 条的 21 天**冲突** → **以 Steamworks 后台显示为准**。
   首次发行建议排 **6-8 周**；最常见失败是"只在自己机器上测过"（缺 DLL / 路径 / 运行时）。
5. **thegamemarketer 2026 分步指南**（英文交叉印证）
   https://www.thegamemarketer.com/insight-posts/how-to-publish-your-game-on-steam-guide
6. ⭐ **itch.io 官方创作者质量准则（AI 部分）** https://itch.io/docs/creators/quality-guidelines
   —— ① 新增 Generative AI disclosure 字段（图形/声音/文本与对话/代码），选是自动带 `AI Generated` 标签；
   ② **未标记的 AI 资产不进浏览页索引**（不删除，只是搜不到，比 Steam 更狠）；
   ③ ⚠️ **新红线：「主要由算法或 AI 生成、人工干预极少」的作品直接点名为 spam**；
   ④ 自包含算法（程序化关卡、NPC 寻路、动态音乐）不算生成式 AI，无需标注。
7. **itch.io 政策中文报道** https://www.bay006.com/bay/2026-06/15122 ｜ https://applet.10100.com/article/1230941
   —— 补执行细节：过渡期 + 批量标记工具 + 之后靠用户举报识别。

### A3 披露与本地化的真实成本（5 条）

8. ⭐ **Valve 2026-01-16 重写 Steam AI 披露规则**（双源交叉）
   http://gamedevaihub.com/steam-ai-disclosure-guide ｜ https://artland3d.com/?p=8574
   —— **效率类工具不再是本节重点**（代码助手 / 调试 / 重画掉的概念图 / 自素材放大降噪，全不用披露）；
   旧文案里 **"code" 从示例清单中悄悄消失**（作者提醒：这是范围收窄，不是免死金牌）；
   只有**玩家会消费的内容**需披露；实时生成要写护栏 + 覆盖层举报按钮；成人实时 AI 绝对红线；
   **Valve 已在下架披露不准确的商店页**。
   → **本作结论**：AI 用在背景/立绘/语音/BGM 上**仍需披露**；AI 辅助写代码**已不在范围**。
9. **政策原文被静默改写过** https://artland3d.com/?p=8574
   —— 旧措辞 2026-05-13 仍在线，**06-17 已换新**，无公告无 changelog。
   数据：已披露 10,258 款（约占全库 8%，估算 $660M）；Game Oracle 2025-12：控制变量后
   **披露方首月评测约为同类一半**（相关非因果）；反例 Arc Raiders 带披露照样成年度大作。
10. **Tim Sweeney"红字"争议** https://www.delightfulblogs.com/tech/steam-ai-disclosure-discovery-reviews-debate
    —— 争议实质是**曝光不是诚实**：2025 年 Steam 发行约 17,900 款，**约一半评测数不足 10 条**，
    而曝光引擎靠评测驱动 → 对小团队只有一条正解：**如实披露 + 想办法拿到真实评测**。
11. **游戏本地化 2026 报价横评（三源）** https://www.gamedevoutsourcing.com/blog/game-localization-cost-guide ｜
    https://www.auto18n.com/en/blog/translation-cost-per-word-2026 ｜
    https://www.artlangs.cn/newsDetail/translation-newsdetail/36653.html
    —— 人工 $0.08-0.20/源词 + LQA $25-80/h（4 万词 8 语言 ≈ $57.6k）；
    **NMT API $10-25/百万字符（与人工差 1000 倍）**；LLM 翻译 $0.00003-0.002/词；
    国内全流程（含 LQA）0.7-1.8 元/字。
    → **本作**：411 对话块 / 5,642 字，机翻成本≈0，真正的成本是**本地化工程（`_()`）与抽检**。
12. **strayspark：AI 本地化平台横评** https://www.strayspark.studio/blog/ai-game-localization-indie-developers
    —— 可抄的判据：**UI 与系统文本走专用翻译 API（便宜稳），叙事与对话走 LLM**（能保持角色口吻与文化适配）；
    游戏专用模型的价值在术语表、复数形式、置信度打分。

### A4 2026 本地中文 TTS 横评（4 条）

13. **博客园六模型选型指南** https://www.cnblogs.com/sensorsen/p/21367537
    —— CosyVoice 2（0.5B/4GB/3s 克隆/情感）· Qwen3-TTS（97ms）· Fish Speech 1.5（1s 克隆/社区最活跃）·
    IndexTTS2（8GB/7 情感+时长）· F5-TTS（0.3B/3GB/**无情感控制**）· Spark-TTS（1-2GB）。
    ✅ **结论：本机 16GB 无独显，Kokoro 仍是最优解**（第 6 轮已量产 159 句）。
14. **CSDN：F5-TTS vs CosyVoice 2（M1 Pro 实测）** https://blog.csdn.net/u011831527/article/details/162006244
    —— F5 是 DiT+Flow Matching，**无时长模型/无文本编码器/无音素对齐**；CosyVoice 2 自回归+流匹配、
    9 种情感与方言。要轻要快选 F5，中文最自然选 CosyVoice 2。
15. **CSDN：四方案横评 + 许可证** https://blog.csdn.net/chenying998179/article/details/161491545 ｜
    https://qianchilang.blog.csdn.net/article/details/145504376
    —— VoxFlash Docker 一键（854MB ONNX）；GPT-SoVITS 需 12G+；**Kokoro 是唯一标注 CPU 可用的**。
    ⚠️ **许可证**：CosyVoice 2 / Fish Speech 是 Apache-2.0（商用友好），
    **GPT-SoVITS 预训练模型是 CC-BY-NC（非商用）** —— 上架前必看。
16. **GitHub 新 TTS（均未安装）**：`FireRedTeam/FireRedTTS3`（1623★，多语言多方言 + **指令化声音设计**）·
    `breezeblue-ai/breeze-tts`（460★）· `nari-labs/nari-qwen3-tts`（176★，Qwen3-TTS 首包 <50ms）·
    `ChenShuo2004/cs-board`（629★）· `Vincentwei1021/anything2explainer`（1823★，Remotion + **Kokoro**）。
    ⚠️ 不装；**FireRedTTS3 记为"有显卡后第一个试"**——指令化声音设计正好绕过
    ROADMAP「明确不做：逐句调音色」的限制。

### A5 游戏 × AI 新项目与信号（10 条）

17. **`Station-Sciences/bot-crossing`（631★）** https://github.com/Station-Sciences/bot-crossing
    —— "一款给 AI agent 玩的游戏"，与第八辑 `minecraft-agent` 是同一件事的两端。
18. **`gary149/h3-game-sprites`（127★）** https://github.com/gary149/h3-game-sprites
    —— Agent Skill：**AI 生成视频 → 2D 精灵表**（真人快打方法，MiniMax H3 当演员）。
    与我们的**绿幕静帧**路线互为对照：优点是天然带动作，缺点是一致性更难控。⚠️ 需 H3 能力，仅参考。
19. **`wave-race-64-recomp`（62★）** https://github.com/danielgomesvieira2000/wave-race-64-recomp —— AI 编码的 N64 PC 移植。
20. **Thursday Arena（09-18，X / Inshorts）**
    https://inshorts.com/en/news/musk-s-team--set-to-build-entire-company-in-3-days-using-ai--builds-a-game-instead-1789745709000
    —— 马斯克团队"3 天建一家公司"，交出来的是一款 bot 自走棋。**"游戏"已是 agent 能力的默认演示品**
    → 纯 vibe coding 供给还会暴涨，第 10 条"评测不够"的问题会更严重。
21. **《无为修仙传》续报（09-02）** https://www.toutiao.com/article/7680734408944501283/
    —— 第 3 款 AI 游戏，8 天，Codex + GPT-5.6 Sol，美术 GPT-image-2，BGM 天工 Music，¥9.9。
    ⚠️ **风险样本**：作者明说"零手写代码、**零 review**"——与第十一辑老刘（有倒推式提问与人工验收）是两种做法。
22. **`FlameskyDexive/XEngine`（24★）** https://github.com/FlameskyDexive/XEngine —— dotnet10 开源 3D AI 引擎，含鸿蒙。
23. **小群**：`wilsjo2/OptiScaler-DLSSNR-PreSR-Multipass`（645★，博德之门 3 DLSS 神经渲染 mod）·
    `groundboxerrespect/Dlls5-auto`（315★，自托管 DLSS5 式服务）· `29-Cu/bisca`（28★，Claude 同桌打牌）·
    `coffeemug/squidgpt`（32★，淘汰死亡游戏研究 agent 行为）。
24. **GLM Worlds 2（智谱）** https://codemypixel.com/blog/ai-news-september-2026-gpt-6-astra
    —— 720p / 24fps 交互虚拟世界；同篇有 Solar WM、World Labs Atlas。⚠️ 前沿信号，需大显存，不落地。
25. **DeepSeek-V4-Flash-Vision-Exp（09-08）** https://agentic-ai-news.uk/?date=2026-09-08
    —— 社区反馈"能吃游戏截图，几天做出像样的游戏世界"。⚠️ 选型信号，当前不接入。
26. **Godot 4 口型驱动机制（补上第五辑"音频同步"缺口）**
    https://lobehub.com/skills/thedivergentai-gd-agentic-skills-godot-dialogue-system
    —— 机制两行：`tts_set_utterance_callback(TTS_UTTERANCE_BOUNDARY, cb)` + `tts_speak()`，回调拿 `char_idx` 驱动嘴型。
    **与本作对照的结论**：Godot 是"实时 TTS + 逐字回调"，Ren'Py（本作）是"整句预生成 + 整句播放"
    → **本作配音天然做不了口型**；将来真要做口型/节奏演出得换引擎或自接回调（属「明确不做」）。
    附：Godot 侧 VN 方案 Dialogic 2（https://blog.csdn.net/gitblog_00528/article/details/154505879）；
    面部动画全链路（https://blog.csdn.net/weixin_32924297/article/details/161297831，Godot 4.3 实测）。

### A6 补充批自测结论

| # | 结论 | 落到哪 |
|---|---|---|
| A2 | ✅ 已读并落地 | ROADMAP 技术债：升级 8.6 前确认 voice/翻译 ID、late audio scan、SDL3 |
| A6 | ✅ 真有用 | 本作 itch.io 标签应为**图形 + 声音**；"人工干预极少"是必须避开的表述 |
| A8 | ✅ 真有用 | README/关于页披露口径：代码辅助已不在范围，素材与语音仍在 |
| A11 | ✅ 真有用 | 第 10 轮英文版预算依据：机翻≈0，成本在工程与抽检 |
| A13-15 | ✅ 真有用 | 反证 Kokoro 选型；GPT-SoVITS **非商用许可**记进"以后别踩" |
| A16 | ⚠️ 不装 | FireRedTTS3 记为"有显卡后第一个试" |
| A18 / A20 / A21 | ⚠️ 参考 / 信号 / 反面教材 | "零 review"列为风险样本 |
| A24 / A25 | ⚠️ 选型信号 | 不接入 |
| A17 / A19 / A22 / A23 | ⚠️ 记录 | 方向信号，未实测 |
| CSDN 文库"Ren'Py 9.x" | ❌ 不采用 | 官方无出处（M-0002） |

### A7 补充批去重（剔除 5 项）

- 第二辑 #30 已收 weixin_27945229《三个月经验总结》→ 同系列 07/08 三篇不重复收
- v3 第 17 条已收 Ziwen Xu / GT-Caliber → 三篇转载不收
- v9 第 8 条已收 `Eurekaleo/awesome-ai-for-games` → 不收（205→208★）
- 《无为修仙传》v5 #15 / v11 #11 已收 → 只作续报（补"零 review"）
- CSDN 文库"Ren'Py 9.x roadmap" → 官方无出处

### A8 补充批新增缺口（并入第十四辑）

- **Steamworks 后台实际等待期**（21 天 vs 30 天两说冲突，需一手证据）
- **上架后如何拿到前 100 条评测**（第 10 条显示这才是生死线）
- **itch.io 流量机制**（本批只查了政策，没查免费/付费/捐赠各能带来多少曝光）
- **本地化工程怎么做**（`_()` 的具体步骤与坑，为第 10 轮铺路）
- **国产视频生成模型的价格与配额**（若走 A18 的"视频取帧"路线）

---

*统计（合并后）：第十三辑共 **27 + 26 = 53 条**新增（另剔除重复/SEO 17 条）→ 累计经验帖约 **385 条**；
GitHub 索引 1071 → **1073 项**；决策原则 37 → **39 条**；mistakes 11 → **13 条**。*
