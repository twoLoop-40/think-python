import random

def has_same(s, t):
    for elem in s:
        if elem in t:
            return True
    return False

def has_duplicates(t):
    length = len(t)
    half = int(length/2)
    if length == 1:
        return False
    else:
        former = t[:half]
        latter = t[half:]
        return has_same(former, latter) or has_duplicates(former) or has_duplicates(latter)

def random_arr(n):
    res = []
    while len(res) < n:
        res.append(random.randint(1, 365))

    return res

def same_birthday(n):
    count = 0
    while True:
        r = random_arr(n)
        print(r)
        count += 1
        if has_duplicates(r):
            break
    
    return 1/count



if __name__ == '__main__':
    p = same_birthday(10)
    print('3명 가운데 같은 생일을 가질 확률은? ', p)



