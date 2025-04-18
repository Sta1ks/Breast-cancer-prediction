import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("breast-cancer-wisconsin.data")
data.replace('?', np.nan, inplace=True)
data.dropna(inplace=True)
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

classifier = LogisticRegression(random_state=0)
print(X_train)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))

"""
[[89  3]
 [ 2 43]]
 To evaluate a model there is 3 type I errors(meaning a person was predicted cancer,
 but in reality he/she doesn't have. And also 2 type II errors(meaning a person was predicted 
 not to have cancer, but in reality he does)), all other 132 observations were predicted correctly.
Accuracy: 96.70 %
Standard Deviation: 2.28 %
"""
