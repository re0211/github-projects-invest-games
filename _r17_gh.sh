set -u
export PATH=/usr/bin:$PATH
cd "$(dirname "$0")"
F="fullName,stargazersCount,language,pushedAt,description,forksCount,createdAt,license"
run(){ echo "### $1"; gh search repos "$1" --sort stars --limit 10 --json $F 2>/dev/null | python -c "
import json,sys
try: d=json.load(sys.stdin)
except: d=[]
for r in d: print('%s | %s | %s | %s | %s' % (r['fullName'], r['stargazersCount'], (r.get('license') or {}).get('key','-'), r['pushedAt'][:10], (r.get('description') or '')[:100]))
"; echo ""; }
# —— 用户点名的五条线 ——
run "context engineering agent created:>2026-09-10"
run "vibe coding created:>2026-09-10"
run "deepseek harness created:>2026-08-01"
run "agent memory context created:>2026-09-10"
run "copilot vscode agent created:>2026-09-10"
run "claude code skills created:>2026-09-14"
run "context compaction LLM created:>2026-08-20"
run "AI game dev created:>2026-09-14"
run "game AI agent created:>2026-09-14"
run "prompt cache LLM created:>2026-09-01"
# —— 第十七辑新扩：Harness / 上下文 / IDE / 去 AI 味 / 发行 ——
run "harness llm created:>2026-09-01"
run "context window management created:>2026-09-01"
run "agent skill marketplace created:>2026-09-14"
run "AI slop detector created:>2026-09-01"
run "steam publishing tool created:>2026-08-01"
run "godot mcp pushed:>2026-09-18"
run "renpy tool pushed:>2026-09-10"
run "unity mcp pushed:>2026-09-18"
run "AI dialogue detection created:>2026-08-20"
run "spec driven development created:>2026-09-10"
run "AGENTS.md created:>2026-09-01"
run "subagent orchestration created:>2026-09-14"
run "token efficiency agent created:>2026-09-01"
run "interactive fiction AI created:>2026-09-14"
run "game design AI created:>2026-09-14"
