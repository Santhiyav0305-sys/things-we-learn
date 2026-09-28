from pathlib import Path
import pandas as pd

def load_csv(path):
    return pd.read_csv(Path(path))

def basic_report(df):
    return {
        "shape": df.shape,
        "missing_values": df.isna().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "numeric_summary": df.describe(numeric_only=True),
    }
