# New Beverage Product Analysis

## Intro
This project analyzes consumer preferences and market trends for launching a new beverage product. All data used is simulated and does not reflect anything from the companies I have worked for.

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

Dataset Description
The raw dataset is located in the data/ folder as raw_data.csv.
It contains 9,973 rows and the following columns:

Region: Geographic location (e.g., North, South, Central) with inconsistent capitalization (e.g., "NORTH" vs. "north").
Sales Channel: Sales channels such as Modern Trade or Traditional Trade.
Company/Provider: Beverage manufacturers, including major and small companies, with some small companies disappearing over time.
Category: Beverage categories (e.g., Water, Tea, Soft Drinks) with mixed formatting (e.g., "TEA" vs. "Tea").
Segment: Product subcategories (e.g., flavored water, diet soda).
Volume Sales (Liters): Sales volume, which may include numbers stored as strings and inconsistent units like liters or kiloliters.
Avg Price Per Liter (VND): Average price per liter, containing extreme outliers and inconsistencies.
Growth Rate (%): Growth percentage, with placeholders like "unknown" and irregular values.
Numeric Distribution (%): Percentage of stores stocking the product.
Weighted Distribution (%): Sales-weighted distribution of the product across stores.
Out-of-Stock Rate (%): Percentage of time the product is unavailable, with some extreme values.
Market Share (%): Share of the market held by the product or company.
Share of Shelf (%): Percentage of shelf space occupied by the product.
Trial Rate (%): Percentage of consumers who tried the product.
Repeat Rate (%): Percentage of consumers who purchased the product again.
Sales Value (USD): Total sales in USD, with some values stored as strings or containing extreme outliers.
Time: The sales timeframe, containing inconsistent formats (e.g., "2021-08-01" vs. "August 2021").
Volume Sales: A supplementary column with mixed units and formats for volume sales (e.g., "70000 liters" vs. "70 kiloliters").

### Notes:
- There are some missing values in the dataset, which will be addressed during the analysis phase.
  
## Setup
To run this project:
```bash
pip install -r requirements.txt
jupyter notebook


