from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import os

print(os.getcwd())

data = np.asarray(pd.read_csv('Support Vector Machines/dataset/svm_data.csv', header=None))

X = data[:, :-1]
y = data[:, -1]

model = SVC(gamma = 50)

print(model)

"""
C: The C parameter.
When C is large, you are forcing your boundary to have fewer errors than when it is a small value.
kernel: The kernel. The most common ones are 'linear', 'poly', and 'rbf'.
By far the most popular kernel is the rbf kernel.
The rbf kernel allows you the opportunity to classify points that seem hard to separate in any space. 
degree: If the kernel is polynomial, this is the maximum degree of the monomials in the kernel.
gamma : If the kernel is rbf, this is the gamma parameter.
When gamma is large, the outcome is similar to having a large value of C, that is your algorithm will 
attempt to classify every point correctly. Alternatively, small values of gamma will try to cluster in a 
more general way that will make more mistakes, but may perform better when it sees new data.
"""

model.fit(X, y)

y_pred = model.predict(X)

acc = accuracy_score(y_pred, y)

print('{:2.2%}'.format(acc))