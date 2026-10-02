

import json


def load_inventory():
    try:
    
        # Read the JSON file
        with open("load_inventory.json", "r", encoding="utf-8") as file:
            data_list = json.load(file)

        # Convert the list into a dictionary keyed by ID
        data_dict = {item["ID"]: item for item in data_list}

        print(data_dict["P002"]["Name"])  # Mouse

        return data_dict

    except FileNotFoundError:
        # Start with an empty inventory
        return {}

def save_inventory(inventory):
    with open("load_inventory.json", "w", encoding="utf-8") as file:
        json.dump(list(inventory.values()), file, indent=4)

def get_valid_input():
    while True:
        choice = input("""----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------
Enter option: """)
        if choice in (1,2,3,4,5,6):
            return choice
        print("Invalid entry, try again")

def program():    
    inventory = load_inventory()
    
    while True:
        value=get_valid_input()

        if value == 6:
            break
        total_tax+=calculate_tax(stock)
        total=process_delivery(total,stock)
        transaction_history.append(stock)
    generate_report(total,total_failed,total_tax)
    save_inventory(total,transaction_history)

program()











    
def process_delivery(current_total,new_value):
    current_total+=new_value
    return current_total

def calculate_tax(amount):
    tax=amount/10
    return tax

def generate_report(total_amount,failed_number,tax):
    print(f"""Total Unit Processed: {total_amount}
Number of Rejected Entries: {failed_number}
Total Tax: {tax} """) 


def program():    
    total, transaction_history = load_inventory()
    total_tax=calculate_tax(total)
    total_failed=0
    print(f"Previously Saved Total: {total}")
    print(f"Previous Transaction History: {transaction_history}")
    
    while True:
        stock,failed=get_valid_input()
        total_failed+=failed
        if stock == "quit":
            break
        total_tax+=calculate_tax(stock)
        total=process_delivery(total,stock)
        transaction_history.append(stock)
    generate_report(total,total_failed,total_tax)
    save_inventory(total,transaction_history)

program()




