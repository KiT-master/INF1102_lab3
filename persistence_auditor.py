from pathlib import Path
import json

init = False
inventory = 0
processCount = 0
failedCount = 0
tax = 0.0
orders = []
fileName = "inventory.json"

def dump_file(orders):
    with open(fileName,'w') as file:
        json.dump(orders, file)
    file.close()
    


def read_file(orders):
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
        orders = json.load(file)
        print(f"Inventory loaded successfully.")
    file.close()
    return orders

def display_orders(orders):
    #orders = read_file(orders)
    print("Current Inventory:")
    print("------------------------------------------------")
    for i in orders:
        print(f"ID:{i['ID']}| Name:{i['Name']}| Price:${i['Price']:.2f}| Stock:{i['Stock']}")
    print("------------------------------------------------\n")
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
    print("\nProduct added successfully.\n")

    #Only be saved when option 4 mode
    #dump_file(orders)
    return orders


def update_stock(orders):
    itemID = input("Enter Product ID: ")

    for i in orders:
        if i['ID'] == itemID:
            print(f"Product Found:\nName: {i['Name']}\nCurrent Stock: {i['Stock']}")
            newStock = int(input("Enter new stock quantity: "))
            i['Stock'] = newStock
            #Only be saved when option 5 mode
            #dump_file(orders)
            print("Stock updated successfully!")
            return orders


    print("Item not found in inventory!")
    return orders

def search_product(orders):
    itemID = input("Enter Product ID: ")

    for i in orders:
        if i['ID'] == itemID:
            print("------------------------------------------------")
            print(f"ID: {i['ID']}\nName: {i['Name']}\nPrice: ${i['Price']:.2f}\nStock: {i['Stock']}")
            print("------------------------------------------------")
            return orders

    print("Item not found in inventory!")
    return orders





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
        orders = update_stock(orders)
    elif menuOption == '4':
        orders = search_product(orders)
    elif menuOption == '5':
        print("Saving inventory...")
        dump_file(orders)
        print(f"Inventory saved successfully to {fileName}.\n")
    elif menuOption == '6':
        print("Saving inventory before exit...")
        dump_file(orders)
        print("Inventory saved successfully.\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break