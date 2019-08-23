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
