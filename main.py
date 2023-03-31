#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    f=1
    for i in range(0, x):
        f=f*(x-i)
    return f
