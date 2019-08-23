import json

#open json file
tweetfile = open("./twitter.json", "r")

#get data from the opened file
tweetdata = json.load(tweetfile)

#close the file we already have the data stored
tweetfile.close()

print("Tweet id: ", tweetdata[0]["id"])
print("Tweet text: ", tweetdata[0]["text"])

for idx in range(len(tweetdata)):
    print("Tweet id:", tweetdata[idx]["id"])
for tweet in tweetdata:
    print("Tweet text: ", tweet["text"])
