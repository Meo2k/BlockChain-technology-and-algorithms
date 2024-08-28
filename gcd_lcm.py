def gcd(a, b):
    while b != 0:
        a, b = b, (a % b)
    return a


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


a = int(input('Input a: '))
b = int(input('Input b: '))
print(f'GCD({a}, {b}): {gcd(a, b)}')
print(f'LCM({a}, {b}): {lcm(a, b)}')
