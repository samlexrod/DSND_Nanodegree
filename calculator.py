


total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00

# Update total_price here
# two lines
total_price += nice_sweater
total_price += fun_books

# one line
total_price_oneline = 0
total_price_oneline += (nice_sweater + fun_books + new_sneakers)

# numpy
import numpy as np
np_total_price = np.array([new_sneakers, 
                           nice_sweater, 
                           fun_books]).sum()


print('The total price is ${:2.2f}'.format(total_price))
print('The total price is ${:2.2f}'.format(total_price_oneline))
print('The total price is ${:2.2f}'.format(np_total_price))