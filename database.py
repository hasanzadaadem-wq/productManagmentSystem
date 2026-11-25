import json
import os

JSON_FILE = "products.json"


def load_products():
    if not os.path.exists(JSON_FILE):
        save_products([])
        return []

    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            products = json.load(file)
            return products if isinstance(products, list) else []
    except (json.JSONDecodeError, OSError):
        print("JSON faylini oxumaq mumkun olmadi.")
        return []


def save_products(products):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)