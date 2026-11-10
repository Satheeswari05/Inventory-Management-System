
import pytest

from inventory.product import Product, Electronics, Grocery
from inventory.exceptions import InvalidProductError


def test_product_creation():
    product = Product("P101", "Book", 100, 5)

    assert product.product_id == "P101"
    assert product.name == "Book"
    assert product.price == 100
    assert product.quantity == 5


def test_product_value():
    product = Product("P101", "Book", 100, 5)

    assert product.calculate_value() == 500


def test_electronics_value():
    product = Electronics("E101", "Laptop", 50000, 2)

    assert product.calculate_value() == 118000


def test_grocery_value():
    product = Grocery("G101", "Rice", 60, 10)

    assert product.calculate_value() == 600


def test_update_quantity():
    product = Product("P101", "Book", 100, 5)

    product.update_quantity(10)

    assert product.quantity == 10


def test_negative_price():
    with pytest.raises(InvalidProductError):
        Product("P101", "Book", -100, 5)


def test_negative_quantity():
    with pytest.raises(InvalidProductError):
        Product("P101", "Book", 100, -5)


def test_invalid_quantity_update():
    product = Product("P101", "Book", 100, 5)

    with pytest.raises(InvalidProductError):
        product.update_quantity(-10)


def test_missing_product_details():
    with pytest.raises(InvalidProductError):
        Product("", "Book", 100, 5)
