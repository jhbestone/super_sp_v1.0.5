# Super SP v1.0.5 - 亚马逊广告全景分析系统

> 基于 AI 智能分类的广告数据分析工具，支持可视化大屏、否定关键词挖掘、花费结构分析等功能，采用Vercel 开源的设计系统开源设计可视化面板

## 功能特性

- **14 维度分类**：自动将广告数据分类为超级/高潜力/次级潜力/无效/低效/无竞争力/高竞争 关键词和 ASIN
- **趋势分析**：近 7 天 vs 前 23 天对比，识别上升/下降趋势
- **状态核查**：自动检测暂停/归档状态
- **策略生成**：根据分类自动生成投放、竞价、位置、匹配类型建议
- **可视化大屏**：KPI 卡片 + 14 维分类侧边栏 + 排序筛选 + 分页 + 一键导出 CSV
- **多格式输出**：JSON（13 字段含指标）、Excel（4 个 Sheet）、HTML 可视化面板
- **花费结构分析**：ASIN/关键词 ~ 出单/不出单 花费分布
- **否定关键词挖掘**：手动提取 + 自动筛选（高点击无转化/低 CTR/高 ACoS）

## 快速开始

### 环境要求
- Python 3.10+
- pandas
- openpyxl

### 安装依赖
```bash
pip install pandas openpyxl
```

### 运行分析
```bash
# Windows
run.bat

# 或直接运行
python generate.py
```

### 输出文件
| 文件 | 说明 |
|------|------|
| `output/dashboard.html` | 可视化大屏（浏览器打开） |
| `output/report.xlsx` | Excel 报告（4 个 Sheet） |
| `output/analysis.json` | JSON 数据（含指标字段） |

## 项目结构

```
super_sp_v1.0/
├── generate.py           # 主入口脚本（7步流水线）
├── report_loader.py      # 报告加载器（读取/清洗/合并 Excel）
├── trend_engine.py       # 趋势引擎（30天窗口计算）
├── classifier.py         # 14 维度分类器（可配置阈值）
├── strategy_mapper.py    # 策略映射器（分类→4维度策略）
├── status_auditor.py     # 状态核查器（暂停/归档检测）
├── writer.py             # 结果写入器（JSON + Excel + HTML）
├── negative_keywords.py  # 否定关键词挖掘模块（手动/自动）
├── template.html         # 可视化大屏模板
├── run.bat               # Windows 启动器
├── data/                 # 输入目录：放3份Excel报告
├── output/               # 输出目录（运行时自动生成）
└── README.md
```

## 配置说明

### 数据文件要求
将亚马逊广告报告放入 `data/` 目录：
- 搜索词报告（必需）
- 广告位报告（可选）
- 推广商品报告（可选）

### 自定义分类阈值
编辑 `classifier.py` 中的 `THRESHOLDS` 字典：
- `target_acos`: 目标 ACoS（默认 0.30）
- `super_orders_min`: 超级词最低订单数（默认 10）
- `invalid_clicks_min`: 无效词最低点击数（默认 10）

### 可视化大屏功能
- **KPI 卡片**：总花费/总销售额/总订单数/整体 ACoS/平均 CPC（动态更新）
- **14 维分类侧边栏**：按类型切换视图，显示每种分类的计数
- **筛选器**：搜索关键词、广告组合（联动）、广告活动（联动）、匹配类型
- **排序**：点击任意表头排序（asc/desc/null 三态切换）
- **分页**：50 条/页，支持跳转
- **导出**：一键导出当前过滤结果为 CSV

## 14 维度分类

| 优先级 | 类型 | 操作建议 |
|--------|------|----------|
| 🚀 进攻 | 超级关键词、超级ASIN | 立即加大预算 |
| 📈 优化 | 低效关键词、低效ASIN | 优化后继续投放 |
| 📊 观察 | 次级潜力关键词、次级潜力ASIN | 持续观察 |
| ⚠️ 否定 | 无竞争力、无竞争力ASIN | 考虑否定 |
| ❌ 否定 | 无效关键词、无效ASIN | 立即否定 |

## 许可证
MIT License

## 作者
GitHub: [@jhbestone](https://github.com/jhbestone)
