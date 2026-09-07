# Canadian Housing Affordability vs Safety Analysis

## Project Overview
This project looks at **urban housing costs in Canada (2020–2024)** and compares them with **public safety metrics**. The goal is to provide context for anyone evaluating housing markets in major Canadian cities, considering not just rent but also the relative safety of each location.

By combining rental data with crime statistics, I can explore whether higher rents correlate with lower crime and identify trends across regions.

## Motivation
Housing affordability is obviously important, but **cost alone doesn’t tell the full story**. Many people care about **safety and quality of life** when choosing where to live. This project aims to:

- Identify correlations between rental costs and safety in Canadian cities.  
- Highlight regions where affordable housing aligns with higher or lower crime rates.  
- Provide insights that might help prospective renters, policymakers, or urban planners make informed decisions.

## Data Sources

- **CMHC Rental Market Survey (2020–2024)** – Provides average rents, vacancy rates, and other housing affordability statistics for Canadian cities.  
  [Access the data here](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables/rental-market/rental-market-report-data-tables)

- **Statistics Canada Crime Severity Index (2020–2024)** – Annual measures of crime severity by city for comparison of safety levels across regions.  
  [Access the data here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510002601)

## Expected Insights
Based on preliminary research, I anticipate that:

- **Smaller or more remote cities** will generally have lower housing costs.  
- **High-demand, low-crime cities** will likely have the highest rental prices.  
- Cities with **higher crime severity indexes** may show slightly lower rents, suggesting a trade-off between affordability and safety.  
- Visualizations will help spot patterns, trends, and outliers in the housing market relative to safety.

## Project Structure

```
canadian_housing_project/
    data/
        raw/        # Original CMHC and StatsCan downloads
        processed/  # Cleaned datasets used for analysis
    notebooks/
        01_clean_cmhc.ipynb
        02_clean_csi.ipynb
        03_merge_and_eda.ipynb
    images/         # Exported charts and visualizations
    README.md       # Project description, methodology, and findings
```

## Methodology

1. **Data Collection**: Download CMHC RMS and StatsCan CSI datasets for 2020–2024.  
2. **Data Cleaning**: Standardize column names, handle missing values, and ensure consistency.  
3. **Data Merging**: Combine datasets on region (CMA) and year.  
4. **Exploratory Data Analysis (EDA)**: Generate charts to examine rent trends and crime severity across cities.  
5. **Statistical Analysis**: Assess correlations between rental prices and crime severity.  
6. **Reporting**: Summarize findings in notebooks, including visualizations and key insights.

## Future Enhancements

- Add geospatial maps to visualize affordability and safety by city.  
- Incorporate additional statistics, such as tourism, education, employment, income, and food security
- Extending the analysis across a larger timeline

## Visualizations
*Charts and figures generated from notebooks will be placed here (e.g., scatterplots, trends over years).*

## Findings
*My findings using the current dataset are inconclusive at this time. There is some significant positive correlation (> 0.8) in 7 centres, but the remaining 10 show weaker or negative correlations. With such a small dataset (5 years as data points for 17 centres) and so few factors, rent and crime, there aren't other available statistics to consider at this time.

Other things to consider would be the impact of tourism, education, employment, income, and food security on rent and crime. Extending the analysis across a larger span of years would help as well, although data availability will likely be the limitation.*

## License
This project is for educational purposes and uses publicly available datasets from CMHC and Statistics Canada.
