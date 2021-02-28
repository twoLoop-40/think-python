def is_interlockable(w1, w2):
    len_w1 = len(w1)
    len_w2 = len(w2)

    return abs(len_w1 - len_w2) <= 1

def interlock_pair(wlist):
    def accum(res):
        if len(wlist) <= 1:
            return res
        else:
            pvt = wlist.pop(0)
            for word in wlist:
                if is_interlockable(pvt, word):
                    res.append([pvt, word])
                    wlist.remove(word)
                    break
            return accum(res)
    
    return accum([])

    