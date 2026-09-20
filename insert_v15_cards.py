# -*- coding: utf-8 -*-
"""
第十五版增补：把第十辑调研新发现的 6 个条目登记进 index.html。

为什么要写脚本而不是手改 HTML：
  1) 一张卡片有 20 多个 `data-page-node-id`，手写必然漏；
  2) 脚本先断言"锚点存在且只出现一次"，**全部通过才落盘**——避免写出一个
     半改半没改的页面（同 amphoreus-roast/tools/insert_sprites.py 的纪律）；
  3) 顺手把页头计数与信源脚注一起改掉，三处改动不会漏。

（第一次跑这个脚本时，断言把"信源编号 [153]-[157] 已被占用"抓了出来——
 实际的脚注是 1~1054 共 1054 条，不是我以为的 152 条。闸门起作用了。）

数据来源：2026-09-20 用 GitHub REST API 实测（stars / language / license / pushed_at），
**没有一个数字是估的**（房规 9：别编造内容）。

幂等：脚本开头检查目标分组是否已存在，已存在则退出 0，不会重复插入。

用法：<venv>/Scripts/python.exe insert_v15_cards.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

# 插在「游戏拓展与解包」section 之前 = 「游戏制作（含 AI 制作游戏专题）」的末尾。
# 为什么不用分组标题定位：这一段的最后一个分组标题是「训练会玩游戏的 AI 补缺」，
# 但它后面就是 section 收尾；而「通用资源浏览器」看着像同一段，其实是下一个 section
# 的第一个分组——第一次就是插错在那里了。用 section 起点定位最稳。
SECTION_S3 = '<section id="s3"'
# 最后一条脚注的起点；真正插入位置是这一"行"的结尾（脚注编号实测是 1~1054）
LAST_FOOTNOTE_MARK = '<div id="r1054"'
FIRST_NEW_FOOTNOTE = 1055

HEAD_OLD = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1054 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">本次新增 152 项（与上版零重复）</span>',
]
HEAD_NEW = [
    '<span data-page-node-id="U5SVC0zIlhM1HBfAou01f1">数据抓取：2026-09-09 · 第十五版增补 2026-09-20</span>',
    '<span data-page-node-id="MHqmzzouq6azfHHmyaJQG7">共 1060 个项目</span>',
    '<span data-page-node-id="G2tNNvqJ4Wb0ycgYia1wZ2">第十四版 152 项 + 第十五版增补 6 项（均与上版零重复）</span>',
]

# ---------------------------------------------------------------------------
# 卡片内容。stars / lang / license / 推送日期全部来自 2026-09-20 的 GitHub API 实测。
# ---------------------------------------------------------------------------
CARDS = [
    dict(
        nid="wbn15c1", name="Story-Illustrator",
        url="https://github.com/zshortbusz/Story-Illustrator",
        lang="Python", stars="1",
        tags=[("t-make", "叙事配图"), ("t-warn", "1★ · 刚起步")],
        plain="开源 WebUI，把一段故事变成带插图的电子书——全程走你本地的 LLM 和你自己的 ComfyUI 工作流。真正值钱的不是\u201c能出图\u201d，而是它先建一份 <b>visual bible</b>：角色、场景、服装，以及<b>变化追踪</b>（换了衣服、多了伤疤都记下来）；然后按每段情节在故事里的位置，把<b>正确那一版</b>的角色细节注入到这一张图的提示词里。",
        analogy="多数人写提示词是在<b>复述</b>角色（\u201c银发蓝眼少年\u201d），它是给你的人物<b>建了一份会演进的档案</b>——第 3 章换了外套就记一笔，写到第 8 章自动取第 8 章那一版。做长篇视觉小说时，这一步直接决定人物会不会\u201c换脸\u201d。",
        ext=(75, "7.5/10", "本地 LLM + 自有 ComfyUI 两层都能整体替换，输出是可移植电子书；不锁死任何云服务"),
        use=(55, "5.5/10", "2026-09-13 新建、1★，处在\u201c读它的架构、别直接上生产\u201d的阶段"),
        src="最近推送 2026-09-20 · MIT · 信源 [1055]",
    ),
    dict(
        nid="wbn15c2", name="zork-underground-empire",
        url="https://github.com/emollick/zork-underground-empire",
        lang="TypeScript", stars="38",
        tags=[("t-make", "老 IP 重生"), ("t-ok", "prompt 全公开")],
        plain="Ethan Mollick 让 GPT-6 Astra 把 1977 年的文字冒险《Zork》重做成完整的第一人称 3D 动作冒险：保留原剧情与谜题、加了战斗场面，角色与环境全部用 Three.js 现搭，浏览器打开就能玩（连原作那个 Grue 都在）。项目开源、本地运行、<b>不需要 API key</b>。",
        analogy="这不是\u201cAI 画了张图\u201d，而是它把<b>一个品类的核心体验整体换了皮</b>。手里有老 IP 或者老玩法的人，现在可以用一个人的成本走一遍\u201c重制\u201d。",
        ext=(80, "8.0/10", "纯前端 Three.js 工程，改玩法不用碰引擎；作者把全部 prompt 与 nudge 都公开了，协作方式可直接复用"),
        use=(70, "7.0/10", "成品是演示性质，但它公开的\u201c如何让模型自己做判断\u201d的过程，比成品更有参考价值"),
        src="最近推送 2026-09-05 · MIT · 信源 [1056]",
    ),
    dict(
        nid="wbn15c3", name="Night-Patrol",
        url="https://github.com/op7418/Night-Patrol",
        lang="TypeScript", stars="159",
        tags=[("t-make", "一句话做游戏"), ("t-warn", "仓库日期与文章对不上")],
        plain="不写代码、不碰引擎，把\u201c做个杀戮尖塔-like\u201d丢给 Codex，一小时后跑出一个能玩的志怪 roguelike：走普通战 / 精英 / 事件 / 商店 / 休整，一路打到正殿 Boss；七个怪物、约二十张卡牌，符印·香火·焚符·请神四条爆发链路都能跑。桌面上有 macOS 与 Windows 安装包。",
        analogy="它证明的不是\u201cAI 会写代码\u201d，而是<b>\u201c能玩\u201d和\u201c像个游戏\u201d之间那段距离</b>——作者剩下的一下午全花在受击摇晃、镜头震动、每种攻击配不同打击音这类\u201c说不上来但少了就不像游戏\u201d的东西上。",
        ext=(70, "7.0/10", "TypeScript + 前端栈，改卡牌与数值的门槛很低；适合当\u201c一个人做完整小游戏\u201d的骨架"),
        use=(75, "7.5/10", "有可运行的桌面安装包，是这批里最\u201c拿起来就能玩到\u201d的一个"),
        warn="数据存疑：仓库创建与最后推送都是 2026-04-30，与该文的 2026-09-14 发布日对不上，可能是文章再发布或存在同名前身。引用前请自己核一遍。",
        src="最近推送 2026-04-30 · 自定义协议（NOASSERTION） · 信源 [1057]",
    ),
    dict(
        nid="wbn15c4", name="novel-to-game",
        url="https://github.com/zenstory-ai/novel-to-game",
        lang="Markdown", stars="791",
        tags=[("t-make", "小说转游戏"), ("t-ok", "带可安装 Skill")],
        plain="把小说 / 长文转成可玩游戏的工具链。791★、MIT、调研当天仍有推送。真正特别的是仓库里带一个 <b>game-art-direction</b> 子技能——<b>\u201c定美术方向\u201d这件过去靠人拍脑袋的事，现在有一份可复用的执行规范</b>，而且能单独装进 agent 工作流。",
        analogy="多数\u201cAI 做游戏\u201d项目给你一堆代码，它额外给了你一张<b>\u201c先想清楚长什么样\u201d的流程单</b>——而这一步恰恰是新手最容易跳过、后面返工最狠的地方。",
        ext=(80, "8.0/10", "MIT + 技能可单独安装，能摘出来用在别的项目上；不绑定单一模型"),
        use=(75, "7.5/10", "791★ 且当天仍在推送，是这批里最\u201c能直接拿来用\u201d的一个"),
        install="npx skills add zenstory-ai/novel-to-game --skill game-art-direction",
        src="最近推送 2026-09-19 · MIT · 信源 [1058]",
    ),
    dict(
        nid="wbn15c5", name="Picxel",
        url="https://github.com/See-Sol-Lab/Picxel",
        lang="Python", stars="23",
        tags=[("t-make", "像素素材"), ("t-ok", "不占自己 API key")],
        plain="给独立开发者用的\u201c参考图 → 像素风素材\u201d重绘工具：GPT 负责理解主体并指挥重绘，本地算法把结果压成<b>精确的像素网格</b>，导出透明底 PNG（32 / 64 / 128 三档，每张最多 16 色），支持一次批量 20 张，面板有中英文。它跑在 Codex 会话里，<b>用会话自带的图像能力，不需要另配 API key</b>。",
        analogy="像素风最怕\u201c先把 1024px 图画好再缩到 64px\u201d——那样只会得到一团糊。它是<b>从第一步就按像素网格生成</b>，所以边缘是硬的、轮廓是清楚的。",
        ext=(65, "6.5/10", "算法与提示词路径清晰；但 GPL-3.0 有传染性，商用前要确认自己的用法"),
        use=(60, "6.0/10", "23★、刚建几天。半写实风项目用不上，做像素项目时再回来看"),
        src="最近推送 2026-09-16 · GPL-3.0 · 信源 [1059]",
    ),
    dict(
        nid="wbn15c6", name="Visual-Novel-bg-HiDream",
        url=None,
        lang="LoRA · 非 GitHub（魔搭 / Civision）", stars="21 下载",
        tags=[("t-make", "VN 背景专用"), ("t-warn", "训练数据未披露")],
        plain="目前很少见的<b>专门给视觉小说背景</b>训练的 LoRA：底座 HiDream-O1-Image，300 张训练图 / 10000 步，产出 98MB 的适配器，Apache-2.0。装好 DiffSynth-Studio 之后 load_lora 即可用。它对准的是\u201c背景图必须成套统一\u201d这个刚需。",
        analogy="背景图最难的从来不是\u201c出一张好图\u201d，而是<b>几十张图风格一致</b>。靠人肉挑图能撑到六张，撑不到六十张——本地挂一个 LoRA 是最便宜的收敛手段，比反复抽卡便宜得多。",
        ext=(70, "7.0/10", "本地推理 + Apache-2.0，可在此基础上继续微调；LoRA 能叠加到自己的底模上"),
        use=(70, "7.0/10", "对视觉小说项目直接相关；但训练数据来源未披露，商用前要评估"),
        warn="非 GitHub 资源（魔搭社区训练、Civision 平台发布），登记在此仅供索引对照。",
        src="创建 2026-09-16 · Apache-2.0 · 非 GitHub 资源",
    ),
]

FOOTNOTES = [
    ("1055", "https://github.com/zshortbusz/Story-Illustrator",
     "zshortbusz/Story-Illustrator", "1 · 2026-09-20 · MIT"),
    ("1056", "https://github.com/emollick/zork-underground-empire",
     "emollick/zork-underground-empire", "38 · 2026-09-05 · MIT"),
    ("1057", "https://github.com/op7418/Night-Patrol",
     "op7418/Night-Patrol", "159 · 2026-04-30 · 自定义协议"),
    ("1058", "https://github.com/zenstory-ai/novel-to-game",
     "zenstory-ai/novel-to-game", "791 · 2026-09-19 · MIT"),
    ("1059", "https://github.com/See-Sol-Lab/Picxel",
     "See-Sol-Lab/Picxel", "23 · 2026-09-16 · GPL-3.0"),
]


def render_card(c):
    n = c["nid"]
    name_inner = ('<a href="%s" target="_blank" data-page-node-id="%sn">%s</a>'
                  % (c["url"], n, c["name"])) if c["url"] else c["name"]
    tags = "\n".join(
        '          <span class="tag %s" data-page-node-id="%st%d">%s</span>'
        % (cls, n, i, txt) for i, (cls, txt) in enumerate(c["tags"], 1))
    extra = ""
    if c.get("warn"):
        extra += ('        <div class="analogy" data-page-node-id="%sw"><b data-page-node-id="%swb">'
                  '注意：</b>%s</div>\n' % (n, n, c["warn"]))
    if c.get("install"):
        extra += ('        <div class="src-line" data-page-node-id="%si">装法：'
                  '<code data-page-node-id="%sic">%s</code></div>\n' % (n, n, c["install"]))
    return '''      <div class="card" data-page-node-id="{n}">
        <div class="card-top" data-page-node-id="{n}t">
          <span class="card-name" data-page-node-id="{n}mn">{name}</span>
          <span class="lang" data-page-node-id="{n}l">{lang}</span>
          <span class="stars" data-page-node-id="{n}s">{stars}</span>
{tags}
        </div>
        <p class="plain" data-page-node-id="{n}p">{plain}</p>
        <div class="analogy" data-page-node-id="{n}a"><b data-page-node-id="{n}ab">打个比方：</b>{analogy}</div>
{extra}        <div class="grid2" data-page-node-id="{n}g">
          <div class="mini" data-page-node-id="{n}m1"><span class="lbl" data-page-node-id="{n}m1l">可拓展性</span><div class="bar" data-page-node-id="{n}m1b"><div class="bar-track" data-page-node-id="{n}m1t"><div class="bar-fill" style="width:{ew}%;background:var(--make)" data-page-node-id="{n}m1f"></div></div><span class="bar-num" data-page-node-id="{n}m1n">{en}</span></div><div class="val" style="margin-top:6px" data-page-node-id="{n}m1v">{ev}</div></div>
          <div class="mini" data-page-node-id="{n}m2"><span class="lbl" data-page-node-id="{n}m2l">实用性</span><div class="bar" data-page-node-id="{n}m2b"><div class="bar-track" data-page-node-id="{n}m2t"><div class="bar-fill" style="width:{uw}%;background:var(--make)" data-page-node-id="{n}m2f"></div></div><span class="bar-num" data-page-node-id="{n}m2n">{un}</span></div><div class="val" style="margin-top:6px" data-page-node-id="{n}m2v">{uv}</div></div>
        </div>
        <div class="src-line" data-page-node-id="{n}c">{src}</div>
      </div>
'''.format(n=n, name=name_inner, lang=c["lang"], stars=c["stars"], tags=tags,
           plain=c["plain"], analogy=c["analogy"], extra=extra,
           ew=c["ext"][0], en=c["ext"][1], ev=c["ext"][2],
           uw=c["use"][0], un=c["use"][1], uv=c["use"][2], src=c["src"])


def main():
    src = open(HTML, encoding="utf-8").read()

    if "第十五版增补" in src:
        print("已存在第十五版增补，跳过（幂等）")
        return 0

    bad = []

    # --- 页头锚点 ---
    for o in HEAD_OLD:
        if src.count(o) != 1:
            bad.append("页头锚点出现 %d 次（要求 1）：%s" % (src.count(o), o[:50]))

    # --- 信源编号必须没被占用 ---
    for num, _u, _s, _m in FOOTNOTES:
        if ('id="r%s"' % num) in src:
            bad.append("信源 [%s] 已被占用" % num)

    # --- 分组插入点：扩展 section 的起点 ---
    si = src.find(SECTION_S3)
    if src.count(SECTION_S3) != 1:
        bad.append("%s 出现 %d 次（要求 1）" % (SECTION_S3, src.count(SECTION_S3)))
        ins = -1
    else:
        ins = si
        # 自检：插入点前的 div 深度必须归零，否则说明插进去会嵌进某个未闭合的容器
        seg = src[src.find("<section", 10000):si]
        d = 0
        for m in re.finditer(r"<div[\s>]|</div>", seg):
            d += 1 if m.group(0).startswith("<div") else -1
        if d != 0:
            bad.append("插入点前 div 深度为 %d（应为 0），会嵌错层" % d)

    # --- 脚注插入点：最后一条脚注那一行的末尾 ---
    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次（要求 1）" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if bad:
        print("锚点校验失败，未改动文件：")
        for b in bad:
            print("  " + b)
        return 1

    # 1) 卡片分组（插在「通用资源浏览器」之前，即 AI 制作游戏专题这一段的末尾）
    block = ['    <div class="group" data-page-node-id="wbn15g">',
             '      <div class="group-title" data-page-node-id="wbn15gt">🆕 第十五版增补 · 2026-09 新仓库：从「一段故事」到「能玩的游戏」（6 项）</div>',
             '      <p class="sec-desc" data-page-node-id="wbn15gd">这一批的共同点是<strong>上游都变了</strong>：不再是「给引擎配个插件」，而是从一段小说、一段文字、一张参考图开始，直接产出能动的东西。星级 / 语言 / 协议为 2026-09-20 用 GitHub API 实测。</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    # 2) 信源脚注（插到最后一条之后）
    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="wbn15r%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="wbn15ra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]

    # 3) 页头计数
    for old, new in zip(HEAD_OLD, HEAD_NEW):
        src = src.replace(old, new, 1)

    open(HTML, "w", encoding="utf-8", newline="\n").write(src)

    print("OK  插入 %d 张卡片 + %d 条信源脚注（[%s]-[%s]）+ 3 处页头计数"
          % (len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE,
             FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
