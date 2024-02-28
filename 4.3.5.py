from numpy import exp,sin,cos
def summation(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def division(x,y):
    return x/y
def multiplication(x,y):
    return x*y
def exponent(x,y):
    return exp(x+y)
def sine(x,y):
    return sin(x+y)
def cosine(x,y):
    return cos(x+y)
def exponentiation(x,y):
    return x**y
print('Все возможные операции: "+","-","/","*","e^(x+y)","sin","cos","x^y"')
x=float(input())
operation=input()
y=float(input())
if operation=='+':
    print(summation(x,y))
elif operation=='-':
    print(subtraction(x,y))
elif operation=='/':
    print(division(x,y))
elif operation=='*':
    print(multiplication(x,y))
elif operation=='e^(x+y)':
    print(exponent(x,y))
elif operation=='sin':
    print(sine(x,y))
elif operation=='cos':
    print(cosine(x,y))
elif operation=='x^y':
    print(exponentiation(x,y))
else:
    print('Ошибка. Неверно введена операция. Все возможные операции: ("+","-","/","*","e^(x+y)","sin","cos","x^y")')