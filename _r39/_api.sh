#!/bin/bash
for r in "$@"; do
  out=$(gh api "repos/$r" 2>&1)
  if echo "$out" | head -1 | grep -q "^{"; then
    echo "$out" | python -c "
import json,sys
d=json.load(sys.stdin)
lic=(d.get('license') or {}).get('spdx_id') or 'none'
print('%-60s star=%-7s lic=%-16s lang=%-14s created=%s pushed=%s updated=%s' % (d['full_name'], d['stargazers_count'], lic, d.get('language') or '-', d['created_at'][:10], d['pushed_at'][:10], d['updated_at'][:10]))
print('    desc:', (d.get('description') or '')[:160])
print('    home:', d.get('homepage') or '-', '| forks:', d.get('forks_count'), '| open_issues:', d.get('open_issues_count'), '| size:', d.get('size'))
"
  else
    echo "$r -> API_FAIL: $(echo "$out" | head -1 | cut -c1-120)"
  fi
done
