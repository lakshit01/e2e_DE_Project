import os
import pandas as pd

from sqlalchemy import create_engine


# ====================================================
# CONFIGURATION
# ====================================================

RDS_HOST = "logistics-mysql.cju20w6u0l15.ap-south-1.rds.amazonaws.com"

RDS_PORT = 3306

DATABASE = "logistics"

USERNAME = "admin"

PASSWORD = "Admin-321"


# ====================================================
# CREATE CONNECTION
# ====================================================

connection_string = (
    f"mysql+pymysql://"
    f"{USERNAME}:{PASSWORD}"
    f"@{RDS_HOST}:{RDS_PORT}/{DATABASE}"
)

engine = create_engine(
    connection_string
)

print("Connected to RDS")


# ====================================================
# FILE → TABLE MAPPING
# ====================================================

TABLE_MAPPING = {

    "customers.csv": "customers",

    "drivers.csv": "drivers",

    "vehicles.csv": "vehicles",

    "warehouses.csv": "warehouses",

    "routes.csv": "routes",

    "shipments.csv": "shipments"

}


# ====================================================
# LOAD FILES
# ====================================================

for file_name, table_name in TABLE_MAPPING.items():

    file_path = os.path.join(
        "outputs",
        file_name
    )

    print(
        f"\nLoading {file_name} "
        f"→ {table_name}"
    )

    df = pd.read_csv(file_path)

    print(
        f"Records Found: {len(df)}"
    )

    df.to_sql(

        name=table_name,

        con=engine,

        if_exists="append",

        index=False,

        chunksize=1000,

        method="multi"

    )

    print(
        f"Loaded {len(df)} records "
        f"into {table_name}"
    )

print(
    "\nAll Files Loaded Successfully"
)