from pathlib import Path
import json
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Supplier import Supplier

class File:
    __fileName = ""

    def __init__(self, fileName):
         self.__fileName = fileName

    def load_invetory(self):
        fileName = self.__fileName
        inventory = Inventory()

        if not Path(fileName).exists():
            print(f"File {fileName} does not exist. Creating a new file...")
            supplier = {
                "supplier_id": "S001",
                "name": "Default Supplier",
                "contact_email": "supplier@example.com",
            }
            with open(fileName, "w") as file:
                items = [{
                    "Type":"Physical",
                    "ID":"P001",
                    "Name":"Laptop",
                    "Price":1200.0,
                    "Stock":40,
                    "Weight":10,
                    "supplier": supplier,
                },
                {
                    "Type":"Physical",
                    "ID":"P002",
                    "Name":"Mouse",
                    "Price":25.50,
                    "Stock":40,
                    "Weight":10,
                    "supplier": supplier,
                },
                {
                    "Type":"Physical",
                    "ID":"P003",
                    "Name":"Keyboard",
                    "Price":45.0,
                    "Stock":25,
                    "Weight":10,
                    "supplier": supplier,
                },
                {
                    "Type":"Digital",
                    "ID":"P004",
                    "Name":"Windows",
                    "Price":100.0,
                    "Stock":25,
                    "Size":100,
                    "supplier": supplier,
                }
                ]

                json.dump(items, file, indent=2)
            print(f"{fileName} created successfully.")

        with open(fileName, "r") as file:
            print(f"{fileName} found")
            inventory_raw = json.load(file)
            for p in inventory_raw:
                supplier_data = p.get("supplier")
                if supplier_data is None:
                    print(
                        f"Warning: product {p['ID']} has no supplier data; "
                        "using Unknown Supplier."
                    )
                    supplier = Supplier(
                        "UNKNOWN", "Unknown Supplier", "unknown@example.com"
                    )
                else:
                    supplier = Supplier(
                        supplier_data["supplier_id"],
                        supplier_data["name"],
                        supplier_data["contact_email"],
                    )

                if p["Type"] == "Physical":
                    product = PhysicalProduct(
                        p["ID"], p["Name"], p["Price"], p["Stock"], p["Weight"],
                        supplier,
                    )
                elif p["Type"] == "Digital":
                    product = DigitalProduct(
                        p["ID"], p["Name"], p["Price"], p["Stock"], p["Size"],
                        supplier,
                    )
                else:
                    raise ValueError(f"Unknown product type: {p['Type']}")
                inventory.add_products(product=product)
            print(f"Inventory loaded successfully.")
        return inventory

    def save_inventory(self,inventory):
        fileName = self.__fileName
        json_inventory = []

        for product in inventory:
            supplier = product.supplier
            item = {
                "ID": product.get_id(),
                "Name": product.get_name(),
                "Price": product.get_price(),
                "Stock": product.get_stock(),
                "supplier": {
                    "supplier_id": supplier.supplier_id,
                    "name": supplier.name,
                    "contact_email": supplier.contact_email,
                },
            }
            if isinstance(product, PhysicalProduct):
                item["Type"] = "Physical"
                item["Weight"] = product.get_weight()
            elif isinstance(product, DigitalProduct):
                item["Type"] = "Digital"
                item["Size"] = product.get_size()
            else:
                raise TypeError(f"Unsupported product type: {type(product).__name__}")
            json_inventory.append(item)

        with open(fileName, "w") as file:
            json.dump(json_inventory, file, indent=2)

    
