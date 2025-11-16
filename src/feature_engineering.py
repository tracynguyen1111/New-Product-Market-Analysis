import pandas as pd
from typing import List, Optional
from sklearn.preprocessing import OneHotEncoder


class FeatureEngineer:
    """
    Create FMCG specific features and encoded variables.
    """

    def __init__(self):
        self.encoder: Optional[OneHotEncoder] = None
        self.encoded_cols: Optional[List[str]] = None

    def add_business_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add derived features that reflect business logic.
        """
        df = df.copy()

        # Price normalized by simple global mean
        if "price_per_liter" in df.columns:
            mean_price = df["price_per_liter"].mean()
            df["price_per_liter_norm"] = df["price_per_liter"] / mean_price

        # Distribution velocity: volume per distribution point
        if {"sales_volume_liters", "distribution_pct"}.issubset(df.columns):
            df["distribution_velocity"] = df["sales_volume_liters"] / (
                df["distribution_pct"].replace(0, pd.NA)
            )

        # Trial to repeat ratio
        if {"trial_rate", "repeat_rate"}.issubset(df.columns):
            df["trial_repeat_ratio"] = df["trial_rate"] / (
                df["repeat_rate"].replace(0, pd.NA)
            )

        return df

    def fit_encoder(self, df: pd.DataFrame, cat_cols: List[str]) -> None:
        """
        Fit one hot encoder on selected categorical columns.
        """
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        self.encoder.fit(df[cat_cols])
        self.encoded_cols = list(self.encoder.get_feature_names_out(cat_cols))

    def transform_with_encoder(
        self, df: pd.DataFrame, cat_cols: List[str]
    ) -> pd.DataFrame:
        """
        Apply encoder and return dataframe with encoded columns appended.
        """
        if self.encoder is None:
            raise ValueError("Encoder is not fitted. Call fit_encoder first.")

        df = df.copy()
        encoded_array = self.encoder.transform(df[cat_cols])
        encoded_df = pd.DataFrame(encoded_array, columns=self.encoded_cols, index=df.index)

        result = pd.concat([df.drop(columns=cat_cols), encoded_df], axis=1)
        return result
