# Traffic Accident Data Analysis & Prediction

Analysis of traffic accident causes, severity, timing, and weather conditions — with a machine learning model to predict accident severity.

## Project Overview

This project explores patterns in traffic accident data across time, location, weather, and road conditions, then builds a classification model to predict accident severity level.

## Dataset

| Source | Description |
|--------|-------------|
| [US Accidents Dataset (Kaggle)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents) | 2.8M accident records across 49 US states |
| [NHTSA Crash Data](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) | Fatality Analysis Reporting System (FARS) |
| [NOAA Climate Data](https://www.ncdc.noaa.gov/cdo-web/) | Historical weather for accident location correlation |

> **Note:** Raw data files are not committed to this repo. Download sources above and place in `data/raw/`.

## Project Structure

```
traffic-accident-prediction/
├── data/
│   ├── raw/              # Source data (gitignored)
│   └── processed/        # Cleaned, feature-engineered data
├── notebooks/
│   ├── 01_eda.ipynb          # Exploratory data analysis
│   ├── 02_features.ipynb     # Feature engineering & preprocessing
│   ├── 03_modelling.ipynb    # Model training & evaluation
│   └── 04_insights.ipynb     # Final insights & visualizations
├── src/
│   ├── preprocessing.py      # Data cleaning utilities
│   ├── features.py           # Feature engineering helpers
│   └── evaluation.py         # Classification metrics
├── reports/
│   └── final_report.pdf
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/yourusername/traffic-accident-prediction.git
cd traffic-accident-prediction
pip install -r requirements.txt
jupyter notebook notebooks/01_eda.ipynb
```

## Phases

| Phase | Focus | Milestone |
|-------|-------|-----------|
| 1 | Data collection & EDA | Clean dataset + severity distribution analysis |
| 2 | Feature engineering | Modelling-ready feature matrix |
| 3 | Modelling & evaluation | Best classifier selected, metrics documented |
| 4 | Insights & presentation | Final report + accident pattern visualizations |

## Results

_To be updated after modelling is complete._

## Tech Stack

Python · pandas · scikit-learn · XGBoost · matplotlib · seaborn · folium · Jupyter

## Author

Your Name — [GitHub](https://github.com/yourusername)
