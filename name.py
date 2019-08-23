#import random
#names = ["Bob", "Jerry", "Sam", "Oliver", "Alice", "Wendy", "Mary"]
#name = random.choice(names)
#print("Your name is: " + name)


import random
ranname = ["Bob", "Jerry", "Sam", "Oliver", "Alice", "Wendy", "Mary"]
ranbus= ["Apple", "Samsung", "Microsoft", "Google", "Samsung", "Walmart", "Target"]
#filler
names = random.choice(ranname)
businesses = random.choice(ranbus)
#filler
print("Do you want the name of a Business or just a Name?")
while True:
    namu = input("Type 'name' or 'business': ")
    if namu == "name":
        print(names)
    elif namu == "business":
        print(businesses)
    else:
        print("That is not a valid choice")
