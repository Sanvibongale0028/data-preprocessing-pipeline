import pandas as pd


def extract_features(df):

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    df["row_sum"] = df[numeric_cols].sum(axis=1)
    df["row_mean"] = df[numeric_cols].mean(axis=1)

    print("Basic feature extraction completed")

    return df