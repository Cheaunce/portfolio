# Canadian Housing Affordability vs Safety Analysis

## Project Overview
This project examines urban rental housing in Canada (2020–2024) and compares it with public safety metrics. The goal is to provide context for anyone evaluating Canadian cities, considering not just rent but also relative safety.

By combining CMHC rental data with Crime Severity Index (CSI) statistics, I explore whether higher rents correlate with lower crime and identify trends across regions.

## Motivation
Housing affordability is important, but **cost alone doesn’t tell the full story**. Safety and quality of life are critical factors in housing decisions. This project aims to:

- Identify correlations between rental costs and crime rates across major Canadian cities.  
- Highlight regions where affordable rental housing coincides with higher or lower safety.  
- Provide insights for prospective renters, policymakers, or urban planners.

## Data Sources
- **CMHC Rental Market Survey (2020–2024)** – Provides average rents, vacancy rates, and other housing affordability statistics for Canadian cities.  
  [Access the data here](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables/rental-market/rental-market-report-data-tables)

- **Statistics Canada Crime Severity Index (2020–2024)** – Annual measures of crime severity by city for comparison of safety levels across regions.  
  [Access the data here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510002601)

## Expected Insights
Based on preliminary research, I anticipate:

- Smaller or more remote cities will generally have lower housing costs.  
- High-demand, low-crime cities will likely have the highest rental prices.  
- Cities with higher crime severity indexes may show slightly lower rents, suggesting a trade-off between affordability and safety.  
- Visualizations will help spot patterns, trends, and outliers in the housing market relative to safety.

## Project Structure
```
canadian_housing_project/
    data/       # Raw datasets (CMHC RMS, CSI)
    notebooks/  # Jupyter notebooks for cleaning, analysis, and visualization
    images/     # Charts and visualizations exported for README
    README.md   # Project description, methodology, and findings
```

## Methodology
1. **Data Collection**: Download CMHC RMS and StatsCan CSI datasets for 2020–2024.  
2. **Data Cleaning**: Standardize column names, handle missing values, and remove metadata rows.  
3. **Data Merging**: Combine datasets on region (CMA) and year.  
4. **Exploratory Data Analysis (EDA)**: Generate charts to examine rent trends and crime severity across cities.  
5. **Statistical Analysis**: Assess correlations between rental prices and crime severity.  
6. **Reporting**: Summarize findings in notebooks, including visualizations and key insights.

## Future Enhancements
- Build interactive dashboards using Plotly, Streamlit, or Looker Studio.  
- Add geospatial maps to visualize affordability and safety by city.  
- Incorporate additional quality-of-life datasets, such as income, employment, or education statistics.

## Visualizations
*Charts and figures generated from notebooks will be placed here (e.g., scatterplots, trends over years).*

## Findings
*Placeholder for key insights and observations derived from the analysis.*

## License
This project is for educational purposes and uses publicly available datasets from CMHC and Statistics Canada.
