# GitHub 开源项目梳理 · 游戏制作 × 游戏拓展 × AI 制作游戏

一份面向实践的项目地图：从 GitHub 筛出活跃、可落地的开源项目，按「游戏制作」「游戏拓展与解包」「AI 制作游戏」三条线梳理，逐项评估可拓展性与实用性，并用通俗语言（含类比）讲清楚。

## 在线查看

https://re0211.github.io/github-projects-invest-games/

## 内容结构

2. **游戏制作** — 通用引擎 / 视觉小说引擎 / AI 辅助开发 / 游戏 AI / 中间件 / 内容生产工具
3. **游戏拓展与解包** — 通用资源浏览器 / 分引擎解包 / MOD 框架 / AI 本地化 / 逆向工具链 / 模拟器 / 引擎重实现
4. **推荐组合与落地路线** — 三条路径（做游戏 / 解包到 MOD / 接上 AI 制作游戏专题）
5. **避坑与合规** — 维护状态、License、过拟合、解包边界

## 评分口径

- **可拓展性**：二次开发、脚本化、接入自有系统的难度（越高越容易扩展）
- **实用性**：当下就能解决问题的程度

两项均为基于项目架构、文档、社区与更新状态的主观评估。

## 数据来源

GitHub Repository API、Search API 与 GraphQL API，抓取时间 **2026-09-09**（UTC+8）。共 **1054** 个项目，星级、最近更新时间、License、归档状态均为逐项实测值。

### 版本记录

| 版本 | 项目数 | 本轮重点 |
| --- | --- | --- |
| 2026-09-01 | ~40 | 建立三条线骨架 |
| 2026-09-02 | 72 | 补齐 MOD 框架与 AI 本地化 |
| 2026-09-03 | 214 | 补齐引擎阵容、引擎重实现、AI 投研智能体 |
| 2026-09-04 | 295 | 补投资线「通道层」（openctp / ib_async / alpaca-py）；补 three.js、Aseprite、Box2D 等基础设施；新增游戏 AI 子类与 Unity IL2CPP 逆向链、模拟器谱系 |
| 2026-09-06 | 212 | 应要求删除投资线，全面转向游戏；新增「AI 制作游戏」专题（5 组 23 项） |
| 2026-09-08 | 263 | 零重复增量 51 项：MOD 运维、开源样本库、模拟器前端、AI 生成 3D / 配音 / 玩游戏 |
| 2026-09-08 | 319 | 零重复增量 56 项：补齐物理引擎替换、游戏音频、现代联机、二进制分析四大空白 |
| 2026-09-08 | **398** | 零重复增量 79 项：图形调试与 Shader 链路、底层基座、中文热更新生态、本地跑模型与 Agent 协作、OCR 与老素材修复、UE 改造、Proton/DXVK 兼容层、radare2/angr 自动化逆向、街机与掌机模拟器 |
| 2026-09-08 | **508** | 零重复增量 110 项：界面与编辑器、数学/窗口/图形底座、数据序列化、资产管线、网络传输层、多语言引擎框架、构建与性能剖析、Steam 接入、VR；AI 侧新增立绘抠图放大与「让角色开口说话」、离线语音识别；解包侧新增 .NET 逆向五件套、IL2CPP 最后一公里、音频提取、视觉小说底层引擎（KiriKiri / ONScripter / RPA） |
| 2026-09-08 | **638** | 零重复增量 130 项：摄影测量与 3D 重建（Meshroom / COLMAP / VGGT）、动作捕捉（MediaPipe / OpenPose / FreeMoCap / AnimateAnyone）、关卡生成研究环境（Procgen / MiniGrid / TextWorld）、游戏测试自动化、游戏运营分析；补缺网页游戏引擎、字体与文字排版、3D 资产管线、中文游戏服务端、开源游戏样本、Minecraft MOD 生态、ROM 自建库 |
| 2026-09-08 | **753** | 零重复增量 115 项。覆盖面开始饱和（268 个候选里 153 个上版已收），转向细分空档：MMO 服务端（TrinityCore / rAthena）、棋类与博弈 AI（Stockfish / KataGo / Pikafish）、幻想计算机（wasm4）、音频工作站与芯片音乐（Ardour / OpenMPT / MilkyTracker）、神经渲染（nerfstudio / instant-ngp）、后端即服务（PocketBase / Supabase）、资源压缩与编解码底座（zstd / Opus / libpng）、Doom 源端口与 Minecraft 生态、AI Agent 评测基准（SWE-bench / terminal-bench / LiveCodeBench） |
| 2026-09-09 | **902** | 零重复增量 149 项。饱和度再刷新（353 个候选里 147 个上版已收）。补十一块空档：工业级 3D 资产管线（OpenUSD / MaterialX / OpenVDB / OpenImageIO / OpenColorIO）、高斯泼溅生态、注入式画质增强（OptiScaler / Magpie / MangoHud）、DOS 与老 PC 兼容层谱系、掌机与复古前端、Minecraft 模组生态、REDengine 模组工具；AI 侧重点补世界模型与生成式游戏引擎（Matrix-Game / DIAMOND）、具身智能仿真环境（Genesis / MuJoCo / IsaacLab）、本地推理与量化部署（ktransformers / MLX / PowerInfer）、抠图与说话头像（BiRefNet / EchoMimic）、AI 音乐生成（YuE）、LLM Agent 与代码能力基准（SWE-agent / MLE-bench / tau-bench） |
| 2026-09-09 | **1054** | 零重复增量 152 项。饱和度再刷新（382 个候选里 241 个上版已收），增量转向「引擎下面的那一层」。补的十一块空档：免费 2D 美术与动画（GIMP / Krita / Synfig / OpenToonz）、着色器编译链（DXC / Slang / SPIRV-Tools / WebGPU）、内存分配器（mimalloc / jemalloc / rpmalloc）、图像压缩与转码底座（JPEG XL / WebP / AV1）、光追与离线渲染（Embree / OIDN / OSPRay）、深度学习框架与分布式训练（PyTorch / JAX / DeepSpeed / Ray）、多 Agent 协作与可观测（ChatDev / Letta / Langfuse）、MCP 协议规范、RPG Maker 与 Roguelike 的开源实现、掌机与手机兼容层生态（Winlator / FEX / box64 / MiSTer）、汉化最后一公里（fonttools 字体子集化 / Aegisub / Textractor） |

每轮都会重新抓取全部条目的星级与更新时间，对超过 18 个月未更新的项目打「停更」标记。

## 信源规范

正文每张卡片底部标注最近更新时间、License 与信源编号，编号可点击跳转至页脚完整信源清单（共 1054 项，全部可追溯）。信源编号按正文出现顺序编排，正文条目与页脚清单一一对应。

## 说明

本项目仅用于技术调研参考，不构成投资建议。涉及解包工具的使用请遵守当地法律法规与软件许可协议。
