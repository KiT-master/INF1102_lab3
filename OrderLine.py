from Product import Product

class OrderLine:
    def __init__(self,product:Product,quantity:int):
        self.__product = product
        self.__quantity = quantity

    def caculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity