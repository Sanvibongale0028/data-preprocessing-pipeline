import pandas as pd


def encode_categorical(df):

    categorical_cols = df.select_dtypes(include=["object"]).columns

    df = pd.get_dummies(df, columns=categorical_cols)

    print("Categorical encoding completed")

    return df