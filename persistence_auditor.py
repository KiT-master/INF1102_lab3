from pathlib import Path
import json

init = False
inventory = 0
processCount = 0
failedCount = 0
tax = 0.0
orders = []
fileName = "inventory.json"

def read_file(orders):
    if Path(fileName).exists() == False:
        print(f"File {fileName} does not exist. Creating a new file...")
        with open(fileName,'+w') as file:
            items = [{
                "ID":1001,
                "Name":"Laptop",
                "Price":1200.0,
                "Stock":40
            },
            {
                "ID":1002,
                "Name":"Mouse",
                "Price":25.50,
                "Stock":40
            },
            {
                "ID":1003,
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
        orders = json.load(file)
        print(f"Inventory loaded successfully.")
    file.close()
    return orders

def add_product(orders):
    print("Add Product")
    productID = input("Enter the product ID: ")
    productName = input("Enter the product name: ")
    productPrice = float(input("Enter the product price: "))
    productStock = int(input("Enter the product stock: "))

    product = {
        "ID": productID,
        "Name": productName,
        "Price": productPrice,
        "Stock": productStock
    }
    orders.append(product)
    print(f"Updated Inventory:\n{orders}")
    print("\nProduct added successfully.\n")

    with open(fileName,'w') as file:
        json.dump(orders, file)
    file.close()
    return orders


def save_output(output):
    with open(fileName,'+a') as file:
        file.write(str(output))
    file.close()

def display_orders(orders):
    print(orders)
    print("Current Inventory:")
    print("------------------------------------------------")
    for i in orders:
        print(f"ID:{i['ID']}| Name:{i['Name']}| Price:${i['Price']:.2f}| Stock:{i['Stock']}")
    print("------------------------------------------------\n")



def initialize(orders):
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================\n")
    orders = read_file(orders)
    display_orders(orders)
    print("----------- MENU -----------")
    print("1. Display All Products\n"+
            "2. Add Product\n"+
            "3. Update Stock\n"+
            "4. Search Product\n"+
            "5. Save Inventory\n"+
            "6. Exit")
    print("----------------------------\n")
    return orders


while True:
    orders = []
    if init == False:
        orders = initialize(orders)
        init = True
    menuOption = input("Enter option: ")


    if menuOption == '1':
        print("Display All Products")
        display_orders(orders)
    elif menuOption == '2':
        orders = add_product(orders)
    elif menuOption == '3':
        pass
    elif menuOption == '4':
        pass
    elif menuOption == '5':
        pass
    elif menuOption == '6':
        pass
    