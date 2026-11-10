from ..Inventory import Inventory
from ..DigitalProduct import DigitalProduct
from ..PhysicalProduct import PhysicalProduct
from ..supplier import Supplier


def test_remove_physical_product_keeps_digital_product():
    inventory = Inventory()
    supplier = Supplier("TEST-SUPPLIER", "Test Supplier", "test@example.com")
    physical_product = PhysicalProduct(
        "TEST-PHYSICAL-001", "Physical product", 10.0, 5, 1.0, supplier
    )
    digital_product = DigitalProduct(
        "TEST-DIGITAL-001", "Digital product", 10.0, 5, 1.0, supplier
    )

    inventory.add_products(physical_product)
    inventory.add_products(digital_product)

    products = inventory.get_inventory()
    print(f"Current invetory:{products}")

    inventory.remove_products(physical_product.get_id())

    assert inventory.search_products(physical_product.get_id()) is None
    assert inventory.search_products(digital_product.get_id()) is digital_product

    print(f"removed invetory:{products}")

if __name__ == "__main__":
    test_remove_physical_product_keeps_digital_product()