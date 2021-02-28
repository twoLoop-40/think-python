
def has_duplicates(s):
    d = dict()
    for item in s:
        if item not in d:
            d[item] = 1
        else:
            return True
    return False
    
if __name__ == '__main__':
    t = [1, 2, 3, 4, 8, 5, 6]
    print(has_duplicates(t))

