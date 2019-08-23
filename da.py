'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
from wordcloud import WordCloud
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

#store each tweet's polarity and subectivity in the list
#create a list called polarity and subjectivity
polarity = []
subjectivity = []
all=[]

for tweet in tweetData:
    all.append(tweet["text"])
    temp = TextBlob(tweet["text"])
    polarity.append(temp.sentiment.polarity)
    subjectivity.append(temp.sentiment.subjectivity)

print(polarity)
print(subjectivity)
print(" Polarity Average:", sum(polarity)/len(polarity))
print(" Subjectivity Average:", sum(subjectivity)/len(subjectivity))
print("".join(all))





 #Set a clean upper y-axis limit
plt.hist(polarity, 5)
plt.title('Polarity')
plt.xlabel('the polarity')
plt.ylabel('the # of tweets')
plt.show()
plt.hist(subjectivity, 5)
plt.xlabel('the Subjectivity')
plt.ylabel('the # of tweeets')
plt.title('Subjectivity')
plt.show()

""
