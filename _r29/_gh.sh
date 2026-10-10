set -u
OUT=_r29_gh_raw.txt
: > $OUT
Q=(
"live2d+in:name,description,readme&sort=stars&order=desc&per_page=100"
"live2d+cubism&sort=stars&order=desc&per_page=100"
"live2d+vtuber&sort=stars&order=desc&per_page=100"
"live2d&sort=updated&order=desc&per_page=100"
"cubism+moc3&sort=stars&order=desc&per_page=100"
"live2d+pushed:>2026-07-01&sort=updated&order=desc&per_page=100"
"live2d+model+viewer&sort=stars&order=desc&per_page=100"
"live2d+ai&sort=updated&order=desc&per_page=100"
)
i=0
for q in "${Q[@]}"; do
  i=$((i+1))
  echo "### QUERY $i : $q" >> $OUT
  gh api "search/repositories?q=$q" --jq '.items[] | [.full_name, (.stargazers_count|tostring), (.license.spdx_id // "NOASSERTION"), (.language // "-"), (.pushed_at // "-"), (.archived|tostring), (.html_url), ((.description // "")|gsub("[\r\n]";" ")|.[0:150])] | @tsv' >> $OUT 2>>$OUT
  echo "" >> $OUT
done
echo "DONE queries=$i"
