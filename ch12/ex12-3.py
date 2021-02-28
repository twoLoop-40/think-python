def len_check(w1, w2):
    return len(w1) == len(w2)

def list_maker(checker):
    
    def same_len(w1, wlist):
        res = []
        for item in wlist:
            if checker(w1, item) and item not in res:
                res.append(item)
        return res

    return same_len

def change_to_num(w):
    res = []
    for s in w:
        res.append(ord(s))

    return res

def remove_letter(s, alist):
    res =[]
    for item in alist:
        if s != item:
            res.append(item)
    
    return res

def make_exchanger(ctn, rl):
    def is_transformable(w1, w2):
        w1_num_list = change_to_num(w1)
        w2_num_list = change_to_num(w2)
        res = []
        for i in range(len(w1)):
            res.append(w1_num_list[i] - w2_num_list[i])

        Rem = 0
        print(res)
        new_res = remove_letter(Rem, res)
        print(new_res)
        print(sum(new_res))
        
        if len(new_res) != 2:
            return False
        elif sum(new_res):
            return False
        else:
            return True

    return is_transformable

def two_letter_change(w1, w2):
    transformed = make_exchanger(change_to_num, remove_letter)
    if len_check(w1, w2):
        return transformed(w1, w2)
    else:
        raise('주어진 글자의 길이가 다름!')



def same_len_list(w, wlist):
    return list_maker(len_check)(w, wlist)

def del_item(item, t):
    if item not in t:
        return t
    else:
        t.remove(item)
        return del_item(item, t)


def transformable_list(t):
    def recurse(accum):
        first_elem = t[0]
        candidate = same_len_list(first_elem, t[1:])
        res = []
        for word in candidate:
            if two_letter_change(first_elem, word):
                res.append(word)
        if res:
            res.append(first_elem)
            for item in res:
                del_item(item, t)
    
        if not t:
            return accum.append(res)
        else:
            return recurse(accum)

    return recurse([])

if __name__ == '__main__':
    print(two_letter_change('leejho', 'eeljho'))
    t = [1, 2, 3, 3, 2, 1, 1, 1, 1]
    print(t)
    del_item(1, t)
    print(t)



