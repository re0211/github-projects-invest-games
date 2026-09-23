set -u
export PATH=/usr/bin:$PATH
cd "$(dirname "$0")"
F="fullName,stargazersCount,language,pushedAt,description,forksCount,createdAt,license"
run(){ echo "### $1"; gh search repos "$1" --sort stars --limit 10 --json $F 2>/dev/null | python -c "
import json,sys
try: d=json.load(sys.stdin)
except: d=[]
for r in d: print('%s | %s | %s | %s | %s | %s' % (r['fullName'], r['stargazersCount'], r['forksCount'], (r.get('license') or {}).get('key','-'), r['pushedAt'][:10], (r.get('description') or '')[:90]))
"; echo ""; }
run "context engineering agent created:>2026-09-18"
run "agent skills created:>2026-09-18"
run "game engine MCP created:>2026-09-18"
run "visual novel AI created:>2026-09-10"
run "renpy created:>2026-09-10"
run "context window token created:>2026-09-18"
run "copilot agent vscode created:>2026-09-15"
run "deepseek harness plugin created:>2026-09-10"
run "llm benchmark evaluation created:>2026-09-15"
run "game dev AI agent pushed:>2026-09-20"
run "prompt caching agent created:>2026-09-15"
run "AI code review created:>2026-09-15"
run "agent sandbox orchestrator created:>2026-09-10"
run "memory agent markdown created:>2026-09-10"
run "git worktree agent created:>2026-09-01"
