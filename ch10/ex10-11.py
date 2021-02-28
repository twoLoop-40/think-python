def is_reverse(w1, w2):
    return w1 == w2[::-1]

def reverse_pair(wlist):
    def accum(res):
        if len(wlist) <= 1:
            return res
        else:
            pvt = wlist.pop(0)
            for word in wlist:
                if is_reverse(pvt, word):
                    res.append([pvt, word])
                    wlist.remove(word)
                    break
            return accum(res)
    
    return accum([])





if __name__ == '__main__':
    print(is_reverse('이준', '준이'))
    alist = ['ley', 'ljh', 'loo', 'yel', 'jhh', 'ool']
    print(reverse_pair(alist))

