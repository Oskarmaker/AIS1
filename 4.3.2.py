from math import sqrt,log,exp,cos,sin
import matplotlib.pyplot as plt
def f(x):
    return sqrt(1+exp(sqrt(x))+cos(x**2))/abs(1-sin(x)**3)+log(abs(2*x))
l_x=[i for i in range(1,10)]
l_y=[f(l_x[i]) for i in range(9)]
plt.plot(l_x,l_y)
plt.show()
plt.scatter(l_x[:5],l_y[:5])
plt.show()