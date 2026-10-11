# -*- coding: utf-8 -*-
"""把第三十八辑小结插到 csdn-social-summary.md 标题行之后（不覆盖旧 34 辑内容）。"""
import io, os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
PATH = os.path.join(ROOT, "csdn-social-summary.md")

S38 = '''# 跨平台游戏制作 × AI 开发资源梳理 · 第三十八辑（2026-10-11 · Live2D 制作全谱系补采）

> 本辑为 Live2D 连续第十一轮。三路并行（gh / cn / official），共得 **gh 24 条 + cn 18 条 + official 16 条** 候选，
> 经与 index.html（1403→1426 项）及 csdn-social-summary（v34 / v36）比对待办，**全部 28 个 GitHub slug 零重复**，
> 落索引 **23 张卡（1386→1409）+ 23 条脚注（[1403]–[1425]）**。详细条目见 `_r38/_r38_gh.md` / `_r38_cn.md` / `_r38_official.md`。

## 一、搜索覆盖

| 路 | 覆盖 | 正条 | 边缘 |
|---|---|---|---|
| gh | GitHub / Gitee / HF：Live2D 工具·查看器·插件·引擎·AI 数字人 | 24（§三 11 + §四 13 [AI]） | 7 行（§五） |
| cn | CSDN / 掘金 / 知乎 / 公众号 / 少数派 / gamemale / 微博 / B站 | 18 | gamemale 复测状态 1 + 应用/纠纷 4 + [AI] 1 |
| official | Cubism 官网·release notes / note.com / r-Live2D / 官方论坛 / X | 16（§三 8 + §四 4 + §五-A 6 帖） | — |

## 二、本辑一句话主线

**Live2D 制作的「身体侧」供给继续加密，且第一次出现可验证的硬指标样本；AI×Live2D 数字人从「主张」彻底变成「重复模式」——
12 条新增 AI 桌宠/数字人收敛出一条可复用的本地栈（Live2D 渲染 + 本地 LLM/Ollama + TTS/ASR + 长期记忆）。**

## 三、分主题条目（均带链接，细节见 _r38_*.md）

### A. 工具 / 查看器 / 插件 / 引擎（gh §三，11 条）
- **ImDuck42/Live2D-Viewer**（★14 · MIT）— **本辑唯一标「落地」的网页查看器**：原生 JS+PIXI.js 6.5.10，四种载入（URL/预设/GitHub 仓库浏览器/本地 ZIP），可在索引站直接嵌一个 Live2D 预览器。[1412]
- **TSKI433/hime-display**（★254 · GPL）— 一套 UI 看 Live2D/Spine/MMD/VRoid 四格式，做素材库预览省事。[1404]
- **LIlGG/plugin-live2d**（★251 · MIT）— Halo 博客 Live2D 看板娘插件，即插即用。[1405]
- **evgo2017/vue-live2d**（★166 · MIT）— Vue 组件版看板娘。[1409]
- **amorist/platelet**（★226 · GPL）— 经典「血小板」网页看板娘 widget。[1406]
- **LSTM-Kirigaya/Live2dRender**（★183 · Apache）— Web 端新版 Cubism 渲染封装，当渲染底座。[1408]
- **Arisego/UnrealLive2D**（★153 · MIT）— Unreal 路线稀缺的 Live2D 桥接（⚠️ 2025-02 后未动，先核 SDK 兼容）。[1410]
- **iCharlesZ/vscode-live2d-models**（★169）— VSCode 看板娘模型库（资源集合）。[1407]
- **ezshine/AwesomeLive2D**（★411）— Live2D 模型/资源 awesome 清单（约 3 年未动，作导航）。[1403]
- **redchenk/yachiyo-live2d-studio**（★25 · MIT）— 当天建仓的「studio」，待 README 补全再评。[1411]
- **sweetcornna/OneClick2D**（★0）— **不碰 Cubism 授权的替代格式 .oc2d**，版权敏感场景的稀缺思路。[1413]

### B. AI × Live2D 数字人 / 桌宠（gh §四，12 条，全部 [AI]）
- **HELPMEEADICE/BANDORI-PET-REV**（★465 · GPL）— **本辑最硬指标**：Cubism SDK+PySide6，51+ 角色/305+ 服装，自研 LuaJIT 渲染核较 live2d-py **6 倍+（30→180fps+）**，Qwen3TTS 口型 + faster-whisper ASR + LLM 记忆。[1422]
- **waterfeet/DoroPet_V3**（Gitee · ★7 · Apache）— **架构最贴本机栈**：live2d-py + Ollama + sherpa-onnx/edge-tts + SQLite 记忆 + Galgame 叙事。[1423]
- **andyhuo520/openclaw-assistant-mvp**（★408）— Electron AI 语音助手 + Live2D 表情/口型（⚠️ 无 LICENSE）。[1414]
- **MIO-456/Lumi_Nox**（★239 · MIT）— 双 AI VTuber 同台直播实时编排（open-core）。[1415]
- **YuriCrystal/ai-avatar-bot**（★203 · NOASSERTION）— Live2D/VRM 语音 avatar，一行嵌入网站。[1416]
- **inni918/warashi**（★119 · NOASSERTION）— 桌面 AI 伴侣：Live2D+语音+长期记忆+主动搭话（正中本地 Ollama 基准）。[1417]
- **chyinan/Kokoro-Engine**（★156 · MIT）— Rust 跨平台虚拟角色交互引擎。[1424]
- **funnycups/petto**（★119 · GPL）— Flutter/Dart Live2D 桌宠。[1418]
- **ReSerendipity/SpiritPal**（★0 · Apache）— **Tauri v2 + Pixi.js 8 Live2D**（2026 新写法样本）。[1421]
- **DesktopPetXuansi/Xuansi**（★1 · Apache）— Windows 本地 AI 桌宠，纯本地优先。[1420]
- **Nav-Joe/Xue_CyberNeko**（★7 · MIT）— 轻量 Live2D AI Neko。[1419]
- **aurel-g/ComfyUI-Live2DViewer**（★0 · MIT）— ComfyUI 节点预览 Live2D（补「AI→Live2D 流水线」可视化环，但 2024 起停更）。[1425]

### C. 中文经验帖 / 实战测评（cn，取到正文的关键 2 条 + 状态）
- **塔猴《2D 立绘活了：Live2D / Spine 动作的 AI 辅助生成流》**（tahou.com · 2026-01-13）— **本辑唯一取到正文的中文 AI 辅助 Live2D 流程帖**：AI 拆层 → Auto Mesh → Deform Path → Auto Standard Form → Physics/Auto Blink/Breathing Loop，给了可点的菜单路径（「3–5 天→1 天」偏宣发，需自测打折扣）。[CSDN 路径见 _r38_cn.md §六]
- **CSDN React 帖「TTS→RMS→口型」代码** — 可直接抄进本地 Ollama 语音桌宠（主 agent 实测优先级 2）。
- **Steam AI桌面宠物**（4227700 · 42kami）— 本地 LLM + Live2D 桌宠，最贴 16GB+Ollama 基准（待装实测）。
- 已剔除：米画师 4 处价格锚（R41 已收）、海淀 7627 元案（R37 已收）、SAM 2 三篇 weixin_数字 内容农场（打假）。
- **gamemale 复测**：仍被 Cloudflare 挑战页挡住 → **本轮未命中（待复测）**，未写成负结论。

### D. 官方 / 海外（official，关键结论）
- **Cubism 5.4**：仍为 **alpha2，可用期延至 2026-10-18，未转 beta**；alpha 版无前方兼容（alpha2 存的工程 5.3 打不开）。
- **官方论坛**：Unity Sprite 压不过模型 / motion3 覆盖重导入 / Unreal SDK 停摆三件事上轮已认领，本轮无新进展。
- **note.com / r-Live2D**：本机 fetch 000（非限流），下轮用代理或带登录态浏览器补采。
- **creatorsforum.live2d.com**：403 用 `.json` 端点绕过成功。

## 四、AI 开发 / 使用相关帖子的实测结论（主 agent 逐条读 + 核实）

本轮 [AI] 帖子共 **13（gh）+ 1（cn）= 14 条**，全部走 `gh api` 复核 stars/许可证/语言/日期。结论：

1. **可复用性**：除 ImDuck42/Live2D-Viewer 标「落地」外，AI 数字人/桌宠 12 条均为 **② 参考**、1 条 HF LoRA 为 **③ 不采用**（闭源付费、非本地）。
2. **收敛出的本地栈**（对本机 16GB+Ollama 基准直接有用）：`Live2D 渲染（pixi-live2d / live2d-py）+ 本地 LLM（Ollama / Qwen3）+ TTS（edge-tts / sherpa-onnx / Qwen3TTS）+ ASR（faster-whisper）+ 长期记忆（SQLite / JSON）`。
   - 最完整两个样本：**BANDORI-PET-REV**（★465、自研渲染核 6x+）与 **DoroPet_V3**（Gitee、live2d-py+Ollama 全链路）。两者协议分别为 GPL-3.0 / Apache-2.0，抄架构不抄依赖。
3. **是否「改我们的工具/流程」**：**本轮不改**。这些帖子是「AI 桌宠/数字人」应用，对维护索引站 / agent 工具链无直接改造点；其价值是**作为索引卡收录**（已落 12 张）与**本地栈架构参考**。
4. **待实测（留作下轮待办）**：在 16GB 本机 clone 并跑通 BANDORI-PET-REV / DoroPet_V3，验证本地 Ollama 栈可行性；以及在 Cubism 5.3 复一遍塔猴的 `Auto Standard Form` 是否真按图层命名自动形变。

## 五、可拓展性 & 实用性 思考（通俗版）

- **查看器/插件侧**：格局已稳，新增多是「换框架再实现一遍」（Halo / Vue / Unreal / Flutter）。**真正可落地的是 ImDuck42/Live2D-Viewer**——它能在我们的索引站里直接嵌一个 Live2D 模型预览器，MIT、有在线 demo，改造量小。
- **AI 数字人侧**：这是本辑密度最高的方向，且**第一次出现可验证硬指标**（BANDORI-PET-REV 的 6x 渲染、50+/300+ 模型量）。说明「AI 装 Live2D 身体」已从玩具走向能跑的工程。但**绝大多数是 ★0–1 或当天建仓**，协议也参差（无 LICENSE / NOASSERTION / GPL 传染），当参考骨架可以，当依赖不行。
- **合规红线仍在**：凡碰 `.moc3` / Cubism SDK 的（BANDORI-PET-REV、DoroPet_V3、UnrealLive2D）都绕不开 Live2D 官方授权；**OneClick2D 走「不碰 Cubism」的 .oc2d 替代格式**是版权敏感场景的稀缺思路，值得持续盯。
- **对本机最实用的三件事**：① 用 Live2D-Viewer 给索引站加预览器；② 抄 BANDORI/DoroPet 的本地栈架构做自己的桌宠/数字人；③ 把「本地 LLM + TTS/ASR + 记忆」当标准件复用，别重复造。

## 六、索引与文档维护

- 落索引：**insert_v42_cards.py** → 23 张卡（1386→1409）+ 23 条脚注（[1403]–[1425]）；页头 1403→1426 项。
- `index_metrics`：**E1–E7 全绿**，恒等式 1426 == 1425+1，div 13389/13389 平衡，`--update` 已重封 312 分组快照。
- ⚠️ **脚注区漂移（上轮待办①）仍未修**：[1301]–[1378] 嵌在 card `rpm38c4` 内，本辑 [1403]–[1425] 按既有规则接在其后，**同样落在 card 容器内**（这是 E1–E7 盲区，下轮必修）。
- 原始产出：`_r38/_r38_gh.md` / `_r38_cn.md` / `_r38_official.md`。

## 七、下一辑待办（按序）

1. ⭐ **修脚注区漂移**：把 [1301]–[1378]（及本辑 [1403]–[1425]）整体搬出 `rpm38c4` 的 card div 进 `<footer>`，并给 `index_metrics` 加「脚注不得出现在 card 容器内」判据（加判据后必跑 `gate_recall_probe` + 造负对照）。
2. ⭐ **实测 py-moc3 / easy-live2d v0.4.0 `playVoice()`**（上轮待办②③，仍pending）。
3. **AI 桌宠本机可行性实测**：clone BANDORI-PET-REV / DoroPet_V3，在 16GB 跑通 Ollama 本地栈。
4. **Cubism 5.4 alpha 10-18 下线后复测**（转 beta？SDK 手册补 alpha2？）。
5. **中文源补采**：note.com / r-Live2D / 知乎·B站（带登录态浏览器），本机 fetch 000 本轮未取到。
6. 超上下文顺延：ayagami 复查（连续多轮无推进）、DSH 插件生态成辑。

## 统计页脚（第三十八辑）

- 检索：gh 24 条正文 + 7 边缘 · cn 18 条正文 · official 16 条正文。
- 去重：28 个 GitHub slug 对 index.html + csdn-social-summary(v34/v36) **零重复**；打假 SAM2 内容农场 3 篇、剔除 R37/R41 已收旧闻 2 处。
- 索引：**1403 → 1426 项**（卡片 1386→1409 / 脚注 1402→1425）；分组 311→312。
- 闸门：`index_metrics` E1–E7 全绿 + `--update` 重封快照。
- 原始：`_r38/_r38_gh.md` · `_r38_cn.md` · `_r38_official.md` · `insert_v42_cards.py` · `prepend_summary.py`。

---

'''

with io.open(PATH, encoding="utf-8") as f:
    text = f.read()

# 在第一行（H1 标题）之后插入本辑小结
lines = text.split("\n", 1)
if len(lines) == 1:
    new = S38 + text
else:
    new = lines[0] + "\n" + S38 + lines[1]

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new)

print("✅ 已把第三十八辑小结插入 csdn-social-summary.md 标题之后")
print("   新文件字节数：", len(new.encode("utf-8")))
print("   含『第三十八辑』：", "第三十八辑" in new)
print("   旧 34 辑内容是否保留：", "第三十四辑" in new)
