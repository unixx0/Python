#passing function inside a function

def square(x):
    return x*x


def cube(fx, x):
    return(fx(x)*x)


a=5
b= cube(square, a)
print(b)