from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from file import File


fileName = "inventory.json"

class Main:
    __inventory = Inventory()
    __file = File(fileName)

    def __init__(self):
        file = self.__file
        inventory = self.__inventory
        self.read_file()
        self.display_menu()
        while True:
            option = self.get_input()
            if option == 1:
                inventory.display_products()
            elif option == 2:
                self.add_products(inventory)
            elif option == 3:
                self.update_stocks(inventory)
            elif option == 4:
                self.search_products(inventory)
            elif option == 5:
                self.save_products(inventory,file)
            elif option == 6:
                self.end(inventory,file)
                break


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
        file = self.__file
        self.__inventory = file.load_invetory()

    def add_products(slef,inventory):
        print("Add Product")
        while True:
            try:
                productType = int(input("Enter the product type [1:Physical,2:Digital]: "))
                productID = input("Enter the product ID: ")
                productName = input("Enter the product name: ")
                productPrice = float(input("Enter the product price: $"))
                productStock = int(input("Enter the product stock: "))

                if productType == 1:
                    productWeight = float(input("Enter the product weight: "))
                    product = PhysicalProduct(productID,productName,productPrice,productStock,productWeight)
                elif productType == 2:
                    productSize = float(input("Enter the product download size: "))
                    product = DigitalProduct(productID,productName,productPrice,productStock,productSize)
                else:
                    print("Please only use int 1 or 2! for product types!")
                    continue
                break
            except:
                print("Please input valid fields!")
        inventory.add_products(product)

    def update_stocks(self,inventory):
        itemID = input("Enter Product ID: ")
        product = inventory.search_products(itemID)
        if product != []:
            print(f"Product Found:")
            print(f"Name: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
            newStock = int(input("Enter new stock quantity: "))
            product.update_stock(newStock)
            print("Stock updated successfully!")
            return
        print("Product not in inventory,,")

    def search_products(self,inventory):
        itemID = input("Enter Product ID: ")
        product = inventory.search_products(itemID)
        if product != None:
            print("------------------------------------------------")
            product.display_information()
            print("------------------------------------------------")
            return
        print("Product not in inventory,,")

    def save_products(self,inventory,file):
        print("Saving inventory...")
        print("Saving inventory...")
        file.save_inventory(inventory.get_inventory())
        print(f"Inventory saved successfully to {fileName}.\n")

    def end(self,inventory,file):
        print("Saving inventory before exit...")
        file.save_inventory(inventory.get_inventory())
        print("Inventory saved successfully.\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
                        

if __name__ == "__main__":
    main = Main()