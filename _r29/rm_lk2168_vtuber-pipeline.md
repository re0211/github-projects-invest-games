# vtuber-pipeline

把一张动漫立绘变成能在 VTube Studio 里直播的 Live2D 模型。

[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![dependencies](https://img.shields.io/badge/deps-requirements.txt-blue)](requirements.txt)

**写给谁**：想自己做一个 AI 虚拟主播形象、并且愿意动手改图层的人。
如果你只想点几下就拿到成品，这个仓库帮不上忙。

**前提**（这些要你自己准备好，本项目不替你安装，步骤见下面的「环境准备」）：
Windows 系统；NVIDIA 显卡 8GB 显存；可用内存 3GB 以上；
装好 ComfyUI 并让它在本机 8188 端口运行；装好 VTube Studio 并开启插件 API；
愿意按自己的环境改脚本里的绝对路径。

**状态**：主链路已经跑通，产出的模型可以加载进 VTube Studio 直播。
眼睛和嘴的多状态表情需要手工补，见「限制」。

> **English TL;DR**: A glue layer between [See-through](https://github.com/shitagaki-lab/see-through)
> (illustration to semantic layers) and [PSD2Live](https://github.com/tsunehimatoi/psd2live)
> (layered PSD to rigged Live2D model), plus the format gotchas and layer-quality fixes
> that break the handoff.

---

## 它解决什么问题

两个上游工具各自都能跑，但中间缺一环：

```
立绘 PNG
   │
   ├─ See-through      拆成 20+ 个语义图层（PNG + layers.json）
   │                   不给 PSD，官方 PSD 要在网页上手点生成
   │
   ✗  缺的是这里：分层结果 → 符合 PSD2Live 规范的 PSD
   │
   └─ PSD2Live         分层 PSD → .moc3 + 物理 + 动作
                       对 PSD 格式有硬性要求，不满足就出黑方块
```

本仓库提供这一环，并处理沿途会碰到的三类问题。

| 步骤 | 工具 | 做什么 |
|---|---|---|
| 1 | `prep_source.py` | 从画面四边泛洪，抠掉背景，裁到内容边界 |
| 2 | See-through | 按语义把立绘拆成 20 多个图层，输出每层 PNG 和 `layers.json` |
| 3 | `face_pass.py`（可选） | 脸部单独再分一次层，提高眼睛和嘴的贴图分辨率 |
| 4 | `compose_psd.py` | 把分层结果重建为 PSD2Live 能读的 PSD |
| 5 | PSD2Live（由 `build_avatar.py` 调用） | 自动绑定，输出 `.moc3` 模型 |
| 6 | `build_avatar.py --install` | 把模型复制进 VTube Studio 的模型目录 |

`run_full.py` 把 1 到 6 串成一条命令。

另外有一个 `vts_load_model.py` 不在这条链里：它通过 VTube Studio 的插件 API
加载**已经装好**的模型，也可以列出当前有哪些模型。自动化测试时会用到它。

---

## 环境准备

按顺序装四样东西：ComfyUI、本项目的依赖、See-through 插件、PSD2Live。

### 1. ComfyUI

分层这一步是通过 ComfyUI 的 HTTP API 调用的，所以先要有它。
从 <https://github.com/comfyanonymous/ComfyUI> 获取并装好，
确认能用浏览器打开 `http://127.0.0.1:8188`。

### 2. 本项目的依赖

```bash
pip install -r requirements.txt
```

### 3. 上游工具

本仓库不包含它们的代码和权重。

```bash
# See-through：走 ComfyUI 插件最省事，插件里已内置完整源码
git clone https://github.com/jtydhr88/ComfyUI-See-through.git \
  <ComfyUI>/custom_nodes/ComfyUI-See-through
pip install diffusers peft accelerate opencv-python scikit-learn matplotlib bitsandbytes

# PSD2Live：Windows 便携版
# https://github.com/tsunehimatoi/psd2live/releases 下载 portable.zip
# 解压后把 PSD2Live.exe 整个目录放到 <仓库>/tools/ 下
# （build_avatar.py 第 37 行写死了这个位置；想放别处就改那一行）

# 模型权重放进 <ComfyUI>/models/SeeThrough/，目录下需有 model_index.json
```

注意 SDXL 有两个 tokenizer（`tokenizer/` 和 `tokenizer_2/`），各需要一份 `merges.txt`，
少一份会在加载时失败。

**必须改的路径与必须就位的东西**。三个路径常量都在脚本顶部的常量区，
另有一个可执行文件必须放到指定位置：

| 位置 | 是什么 | 说明 |
|---|---|---|
| `run_full.py` 的 `OUT` | 你的 ComfyUI `output` 目录 | 分层结果写在这里 |
| `build_avatar.py` 的 `VTS_MODELS` | 你的 VTube Studio `Live2DModels` 目录 | 加 `--install` 时复制到这里 |
| `prep_source.py` 的 `DEST` | 去背景结果的存放目录 | **必须与 `run_full.py` 期望的 `<仓库>/_work/src` 一致**，否则 `run_full.py` 在第二步直接报错退出 |
| `<仓库>/tools/PSD2Live.exe` | 上游绑定工具 | 不放这里就要改 `build_avatar.py` 第 37 行 |

`OUT` 和 `VTS_MODELS` 彼此无关，各自改对即可；只有 `DEST` 需要与 `run_full.py` 对齐。

---

## 用法

运行前确认两件事：ComfyUI 已经在 8188 端口运行，VTube Studio 已经启动并开启插件 API（8001 端口）。

```bash
python pipeline/run_full.py <立绘.png> <模型名> --resolution 1280
```

这条命令最后一步会把模型装进 VTube Studio。只想生成不想安装的话，加 `--no-install`。

分步执行：

```bash
python pipeline/prep_source.py 立绘.png
python pipeline/build_avatar.py --layers <layers.json> --name <模型名> \
    --source <prepped.png> --split-occlusion bottomwear:legwear
```

参数说明。下表的默认值来自 `run_full.py` 和 `build_avatar.py`；
如果直接调用 `compose_psd.py`，`--expand` 和 `--lash-trim` 的默认值都是 0，必须显式传。

| 参数 | 默认 | 说明 |
|---|---|---|
| `--resolution` | 1280 | 分层分辨率。1024 偏糊，1536 显著变慢 |
| `--quant` | none | 分层模型的量化方式。不要改成 nf4，会让 ComfyUI 原生崩溃（`Fatal Python error: Aborted`） |
| `--expand` | 6 | 每层 alpha 向外扩的像素数，用来掩盖图层之间的接缝 |
| `--lash-trim` | 45 | `eyelash` 只保留顶部百分比。PSD2Live 要求它只含上睫毛线，而 See-through 输出的是整个上眼睑 |
| `--split-occlusion` | bottomwear:legwear | 遮挡拆分，让腿真正位于裙子内部 |
| `--no-install` | 关 | 只生成模型，不装进 VTube Studio |

---

## 实际会踩的坑

六条，按类型分成格式 2 条、上游插件 1 条、本仓库脚本 1 条、运行环境 2 条。

### 格式 1：PSD 的透明必须用原生 alpha 通道

**症状**：模型贴图是黑底加碎片，VTube Studio 里只看得见头发。

**原因**：用 `psd-tools` 的 `PSDImage.new(mode="RGB")` 建 PSD，再用
`PixelLayer.frompil()` 传入 RGBA 图像时，alpha 会被写成图层蒙版，文件只有 3 个通道。
而 PSD2Live 使用自研的 PSD 读取器，只读原生 alpha 通道，不读图层蒙版，
于是把图像读成"全不透明 + 黑底"。

**解决**：

```python
psd = PSDImage.new(mode="RGBA", size=(W, H))   # 必须是 RGBA，不是 RGB
```

不用打开软件就能验证：用 `psd-tools` 读成品 PSD，`psd.channels` 应该是 4，
每层的 `has_mask` 应该是 `False`。如果是 3 且 `has_mask=True`，说明透明度被写成了图层蒙版。

### 格式 2：`eyelash` 的语义冲突

| | 要求 |
|---|---|
| PSD2Live 文档 | `eyelash` 仅限上睫毛线，不能混入下睫毛或下眼眶线 |
| See-through 实际输出 | 整个上眼睑，实测 51×40，比 `eyewhite`（34×26）还大 |

结果就是眼睑盖住眼球，渲染出来眼睛是一条缝。解决办法是只保留 `eyelash` alpha
内容的顶部若干高度，默认 45%。

```bash
python pipeline/compose_psd.py in.json out.psd --lash-trim 45
```

### 上游插件 3：硬编码了联网拉取 scheduler

**症状**（离线使用时必然出现）：

```
OSError: frankjoshua/juggernautXL_version6Rundiffusion does not appear to have a file named scheduler_config.json
```

**原因**：`see-through/common/modules/layerdiffuse/diffusers_kdiffusion_sdxl.py` 约 120 行
硬编码了 `frankjoshua/juggernautXL_version6Rundiffusion` 去 `from_pretrained(subfolder="scheduler")`，
而 `nodes.py` 传的是 `scheduler=None`，于是必然走到这个分支，在 `local_files_only=True` 下失败。

**解决**：补丁在 [`patches/`](patches/)，改为优先读取本地仓库自带的
`scheduler/scheduler_config.json`，读不到才回退联网。

### 自身脚本 4：分层失败时曾经仍然返回 0

最早版本的 `test_seethrough.py` 拿到 `status_str == "error"` 时只打印日志，返回码依然是 0。
上层因此认为成功，接着去取 mtime 最新的 `*_layers.json`，取到的其实是上一次分层的清单，
再配上这一次的源图，产出一个层与图完全不匹配的模型，日志还打印"全部完成"。

现在这两处都堵住了：该脚本失败时以非 0 退出，
`run_full.py` 也只接受本次任务开始之后生成的清单，取不到就报错停止。

### 运行环境 5：`Allocation on device` 是显存不足

不是内存不足。ComfyUI 自身会占用 5 到 6 GB 显存（共 8 GB 时），
而分层峰值需要约 6.5 GB。跑之前先让它卸载模型：

```bash
curl -X POST http://127.0.0.1:8188/free \
  -H "Content-Type: application/json" \
  -d '{"unload_models":true,"free_memory":true}'
```

### 运行环境 6：跑得慢通常是系统内存不足

可用内存降到 1 到 2 GB 时会发生换页，同一张图能从几分钟拖到十五分钟以上。
跑之前检查可用内存，低于 3 GB 就不要开始。实测数据见 [链路实测报告](docs/链路实测报告.md)。

---

## 分层结果的画质问题

See-through 输出的图层，某些层的 alpha 形状或像素内容不准确。典型表现是刘海被额头盖住、
脖子像断开、头饰消失、图层边缘露出方形边界。下面两张图是实际例子。

![26 个语义图层的 alpha 网格，可以看到每层负责哪个部位](examples/screenshots/layers-grid.png)

*分层结果。每个格子是一个图层的 alpha 蒙版。*

![同一位置的三个版本对比：原图、修之前、修之后](examples/screenshots/layer-fix-example.png)

*脖子区域的修复对比。左为原图，中间是修之前（脖子下半段被衣领盖住），右边是修完的结果。*

修这类问题的原则是**改那一层本身**，或者**调整层的先后顺序**。
不要在顶层盖一张原图遮住：静态渲染看着没问题，但模型一动，
那个大图层会被拉伸变形，整个头都会歪。

### 先定位，再动手

`probe_points.py` 取原图上的一个点，逐个层查看谁覆盖了它、那一层的像素与原图差多少。

```bash
python pipeline/probe_points.py <layers.json> <原图.png> \
  --points "脖子正中:640,520;刘海中间:640,330;蝴蝶结中心:640,60"
```

根据结果分三种情况处理：

| 情况 | 含义 | 处理 |
|---|---|---|
| 某层像素接近原图 | 内容在这一层里是正确的 | 只修这一层的形状或顺序，不需要补像素 |
| 该层像素与原图差很多 | 这一层在这里盖住了别的东西 | 把这块从它的 alpha 里去掉，让位于它下方（z 序更低）的正确图层露出来 |
| 没有任何层覆盖 | 内容真的被丢弃了 | 从原图取像素，填回本该承载它的那一层 |

### 修复工具

| 脚本 | 用途 |
|---|---|
| `probe_points.py` | 按点诊断内容归属（只读，先跑它） |
| `trim_layer_by_skin.py` | 按与原图的内容一致性修剪某层 alpha |
| `extract_ornament_by_color.py` | 按颜色把丢失的部件提取成一层 |
| `promote_layer_to_top.py` | 调整层序、挖掉指定层占用的区域、羽化边缘 |
| `rebuild_layer_from_source.py` | 用原图重建某一层的形状与像素 |
| `reskin_layer_from_source.py` | 只替换某一层的颜色，alpha 不动 |
| `find_dropped_pixels.py` | 找出原图中有、但没有任何层覆盖的内容 |
| `clip_layers_by_source.py` | 用原图剪掉层里越界的部分 |
| `erase_watermark.py` | 抹掉生图工具的水印 |

### 几条规则

**判断某块内容属于哪一层，用内容一致性，不要用颜色类别。**
"偏蓝即头发"会把浅蓝灰色的衣领立领一起剪掉，脖子就露不出来。
换成比较"该层像素与原图的差异"之后就能分清。

**清理掩码不要用开运算。**
开运算会在边界啃出不规则斑块，还会把脖子这类细结构削细。
用中值滤波，加上只删除面积过小的连通块。

**能用形状就不要用矩形框。**
矩形框的直线边一定会穿过头发或脸，成品上会露出矩形边。

![两种取法的对比：矩形框会带进整块背景，按形状取则贴合部件](examples/screenshots/mask-shape-vs-rect.png)

*同一个头饰的两种取法。上边用矩形框，下边按颜色取形状。*

**验收要在深色或彩色背景上做。**
白底渲染图看不出镂空，因为白洞在白底上不可见。换成深色背景之后
才发现白色蕾丝和袜子被误剪掉了一大块。

**生成时不要用 `cel shading`。**
它会让画面显得廉价，换成 `soft shading`、`gradient shading`，
再加上发丝高光、环境光遮蔽和边缘光，观感会好很多。完整的提示词见
[千问生图提示词](docs/千问生图提示词-20260922.md)。

---

## 实测数据

环境：RTX 4070 Laptop（8 GB 显存）/ 16 GB 内存 / Windows 11。
下表每个数字都标了出处，采集时间是 2026-09-20 到 2026-09-22。

| 指标 | 数值 | 出处 |
|---|---|---|
| 生成立绘（hires 1.5 倍） | 25 到 35 秒每张 | `docs/立绘生成-5轮迭代实录.md` |
| 分层 @1024 | 411 秒；另一次记录 454 秒 | `docs/繁复路线-画质突破与分层极限.md`、`docs/链路实测报告.md` |
| 分层 @1280（模型热机且内存空闲） | 74 秒 | `docs/繁复路线-画质突破与分层极限.md` |
| 分层（可用内存掉到 1 到 2 GB 时） | 同样一张图拖到 15 分钟以上 | `docs/问题排查报告-20260922.md` |
| 峰值显存 | 6.5 GB / 8 GB | `docs/链路实测报告.md` |
| 输出图层数 | 23 层 | `docs/链路实测报告.md` |
| PSD2Live 绑定 | 6 秒，纯 CPU | `docs/链路实测报告.md` |
| 画布加倍后的图集页数 | 3 页变 21 页 | `pipeline/compose_psd.py` 注释 |
| 被丢弃的内容（Q 版立绘） | 6% | `pipeline/find_dropped_pixels.py` |

`docs/链路实测报告.md` 记录的一次完整流程是：分层 7.5 分钟，加绑定 6 秒。

分层耗时对内存和显存状态非常敏感，上表的 74 秒是理想值。
`docs/问题排查报告-20260922.md` 里明确写了这一点，不要把它当成常规预期。

画布加倍（`--hires-scale 2`）之后，眼睛和嘴的贴图分辨率大约提高到 1.8 倍，
瞳孔从 82×98 变成 148×175，嘴从 52×15 变成 93×27。

---

## 限制

| 目标 | 可行性 |
|---|---|
| 生成的立绘观感接近商业皮套（即商业虚拟形象模型） | 可以 |
| 一键得到同等质量的可动模型 | 做不到 |

差别在于作画方式。商业皮套由画师按图层规范作画，例如 `eyelash` 只画上睫毛线；
而这条链路是从平面图反推图层，精细部件经常不准：单一颜色的立领能差 1 像素复原，
但睫毛、眉毛这类细结构常被整块丢掉，或者被相邻图层盖住。

**张嘴和闭眼这类多状态，自动流水线到不了。**
实测自动绑定的 `MouthOpen` 几乎推不动嘴；闭眼是把睁眼网格压扁，会塌成两条线。
正确做法是另做一套贴图，按参数切换，但这一步必须在 Live2D Cubism Editor 里手工完成，
PSD2Live 只支持"参数到网格变形"，没有多状态贴图的能力。

装饰性元素（飘带、光环、花环、翼状布片）会被合并进头发或衣服层，做成模型后会跟着头动。
提示词可以降低出现概率，但堵不干净。

突出于角色轮廓之外的头饰，例如头顶高高翘起的大蝴蝶结，会被当作背景装饰整块丢弃，
和拱门、花环被丢弃是同一个机制。`find_dropped_pixels.py` 可以量出丢失了多少内容，
Q 版立绘实测丢了 6%。

现实路径是 AI 生成加人工修图层。人工这部分的工具在本仓库的 `pipeline/` 里，
能自动化掉大部分，剩下真正需要手工的只有多状态贴图这一件事。

---

## 深入阅读

| 文档 | 内容 |
|---|---|
| [虚拟形象入门-从零讲起](docs/虚拟形象入门-从零讲起.md) | 什么是虚拟形象，行业怎么做，AI 能替代哪一步 |
| [链路实测报告](docs/链路实测报告.md) | 各环节的耗时、显存、参数实测 |
| [繁复路线-画质突破与分层极限](docs/繁复路线-画质突破与分层极限.md) | 画质调优与分层的上限 |
| [问题排查报告-20260922](docs/问题排查报告-20260922.md) | 一次完整的问题定位过程 |
| [Q版首轮实测报告-20260922](docs/Q版首轮实测报告-20260922.md) | Q 版立绘的完整跑通记录 |

---

## 仓库结构

```
pipeline/
  run_full.py                 一条龙
  build_avatar.py             分层结果 → 模型 → 装进 VTS
  compose_psd.py              分层结果 → 合规 PSD
  prep_source.py              去背景、裁边
  face_pass.py                脸部单独分层
  test_seethrough.py          走 ComfyUI API 跑分层
  vts_load_model.py           用 VTS API 加载模型

  # 分层画质诊断与修复
  probe_points.py             按点诊断内容归属
  trim_layer_by_skin.py       按内容一致性修剪层 alpha
  extract_ornament_by_color.py  按颜色提取丢失部件
  promote_layer_to_top.py     层序、挖区域、羽化
  rebuild_layer_from_source.py  用原图重建某层
  reskin_layer_from_source.py   只换某层颜色
  find_dropped_pixels.py      找出被丢弃的内容
  clip_layers_by_source.py    用原图剪掉越界部分
  erase_watermark.py          去水印

  # 生图与评估
  gen_*.py                    生图
  score_layers.py             图层质量评分（0-100）
  render_preview.py           成品图与图层网格
  bench_configs.py            参数对比实验
  diag_*.py  crop_*.py  overlay_layers.py  show_layer.py   各类诊断

patches/     上游补丁
docs/        实测报告、迭代记录、提示词
examples/    效果截图
```

---

## 许可与致谢

本项目代码使用 MIT 许可，不包含任何上游工具的代码或模型权重，详见 [THIRD_PARTY.md](THIRD_PARTY.md)。

| 上游 | 许可 |
|---|---|
| See-through | Apache 2.0 |
| PSD2Live | GPL v3（本项目仅调用其可执行文件） |
| ComfyUI-See-through | MIT |
| Animagine XL 4.0 | CreativeML Open RAIL++-M |

感谢 [See-through](https://github.com/shitagaki-lab/see-through)（Jian Lin 等，
*Single-image Layer Decomposition for Anime Characters*，ACM SIGGRAPH 2026）、
[PSD2Live](https://github.com/tsunehimatoi/psd2live) 和
[ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through)。
