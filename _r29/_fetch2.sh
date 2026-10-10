set -u
REPOS="Ariakage/live2d-agent-kit RevStudio/Rev2D luomo66ccff/Amahane-Hikari-Live2D cyanfish-x/dsh-live2d-pets joyparkray/agent-avatar Untitled-Story/untitled-pixi-live2d-engine aethiopicuschan/cubism-go Arcelyth/live-ascii lmmtrr/spive2d nanlingyin/soullink-emotion-sdk Mikazuki-kufgr/webgal-attachment myths-labs/prometheus-avatar lk2168/vtuber-pipeline lvhaojie456/image-to-live2d funlin724/emote-to-cubism rydanee/live2drust so0420/doro-live2d-web Heonys/live2d-web canyueY/pyqt-live2d-bridge turboism/Turboism NekoUnix/A.R.I.A Hera-Berg/open-avatar-creator XucroYuri/L2MAS zeikar/charivo"
for r in $REPOS; do
  f=$(echo "$r" | tr '/' '_')
  gh api "repos/$r/readme" --jq '.content' 2>/dev/null | base64 -d 2>/dev/null > "rm_$f.md"
  echo "$r $(wc -c < rm_$f.md)"
done
