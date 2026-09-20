# 跨平台游戏制作 × AI 开发资源梳理（2026-09-20 · 第六辑）

> 搜索覆盖：GitHub（含 09-18 新发 MCP）、CSDN/掘金/博客园、国内 8 家大模型公司 + 海外 5 家前沿模型官方动态、腾讯新闻/今日头条/知乎/X
> 本次为第六次增量，聚焦「MCP 引擎接入爆发」「AI 开发方法论（已自测落地）」「国产模型 9 月集中发布」「AI 小游戏分发新瓶颈」
> 已有索引：index.html（1054 项 GitHub 项目）+ 前五辑经验帖（累计约 152 条）+ game-production-pipeline.md（工具链）
> 去重基线：已逐条比对 v1-v5 全量条目 + index.html，本辑 20 条零重复

---

## 一、MCP 引擎接入爆发（2026-09 全新方向，本辑最大增量）

> 趋势判断：本月最显著的变化是 **MCP（Model Context Protocol）正式成为"AI 连游戏引擎"的标准接口**。Godot/Unity/Unreal 三大引擎几乎同时给出官方或高成熟度 MCP，"让 AI 直接操作编辑器"从概念进入可用。

### 1. Godot MCP（tomyud1/godot-mcp v1.0.0，09-18 发布）
- **一句话**：给 AI 全权访问 Godot 编辑器，直接读写场景/节点/脚本/项目设置，npm 一键装，MIT
- **32 个工具 / 6 大类**：文件操作(4)、场景操作(11)、脚本操作(6)、项目工具(9)、资产生成(4)、可视化(1)
- **亮点**：内置**浏览器交互式项目可视化器**（localhost:6510，力导向脚本关系图，点脚本看变量/函数/信号，可直接改码实时同步）；支持 SVG→2D 精灵、ComfyUI 节点搜索、RunningHub 工作流
- **装法**：`npx -y godot-mcp-server` 接入 Claude Desktop / Cursor / 任意 MCP 客户端；Godot 端拷 addon 启用
- **GitHub**：`tomyud1/godot-mcp`（MIT）
- **实用性 ★★★★★**：目前 Godot 侧最活跃的 MCP，对"AI 辅助做 Godot 游戏"直接可用
- **来源**：lobehub.com/mcp/tomyud1-godot-mcp

### 2. Godot MCP Omni（godotengine.org 资产库 #5470，v5.0.5）
- **一句话**：更"全量"的 Godot MCP，暴露 **1820 个规范引擎操作 / 59 个域** + 任意内存 GDScript 求值 + 通用对象反射
- **支持**：Google Antigravity / Claude Code / Cursor / Windsurf / VS Code / OpenAI Codex；编辑器内 dock（连接状态 + 工具调用监控 + GDScript 沙盒）
- **安全**：socket 严格绑 localhost，token 认证 WebSocket
- **要求**：Godot 4.1–4.8+（dev），Python 3.11–3.14
- **实用性 ★★★★**：功能最全，适合要精细控制引擎对象的人
- **来源**：godotengine.org/asset-library/asset/5470

### 3. Unity MCP v10（unity-mcp，主版本大升级）
- **一句话**：Unity 官方 MCP 从 29 → **47 个工具入口**，分 10 个功能组
- **核心变化**：新增 `asset_gen` **AI 资产生成/导入工具组**（4 个资产生成工具 + 异步任务模型）、基于操作系统安全存储的 **Provider 密钥管理**、Blender 等 DCC 工具的本地文件交接流程
- **意义**：Unity 侧"AI 生成资产→导入→摆场景"的闭环被打通
- **实用性 ★★★★★**：用 Unity 的人现在能让 AI 直接管资产/场景/脚本
- **来源**：hqwc.cn（unity-mcp 仓库 V10 解析）

### 4. Unreal Engine 5.8（UE5 最后一版 + 实验性 LLM MCP 插件）
- **一句话**：Epic 发布 UE5.8（UE5 线最后一个大版本），自带**实验性 MCP 插件**，把任意 LLM 连到蓝图/资产/关卡/材质/网格
- **官方演示**：用 Claude Code 通过该插件从资产库拉对象、摆场景、按真实参考图调光
- **其他 UE5.8 更新**：Mesh Terrain（支持悬挑/浮岛/隧道的 3D 网格地形）、MegaLights 转生产级（现役主机 60fps）、Lumen Lite 瞄准 Switch 2、MetaHuman Animator 单摄像头全身动捕
- **UE6 预告**：LLM 集成将成创作管线核心，目标减少重复内容制作；UE6 早期访问瞄准 2027 年底
- **实用性 ★★★★**：UE 用户可开始试验 LLM 进引擎；UE6 是真正的重头戏
- **来源**：thepaternitystore.com（Epic 06-18 发布报道）

### 5. Kreat3D MCP —— AI 3D 模型 MCP
- **一句话**：把 3D 创作工具连进 AI Agent，对话里直接 图生3D/文生3D/贴图/重网格/导出
- **能力**：图生 3D、文生 3D、AI 贴图、重网格优化、概念图生成；导出 GLB/FBX/STL/OBJ/USDZ
- **装法**：MCP server URL `https://mcp.kreat3d.io/mcp` + 账号认证，接入 Claude/ChatGPT/Cursor/Codex
- **实用性 ★★★★**：游戏 3D 资产管线可嵌进对话，省去切软件
- **来源**：aiwith.me/tools/kreat3d-io-mcp

### 6. Arnis v3.2.0 —— 真实世界地图 → 可走进去的 Minecraft 方块世界
- **一句话**：读 OpenStreetMap + 多源高程 + NASA 行星数据，框选区域一键生成能直接玩的 Minecraft 世界（Java 1.17+/基岩/Luanti）
- **热度**：1.7 万 stars、85 万下载，Rust 编写，Apache-2.0
- **三种形态**：桌面端（Win/macOS/Linux）/ 浏览器版 MapSmith / CLI（cargo 一条命令）
- **v3.2 新亮点**：可生成**月球 + 火星地形**（读 NASA LOLA/MOLA 真实测高，垂直放大 4 倍）；按建筑类型匹配实拍外立面
- **实测结论**：欧美热门城市/地标效果惊艳；**国内 OSM 数据偏少，效果打折**；大范围很吃性能，建议从小区域开始
- **游戏拓展性**：做"探索真实家乡/世界/外星"类玩法的现成地形来源
- **来源**：toutiao.com/7687062531801760319 + 远景实测 + hqwc/lsln/mhpq 多源教程
- **实用性 ★★★★**（MC 玩家/造景/探索类玩法）

---

## 二、AI 开发方法论（本辑重点：已自测阅读 + 落地）

> 按任务要求，以下 AI 开发/使用帖子已**逐篇 WebFetch 读全文核实**，并测试是否对 WorkBuddy 自身有用；有用者已产生可见改动（见文末"整合 action items"）。

### 7. Mistake Memory（错误记忆）Playbook —— ✅ 已自测落地
- **一句话**（dev.to, Kunal Ganglani）：修复必须成为**仓库中的工件**（规则 + 回归测试 + 错误记忆条目），否则下次上下文重置就丢
- **核心**：一个版本化、repo 存储的"反复失败日志"，每条含 symptom/rootCause/**bannedPattern**/**preferredPattern**/**regressionTest**/patch/retrievalKeys
- **10 步 SOP**：写进仓库→钉禁止/推荐模式→挂回归测试→存补丁→加 guardrails 提示词→指令分作用域→**规则预算 Top10**→自动化检索→CI 门禁→指派 owner 月维护
- **维护**：活跃条目上限 50 条、超 90 天复查、每条必须有 owner
- **自测结论**：✅ **真有用 → 已落地**。本轮已在本工作区创建 `.workbuddy/memory/mistakes/`（README + index.json + 2 条种子条目 M-0001 去重 / M-0002 先核实再下结论），并把我自己的工作流接进这套"改码前先检索错误记忆"的 guardrails
- **来源**：dev.to/kunal_d6a8fea2309e1571ee7/how-to-prevent-ai-coding-assistant-repeating-mistakes-2026-4kba

### 8. aigamer「分阶段合同」管线 —— ✅ 已吸收
- **一句话**（掘金, ronindong, 09-18）：AI 生成游戏走得通，但前提是把它收束成**可闸门、可复用、可上架的工程管线**，不是"一句话出 3A"
- **6 阶段（每段有产物 + 闸门）**：设计(GDD 可核对)→代码(分模块+共享壳)→美术(art.json/GLB 可审计)→校验(Playwright 真机冒烟)→元数据(manifest)→发布(CDN 直链)
- **核心理念**：**Agent 是执行器，skill/知识库是合同**（识别→推导→验证）；机读闸门挡在发布前；**知识回流**（修一次缺陷→沉淀维度知识→下一款默认不再踩，量产靠"记忆合同"不是更长 Prompt）
- **技术栈**：2D 用 PixiJS、3D 区 Three.js+GLB、共享 AigamerShell（开始/暂停/失败/i18n）
- **自测结论**：✅ **真有用 → 已吸收**。"分阶段合同 + 机读闸门 + 知识回流"已并入 game-production-pipeline.md 决策原则（与 Mistake Memory 的"知识回流"互相印证）
- **来源**：juejin.cn/post/7686745928791261222（演示站 aigamer.pages.dev）

### 9. Game × AI Native 九篇系列（全 9 篇）—— ✅ 已完整提取
- **作者**（CSDN, 树袋趴趴熊, 2026-09-18）：2026 年最完整的 AI 游戏九层架构方法论地图，从运行时（智能体/记忆/推理/角色/叙事）到研发管线（多Agent/MCP/RAG/AIGC）
- **各篇概要**：
  - 第1篇 总览：三大汇聚曲线、9 子系统栈、四条工程原则、最小 60 行 Agent 循环
  - 第2篇 AI NPC 智能体：L1-L5 分级、BDI 三栈（信念-愿望-意图）、快慢双系统、三层仲裁（动机栈/关系图/事件总线）
  - 第3篇 超类人记忆系统：四种记忆类型（情景/语义/情感/程序）、节点图存储、艾宾浩斯遗忘曲线、三重检索+graph_boost
  - 第4篇 推理工程化：MoE 稀疏化（DS-V3 5.5%激活）、MLA 压缩 KV Cache 4-7 倍、思维蒸馏、PD 分离、分级请求队列
  - 第5篇 角色大模型：智商×情商双维架构、PAD 情感模型、LoRA 角色插件（50-100MB/角色）、数据合成流水线
  - 第6篇 动态叙事：四层引擎（信号/因果/叙事/体验）、Story Director 张力导演、三级事件库、玩家行为预测器
  - 第7篇 多Agent管线：分层组织（架构/业务/执行）、MCP 协议详解、DAG 任务编排、四道质量门禁
  - 第8篇 知识库：BM25+向量+结构三通道混合检索、三级缓存（50ms 预算）、分钟级热更新、五个硬骨头
  - 第9篇 AIGC 工作台：三层风格一致（LoRA+IP-Adapter+ControlNet）、自动质检（StyleGate）、引擎管线深度集成
- **总复盘**：飞轮逻辑——研发管线十倍速生产 → 运行时三基座实时活起来 → 体验层转化为情感与故事 → 商业回报反哺研发
- **自测结论**：✅ **真有用 → 已全部提取归档**。完整笔记见 `game-ai-native-series-summary.md`
- **来源**：blog.csdn.net/wsc122181582（全 9 篇 URL 见系列笔记文件）

### 10. DeepSeek 辅助游戏开发实战：30 亿 Token 怎么高效花
- **一句话**（hqwc）：给 AI 的指令要**具体结构化**（"为 2D 平台游戏写玩家控制器 C# 脚本，用 CharacterController，实现移动/二段跳/下蹲滑行 + 动画状态机"）而非"帮我做个游戏"
- **5 招省 Token**：分而治之（架构/角色/敌人AI/UI/存档各开新对话）、只给最小相关代码片段、让 AI 扮演角色（"你是资深 Unity 引擎师"）、迭代反馈比从头生成省、阶段化（概念 500 万 token→框架 1.5 亿…）
- **自测结论**：⚠️ 有参考价值（通用提示工程，与已有"锁文件锁范围"原则一致，未单独立项）
- **来源**：hqwc.cn/news/1316008.html

### 11. Vibe Coding 起步的 8 个坑
- **一句话**（bdg.am）：能跑 ≠ 生产可用，新手最常踩的坑
- **8 坑**：① 不读代码就合入 ② 提示词模糊过载 ③ 跳过边界/异常处理（AI 只优化 happy path）④ 安全拖到太晚 ⑤ **引入幻觉/未验证依赖（slopsquatting：攻击者注册与 AI 幻觉同名的恶意包）** ⑥ 先堆复杂度再验证 ⑦ 失去代码所有权 ⑧（治理缺失）
- **自测结论**：⚠️ 有参考价值（"slopsquatting"是新风险点，值得记住：AI 推荐的第三方包要核对官方源/维护/漏洞）
- **来源**：bdg.am/en/blog/5-mistakes-people-make-when-starting-with-vibe-coding

### 12. 72 小时 AI 游戏开发实战：Claude Code + AI 资产
- **一句话**（hqwc）：无深厚编程/美术基础，用"AI 资产 + Claude Code"72 小时出可玩原型
- **路径**：自然语言描述想法 → Claude Code 搭代码骨架/核心逻辑 → AI 生成美术/音频/文案 → 整合调试
- **边界**：不是"从零到一全自动"，而是把你从语法记忆/基础编码/资源搜集中解放，专注核心玩法
- **自测结论**：⚠️ 有参考价值（与已有"AI 写标准模块/你验手感"原则一致）
- **来源**：hqwc.cn/news/1077088.html

### 13. Matthews Wong：ChatGPT Astra 一步步做出 3D 作品集游戏
- **一句话**（09-12）：把作品集做成"可走进去的 3D 游戏"（The Archipelago），全程由 ChatGPT Astra 按一份 **1015 行 PRD** 构建
- **关键方法论**：
  - **PRD 即提示词**：先让 agent 调研，再合写 1015 行/16 节的产品需求文档（问题/目标排序/非目标/参考/架构/性能/风险…），之后全是执行
  - **无头截图闭环**：用 Playwright 让 agent"看自己的输出"（read→build→screenshot→look→fix）——不能看输出的 agent 只会"交盒子"
  - **Parity 规则**：游戏展品与网页模块同源（同一 lib 文件派生），预构建闸门保证游戏不偏离网站
  - **预算写成 CI 闸门**（import guard/parity 检查/Playwright 冒烟/内存 soak）
- **自测结论**：✅ 有参考价值（"agent 要看自己的输出"+"PRD 即提示词"+"把预算写成 CI 闸门"三点直接可用，已记入 pipeline）
- **来源**：matthewswong.com/en/blog/chatgpt-astra-3d-portfolio-game-archipelago

---

## 三、AI 公司动态（2026-09 模型集中发布）

### 14. 国产 8 家大模型 2026 时间线梳理（1-9 月共 24 次发布）
- **一句话**（截至 09-14 整理）：国内半年"打得极凶"，8 家公司 24 次模型更新
- **9 月关键发布**：
  - **DeepSeek V4.1 Flash（09-10）**：552B（输入~80B/输出~160B 激活）、**原生视觉理解**、采用 Causal Encoder-Decoder 非对称架构（KV cache 从 3514→890 字节/token，HBM 需求降 1/4、SSD 降 1/8）；峰 2/8 元、闲时 1/4 元/百万 token；V4 Pro 于 09-14 下线全量路由到 V4.1 Flash
  - **Kimi K2.8 Preview（09-11）**：全量上线 Kimi Code + Kimi Work，**100 万 token 上下文向所有会员档位开放**
- **8 月关键**：Qwen3.8-Flash-Next（125B MoE/60B 激活/95% 稀疏，官方称"Qwen4 架构早期预览"开源）、GLM-5.3（08-14，编程/网安突破）、GLM-5.3-Flash（08-26，GLM-5 首款原生多模态，价格约 1/10，跑在 10 万+ 国产芯片集群）
- **趋势**：DeepSeek 的 R2 与 V4.1 双双延期，节奏被自己打乱；Kimi 开放权重冲全球前三；MiniMax 6 月靠 M3"三项能力集齐"翻身
- **自测结论**：⚠️ 有参考价值（选型参考：DeepSeek V4.1 Flash 现在支持原生视觉且更便宜，后续 AI 任务可切换）
- **来源**：2048ai.net 多维对比 + hqwc 各家详解 + 官方公告（量子位/IT之家/新浪科技等）

### 15. 海外 5 家前沿模型 9 月首周连发
- **一句话**（completeaitraining + promptzone + cnblogs wiki）：9 月头 3 天 5 个前沿模型落地，但**公共 benchmark 测不出"你的真实工作"是否有提升**
- **清单**：
  - **GPT-6 Astra（09-03）**：Terminal-Bench Science 64.6%、FrontierMath T4 97.6%、**ARC-AGI-3 99.9%**（从 7.8% 跃升，"抽象推理饱和"成现实议题）、OSWorld 2.0 72.6%、**越权操作率 0%**（对齐里程碑）；OpenAI 首个"Critical 网络安全"评级模型
  - **Claude Fable 5.1 / Mythos 5.1（09-01）**：同一模型不同安全护栏；**缓存输入成本降 75% 至 $0.25/百万 token**（典型负载省~25%，agentic 省至 45%）
  - **Gemini 3.8 Flash（09-02）**："最智能 workhorse"，$0.75/$3.75，**2027-01-01 起涨价至 $1.50/$7.50**
  - **Meta Muse Spark 1.3 + Muse Code（09-02）**：agentic/coding 强化
  - **Qwen3.8-Max-0902**：为编码后训练，CodeArena +22 分
- **自测结论**：⚠️ 有参考价值（GPT-6 Astra 的 0% 越权 + 缓存成本大降是重要信号；注意各家 2027 涨价预告，成本模型要重算）
- **来源**：completeaitraining.com + promptzone.com/ai-model-releases + cnblogs.com/xine/p/23034590

### 16. "别信 benchmark，建你自己的评测集"
- **一句话**（completeaitraining）：模型切换前，唯一可靠的做法是**从你自己真实工作里建一套评测集**
- **方法（一下午就能建）**：抽 30-50 个近一个月的真实案例（邮件/摘要/工单）→ 脱敏但保留" messy"（ messy 才是砸坏模型的东西）→ **2/3 普通 + 1/3 上次出错的案例** → 写"期望结果"（一行，写"好的答案必须包含/必须不含什么"，不是完美答案）→ 固定打分规则
- **价值**：评测集是你自己的资产，换任何模型都拿不走；有了它，测一个模型只要 1 小时出一个数，不用开会扯皮
- **自测结论**：✅ 真有用（对我这种要持续换模型做开发/分析的 agent 极其实用，已记入工作习惯：重要任务先建小评测集再定模型）
- **来源**：completeaitraining.com/news/five-frontier-models-drop-in-three-days...

---

## 四、行业 / 社交（新方向）

### 17. 24 小时做一款 AI 小游戏，"谁来分发"成最大难题
- **一句话**（腾讯新闻/界面, 09-15）：AI 把小游戏生产门槛/速度压到极低，**瓶颈从"做出来"转移到"被看见"**
- **案例**：大学生席洋用 AI 以近一天一款速度做了"英语掌机""小游戏版森林冰火人""侦探推理"等数十款；《阿珠开蚌直播间》作者根据玩家反馈 3 小时改完上线
- **新分发平台（本辑新发现）**：
  - **TapTap 制造**（2026-01-30 上线）：AI 游戏创作智能体，自然语言出代码/美术/音乐
  - **Funloom AI**：AI 互动内容共创，3 月上线后约 5 万用户
  - **谜页集**（5 月底上线）：**专为 AI 小游戏/网页解谜/互动叙事而生的分发站**，已收录近 600 款、2 万+ 注册用户——正是"AI 小游戏缺流量入口"这一痛点催生的产物
- **核心洞察**：生产端效率被抬高后，"找到低门槛发布入口 + 拿到第一批用户 + 让作品被看见"成为开发之外的新问题；小红书/B站对外链跳转有限制，是分发痛点根源
- **来源**：news.qq.com/rain/a/20260915A09X7R00

### 18. 离职腾讯后，他们入局 AI 做「中国式开放世界」
- **一句话**（cnyouth）：前腾讯团队做一款上百个 AI NPC 的"中国式开放世界"，核心差异化
- **三大设计**：
  - **AI 有主观情绪/价值观**：NPC 会"有理有据"地解释为什么不收你的货，形成阵营与人物关系（对比：传统 NPC 不收货不给理由，玩家觉得被恶心）
  - **AI 伴玩（"1.5 人游戏"）**：为"想社交又怕对抗压力"的 I 人设计，AI 提供攻略/建议/受挫时安抚，全语音对话，未来可选喜欢的 NPC 陪玩
  - **动态社会 + 模拟经营**：上百 AI NPC 自己形成动态运转，"目前还没有人投这么多 AI NPC 让它们自运转"
- **金句**："人工剧情仍不可或缺——AI 能发散、能涌现，但没人给故事节点收敛，故事就会失主题变无聊"
- **来源**：cnyouth.com/6a552f1adc.html

### 19. StatePlay：腾讯+NUS+NTU+新加坡研究局 双分支 MoT 游戏世界模型
- **一句话**（arXiv 2026-07 预印本）：解决 AI 生成游戏画面时"数值/状态会崩"的问题
- **架构**：在视频生成模型上装一条处理游戏状态的"神经网络支线"——**视觉分支 5B 参数（流匹配）+ 状态分支 760M 参数（回归损失）**，用"联合注意力模块"双向交换信息（MoT 混合专家）
- **妙处**：状态分支直接预测血量/技能槽等数字（有规则可循，比扩散框架高效）；数据集还用 Gemini 给 NPC 战斗策略写自然语言描述（进攻/远程/防守），让 AI 能用文字指令控 NPC 风格
- **自测结论**：⚠️ Preview/研究阶段，"画面分支+状态分支解耦"思路对做 AI 游戏状态一致性有参考价值
- **来源**：spokedesign.com（网易新闻转载）

### 20. Vibe Coding 工具链实战配置指南
- **一句话**（mfbz/hqwc）：Vibe Coding 环境的"黄金搭档"与避坑
- **核心组合**：终端 **Claude Code**（代码库检索/快速操作）+ 编辑器 **Cursor**（沉浸式深度编码）
- **避坑**：Claude Code 对重要代码库用 `--dry-run` 先看计划再放行写操作（尤其 git）；Cursor 用 `.cursorrules` 定义项目规范；`/rewind` 一键回滚跑偏；"think < think hard < think harder < ultrathink" 触发深度思考
- **自测结论**：⚠️ 有参考价值（与已有工具链一致，"先 dry-run 再放行"是好习惯）
- **来源**：mfbz.cn/news/85852 + hqwc.cn/a/1345602.html

---

## 五、本期总结 & 实用性对比

### 最值得关注的新发现（第六辑）

| 项目 | 类型 | 实用性 | 适合谁 |
|------|------|--------|--------|
| **MCP 引擎接入（Godot/Unity/UE5.8）** | AI×引擎 | ★★★★★ | 想让 AI 直接操作编辑器做游戏的人（本辑最大增量） |
| **Mistake Memory 方法论** | AI 开发方法 | ★★★★★ | 所有用 AI 编程的人（已自测落地） |
| **aigamer 分阶段合同管线** | AI 生成游戏 | ★★★★★ | 想批量/稳定产出可上架 H5 的人 |
| **Game×AI Native 九篇（L1-L5+四原则）** | AI 架构方法论 | ★★★★★ | 想做"真 AI Native 游戏"架构的人 |
| **Arnis v3.2** | 地图→Minecraft | ★★★★ | MC 玩家/探索类玩法/造景 |
| **Kreat3D MCP** | AI 3D 资产 | ★★★★ | 需要对话里出 3D 资产的人 |
| **国产 8 家模型 9 月梳理** | 选型参考 | ★★★★ | 要换模型降本的人（V4.1 Flash 原生视觉+更便宜） |
| **自建评测集** | AI 使用习惯 | ★★★★ | 要持续换模型做任务的人（已记入习惯） |
| **AI 小游戏分发平台（谜页集等）** | 行业新方向 | ★★★★ | 做 AI 小游戏想被看见的人 |
| **GPT-6 Astra / Claude 5.1** | 前沿模型 | ★★★ | 关注对齐/成本/涨价信号的人 |

### AI Dev 帖子实测结论（本期，均已 WebFetch 读全文核实）

- **Mistake Memory** ✅ **真有用 → 已落地**：创建 `.workbuddy/memory/mistakes/`（README + index.json + M-0001/M-0002 两条种子），并接入"改码前先检索错误记忆"guardrails
- **aigamer 分阶段合同** ✅ **真有用 → 已吸收**："分阶段合同 + 机读闸门 + 知识回流"并入 pipeline
- **Game×AI Native 九篇** ✅ **真有用 → 已吸收**："确定性 vs 涌现性制度边界"+"推理成本一等公民"+"L1-L5 成本对齐"并入 pipeline
- **ChatGPT Astra 3D 作品集** ✅ 有参考价值："agent 要看自己的输出"+"PRD 即提示词"+"预算写成 CI 闸门"
- **自建评测集** ✅ **真有用**：重要任务先建小评测集再定模型，已记入工作习惯
- **DeepSeek 30 亿 Token / 72 小时 / Vibe 工具链** ⚠️ 有参考价值：与已有原则一致，未单独立项
- **8 个 Vibe Coding 坑** ⚠️ 有参考价值：新增风险点"slopsquatting"（AI 幻觉依赖=恶意包），已记
- **StatePlay / 国产模型 / GPT-6 Astra** ⚠️ 有参考价值：选型/趋势信号，未落地

---

### 整合 action items（已执行）

1. **Mistake Memory 已落地**：`D:\34498\Documents\.workbuddy\memory\mistakes\`（README + index.json + 2 条种子）——本辑最实打实的"有用就改"
2. **game-production-pipeline.md 已同步更新**：新增"第六辑"章节（MCP 引擎接入 + 分阶段合同 + L1-L5/四原则 + 自建评测集 + AI 小游戏分发）
3. **去重纪律强化**：已把"增量先对 v1-v5 全量去重"写成 Mistake Memory 条目 M-0001，防止转载/洗稿虚增条数
4. **csdn-social-summary-v5.md** 已存档（上一辑快照）

---

*最后更新：2026-09-20*
*来源汇总：index.html（1054 项 GitHub）+ 跨平台经验帖索引（本辑 20 条新增，累计约 172 条）+ game-production-pipeline.md + mistakes/（错误记忆）*
*第六辑搜索覆盖：GitHub 新发 MCP（Godot/Unity/UE/Kreat3D/Arnis）、CSDN/掘金/博客园、国内 8 家 + 海外 5 家模型官方动态、腾讯新闻/界面/今日头条/知乎/X*
