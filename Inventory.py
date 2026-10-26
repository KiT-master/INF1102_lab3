from Product import Product

class Inventory: 
    __products = []

    def add_products(self, product):
        self.__products.append(product)

    def search_products(self, name):
        products = self.__products
        product = [i for i in products if i.__name == name][0]
        return product

    def display_products(self):
        products = self.__products
        print("Displaying all products:")
        for p in products:print(f"------------------------------------------------\nID: {p.__product_id}\nName: {p.__name}\nPrice: ${p.__price:.2f}\nStock: {p.__stock}\n------------------------------------------------\n")