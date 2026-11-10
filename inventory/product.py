
from inventory.exceptions import InvalidProductError


class Product:
    def __init__(self, product_id, name, price, quantity):
        if not product_id or not name:
            raise InvalidProductError("Product ID and name are required.")

        if price < 0 or quantity < 0:
            raise InvalidProductError(
                "Price and quantity cannot be negative."
            )

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # Encapsulation using properties
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def update_quantity(self, quantity):
        if quantity < 0:
            raise InvalidProductError("Quantity cannot be negative.")
        self.__quantity = quantity

    def calculate_value(self):
        return self.__price * self.__quantity

    def get_details(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "quantity": self.__quantity,
            "total_value": self.calculate_value()
        }


class Electronics(Product):
    def calculate_value(self):
        return super().calculate_value() * 1.18


class Grocery(Product):
    def calculate_value(self):
        return super().calculate_value()
