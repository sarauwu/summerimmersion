# --- Define your functions below! ---
import random
# The chatbot introduces itself and gives the user instructions.
def intro():
  print("Hi, my name is Chatbot. Let's talk!")
  print("Type something and hit enter.")

#choices
valid = ["good", "great"]
gamechoice = ["word", "guess", "guessing", "word guessing"]
positiveanswerchoice = ["yes", "sure", "yeh"]
rockgame = ["rock", "scissors", "paper"]

# Choose a response based on the user's input.
def process_input(answer):
  if answer == "hi":
    say_greeting()
  else:
    say_default()
def namee(name):
    print("Nice to meet you " + name)
def mood(answer):
    while True:
        if answer.lower() in valid:
            print("That's good to hear!")
            break
        elif answer == "bad":
            print("I hope it gets better")
            break
        else:
            say_default()
            break

#game functions
#adventure game
def adven():
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
#word game
def wordga():
    start = '''
    It was a dark, gloomy halloween night, and you and your friends found a haunted house.
    You go inside.
    The power is out, so everything is dark. Then, you see a light. Two lights, in fact.
    One leads to a red door, and the other leads to a blue door.
    '''
    #starting the game...
    print(start)
    user_input = input("Which one do you want to go through? ")
    #starting the choices
    if user_input == "red":
        print("You decided to go through the red door, and beyond it you see two staircases.")
        print("One is green, and the other is yellow.")
        user_input = input("Which staircase do you go up?")
        if user_input == "green":
            print("You go up the green staircase. When you reach the top, you're in a gross, big room that had two trap doors.")
            print("One is white, and the other is black.")
            user_input = input("Which one do you go through? ")
            if user_input == "black":
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
            else:
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
        else:
            print("You go up the yellow staircase. When you reach the top, you're in a gross, big room that had two trap doors.")
            print("One is white, and the other is black.")
            user_input = input("Which one do you go through? ")
            if user_input == "black":
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
            else:
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")

    else:
        print("You decided to go through the blue door, and beyond it you see two staircases.")
        print("One is purple, and the other is orange.")
        user_input = input("Which staircase do you go up?")
        if user_input == "purple":
            print("You go up the purple staircase. When you reach the top, you're in a gross, big room that had two trap doors.")
            print("One is white, and the other is black.")
            user_input = input("Which one do you go through? ")
            if user_input == "black":
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
            else:
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
        else:
            print("You go up the orange staircase. When you reach the top, you're in a gross, big room that had two trap doors.")
            print("One is white, and the other is black.")
            user_input = input("Which one do you go through? ")
            if user_input == "black":
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
            else:
                print("The trap door lands you in a long, narrow hallway that leads to a room.")
                print("In the room sits an electric chair, a gun, a knife, and a ninja.")
                print("In order to escape, you must use on of them on yourself.")
                user_input = input("Which one do you choose? ")
                if user_input == "electric chair":
                    print("Because the power is out, you escaped unscathed. Good job!")
                elif user_input == "gun":
                    print("You make it out of the room after shooting yourself in the foot but you died of bloodloss.")
                elif user_input == "knife":
                    print("You stabbed yourself in the arm, and that arm will never be the same again.")
                else:
                    print("The ninja kills you. He feels no remorse.")
#rockpaperscissors game
def rockugame():
    from random import randint

    #create a list of play options

    t = ["rock", "paper", "scissors"]

    #assign a random play to the computer
    computer = t[randint(0,2)]


    #set player to False
    player = False

    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors? ")
        if player == computer:
            print("Tie!")
            break
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                break
            else:
                print("You win!", player, "smashes", computer)
                break
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                break
            else:
                print("You win!", player, "covers", computer)
                break
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                break
            else:
                print("You win!", player, "cut", computer)
                break
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]

#game to play
def thingstodo(answer):
    if answer.lower() in positiveanswerchoice:
        print("Awesome")
        print("What type of game do you want to play?")
        answer = input("('Adventure', 'Word Guessing' or 'Rock, Paper, Scissors') ")
        if answer.lower() in gamechoice:
            wordga()
            while True:
                answer = input("(Do you want to play again?) ")
                if answer.lower() in positiveanswerchoice:
                    adven()
                else:
                    say_default()
                    break
        elif answer.lower() == "adventure":
            adven()
            while True:
                answer = input("(Do you want to play again?) ")
                if answer.lower() in positiveanswerchoice:
                    adven()
                else:
                    say_default()
                    break
        elif answer.lower() in rockgame:
            rockugame()
            while True:
                answer = input("(Do you want to play again?) ")
                if answer.lower() in positiveanswerchoice:
                    adven()
                else:
                    say_default()
                    break
    else:
        say_default()

#poems
#The Narrow Road to Deep North
def poem1():
    print("The door of thatched hut")
    print("Also changed the owner.")
    print("At the Doll's Festival")
def poem2():
    print("Spring is passing.")
    print("The birds cry, and the fishes fill")
    print("With tears on their eyes.")
def poem3():
    print("Grasses in summer.")
    print("The warriors' dreams")
    print("All that left."")
def poem4():
    print("The early summer rain")
    print("Leaves behind")
    print("Hikari-do")






    
# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

# Display a default message to the user.
def say_default():
  print("Okay uwu")


# --- Put your main program below! ---
def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)
    answer = input("(What is your name?) ")
    namee(answer)
    answer = input("(How are you?) ")
    mood(answer)
    answer = input("(Do you want to play a game??) ")
    thingstodo(answer)
    answer = input("(Are you sure you dont want to play a game?) ")
    if answer.lower() in positiveanswerchoice:
        say_default()
    else:
        answer = input("(Then say yes!) ")
        thingstodo(answer)
    #answer = input("(Do you want to hear a poem?) ")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
