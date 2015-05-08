
corpus =[]
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
csv.field_size_limit(2147483647)
with open("output1.csv") as f:
    reader = csv.reader(f)
    values = [(line[1]) for line in reader]
#df = pd.read_csv("output1.csv")
#saved_column = df.Text
#for text in range(saved_column):
review = "".join([thing for thing in values])
corpus.append(review)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus) #docs is your list of parsed text for each of the documents
#
## Fit the NMF model
#
nmf = NMF(n_components=10, random_state=1).fit(tfidf) #n_topics is the number of topics to be extracted
feature_names = vectorizer.get_feature_names()
##display topic# and words associated with each
for topic_idx, topic in enumerate(nmf.components_):
   print("Topic #%d:" % topic_idx)
   print(" ".join([feature_names[i]
                   for i in topic.argsort()[:-25 - 1:-1]])) #n_top_words is the number of words you need for each topic; you must set this earlier in your code
   print()
