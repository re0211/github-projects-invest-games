# 跨平台游戏制作 × AI 开发资源梳理（2026-09-20 · 第九辑）

> 搜索覆盖：CSDN/掘金/博客园、国内大模型公司官方动态（千问三连/阿里）、海外（Suno/Google Lyria/NVIDIA/OpenRouter/Trail of Bits）、GitHub 趋势（PullRepo 日报 + 仓库核实）、社媒（r/ClaudeAI→agihunt / Show HN / PC Gaming Wiki 事件链 / arXiv）、Modding 专项（Minecraft/Modding 社区）
> 本次为第九次增量，聚焦「LLM 驱动世界（AI 小镇）」「Modding 社区 AI 使用规范」「本地 TTS 配音选型落定」「协议先行方法论」
> 已有索引：index.html（1054 项 GitHub 项目）+ 前八辑经验帖（累计约 228 条）+ game-production-pipeline.md（工具链）+ mistakes/（错误记忆 4 条）+ agent-house-rules.md（21 条房规）
> 去重基线：已逐条比对 v1-v8 全量条目 + index.html 1054 项。本辑 24 条零重复。
> 去重记录（本次主动剔除）：
> - ❌ hqwc 1442690「AI真能做游戏吗」——v8 #9 已收录（本次搜索再次命中，判重）
> - ❌ mzlw.cn/news/121610 像素射击全流程——v7 #14 同一 URL，判重
> - ❌ Game×AI Native「开篇」（CSDN 165889155，wsc122181582）——v6 已收该系列九篇（同作者），判重
> - ❌ debpalash/VoiceStudio——v5 #27 已收录（本次 heatdrop 页为同一项目），判重
> - ❌ Qwen3.8-Omni-Flash 模型本身 / GLM-5.3-FlashX——v7 #5 已收录；本辑 #14 收的是**同日新放出的开源组件与 LiveTranslate**，属新条目
> - ❌ Google I/O 2026 系列长文（bizarro/treeplmn）——5 月旧闻（Gemini Omni/3.5 Flash 等均已过期），不收
> - ❌ mhpq「AI 大模型日报」模型时间线——汇总文且条目多为 4-7 月旧闻，个别新点（GPT-5.6 家族）信源单薄，不收
> - ❌ Figure Helix 2.5 / 丰田机器人需求——具身智能方向，延续 v7/v8 判定不收录
> - ❌ 豆包 2.1 Pro 0915 / 谷歌 Gemini 红队越界 / Hacktron Opus 5——v8 #19/#20/#21 已收录（12pb 日报再次命中，判重）

## 本辑一句话

**"AI 用进游戏"从模型能力竞赛，走到了工程规范竞赛**：Harbour Masters 的 Modding 社区 AI 争议（披露/parity 测试/署名）定下了开源 Mod 项目用 AI 的三条规矩；Qwen 一天放了三样能直接接进工作流的东西（MM-Plugins / LiveTranslate / Qwen3-TTS 仓库核实）；本机最该用的三件事全部落到 amphoreus-roast 的排期上（Qwen3-TTS → 第 5 轮配音、Suno v6/Lyria 3.5 → 第 2 轮正式音频候选、程序化占位音已先行合入）。

---

## 一、游戏 × AI 新项目（本辑最大增量：LLM 驱动世界）

### 1. my_ai_town（mewamew，Godot 4.7，2026-08-08 首次开源）——✅ GitHub 仓库深读
- **一句话**：LLM 驱动居民生活的像素小镇模拟（单机生活模拟），居民有自己的性格/职业/关系/记忆，会自主决定去哪、做什么、和谁说话
- **关键架构（对本工作区游戏直接可借鉴）**：
  - 仓库结构 `game/agent/`（居民决策/提示词/记忆/模型接入）、`game/world/`（世界数据/规则/地图/表现）、`game/ui/`、`game/tests/`（合同测试+集成测试+运行验收）——**测试和验收是一等公民**
  - **「世界日志」与「居民记忆」分离**：客观经过由世界系统确认，每个居民对同一件事可以有不同主观理解——这正是"剧本记得你选了啥"（amphoreus-roast 的 persistent 层）的规模化版本
  - 照片进记忆的处理：先转文字再入记忆，原始图片立即清理（控制长期运行的上下文膨胀）
- **运行**：Godot 4.7 + 任意 LLM API（游戏内设置配 key，不写仓库）；Windows 用 D3D11(ANGLE) 兼容渲染
- **注意**：⚠️ 仓库根许可证"仍在整理"——**可学架构，不可抄代码**
- **实用性 ★★★★**：与我们的 persistent/记忆层设计同构，第 4 轮成就系统/第 6 轮章节回顾可直接参考它的"世界日志"模式
- **来源**：github.com/mewamew/my_ai_town（0.1.0-beta.6，9 月初仍在活跃迭代）

### 2. CaLLMar（HN 项目 → hqwc 两篇教程）——⚠️ 摘录级（原文 fetch 超时）
- **一句话**：把经典文字冒险游戏搬进 LLM 聊天窗口——模型当"游戏主持人"，玩家输入/模型输出/游戏状态三者形成稳定循环
- **核心工程点**：聊天框不是用来聊天的，是用来推进**状态循环**的（`player_location / inventory / health` 每轮都要模型参考并更新）；先设计状态机再跑最小原型，再校验+批量场景生成
- **适用**：给"对话式游戏原型"找练手小项目的三类人（玩家/Agent 工程师/互动叙事设计师）
- **实用性 ★★★**：与我们"LLM NPC 不做"的决策不冲突——它是状态循环+自由文本的中间形态，以后做对话式品类时再启用
- **来源**：hqwc.cn/a/1370091.html + hqwc.cn/news/1367706.html（两篇同源，后者更偏最小原型代码）

### 3. jev_vampire_survivors（r/ClaudeAI → agihunt）
- **一句话**：Reddit 用户 vibe-code 了一个 Vampire Survivors mod + Python "大脑"，让 Jev（System 1 模型）实际玩割草游戏，代码已开源
- **价值**：Jev 生态（第八辑主线）在游戏场景的第二个公开 demo（第八辑收的是 minecraft-agent 打末影龙）；"模型做决策 + mod 做世界"的分工模式第三次被独立验证
- **实用性 ★★★**（信号级）：System 1 在游戏里的用法从"规划+控制"细化到"持续决策引擎"
- **来源**：agihunt.info（via r/ClaudeAI），repo `jev_vampire_survivors`

### 4. GPT-6 Astra 把 BO2「Hijacked」地图搬进 Minecraft（yomimono，引 GameBusiness.jp）
- **一句话**：开发者 Luckey Faraday 用 GPT-6 Astra 把一个先在浏览器里跑通的地图项目整体重写为 Java Fabric mod（地图/碰撞/bot/导航网格/武器/渲染全进 Minecraft 的 OpenGL 上下文），视频显示 45fps 全屏
- **注意**：作者自述"还有很多问题"，非完工品；单信源（GameBusiness.jp）
- **价值**：跨语言跨运行时整包重写（Web→Java mod）是当前旗舰模型"携带整个项目"能力的具象数据点
- **实用性 ★★☆**（信号级）：游戏移植/跨引擎重写场景的参考案例
- **来源**：yomimono.id/ai-coder-runs-black-ops-2-s-hijacked-map-inside-minecraft-using-gpt-6-astra

### 5. DeepSeek-V4-Pro 生成 Minecraft Java 模组全流程（hqwc 1287112）
- **一句话**：环境搭建→提示词设计→API 调用→代码生成→集成测试的 MC Java 模组 AI 辅助开发完整工作流（与 v5 已收的"手机端 MC 模组 AI"是不同形态：那是自然语言出 Addon，这是真正的 Java 代码生成）
- **核心收获（文章总结，与已有决策原则一致处不重复立项）**：提示词必须含充足上下文；人工审查必不可少（需具备 MC 模组开发知识兜底）；AI 是副驾驶不是司机
- **可扩展方向**：数据包/命令（JSON+.mcfunction 纯文本，特别适合 AI 生成）、按运行时错误日志迭代修正
- **实用性 ★★★**：以后做 MC 生态内容（我们资料库里有 MC 类资产）可直接套用
- **来源**：hqwc.cn/news/1287112.html

### 6. verity 基岩版模组 + LLM API 接入教程（mhpn/kwkr 两篇同源教程）
- **一句话**：Minecraft 基岩版 verity 模组（脚本体系允许发 HTTP 请求）接大模型 API 做可对话 NPC 的完整实操：装模组→拿 API→填配置→验证对话
- **架构要点**：直连 vs 中转两种接入方式（个人测试直连、公开图要中转）；请求体就是标准 `messages[{system},{user}]` 结构，system 里写 NPC 身份设定；技能触发指令 vs 纯文本回复的分支处理
- **实用性 ★★★★**（对 Modding 场景）：零引擎改动的 AI NPC 最低成本路径；国产 OpenAI 兼容接口（DeepSeek 等）直接能填
- **来源**：mhpn.cn/news/1995217 + kwkr.cn/news/304176（同一教程的两个站点转载，取信息更全处核对）

### 7. StarCharM：GenAI 做游戏 Modding 的学术研究（arXiv 2507.13951，ACM PCHI 2025）
- **一句话**：蒙特利尔理工的 Stardew Valley GenAI NPC 创建工具 + 10 名玩家用研：玩家乐于让 AI 把角色想法变成真 mod，但抱怨"生成丰富内容填不满复杂构想"，并担忧原创性与社区参与感被稀释
- **价值**：「Democratizing Game Modding」方向目前最完整的一手用研证据，给"Mod 工具该给玩家多大控制粒度"提供了设计依据
- **实用性 ★★★**（研究参考）：2025-10 发表，略旧但方向正热
- **来源**：arxiv.org/pdf/2507.13951v1

## 二、GitHub 趋势（PullRepo 2026-09-20 日报 + 本周）

### 8. Eurekaleo/awesome-ai-for-games（205★，近月 79 commits）
- **一句话**：AI×游戏各阶段研究精选库（Growth Score 22.06）
- **价值**：与 v5 的 Ai-Game-DevTools（工具导航）互补——这个是**研究侧**索引，适合追论文
- **实用性 ★★★**：已加入 pipeline 参考源清单

### 9. solis-team/XRepoTest（170★）
- **一句话**：LLM 跨多语言单元测试生成 benchmark
- **价值**：与"AI 写标准模块可信"（决策原则 2）互为印证——单测生成是 AI 编程里证据最硬的场景之一
- **实用性 ★★★**（信号级）

## 三、AI 开发经验帖（含自测）

### 10. 码道：从一段 Python 流式代码到"成语接龙 AI 对话"完整项目（CSDN 165882932，09-18）——✅ 已读全文自测
- **一句话**：零依赖纯前端（HTML/CSS/JS 四文件）把 DeepSeek-V4-Flash 做成可玩的成语接龙小游戏，含 SSE 流式、结构化 JSON 渲染、国风 UI、localStorage 持久化、Puppeteer E2E
- **自测吸收的 5 条（全部对我有用，已进决策原则）**：
  1. **协议先行**：先定义消息格式（status ok/error/help 三分支 + 固定字段），再让模型"按协议讲话"，前端只做 `switch(status)`——"提示词规定 JSON，前端就拿到结构化数据；把协议边界摸清楚，Demo 才长成作品"
  2. **SSE 半字坑**：`TextDecoder("utf-8", {stream:true})` + buffer 留尾巴，UTF-8 汉字 3 字节被网络块切断必乱码
  3. **reasoning_content 与 content 分离**：思考型模型（DeepSeek-V4-Flash）delta 里两个字段同时出现，只取 `content`，否则前端 JSON 解析全崩（与本地记忆"推理模型 reasoning_tokens 吃额度"互为表里：一边吃 token 额度，一边污染输出流）
  4. **防御式解析三道兜底**：正则提最长花括号段 → JSON.parse → 换行替换重试
  5. **CORS 先探**：动手前 `curl -X OPTIONS` 预检，省掉整个 Node 中转层
- **另一条踩坑（通用）**：自定义 STORE 的 getter 返回副本数组，`history[idx-1] = x` 改的是副本不落盘——改完必须 set 回去
- **实用性 ★★★★★**：前端接大模型的"最小完整产品"范本，CCGS 桥接脚本（HTTP+JSON）直接适用
- **来源**：blog.csdn.net/2501_93886861/article/details/165882932

### 11. Harbour Masters《时之笛》PC 移植组承认多年用 AI，社区爆发"vibecoded slop"争议（realhacker.news，09-16 事件）——✅ 已读长文核实
- **一句话**：最知名的 N64 逆向移植组（Ship of Harkinian / libultraship）被 PC Gaming Wiki 发帖指"数千行代码是 AI 生成、甚至移除了 co-author 署名"，团队确认部分成员用 AI 多年但否认"slop"；核心澄清：**"用 AI 辅助开发的脚本做批量函数转换，转换后做 parity 测试"**——代码是人审的
- **沉淀的三条 Modding 社区规范（新，重要）**：
  1. **披露**：AI 辅助比例与用途应向社区说明，"隐藏"比"使用"激怒人多得多
  2. **parity 测试**：AI 批量转换的代码必须逐函数验证行为等价，"质量不像 slop"不能替代"被验证过"
  3. **署名**：AI 工具的 co-author/贡献标注不要移除
- **对我们**：amphoreus-roast 发行时（Steam/itch.io）AI 生成素材与代码的披露策略现在就该定，别等被问
- **实用性 ★★★★★**（规范级）
- **来源**：realhacker.news/team-behind-popular-ocarina-of-time-pc-port-admit-to-using-ai-for-years...（事件链：PC Gaming Wiki → ResetEra → Bluesky → 团队 Discord 公开回应）

### 12. AI 重构游戏开发：独立项目效率提升 90% 实战解析（hqwc a/225593）——⚠️ 摘录级（fetch 超时）
- **一句话**：Unity+Cursor 做基因进化类独立游戏：C# 类用"文件头注释写需求 + Cmd+K 生成框架"、基因影响系统自然语言驱动、Leonardo.Ai Alchemy 模式出 UI 图标、Midjourney Vary(Region)/SD Inpainting 统一美术基调
- **与已有原则对照**：大部分与 v8 决策原则（附图>写话、标准模块 AI 写）重合，增量点是 **Leonardo Alchemy 对 icon/flat/symbol 类需求更准**这个具体选型
- **实用性 ★★★**
- **来源**：hqwc.cn/a/225593.html

### 13. Show HN 两则（09-16 前后）
- **Pixel Agents**（mateovalle，HN 热帖）：像素风"任务控制中心"看 Claude Code 多 agent——把 agent 活动映射成 16-bit 战略游戏式视觉，"日志洪水里的救生艇"。实用性 ★★☆（好玩+有启发：agent 监控的可视化方向）
- **Loss.**（Show HN 小讽刺游戏）：玩家亲手点按钮做 token 预测，体验"从推理工人到监视监视机器的机器"的自动化讽刺。实用性 ★★（品类参考：极简叙事游戏）
- **来源**：clawdbytes.com/article/2026-09-16-show-hn-pixel-agents... + gipyeong-lee.github.io 09-16

## 四、AI 公司官方动态（09-02 ~ 09-19，剔除 v7/v8 已收）

### 14. 千问 09-19 三连：Qwen3.8-Omni-Flash 开源组件 + Qwen-Live Harness + Qwen3.8-LiveTranslate
- **Qwen-MM-Plugins（开源组件，本辑新）**：给 Claude Code / Gemini CLI / Qwen Code 等 agent 补**视频剪辑、说话人识别、PDF 视频笔记、可复用工作流**能力 → 可直接给我们的 agent 工作流加视频能力
- **Qwen-Live Harness**：调用摄像头/麦克风实时交互的 harness
- **Qwen3.8-LiveTranslate**：60 语言实时同传，Interleave 架构，LAAL 2.8s→2.3s，新增实时说话人分离 + 原文译文同帧 + 长上下文消歧
- **Omni-Flash 补充数据**（v7 已收模型，此处补商业数据）：$0.15/$0.47 每百万 token，音频输入 <$0.01/小时，720p 视频约 $0.20/秒（1fps）；对比 Gemini 3.8 Flash $0.75/$3.75 且 2027-01-01 涨价
- **实用性 ★★★★**：MM-Plugins 是可直接装的东西；同传对多语言发行（第 8 轮英文版）有参考
- **来源**：亿邦动力 m.ebrun.com/708650.html + 凤凰网科技 + juejin AI日报 09-19

### 15. Qwen3-TTS 官方仓库核实（QwenLM/Qwen3-TTS）——✅ GitHub 深读
- **一句话**：开源 TTS，0.6B / 1.7B 两档（12Hz 系列），10 语言（中/英/日/韩/德/法/俄/葡/西/意），9 个 Premium 音色（含北京话 Dylan、四川话 Eric），**3 秒快速克隆**，首包延迟 97ms（Dual-Track 混合流式架构），`pip install qwen-tts` + 一行 `qwen-tts-demo` 起 WebUI
- **工作流亮点**：VoiceDesign（自然语言设计声线）→ 克隆模型复用的"先设计后克隆"管线；`create_voice_clone_prompt` 可复用克隆提示避免重复计算
- **对本工作区**：**amphoreus-roast 第 5 轮（配音）首选本地方案**——0.6B 档 16GB 机器有机会跑（CPU 慢但批量合成可行）；「剧本」用低沉男声（Uncle_Fu 类）、「灰毛」用青年声，先各出 10 句试
- **⚠️ 注意**：官方仓库页面未见明确 LICENSE 声明（媒体镜像称 Apache 2.0）——**商用前必须查清许可证**，本作非商用暂不受阻
- **来源**：github.com/QwenLM/Qwen3-TTS（commit 历史：2026-01 初始、02 tokenizer 修复、03 微调 bug 修复）

### 16. Suno v6 家族 + Google Lyria 3.5（音乐生成双雄，09-10 / 09-05）
- **Suno v6**（09-10）：v6（精准打磨）/ v6-wild（实验向）/ v6-mini（快速，**Free 档可用**），与艺术家/制作人合作训练，理解人声/乐器/结构/情绪的音乐术语
- **Lyria 3.5**（09-05，Google）：AI Studio/Gemini API/Gemini app 可用，44.1kHz 立体声整首歌（主副歌），文本/图像提示，**自定义歌词 + 时间戳结构控制**，SynthID 水印
- **对本工作区**：第 2 轮当前是程序化占位音（本轮已合入），正式版的两条候选路：Suno v6-mini（免费档先试）或 Lyria 3.5（要 API key）；时间戳结构控制对"30s 循环 BGM"这种精确规格需求尤其合适
- **实用性 ★★★★**（第 2 轮升级候选）
- **来源**：headsupai.io/ai-news-and-updates/this-month（Suno 09-10 条 + Lyria 09-05 条）

### 17. NVIDIA PAIR（09-04，免费 beta）
- **一句话**：把局域网内的 RTX / DGX Spark / Mac 串成私有推理集群，自动把推理请求路由到有空闲算力的设备；支持 Ollama 与 LM Studio 后端（Win/Linux/macOS）
- **对本工作区**：以后家里/学校凑出第二台带卡机器时，本地 16GB 约束可以横向破——Ollama 后端直接兼容我们现有配置
- **实用性 ★★★**（待有第二台机器时验证）
- **来源**：headsupai.io（09-04 条）

### 18. Qwen3.8-Max-0902（09-02）
- **一句话**：2.4T 参数、1M token 上下文，Code Arena WebDev 榜首（1691 分），$2/$6 每百万 token（QwenCloud API）
- **价值**：国产旗舰编码档的价格锚点——比 v7 收录的 Qwen3-Max 定价（¥3/¥22 每百万 ≈ $0.42/$3.1）贵一截，选型时按任务分级
- **实用性 ★★★**（选型数据）
- **来源**：headsupai.io（09-02 条）

### 19. Anthropic 实验室进展度量提案（09-17）+ HF 开放对齐倡议（09-13）+ Anthropic×Accenture 嵌入式评估（09-19）
- **一句话**：三件事指向同一趋势——**第三方嵌入式独立评估变成前沿实验室的标配动作**：Anthropic 提出"lab 内度量"指标框架；HF（Thomas Wolf 牵头）发起 Open Alignment Initiative 并申请进入 Anthropic 嵌入式评估员计划（永久员工级访问）；Anthropic 与 Accenture（Faculty 团队）各投 ≥$10 亿做嵌入式模型评估/红队/护栏测试
- **对我们**：写调研报告时"厂商自测数据要标注"（v8 已有原则）升级为——"有第三方嵌入式评估的厂商声明，可信度上调一档"
- **实用性 ★★★**（方法论）
- **来源**：dwaynehelena.com 09-18 brief + headsupai.io（HF 09-13 条）+ 12pb AI Daily 09-19

### 20. 行业速报（三则一过）
- **NYT 诉 OpenAI/Microsoft 申请即决判决（09-19）**：92 页新诉状披露内部材料——微软 Brent Hecht 2023 备忘录称大模型吞噬劳动成果是"人类史上最大盗窃"；微软数据自认 Copilot 使 NYT 点击率较 Bing 最多降 93% → 版权风险与竞品数据自伤同时坐实
- **ZCode 逆向（开发者 devferstar）**：Z.ai 的 AI 编码桌面端登录后**静默打包整个工作区（含完整 .git 历史、LFS、reflogs、全局配置）加密上传阿里云 OSS**——单次快照 42,411 文件 / 313MB，.git 占 86.6% → **敏感代码库不要接入这类工具**（我们 CCGS 桥接走本地 Ollama 的决策再次被印证）
- **OpenRouter 20 个图像生成模型横评**：同一 prompt 计费 $0.006–$0.134/张（22 倍差）；Trail of Bits 用 agent 花 6 个月自建 MASM LSP/反编译器/静态分析/Lean 形式化证明，在 zkVM 审计中挖出高危漏洞 + 400+ 类型校验缺陷 + 95 个机器可验证证明
- **来源**：12pb.com/en/news/ai-daily-2026-09-19 + OpenRouter 公告 + Trail of Bits

## 五、本地语音工具（第 5 轮配音专项，v5 之后的新增）

### 21. sherpa-onnx Unity 集成全攻略（hqwc a/637389）
- **一句话**：Unity 里走 C++ API 编译 sherpa-onnx 动态库，实现**离线、流式、低延迟** TTS（打字按下合成键→几乎无延迟出音，全程本地）
- **价值**：端侧 ONNX Runtime 跑 VITS 系模型的完整工程路径（环境→编译→播放优化→踩坑）；Ren'Py 无此需求（VN 不需要实时），但以后做 3D 项目接 AI NPC 语音时是标准方案
- **实用性 ★★★**（3D 场景预案）
- **来源**：hqwc.cn/a/637389.html

### 22. ChatTTS-ui（hqwc a/1920455）
- **一句话**：ChatTTS 的本地 WebUI + HTTP API：Windows 预打包 `app.exe` 双击即用，首次下 ~2GB 模型后**完全离线**，浏览器 127.0.0.1:9966 直接出语音
- **对本工作区**：与 Qwen3-TTS 并列的第 5 轮候选——ChatTTS 强在中文口语感/语气词，Qwen3-TTS 强在音色可控+克隆；两边各出 5 句台词 A/B 再定
- **实用性 ★★★★**（16GB 机器可跑）
- **来源**：hqwc.cn/a/1920455.html

### 23. Willow Inference Server（promptquorum 评测，2026-09 更新）
- **一句话**：免费开源（Apache 2.0）自托管 ASR+TTS 服务器：Whisper 系识别 + 自定义音色合成，WebRTC/REST/WebSocket 三种接入，Docker Compose 部署（Win 走 WSL），GTX 1060 3GB 可跑、ASR+TTS 同开建议 6GB 显存
- **注意**：2026-02 已移除 LLM/聊天推理，只做语音——通用文本生成另配 Ollama
- **实用性 ★★★**（ASR 侧对我们暂无需求，TTS 侧作备选记录）
- **来源**：promptquorum.com/zh/power-local-llm/willow-inference-server-review

## 六、本期总结 & 实用性对比

### 最值得关注的新发现（第九辑）
1. **Harbour Masters 争议**（#11）——开源 Modding 用 AI 的三条社区规范（披露/parity/署名）第一次被完整暴露并讨论，做游戏的每个人迟早要面对
2. **my_ai_town**（#1）——Godot 4.7 + LLM 居民小镇，"世界日志/居民记忆分离"架构与我们的 persistent 层同构，第 4/6 轮的直接参考
3. **Qwen 09-19 三连 + Qwen3-TTS 核实**（#14/#15）——配音轮（第 5 轮）的技术选型基本落定：Qwen3-TTS 0.6B 主选，ChatTTS-ui 备 A/B
4. **Suno v6 / Lyria 3.5**（#16）——第 2 轮占位音的正式替换方案明确（v6-mini 免费档可先试）
5. **协议先行**（#10 码道）——"先定消息格式再让模型说话"，CCGS 桥接与一切 API 集成的通用原则

### AI Dev 帖子自测结论（本期）
- **码道·成语接龙**（#10）✅ **已读全文** → 已吸收 5 条（协议先行/SSE 半字/reasoning_content 分离/防御式解析/CORS 先探）+ 1 条通用坑（getter 副本不落盘）→ 进 pipeline 决策原则 21
- **Harbour Masters**（#11）✅ **已读长文** → 已吸收 3 条 Modding AI 规范 → 进 pipeline 决策原则 22；**行动项：amphoreus-roast 的 AI 披露策略写进 README**
- **Qwen3-TTS**（#15）✅ **官方仓库核实** → 第 5 轮主选方案确认；许可证待查
- **my_ai_town**（#1）✅ **仓库深读** → 架构参考（不抄代码，许可证未定）
- **CaLLMar / Unity 90% / verity / BO2 mod / 码道扩展** ⚠️ 摘录级或有重合，未单独立项
- **Suno v6 / Lyria 3.5 / PAIR** ⚠️ 无 API 通道/无第二台机器，列为候选未落地
- **ZCode 逆向** ✅ 核实 → 风险清单 +1（敏感库禁接）

### 整合 action items（已执行/排期）
- [x] 本文件（第九辑）+ v8 存档
- [x] amphoreus-roast 第 2 轮音频层：程序化占位音合入（本轮完成，见 ROADMAP）
- [x] pipeline 决策原则 21（协议先行）/ 22（Modding AI 三规范）
- [ ] 第 5 轮配音：Qwen3-TTS 0.6B 本机试跑（先查许可证）
- [ ] 第 2 轮正式版音频：Suno v6-mini 免费档试用
- [ ] amphoreus-roast README 补"AI 生成内容披露"段落
- [ ] JDK 21 + Android SDK → 安卓打包（v8 遗留，仍未动）

### 累计信源统计（更新）
- 第九辑：23 条（正文编号 1-23，其中 #13 含 2 则）→ 实际 24 个条目
- 累计：约 228 + 24 = **约 252 条**
- GitHub 项目索引：1054 项（本辑新增 4 个仓库级条目未并入 1054 主索引：my_ai_town / jev_vampire_survivors / awesome-ai-for-games / XRepoTest，下轮并入 index.html 时登记）
- 下一辑基线：约 252 条 + 1054 项 + 房规 21 条 + mistakes 4 条；待办：JDK21/安卓包、Qwen3-TTS 试跑、Suno v6-mini 试用
