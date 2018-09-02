# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression
import os


# Assign the dataframe to this variable.
# TODO: Load the data
data = pd.read_csv(os.listdir()[3]+'\\bmi_and_life_expectancy.csv', sep=',')

split_columns = data.columns[0].replace(' ', '_').split(',')

data = data[data.columns[0]].str.rsplit(',', 2, expand=True)

data.columns = split_columns

bmi_life_data = data

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()

print(data.head())

x_values = bmi_life_data.iloc[:, 2].values.reshape(-1, 1)
y_values = bmi_life_data.iloc[:, 1].values.reshape(-1, 1)

print(x_values.shape)
print(y_values.shape)

bmi_life_model.fit(x_values, y_values)

# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
bmi = 21.07931
laos_life_exp = bmi_life_model.predict(bmi)

print("A person with a BMI of {bmi} has a predicted life expectancy of {life:.2f} years".\
    format(bmi=bmi, life=laos_life_exp[0][0]))