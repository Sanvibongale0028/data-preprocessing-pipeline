# import sys

# from data_loader.load_dataset import load_dataset
# from dataset_identifier.detect_dataset_type import detect_dataset_type
# from cleaning.handle_missing import handle_missing_values
# from cleaning.remove_duplicates import remove_duplicates
# from transformation.encoding import encode_categorical
# from transformation.scaling import scale_features
# from transformation.normalization import normalize_features
# from feature_engineering.feature_extraction import extract_features


# def main(file_path):

#     print("Starting preprocessing pipeline")

#     # Load dataset
#     df = load_dataset(file_path)

#     # Detect dataset type
#     dataset_type = detect_dataset_type(df)
#     print(f"Dataset type detected: {dataset_type}")

#     # Cleaning
#     df = remove_duplicates(df)
#     df = handle_missing_values(df)

#     # Transformation
#     df = encode_categorical(df)
#     df = scale_features(df)
#     df = normalize_features(df)

#     # Feature Engineering
#     df = extract_features(df)

#     output_path = "processed_dataset.csv"
#     df.to_csv(output_path, index=False)

#     print("Preprocessing completed")
#     print(f"Processed dataset saved at {output_path}")


# if __name__ == "__main__":
#     file_path = sys.argv[1]
#     main(file_path)

import sys
import os

from data_loader.load_dataset import load_dataset
from dataset_identifier.detect_dataset_type import detect_dataset_type
from cleaning.handle_missing import handle_missing_values
from cleaning.remove_duplicates import remove_duplicates
from transformation.encoding import encode_categorical
from transformation.scaling import scale_features
from transformation.normalization import normalize_features
from feature_engineering.feature_extraction import extract_features


def main(file_path):

    print("Starting preprocessing pipeline")

    # Load dataset
    df = load_dataset(file_path)

    # Detect dataset type
    dataset_type = detect_dataset_type(df)
    print(f"Dataset type detected: {dataset_type}")

    # Cleaning
    df = remove_duplicates(df)
    df = handle_missing_values(df)

    # Transformation
    df = encode_categorical(df)
    df = scale_features(df)
    df = normalize_features(df)

    # Feature Engineering
    df = extract_features(df)

    # Create processed folder if it doesn't exist
    processed_dir = "backend/processed"
    os.makedirs(processed_dir, exist_ok=True)

    # Get original filename
    filename = os.path.basename(file_path)

    # Create processed filename
    output_path = os.path.join(processed_dir, f"processed_{filename}")

    # Save dataset
    df.to_csv(output_path, index=False)

    print("Preprocessing completed")
    print(f"Processed dataset saved at {output_path}")


if __name__ == "__main__":
    file_path = sys.argv[1]
    main(file_path)