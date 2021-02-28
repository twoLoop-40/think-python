def flie_to_obj(name):
    return open(name)

def word_to_list_1(fo):
    res = []
    for line in fo:
        word = line.strip()
        res.append(word)
    
    return res

def in_bisect(sl, val):
    length = len(sl)
    half = int(length/2)
    if sl[half] == val:
        return half
    elif sl[half] > val:
        return in_bisect(sl[:half], val)
    else:
        return half + in_bisect(sl[half:], val)

if __name__ == '__main__':
    st = 'abloom'
    fin = flie_to_obj('words.txt')
    word_list = word_to_list_1(fin)
    print(in_bisect(word_list, st))

    