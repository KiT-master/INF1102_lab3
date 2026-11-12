import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from DigitalProduct import DigitalProduct
from Order import Order
from Supplier import Supplier


def test_same_product_in_two_orders_creates_two_order_lines() -> None:
    """Expected: two OrderLine objects refer to the same single Product object."""
    supplier = Supplier("TEST-SUPPLIER", "Test Supplier", "test@example.com")
    product = DigitalProduct(
        "TEST-DIGITAL-001", "Digital product", 12.0, 5, 1.0, supplier
    )
    first_order = Order("TEST-ORDER-001")
    second_order = Order("TEST-ORDER-002")

    first_order.add_order_line(product, 1)
    second_order.add_order_line(product, 1)

    first_line = first_order.order_lines[0]
    second_line = second_order.order_lines[0]

    print(
        "OrderLine objects across both orders:",
        len(first_order.order_lines) + len(second_order.order_lines),
    )
    print("Are the OrderLine objects distinct?", first_line is not second_line)

    first_product = first_line._OrderLine__product
    second_product = second_line._OrderLine__product
    print("Do both OrderLines reference the same Product?", first_product is second_product)
    print("Product object IDs:", id(first_product), id(second_product))

if __name__ == "__main__":
    test_same_product_in_two_orders_creates_two_order_lines()