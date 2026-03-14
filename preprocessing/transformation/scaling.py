from sklearn.preprocessing import StandardScaler
import pandas as pd


def scale_features(df):

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    scaler = StandardScaler()

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("Feature scaling applied")

    return df