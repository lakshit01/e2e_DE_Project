import pandas as pd
from loaders.logger import logger

CHUNK_SIZE = 1000

def load_csv(engine, csv_file):

    table_name = csv_file.stem

    logger.info(f"Loading {table_name}")

    total_rows = 0

    for chunk in pd.read_csv(csv_file, chunksize=CHUNK_SIZE):

        chunk.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

        total_rows += len(chunk)

    logger.info(f"{table_name}: {total_rows} rows loaded")

    return total_rows