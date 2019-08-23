
#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
text = f.read().strip().split()

print("\nCan your password survive a dictionary attack? You have three tries.")
for i in range(3):
    x = input("Type in a trial password: ")
    if x in text:
        print("The password: " + "'"+ (x) + "'" + " is too weak.")
        print("I hacked you! HAHA")
        print("Try again!\n")
    else:
        print("Good job")
        break
