def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, [])
        inverse[val].append(key)

    return inverse

if __name__ =='__main__':
    hist = {
        'a': 1, 'p': 1, 'r': 2, 't': 1, 'o':1
        }
    inverse = invert_dict(hist)
    print(inverse)
