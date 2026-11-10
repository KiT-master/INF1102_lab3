import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier
from Product import Product


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_show_product_details() -> None:
    supplier = Supplier("TEST-SUPPLIER", "Test Supplier", "test@example.com")
    digital_product = DigitalProduct(
        "TEST-DIGITAL-001", "Digital product", 12.0, 5, 1.0, supplier
    )
    physical_product = PhysicalProduct(
        "TEST-PHYSICAL-001", "Physical product", 10.0, 5, 2.0, supplier
    )

    show_product_details(digital_product)
    show_product_details(physical_product)


if __name__ == "__main__":
    test_show_product_details()
