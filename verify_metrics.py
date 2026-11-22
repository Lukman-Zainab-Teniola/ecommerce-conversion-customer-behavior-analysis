"""Reproduce descriptive KPIs from the e-commerce session CSV.

Companion verification script, not a claim that Python built the Power BI dashboard.
Usage: python analysis/verify_metrics.py data/ecommerce_user_behavior_sessions.csv
"""
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = {
    "session_id", "visit_date", "country", "device_type", "traffic_source",
    "product_category_viewed", "pages_viewed", "time_on_site_minutes",
    "added_to_cart", "purchased", "order_value_usd",
}


def main(path: Path) -> None:
    df = pd.read_csv(path)
    missing_columns = REQUIRED - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")
    sessions = df["session_id"].nunique()
    purchases = int(df["purchased"].sum())
    revenue = df["order_value_usd"].sum()
    print(f"Rows: {len(df):,} | Unique sessions: {sessions:,}")
    print(f"Missing cells: {int(df.isna().sum().sum())} | Duplicate rows: {int(df.duplicated().sum())} | Duplicate session IDs: {int(df.session_id.duplicated().sum())}")
    print(f"Purchases: {purchases:,} | Cart additions: {int(df.added_to_cart.sum()):,}")
    print(f"Conversion rate: {purchases / sessions:.2%}")
    print(f"Revenue: ${revenue:,.2f} | Average order value: ${revenue / purchases:,.2f}")
    print("\nEngagement by purchase status:")
    print(df.groupby("purchased")[["pages_viewed", "time_on_site_minutes"]].mean().round(2).to_string())
    for col in ["traffic_source", "device_type", "product_category_viewed", "country"]:
        print(f"\nConversion rate by {col}:")
        print((df.groupby(col)["purchased"].mean().sort_values(ascending=False) * 100).round(2).to_string())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    main(args.csv_path)
