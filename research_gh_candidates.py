# -*- coding: utf-8 -*-
"""GitHub 候选调研引擎（跨平台资源梳理自动化的可复用部分）。

用途：为每一辑「跨平台资源梳理」跑 GitHub 这一路 ——
  gh search（多查询）→ 自动去重（对照 index.html）→ 相关性分档 → 输出候选短名单。

用法（在仓库根目录）：
    python research_gh_candidates.py                      # 跑内置查询集
    python research_gh_candidates.py --since 2026-09-14   # 改"新建时间下限"
    python research_gh_candidates.py --out _r17_short.txt # 改输出文件

产物：
  1) 标准输出 / --out 指定的 txt：按档位分组的候选短名单
  2) _gh_candidates.json：结构化候选（便于二次脚本处理）

踩坑记录（别再踩）：
  * `gh search repos --json` 的 fork 数字段名是 **`forksCount`**，不是 `forkCount`；
    写错会整条查询报 "Unknown JSON field" 并把结果静默变成 0 条（本脚本第一版就栽在这）。
  * 查询串把关键词与限定符写在**同一个参数**里最稳：`gh search repos "AI game created:>2026-09-14"`。
  * 本环境跑 gh 前建议 `export PATH=/usr/bin:$PATH`（PortableGit 缺 coreutils 的既有问题）。

相关性分档（tier）：
  GAME×AI —— 游戏 + AI 双命中（最优先）
  AI-dev  —— 只命中 AI 侧
  game    —— 只命中游戏侧
  other   —— 都没命中（仅当 star 足够大才留）

注意：**这不是查重工具**。它只能发现"已在 index.html 里"的重复；
"内容级重复"（新仓库但同一件事，或新 URL 但旧叙事）仍必须人工判 —— 见 mistakes/M-0001。
"""
import argparse
import json
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")

# gh search 支持的字段（写错字段名会让整条查询静默失败）
FIELDS = ("fullName,stargazersCount,language,pushedAt,description,"
          "forksCount,createdAt,license,isArchived")

# 查询模板：(关键词, 时间限定符)。{since} 会被 --since 替换。
QUERY_TEMPLATE = [
    ("AI game", "created:>{since}"),
    ("game AI", "created:>{since}"),
    ("MCP godot", "created:>{since}"),
    ("MCP unity", "created:>{since}"),
    ("visual novel", "created:>{since}"),
    ("AI NPC", "created:>{since}"),
    ("game engine", "created:>{since}"),
    ("interactive fiction", "created:>{since}"),
    ("godot", "created:>{since}"),
    ("renpy", "created:>{since}"),
    ("game mod", "pushed:>{since}"),
    ("LLM benchmark", "created:>{since}"),
    ("model comparison", "created:>{since}"),
    ("AI code review", "created:>{since}"),
    ("agent harness", "created:>{since}"),
    ("game asset", "created:>{since}"),
    ("game world model", "created:>{since}"),
    ("AI dialogue", "created:>{since}"),
    ("mcp server game", "created:>{since}"),
    ("sprite generator", "created:>{since}"),
]

GAME = re.compile(r"game|godot|unity|unreal|ren'?py|renpy|visual novel|\bvn\b|rpg|"
                  r"sprite|npc|narrative|interactive fiction|mod(ding)?\b|voxel|"
                  r"roguelike|shader|tilemap|engine", re.I)
AIDEV = re.compile(r"\bai\b|llm|agent|mcp|gpt|claude|gemini|qwen|deepseek|codex|"
                   r"prompt|harness|coding|eval(uation)?|benchmark|inference|"
                   r"diffusion|model", re.I)
# 已知噪音：awesome-list、面经、非主线领域
NOISE = re.compile(r"awesome-|roadmap|interview|leetcode|\bweb3\b|blockchain|"
                   r"crypto|trading|stock|quant", re.I)
# 同模板 SEO 农场的特征（2026-09 实测：十几个 *-dev.github.io 批量创建）
SEO_FARM = re.compile(r"-dev\.github\.io$|\.github\.io$", re.I)

TIER_RANK = {"GAME×AI": 2, "AI-dev": 1, "game": 1, "other": 0}


def run(q, qual, limit=15):
    full = "%s %s" % (q, qual)
    try:
        out = subprocess.run(
            ["gh", "search", "repos", full, "--sort", "stars",
             "--limit", str(limit), "--json", FIELDS],
            capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            sys.stderr.write("gh 返回非零（%s）：%s\n" % (full, out.stderr.strip()[:200]))
            return []
        return json.loads(out.stdout or "[]")
    except Exception as e:
        sys.stderr.write("ERR %s: %s\n" % (full, e))
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-09-14",
                    help="新建/推送时间下限（YYYY-MM-DD）")
    ap.add_argument("--out", default="_gh_candidates.txt")
    ap.add_argument("--json-out", default="_gh_candidates.json")
    ap.add_argument("--min-stars", type=int, default=8,
                    help="AI/game 单侧命中时的最低 star（双命中不看 star）")
    args = ap.parse_args()

    if not os.path.exists(HTML):
        print("找不到 index.html（%s）—— 查重无法进行" % HTML)
        return 1
    html = open(HTML, encoding="utf-8").read().lower()

    seen, order = {}, []
    for q, qual_tpl in QUERY_TEMPLATE:
        qual = qual_tpl.format(since=args.since)
        for r in run(q, qual):
            f = r.get("fullName", "")
            if not f:
                continue
            k = f.lower()
            if k in seen:
                seen[k]["q"].append(q)
                continue
            seen[k] = dict(
                f=f, s=r.get("stargazersCount", 0), l=r.get("language") or "-",
                p=(r.get("pushedAt") or "")[:10], c=(r.get("createdAt") or "")[:10],
                lic=(r.get("license") or {}).get("spdxId") or "-",
                fk=r.get("forksCount", 0), arch=r.get("isArchived", False),
                d=(r.get("description") or "").replace("\n", " "), q=[q])
            order.append(k)

    inidx, core, seofarm = 0, [], []
    for k in order:
        it = seen[k]
        blob = it["f"] + " " + it["d"]
        if it["f"].lower() in html:
            inidx += 1
            continue
        if SEO_FARM.search(it["f"]):
            seofarm.append(it)
            continue
        if it["arch"] or NOISE.search(blob):
            continue
        g, a = bool(GAME.search(blob)), bool(AIDEV.search(blob))
        it["g"], it["a"] = g, a
        it["tier"] = ("GAME×AI" if (g and a) else
                      "AI-dev" if a else "game" if g else "other")
        if it["tier"] == "other" and it["s"] < 100:
            continue
        if it["tier"] != "GAME×AI" and it["s"] < args.min_stars:
            continue
        core.append(it)

    core.sort(key=lambda x: (-TIER_RANK[x["tier"]], -x["s"]))
    lines = ["raw unique: %d  |  已在 index.html: %d  |  SEO 农场: %d  |  入短名单: %d\n"
             % (len(order), inidx, len(seofarm), len(core))]
    for it in core:
        lines.append("[%-8s] %s ★%d %s %s lic:%s fk:%d c:%s"
                     % (it["tier"], it["f"], it["s"], it["l"], it["p"],
                        it["lic"], it["fk"], it["c"]))
        lines.append("           %s" % (it["d"][:170] or "(no desc)"))
    if seofarm:
        lines.append("\n--- 疑似 SEO 农场（不收录，只登记）---")
        for it in seofarm[:25]:
            lines.append("  %s ★%d c:%s" % (it["f"], it["s"], it["c"]))

    text = "\n".join(lines)
    open(os.path.join(BASE, args.out), "w", encoding="utf-8").write(text)
    json.dump(core, open(os.path.join(BASE, args.json_out), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(text)
    print("\n→ 已写 %s 与 %s" % (args.out, args.json_out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
