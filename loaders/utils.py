from pathlib import Path

DATA_FOLDER = Path("outputs")

def get_csv_files():

    return sorted(DATA_FOLDER.glob("*.csv"))