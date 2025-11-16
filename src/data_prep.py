import pandas as pd
from pathlib import Path
from typing import Tuple


class DataLoaderCleaner:
    """
    Load and clean raw data.
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)

    def load_raw_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load raw beverage innovations and optional consumer survey data.
        """
        innovations_path = self.data_dir / "raw" / "beverage_innovations_raw.csv"
        consumer_path = self.data_dir / "raw" / "consumer_survey_raw.csv"

        innovations = pd.read_csv(innovations_path)

        try:
            consumers = pd.read_csv(consumer_path)
        except FileNotFoundError:
            consumers = pd.DataFrame()

        return innovations, consumers

    def clean_innovations(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Basic cleaning for innovations:
        - Standardize string labels
        - Handle missing values
        - Remove extreme outliers
        """
        df = df.copy()

        # Strip and lower string columns
        str_cols = df.select_dtypes(include="object").columns
        for col in str_cols:
            df[col] = df[col].str.strip()

        # Example: fill missing distribution with median
        if "distribution_pct" in df.columns:
            df["distribution_pct"] = df["distribution_pct"].fillna(
                df["distribution_pct"].median()
            )

        # Example: clip price per liter to a reasonable range
        if "price_per_liter" in df.columns:
            df["price_per_liter"] = df["price_per_liter"].clip(lower=0)

        return df

    def clean_consumers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Basic cleaning for consumer survey data.
        """
        if df.empty:
            return df

        df = df.copy()

        # Example: fill missing income_band with "Unknown"
        if "income_band" in df.columns:
            df["income_band"] = df["income_band"].fillna("Unknown")

        return df

    def save_processed(
        self, innovations: pd.DataFrame, consumers: pd.DataFrame
    ) -> None:
        """
        Save cleaned data to processed folder.
        """
        processed_dir = self.data_dir / "processed"
        processed_dir.mkdir(parents=True, exist_ok=True)

        innovations.to_csv(
            processed_dir / "beverage_innovations_clean.csv", index=False
        )

        if not consumers.empty:
            consumers.to_csv(
                processed_dir / "consumer_survey_clean.csv", index=False
            )
