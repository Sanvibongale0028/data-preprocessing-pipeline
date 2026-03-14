from sklearn.preprocessing import MinMaxScaler


def normalize_features(df):

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    scaler = MinMaxScaler()

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("Normalization applied")

    return df