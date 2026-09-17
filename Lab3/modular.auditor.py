
def get_valid_input(total,failed):
    while True:
        stock=input("Enter stock quantity: ")
        if stock == "quit":
            return total
        if not stock.isdigit():
            failed+=1
            continue
        total=process_delivery(total,int(stock))

def process_delivery(current_total,new_value):
    current_total+=new_value
    return current_total


print(get_valid_input(total=0,failed=0))