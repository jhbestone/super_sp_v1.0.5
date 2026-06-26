"""结果写入器：输出 JSON、HTML、Excel 报告"""
import pandas as pd
import json
import os
import re
from datetime import datetime

def is_asin(search_term):
    if not search_term or pd.isna(search_term):
        return False
    search_term = str(search_term).strip().upper()
    if len(search_term) == 10 and re.match(r'^[A-Z0-9]{10}$', search_term):
        return True
    return False

STRATEGY_INSIGHT_MAP = {
    "🚀 进攻型：加大投放，提高竞价，抢占流量": "增加预算和溢价，优先推广",
    "🚀 进攻型：逐步提高竞价，观察趋势": "提高竞价，增加曝光机会，优先推广",
    "📊 观察型：维持现状，持续监控": "增加预算测试潜力，尝试提升转化率：优化详情页",
    "🚫 防守型：降低竞价或暂停，避免浪费": "降低竞价，控制成本，防止进一步亏损",
    "🚫 防守型：降低出价，优化广告素材": "降低竞价，优化后重新测试",
    "❌ 立即否定：添加为否定关键词/ASIN": "立即停止投放，添加为否定关键词",
    "❌ 低效流量：建议否定或降低竞价": "考虑否定或降低竞价，减少浪费",
    "📊 待观察：数据不足，持续监控": "数据不足，建议持续观察",
    "无需操作（已暂停/归档）": "已暂停/归档，无需操作"
}

def get_strategy_insight(strategy_text):
    for key, value in STRATEGY_INSIGHT_MAP.items():
        if key in strategy_text:
            return value
    return strategy_text[:30]

def generate_strict_json(df, json_path):
    records = []
    for idx, row in df.iterrows():
        portfolio = row.get("portfolio_name", "")
        if portfolio == "-" or pd.isna(portfolio) or str(portfolio).strip() == "":
            portfolio = "No Portfolio"
        strategy_text = row.get("建议策略", "")
        records.append({
            "类型": row.get("类型", ""),
            "广告组合": portfolio,
            "广告活动名称": row.get("campaign_name", ""),
            "广告组名称": row.get("ad_group_name", ""),
            "客户搜索词/ASIN": row.get("search_term", ""),
            "建议定向策略": row.get("建议定向策略", ""),
            "匹配类型": row.get("match_type", ""),
            "建议策略洞察": get_strategy_insight(strategy_text),
            "cost": float(row.get("cost_all", 0) or 0),
            "sales": float(row.get("sales_all", 0) or 0),
            "orders": int(row.get("orders_all", 0) or 0),
            "clicks": int(row.get("clicks_all", 0) or 0)
        })
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return records

COL_CN = {
    "campaign_name": "广告活动名称",
    "portfolio_name": "广告组合名称",
    "ad_group_name": "广告组名称",
    "search_term": "客户搜索词/ASIN",
    "match_type": "匹配类型",
    "targeting": "投放",
    "type": "类型",
    "类型": "类型",
    "建议定向策略": "建议定向策略",
    "建议竞价策略": "建议竞价策略",
    "建议投放位置": "建议投放位置",
    "建议匹配类型": "建议匹配类型",
    "建议策略": "建议策略",
    "cost_all": "花费(30天)",
    "sales_all": "销售额(30天)",
    "orders_all": "订单(30天)",
    "clicks_all": "点击(30天)",
    "acos_all": "ACoS(30天)",
    "ctr_all": "CTR(30天)",
    "impressions_all": "展示(30天)",
    "status_flag": "状态标记",
    "status_reason": "状态原因"
}

def calculate_kpis(df):
    total_cost = df["cost_all"].sum() if "cost_all" in df.columns else 0
    total_sales = df["sales_all"].sum() if "sales_all" in df.columns else 0
    total_orders = df["orders_all"].sum() if "orders_all" in df.columns else 0
    total_clicks = df["clicks_all"].sum() if "clicks_all" in df.columns else 0
    acos = (total_cost / total_sales * 100) if total_sales > 0 else 0
    avg_cpc = (total_cost / total_clicks) if total_clicks > 0 else 0
    return {
        "TOTAL_COST": "${:,.2f}".format(total_cost),
        "TOTAL_SALES": "${:,.2f}".format(total_sales),
        "TOTAL_ORDERS": "{:,}".format(int(total_orders)),
        "ACOS": "{:.1f}%".format(acos),
        "AVG_CPC": "${:.2f}".format(avg_cpc)
    }

def calculate_spend_structure(df):
    df = df.copy()
    if "search_term" in df.columns:
        search_col = "search_term"
    else:
        return {
            "asin_no_order": 0, "asin_has_order": 0,
            "keyword_total": 0, "keyword_no_order": 0, "keyword_has_order": 0,
            "high_click_no_order": 0, "low_click_no_order": 0,
            "keyword_no_order_pct": 0, "high_click_pct": 0, "low_click_pct": 0
        }
    df["is_asin"] = df[search_col].apply(is_asin)
    cost_col = "cost_all" if "cost_all" in df.columns else "cost"
    orders_col = "orders_all" if "orders_all" in df.columns else "orders"
    clicks_col = "clicks_all" if "clicks_all" in df.columns else "clicks"

    asin_no_order = df[(df["is_asin"] == True) & (df[orders_col] == 0)][cost_col].sum()
    asin_has_order = df[(df["is_asin"] == True) & (df[orders_col] > 0)][cost_col].sum()
    keyword_total = df[df["is_asin"] == False][cost_col].sum()
    keyword_no_order = df[(df["is_asin"] == False) & (df[orders_col] == 0)][cost_col].sum()
    keyword_has_order = df[(df["is_asin"] == False) & (df[orders_col] > 0)][cost_col].sum()
    high_click_no_order = df[(df["is_asin"] == False) & (df[orders_col] == 0) & (df[clicks_col] > 17)][cost_col].sum()
    low_click_no_order = df[(df["is_asin"] == False) & (df[orders_col] == 0) & (df[clicks_col] < 5)][cost_col].sum()
    keyword_no_order_pct = (high_click_no_order / keyword_total * 100) if keyword_total > 0 else 0
    high_click_pct = (high_click_no_order / keyword_total * 100) if keyword_total > 0 else 0
    low_click_pct = (low_click_no_order / keyword_total * 100) if keyword_total > 0 else 0

    return {
        "asin_no_order": asin_no_order, "asin_has_order": asin_has_order,
        "asin_total": asin_no_order + asin_has_order,
        "keyword_total": keyword_total, "keyword_no_order": keyword_no_order,
        "keyword_has_order": keyword_has_order,
        "high_click_no_order": high_click_no_order, "low_click_no_order": low_click_no_order,
        "keyword_no_order_pct": keyword_no_order_pct,
        "high_click_pct": high_click_pct, "low_click_pct": low_click_pct
    }

def write_excel(df, excel_path):
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        export_df = df.copy()
        export_df.columns = [COL_CN.get(c, c) for c in export_df.columns]
        export_df.to_excel(writer, index=False, sheet_name="全量数据")
        total_cost = df["cost_all"].sum() if "cost_all" in df.columns else 0
        total_sales = df["sales_all"].sum() if "sales_all" in df.columns else 0
        total_orders = df["orders_all"].sum() if "orders_all" in df.columns else 0
        total_clicks = df["clicks_all"].sum() if "clicks_all" in df.columns else 0
        total_records = len(df)
        acos = (total_cost / total_sales * 100) if total_sales > 0 else 0
        kpi_data = {
            "指标": ["记录数", "总花费", "总销售额", "总订单数", "总点击量", "整体ACoS", "平均CPC"],
            "数值": [
                total_records, round(total_cost, 2), round(total_sales, 2),
                int(total_orders), int(total_clicks), f"{acos:.1f}%",
                f"${(total_cost / total_clicks):.2f}" if total_clicks > 0 else "$0.00"
            ]
        }
        kpi_df = pd.DataFrame(kpi_data)
        kpi_df.to_excel(writer, index=False, sheet_name="汇总统计")
        attack_df = df[df["类型"].str.contains("超级|高潜力", na=False)]
        attack_df_cn = attack_df.copy()
        attack_df_cn.columns = [COL_CN.get(c, c) for c in attack_df_cn.columns]
        attack_df_cn.to_excel(writer, index=False, sheet_name="进攻型策略")
        defend_df = df[df["类型"].str.contains("无效|低效|无竞争力|高竞争", na=False)]
        defend_df_cn = defend_df.copy()
        defend_df_cn.columns = [COL_CN.get(c, c) for c in defend_df_cn.columns]
        defend_df_cn.to_excel(writer, index=False, sheet_name="防守型策略")

def generate_dashboard_html(json_data, template_path, output_path, df=None, search_file_name=None):
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
    json_str = json.dumps(json_data, ensure_ascii=False, indent=2)
    html = re.sub(
        r"const mockData = \[.*?\];",
        "const mockData = " + json_str + ";",
        html, count=1, flags=re.DOTALL
    )
    if df is not None:
        kpis = calculate_kpis(df)
        for key, value in kpis.items():
            html = html.replace("{{" + key + "}}", value)
        spend_struct = calculate_spend_structure(df)
        html = html.replace("{{ASIN_NO_ORDER}}", "${:,.2f}".format(spend_struct["asin_no_order"]))
        html = html.replace("{{ASIN_HAS_ORDER}}", "${:,.2f}".format(spend_struct["asin_has_order"]))
        html = html.replace("{{ASIN_TOTAL}}", "${:,.2f}".format(spend_struct["asin_total"]))
        html = html.replace("{{KEYWORD_NO_ORDER}}", "${:,.2f}".format(spend_struct["keyword_no_order"]))
        html = html.replace("{{KEYWORD_HAS_ORDER}}", "${:,.2f}".format(spend_struct["keyword_has_order"]))
        html = html.replace("{{KEYWORD_TOTAL}}", "${:,.2f}".format(spend_struct["keyword_total"]))
        html = html.replace("{{KEYWORD_NO_ORDER_PCT}}", "{:.2f}%".format(spend_struct["keyword_no_order_pct"]))
        html = html.replace("{{HIGH_CLICK_PCT}}", "{:.2f}%".format(spend_struct["high_click_pct"]))
        html = html.replace("{{LOW_CLICK_PCT}}", "{:.2f}%".format(spend_struct["low_click_pct"]))
    data_source = search_file_name if search_file_name else "系统解析"
    html = html.replace("数据来源：系统解析", f"数据来源：{data_source}")
    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = html.replace("{{GENERATED_TIME}}", generated_time)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 可视化大屏已生成：{output_path}")
