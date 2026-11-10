
import pytest

from inventory.product import Electronics, Grocery
from inventory.inventory import Inventory
from inventory.exceptions import (
    ProductNotFoundError,
    DuplicateProductError,
    InsufficientStockError
)


@pytest.fixture
def inventory():
    inv = Inventory()
    inv.add_product(Electronics("E101", "Laptop", 50000, 5))
    inv.add_product(Grocery("G101", "Rice", 60, 20))
    return inv


def test_add_product(inventory):
    assert len(inventory.get_all_products()) == 2


def test_duplicate_product(inventory):
    product = Electronics("E101", "Tablet", 30000, 2)

    with pytest.raises(DuplicateProductError):
        inventory.add_product(product)


def test_get_product(inventory):
    product = inventory.get_product("E101")
    assert product.name == "Laptop"


def test_product_not_found(inventory):
    with pytest.raises(ProductNotFoundError):
        inventory.get_product("X101")


def test_update_stock(inventory):
    inventory.update_stock("E101", 10)
    assert inventory.get_product("E101").quantity == 10


def test_remove_product(inventory):
    inventory.remove_product("G101")
    assert len(inventory.get_all_products()) == 1


def test_remove_missing_product(inventory):
    with pytest.raises(ProductNotFoundError):
        inventory.remove_product("X101")


def test_search_product(inventory):
    results = inventory.search_product("lap")
    assert len(results) == 1
    assert results[0].name == "Laptop"


def test_sell_product(inventory):
    inventory.sell_product("E101", 2)
    assert inventory.get_product("E101").quantity == 3


def test_insufficient_stock(inventory):
    with pytest.raises(InsufficientStockError):
        inventory.sell_product("E101", 10)


def test_invalid_sale_quantity(inventory):
    with pytest.raises(ValueError):
        inventory.sell_product("E101", 0)


def test_total_inventory_value(inventory):
    expected = (50000 * 5 * 1.18) + (60 * 20)
    assert inventory.total_inventory_value() == expected
