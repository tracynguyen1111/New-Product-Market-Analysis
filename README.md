# TCCC New Beverage Product Analysis

## Intro
FMCG (Fast-Moving Consumer Goods) companies frequently launch new products, it's normal for them to release new items every month. For large corporations, every action must serve a clear purpose. A product that costs millions of dollars to develop and launch must fulfill at least one strategic goal:

(1) Protect their position: Category competition is intense. Even market leaders must refresh their portfolio to hold share and visibility on shelves.

(2) Meet Changing Consumer Needs: Preferences around sugar, flavor, packaging, and consumption occasions shift quickly. Many innovations are intentionally short-term to capture seasonal or emerging trends.

(3) Drive trial, revenue, and learning: Whether short-lived or permanent, new products can bring significant profits or create jobs during clearance efforts. Many experts believe it's impossible to predict which products will succeed, so companies often follow a high-launch-volume strategy—despite the risk of wasting millions.

From my perspective, Product innovation is not about predicting a “perfect” product—it's about making disciplined decisions with limited information and allocating resources to the concepts with the highest potential. But even to the biggest player,resources are always limited, which types of innovations should be prioritized for launch and support?

From a business perspective, the goals are to:
- Identify high potential innovation types  
- Understand which channels and segments overperform  
- Quantify the drivers behind trial, repeat, and market share  
- Simulate financial outcomes under different investment scenarios  

By apply a technical perspective, the goals are to:
- Apply unsupervised learning for segmentation  
- Train and evaluate predictive models on key KPIs  
- Implement a simple scenario simulation engine that turns business assumptions into numbers  
- Organize the project code in a modular and reusable way

## Disclaimer
All datasets used in this project are fully synthetic and generated solely for learning purpose.
Nothing in this repository reflects real data, internal information, or proprietary processes from any of my past employers.
I do not represent, speak for, or disclose any information on behalf of any past employer.

## Dataset

The dataset is fully synthetic and designed to resemble typical FMCG innovation data. Each row represents a beverage innovation with fields in three groups:

### Innovation Attributes

- `innovation_id`  
- `innovation_type` (New Flavor, Zero Sugar, Upsize, Downsize, Limited Edition, Pack Redesign)  
- `category` and `segment`  
- `region` (e.g. North, Central, South)  
- `channel` (Modern Trade, General Trade, On Premise)  
- `launch_week` and `weeks_on_shelf`  

### Performance Metrics

- `sales_volume_liters`  
- `sales_value`  
- `price_per_liter`  
- `distribution_pct`  
- `oos_rate` (out of stock)  
- `trial_rate`  
- `repeat_rate`  
- `market_share_pct`  

### Optional Consumer Data 

- Demographics and income band  
- Consumption frequency  
- Flavor and sugar preference  
- Price sensitivity  

Some values are missing by design to reflect real world data.

---

## Tools and Tech Stack

- **Language**: Python  
- **Core libraries**:  
  - `pandas`, `numpy` for data wrangling  
  - `matplotlib`, `seaborn` for visualization  
  - `scikit-learn` for modeling and segmentation  
  - `scipy` for statistical tests  

Files are organized into:
- **`src/`** for reusable code modules  
- **`notebooks/`** for step by step analysis  
- **`data/`** for raw and processed data  
- **`reports/`** for presentation ready outputs  

---

## 5. Project Structure

```text
.
├── data/
│   ├── raw/
│   │   ├── beverage_innovations_raw.csv
│   │   └── consumer_survey_raw.csv         
│   └── processed/
│       ├── beverage_innovations_clean.csv
│       └── consumer_survey_clean.csv        
│
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_feature_engineering_and_segments.ipynb
│   ├── 03_modeling_trial_repeat_share.ipynb
│   └── 04_scenario_simulation_dashboard.ipynb
│
├── reports/
│   └── new_beverage_insights_summary.pdf   
│
├── src/
│   ├── data_prep.py
│   ├── feature_engineering.py
│   ├── modeling.py
│   ├── scenario_simulator.py
│   └── visualization.py
│
├── requirements.txt
└── README.md
## License
This project is released under the MIT License. See the `LICENSE` file for details.

