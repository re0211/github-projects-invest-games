# -*- coding: utf-8 -*-
"""诊断：每条脚注 [N] 当前落在哪个容器里（card / srcs / other）。
用法：python _r39/diag_footnote_container.py
"""
import re, os, collections

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "index.html")

lines = open(HTML, encoding="utf-8").read().split("\n")

stack = []          # (class, id, lineno)
info = {}           # N -> (lineno, container)
depth_drift = []    # 记录 card 深度异常

for lineno, line in enumerate(lines, 1):
    for m in re.finditer(r'<div\b([^>]*)>|</div>', line):
        tok = m.group(0)
        if tok == "</div>":
            if stack:
                stack.pop()
            continue
        attrs = m.group(1) or ""
        cls = re.search(r'class="([^"]*)"', attrs)
        did = re.search(r'id="([^"]*)"', attrs)
        c = cls.group(1) if cls else ""
        d = did.group(1) if did else ""
        stack.append((c, d, lineno))
        if re.fullmatch(r"r\d+", d):
            anc = [x[0] for x in stack[:-1]]           # 祖先
            in_card = any("card" in a.split() for a in anc)
            in_srcs = any("srcs" in a.split() for a in anc)
            container = "card" if in_card else ("srcs" if in_srcs else "other")
            info[int(d[1:])] = (lineno, container)

print("脚注总数:", len(info))
cnt = collections.Counter(v[1] for v in info.values())
print("容器分布:", dict(cnt))

for want in ("card", "srcs", "other"):
    ns = sorted(n for n, v in info.items() if v[1] == want)
    if not ns:
        continue
    # 归并成区间
    ranges, s, p = [], ns[0], ns[0]
    for n in ns[1:]:
        if n == p + 1:
            p = n
        else:
            ranges.append((s, p)); s = p = n
    ranges.append((s, p))
    print(f"\n[{want}] {len(ns)} 条，区间 {len(ranges)} 段：")
    for a, b in ranges:
        print(f"   {a}-{b}  (行 {info[a][0]} … {info[b][0]})")
