from pathlib import Path
import json
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory

class File:
    __fileName = ""

    def __init__(self, fileName):
         self.__fileName = fileName

    def load_invetory(self):
        fileName = self.__fileName
        inventory = Inventory()

        if Path(fileName).exists() == False:
            print(f"File {fileName} does not exist. Creating a new file...")
            with open(fileName,'+w') as file:
                items = [{
                    "Type":"Physical",
                    "ID":"P001",
                    "Name":"Laptop",
                    "Price":1200.0,
                    "Stock":40,
                    "Weight":10
                },
                {
                    "Type":"Physical",
                    "ID":"P002",
                    "Name":"Mouse",
                    "Price":25.50,
                    "Stock":40,
                    "Weight":10
                },
                {
                    "Type":"Physical",
                    "ID":"P003",
                    "Name":"Keyboard",
                    "Price":45.0,
                    "Stock":25,
                    "Weight":10
                },
                {
                    "Type":"Digital",
                    "ID":"P004",
                    "Name":"Windows",
                    "Price":100.0,
                    "Stock":25,
                    "Size":100
                }
                ]

                json.dump(items, file)
            print(f"{fileName} created successfully.")
            file.close()

        with open(fileName,'+r') as file:
            print(f"{fileName} found")
            inventory_raw = json.load(file)
            for p in inventory_raw:
                if p["Type"] == "Physical":
                    inventory.add_products(product=PhysicalProduct(p["ID"],p["Name"],p["Price"],p["Stock"],p["Weight"]))
                elif p["Type"] == "Digital":
                    inventory.add_products(product=DigitalProduct(p["ID"],p["Name"],p["Price"],p["Stock"],p["Size"]))
            print(f"Inventory loaded successfully.")
        file.close()
        return inventory

    def save_inventory(self,inventory):
        fileName = self.__fileName
        json_inventory = []

        #1 line if else for loop to one shot convert into json convertable format
        #Try for fun HAHAHA
        #for p in inventory: print(f"Checking Object Type {p.get_fulfilment_info().split()[3]}")
        json_inventory = [ {"Type":"Physical","ID":p.get_id(), "Name": p.get_name(), "Price": p.get_price(), "Stock": p.get_stock(),"Weight": p.get_weight()} if  p.get_fulfilment_info().split()[3] == "physical" else {"Type":"Digital","ID":p.get_id(), "Name": p.get_name(), "Price": p.get_price(), "Stock": p.get_stock(),"Size": p.get_size()} 
                          for p in inventory]
        
        with open(fileName,'w') as file:
            json.dump(json_inventory, file)
        file.close()

    

