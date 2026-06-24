from pathlib import Path

class Exporter:

    @staticmethod
    def export_csv(df, path):

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(
            path,
            index=False
        )

    @staticmethod
    def export_json(df, path):

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_json(
            path,
            orient="records",
            indent=4
        )