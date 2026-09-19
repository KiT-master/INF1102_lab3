inventory = 0
processCount = 0
failedCount = 0
tax = 0.0

def get_valid_input():
    userInput = input("Enter the inventory count (or type 'quit' to exit): ")
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
    userInput = get_valid_input()
    processCount += 1

    if userInput == None:
            break
    elif userInput == False:
            failedCount += 1
            continue

    inventory = process_inventory(inventory, userInput)
    tax += calculate_tax(userInput)
  
    if inventory > 500:
        print("Overstock Alert!")
        failedCount += 1
        break

generate_report(processCount, failedCount)