import pandas as pd
from sklearn import preprocessing, model_selection, neighbors
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

X=[]
y=[]


df = pd.read_pickle('./data.pickle')

features = {}
index = 0
for k,v in df.items():
    features[k] = v.flatten()
    X.append(v.flatten())
    y.append(k)

X = np.array(X)
y = np.array()

print(X)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.3)
# print(X_train)
# print(y_train)
# print(X_test)
# print(y_test)

clf =  KNeighborsClassifier()

clf.fit(X_train,y_train)

accuracy = clf.score(X_test,y_test)
print(accuracy)
