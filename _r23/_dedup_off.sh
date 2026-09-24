#!/bin/bash
# usage: _dedup_off.sh term1 term2 ...
cd D:/34498/Documents/github-projects-invest-games
for t in "$@"; do
  n=$(grep -icF "$t" index.html csdn-social-summary.md csdn-social-summary-v20.md csdn-social-summary-v21.md _r22/_r22_official.md _r22/_r22_gh.md _r22/_r22_cn.md 2>/dev/null | awk -F: '{s+=$2} END{print s+0}')
  echo -e "$t\t$n"
done
