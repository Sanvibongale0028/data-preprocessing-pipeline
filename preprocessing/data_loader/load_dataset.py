import pandas as pd
import os


def load_dataset(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)

    elif ext == ".xlsx":
        df = pd.read_excel(file_path)

    elif ext == ".json":
        df = pd.read_json(file_path)

    elif ext == ".parquet":
        df = pd.read_parquet(file_path)

    else:
        raise ValueError("Unsupported dataset format")

    print("Dataset loaded successfully")

    return df