import json
from product import Product
from inventory import Inventory

def load_inventory():
    try:
        with open("inventory.json", "r", encoding="utf-8") as file:
            data_list = json.load(file)

        # Convert the list into a dictionary keyed by ID
        inventory = Inventory()
        for item in data_list:
            product_id = item["ID"]
            product_obj = Product(item["ID"], item["Name"], item["Price"], item["Stock"])
            inventory.add_product(product_id, product_obj)
        print("""Inventory.json found.
Inventory loaded successfully
""")

        return inventory

    except FileNotFoundError:
        # Start with an empty inventory
        return Inventory()

def save_inventory(inventory):
    storage_list = []
    inventory_list = inventory.display_all()
    for product in inventory_list:
        storage_list.append(product.display_information())
    
    with open("inventory.json", "w", encoding="utf-8") as file:
        json.dump(storage_list, file, indent=4)

def get_valid_input():
    while True:
        choice = input("Enter option: ")
        if choice in ("1","2","3","4","5","6"):
            return choice
        print("Invalid entry, try again")

def display(inventory):
    print("Current Inventory")
    print("-------------------------------------------------------------------")
    for product in inventory.display_all():
        print(" | ".join(
            f"{key}: {value}"
            for key, value in product.display_information().items()
        ))

    print("---------------------------------------------------------------------")

def get_non_negative_number(field,number_type,prompt):
    while True:
            try:
                value = number_type(input(f"{prompt}"))
    
                if value < 0:
                    print(f"{field} cannot be negative.")
                    continue
    
                return value
            except ValueError:
                print("Please enter a number.")


def handles_add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ")

    if inventory.search_product(product_id):
        print("Product ID already exists.")
        return

    name = input("Product Name: ")
    price = get_non_negative_number("price",float,"Price: ")
    stock = get_non_negative_number("stock",int,"Stock: ")

    new_product = Product(product_id, name, price, stock)
    inventory.add_product(product_id, new_product)

    print("Product added successfully")

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if not product:
        print("Product not found.")
        return

    print("Product Found:")
    details = product.display_information()
    print(f"Name: {details['Name']}")
    print(f"Current Stock: {details['Stock']}")

    stock = get_non_negative_number("stock", int, "New Stock Quantity: ")
           
    product.update_stock(stock)

    print("Stock updated successfully!")

def handles_search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)

    if not product:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    print("\n".join(
                f"{key}: {value}"
                for key, value in product.display_information().items()
            ))
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
        elif value == "2":
            handles_add_product(inventory)
        elif value == "3":
            update_stock(inventory)
        elif value == "4":
            handles_search_product(inventory)
        elif value == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif value == "6":
            print("Saving inventory before exit...")
            break

    save_inventory(inventory)
    print("Inventory saved successfully.")
    print("Thank you for using Inventory Management System.")
    print("Program terminated.")


program()




