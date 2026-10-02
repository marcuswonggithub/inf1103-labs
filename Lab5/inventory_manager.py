

import json


def load_inventory():
    try:
    
        # Read the JSON file
        with open("load_inventory.json", "r", encoding="utf-8") as file:
            data_list = json.load(file)

        # Convert the list into a dictionary keyed by ID
        data_dict = {item["ID"]: item for item in data_list}

        print("""Inventory.json found.
        Inventory loaded successfully
        
----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------
Enter option: """)

        return data_dict

    except FileNotFoundError:
        # Start with an empty inventory
        return {}

def save_inventory(inventory):
    with open("load_inventory.json", "w", encoding="utf-8") as file:
        json.dump(list(inventory.values()), file, indent=4)

def get_valid_input():
    while True:
        choice = input("Enter option: ")
        if choice in (1,2,3,4,5,6):
            return choice
        print("Invalid entry, try again")

def display(inventory):
    print("Current Inventory")
    print("-------------------------------------------------------------------")
    for product in inventory.values():
        print(
            f"ID: {product['ID']} | "
            f"Name: {product['Name']} | "
            f"Price: {product['Price']} | "
            f"Stock: {product['Stock']}"
        )

    print("---------------------------------------------------------------------")

def add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ")

    if product_id in inventory:
        print("Product ID already exists.")
        return

    name = input("Product Name: ")

    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            break
        except ValueError:
            print("Please enter a number.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
                continue

            break
        except ValueError:
            print("Please enter a whole number.")

    inventory[product_id] = {
        "ID": product_id,
        "Name": name,
        "Price": f"${price:.2f}",
        "Stock": stock
    }

    print("Product added successfully")

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {inventory[product_id]['Name']}")
    print(f"Current Stock: {inventory[product_id]['Stock']}")

    while True:
        try:
            stock = int(input("New Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
                continue

            break
        except ValueError:
            print("Please enter a whole number.")

    inventory[product_id]["Stock"] = stock
    print("Stock updated successfully!")



def program():    
    inventory = load_inventory()
    
    while True:
        value=get_valid_input()
        if value == 1:
            display(inventory)
        if value == 2:
            add_product(inventory)
        if value == 3:
            update_stock(inventory)
        if value == 6:
            break
    save_inventory(inventory)



program()




