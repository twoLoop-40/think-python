import math

'''
my factorial doesn't work

def factorial(n):
    def iter(result, num):
        if num == n:
            return result * num
        else:
            return iter(result *num, num + 1 )
    return iter(1, 1)
'''
def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def piEachTerm(k):
    numer = factorial(4*k)*(1103 + 26390*k)
    denom = ((factorial(k))**4)*396**(4*k)
    return numer/denom

def estimate_pi():
    coeffi = 2*math.sqrt(2)/9801
    sum = 0
    k = 0
    while piEachTerm(k) >= 1e-15:
        sum = sum + piEachTerm(k)
        k = k + 1
    
    return 1/(coeffi*sum)

        
if __name__ == '__main__':
    print(factorial(5))
    print(estimate_pi())


