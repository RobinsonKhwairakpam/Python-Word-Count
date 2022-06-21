from stopwords import stopWords              #function from another file
import re                                  #regular expression

regex = re.compile('[^a-zA-Z]')
with open("textfile.txt",'r') as f:
        words = (f.read().lower().split())
           
d = dict()

for word in words:
    word = re.sub(regex,'',word)     #replace with blank
    if not stopWords(word):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

d = sorted(d.items(), key=lambda x: x[1], reverse = True)  #sort in descending order of values
   
for i in range(3):    
    print(d[i][0],d[i][1])