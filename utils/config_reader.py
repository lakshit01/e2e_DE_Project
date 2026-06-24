import yaml
from pathlib import Path

def load_config(env: str = "dev") -> dict:

    config_file = Path(
        f"config/{env}.yaml"
    )

    if not config_file.exists():
        raise FileNotFoundError(
            f"{config_file} not found"
        )

    with open(config_file, "r") as file:
        return yaml.safe_load(file)