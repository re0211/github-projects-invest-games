# 第二十三辑 · 意图文件（Foremerge 最小版）

- **started_at**: 2026-09-24T08:29:01Z（脚本 `date -u` 打戳，非模型自报）
- **本地基线 HEAD**: `8baab10`
- **远端 HEAD**: `4e3faf0`（= 第二十二辑补，**推送已闭环**）
- **索引基线**: index.html 1141 项（卡片 1130 / 脚注 1140 / 页头 1141）
- **汇总基线**: `csdn-social-summary.md` 约 839 条（上一辑存档 `csdn-social-summary-v21.md`）
  ⚠️ 本轮开工**必须先补建 `csdn-social-summary-v22.md`**（第二十二辑当时未存档，第二十一辑开工时才补的 v21）

## 本轮角色
- `r23-gh`：GitHub 路（新仓库 / 新工具）
- `r23-cn`：中文社媒路（CSDN / 知乎 / 公众号 / B站 / 掘金 / 少数派等）
- `r23-off`：官方 + 海外路（厂商博客 / arXiv / HN / r-LocalLLaMA / X）

## 共同硬约束
1. **查重是硬工序**：每个候选必须比对本仓 `index.html`（1141 项）与
   `csdn-social-summary-v1..v21.md` + `csdn-social-summary.md`。
   用 `owner/repo` **小写精确比对**，不用关键词模糊匹配。
   五种重复形态（M-0001）：换名 / 旧闻换日期 / 转载 / ID 新≠内容新 / SEO 镜像站（`hqwc.cn`/`mhpn.cn`）。
2. **不核实不下结论**：README 写了 ≠ 能装（M-0016）。★ 数必须带「数据日期」。
3. **只登记不采用**的，要明确写理由。
4. **克隆/安装前先看 60 秒**：0★ 空壳、README 只有一句的，直接剔。
5. 产出写 `D:\34498\Documents\github-projects-invest-games\_r23\_r23_<路>.md`，
   ⚠️ **每查到 5 条就落盘一次**（上次官方路被 429 打断，30 分钟白干）。

## 本轮重点方向（承接第二十二辑）
- 游戏制作及拓展（引擎 AI 集成、Modding、发行、变现）
- AI 开发与使用（**上下文管理**为第一优先级）
- VSCode / vibe coding / DeepSeek harness / memory 管理
- 模型测评与上新新闻

## 上轮承接（本轮主 agent 自己做，不占子 agent 预算）
1. 追 DSH 源码实战第 13/14/16 章正文（`alchaincyf/deepseek-harness-orange-book`）
2. 「花叔生态」14 个仓库「是否真人关注」核实（看 fork/issue/PR，不看 ★）
3. `game-production-pipeline.md` 994 行超 200 行上限 → 该砍
