PI = 3.141592653589793


def factorial(x):
    if (x <= 1):
        return 1
    else:
        return x * factorial(x - 1)


def caps(a, b):
    result = 1
    for x in range(b):
        result *= a
    return result


def radian(deg):
    return deg * PI / 180


# Taylor algorithms :

def sin(deg, accuracy):
    result = 0
    for n in range(accuracy):
        term = (caps(-1, n)*caps(deg, 2*n+1))/factorial(2*n+1)
        result += term
    return result


a = 30
a = radian(a)
a = sin(a, 10)
print(a)
