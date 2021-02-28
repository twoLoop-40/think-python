import math 
def mysqrt(a):
    epsilon = 0.0000001
    x = 1.0
    while True:
        y = (x + a/x) /2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def str_toTheLength(a, n):
    str_len = len(a)
    if str_len > n:
        return a[:n]
    else :
        return a + ' '*(n-str_len + 1)


def form(s1, s2, s3, s4):
    return str_toTheLength(str(s1), 4) + str_toTheLength(str(s2), 18) + str_toTheLength(str(s3), 18)+ str(s4)

def test_square_root(s, e):
    firstLine = str_toTheLength('a', 4) + str_toTheLength('mysqrt(a)', 17)+str_toTheLength('math.sqrt(a)', 17) + 'diff'
    print(firstLine)
    print(form('-', '-'*16, '-'*16, '-'*16))
    num = s
    while num <= e:
        print(form(num, mysqrt(num), math.sqrt(num), abs(math.sqrt(num)-mysqrt(num))))
        num = num + 1

    
if __name__ == '__main__':
    test_square_root(1, 15)

    





