
import json
import csv
from pathlib import Path

from inventory.product import Product, Electronics, Grocery
from inventory.inventory import Inventory
from inventory.exceptions import InventoryError


class Storage:

    @staticmethod
    def _product_to_dict(product):
        if isinstance(product, Electronics):
            product_type = "Electronics"
        elif isinstance(product, Grocery):
            product_type = "Grocery"
        else:
            product_type = "Product"

        return {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "product_type": product_type
        }

    @staticmethod
    def _dict_to_product(data):
        try:
            product_type = data.get("product_type", "Product")

            classes = {
                "Product": Product,
                "Electronics": Electronics,
                "Grocery": Grocery
            }

            if product_type not in classes:
                raise InventoryError("Unknown product type.")

            return classes[product_type](
                data["product_id"],
                data["name"],
                float(data["price"]),
                int(data["quantity"])
            )

        except (KeyError, TypeError, ValueError) as error:
            raise InventoryError(
                "Invalid product data."
            ) from error

    # SAVE JSON
    @staticmethod
    def save_json(inventory, filename):
        path = Path(filename)

        path.parent.mkdir(parents=True, exist_ok=True)

        data = [
            Storage._product_to_dict(product)
            for product in inventory.get_all_products()
        ]

        try:
            with path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            raise InventoryError(
                "Unable to save JSON file."
            ) from error

    # LOAD JSON
    @staticmethod
    def load_json(filename):
        path = Path(filename)

        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise InventoryError(
                    "JSON data must contain a list."
                )

            inventory = Inventory()

            for item in data:
                if not isinstance(item, dict):
                    raise InventoryError("Invalid product record.")

                product = Storage._dict_to_product(item)
                inventory.add_product(product)

            return inventory

        except (OSError, json.JSONDecodeError) as error:
            raise InventoryError(
                "Unable to load JSON file."
            ) from error

    # SAVE CSV
    @staticmethod
    def save_csv(inventory, filename):
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        fields = [
            "product_id", "name", "price",
            "quantity", "product_type"
        ]

        try:
            with path.open(
                "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file, fieldnames=fields
                )

                writer.writeheader()

                for product in inventory.get_all_products():
                    writer.writerow(
                        Storage._product_to_dict(product)
                    )

        except OSError as error:
            raise InventoryError(
                "Unable to save CSV file."
            ) from error

    # LOAD CSV
    @staticmethod
    def load_csv(filename):
        path = Path(filename)

        try:
            with path.open(
                "r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.DictReader(file)

                required = {
                    "product_id", "name", "price",
                    "quantity", "product_type"
                }

                if not required.issubset(
                    set(reader.fieldnames or [])
                ):
                    raise InventoryError(
                        "CSV file has missing columns."
                    )

                inventory = Inventory()

                for row in reader:
                    product = Storage._dict_to_product(row)
                    inventory.add_product(product)

                return inventory

        except (OSError, csv.Error) as error:
            raise InventoryError(
                "Unable to load CSV file."
            ) from error
