from dataclasses import dataclass
from typing import List, Tuple, Dict

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


@dataclass
class ModelResult:
    model: RandomForestRegressor
    metrics: Dict[str, float]
    feature_importances: pd.DataFrame


class TrialRepeatModeler:
    """
    Train and evaluate models to predict KPIs such as trial rate, repeat rate, or market share.
    """

    def __init__(
        self,
        target_col: str,
        feature_cols: List[str],
        test_size: float = 0.2,
        random_state: int = 42,
    ):
        self.target_col = target_col
        self.feature_cols = feature_cols
        self.test_size = test_size
        self.random_state = random_state

    def train_model(self, df: pd.DataFrame) -> ModelResult:
        """
        Train a RandomForestRegressor and return model and metrics.
        """
        data = df.dropna(subset=[self.target_col] + self.feature_cols).copy()

        X = data[self.feature_cols].values
        y = data[self.target_col].values

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
        )

        model = RandomForestRegressor(
            n_estimators=300,
            max_depth=None,
            random_state=self.random_state,
            n_jobs=-1,
        )
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        metrics = {
            "rmse": float(np.sqrt(mean_squared_error(y_test, y_pred))),
            "mae": float(mean_absolute_error(y_test, y_pred)),
            "r2": float(r2_score(y_test, y_pred)),
        }

        feature_importances = pd.DataFrame(
            {
                "feature": self.feature_cols,
                "importance": model.feature_importances_,
            }
        ).sort_values("importance", ascending=False)

        return ModelResult(
            model=model,
            metrics=metrics,
            feature_importances=feature_importances,
        )
