import json
import statistics
ages = []
may = 0
december = 0
with open('results.json') as json_file:
    data = json.load(json_file)
questions = [['What is your name?','Name'],['What is your date of birth? (MM/DD/YYYY)','Birthday'],['What is your age?','Age'],['Where do you call home? (City, State, Country)','Home'],['How many people live in your home more than 50% of the time?','Family'],['How many hours per week do you spend on the phone?','Phone'],['Name the app, program, or website that you use most frequently.','Program/App']]
for person in data:
    for question in questions:
        print (question[0]+':  '+data[person][question[1]])
        #if question[1] == 'Age' : ages.append(int(data[person][question[1]]))
        #if question[1] == 'Birthday' and data[person][question[1]] [1] == '5' : may+=1
        #if question[1] == 'Birthday' and data[person][question[1]] [0] == '1' and data[person][question[1]] [2] == '1':
            #december+=1
    print ('\n\n')

#print (statistics.mean(ages))
#print (len(data))
#print (may)
#print (december)
