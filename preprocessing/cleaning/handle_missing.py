import pandas as pd


def handle_missing_values(df):

    for column in df.columns:

        if df[column].dtype == "object":
            df[column].fillna(df[column].mode()[0], inplace=True)

        else:
            df[column].fillna(df[column].mean(), inplace=True)

    print("Missing values handled")

    return df