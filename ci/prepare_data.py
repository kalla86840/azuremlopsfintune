import pandas as pd
import os

def prepare_data():
    input_path = os.path.join("..", "CSV fine tune file - medical speciality.csv")

    df = pd.read_csv(input_path)

    if "prompt" not in df.columns or "completion" not in df.columns:
        raise ValueError("CSV must contain 'prompt' and 'completion' columns.")

    df["prompt"] = df["prompt"].astype(str).str.strip() + " ->"
    df["completion"] = df["completion"].astype(str).str.strip() + " END"

    out_path = "prepared_data.jsonl"
    df.to_json(out_path, orient="records", lines=True)
    print(f"Prepared data written to {out_path}")

if __name__ == "__main__":
    prepare_data()
