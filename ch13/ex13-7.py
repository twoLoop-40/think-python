import random

def in_bisect(sl, val):
    length = len(sl)
    half = int((length-1)/2 ) 
    if length == 1:
        return 0
    elif sl[half] == val:
        return half
    elif sl[half] > val:
        return in_bisect(sl[:half+1], val)
    else:
        return (half+1) + in_bisect(sl[half+1:], val)

def word_histo(t):
    d = {}
    for word in t:
        d.setdefault(word, 0)
        d[word] += 1
    
    return d
    
def cum_sum(dic):
    '''
    dic : dictionary
    '''
    key_list = list(dic.keys())
    first = dic[key_list[0]]
    res = [first]
    key_len = len(key_list)
    for i in range(1, key_len):
        pre = res[i-1]
        now = dic[key_list[i]]
        res.append(pre+now)

    return res

def rand_choice(dic):
    accum = cum_sum(dic)
    total = accum[len(accum)-1]
    rand_num = random.randint(1, total)
    print(rand_num)
    idx = in_bisect(accum, rand_num) 
    print(idx)
    words = list(dic.keys())
    return words[idx]


if __name__ == '__main__':
    test_dic = {'a': 2, 'b': 3, 'lee': 4, 'hwang': 2}
    print(cum_sum(test_dic))
    print(rand_choice(test_dic))
