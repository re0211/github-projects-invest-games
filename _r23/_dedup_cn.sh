#!/bin/bash
# usage: _dedup_cn.sh term1 term2 ...
cd D:/34498/Documents/github-projects-invest-games
for t in "$@"; do
  n=$(grep -icF "$t" index.html csdn-social-summary.md csdn-social-summary-v21.md csdn-social-summary-v20.md csdn-social-summary-v19.md csdn-social-summary-v18.md _r22/_r22_cn.md _r21/_r21_cn.md 2>/dev/null | awk -F: '{s+=$2} END{print s}')
  echo -e "$t\t$n"
done
