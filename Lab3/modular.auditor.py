
def get_valid_input(total,failed):
    while True:
        stock=input("Enter stock quantity: ")
        if stock == "quit":
            return total
        if not stock.isdigit():
            failed+=1
            continue
        total+=int(stock)

print(get_valid_input(total=0,failed=0))