from Product import Product
from supplier import Supplier

class DigitalProduct(Product):
    __download_size:float

    def __init__(self, product_id, name, price, stock, download_size,supplier:Supplier):
        super().__init__(product_id, name, price, stock,supplier)
        self.__download_size = download_size

    def get_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Dowload Size:{self.__download_size}")

    def get_fulfilment_info(self):
        productName = self.get_name()
        msg = f"The product:{productName} is delivered digitally!"
        return msg


if __name__ == "__main__":
    #Testing syntaxt
    supplier = Supplier("S001","KitKAt","9g@gmail.com")
    product = DigitalProduct(1, "Windows", 12 , 3, 4,supplier)
    product.display_information()
    print(product.get_fulfilment_info())