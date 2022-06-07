x = input("Please enter a line length: ")
x=int(int(x))
y = input("do you want your line horizontal or vertical?: " )
if str(y) == str("vertical"):
    for i in range (0,x):
        print("*")
        
else:
    for i in range (0,x):
        print("*",end=" ")
            