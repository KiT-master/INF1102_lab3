from Product import Product
from Inventory import Inventory
from file import File


fileName = "inventory.json"

class Main:
    __inventory = Inventory

    def __init__(self):
        while True:
            self.read_file()
            self.display_menu()
            option = self.get_input()
            if option == 1:
                self.__inventory.display_products()
            elif option == 2:
                print("Add Product")
                productID = input("Enter the product ID: ")
                productName = input("Enter the product name: ")
                productPrice = float(input("Enter the product price: $"))
                productStock = int(input("Enter the product stock: "))
                product = Product(productID,productName,productPrice,productStock)
                self.__inventory.add_products(product)



    def display_menu(self):
        print("========================================")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("========================================\n")
        print("----------- MENU -----------")
        print("1. Display All Products\n"+
                "2. Add Product\n"+
                "3. Update Stock\n"+
                "4. Search Product\n"+
                "5. Save Inventory\n"+
                "6. Exit")
        print("----------------------------\n")

    def get_input(self):
        while True:
            try: 
                option = input("Enter option: ")
                option = int(option)
                if option < 1 or option > 6: raise ValueError
                break
            except:
                print("Invalid option pls chose from 1-6,")
                continue

        return option

    def read_file(self):
        file = File(fileName)
        self.__inventory = file.load_invetory()
