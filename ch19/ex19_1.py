binom = {}
def binomial_coeff(n, k):
    return 1 if k == 0 else 0 if n == 0 else binom.setdefault((n, k), binomial_coeff(n-1, k)+ binomial_coeff(n, k-1))

if __name__ == '__main__':
    print(binomial_coeff(4, 2))
