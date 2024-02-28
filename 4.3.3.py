from numpy import trapz,cos,abs,exp,log
from scipy.integrate import simps
import matplotlib.pyplot as plt
def f(x):
    return abs(cos(x*exp(cos(x)+log(x+1))))
x=[]
y=[]
for i in range(1,10):
        x.append(i)
        y.append(f(i))
print(trapz(y))
plt.grid()
plt.plot(x,y,c='r')
plt.fill_between(x,y)
plt.show()
