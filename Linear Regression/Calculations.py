


# *********************************************
# Absolute Trick
p = 0
q = 0
a = 0
slope = 0
intercept = 0

# w_1 
# (p, q) = (x, y)

print('Absolute Trick:')
new_slope = round(slope - p*a, 2)
print(new_slope)

# w_2
new_intercept = round(intercept - a, 2)
print(new_intercept)

# equation
print('y = {slope}x + {intercept}'.format(slope=new_slope, intercept=new_intercept), '\n')

#************************************************
# Square Trick
p = 0
q = 0
a = 0
slope = 0
intercept = 0

#w_1
print('Square Trick:')
# solving for y or q_prime
q_prime = slope*p + intercept

q_qprime = q - q_prime
print('y =', q_prime, '; q - q_prime = ', q_qprime)

new_slope = round(slope + p*(q-q_prime)*a , 2)
print(new_slope)

#w_2
new_intercept = round(intercept + (q_qprime)*a, 2)
print(new_intercept)

# equation
print('y = {slope}x + {intercept}'.format(slope=new_slope, intercept=new_intercept))
"""
# ****************************************************
# REGRESSION MEASURES
# ******************************************************

# Mean Absolute Deviations (Error)
import numpy as np

x_points, y_points = zip((2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14))

predictions = [(1.2 * x + 2) for x in x_points]

print(predictions)

np_errors = abs(np.array(y_points) - np.array(predictions))

MAD = np_errors.sum() / len(np_errors)

print(MAD) # Awesome Sauce!


# Mean Square Deviations (Errors)
np_sq_errors = (np.array(y_points) - np.array(predictions))**2

SDM = np_sq_errors.sum() / (2 * len(np_sq_errors))

print(SDM) # Awesome Sauce!
"""


