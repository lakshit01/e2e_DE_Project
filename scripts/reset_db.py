from sqlalchemy import create_engine, text

def main(
    host: str = "localhost",
    port: int = 3306,
    database: str = "logistics",
    username: str = "root",
    password: str = "root",
):

    # Connect to server without selecting a database
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/"
    )

    with engine.begin() as conn:
        conn.execute(text(f"DROP DATABASE IF EXISTS `{database}`"))
        conn.execute(text(f"CREATE DATABASE `{database}`"))

    print(f"Database '{database}' dropped and recreated")


if __name__ == "__main__":
    main()
