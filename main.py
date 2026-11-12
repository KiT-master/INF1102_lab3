from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from file import File
from Supplier import Supplier


fileName = "inventory.json"

class Main:
    def __init__(self):
        self.__inventory = Inventory()
        self.__file = File(fileName)
        self.read_file()
        self.display_menu()
        while True:
            option = self.get_input()
            if option == 1:
                self.__inventory.display_products()
            elif option == 2:
                self.add_products()
            elif option == 3:
                self.update_stocks()
            elif option == 4:
                self.search_products()
            elif option == 5:
                self.remove_product()
            elif option == 6:
                self.save_products()
            elif option == 7:
                self.end()
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
                "5. remove product\n"+
                "6. Save Inventory\n"+
                "7. Exit")
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
        self.__inventory = self.__file.load_invetory()

    def add_products(self):
        print("Add Product")
        while True:
            try:
                productType = int(input("Enter the product type [1:Physical,2:Digital]: "))
                productID = input("Enter the product ID: ")
                productName = input("Enter the product name: ")
                productPrice = float(input("Enter the product price: $"))
                productStock = int(input("Enter the product stock: "))
                supplier_id = input("Enter the supplier ID: ")
                supplier_name = input("Enter the supplier name: ")
                supplier_email = input("Enter the supplier contact email: ")
                supplier = Supplier(supplier_id, supplier_name, supplier_email)

                if productType == 1:
                    productWeight = float(input("Enter the product weight: "))
                    product = PhysicalProduct(
                        productID, productName, productPrice, productStock,
                        productWeight, supplier,
                    )
                elif productType == 2:
                    productSize = float(input("Enter the product download size: "))
                    product = DigitalProduct(
                        productID, productName, productPrice, productStock,
                        productSize, supplier,
                    )
                else:
                    print("Please only use int 1 or 2! for product types!")
                    continue
                break
            except:
                print("Please input valid fields!")
        self.__inventory.add_products(product)

    def update_stocks(self):
        itemID = input("Enter Product ID: ")
        product = self.__inventory.search_products(itemID)
        if product is not None:
            print(f"Product Found:")
            print(f"Name: {product.get_name()}\nCurrent Stock: {product.get_stock()}")
            newStock = int(input("Enter new stock quantity: "))
            product.update_stock(newStock)
            print("Stock updated successfully!")
            return
        print("Product not in inventory,,")

    def search_products(self):
        itemID = input("Enter Product ID: ")
        product = self.__inventory.search_products(itemID)
        if product != None:
            print("------------------------------------------------")
            product.display_information()
            print("------------------------------------------------")
            return
        print("Product not in inventory,,")

    def remove_product(self):
        inventory = self.__inventory
        itemID = input("Enter Product ID to remove: ")
        product = inventory.search_products(itemID)
        if product != None:
            self.__inventory.remove_products(itemID)
            print("------------------------------------------------")
            product.display_information()
            print("------------------------------------------------")
            print("Product removed!")
            return
        print("Product not found!")

    def save_products(self):
        print("Saving inventory...")
        print("Saving inventory...")
        self.__file.save_inventory(self.__inventory.get_inventory())
        print(f"Inventory saved successfully to {fileName}.\n")

    def end(self):
        print("Saving inventory before exit...")
        self.__file.save_inventory(self.__inventory.get_inventory())
        print("Inventory saved successfully.\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
                        

if __name__ == "__main__":
    main = Main()