
from inventory.exceptions import (
    ProductNotFoundError,
    DuplicateProductError,
    InsufficientStockError
)


class Inventory:
    def __init__(self):
        self.__products = {}

    # CREATE
    def add_product(self, product):
        product_id = product.product_id

        if product_id in self.__products:
            raise DuplicateProductError(
                f"Product {product_id} already exists."
            )

        self.__products[product_id] = product

    # READ
    def get_product(self, product_id):
        if product_id not in self.__products:
            raise ProductNotFoundError(
                f"Product {product_id} not found."
            )

        return self.__products[product_id]

    def get_all_products(self):
        return list(self.__products.values())

    # UPDATE
    def update_stock(self, product_id, quantity):
        product = self.get_product(product_id)
        product.update_quantity(quantity)

    # DELETE
    def remove_product(self, product_id):
        if product_id not in self.__products:
            raise ProductNotFoundError(
                f"Product {product_id} not found."
            )

        del self.__products[product_id]

    # SEARCH
    def search_product(self, name):
        return [
            product for product in self.__products.values()
            if name.lower() in product.name.lower()
        ]

    # STOCK MANAGEMENT
    def sell_product(self, product_id, quantity):
        product = self.get_product(product_id)

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if quantity > product.quantity:
            raise InsufficientStockError(
                "Not enough stock available."
            )

        product.update_quantity(product.quantity - quantity)

    def total_inventory_value(self):
        return sum(
            product.calculate_value()
            for product in self.__products.values()
        )
