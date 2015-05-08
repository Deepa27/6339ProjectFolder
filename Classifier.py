# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:44:19 2015

@author: Nikita
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import sklearn.metrics as metrics
from sklearn.preprocessing import Imputer
from sklearn.linear_model.stochastic_gradient import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

def evaluate(clf):
   
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    print("The accuracy score for the classifier is: ")
    print(metrics.accuracy_score(y_test, y_pred))
    print("Metrics for classifier is: \n")
    print(metrics.classification_report(y_test, y_pred, target_names= ['good' , 'bad']))
      
df= pd.read_csv("preprocessed.csv")
pca_estimator = PCA(n_components=20)
train = df.values
target = train[:,-1:]
train = train [:,1:-1]

train = pca_estimator.fit_transform(train)
x_train, x_test, y_train, y_test = train_test_split(train, target, test_size=0.20, random_state=0)
std_scale = preprocessing.StandardScaler().fit(x_train)
x_train = std_scale.transform(x_train)
x_test = std_scale.transform(x_test)

#Logistic 
print("\nLogisticRegression classifier\n")
clf = LogisticRegression()
evaluate(clf)

#SVM 
print("\nSVM classifier with linear \n")
clf = svm.SVC(kernel='linear')
evaluate(clf)

#SVM 
print("\nSVM classifierwith rbf  \n")
clf = svm.SVC(kernel='rbf')
evaluate(clf)

#RandomForest Classifier
print("\nRandomForest classifier\n")
clf = RandomForestClassifier()
evaluate(clf)

#ExtraTrees Classifier 
print("\nExtraTrees classifier\n")
clf = ExtraTreesClassifier()
evaluate(clf)

