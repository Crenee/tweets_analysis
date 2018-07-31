

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data #path to our file
tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


for tweet in tweetData:
    #print(tweet["text"])
    blob = TextBlob(tweet["text"])
    print(blob.polarity)










tb = TextBlob("")
print(tb.polarity)
