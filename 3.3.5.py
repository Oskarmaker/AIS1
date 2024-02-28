x=[0,1,2,3,4,5,6,7,8]
l=(len(x)-1)//2
for i in range(l):
    el=x[i]
    if el%2==0:
        elz=x[i]
        x[i]=x[2*l-i]
        x[2*l-i]=elz
print(x)