
import pytest

from inventory.product import Electronics, Grocery
from inventory.inventory import Inventory
from inventory.storage import Storage
from inventory.exceptions import InventoryError


@pytest.fixture
def inventory():
    inv = Inventory()
    inv.add_product(Electronics("E101", "Laptop", 50000, 3))
    inv.add_product(Grocery("G101", "Rice", 60, 20))
    return inv


def test_save_json(inventory, tmp_path):
    file = tmp_path / "inventory.json"

    Storage.save_json(inventory, file)

    assert file.exists()


def test_load_json(inventory, tmp_path):
    file = tmp_path / "inventory.json"

    Storage.save_json(inventory, file)
    loaded = Storage.load_json(file)

    assert len(loaded.get_all_products()) == 2
    assert loaded.get_product("E101").name == "Laptop"


def test_json_preserves_product_type(inventory, tmp_path):
    file = tmp_path / "inventory.json"

    Storage.save_json(inventory, file)
    loaded = Storage.load_json(file)

    assert isinstance(
        loaded.get_product("E101"), Electronics
    )


def test_save_csv(inventory, tmp_path):
    file = tmp_path / "inventory.csv"

    Storage.save_csv(inventory, file)

    assert file.exists()


def test_load_csv(inventory, tmp_path):
    file = tmp_path / "inventory.csv"

    Storage.save_csv(inventory, file)
    loaded = Storage.load_csv(file)

    assert len(loaded.get_all_products()) == 2
    assert loaded.get_product("G101").name == "Rice"


def test_csv_preserves_product_type(inventory, tmp_path):
    file = tmp_path / "inventory.csv"

    Storage.save_csv(inventory, file)
    loaded = Storage.load_csv(file)

    assert isinstance(
        loaded.get_product("G101"), Grocery
    )


def test_missing_json_file(tmp_path):
    file = tmp_path / "missing.json"

    with pytest.raises(InventoryError):
        Storage.load_json(file)


def test_missing_csv_file(tmp_path):
    file = tmp_path / "missing.csv"

    with pytest.raises(InventoryError):
        Storage.load_csv(file)


def test_malformed_json(tmp_path):
    file = tmp_path / "invalid.json"
    file.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(InventoryError):
        Storage.load_json(file)
