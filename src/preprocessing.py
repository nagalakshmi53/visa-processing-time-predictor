import pandas as pd
import os

def load_and_preprocess(input_path, output_path):
    df = pd.read_csv(input_path)

    df["application_date"] = pd.to_datetime(df["application_date"])
    df["decision_date"] = pd.to_datetime(df["decision_date"])

    df["processing_days"] = (df["decision_date"] - df["application_date"]).dt.days

    df = df.dropna()

    df.to_csv(output_path, index=False)
    print("Preprocessing completed. Cleaned file saved at:", output_path)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, "data", "visa_data.csv")
    output_file = os.path.join(base_dir, "data", "visa_data_cleaned.csv")

    load_and_preprocess(input_file, output_file)
