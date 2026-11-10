
from inventory.product import Electronics, Grocery
from inventory.inventory import Inventory
from inventory.storage import Storage
from inventory.exceptions import InventoryError


def display_products(inventory):
    products = inventory.get_all_products()

    if not products:
        print("\nInventory is empty.")
        return

    print("\n========== PRODUCT LIST ==========")

    for product in products:
        print(f"""
ID       : {product.product_id}
Name     : {product.name}
Price    : ₹{product.price}
Quantity : {product.quantity}
Value    : ₹{product.calculate_value()}
-----------------------------------
""")


def main():
    inventory = Inventory()

    while True:
        print("""
========== INVENTORY MANAGEMENT ==========
1. Add Electronics
2. Add Grocery
3. View All Products
4. Search Product
5. Update Stock
6. Sell Product
7. Delete Product
8. Total Inventory Value
9. Save Inventory
10. Load Inventory
11. Exit
==========================================
""")

        choice = input("Enter your choice: ")

        try:
            if choice in ("1", "2"):
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))

                if choice == "1":
                    product = Electronics(
                        product_id, name, price, quantity
                    )
                else:
                    product = Grocery(
                        product_id, name, price, quantity
                    )

                inventory.add_product(product)
                print("Product added successfully!")

            elif choice == "3":
                display_products(inventory)

            elif choice == "4":
                name = input("Enter product name: ")
                results = inventory.search_product(name)

                for product in results:
                    print(product.get_details())

                if not results:
                    print("No matching products found.")

            elif choice == "5":
                product_id = input("Product ID: ")
                quantity = int(input("New quantity: "))

                inventory.update_stock(product_id, quantity)
                print("Stock updated successfully!")

            elif choice == "6":
                product_id = input("Product ID: ")
                quantity = int(input("Quantity to sell: "))

                inventory.sell_product(product_id, quantity)
                print("Sale completed successfully!")

            elif choice == "7":
                product_id = input("Product ID: ")
                inventory.remove_product(product_id)
                print("Product deleted successfully!")

            elif choice == "8":
                print(
                    "Total Inventory Value: ₹",
                    inventory.total_inventory_value()
                )

            elif choice == "9":
                format_choice = input(
                    "Save as JSON or CSV? "
                ).strip().lower()

                if format_choice == "json":
                    Storage.save_json(
                        inventory, "data/inventory.json"
                    )
                elif format_choice == "csv":
                    Storage.save_csv(
                        inventory, "data/inventory.csv"
                    )
                else:
                    print("Invalid format!")
                    continue

                print("Inventory saved successfully!")

            elif choice == "10":
                format_choice = input(
                    "Load from JSON or CSV? "
                ).strip().lower()

                if format_choice == "json":
                    loaded = Storage.load_json(
                        "data/inventory.json"
                    )
                elif format_choice == "csv":
                    loaded = Storage.load_csv(
                        "data/inventory.csv"
                    )
                else:
                    print("Invalid format!")
                    continue

                inventory = loaded
                print("Inventory loaded successfully!")

            elif choice == "11":
                print("Thank you for using Inventory Manager!")
                break

            else:
                print("Invalid choice. Try again.")

        except (InventoryError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
