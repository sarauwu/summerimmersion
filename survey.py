import json
data = {'cat' : 'dog'}
def ask (question):
    return (input(question+'   '))
questions = [['What is your name?','Name'],['What is your date of birth? (MM/DD/YYYY)','Birthday'],['What is your age?','Age'],['Where do you call home? (City, State, Country)','Home'],['How many people live in your home more than 50% of the time?','Family'],['How many hours per week do you spend on the phone?','Phone'],['Name the app, program, or website that you use most frequently.','Program/App']]

while True:
    print ('\n\nStarting new survey!')
    answer={}
    for q in questions:
        answer[q[1]] = ask(q[0])
    with open('results.json') as json_file:
        data = json.load(json_file)
        data.update({answer['Name']:answer})
        with open('results.json', 'w') as outfile:
            json.dump(data, outfile)

        
