from math import e


class sigmoid:

    def __init__(self, x):
        self.x = x
        self.results = 1/(1 + e**-x)
        print(self.results)


x1 = -4
x2 = 5

x = 4*x1 + 5*x2 - 9
sigmoid(x).results

print(e)
