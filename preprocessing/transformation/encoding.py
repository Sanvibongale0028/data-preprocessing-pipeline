# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# def encode_categorical(df):

#     df = df.copy()
#     n_rows = len(df)

#     # Identify categorical columns
#     cat_cols = df.select_dtypes(include=['object','category']).columns.tolist()

#     for col in cat_cols:

#         unique_vals = df[col].nunique()
#         unique_ratio = unique_vals / n_rows

#         # --------------------------------
#         # 1️⃣ Detect ID-like columns
#         # --------------------------------
#         if unique_ratio > 0.95:
#             df = df.drop(columns=[col])
#             continue

#         # --------------------------------
#         # 2️⃣ Low cardinality → One-hot
#         # --------------------------------
#         if unique_vals <= 15:
#             dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
#             df = pd.concat([df, dummies], axis=1)
#             df = df.drop(columns=[col])

#         # --------------------------------
#         # 3️⃣ Medium cardinality → Label encoding
#         # --------------------------------
#         elif unique_vals <= 100:
#             le = LabelEncoder()
#             df[col] = le.fit_transform(df[col])

#         # --------------------------------
#         # 4️⃣ High cardinality → Frequency encoding
#         # --------------------------------
#         else:
#             freq_map = df[col].value_counts(normalize=True)
#             df[col] = df[col].map(freq_map)

#     return df

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_categorical(df):

    df = df.copy()
    n_rows = len(df)

    # --------------------------------
    # Detect categorical columns only
    # (exclude datetime columns)
    # --------------------------------
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    for col in cat_cols:

        # Try converting to datetime first
        # If conversion succeeds → skip encoding
        try:
            temp = pd.to_datetime(df[col])
            if not temp.isna().all():
                continue
        except:
            pass

        unique_vals = df[col].nunique()
        unique_ratio = unique_vals / n_rows

        # --------------------------------
        # 1️⃣ Detect ID-like columns
        # --------------------------------
        if unique_ratio > 0.95:
            df = df.drop(columns=[col])
            continue

        # --------------------------------
        # 2️⃣ Low cardinality → One-hot
        # --------------------------------
        if unique_vals <= 15:
            dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
            df = pd.concat([df, dummies], axis=1)
            df = df.drop(columns=[col])

        # --------------------------------
        # 3️⃣ Medium cardinality → Label encoding
        # --------------------------------
        elif unique_vals <= 100:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

        # --------------------------------
        # 4️⃣ High cardinality → Frequency encoding
        # --------------------------------
        else:
            freq_map = df[col].value_counts(normalize=True)
            df[col] = df[col].map(freq_map)

    return df