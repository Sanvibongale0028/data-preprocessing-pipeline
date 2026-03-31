# import pandas as pd
# import numpy as np
# from sklearn.impute import KNNImputer

# def handle_missing_values(df):

#     df = df.copy()

#     # Separate column types
#     num_cols = df.select_dtypes(include=np.number).columns.tolist()
#     cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()

#     # Calculate missing percentage
#     missing_percent = df.isnull().mean()

#     # -------------------------------
#     # 1️⃣ Drop columns with >50% missing
#     # -------------------------------
#     drop_cols = missing_percent[missing_percent > 0.5].index.tolist()
#     df = df.drop(columns=drop_cols)

#     # Update column lists
#     num_cols = df.select_dtypes(include=np.number).columns.tolist()
#     cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()

#     # -------------------------------
#     # 2️⃣ Add missing indicator columns
#     # -------------------------------
#     for col in df.columns:
#         if df[col].isnull().sum() > 0:
#             df[col + "_is_missing"] = df[col].isnull().astype(int)

#     # -------------------------------
#     # 3️⃣ Handle <5% missing values
#     # -------------------------------
#     low_missing = missing_percent[(missing_percent > 0) & (missing_percent < 0.05)].index

#     for col in low_missing:
#         if col in num_cols:
#             df[col] = df[col].fillna(df[col].median())
#         elif col in cat_cols:
#             df[col] = df[col].fillna(df[col].mode()[0])

#     # -------------------------------
#     # 4️⃣ Handle 5–50% missing values
#     # -------------------------------
#     mid_missing = missing_percent[(missing_percent >= 0.05) & (missing_percent <= 0.5)].index

#     num_mid = [col for col in mid_missing if col in num_cols]
#     cat_mid = [col for col in mid_missing if col in cat_cols]

#     # Numerical → KNN Imputer
#     if len(num_mid) > 0:
#         knn = KNNImputer(n_neighbors=5)
#         df[num_mid] = knn.fit_transform(df[num_mid])

#     # Categorical → Unknown
#     for col in cat_mid:
#         df[col] = df[col].fillna("Unknown")

#     return df

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

def handle_missing_values(df):

    df = df.copy()

    # --------------------------------
    # 0️⃣ Convert numeric-like object columns to numeric safely
    # --------------------------------
    for col in df.select_dtypes(include=['object']).columns:
        converted = pd.to_numeric(df[col], errors='coerce')

        # Only convert if majority values are numeric
        if converted.notna().sum() > df[col].notna().sum() * 0.5:
            df[col] = converted

    # --------------------------------
    # 1️⃣ Calculate missing percentage
    # --------------------------------
    missing_percent = df.isnull().mean()

    # --------------------------------
    # 2️⃣ Drop columns with >50% missing
    # --------------------------------
    drop_cols = missing_percent[missing_percent > 0.5].index.tolist()
    df = df.drop(columns=drop_cols)

    # Recalculate column types
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()

    # Recalculate missing %
    missing_percent = df.isnull().mean()

    # --------------------------------
    # 3️⃣ Add missing indicator columns
    # --------------------------------
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            df[col + "_is_missing"] = df[col].isnull().astype(int)

    # --------------------------------
    # 4️⃣ Handle <5% missing values
    # --------------------------------
    low_missing = missing_percent[
        (missing_percent > 0) & (missing_percent < 0.05)
    ].index.tolist()

    for col in low_missing:

        if col in num_cols:
            df[col] = df[col].fillna(df[col].median())

        elif col in cat_cols:
            mode_val = df[col].mode()
            if not mode_val.empty:
                df[col] = df[col].fillna(mode_val[0])
            else:
                df[col] = df[col].fillna("Unknown")

    # --------------------------------
    # 5️⃣ Handle 5–50% missing values
    # --------------------------------
    mid_missing = missing_percent[
        (missing_percent >= 0.05) & (missing_percent <= 0.5)
    ].index.tolist()

    num_mid = [col for col in mid_missing if col in num_cols]
    cat_mid = [col for col in mid_missing if col in cat_cols]

    # Numerical → KNN Imputation
    if num_mid:
        knn = KNNImputer(n_neighbors=5)
        df[num_mid] = knn.fit_transform(df[num_mid])

    # Categorical → fill with "Unknown"
    for col in cat_mid:
        df[col] = df[col].fillna("Unknown")

    return df