def flie_to_obj(name):
    return open(name)



def word_to_list_1(fo):
    res = []
    for line in fo:
        word = line.strip()
        res.append(word)
    
    return res

def word_to_list_2(fo):
    res = []
    for line in fo:
        word = line.strip()
        res = res + [word]
    
    return res

    
