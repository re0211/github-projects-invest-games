#!/bin/bash
# usage: _dedup.sh term1 term2 ...
cd D:/34498/Documents/github-projects-invest-games
for t in "$@"; do
  n=$(grep -icF "$t" index.html csdn-social-summary.md csdn-social-summary-v21.md csdn-social-summary-v20.md 2>/dev/null | awk -F: '{s+=$2} END{print s}')
  echo -e "$t\t$n"
done
