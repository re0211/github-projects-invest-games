#!/bin/bash
# usage: _dedupe.sh  (reads candidates from stdin, one per line, format owner/repo)
cd "d:/34498/Documents/github-projects-invest-games"
while read -r line; do
  [ -z "$line" ] && continue
  repo=$(echo "$line" | awk '{print $1}')
  base=$(echo "$repo" | sed 's#.*/##')
  hit=""
  # full owner/repo
  if grep -qiF "$repo" index.html csdn-social-summary.md csdn-social-summary-v36.md csdn-social-summary-v34.md csdn-social-summary-v33.md _r38/_r38_gh.md _r38/_r38_cn.md _r38/_r38_official.md 2>/dev/null; then hit="FULL"; fi
  if [ -z "$hit" ]; then
    if grep -qiF "$base" index.html csdn-social-summary.md csdn-social-summary-v36.md csdn-social-summary-v34.md csdn-social-summary-v33.md _r38/_r38_gh.md _r38/_r38_cn.md _r38/_r38_official.md 2>/dev/null; then hit="BASE"; fi
  fi
  if [ -n "$hit" ]; then echo "DROP($hit) $line"; else echo "KEEP       $line"; fi
done
