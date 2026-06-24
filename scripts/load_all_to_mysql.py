import pandas as pd

# Ensure project root is on sys.path when running this script directly
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from loaders.mysql_loader import MySQLLoader

loader = MySQLLoader()

files = {

    "customers":
        "outputs/customers.csv",

    "drivers":
        "outputs/drivers.csv",

    "vehicles":
        "outputs/vehicles.csv",

    "warehouses":
        "outputs/warehouses.csv",

    "shipments":
        "outputs/shipments.csv"

}

for table,file_path in files.items():

    df = pd.read_csv(
        file_path
    )

    # Use 'replace' to overwrite existing table data and avoid duplicate primary key errors
    loader.load(
        table,
        df,
        mode="replace"
    )