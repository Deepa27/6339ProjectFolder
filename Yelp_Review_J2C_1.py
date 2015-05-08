# -*- coding: utf-8 -*-

import json
import os
import csv
import string
import re
import nltk
os.chdir('C:\\Users\\nikita\\Documents\\6339Project\\Project')


bus_id2=[]
usr_id=[]
txt_date=[]
txt=[]
typ2=[]
stars=[]

                       
with open('yelp_academic_dataset_review.json','r') as f2:

    f1 = open("output1.csv",'wt', newline='')

    wr = csv.writer(f1, dialect='excel')

    for line2 in f2:
        dict_line2 = json.loads(line2)
        bus_id2.append(dict_line2['business_id'])
        #txt.append(dict_line2['text'].encode('utf-8'))
        text1 = dict_line2['text']
        t=''.join(text1)
        p=string.punctuation
        d=string.digits
        table=str.maketrans(p,' '*len(p))#remove punctuation
        t=t.translate(table)
        table=str.maketrans(d,' '*len(d))#remove digits
        t=t.translate(table)

        #create a list of stop words and stop lists
        codelist=['/r','/n','/t']
        more_stop_words=['cant','didnt','doesnt','dont','goes','isnt','hes',\
        'shes','thats','theres','theyre','wont','youll','youre','youve',\
        're','tv','g','us','en','ve','vg','didn','pg','gp','our','we',
        'll','film','video','name','years','days','one','two','three',\
        'four','five','six','seven','eight','nine','ten','eleven','twelve','http','rt','co','amp']
        stoplist=nltk.corpus.stopwords.words('english')+more_stop_words
        t=t.lower()
        t=re.sub('[^a-zA-Z]',' ',t)#anything that doesnt begin with an alphabet is removed
        for i in codelist:
            stopstring=' '+i+' ' 
            t=re.sub(stopstring,' ',t)#stop words are removed
        for i in stoplist:
            stopstring=' '+i+' '
            t=re.sub(stopstring,' ',t)
        t=re.sub('\s.\s',' ',t)#single letter words removed
        t=re.sub('\s',' ',t)#multiple spaces replaced with single space
        t=t.strip()
        txt.append(t)
        stars.append(dict_line2['stars'])
        txt_date.append(dict_line2['date'])

    rows = zip(bus_id2,txt,stars,txt_date)
    
    for row  in rows:
        wr.writerow(row)
         
    f1.close()          
f2.close()        


