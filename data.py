#'''
#In this project, you will visualize the feelings and language used in a set of
#Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
#need!
#'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt




#Get the JSON data
tweetFile = open("./twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

polarity = []
subjectivity = []

for tweet in tweetData:
    testimonial = TextBlob(tweet["text"])
    polarity.append(testimonial.sentiment.polarity)
print(polarity)
print(subjectivity)

plt.hist(polarity, 10, facecolor = 'blue', alpha=0.5)
plt.show()

plt.hist(subjectivity, 10, facecolor = 'blue', alpha=0.5)
plt.show()
