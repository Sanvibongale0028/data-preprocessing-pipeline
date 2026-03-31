# from sklearn.preprocessing import StandardScaler
# import numpy as np

# def scale_features(df):
    
#     df = df.copy()
    
#     scaler = StandardScaler()
    
#     num_cols = df.select_dtypes(include=np.number).columns
    
#     # select only non-binary columns
#     scale_cols = [col for col in num_cols if df[col].nunique() > 2]
    
#     df[scale_cols] = scaler.fit_transform(df[scale_cols])
    
#     return df

from sklearn.preprocessing import StandardScaler
import numpy as np

def scale_features(df):
    
    df = df.copy()
    
    scaler = StandardScaler()
    
    num_cols = df.select_dtypes(include=np.number).columns
    
    # Select only continuous columns
    scale_cols = [
        col for col in num_cols
        if df[col].nunique() > 10   # skip binary + low-cardinality (month, weekday, etc.)
        and df[col].std() != 0      # skip constant columns
    ]
    
    df[scale_cols] = scaler.fit_transform(df[scale_cols])
    
    return df