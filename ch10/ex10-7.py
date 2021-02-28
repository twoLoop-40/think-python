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


if __name__ == '__main__':
    s = [1, 2]
    t = [3, 4, 5]
    print(has_same(s, t))
    r = [1, 2, 3, 4, 8, 6, 7]
    print(has_duplicates(r))

    
