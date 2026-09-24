#!/usr/bin/env bash
# 花叔生态 14 仓库「是否真人关注」核实 —— 看 fork / issue / PR / 外部参与者，不看 ★
# 判据：★ 可刷；fork、外部 issue、外部 PR、外部 contributor 才算真人关注
export PATH=/usr/bin:$PATH
OWNER=alchaincyf
REPOS="deepseek-harness-orange-book claude-code-orange-book 3d-vibe-coding-handbook darwin-skill deepseek-influence-report deepseek-v4-deep-dive h-book huasheng_editor huashu-design huashu-report huashu-skills karpathy-skill nuwa-skill zhangxuefeng-skill"
OUT=_r23/_huashu_probe.txt
: > "$OUT"
for r in $REPOS; do
  [ "$r" = "h-book" ] && r="hermes-agent-book"
  j=$(gh api "repos/$OWNER/$r" --jq '{stars:.stargazers_count,forks:.forks_count,subs:.subscribers_count,open_issues:.open_issues_count,created:.created_at,pushed:.updated_at,lic:(.license.spdx_id//"none"),lang:.language}' 2>/dev/null)
  if [ -z "$j" ]; then echo "$r | 404/不可达" >> "$OUT"; continue; fi
  # 外部参与者：最近 issue/PR 的作者里，非 owner 的人数
  ext_issue=$(gh api "repos/$OWNER/$r/issues?state=all&per_page=100" --jq '[.[]|select(.user.login!="'"$OWNER"'")|.user.login]|unique|length' 2>/dev/null)
  ext_pr=$(gh api "repos/$OWNER/$r/pulls?state=all&per_page=100" --jq '[.[]|select(.user.login!="'"$OWNER"'")]|length' 2>/dev/null)
  contrib=$(gh api "repos/$OWNER/$r/contributors?per_page=100&anon=false" --jq 'length' 2>/dev/null)
  echo "$r | $j | 外部issue作者=$ext_issue 外部PR=$ext_pr contributors=$contrib" >> "$OUT"
  sleep 0.3
done
cat "$OUT"
