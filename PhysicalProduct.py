from Product import Product
from CanBeShipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    __weight:float
    __SHIPPING_RATE_PER_KG = 3.0

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight
    
    def calculate_shipping_cost(self):
        return self.__weight * self.__SHIPPING_RATE_PER_KG

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight}")

    def get_fulfilment_info(self):
        productName = self.get_name()
        msg = f"The product:{productName} requires physical shipping!"
        return msg

if __name__ == "__main__":
    # Test shipping costs for products with different weights.
    lightProduct = PhysicalProduct(1, "kitkat", 12, 3, 1)
    heavyProduct = PhysicalProduct(2, "Heavy item", 30, 2, 4)
    productList = [lightProduct,heavyProduct]
    for i in productList:
        print(f"The Product:{i.get_name}")
        print(i.get_fulfilment_info())
        print(f"Shipping Cost:${i.calculate_shipping_cost()}")