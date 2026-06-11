import pandas as pd


def add_time_features(df: pd.DataFrame, datetime_col: str) -> pd.DataFrame:
    """Extract time-based features from a datetime column."""
    dt = df[datetime_col]
    df["hour"] = dt.dt.hour
    df["day_of_week"] = dt.dt.dayofweek
    df["month"] = dt.dt.month
    df["is_weekend"] = (dt.dt.dayofweek >= 5).astype(int)
    df["is_rush_hour"] = (
        dt.dt.hour.isin(range(7, 10)) | dt.dt.hour.isin(range(16, 19))
    ).astype(int)
    df["is_night"] = (
        (dt.dt.hour >= 21) | (dt.dt.hour < 6)
    ).astype(int)
    return df


def add_road_features(df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder: encode road type, speed limit, junction flags."""
    # Add your road feature logic here
    return df


def encode_categoricals(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """One-hot encode categorical columns."""
    return pd.get_dummies(df, columns=cols, drop_first=True)
