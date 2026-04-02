# import pandas as pd

# def handle_datetime(df):

#     df = df.copy()

#     # detect datetime columns
#     datetime_cols = df.select_dtypes(include=['datetime64[ns]', 'datetime64']).columns.tolist()

#     # also detect object columns that might contain dates
#     object_cols = df.select_dtypes(include=['object']).columns

#     for col in object_cols:
#         try:
#             df[col] = pd.to_datetime(df[col])
#             datetime_cols.append(col)
#         except:
#             pass

#     datetime_cols = list(set(datetime_cols))

#     for col in datetime_cols:

#         df[col] = pd.to_datetime(df[col])

#         # extract features
#         df[col + "_year"] = df[col].dt.year
#         df[col + "_month"] = df[col].dt.month
#         df[col + "_day"] = df[col].dt.day
#         df[col + "_dayofweek"] = df[col].dt.dayofweek
#         df[col + "_weekofyear"] = df[col].dt.isocalendar().week.astype(int)
#         df[col + "_is_weekend"] = (df[col].dt.dayofweek >= 5).astype(int)

#         # drop original column
#         df = df.drop(columns=[col])

#     return df