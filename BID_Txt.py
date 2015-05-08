import csv
import os 
from itertools import groupby
file = open("AFINN-111.txt","r")
affy_file = file.readlines()
sentiscore_dict = {}
for line in affy_file:
    newWord = line.replace("\n", "");
    split_line = newWord.split("\t")
    sentiscore_dict[split_line[0]] = (split_line[1])
file.close()


writer = csv.writer(open('output1.csv', 'wt'))
writer.writerow(["Business_ID", "Text","Score"])

with open('review3.csv', 'rt') as f:
    reader = csv.reader(f)
     
    for key, group in groupby(reader, lambda x: x[0]):
        review = " ".join([thing[1] for thing in group])
        words = review.split()
        senti_score = 0
        for word in words:
            if word in sentiscore_dict.keys():
                value = int(sentiscore_dict[word])
                senti_score = senti_score + value
            else:
                senti_score += 0
        
        
        writer.writerow([key,review,senti_score])
f.close()

        
      

