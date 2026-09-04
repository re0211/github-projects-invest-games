# -*- coding: utf-8 -*-
"""
第三轮更新脚本：
1) 用 GitHub API 实测数据刷新上一版 111 个项目的星级 / 更新时间 / License
2) 追加本轮新发现的 103 个项目（投资 36 / 游戏制作 35 / 游戏拓展 32）
3) 更新 header 计数、本次更新说明、页脚信源清单
"""
import io, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "index.html")
SNAPSHOT = "2026-09-03"

# ---------------------------------------------------------------- 数据：已有项目（实测刷新）
EXISTING_TSV = r"C:\Users\34498\AppData\Local\Temp\ghproj\existing_verified.tsv"

def load_existing():
    d = {}
    with io.open(EXISTING_TSV, encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 5:
                continue
            d[p[0].lower()] = {
                "stars": int(p[1]),
                "pushed": p[2][:10],
                "license": p[3],
                "archived": p[4] == "true",
            }
    return d

LIC_MAP = {"NOASSERTION": "自定义协议", "": "无 License"}

def fmt_stars(n):
    if n >= 1000:
        s = "%.1fk" % (n / 1000.0)
        return s[:-2] + "k" if s.endswith(".0k") else s
    return str(n)

# ---------------------------------------------------------------- 本轮新增项目数据
# 字段: slug, name, lang, stars, pushed, license, line(invest/make/mod),
#       tags, plain, analogy, exp(分,说明), uti(分,说明)
NEW = [
 # ============================ 一、投资与量化 ============================
 dict(slug="vnpy/vnpy", name="vn.py", lang="Python", stars=45071, pushed="2026-09-01", lic="MIT", line="invest",
   tags=["A股首选","实盘级"],
   plain="国内最成熟的<em>量化交易平台开发框架</em>：行情网关、交易接口、策略引擎、风控模块、图形界面全都有。它不是研究库，是能直接接券商柜台跑真钱的生产系统。",
   analogy="<b>打个比方：</b>如果 AKShare 是水龙头、backtesting.py 是试炼场，vn.py 就是<em>整套厨房加餐厅</em>——从进货到上菜一条龙。代价是重，学完整套要几周。",
   exp=(8.5,"全部模块化，C++/Python 双栈，接口定义清晰，想接自家券商的柜台照着 Gateway 接口写一个就行。"),
   uti=(9.0,"中文文档、中文社区、国内主流券商/期货接口基本都覆盖，是机构和个人都能落地的一条路。")),

 dict(slug="ZhuLinsen/daily_stock_analysis", name="daily_stock_analysis", lang="Python", stars=64543, pushed="2026-09-01", lic="MIT", line="invest",
   tags=["AI 投研","本轮新增"],
   plain="用大模型做<em>多市场股票智能分析</em>：拉行情、抓实时新闻、生成决策看板、定时推送到微信/飞书。号称零成本定时运行——数据用免费的，模型用便宜的。",
   analogy="<b>打个比方：</b>它相当于给你雇了个<em>每天早起读完全球财经新闻后给你写一份简报的助理</em>。注意：助理会写，但不会替你负责。",
   exp=(7.0,"流水线是脚本拼起来的，数据源与模型都可换，适合当成脚手架改。"),
   uti=(8.5,"装上就能每天收到推送，即时价值高；但结论质量高度依赖你喂的模型和数据源。")),

 dict(slug="myhhub/stock", name="stock（选股全家桶）", lang="Python", stars=14264, pushed="2026-04-02", lic="Apache-2.0", line="invest",
   tags=["A股","一体化"],
   plain="一个<em>贪心到把所有事都做了</em>的 A 股项目：取数据、算指标、算筹码分布、识别 K 线形态、综合选股、策略回测、甚至自动交易，还带 Web 和移动端界面。",
   analogy="<b>打个比方：</b>它不是工具，是<em>一整套已经装好的炒股软件</em>。好处是开箱即用，坏处是——你想改其中一环时，会发现它跟其他环长在一起了。",
   exp=(6.0,"大而全导致耦合度高，改一处容易牵一片；更适合整体使用而不是拆件复用。"),
   uti=(8.0,"想快速看到\"选股结果\"的人会觉得非常爽，省去自己拼装的时间。")),

 dict(slug="simonlin1212/a-stock-data", name="A股全栈数据工具包", lang="Python", stars=9493, pushed="2026-09-02", lic="Apache-2.0", line="invest",
   tags=["A股","面向 AI Agent"],
   plain="把 A 股数据做成<em>十一层架构、54 个端点、19 个数据源、零鉴权</em>的一套服务，明确为 AI Agent 设计——接口返回结构化数据，方便大模型直接调用。",
   analogy="<b>打个比方：</b>AKShare 是\"你去菜市场买菜\"，这个是\"<em>菜市场直接给你开了个 API，还能送到门口</em>\"。为自动化而生的设计思路，方向是对的。",
   exp=(8.5,"天然为程序化调用设计，接进自己的 Agent 流水线非常顺。"),
   uti=(7.5,"免鉴权是双刃剑：方便，但稳定性和长期可用性要自己盯。")),

 dict(slug="hello245m/free-stockdb", name="free-stockdb", lang="Python", stars=2381, pushed="2026-08-27", lic="MIT", line="invest",
   tags=["A股","本地化"],
   plain="面向 A 股<em>日 K、分钟 K 与 ETF 分钟数据</em>的本地量化引擎：增量同步、本地缓存、自动复权、批量查询、回测、指标计算，全在本地跑。",
   analogy="<b>打个比方：</b>别人每次分析都要去网上现抓数据，它是<em>先把数据搬回自己家仓库存好</em>，之后想怎么翻怎么翻，速度快且不依赖外网。",
   exp=(7.5,"纯本地存储 + Python API，方便接入自建体系。"),
   uti=(7.0,"分钟级数据的本地化是刚需，但项目较新，生态和文档还在长。")),

 dict(slug="shy3130/tick-stock-panel", name="TSP 量化工作台", lang="Python", stars=4237, pushed="2026-09-03", lic="MIT", line="invest",
   tags=["A股","自托管"],
   plain="自托管、零运维的 A 股<em>「选股 + 监控 + 回测」工作台</em>，用 LLM 帮你定制策略、分析个股、做复盘，数据源可自由替换。",
   analogy="<b>打个比方：</b>它把\"散户每天要做的事\"——看盘、选股、记笔记——<em>做成了自己的一个网页</em>。数据在你自己机器上，不经过别人服务器。",
   exp=(7.0,"插件式数据源设计，可拓展；LLM 部分可换模型。"),
   uti=(7.5,"对个人用户友好，但作者明说是个人项目，长期维护有不确定性。")),

 dict(slug="hugo2046/QuantsPlaybook", name="QuantsPlaybook", lang="Jupyter", stars=5933, pushed="2026-09-03", lic="自定义协议", line="invest",
   tags=["中文","研报复现"],
   plain="<em>券商金工研报的代码复现合集</em>。券商研报常讲了个好思路却不给代码，这里一篇篇把因子和策略还原成可运行的 Notebook。",
   analogy="<b>打个比方：</b>研报是\"菜谱\"，这个仓库是<em>照着菜谱真做出来的那盘菜，还把配方写在旁边</em>。想学怎么做因子，这比读论文快十倍。",
   exp=(6.5,"是 Notebook 合集不是库，不能直接 import，得抄。"),
   uti=(9.0,"对学因子研究的人来说，这是中文圈最好的免费教材之一。")),

 dict(slug="FinHackCN/finhack", name="FinHack", lang="Python", stars=1154, pushed="2026-08-19", lic="自定义协议", line="invest",
   tags=["A股","因子工厂"],
   plain="一个强调<em>「易于拓展」</em>的量化框架，把数据采集、因子计算、因子挖掘、因子分析、机器学习、策略编写、回测、实盘接入串成一条全流程。",
   analogy="<b>打个比方：</b>如果大部分量化项目是\"给你一套工具\"，FinHack 想做的是\"<em>给你一条流水线</em>\"，每个环节都能插自己的东西进去。",
   exp=(8.0,"设计上就奔着可扩展去的，插件点是明确的。"),
   uti=(6.5,"星数不高、社区不大，遇到问题多半得自己啃源码。")),

 dict(slug="refraction-ray/xalpha", name="xalpha", lang="Python", stars=2687, pushed="2026-07-25", lic="MIT", line="invest",
   tags=["基金","中文"],
   plain="<em>基金投资管理的回测引擎</em>。专门处理场外基金的那些烦人事：申赎确认、费率、分红、拆分、定投，股票回测库基本都不管这些。",
   analogy="<b>打个比方：</b>股票回测像算\"买卖差价\"，基金回测还要算\"<em>今天买的份额后天才能确认，中间还扣了手续费</em>\"。xalpha 就是专门算这些的。",
   exp=(7.0,"API 清晰，能接自己的策略逻辑。"),
   uti=(8.0,"如果你真买基金而不是股票，这是中文圈几乎唯一靠谱的选择。")),

 dict(slug="simonlin1212/TradingAgents-astock", name="TradingAgents-A股版", lang="Python", stars=3150, pushed="2026-09-02", lic="Apache-2.0", line="invest",
   tags=["多Agent","A股适配"],
   plain="把 TradingAgents 深度改造适配 A 股：<em>接入龙虎榜、游资、解禁等本地特色数据源</em>，7 位 AI 分析师按 A 股规则做多空辩论后决策。",
   analogy="<b>打个比方：</b>原版是\"<em>七个华尔街分析师开会</em>\"，这个版本是\"七个懂 A 股的国内研究员开会，还知道要看龙虎榜\"。语境对了一大截。",
   exp=(8.0,"沿用 TradingAgents 的模块化结构，分析师角色可增删改。"),
   uti=(7.5,"A 股规则适配是真正的差异化，但同样要警惕：辩论得再热闹也不是盈利保证。")),

 dict(slug="ValueCell-ai/valuecell", name="ValueCell", lang="Python", stars=11004, pushed="2026-03-09", lic="Apache-2.0", line="invest",
   tags=["多Agent","金融应用"],
   plain="社区驱动的<em>金融多智能体平台</em>，把选股、研究、风控等能力拆成一个个 Agent，可以自由组合成不同的金融应用。",
   analogy="<b>打个比方：</b>它不是某一个 App，而是<em>一个让你拼 App 的底座</em>。想做\"财报速读\"还是\"异动监控\"，自己搭。",
   exp=(8.5,"Agent 化的架构天然利于扩展，新增一个能力就是加一个 Agent。"),
   uti=(7.0,"框架感强于成品感，需要自己填充业务内容才有用。")),

 dict(slug="ginlix-ai/LangAlpha", name="LangAlpha", lang="Python", stars=1719, pushed="2026-09-03", lic="Apache-2.0", line="invest",
   tags=["AI 投研","命令行"],
   plain="自称<em>「金融市场版的 Claude Code」</em>：在终端里用自然语言查行情、做分析、跑策略，把投研工作流做成了可对话的命令行。",
   analogy="<b>打个比方：</b>把\"开一堆网页查数据再复制到 Excel\"变成\"<em>跟终端说一句话</em>\"。适合本来就习惯命令行的人。",
   exp=(7.5,"工具化封装，可接自己的数据源与分析函数。"),
   uti=(6.5,"很新，形态还在变；适合尝鲜，不适合当主力。")),

 dict(slug="The-Swarm-Corporation/AutoHedge", name="AutoHedge", lang="Python", stars=4338, pushed="2026-05-11", lic="MIT", line="invest",
   tags=["多Agent","激进"],
   plain="口号是<em>「几分钟搭一个自治对冲基金」</em>，用群体智能和多 Agent 把市场分析、风控、下单执行串起来自动跑。",
   analogy="<b>打个比方：</b>它把\"一家对冲基金的分工\"——研究员、风控官、交易员——<em>全部换成了 AI</em>，然后让它们自己开会自己下单。听起来很酷，实际上风险也全在你身上。",
   exp=(7.0,"Agent 编排基于 swarm 框架，可改造。"),
   uti=(5.0,"高度概念化，回测与实盘的严谨性远不及专业框架；建议当思路参考，别真上钱。")),

 dict(slug="imbue-bit/AlphaGPT", name="AlphaGPT", lang="Python", stars=3103, pushed="2026-06-12", lic="Apache-2.0", line="invest",
   tags=["因子挖掘","强化学习"],
   plain="基于深度强化学习的<em>开源自动因子工厂</em>：让模型自动搜索、组合、生成有效的选股因子，替代人肉挖因子。",
   analogy="<b>打个比方：</b>传统做法是\"研究员凭经验和直觉猜因子\"，这是\"<em>让机器在公式空间里自己找</em>\"。效率更高，但也更容易找到一堆过拟合的垃圾。",
   exp=(7.5,"框架开放，可接自己的因子算子集和标的池。"),
   uti=(6.5,"自动化挖因子是趋势，但产出因子的可解释性与稳定性仍是难题。")),

 dict(slug="AI4Finance-Foundation/FinRL-Trading", name="FinRL-X", lang="Python", stars=3658, pushed="2026-05-02", lic="Apache-2.0", line="invest",
   tags=["强化学习","新一代"],
   plain="FinRL 团队的新一代作品：<em>面向量化交易的 AI 原生模块化基础设施</em>，比老 FinRL 更强调工程化和可组合。",
   analogy="<b>打个比方：</b>老 FinRL 像\"论文配套代码\"，FinRL-X 想做成\"<em>能用的工程框架</em>\"。同一批人的第二次尝试，通常更靠谱。",
   exp=(8.0,"模块化设计是明确的改进方向。"),
   uti=(6.5,"强化学习做交易本身就很玄学，建议先用它理解范式，别直接信收益。")),

 dict(slug="TradeMaster-NTU/TradeMaster", name="TradeMaster", lang="Jupyter", stars=3057, pushed="2025-06-04", lic="Apache-2.0", line="invest",
   tags=["强化学习","学术"],
   plain="南洋理工出的<em>强化学习量化交易平台</em>，把 RL 训练、回测、评测做成统一流程，附带多个基准数据集。",
   analogy="<b>打个比方：</b>它像\"<em>量化 RL 的 ImageNet</em>\"——提供标准赛道和标准跑分，方便比较不同算法谁更强。",
   exp=(7.0,"平台化程度高，算法层可插拔。"),
   uti=(6.0,"学术味重，离实盘较远；更新停在 2025-06，注意时效。")),

 dict(slug="lballabio/QuantLib", name="QuantLib", lang="C++", stars=7574, pushed="2026-09-01", lic="自定义协议", line="invest",
   tags=["定价","工业标准"],
   plain="金融<em>衍生品定价与风险管理的工业标准库</em>：利率模型、期权定价、波动率曲面、信用衍生品， Banking 界用了二十年的东西。有 Python 封装（QuantLib-Python）。",
   analogy="<b>打个比方：</b>其他量化库是\"帮你做交易决策\"，QuantLib 是\"<em>帮银行算清楚这份合约到底值多少钱</em>\"。它是数学层，不是策略层。",
   exp=(9.0,"架构极其开放，几乎每个模型都可替换、可扩展，是教科书级的设计。"),
   uti=(7.0,"如果你不做衍生品/固收，它可能一辈子用不上；一旦需要，它是唯一选择。")),

 dict(slug="TA-Lib/ta-lib-python", name="TA-Lib (Python)", lang="Cython", stars=12227, pushed="2026-08-29", lic="BSD-2-Clause", line="invest",
   tags=["技术指标","基础设施"],
   plain="150+ 种<em>技术分析指标的 C 语言实现</em>，Python 封装。MACD、RSI、布林带、KDJ……所有你听说过的指标都在这里，而且算得飞快。",
   analogy="<b>打个比方：</b>它是量化界的\"<em>标准螺丝</em>\"。几乎所有回测框架底层都在用它，你迟早会装上——只是安装时可能要跟 C 编译搏斗一番。",
   exp=(8.0,"纯函数库，输入输出都是数组，接哪都行。"),
   uti=(9.0,"必备基础设施。指标本身不赚钱，但没它寸步难行。")),

 dict(slug="ranaroussi/quantstats", name="QuantStats", lang="Python", stars=7609, pushed="2026-07-20", lic="Apache-2.0", line="invest",
   tags=["绩效评估","报表"],
   plain="一行代码生成<em>专业级策略绩效报告</em>：年化收益、夏普、索提诺、最大回撤、月度收益热力图、与基准对比……HTML 报表直接出。",
   analogy="<b>打个比方：</b>回测跑完你只知道\"赚了 30%\"，它是那个<em>告诉你要扛多大回撤、什么时候最难熬、跟大盘比谁更强的会计</em>。",
   exp=(7.5,"输出可自定义，报表模块可嵌入自己的系统。"),
   uti=(9.0,"每个做回测的人都该装。看到完整绩效指标的那一刻，你对策略的认知会变。")),

 dict(slug="JerBouma/FinanceToolkit", name="FinanceToolkit", lang="Python", stars=5282, pushed="2026-09-01", lic="MIT", line="invest",
   tags=["基本面","财报分析"],
   plain="把<em>基本面分析做成 150+ 个财务比率和模型</em>：盈利能力、偿债能力、估值倍数、杜邦分析，还能直接跑 WACC、DCF。数据来源接 FinancialModelingPrep。",
   analogy="<b>打个比方：</b>技术指标库管的是\"价格\"，这个管的是\"<em>公司本身好不好</em>\"。想做价值投资而不是看图，工具箱完全是另一套。",
   exp=(8.0,"每个模块都能单独调用，也可以整体当分析流水线用。"),
   uti=(7.5,"美股数据完善；A 股需要自己换数据源，工作量不小。")),

 dict(slug="domokane/FinancePy", name="FinancePy", lang="Python", stars=3125, pushed="2026-09-02", lic="GPL-3.0", line="invest",
   tags=["衍生品","纯Python"],
   plain="纯 Python 的<em>衍生品定价与风险管理库</em>，覆盖固收、权益、外汇、信用衍生品——可以理解为 QuantLib 的 Python 原生平替。",
   analogy="<b>打个比方：</b>QuantLib 是\"<em>C++ 写的大部头，性能强但难改</em>\"，FinancePy 是\"<em>纯 Python 写的同题材教材版，慢一点但每一行你都看得懂</em>\"。",
   exp=(8.5,"纯 Python 意味着改起来毫无障碍，学习成本远低于 QuantLib。"),
   uti=(6.5,"性能是短板，适合研究与教学，不适合高频场景。")),

 dict(slug="google/tf-quant-finance", name="tf-quant-finance", lang="Python", stars=5493, pushed="2026-08-06", lic="Apache-2.0", line="invest",
   tags=["Google","高性能"],
   plain="Google 出的<em>高性能量化金融 TensorFlow 库</em>：用 GPU 加速蒙特卡洛、期权定价、利率模型，还能做梯度优化。",
   analogy="<b>打个比方：</b>它把\"<em>算一次要跑一小时的定价模型</em>\"丢到显卡上，几分钟出结果。适合那种\"算得动才算得出来\"的重型模型。",
   exp=(7.5,"基于 TensorFlow，扩展要靠写 TF 算子，门槛较高。"),
   uti=(6.0,"场景窄——只有当你真的需要大规模数值计算时才值得。")),

 dict(slug="questdb/questdb", name="QuestDB", lang="Java", stars=17295, pushed="2026-09-03", lic="Apache-2.0", line="invest",
   tags=["时序数据库","基础设施"],
   plain="<em>高性能开源时序数据库</em>，专为行情这类\"每秒几十万条、按时间查\"的数据设计，支持 SQL，吞吐惊人。",
   analogy="<b>打个比方：</b>用 CSV 存三年分钟线，查一次要翻半天；用 QuestDB，<em>同样的查询是毫秒级</em>。数据量到了一定规模，瓶颈就从策略变成了存储。",
   exp=(8.5,"标准 SQL 接口，任何语言都能接。"),
   uti=(7.5,"只有当你开始存全市场分钟级数据，它的价值才真正体现。")),

 dict(slug="jesse-ai/jesse", name="Jesse", lang="Python", stars=8409, pushed="2026-09-02", lic="MIT", line="invest",
   tags=["加密货币","体验好"],
   plain="一个<em>讲究代码美感的加密交易机器人</em>：回测、实盘、策略编写一条龙，作者花了大力气在 API 的简洁度上。",
   analogy="<b>打个比方：</b>同赛道的 Freqtrade 像\"<em>功能堆满的工具箱</em>\"，Jesse 像\"<em>一把打磨得很顺手的刀</em>\"。功能少一点，用起来舒服很多。",
   exp=(7.5,"策略就是继承一个类写几个方法，扩展直接。"),
   uti=(7.5,"做加密的话值得和 Freqtrade 都试一遍，选顺手的那个。")),

 dict(slug="enarjord/passivbot", name="Passivbot", lang="Python", stars=2087, pushed="2026-09-02", lic="Unlicense", line="invest",
   tags=["加密货币","做市"],
   plain="主打<em>网格做市策略</em>的加密交易机器人，支持 Bybit、OKX、Binance 等一众交易所，走的是\"低买高卖赚波动\"的路子。",
   analogy="<b>打个比方：</b>趋势策略是\"赌方向\"，它是\"<em>不赌方向，只赚来回震荡的差价</em>\"。行情横着走时它最舒服，单边暴涨暴跌时最难受。",
   exp=(7.0,"参数与配置驱动，策略逻辑集中在少数文件里。"),
   uti=(6.5,"网格策略的固有风险是单边行情扛不住，需要自己设好止损。")),

 dict(slug="marketcalls/openalgo", name="OpenAlgo", lang="Python", stars=2569, pushed="2026-09-03", lic="AGPL-3.0", line="invest",
   tags=["券商对接","印度市场"],
   plain="开源<em>算法交易平台</em>，用统一 API 对接多家券商，还内置行情、策略和 Web 界面。主要服务印度市场，但架构是通用的。",
   analogy="<b>打个比方：</b>它解决的是\"<em>每家券商接口都不一样，换个券商就要重写一遍</em>\"这个老问题——统一封装一层。",
   exp=(8.0,"Broker 插件架构清晰，理论上接国内券商也是照着写。"),
   uti=(6.0,"印度券商适配对你可能没用，但它的架构值得抄。")),

 dict(slug="cuemacro/finmarketpy", name="finmarketpy", lang="Python", stars=3807, pushed="2026-04-16", lic="Apache-2.0", line="invest",
   tags=["宏观","多资产"],
   plain="偏<em>宏观与多资产</em>的回测分析库：股票、外汇、利率、商品都能处理，自带一批现成的策略模板和事件研究工具。",
   analogy="<b>打个比方：</b>大部分回测库是为\"<em>一只股票的进出场</em>\"设计的，它是为\"<em>一类资产该不该配、配多少</em>\"设计的。层级更高一层。",
   exp=(7.0,"面向资产配置场景设计，模块化尚可。"),
   uti=(6.5,"做资产配置/宏观对冲才有感；纯做选股的人会觉得它太重。")),

 dict(slug="joshyattridge/smart-money-concepts", name="Smart Money Concepts", lang="Python", stars=1973, pushed="2026-04-03", lic="MIT", line="invest",
   tags=["ICT","指标库"],
   plain="把 <em>ICT（Inner Circle Trader）那套\"聪明钱\"概念</em>实现成 Python 指标：订单块、公允价值缺口、流动性扫单、突破结构……",
   analogy="<b>打个比方：</b>传统指标（MACD/RSI）是\"<em>价格的数学变换</em>\"，SMC 是\"<em>从价格里读机构的意图</em>\"。前者客观，后者带解读——这也意味着它更主观。",
   exp=(6.5,"就是个指标函数库，接哪都行，但概念本身没有统一标准。"),
   uti=(6.0,"信 SMC 的人会如获至宝，不信的人觉得是玄学。建议先当观察工具。")),

 dict(slug="quantopian/zipline", name="Zipline", lang="Python", stars=20078, pushed="2024-02-13", lic="Apache-2.0", line="invest",
   tags=["经典","停更"],
   plain="曾经的<em>量化回测事实标准</em>，Quantopian 出品，无数策略框架都抄过它的设计。可惜 Quantopian 关停后基本停止维护。",
   analogy="<b>打个比方：</b>它是量化界的\"<em>Windows XP</em>\"——一代人的启蒙，设计影响深远，但今天新项目不该再以它为底座。",
   exp=(5.0,"架构优秀，但依赖老化，Python 新版本下安装经常翻车。"),
   uti=(3.5,"已停更近三年。<b>新项目请改用 backtesting.py 或 rqalpha</b>，想学设计可以看它的源码。")),

 dict(slug="bbfamily/abu", name="阿布量化（abu）", lang="Python", stars=18534, pushed="2026-01-24", lic="GPL-3.0", line="invest",
   tags=["中文","教学向"],
   plain="中文的<em>量化交易系统</em>，覆盖股票、期权、期货、比特币，配了一整套\"从入门到实盘\"的中文教程和示例。",
   analogy="<b>打个比方：</b>它是\"<em>带教材的量化工具箱</em>\"。别的库默认你会，它默认你不会——对新手反而更友好。",
   exp=(6.0,"功能多但代码组织偏老派，二次开发不如新框架顺手。"),
   uti=(7.0,"星数很高说明影响力在，但更新节奏已经慢下来；当教材看比当生产工具更合适。")),

 dict(slug="Fincept-Corporation/FinceptTerminal", name="FinceptTerminal", lang="C++", stars=30910, pushed="2026-09-01", lic="自定义协议", line="invest",
   tags=["终端","数据聚合"],
   plain="一个<em>现代金融终端</em>：市场分析、投研、宏观经济数据，聚合在一个可交互探索的界面里，对标彭博终端的开源平替。",
   analogy="<b>打个比方：</b>彭博终端一年几十万，它想做的是\"<em>免费版能做到的最好样子</em>\"。野心很大，完成度要看你用多深。",
   exp=(6.5,"C++ 单体应用为主，二次开发门槛比 Python 生态高一截。"),
   uti=(6.5,"作为\"看数据的一个界面\"有价值，但不要指望它替代专业数据源。")),

 dict(slug="stefan-jansen/machine-learning-for-trading", name="ML4T（机器学习交易）", lang="Jupyter", stars=20766, pushed="2026-09-03", lic="MIT", line="invest",
   tags=["教材","体系"],
   plain="《Machine Learning for Trading》第三版的<em>官方配套代码</em>：从数据获取、因子工程、模型训练、组合优化到实盘执行，几百个 Notebook 全流程覆盖。",
   analogy="<b>打个比方：</b>这是量化界的\"<em>《深度学习》花书 + 课后作业全解</em>\"。想系统学一遍而不是东拼西凑，走这一套最省事。",
   exp=(6.0,"是教学代码不是库，要抄不要 import。"),
   uti=(9.0,"中文圈最好的系统性 ML 量化教材之一，而且是免费的。强烈推荐按顺序刷一遍。")),

 dict(slug="paperswithbacktest/awesome-systematic-trading", name="awesome-systematic-trading", lang="索引", stars=14120, pushed="2026-09-01", lic="自定义协议", line="invest",
   tags=["索引","系统化交易"],
   plain="<em>系统化交易的资源大全</em>：库、策略、书籍、博客、论文、教程，按主题分类。由 PaperWithBacktest 社区维护。",
   analogy="<b>打个比方：</b>awesome-quant 是\"<em>整个量化的地图</em>\"，这个更聚焦——只画\"<em>系统化交易</em>\"这一块，但画得更细。",
   exp=(2.5,"纯清单，无接口。"),
   uti=(8.5,"想找\"某个方向还有什么工具\"，来这里翻比搜索快得多。")),

 dict(slug="firmai/financial-machine-learning", name="financial-machine-learning", lang="索引", stars=8773, pushed="2025-01-03", lic="自定义协议", line="invest",
   tags=["索引","金融ML"],
   plain="专攻<em>金融机器学习</em>的资源清单：从特征工程、标签定义（三重屏障法）、样本权重到回测陷阱，偏\"学术前沿 + 实战代码\"。",
   analogy="<b>打个比方：</b>如果你已经会写策略，卡在\"<em>为什么回测很美实盘很惨</em>\"，这份清单里那批讲过拟合和数据泄漏的材料就是答案。",
   exp=(2.5,"纯清单，无接口。"),
   uti=(8.0,"偏进阶；新手读会觉得吃力，老手会觉得相见恨晚。")),

 dict(slug="LLMQuant/quant-wiki", name="LLMQuant 量化百科", lang="索引", stars=4118, pushed="2026-04-16", lic="自定义协议", line="invest",
   tags=["中文","知识库"],
   plain="致力于<em>量化知识开源与汉化</em>的中文知识库，目标是打破国内外量化金融的信息差——把英文世界的经典资料翻成中文并整理成体系。",
   analogy="<b>打个比方：</b>量化圈子很多好东西只存在于英文 PDF 和付费课程里，这个项目在做\"<em>把门撬开，把东西搬出来摆好</em>\"这件事。",
   exp=(3.0,"知识库性质，无接口，但内容可自由引用。"),
   uti=(7.5,"中文读者的价值远高于星数所显示的；适合当常备参考。")),

 dict(slug="cantaro86/Financial-Models-Numerical-Methods", name="Financial Models · Numerical Methods", lang="Jupyter", stars=7432, pushed="2024-10-22", lic="AGPL-3.0", line="invest",
   tags=["教材","数学"],
   plain="用<em>可交互 Notebook 讲金融数学</em>：随机过程、期权定价、蒙特卡洛、有限差分，每个公式都配可运行的代码。",
   analogy="<b>打个比方：</b>它是\"<em>能跑的教科书</em>\"——别的书让你看公式，它让你改参数看曲线怎么变。理解深度完全不同。",
   exp=(5.5,"教学代码，需自行提炼成库。"),
   uti=(8.0,"想真正搞懂期权定价而不只是调包，这是最好的路径之一。更新停在 2024-10。")),

 # ============================ 二、游戏制作 ============================
 dict(slug="raysan5/raylib", name="raylib", lang="C", stars=34563, pushed="2026-09-02", lic="Zlib", line="make",
   tags=["C/C++","强烈推荐"],
   plain="一个<em>极简的 C 语言游戏编程库</em>：没有编辑器、没有工程系统，就是你写 C 代码，它给你窗口、图形、输入、音频。整个库小而干净，头文件就能读完。",
   analogy="<b>打个比方：</b>引擎是\"<em>精装交付的房子</em>\"，raylib 是\"<em>一堆高质量建材和一套说明书</em>\"。想理解游戏到底怎么跑起来的，从它入手最清楚。",
   exp=(8.5,"纯库无框架束缚，想怎么组织代码都行；官方有 60+ 语言绑定。"),
   uti=(8.0,"做小游戏、做原型、做教学都极好；做大型项目需要自己搭脚手架。")),

 dict(slug="libgdx/libgdx", name="libGDX", lang="Java", stars=25361, pushed="2026-09-01", lic="Apache-2.0", line="make",
   tags=["Java","跨平台"],
   plain="成熟的<em>Java 跨平台游戏开发框架</em>，一套代码编译到桌面、Android、iOS、网页。Minecraft 早年生态和大量独立游戏都用它。",
   analogy="<b>打个比方：</b>它是\"<em>Java 圈的 Unity 平替</em>\"。没有可视化编辑器，但胜在稳定、自由、不收你一分钱也不抽成。",
   exp=(8.5,"模块可自由裁剪，只想要 2D 渲染就只引 2D 部分。"),
   uti=(7.5,"Java/Kotlin 开发者的最优解；不熟 JVM 生态的话上手偏慢。")),

 dict(slug="cocos2d/cocos2d-x", name="Cocos2d-x", lang="C++", stars=19172, pushed="2025-05-09", lic="自定义协议", line="make",
   tags=["手游","国内主流"],
   plain="国内手游时代的<em>主力开源引擎</em>，C++/Lua/JS 多语言绑定，曾撑起大量国产手游。如今官方重心已转向 Cocos Creator。",
   analogy="<b>打个比方：</b>它像\"<em>上一代的功勋老将</em>\"。你现在新项目不该选它，但你遇到的很多国产手游内部就是它——分析老项目时会碰到。",
   exp=(7.0,"源码开放且资料极多，中文社区庞大。"),
   uti=(5.0,"更新已明显放缓（2025-05）。<b>新项目请用 cocos-engine（Cocos Creator）</b>，这个当学习/维护用。")),

 dict(slug="MonoGame/MonoGame", name="MonoGame", lang="C#", stars=14381, pushed="2026-08-27", lic="自定义协议", line="make",
   tags=["C#","XNA 精神续作"],
   plain="微软 XNA 框架的<em>开源精神续作</em>，用 C# 做跨平台 2D/3D 游戏。《星露谷物语》《蔚蓝》《以撒》都是它做的。",
   analogy="<b>打个比方：</b>Unity 是\"<em>全套家具的精装房</em>\"，MonoGame 是\"<em>毛坯房 + 一套好工具</em>\"。<b>《星露谷》证明这条路能做出爆款</b>——一个人、四年、纯代码。",
   exp=(8.5,"无编辑器束缚，代码全是你自己的，想怎么架构都行。"),
   uti=(8.0,"会 C# 又不喜欢 Unity 编辑器的人的最优解；社区虽小但非常资深。")),

 dict(slug="o3de/o3de", name="Open 3D Engine (O3DE)", lang="C++", stars=9654, pushed="2026-09-02", lic="Apache-2.0", line="make",
   tags=["3A级","亚马逊支持"],
   plain="亚马逊支持的<em>Apache-2.0 授权 3A 级 3D 引擎</em>，由 CryEngine 分支而来（原 Amazon Lumberyard）。做高保真 3D 世界、仿真、影视级内容，<b>无任何费用和商业义务</b>。",
   analogy="<b>打个比方：</b>Unreal 抽你 5% 分成，O3DE 说\"<em>随便用，赚多少都是你的</em>\"。代价是生态和文档远不如 Unreal，你得自己扛。",
   exp=(9.0,"完全开源、模块化 Gem 系统，引擎层能改到根上。"),
   uti=(6.0,"能力有，但学习曲线陡、社区小；适合有引擎经验的团队，不适合第一个项目。")),

 dict(slug="pygame/pygame", name="Pygame", lang="C", stars=8913, pushed="2025-11-01", lic="自定义协议", line="make",
   tags=["Python","入门首选"],
   plain="Python 的<em>多媒体与游戏库</em>，SDL 的 Python 封装。几乎所有用 Python 学编程的人做的第一个游戏都是用它。",
   analogy="<b>打个比方：</b>它是游戏开发的\"<em>自行车辅助轮</em>\"。帮你理解游戏循环、事件、碰撞这些概念，但别指望骑它上高速。",
   exp=(6.0,"简单到没有架构可言，好处是自由，坏处是大项目会失控。"),
   uti=(8.0,"教学价值满分，生产价值有限；<b>做正经 2D 游戏建议直接上 Pyxel 或 Godot</b>。")),

 dict(slug="love2d/love", name="LÖVE", lang="C++", stars=8671, pushed="2026-08-26", lic="自定义协议", line="make",
   tags=["Lua","极简"],
   plain="用 <em>Lua 写 2D 游戏</em>的框架，核心哲学是\"只做必要的事\"：绘图、声音、输入、物理，其余交给 Lua 生态。",
   analogy="<b>打个比方：</b>它是\"<em>一把磨得极锋利的小刀</em>\"。Lua 轻、热重载快，改一行代码立刻看到效果——这种反馈速度对创作节奏影响很大。",
   exp=(7.5,"Lua 脚本层完全开放，配合 LuaRocks 生态扩展。"),
   uti=(7.5,"做 Game Jam、做 2D 独立游戏非常舒服；大型项目需要自己补工程化。")),

 dict(slug="playcanvas/engine", name="PlayCanvas", lang="JavaScript", stars=16610, pushed="2026-09-03", lic="MIT", line="make",
   tags=["网页3D","WebGPU"],
   plain="纯网页的<em>3D 图形运行时</em>，支持 WebGL / WebGPU / WebXR / glTF，配一个云端可视化编辑器。浏览器里打开就能做 3D。",
   analogy="<b>打个比方：</b>别的 3D 引擎要你装几个 G 的软件，它是\"<em>打开一个网页就开始建模</em>\"。分享作品就是一个链接。",
   exp=(8.0,"引擎 MIT 开源，编辑器为云服务（有免费额度）；引擎本身可完全自托管。"),
   uti=(8.0,"做网页 3D 展示、广告互动、轻量 3D 游戏的首选之一。")),

 dict(slug="clockworklabs/SpacetimeDB", name="SpacetimeDB", lang="Rust", stars=25089, pushed="2026-09-03", lic="自定义协议", line="make",
   tags=["游戏后端","新范式"],
   plain="把<em>数据库和服务器合成一个东西</em>：你的游戏逻辑写成一个模块直接跑在数据库里，客户端连上来就像直连数据库，延迟极低。",
   analogy="<b>打个比方：</b>传统做法是\"<em>游戏服务器 ↔ 数据库</em>\"来回跑；它是\"<em>把游戏逻辑搬进数据库里住下</em>\"，省掉中间那趟路。做多人实时游戏时这个差别很大。",
   exp=(8.0,"模块可用 Rust/C# 编写，架构新颖；但范式较新，生态还在长。"),
   uti=(7.0,"适合多人实时、需要强一致性的游戏；单机或小项目用不上。")),

 dict(slug="heroiclabs/nakama", name="Nakama", lang="Go", stars=13260, pushed="2026-08-25", lic="Apache-2.0", line="make",
   tags=["游戏后端","开箱即用"],
   plain="<em>开源游戏后端服务器</em>：账号、多人匹配、排行榜、聊天、社交、存档、内购校验，这些\"每个游戏都要但没人想写\"的东西它全包了。",
   analogy="<b>打个比方：</b>你做的是一辆车，它是\"<em>现成的加油站、公路和交通规则</em>\"。没有它，你的车再好也只能在院子里转。",
   exp=(8.5,"服务端逻辑可用 Go/Lua/JS/TS 写，可完全自托管和定制。"),
   uti=(8.5,"任何需要联网、多人、排行榜的游戏都该看看它，省下几个月后端开发。")),

 dict(slug="Orama-Interactive/Pixelorama", name="Pixelorama", lang="GDScript", stars=10236, pushed="2026-09-01", lic="MIT", line="make",
   tags=["像素美术","自带"],
   plain="用 Godot 写的<em>开源像素画工具</em>：画精灵、画瓦片、做逐帧动画、做像素字体，跨平台还有网页版。",
   analogy="<b>打个比方：</b>Aseprite 要买（虽然不贵），它是\"<em>免费的那个，而且功能不差</em>\"。做像素风游戏，美术工具这块可以直接结案。",
   exp=(8.0,"用 Godot 写的意味着——如果你会 GDScript，<em>可以自己给它加功能</em>。"),
   uti=(9.0,"免费、好用、活跃维护。做像素游戏没有理由不用它。")),

 dict(slug="mapeditor/tiled", name="Tiled", lang="C++", stars=12861, pushed="2026-09-02", lic="自定义协议", line="make",
   tags=["关卡编辑","行业标准"],
   plain="<em>通用关卡/地图编辑器</em>，几乎所有 2D 引擎都支持导入它的 .tmx 格式。画瓦片地图、放物件、设碰撞区、加自定义属性。",
   analogy="<b>打个比方：</b>它是 2D 游戏界的\"<em>通用插座</em>\"——换引擎不用重做地图，因为你用的不是某引擎的私有格式。",
   exp=(9.0,"格式完全开放、有规范文档，自定义属性可以塞任何数据。"),
   uti=(9.0,"做 2D 关卡几乎是必装。学半小时能上手，能用一辈子。")),

 dict(slug="skypjack/entt", name="EnTT", lang="C++", stars=13076, pushed="2026-09-02", lic="MIT", line="make",
   tags=["ECS","高性能"],
   plain="现代 C++ 的<em>实体组件系统（ECS）库</em>，header-only，性能极强。被大量商业引擎和自研引擎采用。",
   analogy="<b>打个比方：</b>传统写法是\"<em>物体是什么</em>\"（继承），ECS 是\"<em>物体有哪些数据</em>\"（组合）。换个组织方式，同一个游戏能快好几倍。",
   exp=(9.5,"纯库、无框架侵入，塞进任何 C++ 项目都行。"),
   uti=(7.0,"写 C++ 引擎或性能敏感模块时的标配；不写 C++ 就跟你无关。")),

 dict(slug="SanderMertens/flecs", name="flecs", lang="C", stars=8641, pushed="2026-09-02", lic="自定义协议", line="make",
   tags=["ECS","带工具"],
   plain="另一个高性能 ECS，但<em>比 EnTT 更\"全家桶\"</em>：自带查询语言、反射系统、Web 可视化调试工具、还有一套系统调度。",
   analogy="<b>打个比方：</b>EnTT 是\"<em>一把好刀</em>\"，flecs 是\"<em>一套带刀架和磨刀石的工具箱</em>\"。想要开箱即用的配套，选它。",
   exp=(8.5,"C/C++ 双接口，自带运行时可视化，调试 ECS 比纯手写舒服得多。"),
   uti=(7.5,"想快速把 ECS 跑起来并看懂内部状态的人更适合它。")),

 dict(slug="jrouwe/JoltPhysics", name="Jolt Physics", lang="C++", stars=11485, pushed="2026-08-31", lic="MIT", line="make",
   tags=["物理","3A级"],
   plain="多核友好的<em>刚体物理与碰撞检测库</em>。<b>《地平线：西之绝境》和《死亡搁浅 2》用的就是它</b>——这不是玩具，是 3A 生产线上的部件。",
   analogy="<b>打个比方：</b>物理引擎是\"<em>让东西掉下来、撞上去、堆起来</em>\"的那层。它做得好，你感觉不到它的存在；做得差，满屏穿模。",
   exp=(8.5,"MIT 授权、架构现代、多核优化，能直接集成进自建引擎。"),
   uti=(8.0,"比 Bullet 更现代，是新项目的更好选择；老项目迁移成本才是问题。")),

 dict(slug="bulletphysics/bullet3", name="Bullet3", lang="C++", stars=14711, pushed="2025-10-22", lic="自定义协议", line="make",
   tags=["物理","经典"],
   plain="老牌<em>开源物理引擎</em>，游戏、VR、特效、机器人、机器学习都在用。二十年的积累，稳定性经过验证。",
   analogy="<b>打个比方：</b>它是物理引擎里的\"<em>丰田卡罗拉</em>\"——不最新，但到处都是、谁都会修、资料一搜一大把。",
   exp=(8.0,"完全开源，可改到源码级；Python 绑定也成熟。"),
   uti=(7.5,"老项目维护、机器人仿真、学术用途依然首选；新游戏项目可以看 Jolt。")),

 dict(slug="recastnavigation/recastnavigation", name="Recast Navigation", lang="C++", stars=7889, pushed="2026-02-27", lic="Zlib", line="make",
   tags=["寻路","行业标准"],
   plain="<em>导航网格（NavMesh）工具集</em>：自动把关卡几何体烘焙成可行走区域，再做寻路。Unity、Unreal、Godot 的寻路底层思想都源自这里。",
   analogy="<b>打个比方：</b>A* 是在格子上找路，NavMesh 是\"<em>先画出'哪些地方能走'，再在面上找路</em>\"。后者快得多，也自然得多。",
   exp=(9.0,"工具链（Recast 烘焙 + Detour 寻路）分离，可只取其中一段。"),
   uti=(8.0,"做 3D 游戏要 AI 会走路，这就是标准答案，没有理由自己写。")),

 dict(slug="assimp/assimp", name="Assimp", lang="C++", stars=13174, pushed="2026-09-02", lic="自定义协议", line="make",
   tags=["模型导入","基础设施"],
   plain="<em>通用模型导入库</em>，把 40+ 种 3D 文件格式（FBX、OBJ、glTF、DAE……）统一转成一套干净的数据结构。",
   analogy="<b>打个比方：</b>建模软件有几十种，格式乱七八糟。它是\"<em>万能转换插头</em>\"——你只对接它一个，它去对接全世界。",
   exp=(9.0,"纯库、输出结构统一，是所有自研引擎的标准零件。"),
   uti=(8.5,"写引擎/工具必装；用成熟引擎的话，它已经在你引擎里了。")),

 dict(slug="ValveSoftware/GameNetworkingSockets", name="GameNetworkingSockets", lang="C++", stars=9883, pushed="2026-08-27", lic="BSD-3-Clause", line="make",
   tags=["网络","V社出品"],
   plain="V 社开源的游戏网络传输层：<em>UDP 之上的可靠/不可靠消息、分片重组、P2P 打洞、加密</em>。Steam 和 CS 的网络基础之一。",
   analogy="<b>打个比方：</b>TCP 太慢（要保证顺序），裸 UDP 太野（会丢包）。它做的是\"<em>游戏要的那种恰到好处的中间态</em>\"——重要消息必达，位置更新丢了就算了。",
   exp=(8.5,"库级组件，可嵌入自己的网络层。"),
   uti=(7.5,"做多人游戏、需要 NAT 穿透时非常有用；不上多人就完全用不到。")),

 dict(slug="ocornut/imgui", name="Dear ImGui", lang="C++", stars=76024, pushed="2026-09-02", lic="MIT", line="make",
   tags=["调试工具","必备"],
   plain="<em>即时模式 GUI 库</em>，专为游戏和工具的调试界面设计：几行代码就能弹出一个面板，实时改参数、看变量、画曲线。",
   analogy="<b>打个比方：</b>正式 UI 是\"<em>给玩家看的精装门面</em>\"，ImGui 是\"<em>给开发者自己看的配电箱</em>\"——丑，但所有开关都在手边。",
   exp=(9.5,"单文件级别的集成难度，移植到任何渲染后端都行，绑定覆盖全语言。"),
   uti=(9.5,"星数说明一切。做引擎、做工具、做编辑器，几乎人手一份。")),

 dict(slug="wolfpld/tracy", name="Tracy Profiler", lang="C++", stars=16710, pushed="2026-09-02", lic="自定义协议", line="make",
   tags=["性能分析","强烈推荐"],
   plain="<em>帧级性能分析器</em>：精确到每一帧、每个函数、每个锁的耗时，还能看 GPU、内存、网络、锁竞争，时间轴可视化做得极好。",
   analogy="<b>打个比方：</b>游戏卡了，普通 profiler 告诉你\"某个函数慢\"；Tracy 告诉你\"<em>第 1432 帧卡了 8 毫秒，是因为渲染线程在等物理线程的锁</em>\"。",
   exp=(8.5,"客户端可自托管，数据格式开放，能接自己的分析脚本。"),
   uti=(9.0,"做游戏做到一定规模，性能优化是绕不过去的坎。它是那把最好用的尺子。")),

 dict(slug="mxgmn/WaveFunctionCollapse", name="WaveFunctionCollapse", lang="C#", stars=25304, pushed="2026-03-22", lic="自定义协议", line="make",
   tags=["程序化生成","经典"],
   plain="<em>波函数坍缩算法</em>：给它一张示例图，它按图中的局部规律生成任意大小的相似图案——地图、纹理、关卡，都能这么造。",
   analogy="<b>打个比方：</b>你画一小块\"草地挨着小路、小路挨着房子\"的示意图，它据此\"<em>长出一整座村庄</em>\"，而且每块地的邻居关系都合理。",
   exp=(8.0,"算法简单、代码短，移植到任何语言都不难（已有几十种实现）。"),
   uti=(7.5,"做 Roguelike、像素地牢、程序化关卡时的经典武器；出图质量和约束设计全靠调。")),

 dict(slug="mxgmn/MarkovJunior", name="MarkovJunior", lang="C#", stars=8177, pushed="2026-03-20", lic="MIT", line="make",
   tags=["程序化生成","新思路"],
   plain="同一作者的<em>概率式程序化生成语言</em>：用\"模式匹配 + 约束传播\"的规则描述生成过程，比 WFC 更强表达力，附 153 个示例。",
   analogy="<b>打个比方：</b>WFC 是\"<em>照着样本长</em>\"，MarkovJunior 是\"<em>按规则推演</em>\"——你可以写\"先铺路，再沿路盖房，再在房边种树\"这种分步逻辑。",
   exp=(8.0,"规则用 XML 描述，改规则不用改代码。"),
   uti=(6.5,"概念领先但工具链不成熟；适合研究和灵感，不太适合直接进生产线。")),

 dict(slug="CoplayDev/unity-mcp", name="Unity MCP", lang="C#", stars=13860, pushed="2026-09-02", lic="MIT", line="make",
   tags=["AI × 引擎","本轮新增"],
   plain="让 AI 助手<em>直接操作 Unity 编辑器</em>的桥接：管理资源、控制场景、改脚本、跑测试——通过 MCP 协议，AI 真的能\"动手\"而不只是\"说说\"。",
   analogy="<b>打个比方：</b>以前 AI 是\"<em>站在你旁边口述步骤让你点鼠标</em>\"，现在是\"<em>接过鼠标自己点</em>\"。和 godot-mcp 是同一思路的 Unity 版。",
   exp=(8.5,"MCP 协议开放，工具可自己增删；也能接自己的 Agent。"),
   uti=(8.0,"Unity 用户的效率倍增器；注意别让 AI 在没有版本控制的情况下改工程。")),

 dict(slug="wellingfeng/UltraGameStudio", name="UltraGameStudio", lang="TypeScript", stars=296, pushed="2026-09-03", lic="MIT", line="make",
   tags=["AI Agent","很新"],
   plain="定位是<em>游戏开发专用的 AI coding agent</em>：不只写代码，还管引擎工作流、玩法代码和素材生成，把\"做游戏\"当成一个整体任务来编排。",
   analogy="<b>打个比方：</b>通用 AI 编程助手帮你写函数，它想做的是帮你<em>从\"我要做个平台跳跃游戏\"一路做到能玩</em>。野心大，星数还小（296），属于早期。",
   exp=(7.0,"很新，架构还在变；但方向值得盯。"),
   uti=(5.5,"现阶段当作观察对象，别指望它替你把游戏做完。")),

 dict(slug="Kirilllive/tuesday-js", name="Tuesday JS", lang="JavaScript", stars=686, pushed="2026-09-02", lic="MIT", line="make",
   tags=["视觉小说","零依赖"],
   plain="<em>纯浏览器的视觉小说编辑器</em>：不装任何软件，打开网页就能搭剧情、分支、立绘、选项，导出成网页游戏。零第三方库依赖。",
   analogy="<b>打个比方：</b>Ren'Py 要装 Python 环境，它是\"<em>打开浏览器就能开工</em>\"。对不想碰命令行的创作者，门槛降了一大截。",
   exp=(7.0,"导出的是标准 HTML/JS 项目，能拿去自己改。"),
   uti=(7.0,"轻量创作、快速原型很合适；复杂项目还是 Ren'Py 稳。")),

 dict(slug="AlmasB/FXGL", name="FXGL", lang="Kotlin", stars=4853, pushed="2026-07-01", lic="MIT", line="make",
   tags=["Java/Kotlin","教学友好"],
   plain="基于 JavaFX 的<em>Java/Kotlin 游戏框架</em>，主打\"不写样板代码\"——几行就能出一个能跑的游戏，内置物理、粒子、UI、寻路。",
   analogy="<b>打个比方：</b>libGDX 是\"<em>给你零件自己装</em>\"，FXGL 是\"<em>零件已经装好大半，你拧最后几颗螺丝</em>\"。教学场景特别爽。",
   exp=(7.0,"API 封装得紧，方便用，但深度定制要绕开封装。"),
   uti=(7.0,"教学、原型、小型 2D 游戏很合适；大型项目能力上限不如 libGDX。")),

 dict(slug="not-fl3/macroquad", name="macroquad", lang="Rust", stars=4609, pushed="2026-08-18", lic="Apache-2.0", line="make",
   tags=["Rust","轻量"],
   plain="Rust 的<em>极简跨平台游戏框架</em>，主打\"编译快、依赖少、单文件就能跑\"，是 Rust 圈做游戏最省心的入门选择。",
   analogy="<b>打个比方：</b>Bevy 是\"<em>重型正规军</em>\"（ECS + 完整架构，学习曲线陡），macroquad 是\"<em>轻骑兵</em>\"——你想马上看到东西在动，选它。",
   exp=(7.5,"无 ECS 束缚，代码直白；但大型项目需要自己补架构。"),
   uti=(7.0,"Rust 新手做游戏的推荐起点；老手做大型项目还是 Bevy 更合适。")),

 dict(slug="KilledByAPixel/LittleJS", name="LittleJS", lang="JavaScript", stars=4173, pushed="2026-08-18", lic="MIT", line="make",
   tags=["网页","极轻量"],
   plain="<em>超小的 HTML5 游戏引擎</em>：功能齐全（渲染、物理、粒子、音效、输入）但<em>零依赖、体积极小</em>，几十 KB 就能跑起来。",
   analogy="<b>打个比方：</b>Phaser 是\"<em>装满的登山包</em>\"，LittleJS 是\"<em>腰包</em>\"。做 Game Jam 那种一小时出成品的场景，小就是快。",
   exp=(7.5,"单个 JS 文件，源码可读完，想改就改。"),
   uti=(7.5,"做小游戏、做 jam、做网页 Demo 手感极好；大型项目功能不够。")),

 dict(slug="KaijuEngine/kaiju", name="Kaiju Engine", lang="Go", stars=4696, pushed="2026-08-29", lic="自定义协议", line="make",
   tags=["Go","自带编辑器"],
   plain="用 Go 写的<em>2D/3D 游戏引擎</em>，基于 Vulkan，<b>自带可视化编辑器</b>——Go 生态里少见地补齐了\"引擎 + 编辑器\"这一环。",
   analogy="<b>打个比方：</b>Ebiten 是\"<em>Go 语言的画板和画笔</em>\"，Kaiju 想做的是\"<em>Go 语言的小型 Unity</em>\"。野心不一样。",
   exp=(8.0,"引擎与编辑器分离，插件与脚本层可扩。"),
   uti=(6.0,"很新，生态和文档薄弱；Go 死忠可以关注，别押宝。")),

 dict(slug="RodZill4/material-maker", name="Material Maker", lang="GDScript", stars=5869, pushed="2026-08-06", lic="MIT", line="make",
   tags=["材质","美术工具"],
   plain="用 Godot 写的<em>程序化材质生成与 3D 模型绘制工具</em>：节点式编辑，实时预览，导出 PBR 贴图。可以理解为免费的 Substance Designer 平替。",
   analogy="<b>打个比方：</b>手工画贴图是\"<em>一笔一笔描</em>\"，程序化材质是\"<em>搭一套生成规则，参数一调就出一批</em>\"。改起来快十倍。",
   exp=(8.0,"节点系统可扩展，Godot 用户还能直接改源码。"),
   uti=(7.5,"做 3D 游戏缺贴图时的救命工具；免费这一点就值回票价。")),

 dict(slug="endless-sky/endless-sky", name="Endless Sky", lang="C++", stars=7530, pushed="2026-09-02", lic="GPL-3.0", line="make",
   tags=["可做参考","开源游戏"],
   plain="一个完整的<em>开源太空探索/贸易/战斗游戏</em>，本身好玩，更重要的是——它的<em>数据全部是纯文本配置</em>，改船、改星系、改剧情不用碰 C++。",
   analogy="<b>打个比方：</b>它是\"<em>一本摊开的游戏设计说明书</em>\"。你想知道\"一个 2D 太空游戏的数据该怎么组织\"，直接看它的目录结构就懂了。",
   exp=(9.0,"数据格式开放，MOD 社区庞大，加内容是改文本文件而不是改代码。"),
   uti=(7.0,"当游戏玩、当教材读、当 MOD 平台用，三种价值都有。")),

 dict(slug="Calinou/awesome-godot", name="awesome-godot", lang="索引", stars=10685, pushed="2026-09-01", lic="CC-BY-4.0", line="make",
   tags=["索引","Godot"],
   plain="Godot 生态的<em>插件、脚本、资源总目录</em>，由 Godot 核心贡献者维护。找\"有没有人已经做过 X\"，这里是最快答案。",
   analogy="<b>打个比方：</b>awesome-renpy 是 Ren'Py 的地图，这是 Godot 的地图，而且<em>由天天在引擎里的人画的</em>，准确性有保障。",
   exp=(2.5,"纯清单，无接口。"),
   uti=(9.0,"用 Godot 就该收藏。省下的搜索时间非常可观。")),

 dict(slug="ellisonleao/magictools", name="magictools", lang="索引", stars=17241, pushed="2026-09-01", lic="MIT", line="make",
   tags=["索引","游戏开发"],
   plain="游戏开发的<em>资源大全</em>：引擎、框架、美术工具、音效、素材站、教程、社区，覆盖面极广，分类清楚。",
   analogy="<b>打个比方：</b>它是\"<em>游戏开发的黄页</em>\"。不教你怎么做，但你想找什么工具时，它告诉你这世界上都有什么。",
   exp=(2.5,"纯清单，无接口。"),
   uti=(8.5,"不知道该用什么工具时先翻它，比搜搜索引擎高效。")),

 dict(slug="lettier/3d-game-shaders-for-beginners", name="3D Game Shaders For Beginners", lang="C++", stars=19867, pushed="2023-06-25", lic="自定义协议", line="make",
   tags=["教材","着色器"],
   plain="一步一步教你实现<em>SSAO、景深、光照、法线贴图、雾效、卡通渲染</em>等着色器效果，每段都配可运行代码和效果图。",
   analogy="<b>打个比方：</b>着色器是\"<em>决定画面长什么样的那层魔法</em>\"，它把魔法拆成了一道道可复现的工序，还让你亲手做一遍。",
   exp=(6.0,"教学代码，需移植到自己的引擎；但原理讲得极透。"),
   uti=(8.0,"想搞懂 3D 画面是怎么\"算\"出来的，这是最好的中文圈外教材之一。更新停在 2023-06，但原理不过时。")),

 # ============================ 三、游戏拓展与解包 ============================
 dict(slug="praydog/REFramework", name="REFramework", lang="C++", stars=5383, pushed="2026-09-03", lic="MIT", line="mod",
   tags=["RE引擎","强烈推荐"],
   plain="<em>卡普空 RE 引擎全系通用的 MOD 框架</em>：MOD 加载、Lua 脚本平台，还带 VR 支持。《生化危机》系列、《怪物猎人：荒野》、《龙之信条 2》都靠它。",
   analogy="<b>打个比方：</b>BepInEx 是\"<em>Unity 游戏的万能钥匙</em>\"，REFramework 是\"<em>RE 引擎游戏的专用主钥匙</em>\"——更贴合，能做到的更多（包括强行上 VR）。",
   exp=(9.0,"内置 Lua 脚本 API 和 VR 运行时，开发者能直接在游戏里写逻辑。"),
   uti=(9.0,"这一代卡普空游戏的 MOD 生态基本建立在它之上，是刚需工具。")),

 dict(slug="praydog/UEVR", name="UEVR", lang="C++", stars=4479, pushed="2026-08-30", lic="自定义协议", line="mod",
   tags=["VR 改造","黑科技"],
   plain="<em>把虚幻引擎游戏强行变成 VR 游戏</em>的通用 MOD，支持 UE 4.8 到 5.4。同一个作者做的，技术含量极高——它不是模拟，是真的把渲染管线改成双目立体输出。",
   analogy="<b>打个比方：</b>正常 VR 游戏是\"<em>为 VR 专门盖的房子</em>\"，UEVR 是\"<em>给已经盖好的房子装上 VR 眼镜</em>\"。效果参差，但能玩到本身就是奇迹。",
   exp=(7.5,"配置驱动为主，深度定制需要懂渲染管线。"),
   uti=(7.5,"有 VR 头显的话非常值得一试；不同游戏适配质量差异很大，要有心理准备。")),

 dict(slug="tModLoader/tModLoader", name="tModLoader", lang="C#", stars=5615, pushed="2026-09-03", lic="MIT", line="mod",
   tags=["Terraria","教科书"],
   plain="《泰拉瑞亚》的<em>MOD 制作与加载平台</em>：自带 MOD 浏览器、一键发布、完善的 C# API，官方甚至把它放进了 Steam 正式支持。",
   analogy="<b>打个比方：</b>这是\"<em>MOD 生态该有的样子</em>\"——官方点头、工具齐全、分发内建、文档完善。其他游戏的 MOD 框架都该照着这个标准来。",
   exp=(9.5,"完整 C# API + 官方模组模板 + 内建分发，二次开发体验极佳。"),
   uti=(9.0,"想学\"怎么做 MOD\"，这是最好的切入点——教程多、反馈快、社区活跃。")),

 dict(slug="geode-sdk/geode", name="Geode", lang="C++", stars=2799, pushed="2026-08-30", lic="BSL-1.0", line="mod",
   tags=["几何冲刺","现代框架"],
   plain="《几何冲刺》的<em>现代化 MOD 框架</em>：解决老 MOD 之间的冲突问题，提供统一 API、内建 MOD 商店和自动更新。",
   analogy="<b>打个比方：</b>老式 MOD 是\"<em>各改各的内存地址，装两个就打架</em>\"，Geode 是\"<em>先修好地基再让大家在上面盖房子</em>\"。",
   exp=(9.0,"现代 C++ API，头文件齐全，MOD 之间可互相调用。"),
   uti=(8.5,"装 MOD 体验大幅提升；对开发者来说 API 质量超出预期。")),

 dict(slug="EverestAPI/Everest", name="Everest", lang="C#", stars=513, pushed="2026-08-27", lic="MIT", line="mod",
   tags=["蔚蓝","框架"],
   plain="《蔚蓝》的<em>MOD 加载器与 Mod API</em>。这款游戏的自定义关卡生态（几千张玩家自制地图）就是靠它撑起来的。",
   analogy="<b>打个比方：</b>游戏本体是\"<em>一座山</em>\"，Everest 让它变成了\"<em>一座任何人都能往上加路的山</em>\"。自制关卡数量早已超过官方内容。",
   exp=(9.0,"完整 API + 地图编辑器集成 + 内建分发，扩展能力极强。"),
   uti=(8.5,"如果你对\"关卡设计\"感兴趣，这里有几千张现成的优秀玩家地图可以拆解学习。")),

 dict(slug="kiooeht/ModTheSpire", name="ModTheSpire", lang="Java", stars=516, pushed="2025-07-12", lic="MIT", line="mod",
   tags=["杀戮尖塔","注入式"],
   plain="《杀戮尖塔》的<em>外部 MOD 加载器</em>，配合 ModTheSpire 的补丁框架实现代码注入。这个游戏的 MOD 生态（尤其\"进阶 mods\"）规模惊人。",
   analogy="<b>打个比方：</b>有些 MOD 是\"<em>加内容</em>\"（新卡牌、新角色），有些是\"<em>改规则</em>\"（重做整个平衡性）。这个框架两者都支持，后者才是它的厉害之处。",
   exp=(8.0,"Java 字节码注入机制，改游戏逻辑不受源码限制。"),
   uti=(7.5,"生态成熟但对开发者要求不低；更新停在 2025-07，注意兼容版本。")),

 dict(slug="GodotModding/godot-mod-loader", name="Godot Mod Loader", lang="GDScript", stars=669, pushed="2026-08-21", lic="CC0-1.0", line="mod",
   tags=["Godot","通用"],
   plain="给 <em>GDScript 写的 Godot 游戏做通用 MOD 加载器</em>（支持 3.x / 4.x）。对你这种\"分析 Godot 游戏源码\"的场景，它是理解 MOD 注入思路的好样本。",
   analogy="<b>打个比方：</b>别的 MOD 框架是\"<em>给某一款游戏配的钥匙</em>\"，它是\"<em>给 Godot 这一整类游戏配的万能钥匙胚</em>\"——照着它就能给任意 Godot 游戏加 MOD 支持。",
   exp=(9.0,"专为二次开发设计，API 与钩子系统开放，CC0 授权随便改。"),
   uti=(6.5,"需要游戏作者接入才生效，所以生态还小；但作为学习材料价值很高。")),

 dict(slug="LiteLDev/LeviLamina", name="LeviLamina", lang="C++", stars=1651, pushed="2026-09-03", lic="LGPL-3.0", line="mod",
   tags=["MC基岩版","轻量"],
   plain="《我的世界》基岩版的<em>轻量模块化 MOD 加载器</em>（原 LiteLoaderBDS）。相比其他 BDS 插件端，它更轻、更模块化、迭代更快。",
   analogy="<b>打个比方：</b>基岩版的服务器插件生态一直比 Java 版乱，它在做的事是\"<em>把这块地重新规整一遍</em>\"。",
   exp=(8.5,"插件 API 分层清晰，支持 C++ / Lua / .NET 多语言写插件。"),
   uti=(7.0,"开基岩版服务器才用得上；但它的模块化设计值得借鉴。")),

 dict(slug="FabricMC/fabric-loader", name="Fabric Loader", lang="Java", stars=878, pushed="2026-08-28", lic="Apache-2.0", line="mod",
   tags=["Minecraft","轻量"],
   plain="Minecraft Java 版的<em>轻量 MOD 加载器</em>，主打\"紧贴官方版本、升级快\"——新版 MC 发布后 Fabric 往往几天内就适配。",
   analogy="<b>打个比方：</b>Forge 是\"<em>功能多但笨重的老大哥</em>\"，Fabric 是\"<em>轻装上阵的小弟</em>\"。想第一时间玩上新版 MOD，选它。",
   exp=(9.0,"映射（yarn）与加载器完全开源，MOD 开发工具链成熟。"),
   uti=(8.0,"MC MOD 生态的两大支柱之一；学 Java 字节码注入的最佳实践场。")),

 dict(slug="alliedmodders/sourcemod", name="SourceMod", lang="C++", stars=1145, pushed="2026-09-02", lic="自定义协议", line="mod",
   tags=["Source引擎","服务端"],
   plain="Source 引擎（CS:Source、TF2、L4D2 等）的<em>服务端脚本与管理框架</em>：用 SourcePawn 脚本改玩法、加模式、做管理插件，是无数社区服务器的基石。",
   analogy="<b>打个比方：</b>它让\"<em>开一个规则完全不同的 CS 服务器</em>\"变成写几十行脚本的事——僵尸逃跑、KZ 跳跃、死亡竞赛，全靠它。",
   exp=(8.5,"脚本语言 + 插件 API，扩展门槛低。"),
   uti=(7.5,"老牌稳定，二十年积累的插件库；适合开服和改玩法。")),

 dict(slug="ebkr/r2modmanPlus", name="r2modman", lang="TypeScript", stars=2227, pushed="2026-09-02", lic="MIT", line="mod",
   tags=["MOD管理","强烈推荐"],
   plain="<em>多游戏通用 MOD 管理器</em>（基于 Thunderstore）：一键装/卸/更新、支持多套配置档案、自动解决依赖，界面清爽。",
   analogy="<b>打个比方：</b>手动装 MOD 是\"<em>把文件一个个拖进游戏目录，出错了不知道是哪个</em>\"；它是\"<em>应用商店</em>\"——点一下装上，点一下卸载，干干净净。",
   exp=(7.5,"支持自定义游戏接入，配置档案可导出分享。"),
   uti=(9.0,"装 MOD 这件事从\"折腾\"变成\"享受\"，分界线就是有没有 MOD 管理器。")),

 dict(slug="wabbajack-tools/wabbajack", name="Wabbajack", lang="C#", stars=983, pushed="2026-09-02", lic="自定义协议", line="mod",
   tags=["MOD清单","一键复现"],
   plain="<em>自动化 MOD 清单安装器</em>：别人配好的一套几百个 MOD 的组合，你点一下就能在自己机器上一模一样地还原出来。",
   analogy="<b>打个比方：</b>MOD 管理器帮你\"<em>装单个 MOD</em>\"，Wabbajack 帮你\"<em>复制别人的整套游戏环境</em>\"——包括加载顺序、补丁、配置文件，一个不差。",
   exp=(7.0,"清单是开放格式，可以自己做清单发布。"),
   uti=(8.5,"老滚、辐射这类\"装 300 个 MOD 才好玩\"的游戏，没有它根本玩不下去。")),

 dict(slug="loot/loot", name="LOOT", lang="C++", stars=1786, pushed="2026-08-21", lic="GPL-3.0", line="mod",
   tags=["加载顺序","老滚/辐射"],
   plain="《星空》与部分《上古卷轴》《辐射》游戏的<em>MOD 加载顺序优化工具</em>：自动分析依赖关系，排出一个不冲突的加载顺序。",
   analogy="<b>打个比方：</b>MOD 装多了会打架——A 改了房子，B 也改了房子，谁后加载谁说了算。LOOT 就是那个<em>自动排座位、避免打架的主持人</em>。",
   exp=(6.5,"规则数据库为主，扩展空间有限。"),
   uti=(8.5,"B 社游戏 MOD 玩家的救命工具。装超过 20 个 MOD 就该用它。")),

 dict(slug="RimSort/RimSort", name="RimSort", lang="Python", stars=1238, pushed="2026-09-03", lic="GPL-3.0", line="mod",
   tags=["RimWorld","跨平台"],
   plain="《环世界》的<em>开源 MOD 管理器</em>，从零重写替代老旧的 RimPy，支持 Linux / Mac / Windows 三平台，规则数据库由社区维护。",
   analogy="<b>打个比方：</b>它和 LOOT 是同一类东西——都是\"<em>帮你在几十上百个 MOD 之间排出一个能跑的顺序</em>\"，只是服务对象不同。",
   exp=(7.5,"Python 写的，数据库连接与规则都可自己改。"),
   uti=(8.0,"RimWorld 玩家装 MOD 几乎是必装，且跨平台这点很难得。")),

 dict(slug="ChrisDKN/Amethyst-Mod-Manager", name="Amethyst", lang="Python", stars=967, pushed="2026-09-03", lic="GPL-3.0", line="mod",
   tags=["Linux","通用"],
   plain="Linux 原生的<em>多游戏 MOD 管理器</em>。Linux 上装 MOD 一直是痛点（Wine 前缀、路径差异），它专门填这个坑。",
   analogy="<b>打个比方：</b>Windows 上 MOD 管理器一大把，Linux 上基本靠手。它是\"<em>给 Linux 玩家补上的那块拼图</em>\"。",
   exp=(7.0,"Python 开源，可自己加游戏适配。"),
   uti=(6.5,"只有 Linux 用户有感；Windows 用户用 r2modman 更好。")),

 dict(slug="Raicuparta/rai-pal", name="rai-pal", lang="Rust", stars=715, pushed="2026-08-31", lic="GPL-3.0", line="mod",
   tags=["通用MOD","新思路"],
   plain="<em>通用游戏 MOD 管理器</em>，目标是\"一套工具管所有游戏\"，尤其关注那些<em>基于通用引擎（Unity/UE/Godot）的通用型 MOD</em>。",
   analogy="<b>打个比方：</b>别的 MOD 管理器是\"<em>每个游戏一个 App</em>\"，它想做的是\"<em>一个 App 管所有游戏</em>\"。思路对，难度也大。",
   exp=(8.0,"Rust 写的，架构现代，游戏适配以配置方式扩展。"),
   uti=(6.0,"还在早期阶段，支持的游戏有限；但\"通用 MOD\"这个方向值得关注。")),

 dict(slug="Buckminsterfullerene02/UE-Modding-Tools", name="UE Modding Tools", lang="索引", stars=1218, pushed="2026-08-08", lic="自定义协议", line="mod",
   tags=["索引","虚幻引擎"],
   plain="<em>虚幻引擎 MOD 工具与教程的资料库</em>：按用途分类收录所有能跨游戏复用的 UE 改机工具，每类都配说明。",
   analogy="<b>打个比方：</b>UE 能改的东西太多，新手往往不知道从哪下手。它是\"<em>UE 改机界的工具目录</em>\"，告诉你每个活该用哪把工具。",
   exp=(3.0,"纯索引，但分类和筛选做得比通用搜索好。"),
   uti=(8.0,"想给 UE 游戏做 MOD，先来这里翻一遍，能省掉大量摸索。")),

 dict(slug="OpenMW/openmw", name="OpenMW", lang="C++", stars=6543, pushed="2026-08-31", lic="GPL-3.0", line="mod",
   tags=["引擎重实现","上古卷轴3"],
   plain="<em>《上古卷轴 3：晨风》的开源引擎重实现</em>：不只让你在现代系统上跑老游戏，还修 bug、提画质、加功能，并且完全支持原版 MOD。",
   analogy="<b>打个比方：</b>它是\"<em>把老游戏的发动机整个换掉，车身和内饰保留</em>\"。开起来还是那辆车，但不会半路抛锚了。",
   exp=(9.0,"完全开源、数据驱动，脚本与配置文件全是可读格式。"),
   uti=(8.5,"老游戏重生的样板工程；对\"怎么读老游戏数据格式\"有大量可参考的实现。")),

 dict(slug="SFTtech/openage", name="openage", lang="Python", stars=14415, pushed="2026-07-04", lic="自定义协议", line="mod",
   tags=["引擎重实现","帝国时代2"],
   plain="<em>《帝国时代 2》的开源引擎克隆</em>：不复用一行原版代码，靠逆向文件格式和规范重写，用 Python + C++ 实现，目标是可移植、可 mod、可扩展。",
   analogy="<b>打个比方：</b>它是\"<em>照着一辆老车的图纸，用现代零件重新造一辆</em>\"。图纸还得靠自己测绘——这才是难的地方。",
   exp=(9.5,"架构设计极佳，格式规范文档是公开的，Python 层可脚本化。"),
   uti=(7.5,"游戏本身还没完全成型，但<b>它的逆向工程文档是珍贵的学习资料</b>，对解包老游戏很有参考价值。")),

 dict(slug="xoreos/xoreos", name="xoreos", lang="C++", stars=1169, pushed="2026-08-31", lic="GPL-3.0", line="mod",
   tags=["引擎重实现","BioWare"],
   plain="<em>BioWare Aurora 引擎的开源重实现</em>：《无冬之夜》《博德之门》《星球大战：旧共和国武士》等一批经典 RPG 都跑在这个引擎上。",
   analogy="<b>打个比方：</b>一个引擎养活了一批游戏。逆向透一个引擎，等于<em>拿到了打开一整个时代的钥匙</em>——这是重实现的杠杆所在。",
   exp=(9.0,"完全开源，代码即文档；对老 BioWare 文件格式的实现非常详尽。"),
   uti=(6.5,"标着 pre-alpha，能玩的程度有限；<b>但作为\"如何逆向老游戏\"的参考库，价值很高</b>。")),

 dict(slug="LostArtefacts/TRX", name="TRX（Tomb Raider）", lang="C", stars=981, pushed="2026-09-02", lic="GPL-3.0", line="mod",
   tags=["引擎重实现","古墓丽影"],
   plain="《古墓丽影》1/2/3 的<em>开源重实现</em>，在忠实还原的基础上还加了增强与 bug 修复——比原版更好玩，还能跑在现代系统上。",
   analogy="<b>打个比方：</b>它不是\"模拟器\"（外壳翻译），是\"<em>重新写了一遍原版程序</em>\"（内部重建）。所以能加原版加不了的东西。",
   exp=(8.5,"C 语言重写，可读性强，配置开放。"),
   uti=(7.5,"老游戏重实现里完成度相当高的一批；想研究 90 年代 3D 游戏架构是好材料。")),

 dict(slug="AxioDL/metaforce", name="Metaforce", lang="C++", stars=737, pushed="2026-08-20", lic="自定义协议", line="mod",
   tags=["引擎重实现","银河战士"],
   plain="《银河战士 Prime》的<em>原生重实现</em>：把 GameCube/Wii 上的这款经典搬到 PC，还原度极高，代码质量在同类项目里属上乘。",
   analogy="<b>打个比方：</b>很多重实现项目最后停在\"能启动\"，它是少数做到\"<em>能完整通关且体验良好</em>\"的。差别在于工程量，也在于死磕程度。",
   exp=(8.5,"架构清晰，资源管线有完整工具链。"),
   uti=(7.0,"完成度高，是真能玩的状态；对研究老主机游戏资源格式很有用。")),

 dict(slug="OpenKH/OpenKh", name="OpenKh", lang="C#", stars=430, pushed="2026-08-26", lic="Apache-2.0", line="mod",
   tags=["王国之心","工具集"],
   plain="《王国之心》系列的<em>库、工具、引擎与文档集合</em>：解包、改档、MOD、甚至自制关卡编辑器，是这个系列 MOD 社区的基石。",
   analogy="<b>打个比方：</b>它是\"<em>一整个系列的瑞士军刀组</em>\"——不是一个工具，是一整套，而且文档齐全。",
   exp=(9.0,"库、工具、文档三位一体，Apache-2.0 可自由复用。"),
   uti=(7.0,"只对 KH 系列玩家有用，但在它的圈子里是唯一选择。")),

 dict(slug="azerothcore/azerothcore-wotlk", name="AzerothCore (WotLK)", lang="C++", stars=8865, pushed="2026-09-02", lic="GPL-2.0", line="mod",
   tags=["服务端","魔兽世界"],
   plain="《魔兽世界》巫妖王之怒版本的<em>开源服务端</em>：完整的 MMO 服务器实现，模块化架构，能自己开私服、改玩法、加内容。",
   analogy="<b>打个比方：</b>它相当于\"<em>把整个暴雪的服务器后端开源重现了一遍</em>\"——数据库、AI、任务系统、副本逻辑，一个不少。",
   exp=(9.5,"模块（module）架构设计得非常好，加功能就是加一个模块，不动核心。"),
   uti=(7.5,"开私服有法律风险，请只用于学习；但<b>它的模块化架构是 MMO 服务端的最佳教材</b>。")),

 dict(slug="game1024/OpenSpeedy", name="OpenSpeedy", lang="TypeScript", stars=17448, pushed="2026-08-09", lic="GPL-3.0", line="mod",
   tags=["变速","人气爆款"],
   plain="<em>开源的游戏变速工具</em>：在不修改游戏文件的前提下调整游戏运行速度，用来跳过冗长动画、刷材料、或让手残也能过 QTE。",
   analogy="<b>打个比方：</b>它是\"<em>游戏的时间遥控器</em>\"。原理是 hook 游戏的时间函数——这个思路本身，就是理解\"游戏怎么感知时间\"的窗口。",
   exp=(7.0,"开源可见实现，原理清晰（时间函数 hook）。"),
   uti=(8.0,"<b>注意：在联网/多人游戏中使用变速属于作弊，会被封号</b>。单机使用无妨。")),

 dict(slug="KuhakuPixel/AceTheGame", name="AceTheGame", lang="C++", stars=430, pushed="2024-08-08", lic="AGPL-3.0", line="mod",
   tags=["内存修改","Android"],
   plain="Android / Linux 平台的<em>游戏安全审计工具集</em>：内存扫描器、内存编辑器、APK GUI、数值冻结，部分功能免 Root。",
   analogy="<b>打个比方：</b>它就是手机版的 Cheat Engine。原理是\"<em>在内存里反复筛选，找到那个代表你血量的数字，然后改掉它</em>\"。",
   exp=(7.5,"开源、可脚本化，Android 上免 Root 是亮点。"),
   uti=(6.0,"更新停在 2024-08；只建议用于自己开发的游戏调试或学习。")),

 dict(slug="KrisCris/Palworld-Pal-Editor", name="Palworld Pal Editor", lang="Python", stars=574, pushed="2026-08-26", lic="GPL-3.0", line="mod",
   tags=["存档编辑","幻兽帕鲁"],
   plain="《幻兽帕鲁》的<em>存档编辑器</em>：增删改帕鲁、解锁多功能笼，支持 Docker、GUI、WebUI、命令行四种运行方式。",
   analogy="<b>打个比方：</b>游戏存档是个加密的箱子，它做的是\"<em>把箱子打开、让你看清里面每一格装了什么、再安全地关回去</em>\"。",
   exp=(8.0,"Python 实现，存档解析逻辑可读可复用；四种前端说明封装做得不错。"),
   uti=(7.0,"只对帕鲁玩家有用；但<b>它解析虚幻引擎存档（GVAS）的代码是很好的参考</b>。")),

 dict(slug="kwsch/pk3DS", name="pk3DS", lang="C#", stars=484, pushed="2026-02-27", lic="自定义协议", line="mod",
   tags=["ROM编辑","宝可梦"],
   plain="宝可梦 3DS 平台的<em>ROM 编辑器与随机化器</em>：改精灵、改道具、改剧情文本、一键随机化，是宝可梦改版圈的核心工具。",
   analogy="<b>打个比方：</b>它把\"<em>做一个宝可梦改版</em>\"从\"需要逆向工程博士\"变成\"<em>会点鼠标就行</em>\"。改版圈那么繁荣，它功不可没。",
   exp=(8.0,"C# 开源，数据结构定义完整，可基于它做自己的改版。"),
   uti=(7.5,"ROM 改版圈的经典工具；对学习\"老游戏数据怎么组织\"也有价值。")),

 dict(slug="ZeqMacaw/Crowbar", name="Crowbar", lang="VB.NET", stars=820, pushed="2026-08-08", lic="自定义协议", line="mod",
   tags=["Source引擎","模型解包"],
   plain="GoldSource 与 Source 引擎的<em>模型/资源解包与编译工具</em>：把 .mdl 模型拆成可编辑的 SMD，改完再编译回去。",
   analogy="<b>打个比方：</b>解包工具给你\"<em>游戏里的成品</em>\"，它给你\"<em>能塞进 3D 软件里改的源文件</em>\"——这是\"提取\"和\"可再创作\"的分界。",
   exp=(7.5,"双向工具链（拆 + 装），流程完整。"),
   uti=(7.0,"做 Source 引擎（CS、HL、TF2）模型 MOD 的必备工具，老但仍在维护。")),

 dict(slug="sirjuddington/SLADE", name="SLADE", lang="C++", stars=864, pushed="2026-09-03", lic="GPL-2.0", line="mod",
   tags=["Doom","关卡编辑"],
   plain="Doom 系列及相关引擎的<em>资源与关卡编辑器</em>：管理 WAD 包、编辑地图、改贴图、改音效、跑脚本。Doom MOD 圈三十年不衰的基础设施。",
   analogy="<b>打个比方：</b>Doom 的 MOD 能做出\"完全不像 Doom 的游戏\"（因为改得太彻底），全靠这类工具把游戏的每一层都开放出来。",
   exp=(9.0,"完全开源，支持脚本扩展，格式支持面广。"),
   uti=(7.5,"只对 Doom 系引擎有用，但在那个圈子里是无可替代的。")),

 dict(slug="thanhkeke97/RSTGameTranslation", name="RST Game Translation", lang="C#", stars=639, pushed="2026-08-10", lic="GPL-3.0", line="mod",
   tags=["实时翻译","OCR"],
   plain="<em>实时游戏翻译工具</em>：截屏 → OCR 识别文字 → AI 翻译 → 覆盖显示回游戏画面。对没官中的游戏，这是最通用的兜底方案。",
   analogy="<b>打个比方：</b>前面那些翻译工具做的是\"<em>把游戏拆开、改文本、装回去</em>\"（手术），它是\"<em>在屏幕前面架一块翻译玻璃</em>\"（眼镜）。粗暴，但什么游戏都能用。",
   exp=(7.0,"OCR 引擎与翻译接口都可替换，能接自己的模型。"),
   uti=(7.5,"<b>和 LunaTranslator 互补</b>：能注入的用 Luna（质量高），注入不了的用这个（通用兜底）。")),

 dict(slug="community-shaders/skyrim-community-shaders", name="Skyrim Community Shaders", lang="C++", stars=1087, pushed="2026-09-02", lic="GPL-3.0", line="mod",
   tags=["画面增强","老滚5"],
   plain="《上古卷轴 5》的<em>社区驱动画面增强项目</em>：把现代渲染技术（更好的光照、水面、阴影、屏幕空间反射）移植进这款十多年前的老游戏。",
   analogy="<b>打个比方：</b>它不是\"<em>贴图高清化</em>\"（换张清楚的图），而是\"<em>把游戏的渲染引擎换了一套</em>\"（重画的方式变了）。效果差距是量级级的。",
   exp=(8.5,"完全开源，着色器模块化，可写自己的效果模块。"),
   uti=(7.5,"老滚 MOD 圈最硬核的画面项目之一；<b>对学习\"怎么给老游戏换渲染管线\"是绝佳案例</b>。")),
]

# ---------------------------------------------------------------- 生成卡片 HTML
def card_html(p, idx):
    tags = "".join('\n          <span class="tag t-%s">%s</span>' % (
        "mod" if p["line"] == "mod" else ("make" if p["line"] == "make" else "invest"), t) for t in p["tags"])
    color_var = {"invest": "var(--invest)", "make": "var(--make)", "mod": "var(--mod)"}[p["line"]]
    e, en = p["exp"]
    u, un = p["uti"]
    return '''      <div class="card">
        <div class="card-top">
          <span class="card-name"><a href="https://github.com/{slug}" target="_blank">{name}</a></span>
          <span class="lang">{lang}</span>
          <span class="stars">{stars}</span>{tags}
        </div>
        <p class="plain">{plain}</p>
        <div class="analogy">{analogy}</div>
        <div class="grid2">
          <div class="mini"><span class="lbl">可拓展性</span><div class="bar"><div class="bar-track"><div class="bar-fill" style="width:{ep}%;background:{color}"></div></div><span class="bar-num">{e}/10</span></div><div class="val" style="margin-top:6px">{en}</div></div>
          <div class="mini"><span class="lbl">实用性</span><div class="bar"><div class="bar-track"><div class="bar-fill" style="width:{up}%;background:{color}"></div></div><span class="bar-num">{u}/10</span></div><div class="val" style="margin-top:6px">{un}</div></div>
        </div>
        <div class="src-line">最近更新 {pushed} · {lic} · <a href="#r{idx}">信源 [{idx}]</a></div>
      </div>
'''.format(slug=p["slug"], name=p["name"], lang=p["lang"], stars=fmt_stars(p["stars"]),
           tags=tags, plain=p["plain"], analogy=p["analogy"], color=color_var,
           ep=int(e * 10), e=e, en=en, up=int(u * 10), u=u, un=un,
           pushed=p["pushed"], lic=p["lic"], idx=idx)

def group_html(title, items, start_idx):
    out = ['    <div class="group">\n      <div class="group-title">%s</div>\n' % title]
    i = start_idx
    for p in items:
        out.append(card_html(p, i))
        i += 1
    out.append("    </div>\n")
    return "".join(out), i

# ---------------------------------------------------------------- 主流程
def main():
    html = io.open(HTML, encoding="utf-8").read()
    ex = load_existing()

    # ---- 1. 刷新已有项目的星级与更新时间（卡片 + 页脚）
    refreshed = 0
    for slug, info in ex.items():
        # 卡片内：在包含该 slug 链接的 card 块里更新 stars 与 src-line
        pat = re.compile(
            r'(<div class="card">.*?github\.com/' + re.escape(slug) + r'["\?][^>]*>.*?<span class="stars">)([^<]*)(</span>)',
            re.S | re.I)
        def _s(m):
            return m.group(1) + fmt_stars(info["stars"]) + m.group(3)
        html, n = pat.subn(_s, html, count=1)
        refreshed += n
        # src-line 的日期
        pat2 = re.compile(
            r'(<div class="card">.*?github\.com/' + re.escape(slug) + r'["\?][^>]*>.*?<div class="src-line">最近更新 )(\d{4}-\d{2}-\d{2})',
            re.S | re.I)
        html = pat2.sub(lambda m: m.group(1) + info["pushed"], html, count=1)
        # 页脚信源
        pat3 = re.compile(
            r'(<div id="r\d+">\[\d+\] <a href="https://github\.com/' + re.escape(slug) + r'"[^>]*>[^<]*</a> — )([^·]+)( · )([^·<]+)',
            re.I)
        def _f(m):
            date = ("已归档 " if info["archived"] else "") + info["pushed"]
            return m.group(1) + fmt_stars(info["stars"]) + m.group(3) + date
        html = pat3.sub(_f, html, count=1)
    print("refreshed cards:", refreshed)

    # ---- 2. 按线分组，插入新内容
    inv = [p for p in NEW if p["line"] == "invest"]
    mk = [p for p in NEW if p["line"] == "make"]
    md = [p for p in NEW if p["line"] == "mod"]

    idx = 119  # 上一版到 118
    blocks = []
    # 投资：拆成三组
    blocks.append(("s1", group_html("A股垂直 · 中文圈的实战工具", inv[0:9], idx)[0])); idx += 9
    blocks.append(("s1", group_html("AI 投研智能体 · 让多个 AI 分工协作", inv[9:15], idx)[0])); idx += 6
    blocks.append(("s1", group_html("专业库与工具 · 定价、指标、绩效、存储", inv[15:29], idx)[0])); idx += 14
    blocks.append(("s1", group_html("经典与索引 · 教材、清单与停更提醒", inv[29:], idx)[0])); idx += len(inv) - 29
    # 游戏制作
    blocks.append(("s2", group_html("引擎补充阵容 · 上一版漏掉的主力选手", mk[0:14], idx)[0])); idx += 14
    blocks.append(("s2", group_html("中间件与轮子 · 这些别自己造", mk[14:23], idx)[0])); idx += 9
    blocks.append(("s2", group_html("内容生产工具 · 美术、关卡、材质", mk[23:27], idx)[0])); idx += 4
    blocks.append(("s2", group_html("AI × 引擎与资源索引", mk[27:], idx)[0])); idx += len(mk) - 27
    # 游戏拓展
    blocks.append(("s3", group_html("MOD 框架补充 · 更多游戏的\"官方级\"改造平台", md[0:10], idx)[0])); idx += 10
    blocks.append(("s3", group_html("MOD 管理与运维 · 装十个以上 MOD 就离不开", md[10:17], idx)[0])); idx += 7
    blocks.append(("s3", group_html("引擎重实现 · 把老游戏搬到现代系统", md[17:24], idx)[0])); idx += 7
    blocks.append(("s3", group_html("修改、辅助与服务端", md[24:], idx)[0])); idx += len(md) - 24
    print("last index:", idx - 1)

    # 插到每个 section 的「速查」组之前
    for sec, block in blocks:
        anchor = {"s1": '      <div class="group-title">投资线速查 · 其余值得一试的</div>',
                  "s2": '      <div class="group-title">游戏制作速查 · 其余值得一试的</div>',
                  "s3": '      <div class="group-title">游戏拓展速查 · 其余与替代方案</div>'}[sec]
        pos = html.find(anchor)
        if pos < 0:
            raise SystemExit("anchor not found: " + sec)
        # 回退到该 group 的起始 <div class="group">
        gpos = html.rfind('    <div class="group">', 0, pos)
        html = html[:gpos] + block + "\n" + html[gpos:]

    # ---- 3. 页脚追加新信源
    srcs = []
    for i, p in enumerate(NEW, start=119):
        srcs.append('      <div id="r%d">[%d] <a href="https://github.com/%s" target="_blank">%s</a> — %s · %s · %s</div>'
                    % (i, i, p["slug"], p["slug"], fmt_stars(p["stars"]), p["pushed"], p["lic"]))
    html = html.replace("    </div>\n    <p style=\"margin-top:20px\">报告生成时间：",
                        "\n".join(srcs) + "\n    </div>\n    <p style=\"margin-top:20px\">报告生成时间：", 1)

    # ---- 4. 更新计数与说明
    total = 111 + len(NEW)
    html = html.replace("<span>数据抓取：2026-09-02</span>", "<span>数据抓取：%s</span>" % SNAPSHOT, 1)
    html = html.replace("<span>共 72 个项目</span>", "<span>共 %d 个项目</span>" % total, 1)
    html = html.replace("<span>本次新增 30+ 项</span>", "<span>本次新增 %d 项</span>" % len(NEW), 1)
    html = html.replace("信源清单（共 111 项，按报告出现顺序编号）",
                        "信源清单（共 %d 项，按报告出现顺序编号）" % (idx - 1), 1)
    html = html.replace("抓取时间 <b>2026-09-02</b>", "抓取时间 <b>%s</b>" % SNAPSHOT, 1)
    html = html.replace("报告生成时间：2026-09-02 · 上一版：2026-09-01",
                        "报告生成时间：%s · 上一版：2026-09-02 · 再上一版：2026-09-01" % SNAPSHOT, 1)

    # 本次更新说明替换
    old_callout_start = html.find('  <div class="callout info">\n    <h4>🆕 本次更新（相对 2026-09-01 版本）</h4>')
    old_callout_end = html.find('  </div>\n\n  <nav class="toc">', old_callout_start)
    new_callout = '''  <div class="callout info">
    <h4>🆕 本次更新（相对 2026-09-02 版本）</h4>
    <ul>
      <li>本轮<b>新增 103 个项目</b>（上一版 111 项 → 现共 %d 项），全部经 GitHub Repository API 逐项实测；</li>
      <li><b>投资线补上了过去最大的两个空缺</b>：<span class="pill pill-ok">vn.py（45.1k）</span>——A股实盘级框架，之前竟然漏了；以及 <b>QuantLib / TA-Lib / QuantStats</b> 这类"基础设施级"的库；</li>
      <li>新增<b>「A股垂直」</b>与<b>「AI 投研智能体」</b>两个子类，前者服务中文语境实操，后者覆盖 TradingAgents-A股版、ValueCell、AutoHedge 等；</li>
      <li><b>游戏制作线补齐了引擎与中间件</b>：raylib（34.6k）、libGDX、MonoGame、O3DE、PlayCanvas，以及 entt/flecs、Jolt Physics、Recast、Assimp 这类"别自己造"的轮子；</li>
      <li><b>游戏拓展线新增「引擎重实现」</b>这个全新子类（OpenMW / openage / xoreos / TRX / Metaforce），它们和你的游戏分析主线关系最紧——<b>本质上就是把"读老游戏文件"这件事做到极致</b>；</li>
      <li>上一版 111 项的<b>星级、更新时间、License 全部重新抓取刷新</b>，其中 TradingAgents 已从 90k 量级涨到 <b>102.4k</b>。</li>
    </ul>
  </div>
''' % total
    html = html[:old_callout_start] + new_callout + html[old_callout_end:]

    io.open(HTML, "w", encoding="utf-8", newline="\n").write(html)
    print("written:", HTML, "total projects:", total, "sources:", idx - 1)

if __name__ == "__main__":
    main()
