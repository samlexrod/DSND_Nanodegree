# TODO: Add import statements
from sklearn.linear_model import Lasso, LinearRegression
import pandas as pd 

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('Linear Regression/data_regularization.csv', header=None)
print(train_data.head())
print(train_data.shape[1])

X = train_data.iloc[:, :-1]
y = train_data.iloc[:, -1]

print(X.head())
print(y.head())

# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso()

# TODO: Fit the model.
lasso_reg.fit(X, y)


# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)