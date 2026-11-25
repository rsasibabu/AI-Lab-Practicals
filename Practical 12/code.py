from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
print(type(iris))
print(iris.keys())
iris.data
iris.target
iris.target_names

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=123
)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)
y_pred
y_test
knn.score(x_test, y_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

y_pred_train = knn.predict(x_train)
print(confusion_matrix(y_train, y_pred_train))
print(classification_report(y_train, y_pred_train))
