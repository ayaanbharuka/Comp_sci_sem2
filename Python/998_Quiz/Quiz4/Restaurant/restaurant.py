import random 
restaurants = ["taco bell", "subway", "burger king "]
tacobell = ["Taco","burrito","nachos"]
subway = ["sandwich","cookie","wrap"]
burgerking = ["burger","coke","fries"]
print("Choose a restaurant from the given list: ")
int1=input(restaurants)
randfood=random.randrange(0,3)

if int1 =="tacobell":
    print("You choose tacobell. They have", tacobell,". But we sugest for you to buy", tacobell[randfood])
elif int1=="subway":
    print("You choose subway. They have", subway,". But we sugest for you to buy", subway[randfood])
elif int1=="burgerking":
    print("You choose burgerking. They have", burgerking,". But we sugest for you to buy", burgerking[randfood])
