from random import sample
import json
import pygame

pygame.mixer.init()
pygame.mixer.music.load("jingle.mp3")
pygame.mixer.music.play()

#empty lists that will contain questions and answers
questions = []
answers = []
#possible answer choices that you can get
positiveanswers = ("yes", "ye", "yeah")
negativeanswers = ("no", "nah")
#a dictionary containing keys of letter grades and values of number grade intervals
grades = {
    "A+": [97,100],
    "A": [94, 96],
    "A-": [90,93],
    "B+": [87,89],
    "B": [84, 86],
    "B-": [80,83],
    "C+": [77,79],
    "C": [74, 76],
    "C-": [70,73],
    "D+":[67,69],
    "D": [65, 66],
    "D-": [60,64],
    "F": [0, 59]
}
#defining function where a letter grade would be returned based on the number grade
def lettergrade(number_grade):
    for letter, bounds in grades.items():
        if number_grade >= bounds[0] and number_grade <= bounds[1]:
            return letter

print("Welcome to the random quiz generator")

print("Please input a question and then answer")

#the juice of the code :)
def quiz():
    wrongquestion = []
    wronganswer = []
    rightanswer = []

    num_right = 0

    #pair a question and answer together based on order
    key = list(zip(questions, answers))

    #randomnize the questions and answers that you have
    randomnize = sample(key, len(questions))

    for i in randomnize:
        #[0] for question and [1] for answer
        print(i[0])
        user_answer = input("Your Guess: ")
        if user_answer.lower() == i[1].lower():
            print("Correct!!!")
            num_right += 1
        else:
            print("Not Correct")
            wrongquestion.append(i[0])
            wronganswer.append(user_answer)
            rightanswer.append(i[1])

    print('\n')

    print("You got " +str(num_right)+ "/" +str(len(questions))+ " Questions Correct")
    number_grade = (num_right/len(questions))*100
    print("That is a " +str(number_grade)+ "% or '" +lettergrade(number_grade)+ "'")
    print('\n')
    if number_grade != 100:
        print("The question(s) you got wrong were: ")
        for item in wrongquestion:
            print(item)
            print ('\n')
        print("The answer(s) were: ")
        for item in rightanswer:
            print(item)
            print ('\n')
        print("You typed in: ")
        for item in wronganswer:
            print(item)
            print ('\n')
    while True:
        print("Do you want to take the quiz again?")
        answer = input()
        if answer.lower() in positiveanswers:
            quiz()
            break
        elif answer.lower() in negativeanswers:
            print("Okay")
            break
        else:
            print("That's not an answer choice")
while True:
    print("Do you want to input a question and answer?")
    answer = input()
    if answer.lower() in positiveanswers:
        questioninput = input("Input a Question: ")
        questions.append(questioninput)
        with open('file.json', 'w') as outfile:
            json.dump([{'question:':questions, 'answer':answers} for questions, answers in zip(questions, answers)], outfile)
        answerinput = input("Input an Answer: ")
        answers.append(answerinput)
        with open('file.json', 'w') as outfile:
            json.dump(list(answers),outfile)
    elif answer.lower() in negativeanswers:
        break
    else:
        print("That's not an answer choice...")
quiz()