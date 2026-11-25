import csv
import os

CSV_FILE = "products.csv"
FIELDS = ["id", "name", "category", "price"]


def read_csv():
    if not os.path.exists(CSV_FILE):
        write_csv([])
        return []

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = []

        for row in reader:
            try:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
            except (KeyError, ValueError):
                continue

        return products


def write_csv(products):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(products)


def show_csv_products():
    products = read_csv()

    if not products:
        print("CSV faylinda mehsul yoxdur.")
        return

    for product in products:
        print(product)