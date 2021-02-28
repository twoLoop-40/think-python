def does_rotate(w1, w2):
    if len(w1) != len(w2):
        return False
    else :
        offset = ord(w2[0]) - ord(w1[0])
        for k in range(len(w1)):
            if ord(w2[k]) - ord(w1[k]) != offset:
                return False
        return True

def rotate_num(w1, w2):
    return ord(w2[0])- ord(w1[0])

def rotate_pair(word, t):
    d = dict()
    for wd in t:
        if does_rotate(word, wd):
            d.setdefault(wd, rotate_num(word, wd))
    
    return d




    

    
    