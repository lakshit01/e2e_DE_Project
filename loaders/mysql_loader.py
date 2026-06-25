from sqlalchemy import create_engine, text

class MySQLLoader:

    def __init__(
        self,
        host="logistics-mysql.cju20w6u0l15.ap-south-1.rds.amazonaws.com",
        port=3306,
        database="logistics",
        username="admin",
        password="Admin-321"
    ):

        self.engine = create_engine(

            f"mysql+pymysql://"
            f"{username}:{password}"
            f"@{host}:{port}"
            f"/{database}"
        )

    def load(
        self,
        table_name,
        dataframe,
        mode="append"
    ):

        if mode == "replace":
            with self.engine.begin() as conn:
                conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
                conn.execute(text(f"DELETE FROM `{table_name}`"))
                conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))

            dataframe.to_sql(
                table_name,
                self.engine,
                if_exists="append",
                index=False
            )
        else:
            dataframe.to_sql(
                table_name,
                self.engine,
                if_exists=mode,
                index=False
            )

        print(
            f"{table_name} loaded"
        )