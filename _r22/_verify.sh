#!/bin/bash
for r in "$@"; do
  out=$(gh api "repos/$r" --jq '"\(.full_name)\tSTAR:\(.stargazers_count)\t\(.license.spdx_id)\t\(.language)\tupd:\(.updated_at[0:10])\tcreated:\(.created_at[0:10])\t\(.description)"' 2>&1)
  echo "$out"
done
