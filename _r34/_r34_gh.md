# R34 GitHub 路线调研 — Live2D 制作工具链 + AI 开发工具

> 基准用户画像：16GB RAM / Windows 11 + 本地 Ollama + 维护一个索引站的个人，非专业美术，目标是"低成本做 Live2D 模型/桌宠"。
> 收录口径：`owner/repo` + 一句话中文说明 + star + license + 语言 + 最近推送日 + 链接；star/license 均用 `gh api` 实取，不凭印象。
> 可复用性三档：`✅ 落地`（本机可跑）/ `⚠️ 参考`（架构或选型参考）/ `❌ 不采用`。

## 一、Live2D 制作工具链（绑定 / rigging / 分层 / 网格 / 参数 / 物理）

> 本节收录 PSD→模型自动绑定、rigging、分层、网格、参数、物理相关的**新**开源项目，已排除索引中已有的 Inochi2D / Ayagami / nijigenerate / psd2live / see-through 等。

### 1. `MangoLion/stretchystudio` — 504★ · JavaScript · MIT · push 2026-04-28
把静态插画转成**网格可变形角色**的 FOSS 2D 动画工具，直接对标 Live2D 的核心"网格/变形器"能力，纯浏览器端。
**⚠️ 参考**：思路（插画→网格→bone 变形）最适合本机低成本复刻；但已近半年无推送（`updated_at` 2026-10-10 只是挂资产，`pushed_at` 停在 04-28），不是活跃项目，不宜直接依赖。
<https://github.com/MangoLion/stretchystudio>

### 2. `Delsin-Yu/GD-PSD-Layer-Import-Plugin` — 10★ · GDScript · MIT · push 2026-03-25
Godot 4.4+ 的 PSD 图层导入插件（纯 GDScript），把分层 PSD 直接读进 Godot——做"Godot 桌宠 / 2D 骨骼绑定"的前置素材管线工具。
**⚠️ 参考**：功能对口、安装简单；但 ⚠️ **疑似假活**（`pushed_at` 2026-03-25 vs `updated_at` 2026-09-22，相差约 6 个月），只是改 README/挂资产，实为停更。
<https://github.com/Delsin-Yu/GD-PSD-Layer-Import-Plugin>

### 3. `coeyes/ComfyUI-PSD-Layers` — 4★ · JavaScript · MIT · push 2026-09-10
ComfyUI 节点：把 Seedream 分层分割结果保存成可编辑 PSD、可逐层读取并还原 Photoshop 混合模式——补上"AI 分层 → Live2D 可用素材"的最后一公里。
**✅ 落地**：ComfyUI 环境即插即用，配合本机 Ollama/图生图链路可跑通"单图→分层 PSD"闭环。
<https://github.com/coeyes/ComfyUI-PSD-Layers>

## 二、moc3 解析与渲染器（Rust / JS / C# / Python）

> 本节收录 moc3 格式解析、渲染、反编译、转换相关的库与工具。

### 4. `Eatgrapes/Mocari` — 47★ · Rust · MIT · push 2026-07-13
纯 Rust 的 Live2D/Cubism 运行时实验，自己解析 moc3——Rust 生态里最接近"绕开官方 Cubism SDK 自建运行时"的实现。
**⚠️ 参考**：本项目 Rust 侧唯一有实质代码量的 moc3 运行时，适合研究 moc3 二进制结构；但是实验性质、非成品，且 ⚠️ `updated_at`(2026-10) 比 `pushed_at`(2026-07) 新 3 个月，热度存在虚高。
<https://github.com/Eatgrapes/Mocari>

### 5. `UlyssesWu/D2Evil` — 139★ · C# · NOASSERTION · push 2026-06-07
托管端（.NET/C#）的 waifu 模型解析库，可读 moc3/psd 等格式——C#/Unity 侧做模型解析、格式转换的参考实现。
**⚠️ 参考**：star 最高、格式覆盖最全；但许可证为 **NOASSERTION（自定义，需自查）**，且已约 4 个月无推送。
<https://github.com/UlyssesWu/D2Evil>

### 6. `YuanNeoMax/YuanLive2D-Minecraft-Forge-Mod` — 0★ · push 2026-08-29
Minecraft Forge 1.20.1 的 Live2D 伴生模组，自带 Cubism runtime 在游戏内渲染模型。
**❌ 不采用**：场景过窄（仅限 MC 模组）、0 star、无许可证信息，对"桌面桌宠/Live2D 模型制作"目标无直接价值。
<https://github.com/YuanNeoMax/YuanLive2D-Minecraft-Forge-Mod>

## 三、不依赖 Cubism Editor 的替代栈

> 本节收录绕开 Live2D Cubism Editor 的整套替代生产/消费链路（对标 Inochi2D / Ayagami / nijigenerate，但均为**新**项目）。

### 7. `rig-c/core` — 12★ · TypeScript · NOASSERTION · push 2026-10-11
"**AI 编写 2D rigging**"：把 rig spec 编译成 **Spine 4.3** skeleton 格式，先用命名断言 + spine-core round-trip 校验、只输出通过校验的结果，并以 **agent skill** 形式分发。2026-08 新建，几乎每日推送。
**✅ 落地 + ⚠️ 参考**：本轮**最值得看**的新项目——它把"AI 自动绑定"做成可验证流水线、且完全绕开 Cubism；缺点是许可证 NOASSERTION，商用需确认。
<https://github.com/rig-c/core>

### 8. `rig-c/parts` — 2★ · TypeScript · MIT · push 2026-10-11
rig-c 的配套件：把一张画（经 see-through 类分层）组装成 rig-ready 的 PNG 图层 + 带权重网格 rig spec，交给 `rig-c/core` 编译校验。
**⚠️ 参考**：必须与 `rig-c/core` 成套使用才有价值，单用意义有限。
<https://github.com/rig-c/parts>

### 9. `broening/idle-web-animation` — 0★ · JavaScript · MIT · push 2026-09-15
"分层图片 + 一个 JSON，不需要引擎、不需要编辑器授权"的 2D 角色待机动画——极轻量的 Live2D 思路替代。
**⚠️ 参考**：体量很小（0 star，5297 KB），但"零引擎/零编辑器"理念正好契合个人低成本桌宠，适合当自研参考。
<https://github.com/broening/idle-web-animation>

## 四、Live2D 运行时（Web / Unity / Godot / Python / 原生窗口）

> 本节收录各平台运行时与查看器，含绕开 PixiJS 的自建渲染实现。

### 10. `o0Nomar0o/Motiv2D` — 45★ · JavaScript · MIT · push 2026-06-26
同时支持 **Spine2d 与 Live2D** 的查看器，纯 JS 实现（不依赖官方 SDK 播放层）。
**⚠️ 参考**：双格式查看器的组织方式值得借鉴，可用于自建索引站的模型预览；但约 3 个月无推送。
<https://github.com/o0Nomar0o/Motiv2D>

### 11. `Hawkbat/VTubeStudioJS` — 68★ · TypeScript · MIT · push 2026-08-22
VTube Studio API 的 Node / 浏览器 JS 实现——用代码驱动 Live2D 模型的表情/动作/参数（发弹幕→换表情就靠它）。
**✅ 落地**：想做"LLM 状态 → Live2D 表情/动作"的桥，这是最省事的 JS 侧通道，MIT 可直接用。
<https://github.com/Hawkbat/VTubeStudioJS>

### 12. `FomTarro/VTS-Sharp` — 50★ · C# · MIT · push 2026-08-18
VTube Studio API 的 C# 客户端库——.NET/Unity 侧对接 Live2D 演出的桥梁。
**⚠️ 参考**：与 VTubeStudioJS 对应，若走 C#/Unity 桌面路线再选它；本项目以 Web/JS 为主时可略过。
<https://github.com/FomTarro/VTS-Sharp>

### 13. `fly3366/YuraYura` — 3★ · Objective-C++ · NOASSERTION · push 2026-07-26
macOS 桌宠，**完全自建 Metal 运行时**，带自动部件提取、声明式主题、音乐驱动跳舞。
**❌ 不采用**：仅 macOS + 自研渲染器，与本机 Windows 11 画像不符；但"自建 GPU 运行时"的架构思路可作 ⚠️ 参考。
<https://github.com/fly3366/YuraYura>

## 五、桌面宠物 / AI 伴侣「身体」侧

> 本节收录把 Live2D/VTuber 模型接到 LLM agent 的桥、状态→表情映射、三层透明窗、托盘常驻；只读本地不联网的优先。

### 14. `Project-N-E-K-O/N.E.K.O` — 3044★ · Python · Apache-2.0 · push 2026-10-11
"会主动找你玩的 AI 猫娘"：实时陪伴、主动发起、共享媒体，带具身情绪引擎；本地 LLM 驱动。
**✅ 落地 + ⚠️ 参考**：活跃度高（当日推送）、Apache-2.0、Python 栈与本机 Ollama 契合，是**桌宠身体侧**最值得细读的成熟参考。
<https://github.com/Project-N-E-K-O/N.E.K.O>

### 15. `jofizcd/Soul-of-Waifu` — 1386★ · Python · GPL-3.0 · push 2026-08-28
桌面角色扮演 & AI 伴侣应用，支持 **Live2D/VRM 头像**、语音、本地 LLM，跨聊天/RPG/桌面陪伴演进。
**⚠️ 参考**：功能面最全的"身体+人格"整合参考；但 GPL-3.0，二次分发需注意传染性。
<https://github.com/jofizcd/Soul-of-Waifu>

### 16. `x380kkm/Live2DPet` — 86★ · JavaScript · MIT · push 2026-06-22
AI 驱动的 Live2D 桌宠伴侣，集成 VOICEVOX TTS。
**⚠️ 参考**：JS 栈、结构清晰，适合起步抄"Live2D 显示 + TTS"骨架；但已约 3.5 个月无推送。
<https://github.com/x380kkm/Live2DPet>

### 17. `marine841023/duty-on` — 3★ · Rust · MIT · push 2026-10-09
Tauri 2 + Rust 的 Live2D 桌宠，**监听你的 Trae / Qoder AI 编码 agent 实时状态**，agent 等你输入时用模型提醒你。
**✅ 落地**：把桌宠当"agent 状态显示器"的范式，和 DSH 桌宠同源；Rust+Tauri 体积小，本机可跑。
<https://github.com/marine841023/duty-on>

### 18. `efficiencyx/JunOS` — 5★ · JavaScript · Apache-2.0 · push 2026-10-09
自托管 AI 伴侣，带 Live2D 动画、语音对话、持久记忆与关系动力学，由本地 LLM 驱动。
**⚠️ 参考**：架构成熟（Web 应用形态），可作"Live2D 身体 + 本地模型 + 记忆"的整合参考。
<https://github.com/efficiencyx/JunOS>

### 19. `1704919/WuziDesktopPet` — 2★ · GDScript · MIT · push 2026-10-11
基于 **Godot 4.7** 的 Windows 桌宠：随机动画、离线对话、桌面互动、图片转换与批量重命名。
**✅ 落地**：Godot 路线在 Windows 上有原生透明窗优势，MIT 许可、当日活跃，适合做轻量离线桌宠底座。
<https://github.com/1704919/WuziDesktopPet>

### 20. `Lsc-91-69/dsh-live2d-avatar` — 1★ · JavaScript · MIT · push 2026-10-07
DSH 插件：把 Live2D 模型变成桌宠，展示 agent 的实时状态与"内心想法"。
**✅ 落地**：直接命中"DSH + Live2D 身体"交叉点，代码量小、MIT，是最贴题的一手样例。
<https://github.com/Lsc-91-69/dsh-live2d-avatar>

## 六、AI 辅助 Live2D 制作

> 本节收录单图→分层 PSD 分割、自动绑定、表情差分自动生成、动作迁移等 AI 工具。（注：头部项目 see-through / ComfyUI-See-through 已在索引中，故本节偏薄。）

### 21. `SkyTNT/anime-segmentation` — 849★ · Python · Apache-2.0 · push 2025-05-21
高精度**动漫角色抠图/分割**模型（去背景、出 alpha），是"单图→分层素材"链路里最常被复用的底座。
**⚠️ 参考**：质量成熟、Apache-2.0，本机可离线推理；但 ⚠️ **疑似假活**（`pushed_at` 2025-05 vs `updated_at` 2026-10，相差近 17 个月），仅资产/README 更新，模型本身未再迭代。
<https://github.com/SkyTNT/anime-segmentation>

### 22. `halli75/motion-mirror` — 127★ · Python · MIT · push 2026-07-22
本地优先的**动作迁移**：把参考视频的动作"搬"到任意角色图上，基于 Wan2.1-VACE，是托管动作控制工具的本地开源替代。
**⚠️ 参考**：与"Live2D 动作生成/差分"方向相关，MIT 可自托管；但依赖 Wan2.1-VACE，对 16GB RAM 本地显存有要求，需实测。
<https://github.com/halli75/motion-mirror>

## 七、AI 开发工具 / Agent Harness

> 本节收录 **DSH（DeepSeek Harness）插件生态**、MCP、skill、上下文与记忆管理、vibe coding 安全。
> ⚠️ 生态提醒：本轮 DSH 相关仓库 star 普遍异常高（数万级），且存在大量**同题材聚合/市场类重复项目**与蹭 `dsh-plugin` 标签者，选型请以 `pushed_at` 活跃度与实际功能为准，勿唯 star。

### 23. `nexu-io/open-design` — 100472★ · TypeScript · Apache-2.0 · push 2026-10-11
DSH 的"设计插件"：让编码 agent 变设计引擎，产出原型/落地页/仪表盘/幻灯片/图视频，可导出 HTML/PDF/PPTX/MP4，BYOK 接 20+ CLI。
**✅ 落地**：与 DSH 主流程配合，可作为索引站/报告的可视化产出工具；Apache-2.0。
<https://github.com/nexu-io/open-design>

### 24. `anywhere-labs/dsh-desktop` — 30398★ · TypeScript · MIT · push 2026-10-10
为 DSH 插件生态打造的现代化桌面端，"万物皆插件，桌面本身也是插件"。
**⚠️ 参考**：DSH 桌面化路线的最主要实现之一，适合研究其插件宿主架构；体量巨大（470MB repo）。
<https://github.com/anywhere-labs/dsh-desktop>

### 25. `zhu1090093659/dsh-web` — 8617★ · TypeScript · Apache-2.0 · push 2026-10-10
DSH 的 **Web 插件聚合生态**，通过"创意工坊"分发插件。
**⚠️ 参考**：Web 侧插件分发/加载机制参考；与 dsh-desktop 属同一生态的不同端。
<https://github.com/zhu1090093659/dsh-web>

### 26. `MemTensor/MemOS` — 11802★ · TypeScript · Apache-2.0 · push 2026-10-10
自演化记忆 OS：超持久记忆、混合检索、跨任务技能复用，宣称省 35.24% token，支持 DSH。
**✅ 落地 + ⚠️ 参考**：**上下文/记忆管理**方向最完整的一个，Apache-2.0、活跃；可作为索引站/agent 长期记忆的候选方案。
<https://github.com/MemTensor/MemOS>

### 27. `liustack/modlens` — 4199★ · TypeScript · MIT · push 2026-10-04
DSH 的首个"视觉插件"，也是所有纯文本 coding agent 的视觉桥：粘贴图片→结构化 JSON 证据（OCR/版面/语义）。
**✅ 落地**：给本地纯文本模型"外挂视觉"的实用件，MIT，对本机 Ollama 文本模型尤其有用。
<https://github.com/liustack/modlens>

### 28. `crafter-station/petdex` — 4226★ · TypeScript · MIT · push 2026-10-10
面向 Codex / Claude Code / **DSH** / Hermes / OpenCode / Gemini CLI 等的**动画桌宠公共画廊**。
**✅ 落地**：直接连接"AI 工具 + 桌宠"两条线，可参考其桌宠资源组织与分发方式。
<https://github.com/crafter-station/petdex>

### 29. `MeteorNOX/DeepSeek-Balance-Whale-Widget` — 4463★ · JavaScript · MIT · push 2026-10-11
住进 DSH 界面右下角的"小鲸鱼娘"，盯 DeepSeek 账户余额：拖拽吸附、翻转、数字滚动动画。
**⚠️ 参考**：轻量 DSH UI 插件的典型范例，适合学"如何写一个 DSH 界面挂件"。
<https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget>

### 30. `YuJunZhiXue/dsh-purge` — 4423★ · JavaScript · MIT · push 2026-10-11
DSH "破甲"插件：支持按模型切换提示词的系统提示解除工具。
**❌ 不采用**：属规避模型安全策略的用途，与"合规使用"目标不符；列入仅为记录生态全貌（也说明 DSH 插件生态缺乏准入审查）。
<https://github.com/YuJunZhiXue/dsh-purge>

### 31. `bruc3van/awesome-dsh-plugin` — 402★ · JavaScript · MIT · push 2026-10-11
DSH 插件精选列表：**每天自动抓取 `dsh-plugin` 项目并逐个复核**，剔除蹭标签项目，按场景分类+热度排行。
**✅ 落地**：本生态**唯一明确做"去伪/复核"**的列表，找 DSH 插件应从这里入口，避免被 star 农场误导。
<https://github.com/bruc3van/awesome-dsh-plugin>

### 32. `pax-beehive/dsh-hub-cli` — 450★ · TypeScript · MIT · push 2026-10-06
DSH Plugin Hub 的开源 CLI + schemas + resolver + agent 工具。
**✅ 落地**：命令行安装/解析 DSH 插件，比手工装更可控，适合脚本化。
<https://github.com/pax-beehive/dsh-hub-cli>

### 33. `V1ki/dsh-plugin-subscriptions` — 444★ · TypeScript · MIT · push 2026-10-09
把 ChatGPT(Codex)/Claude/Grok 订阅当作 DSH 的 LLM provider，Web UI OAuth 登录、**不用 API key**。
**⚠️ 参考**：订阅复用思路对"低成本"很香，但涉及第三方订阅条款，个人自用需自行评估合规。
<https://github.com/V1ki/dsh-plugin-subscriptions>

### 34. `sixtysevenlf/dsh-blender-plugin` — 211★ · Python · BSD-3-Clause · push 2026-10-07
DSH × Blender 直连实时插件：agent 通过 TCP 驱动 Blender（视口帧、任意角度渲染、内部搜索、渲染剖析、安全减面、无头卸载），15 工具 + 28 家族/183 操作。
**⚠️ 参考**：虽面向 3D，但"agent 直连创作软件 + 实时反馈"的架构，对"AI 辅助 Live2D 绑定"有直接借鉴价值。
<https://github.com/sixtysevenlf/dsh-blender-plugin>

## 边缘登记（未入正文，仅备案）

> 均经 `gh api` 核实为真实仓库、且不在去重基线内；因体量过小 / 场景过窄 / 无许可证 / 已停更而未升级为正文条目。

**Live2D / 桌宠侧**
- `Eikanya/Live2d-model` — 3439★ · 无 license · push 2026-10-03。Live2D 模型合集资源仓（repo 达 17.6GB），**是素材源而非代码**，注意授权。
- `rig-c/play` — 3★ · TS · MIT · 2026-10-11。rig-c 编译产物的浏览器播放器（DOM/canvas、轨道/混合/加性层）。
- `qzwxsaedc/Godot-Live2D` — 17★ · GPL-3.0 · **push 2022-05**（`updated_at` 2026-08 属假活）。C++ Godot Live2D 插件，已停更 4 年。
- `ocmi-oscar/godot_live2d` — 0★ · NOASSERTION · 2026-06-20。Godot Live2D 绑定，单次推送、无描述。
- `nyan-mikan/codex-live2d` — 0★ · NOASSERTION · 2026-10-11。Codex 桌面端 Live2D 伴侣，本地模型配置+流式语音。
- `Sky33635/Elaina-Live2D-Desktop-Pet` — 2★ · 无 license · 2026-09-13。Windows 便携 AI 助手桌宠（DeepSeek 驱动）。
- `happy-shine/atri-live2d` — 1★ · 无 license · **push 2026-03-23**（停更）。Tauri + pixi-live2d-display 桌宠，含眼动/口型/表情 API。
- `dendyxanyar/MotionRig-Studio` — 0★ · 无 license · 2026-04-28。2D 绑定+分层+AI 提示工作流，仅作品集性质。
- `naotaro0123/Live2D-ThreeJS` — 15★ · 无 license · **push 2019-03**（假活）。Three.js 联动的早期 WebGL 示例，已过时。

**DSH / Agent 工具侧**
- `dataelement/dsh-desktop` — 13148★ · MIT · 2026-10-10。DSHDesktop 桌面版（与 anywhere-labs 同名同类，选一即可）。
- `Ebony-Vinyl/EAC-Desktop` — 1967★ · MIT · 2026-10-09。让数百 DSH 插件共存的桌面宿主。
- `zhukunpenglinyutong/desktop-cc-gui` — 4460★ · 无 license · 2026-10-10。多引擎（Claude Code/Codex/Gemini/DSH…）GUI 客户端，Tauri。
- `0xsline/awesome-deepseek-harness` — 1162★ · CC0-1.0 · 2026-10-10。DSH 生态聚合列表（与 bruc3van 版同题材）。
- `mrpulor-gh/nuphus-mcp` — 322★ · Rust · MIT · 2026-10-11。桌面自动化 MCP（屏幕/窗口/键鼠/Chrome 控制）。
- `Fishquito7/dsh-skill-mcp-panel` — 194★ · JS · MIT · 2026-09-30。DSH Web UI 的 skill/MCP 管理面板。
- `Nagi-ovo/dsh-find-plugins` — 178★ · JS · BSD-3 · 2026-08-15。DSH 内搜索/安装/验证插件的 Skill。
- `MichengAI/dsh-skills-manager` — 104★ · JS · Apache-2.0 · 2026-10-07。DSH 本机 Agent Skills 统一加载与安全管理。
- `Zhenyu98/dsh-context-doctor` — 37★ · TS · BSD-3 · 2026-09-06。**上下文注入审计**：统计 AGENTS.md/技能目录/工具 schema 的 token 成本并查重冲突。
- `NanmiCoder/dsh-skills-hub` — 26★ · JS · MIT · 2026-10-01。DSH 内浏览/预览/安装第三方 skill。
- `realchendahuang/dsh-skill` — 24★ · JS · MIT · 2026-10-06。DSH 官方插件 & skill 开发套件。
- `agent-contracts/skill-preflight` — 3★ · TS · MIT · 2026-10-11。**skill 安装前安全评分卡**（权限/token 成本/可维护性）。
- `dushaobindoudou/dsh-plugin-security` — 2★ · JS · MIT · 2026-10-11。DSH 插件安全网关（npm advisory + 静态证据 + 调用时放行确认）。
- `979569650/dsh-typesafe` — 2★ · JS · MIT · 2026-09-22。DSH 决策层 + 对不可信工具结果的自动提示注入防护。
- `cline/mcp-marketplace` — 792★ · MIT · **push 2025-06-24**（停更）。Cline 官方 MCP 提交仓，仅作登记。
- `EvolutionUnleashed/skill-sentinel` — 17★ · 无 license · **push 2026-02-20**（停更）。SKILL.md 恶意代码/注入检测扫描器。
- `Cydiar/skill-guard` — 5★ · Python · MIT · **push 2026-05-20**（停更）。Agent skill 安全审计平台（10 维 109 规则）。

## §去重报告

### A. 命中去重基线 `_r34/_dedupe_gh.txt`，直接剔除（*已在索引或本轮已收录*）
| 候选 | 命中情况 | 处置 |
|---|---|---|
| `shitagaki-lab/see-through` | 已在基线 | 剔除（本轮 AI 分层最强项，可惜已收） |
| `jtydhr88/ComfyUI-See-through` | 已在基线 | 剔除 |
| `moeru-ai/airi` | 已在基线 | 剔除 |
| `morettt/my-neuro` | 已在基线 | 剔除 |
| `elevenyellow/handcrafted-persona-engine` | 已在基线 | 剔除 |
| `momori777/Artemis` | 已在基线（小写） | 剔除 |
| `qiyueblues-design/zhuomianling` | 已在基线 | 剔除 |
| `menglimi/astrbot_plugin_live_stream_companion` | 已在基线 | 剔除 |
| `SakuraMotion/PurismCore` | 已在基线 | 剔除 |
| `KurisuMakise004/renderkit` | 已在基线 | 剔除 |
| `goldimpact/Eviler` | 已在基线 | 剔除 |
| `zeikar/iki` | 已在基线 | 剔除（原计划入替代栈） |
| `Heonys/live2d-web` | 已在基线（`heonys/live2d-web`） | 剔除 |
| `lmmtrr/spive2d` | 已在基线 | 剔除 |
| `ariakage/live2d-agent-kit` | 已在基线 | 剔除 |
| `pakholeung37/manosaba-live2d` | 已在基线 | 剔除 |
| `wzhang3912/image2live2d` | 已在基线 | 剔除 |
| `tsunehimatoi/psd2live` | 已在基线 | 剔除 |

### B. 停更 / “假活”识别（`pushed_at` 远早于 `updated_at`，仅改 README/挂资产）
- `qzwxsaedc/Godot-Live2D`（push 2022-05 / update 2026-08，差 ~51 个月）→ 边缘登记。
- `naotaro0123/Live2D-ThreeJS`（push 2019-03 / update 2025-12）→ 边缘登记。
- `Arkueid/lpk2moc3`（push 2023-08，**archived**）、`QiE2035/moc3-reader-re`（push 2022-07，archived）、`kongbaiku/Live2D-M`（push 2021-03）、`zenghongtu/PPet`（push 2024-06）→ 剔除。
- `SkyTNT/anime-segmentation`（push 2025-05 / update 2026-10，差 ~17 个月）→ **保留正文但显著标注**。
- `Delsin-Yu/GD-PSD-Layer-Import-Plugin`（差 ~6 个月）、`MangoLion/stretchystudio`（差 ~5.5 个月）、`Eatgrapes/Mocari`（差 3 个月）→ 正文内标注但保留。
- `cline/mcp-marketplace`、`EvolutionUnleashed/skill-sentinel`、`Cydiar/skill-guard`、`happy-shine/atri-live2d`、`dendyxanyar/MotionRig-Studio` → 边缘登记并标注停更。

### C. SEO 镜像 / 内容农场 / 同题材重复聚合（不重复收录）
- **DSH awesome 列表撞车**：`awesome-dsh-plugin/awesome-dsh-plugin`（基线已有）、`Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins`、`bruc3van/awesome-dsh-plugin`、`0xsline/awesome-deepseek-harness` 内容高度重叠 → 仅收 `bruc3van`（唯一明确“每日复核、剔除蹭标签”者），其余入边缘/剔除。
- **DSH 插件市场撞车**：`dsh-market/dsh-market`、`LivXue/dsh-plugin-shop`、`hellohupc/dsh-plugin-hub`、`AdamPlatin123/dsh-plugin-radar`（多数已在基线）→ 全部剔除。
- **数据售卖壳**：`nextcombo/fully-new-leather-hood-live2d-...`（描述为 “Dataset / resource listing. Sponsor to obtain the full data files.”）→ 剔除，典型 SEO/售卖壳。
- **同名双胞胎**：`anywhere-labs/dsh-desktop` 与 `dataelement/dsh-desktop` 均自称 "DSH Desktop" → 正文取前者，后者入边缘。

### D. 场景不符 / 质量不足（剔除）
- `KurisuMakise004/renderkit`（**archived**，虽 push 2026-10 但已归档）、`YuanNeoMax/YuanLive2D-Minecraft-Forge-Mod`（场景过窄，已降为正文❌条目）、`fly3366/YuraYura`（macOS only，降为正文❌条目）。
- `YanWei...`/`naotaro...` 系列早期 WebGL 示例、`Live2D-WebGL-SDK`（官方 SDK 托管副本，非新项目）→ 剔除。

### E. 计数
- 正文条目：**34** 条（`grep -cE '^### [0-9]+\. '` = 34）。
- 边缘登记：**26** 条。
- 与 `_dedupe_gh.txt` / `_dedupe_urls.txt` 零重复（正文 + 边缘全部逐条 `grep -iF` 校验通过）。
- 全部条目均以 `gh api repos/{owner}/{repo}` 实取 star / license / language / `pushed_at` / `updated_at` / `created_at`。
