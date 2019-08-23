scores = []
# of students
students = int(input("How many students are in your class? "))

print("Now enter each students score on their last test ")
#while for not knowing how many times your want to interate the code
for i in range(students):
    while True:
        scr = int(input("Enter a score: "))
        if scr < 0:
            print("Try again")
        else:
            scores.append(scr)
            break

scores.sort()

print(scores)
print ("Highest score", max(scores))
print ("Lowest score", min(scores))
print("Average:", sum(scores)/len(scores))
