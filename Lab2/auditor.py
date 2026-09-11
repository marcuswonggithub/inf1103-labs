total=0
failed=0
while(True):
    stock=input("Enter stock quantity: ")
    if stock == "quit":
        break
    if not stock.isdigit():
        failed+=1
        continue
    if (stock)<0:
        failed+=1
        continue
    total+=(stock)
    if total>500:
        print("Inventory exceeds 500!")
        break

if stock=="quit":
    print(f"""Total Unit Processed: {total}
Number of Rejected Entries: {failed} """) 
    