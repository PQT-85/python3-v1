import math
x = input('enter your number: ')
y = math.factorial(int(x))
print(f'factorial of {x} is {y}',)


x=int(input('Enter your number: '))
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)
print(fact(x))