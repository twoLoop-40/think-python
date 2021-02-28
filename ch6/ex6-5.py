import math

def remainder(a, b):
    return a % b

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, remainder(a, b))

if __name__ == '__main__':
    print(remainder(-7, 3))
    print(gcd(174, 42))
    
