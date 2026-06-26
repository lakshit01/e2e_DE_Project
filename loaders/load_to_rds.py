from loaders.db_connection import get_engine
from loaders.csv_loader import load_csv
from loaders.utils import get_csv_files
from loaders.logger import logger
import time

def main():

    start = time.time()

    logger.info("Starting ingestion")

    engine = get_engine()

    csv_files = get_csv_files()

    total_tables = 0
    total_rows = 0

    for csv_file in csv_files:

        rows = load_csv(engine, csv_file)

        total_tables += 1
        total_rows += rows

    end = time.time()

    logger.info("===================================")
    logger.info(f"Tables Loaded : {total_tables}")
    logger.info(f"Rows Loaded   : {total_rows}")
    logger.info(f"Execution     : {end-start:.2f} sec")
    logger.info("===================================")

if __name__ == "__main__":
    main()