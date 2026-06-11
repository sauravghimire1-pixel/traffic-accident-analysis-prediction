import pandas as pd
import numpy as np


def drop_duplicates_and_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop duplicate rows and columns with more than `threshold` missing values."""
    df = df.drop_duplicates()
    null_frac = df.isnull().mean()
    df = df.loc[:, null_frac < threshold]
    return df


def fill_missing(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """Fill missing numeric values using mean or median."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mean())
    return df


def parse_datetime(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Parse a datetime column."""
    df[col] = pd.to_datetime(df[col])
    return df


def encode_weather(df: pd.DataFrame, weather_col: str) -> pd.DataFrame:
    """Simplify weather descriptions into broad categories."""
    mapping = {
        "clear": "clear", "sunny": "clear", "fair": "clear",
        "rain": "rain", "drizzle": "rain", "shower": "rain",
        "snow": "snow", "sleet": "snow", "ice": "snow",
        "fog": "fog", "mist": "fog", "haze": "fog",
        "cloud": "cloudy", "overcast": "cloudy",
    }
    def categorize(w):
        if pd.isna(w):
            return "unknown"
        w = w.lower()
        for key, val in mapping.items():
            if key in w:
                return val
        return "other"
    df[weather_col] = df[weather_col].apply(categorize)
    return df
