from Product import Product

class Inventory: 
    __products = []

    def add_products(self, product):
        self.__products.append(product)

    def get_inventory(self):
        return self.__products

    def search_products(self, ID):
        products = self.__products
        product = [p for p in products if p.get_id() == ID]
        product = [] if product == [] else product[0]
        return product

    def display_products(self):
        products = self.__products
        print("Displaying all products:")
        for p in products:
            print("------------------------------------------------")
            p.display_information()
            print("------------------------------------------------")