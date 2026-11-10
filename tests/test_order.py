import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from DigitalProduct import DigitalProduct
from Order import Order
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier


def test_order_total_with_digital_and_physical_products():
    supplier = Supplier("TEST-SUPPLIER", "Test Supplier", "test@example.com")
    digital_product = DigitalProduct(
        "TEST-DIGITAL-001", "Digital product", 50.0, 5, 1.0, supplier
    )
    physical_product = PhysicalProduct(
        "TEST-PHYSICAL-001", "Physical product", 10.0, 5, 2.0, supplier
    )

    order = Order("TEST-ORDER-001")
    order.add_order_line(digital_product, 2)
    order.add_order_line(physical_product, 3)

    total = order.caculate_total()
    print(f"Order total: ${total:.2f}")



if __name__ == "__main__":
    test_order_total_with_digital_and_physical_products()
