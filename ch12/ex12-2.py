def occur(s, word):
    def recur(word, count):
        if not len(word):
            return count
        elif s == word[0]:
            return recur(word[1:], count+1)
        else :
            return recur(word[1:], count)
    
    return recur(word, 0)

def occur_tuple(s, word):
    return occur(s, word), s

def most_frequent(st):
    def get_list(strn):
        res = []
        for s in strn:
            tpl = occur_tuple(s , strn)
            if tpl not in res:
                res.append(tpl)
        return res
    
    st_list = get_list(st)
    st_list.sort(reverse = True)
    
    return tuple(st_list)

def anagram_list(freq_letter, wordlist):
    res = []
    for word in wordlist:
        if freq_letter == most_frequent(word):
            res.append(word)
            wordlist.pop(word)
        
    return res

def get_anagram_dict(al):
    '''
    al : function may be anagram_list
    '''
    d = dict()
    def change_al(wl):
        freq_key = most_frequent(wl[0])
        if not len(wl):
            return d
        else: 
            d[freq_key] = al(freq_key, wl)
            return change_al(wl)

    return change_al

def print_anagram_dict(wl):
    anagram_dict = get_anagram_dict(anagram_list)
    d = anagram_dict(wl)
    for key in d:
        print(d(key))
    
if __name__ == '__main__':
    print(most_frequent('ldfjdkseiofjlglkdjkflsejlhglsjfhwe'))

