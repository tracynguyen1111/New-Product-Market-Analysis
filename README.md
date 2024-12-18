# New Beverage Product Analysis

## Overview
This project analyzes consumer preferences and market trends for launching a new beverage product. 

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

## Setup
To run this project:
```bash
pip install -r requirements.txt
jupyter notebook

## Dataset

The raw dataset is located in the `data/` folder as `raw_data.csv`.  
It contains 1,000 rows and 11 columns with the following features:

- **Region**: Geographic location (e.g., North, South).  
- **Channel**: Sales channels like General Trade or Modern Trade.  
- **Product Category**: Beverage category (Water, Tea, etc.).  
- **Product Name**: Specific product names.  
- **PC (Product Cases)**: Number of product cases sold.  
- **Units per Case**: Units per product case.  
- **Product Volume (L)**: Volume per product.  
- **Sales Value (VND)**: Total sales in VND.  
- **Time Period**: Sales timeframe.  
- **UC (Unit Cases)**: Calculated unit cases.  
- **Price per UC (VND)**: Price per unit case.  

### Notes:
- There are some missing values in the dataset, which will be addressed during the analysis phase.  
- This dataset serves as the starting point for cleaning, exploration, and analysis.
