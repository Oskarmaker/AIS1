from random import random
from matplotlib import pyplot as plt
sp=[random() for i in range(10)]
plt.scatter(sp,[i for i in range(10)])
plt.show()
s=sum(sp)
l=len(sp)
sr=s/l
sp.sort()
if l%2==0:
    sm=(sp[l//2]+sp[l//2+1])/2
else:
    sm=sp[l//2]
print(f'{sr}-среднее значение,{sm}-медианное значение')
