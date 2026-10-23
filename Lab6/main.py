import json
from product import Product
from inventory import Inventory

def load_inventory():
    try:
        with open("inventory.json", "r", encoding="utf-8") as file:
            data_list = json.load(file)

        # Convert the list into a dictionary keyed by ID
        for item in data_list:
            item["ID"] = Product(item)

        data_dict = {item["ID"]: item for item in data_list}

        print("""Inventory.json found.
Inventory loaded successfully
""")

        return data_dict

    except FileNotFoundError:
        # Start with an empty inventory
        return {}

def save_inventory(inventory):
    with open("inventory.json", "w", encoding="utf-8") as file:
        json.dump(list(inventory.values()), file, indent=4)

def get_valid_input():
    while True:
        choice = input("Enter option: ")
        if choice in ("1","2","3","4","5","6"):
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

def get_non_negative_number(field,type,prompt):
    while True:
            try:
                value = type(input(f"{prompt}"))
    
                if value < 0:
                    print(f"{field} cannot be negative.")
                    continue
    
                return value
            except ValueError:
                print("Please enter a number.")


def add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ")

    if product_id in inventory:
        print("Product ID already exists.")
        return

    name = input("Product Name: ")


    
    price = get_non_negative_number("price",float,"price: ")
    
    stock = get_non_negative_number("stock",int,"stock: ")

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

    stock = get_non_negative_number("stock", int, "New Stock Quantity: ")
           

    inventory[product_id]["Stock"] = stock
    print("Stock updated successfully!")

def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found.")
        return

    product = inventory[product_id]

    print("Product Found")
    print("------------------------------------------------")
    print(f"ID: {product['ID']}")
    print(f"Name: {product['Name']}")
    print(f"Price: {product['Price']}")
    print(f"Stock: {product['Stock']}")
    print("------------------------------------------------")

def program():
    print("""========================================
INVENTORY MANAGEMENT SYSTEM
======================================
""")
    inventory = load_inventory()
    print("""----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------""")
    while True:
        value = get_valid_input()
        if value == "1":
            display(inventory)
        if value == "2":
            add_product(inventory)
        if value == "3":
            update_stock(inventory)
        if value == "4":
            search_product(inventory)
        if value == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to load_inventory.json.")
        if value == "6":
            print("Saving inventory before exit...")
            break

    save_inventory(inventory)
    print("Inventory saved successfully.")
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")


program()




