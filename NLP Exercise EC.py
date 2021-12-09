import matplotlib.pyplot as plt
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Word
from textblob import TextBlob
from pathlib import Path
import numpy as np

comments = []
f = open('comments.txt','r')
text = f.readlines()
for i in text:
    i = i.replace('\r\n','')
    i = i.replace('"',"")
    comments.append(i)

positive = 0
negative = 0

for i in comments:
    blob = TextBlob(i, analyzer = NaiveBayesAnalyzer())
    if (blob.sentiment.classification == 'pos'):
        positive += 1
    if (blob.sentiment.classification == 'neg'):
        negative += 1

print("The number of positive comments is",positive, "The number of negative comments is", negative)

color = ['red', 'black']
x = [1,2]
y = [positive, negative]
x_label = ['positive comments', 'negative comments']
plt.xticks(x, x_label) 
plt.bar(x ,y,  width = [0.5,0.5],color = color)
for a,b,i in zip(x,y, range(len(x))):
    plt.text(a,b+0.01,y[i],ha = 'center',fontsize = 15)
plt.show()
