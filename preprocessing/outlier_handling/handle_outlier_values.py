# import pandas as pd
# import numpy as np

# def handle_outliers(df):
#     df = df.copy()

#     num_cols = df.select_dtypes(include=np.number).columns

#     for col in num_cols:

#         # Skip binary columns
#         if df[col].nunique() <= 2:
#             continue

#         # Skip if column has no variance
#         if df[col].std() == 0:
#             continue

#         skewness = df[col].skew()

#         # -------------------------------
#         # 1️⃣ Normal distribution → IQR
#         # -------------------------------
#         if abs(skewness) < 0.5:
#             Q1 = df[col].quantile(0.25)
#             Q3 = df[col].quantile(0.75)
#             IQR = Q3 - Q1

#             lower = Q1 - 1.5 * IQR
#             upper = Q3 + 1.5 * IQR

#             df[col] = df[col].clip(lower, upper)

#         # -------------------------------
#         # 2️⃣ Moderate skew → Capping
#         # -------------------------------
#         elif abs(skewness) <= 1.5:
#             lower = df[col].quantile(0.01)
#             upper = df[col].quantile(0.99)

#             df[col] = df[col].clip(lower, upper)

#         # -------------------------------
#         # 3️⃣ High skew → Log transform
#         # -------------------------------
#         else:
#             # Apply only if all values > 0
#             if (df[col] > 0).all():
#                 df[col] = np.log1p(df[col])  # safer than log(x)
#             else:
#                 # fallback → capping
#                 lower = df[col].quantile(0.01)
#                 upper = df[col].quantile(0.99)
#                 df[col] = df[col].clip(lower, upper)

#     return df

import pandas as pd
import numpy as np

def handle_outliers(df):
    df = df.copy()

    num_cols = df.select_dtypes(include=np.number).columns

    for col in num_cols:

        # Skip binary columns
        if df[col].nunique() <= 2:
            continue

        # Skip low-cardinality columns (month, weekday, etc.)
        if df[col].nunique() <= 10:
            continue

        # Skip if column has no variance
        if df[col].std() == 0:
            continue

        skewness = df[col].skew()

        # -------------------------------
        # 1️⃣ Normal distribution → IQR
        # -------------------------------
        if abs(skewness) < 0.5:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            df[col] = df[col].clip(lower, upper)

        # -------------------------------
        # 2️⃣ Moderate skew → Capping
        # -------------------------------
        elif abs(skewness) <= 1.5:
            lower = df[col].quantile(0.01)
            upper = df[col].quantile(0.99)

            df[col] = df[col].clip(lower, upper)

        # -------------------------------
        # 3️⃣ High skew → Log transform
        # -------------------------------
        else:
            if (df[col] > 0).all():
                df[col] = np.log1p(df[col])
            else:
                lower = df[col].quantile(0.01)
                upper = df[col].quantile(0.99)
                df[col] = df[col].clip(lower, upper)

    return df