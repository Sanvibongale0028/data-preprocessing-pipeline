def detect_dataset_type(df):

    if df is None:
        return "unknown"

    if df.shape[1] > 0:
        return "structured_tabular"

    return "unknown"