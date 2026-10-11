# -*- coding: utf-8 -*-
"""第三十九辑再补录（2026-10-12）：official 路收尾追加的 §八 里最有价值的 2 条。
同 insert_v43b_cards.py 结构，MARKER 不同，可独立运行。
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

SECTION_S3 = '<section id="s3"'
LAST_FOOTNOTE_MARK = '<div id="r1449"'
FIRST_NEW_FOOTNOTE = 1450
MARKER = "第四十三版再补录"

HEAD_OLD = [
    '第四十三版补录 2026-10-12',
    '共 1450 个项目',
    '第四十三版补录 2 项（均与上版零重复）',
]
HEAD_NEW = [
    '第四十三版补录 2026-10-12 · 第四十三版再补录 2026-10-12',
    '共 1453 个项目',
    '第四十三版补录 2 项 + 第四十三版再补录 3 项（均与上版零重复）',
]

CARDS = [
    dict(
        nid="rpm43c25",
        name="Cubism Core 官方合规口径 —— 「不在 GitHub 上发布」，这是那堵墙的官方答案",
        url="https://docs.live2d.com/zh-CHS/cubism-sdk-manual/cubism-core",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "合规")],
        plain="官方手册原文：**「根据 Live2D 专有软件许可协议，不在 GitHub 上发布 Cubism Core」**；适用协议为 **Live2D Proprietary Software License Agreement v2.1**（修订 2025-02-03），対象是 Cubism Core 与 Cubism MotionSync Core。",
        analogy="**追了十几轮的「Cubism Core 这堵墙」，官方给的是这句话**：不是技术拆不动，是**许可协议就不允许它出现在 GitHub 上**。"
                "所以社区那些项目只能「声明不打包 Core、由使用者自己去官方拿」——这不是偷懒，是**唯一合规的做法**。",
        warn="⚠️ 反过来说：任何号称「自带 Core / 免下载 SDK」的仓库，都该先怀疑它的合规性。",
        ext=(45, "45", "不是技术资产，是一条能省掉大量试错的边界陈述。"),
        use=(85, "85", "判断「某个项目为什么不能开箱即用」的依据；也解释了格式线工具为什么都停在只读。"),
        src="official 路 · docs.live2d.com/zh-CHS/cubism-sdk-manual/cubism-core 官方手册原文 · 2026-10-12 核对 · 信源 [1450]",
    ),
    dict(
        nid="rpm43c26",
        name="平台支持表 2026-09-29 更新 + ⚠️ 官方两处口径不一致（第三次撞到）",
        url="https://docs.live2d.com/en/cubism-sdk-manual/platform/",
        lang="官方", stars="—",
        tags=[("t-ok", "官方"), ("t-make", "引擎")],
        plain="官方平台支持表 2026-09-29 更新：Unreal Engine 行新增 **macOS / Android / iOS**（beta2 前仅 Windows）；Native 含 **HarmonyOS**；Unity 含 WebGL 与 HarmonyOS（注：需 **Tuanjie / 团结引擎**，即 Unity 中国版）；Java 支持 Android 5.0–14.0。",
        analogy="⚠️ **同一件事，官方两个地方说法不一样**：GitHub 仓库的 README 至今写未来时「Cubism 5 SDK for Native R2 后支持**将要**终止」，"
                "而官方手册平台表已改成完成态「R2 之后**已终止**」并给了确切日期 **2024-12-19** —— README 是没同步的旧文案。"
                "这是**索引站第三次撞到官方口径打架**；结论：**以官方手册为准，别信仓库 README**。",
        warn="⚠️ 另一个易混点：官方 6 个 SDK 里的「Cubism SDK for **Cocos Creator**」与「**Cocos2d-x**」是两个不同的东西，别混。",
        ext=(50, "50", "平台表是选型时唯一该看的权威表；「以手册为准」是可复用的判据。"),
        use=(70, "70", "做引擎选型时直接查这张表；顺带学会一条：官方自己的 README 也会过期。"),
        src="official 路 · docs.live2d.com/en/cubism-sdk-manual/platform 官方手册 · 2026-09-29 更新 · 2026-10-12 核对 · 信源 [1451]",
    ),
    dict(
        nid="rpm43c27",
        name="⚠️ CubismWebSamples（★393 / 121 forks）—— 官方组织整表扫描挖出来的漏网卡",
        url="https://github.com/Live2D/CubismWebSamples",
        lang="官方", stars="393",
        tags=[("t-ok", "官方"), ("t-make", "工具"), ("t-new", "新")],
        plain="**官方组织里星最高的仓库（★393 / 121 forks）—— 却漏了整整十二辑**。`gh api orgs/Live2D/repos` 整表实取共 **18 个**仓库，按 ★ 排：CubismWebSamples **393** / CubismUnityComponents 264 / "
              "CubismNativeFramework 264 / CubismNativeSamples 239 / CubismWebFramework 237 / CubismViewer 46（2018 停） / "
              "CubismAndroidLiveWallpaper 45（2021 停） / CubismUnrealEngineComponents 32（**2026-09-29**，印证 beta2）/ "
              "CubismJavaSamples 31 / **CubismSpecs 22（2026-08-05，格式规格文档）**/ CubismJavaFramework 16 / "
              "CubismWebMotionSyncComponents 11 / CubismCocosCreatorComponents 8（2023 停）/ **nizimaLIVEPluginAPI 6（2026-03-31）**。",
        analogy="**这是本轮最该记住的一条方法学教训**：连续十二辑都是「想到什么搜什么」，**从没整表扫过官方组织** —— "
                "结果 ★393 / 121 forks 的 `CubismWebSamples`（几乎所有 Web 接入的起点）**漏了整整十二轮**。"
                "同理 `CubismSpecs`（官方格式规格文档）也没进过索引，而你一直在追 moc3 格式。",
        warn="⚠️ 顺带纠一个错：子 agent 报的 `CubismMotionSyncPluginUnity/Native/Web` **三个名字都不对**，"
             "组织里真实存在的是 `CubismWebMotionSyncComponents`（★11 / 2025-03-27）。**子 agent 报的仓库名必须自己复核**。",
        ext=(80, "80", "「整表扫官方组织」应固化为每辑的固定动作；这张卡本身就是那份清单。"),
        use=(88, "88", "CubismWebSamples 是 Web 接入的事实起点；CubismSpecs 是格式线的官方规格。两个都该存。"),
        src="gh api 实测：CubismWebSamples ★393 / forks 121 / 许可 other / 推送 2026-04-02 · 组织整表 18 个仓库 2026-10-12 复核 · 信源 [1452]",
    ),
]

FOOTNOTES = [
    (1450, "https://docs.live2d.com/zh-CHS/cubism-sdk-manual/cubism-core", "Cubism Core 官方手册（合规口径）",
     "official 路 · 原文「**根据 Live2D 专有软件许可协议，不在 GitHub 上发布 Cubism Core**」；"
     "适用 EULA = Live2D Proprietary Software License Agreement **v2.1（修订 2025-02-03）**，対象 Core + MotionSync Core"),
    (1451, "https://docs.live2d.com/en/cubism-sdk-manual/platform/", "官方平台支持表（2026-09-29 更新）",
     "official 路 · Unreal 行新增 **macOS / Android / iOS**（beta2 前仅 Windows）；Native 含 HarmonyOS；Unity 含 WebGL 与 HarmonyOS（需团结引擎）；"
     "⚠️ **官方口径不一致第三例**：GitHub README 仍写未来时「will be ended」，手册已改完成态「**was terminated after** Native R2」并给日期 **2024-12-19**"),
    (1452, "https://github.com/Live2D/CubismWebSamples", "Live2D/CubismWebSamples（★393）+ 官方组织全表（18 个仓库）",
     "gh api orgs/Live2D/repos 整表实取 2026-10-12 · ★ 排序：CubismWebSamples **393** / UnityComponents 264 / NativeFramework 264 / "
     "NativeSamples 239 / WebFramework 237 / UnrealEngineComponents 32（2026-09-29）/ **CubismSpecs 22（格式规格）** / WebMotionSyncComponents 11 / "
     "**nizimaLIVEPluginAPI 6** · ⚠️ 十二辑未整表扫过，★393 的基础件漏了十二轮"),
]


def b(s):
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)


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
           plain=b(c["plain"]), analogy=b(c["analogy"]), extra=b(extra),
           ew=c["ext"][0], en=c["ext"][1], ev=b(c["ext"][2]),
           uw=c["use"][0], un=c["use"][1], uv=b(c["use"][2]), src=c["src"])


def main():
    src = open(HTML, encoding="utf-8").read()

    if MARKER in src:
        print("已存在%s，跳过（幂等）" % MARKER)
        return 0

    bad = []
    for o in HEAD_OLD:
        if src.count(o) != 1:
            bad.append("页头锚点出现 %d 次（要求 1）：%s" % (src.count(o), o[:60]))
    for num, _u, _s, _m in FOOTNOTES:
        if ('id="r%s"' % num) in src:
            bad.append("信源 [%s] 已被占用" % num)
    # ⚠️ 查重不能只管 GitHub 仓库：本辑 3 张卡里有 2 张是官方手册 URL（docs.live2d.com），
    # 只做 slug 检测会让它们整条绕过查重 —— insert_guard_probe 的 N5 就是这么抓到的。
    # 所以：**所有 URL 先做完整串查重**，GitHub 仓库再加一层 slug 查重
    # （slug 太短会假命中，设 ≥8 字符下限：本辑的 github.com/Live2D 组织页 slug 只有 6 字符）。
    for c in CARDS:
        u = c.get("url") or ""
        if not u:
            continue
        if u in src:
            bad.append("URL 已存在，别重复登记：%s" % u)
        if "github.com/" in u:
            slug = u.split("github.com/")[-1].lower()
            if len(slug) >= 8 and slug in src.lower():
                bad.append("仓库已存在，别重复登记：%s" % u)

    si = src.find(SECTION_S3)
    if src.count(SECTION_S3) != 1:
        bad.append("%s 出现 %d 次" % (SECTION_S3, src.count(SECTION_S3)))
        ins = -1
    else:
        ins = si

    fi = src.find(LAST_FOOTNOTE_MARK)
    if src.count(LAST_FOOTNOTE_MARK) != 1:
        bad.append("最后一条脚注标记出现 %d 次" % src.count(LAST_FOOTNOTE_MARK))
        fend = -1
    else:
        fend = src.find("</div>", fi)
        fend = -1 if fend < 0 else fend + len("</div>")

    if bad or ins < 0 or fend < 0:
        for x in bad:
            print("❌ " + x)
        print("未改动 index.html")
        return 1

    desc = ('第三十九辑再补录（3 项）：**① Cubism Core 的官方合规口径** —— 官方手册原文'
            '「根据 Live2D 专有软件许可协议，不在 GitHub 上发布 Cubism Core」，这是追了十几轮的那堵墙的**官方答案**：'
            '不是技术拆不动，是许可不允许；'
            '**② 平台支持表 2026-09-29 更新** —— Unreal 行新增 macOS / Android / iOS，'
            '并撞到**官方两处口径不一致的第三例**（GitHub README 写未来时、官方手册已改完成态），结论是**以手册为准**；'
            '**③ 官方组织全表（18 个仓库）** —— 十二辑从没整表扫过，`CubismWebSamples`（★393 / 121 forks）'
            '和 `CubismSpecs`（官方格式规格）因此漏了整整十二轮。')

    block = ['    <div class="group" data-page-node-id="rpm43cg">',
             '      <div class="group-title" data-page-node-id="rpm43cgt">🆕 第四十三版再补录 · Core 那堵墙的官方答案 + 平台表更新 + 官方组织全表（3 项）</div>',
             '      <p class="sec-desc" data-page-node-id="rpm43cgd">' + desc + '</p>',
             '']
    for c in CARDS:
        block.append(render_card(c))
    block.append('    </div>')
    block.append('')

    # ⚠️ 顺序同 v43：先插位置靠后的脚注，再插位置靠前的卡片组
    notes = []
    for num, url, slug, meta in FOOTNOTES:
        notes.append('      <div id="r%s" data-page-node-id="rpm43cr%s">[%s] <a href="%s" '
                     'target="_blank" data-page-node-id="rpm43cra%s">%s</a> — %s</div>'
                     % (num, num, num, url, num, slug, meta))
    src = src[:fend] + "\n" + "\n".join(notes) + src[fend:]
    src = src[:ins] + "\n".join(block) + "\n" + src[ins:]

    for o, n in zip(HEAD_OLD, HEAD_NEW):
        if src.count(o) != 1:
            print("二次校验失败：页头锚点 %s 出现 %d 次" % (o[:40], src.count(o)))
            return 1
        src = src.replace(o, n)

    open(HTML, "w", encoding="utf-8").write(src)
    print("✅ 已插入 %s：%d 张卡 + %d 条脚注（[%d]-[%d]）"
          % (MARKER, len(CARDS), len(FOOTNOTES), FIRST_NEW_FOOTNOTE, FIRST_NEW_FOOTNOTE + len(FOOTNOTES) - 1))
    print("   页头：1450 → 1452 项；卡片 1433 → %d" % (1433 + len(CARDS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
