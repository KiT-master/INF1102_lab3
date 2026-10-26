from pathlib import Path
import json
from Product import Product
from Inventory import Inventory

class File:
    __inventory = Inventory
    __fileName = ""

    def __init__(self, fileName):
         self.__fileName = fileName

    def load_invetory(self):
        fileName = self.__fileName
        inventory = Inventory

        if Path(fileName).exists() == False:
            print(f"File {fileName} does not exist. Creating a new file...")
            with open(fileName,'+w') as file:
                items = [{
                    "ID":"P001",
                    "Name":"Laptop",
                    "Price":1200.0,
                    "Stock":40
                },
                {
                    "ID":"P002",
                    "Name":"Mouse",
                    "Price":25.50,
                    "Stock":40
                },
                {
                    "ID":"P003",
                    "Name":"Keyboard",
                    "Price":45.0,
                    "Stock":25
                }
                ]

                json.dump(items, file)
            print(f"{fileName} created successfully.")
            file.close()

        with open(fileName,'+r') as file:
            print(f"{fileName} found")
            inventory_raw = json.load(file)
            for p in inventory_raw: inventory.add_products(p)
            print(f"Inventory loaded successfully.")
        file.close()