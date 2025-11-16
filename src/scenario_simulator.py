from dataclasses import dataclass
from typing import Dict, List

import numpy as np
import pandas as pd


@dataclass
class ScenarioConfig:
    """
    Configuration for a launch scenario.
    """
    name: str
    base_price_per_liter: float
    price_multiplier: float
    base_distribution_pct: float
    distribution_multiplier: float
    promo_depth_pct: float
    oos_rate: float
    channel_mix: Dict[str, float]  # example: {"Modern Trade": 0.5, "General Trade": 0.5}


class ScenarioSimulator:
    """
    Simple simulation engine to model sales under different scenarios.
    This is a toy model that uses elasticities and multipliers, not a production forecast.
    """

    def __init__(
        self,
        base_df: pd.DataFrame,
        price_elasticity: float = -1.2,
        distribution_elasticity: float = 0.8,
        promo_lift_per_point: float = 0.02,
    ):
        self.base_df = base_df.copy()
        self.price_elasticity = price_elasticity
        self.distribution_elasticity = distribution_elasticity
        self.promo_lift_per_point = promo_lift_per_point

    def simulate_scenario(self, config: ScenarioConfig) -> pd.DataFrame:
        """
        Simulate sales volume and value under a given scenario.

        Returns a dataframe with simulated KPIs by channel.
        """
        df = self.base_df.copy()

        # Use base distribution and price from config as starting values
        df["price_per_liter"] = config.base_price_per_liter * config.price_multiplier
        df["distribution_pct"] = (
            config.base_distribution_pct * config.distribution_multiplier
        )

        # Base volume anchor (could be mean historical volume)
        if "sales_volume_liters" in df.columns:
            base_volume = df["sales_volume_liters"].mean()
        else:
            base_volume = 10000.0

        # Price effect
        price_effect = (config.price_multiplier) ** self.price_elasticity

        # Distribution effect
        distribution_effect = (config.distribution_multiplier) ** self.distribution_elasticity

        # Promo effect
        promo_effect = 1 + self.promo_lift_per_point * config.promo_depth_pct

        # Out of stock effect (simple linear loss)
        oos_effect = 1 - config.oos_rate

        df["simulated_volume_total"] = (
            base_volume * price_effect * distribution_effect * promo_effect * oos_effect
        )

        # Allocate volume by channel mix
        channel_rows: List[pd.DataFrame] = []
        for channel, share in config.channel_mix.items():
            channel_df = pd.DataFrame(
                {
                    "scenario_name": [config.name],
                    "channel": [channel],
                    "simulated_volume_liters": [df["simulated_volume_total"].iloc[0] * share],
                    "price_per_liter": [df["price_per_liter"].iloc[0]],
                }
            )
            channel_rows.append(channel_df)

        result = pd.concat(channel_rows, ignore_index=True)
        result["simulated_sales_value"] = (
            result["simulated_volume_liters"] * result["price_per_liter"]
        )

        return result

    def compare_scenarios(self, configs: List[ScenarioConfig]) -> pd.DataFrame:
        """
        Run and concatenate multiple scenarios.
        """
        dfs = [self.simulate_scenario(cfg) for cfg in configs]
        return pd.concat(dfs, ignore_index=True)

