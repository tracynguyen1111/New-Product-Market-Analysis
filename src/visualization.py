import matplotlib.pyplot as plt
import pandas as pd
from typing import List


def plot_distribution_by_category(df: pd.DataFrame, category_col: str, value_col: str) -> None:
    """
    Bar chart of average value by category.
    """
    grouped = df.groupby(category_col)[value_col].mean().reset_index()

    plt.figure(figsize=(8, 5))
    plt.bar(grouped[category_col], grouped[value_col])
    plt.xticks(rotation=45, ha="right")
    plt.xlabel(category_col)
    plt.ylabel(f"Average {value_col}")
    plt.title(f"Average {value_col} by {category_col}")
    plt.tight_layout()
    plt.show()


def plot_kpi_trend(df: pd.DataFrame, time_col: str, value_col: str) -> None:
    """
    Line chart for KPI trend over time.
    """
    grouped = df.groupby(time_col)[value_col].mean().reset_index()

    plt.figure(figsize=(8, 5))
    plt.plot(grouped[time_col], grouped[value_col], marker="o")
    plt.xlabel(time_col)
    plt.ylabel(value_col)
    plt.title(f"{value_col} over {time_col}")
    plt.tight_layout()
    plt.show()


def plot_feature_importance(fi_df: pd.DataFrame, top_n: int = 10) -> None:
    """
    Horizontal bar chart for feature importances.
    """
    fi = fi_df.head(top_n).sort_values("importance", ascending=True)

    plt.figure(figsize=(8, 5))
    plt.barh(fi["feature"], fi["importance"])
    plt.xlabel("Importance")
    plt.title(f"Top {top_n} feature importances")
    plt.tight_layout()
    plt.show()
