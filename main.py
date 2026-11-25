from product import (
    add_product,
    show_products,
    deleteProduct,
    filter_by_price
)

from database import load_products
from csvOperations import write_csv, show_csv_products


def main():
    while True:
        print("\n===== PRODUCT MANAGEMENT =====")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Delete Product")
        print("4. Filter By Price")
        print("5. Save Products To CSV")
        print("6. Show CSV Products")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            show_products()

        elif choice == "3":
            deleteProduct()

        elif choice == "4":
            filter_by_price()

        elif choice == "5":
            products = load_products()
            write_csv(products)
            print("CSV faylina yazildi.")

        elif choice == "6":
            show_csv_products()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__== "__main__":
    main()