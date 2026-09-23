set -u
export PATH=/usr/bin:$PATH
cd "$(dirname "$0")"
F="fullName,stargazersCount,language,pushedAt,description,forksCount,createdAt,license"
one(){ gh api "repos/$1" --jq '"\(.full_name) | \(.stargazers_count) | \(.forks_count) | \(.license.spdx_id // "-") | \(.language // "-") | \(.pushed_at[0:10]) | \(.created_at[0:10]) | \(.description // "-" | .[0:110])"' 2>/dev/null || echo "$1 | ERR"; }
for r in \
 deepseek-ai/deepseek-harness anywhere-labs/dsh-desktop awesome-dsh-plugin/awesome-dsh-plugin \
 dsh-tauri/deepseek-harness-desktop dsh-market/dsh-market zhu1090093659/dsh-web \
 qiz029/dscode yindf/taskfold kolawong/fast-compaction-dsh PlxloYzb/dsh-context-management \
 CooperZhuang/dsh-context-window SAXEM1997/specpowers \
 hi-godot/godot-ai Erodenn/godot-mcp-runtime NPGameDev/godot-mcp-toolkit aigengame/godot-agent \
 beckettlab/beckett-godot-mcp hatayama/unity-cli-loop cnfatal/rpycdec the-asind/RenPy-VisualEditor \
 DezFix/OctopusBridge liuyejinghong/game-design-review rakaascode/game-design-council \
 RomainYing/Game-design-theory GabrielBigardi/gamedev-ai-skills Thepizzapie/BuildersGate \
 GiampaoloConti/spellforge NoBrainNoGame/devgame \
 alchaincyf/3d-vibe-coding-handbook pliablepixels/gap-trap Xu123-Bob/Baize awarexone/AXguard \
 nmlemus/harness-token-efficiency prapaa-ai/evalix ARahim3/cachebeat 255308153/CtxGuard \
 SerenQi/llm-cache-gateway RedRobotKK/Replay handyutils/sctxx Waxmell114514/jev-compaction \
 YoadElkayam/windowkeeper beyondworks/castra \
 DefiTanjiro/ai-slop-detector LwkMoon/SlopScan doeixd/jev-pref \
 kerpopule/hermes-jev-skills Dicklesworthstone/skillranker riesaexe/r-doc GarvitAgrawal04/SENTINEL \
 nahid-sparktales/agent-dispatcher ScriptedAlchemy/pstack-codex trustfuture/investigation-video-skill \
 op7418/guizang-product-video-skill i-have-adhd/adhd hyperframes-ai/hyperframes \
 ; do one "$r"; done
