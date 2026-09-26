INVENTORY_FILE = "inventory.txt"


def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            lines = file.read().splitlines()
            total = int(lines[0]) if lines else 0
            if len(lines) > 1 and lines[1]:
                history=[]
                for value in lines[1].split(","):
                    history.append(int(value))
            else:
                history = []

            return total, history

    except FileNotFoundError:
        # Start with an empty inventory
        return 0, []

def get_valid_input():
    failed=0
    while True:
        stock=input("Enter stock quantity or 'quit': ")
        if stock == "quit":
            return "quit", failed
        if stock.isdigit():
            return int(stock), failed
        failed+=1
        print("Invalid entry, try again")
    
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
    total_tax=0
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
    generate_report(total,total_failed,total_tax)

program()




