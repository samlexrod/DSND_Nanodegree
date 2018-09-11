# Import statements 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Read the data as numpy array.
names = ['feature1', 'feature2', 'label']
df = pd.read_csv('decision trees/data_sklearn_decision.csv', header=None, names=names)
# Assign the features to the variable X, and the labels to the variable y. 

# TODO: Create the decision tree model and assign it to the variable model.
# You won't need to, but if you'd like, play with hyperparameters such
# as max_depth and min_samples_leaf and see what they do to the decision
# boundary.

train_set, test_set = train_test_split(df, test_size = 0.33, random_state=1)

X_train = train_set.iloc[:, :-1]
y_train = train_set.iloc[:, -1]
X_test = train_set.iloc[:, :-1]
y_test = train_set.iloc[:, -1]

d_tree = DecisionTreeClassifier()
model = AdaBoostClassifier(base_estimator=d_tree, n_estimators=4)


# TODO: Fit the model.
model.fit(X_train, y_train)

# TODO: Make predictions. Store them in the variable y_pred.
y_pred = model.predict(X_test)

# TODO: Calculate the accuracy and assign it to the variable acc.
acc = accuracy_score(y_test, y_pred)

print('{:2.2%}'.format(acc))