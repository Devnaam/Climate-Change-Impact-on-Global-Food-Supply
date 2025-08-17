# Climate Change Impact on Global Food Supply

Analyze how temperature, precipitation, and CO₂ relate to crop yields across countries and time.

## Structure
- `data/raw/`        → original datasets
- `data/processed/`  → cleaned/merged datasets
- `notebooks/`       → analysis notebooks
- `src/`             → reusable Python code
- `figures/`         → saved charts
- `dashboards/`      → optional app (Streamlit/Dash)
- `reports/`         → exports (PDF/HTML)

## Setup
1. Create venv: `python -m venv .venv` and activate it.
2. Install deps: `pip install -r requirements.txt`
3. Add datasets to `data/raw/`.



## 1. Project Overview

This project analyzes the relationship between climate variables (temperature and CO₂ emissions) and global crop production. Using three distinct datasets, we cleaned and integrated the data to build a predictive model, aiming to understand the potential impact of climate change on food supply.

## 2. Data Sources

The analysis utilized three datasets:
* **Crop Yield Data**: Contains crop production statistics for various states and crops in India.
* **Climate Data**: Provides average monthly temperature records for cities worldwide.
* **CO₂ Emissions Data**: Tracks the share of global CO₂ consumption-based emissions over time.

## 3. Data Cleaning and Integration

The initial datasets were at different temporal and geographical granularities. The following steps were taken to prepare the data for analysis:
* **Missing Values**: Rows with missing temperature data were dropped from the climate dataset.
* **Data Type Conversion**: The date column in the climate data was converted to a proper datetime format.
* **Data Aggregation**: All data was aggregated to a common, comparable level. Crop production and climate data were aggregated by **Year** and **Country**, while the CO₂ data was filtered to represent a global-level trend.
* **Merging**: The cleaned and aggregated dataframes were merged into a single, comprehensive dataset.

## 4. Exploratory Data Analysis (EDA)

Initial visualizations revealed key trends and challenges in the data.

### Global Temperature and CO₂ Trends
Plots showed a clear long-term **upward trend** in both global average temperature and CO₂ emissions. 

### Crop Production Trends
The crop production data, which was specific to India, showed significant **fluctuations** over the years, with periods of both increase and decrease in total production.

## 5. Modeling and Analysis

A **Linear Regression** model was built to predict crop production based on average temperature and global CO₂ emissions.

* **Features (X)**: `AverageTemperature` and `Global_CO2_Emissions`
* **Target (y)**: `Production`

### Model Performance
The model's performance was evaluated using standard metrics. The `Actual vs. Predicted` plot showed a reasonably good fit, suggesting the model captures some underlying patterns in the data. 

### Model Coefficients
The coefficients revealed a surprising and counterintuitive relationship:
* **Average Temperature:** $7.818 \times 10^8$
* **Global CO₂ Emissions:** $1.972 \times 10^{13}$

These coefficients indicate that for every unit increase in temperature and CO₂ emissions, the model predicts a massive increase in crop production.

## 6. Conclusion and Recommendations

The results of this analysis highlight a critical point in data science: **a model's output is only as good as its input**. The highly positive coefficients for both temperature and CO₂ emissions are scientifically implausible and suggest a fundamental issue with the data, specifically the CO₂ emissions data which may be on an incompatible scale.

### Limitations:
* The model assumes a simple linear relationship, which is likely not the case in reality.
* The CO₂ emissions data may not accurately represent the scale of global emissions.
* The analysis only considers two variables, while a complete picture would require factors like precipitation, land use, and technology.

### Future Work:
* **Data Sourcing**: Find a more robust and standard dataset for global CO₂ emissions (e.g., in gigatons).
* **Advanced Modeling**: Explore non-linear models such as **Random Forest Regressor** or **Gradient Boosting** to capture more complex relationships.
* **Feature Engineering**: Integrate additional climate variables like precipitation and humidity to build a more comprehensive model.