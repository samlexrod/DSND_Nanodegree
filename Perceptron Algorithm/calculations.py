x1_coef = 3
x2_coef = 4
b = -10
x, y = (1, 1)
learning_rate = 0.1

x1, x2 = x, y

met_point = True
w1 = x1_coef
w2 = x2_coef

times = 0

while met_point:
    new_w1, new_w2, new_b = w1+x1*learning_rate, w2+x2*learning_rate, b+1*learning_rate
    w1, w2, b = new_w1, new_w2, new_b

    times += 1

    if w1*x1 + w2*x2 + b > 0:
        break

print(times)
