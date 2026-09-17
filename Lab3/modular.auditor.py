
def get_valid_input(total,failed):
    while True:
        stock=input("Enter stock quantity: ")
        if stock == "quit":
            return total, failed
        if not stock.isdigit():
            failed+=1
            continue
        total=process_delivery(total,int(stock))

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
    total_amount,failed_number=get_valid_input(total=0,failed=0)
    tax=calculate_tax(total_amount)
    generate_report(total_amount, failed_number, tax)

program()




