import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from DigitalProduct import DigitalProduct
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier


def test_show_product_details() -> None:
    supplier = Supplier("TEST-SUPPLIER", "Test Supplier", "test@example.com")
    digital_product = DigitalProduct(
        "TEST-DIGITAL-001", "Digital product", 12.0, 5, 1.0, supplier
    )
    physical_product = PhysicalProduct(
        "TEST-PHYSICAL-001", "Physical product", 10.0, 5, 2.0, supplier
    )

    inventory = Inventory()
    inventory.add_products(digital_product)
    inventory.add_products(physical_product)

    for product in inventory.get_inventory():
        product.display_information()
        print(product.get_fulfilment_info())


if __name__ == "__main__":
    test_show_product_details()
