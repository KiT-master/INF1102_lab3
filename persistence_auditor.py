from pathlib import Path

inventory = 0
processCount = 0
failedCount = 0
tax = 0.0
orders = []
fileName = "orders.txt"

def read_file(orders):

    if Path(fileName).exists() == False:
        with open(fileName,'+w') as file:
            file.write("1001,Wireless Mouse,2\n")
            file.write("1002,Keyboard,1\n")
            file.write("1003,USB Cable,3")
        file.close()

    with open(fileName,'+r') as file:
        for line in file:
            orders.append(line.strip())
        file.close()
    return orders

def save_output(output):
    with open(fileName,'+a') as file:
        file.write(str(output))
    file.close()

def read_input(orders):
    for i in orders:
        item = i.split(",")
        print(f"{item[0]}, {item[1]}, {item[2]}")

def get_valid_product_name():
    
    productName = input("Enter the product name: ")
    if productName.lower() == 'quit':
        return None
    return productName

def get_valid_input_quantity():
    userInput = input("Enter quantity: ")
    if userInput.lower() == 'quit':
        return None
    if userInput[0] == '-':
        print("Invalid input. Please enter a positive int.")
        return False
    elif userInput.isdigit() == False:
        print("Invalid input. Please enter a valid int.")
        return False
    return int(userInput)

def process_inventory(current_value, new_value):
    inventory = current_value + new_value
    return inventory
def calculate_tax(amount):
    return 0.10 * amount
def generate_report(total_units, failed_units):
    print(f"Total number of processes: {total_units} ,\nTotal number of failed processes: {failed_units},\nTotal inventory count: {inventory},\nTotal tax collected: {tax}")


while True:
    orders = []
    print("Current orders:\n\n")
    read_file(orders)
    read_input(orders)
    newItem = ""

    itemName = get_valid_product_name()
    itemQuantity = get_valid_input_quantity()

    if itemName == None or itemQuantity == None:
        print("Exiting the program.")
        break

    newItem = f"{int(orders[-1].split(',')[0]) + 1},{itemName},{itemQuantity}"

    print(f"New item added: {newItem}")
    save_output("\n"+newItem)
    print(f"Order sucessfully saved to {fileName}.\n\n")
# while True:
#     read_input()
    

#generate_report(processCount, failedCount)