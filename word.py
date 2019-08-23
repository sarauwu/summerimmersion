import random
#starting message
print("Welcome to the word guessing game!")
print("The word can be one or two words~")
while True:
    start = input("Do you want to start the game? (yes/no): ")
    if start == "yes":
        print("Let's start! Good luck uwu'")
        break
    else:
        print("Say yes :'(")
#word list
words = ["moodys", "girls who code", "tired", "summer", "game", "food", "lunch", "pasta", "potato chips", "lobster roll", "sleep", "music", "college"]

word = random.choice(words)

print("Guess the letters. You have 9 tries")

guesses = ''
#of chances
turns = 9

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed +=1
    if failed == 0:
        print("Good job, you win!")
        print("The word is: ", word)
        break

    guess = input("guess the character: ")
    guesses += guess

    if guess not in word:
        turns -=1
        print("Wrong, Try again...")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose. Better luck next time LOL")
            print("The word is: ", word)
            break
