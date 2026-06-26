from sqlalchemy import create_engine
from config.config import (
    RDS_HOST,
    RDS_PORT,
    RDS_DATABASE,
    RDS_USERNAME,
    RDS_PASSWORD,
)

def get_engine():

    connection_string = (
        f"mysql+pymysql://"
        f"{RDS_USERNAME}:{RDS_PASSWORD}"
        f"@{RDS_HOST}:{RDS_PORT}/{RDS_DATABASE}"
    )

    engine = create_engine(
        connection_string,
        pool_pre_ping=True,
        pool_recycle=3600
    )

    return engine