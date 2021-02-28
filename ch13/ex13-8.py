
def match_prefix(prefix, t, k):
    '''
    t : list
    from k to len(prefix) 
    Check if prefix match t[k:k + len(prefix)]
    '''
    ln = len(t)
    ln_p = len(prefix)

    if ln < k + ln_p:
        return False
    elif prefix == tuple(t[k:k+ln_p]):
        return True
    else : 
        return False

def make_prefix(t, lp):
    '''
    t : list of words
    lp : length of prefix
    '''
    res = []
    for i in range(len(t)-(lp-1)):
        temp = []
        for j in range(i, i+lp):
            temp.append(t[j])
        if temp:
            temp = tuple(temp)
        
        if temp not in res:
            res.append(temp)
        
    return res

def prefix_dic(t):
    '''
    t : list
    '''
    def output(lnp):
        '''
        lnp : length of prefix
        '''
        prefixes = make_prefix(t, lnp)
        lnt = len(t)
        dic = {}
        for prefix in prefixes:
            items = {}
            for i in range(lnt-lnp):
                if match_prefix(prefix, t, i):
                    items.setdefault(t[i+lnp], 0)
                    items[t[i+lnp]] += 1
            if items:
                dic[prefix] = items

        return dic

    return output




    

        
    



if __name__ == '__main__':
    t = ['lee', 'joon', 'ho', 'is', 'joon', 'ho', 'daddy', 'of', 'hankyum', 'and', 'haneum']
    name = ('joon', 'ho')
    #print(match_prefix(name, t, 2))
    #print(make_prefix(t, 2))

    pre_dic= prefix_dic(t)
    length_of_prefix = 2
    print(pre_dic(length_of_prefix))
    
