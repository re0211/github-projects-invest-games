set -u
export PATH=/usr/bin:$PATH
cd "$(dirname "$0")"
one(){ gh api "repos/$1" --jq '"\(.full_name) | \(.stargazers_count) | \(.forks_count) | \(.license.spdx_id // "-") | \(.language // "-") | \(.pushed_at[0:10]) | \(.created_at[0:10]) | \(.description // "-" | .[0:110])"' 2>/dev/null || echo "$1 | ERR"; }
for r in \
 mksglu/context-mode addyosmani/agent-skills max-sixty/worktrunk alibaba/open-code-review \
 cloudflare/security-audit-skill microsoft/skills anthropics/knowledge-work-plugins \
 tigerless-labs/agent-memory tinyhumansai/openhuman FunplayAI/funplay-unity-mcp \
 IvanMurzak/Godot-MCP Donchitos/Claude-Code-Game-Studios wuyoscar/jev-skill sno-ai/sno-station \
 Clearailhc/clearai-dsh a86582751/dsh-nexttavern LuxUmbra697/DSH-Desktop \
 huangziyuan-general/dsh-novel-forge alexgetmancom/claudecut AngelCantugr/context-inspector \
 mawen0317/renpy-vn-engineering adrian-wulf/gamewache yi00it/blender-asset-mcp \
 vitas/dsh-model-pricing Devin-AXIS/jev-dsh-decision devagrawal09/jev-review axonel/axonel \
 wdobry/laya-playground lhlGitHub/threejs-architecture-effects madeye/dsh-session-cost \
 Lance-QwQ/DSH-SEP yzi1b/whale-craft cholf5/dsh-plugin-job-panel \
 ; do one "$r"; done
