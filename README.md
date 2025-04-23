# TCCC New Beverage Product Analysis

## Intro
FMCG (Fast-Moving Consumer Goods) companies frequently launch new products—it's normal for them to release new items every month. For large corporations, every action must serve a clear purpose. A product that costs millions of dollars to develop and launch must fulfill at least one strategic goal:

(1) Stay Competitive: The market is highly saturated. Even top companies must constantly evolve just to maintain their position.

(2) Meet Changing Consumer Needs: Trends, preferences, and lifestyles shift rapidly. Many FMCG products are designed to be temporary, catering to seasonal or short-term demands.

(3) Drive Attention and Revenue: Whether short-lived or permanent, new products can bring significant profits or create jobs during clearance efforts. Many experts believe it's impossible to predict which products will succeed, so companies often follow a high-launch-volume strategy—despite the risk of wasting millions.

From my perspective, product innovation is essential for FMCG companies to stay competitive and resilient in this fast-changing market. The real question is: which product should be launched?

## Tools Used
- Python (pandas, matplotlib)
- Jupyter Notebook

## Steps
1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Visualization of Key Insights

## Results
- Identified key demographic segments.
- Highlighted trends in purchasing behavior.

## Dataset

The raw dataset is located in the data/ folder as raw_data.csv.
It contains 9,973 rows and the following columns:


1. Region: Geographic location (e.g., North, South, Central) with inconsistent capitalization (e.g., "NORTH" vs. "north").
2. Sales Channel: Sales channels such as Modern Trade or Traditional Trade.
3. Company/Provider: Beverage manufacturers, including major and small companies, with some small companies disappearing over time.
4. Category: Beverage categories (e.g., Water, Tea, Soft Drinks) with mixed formatting (e.g., "TEA" vs. "Tea").
5. Segment: Product subcategories (e.g., flavored water, diet soda).
6. Volume Sales (Liters): Sales volume, which may include numbers stored as strings and inconsistent units like liters or kiloliters.
7. Avg Price Per Liter (VND): Average price per liter, containing extreme outliers and inconsistencies.
8. Growth Rate (%): Growth percentage, with placeholders like "unknown" and irregular values.
9. Numeric Distribution (%): Percentage of stores stocking the product.
10. Weighted Distribution (%): Sales-weighted distribution of the product across stores.
11. Out-of-Stock Rate (%): Percentage of time the product is unavailable, with some extreme values.
12. Market Share (%): Share of the market held by the product or company.
13. Share of Shelf (%): Percentage of shelf space occupied by the product.
14. Trial Rate (%): Percentage of consumers who tried the product.
15. Repeat Rate (%): Percentage of consumers who purchased the product again.
16. Sales Value (USD): Total sales in USD, with some values stored as strings or containing extreme outliers.
17. Time: The sales timeframe, containing inconsistent formats (e.g., "2021-08-01" vs. "August 2021").
18. Volume Sales: A supplementary column with mixed units and formats for volume sales (e.g., "70000 liters" vs. "70 kiloliters").

### Notes:
- There are some missing values in the dataset, which will be addressed during the analysis phase.
  
## Setup
To run this project:
```bash
pip install -r requirements.txt
jupyter notebook


