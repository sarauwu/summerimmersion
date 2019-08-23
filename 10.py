#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print('\n\n')
print("Can your password survive a dictionary attack?")

print('\n')
text = f.read().strip().split()
#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

answer = input("Type in a trial password: ")
#Write logic to see if the password is in the dictionary file below here:
for word in f:
    if answer in text:
        print("That word already exists!")
        print("Try another password.")
    else:
        print("good job")
        break
