
items = int(input("how many items?"))
total = 0
for i in range(0,items):
    itemName = input("What the item? ")
    price = float(input("Whats the price"))
    total = total + price
    print("thanks for buying " + itemName)
    
print("Your total is: " + str(total))
