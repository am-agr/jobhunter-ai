import json
from pathlib import Path

CONFIG_DIR = Path("config")


def load_json(filename):
    file_path = CONFIG_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_configs():
    return {
        "companies": load_json("companies.json"),
        "keywords": load_json("keywords.json"),
        "settings": load_json("settings.json")
    }