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
    def get_list(strng):
        res = []
        for s in strng:
            tpl = occur_tuple(s , strng)
            if tpl not in res:
                res.append(tpl)
            strng.pop(s)

        return res
    
    st_list = get_list(st)
    st_list.sort(reverse = True)
    
    for t in st_list:
        print(t)



if __name__ == '__main__':
    most_frequent('leejhodlfjdlksjfeosjlkef')





