from database import load_products, save_products


def add_product():
    products = load_products()

    name = input("Mehsulun adi: ").strip()
    category = input("Kateqoriya: ").strip()

    try:
        price = float(input("Qiymet: "))
        if price < 0:
            print("Qiymet menfi ola bilmez.")
            return
    except ValueError:
        print("Qiymeti reqemle daxil edin.")
        return

    newid = max(
        (product.get("id", 0) for product in products),
        default=0
    ) + 1

    product = {
        "id": newid,
        "name": name,
        "category": category,
        "price": price
    }

    products.append(product)
    save_products(products)

    print("Mehsul elave edildi.")


def show_products():
    products = load_products()

    if not products:
        print("Mehsul yoxdur.")
        return

    for product in products:
        print(product)


def deleteProduct():
    products = load_products()

    try:
        product_id = int(input("Silinecek ID: "))
    except ValueError:
        print("ID tam reqem olmalidir.")
        return

    updated_products = [
        product for product in products
        if product.get("id") != product_id
    ]

    if len(updated_products) == len(products):
        print("Mehsul tapilmadi.")
        return

    save_products(updated_products)
    print("Mehsul silindi.")


def filter_by_price():
    products = load_products()

    try:
        max_price = float(input("Maksimum qiymet: "))
    except ValueError:
        print("Yanlis qiymet.")
        return

    filtered = [
        product for product in products
        if product["price"] <= max_price
    ]

    for product in filtered:
        print(product)