def file_to_obj(name):
    return open(name)

fname = 'words.txt'

def word_to_sum(word):
    sum = 0
    for  s in word:
        sum += ord(s)

    return sum

def store_key(fo):
    d = dict()
    for line in fo:
        wd = line.strip()
        ws = word_to_sum(wd)
        if wd not in d:
            d[wd] = ws
        
    return d

if __name__ =='__main__':
    fobj = file_to_obj(fname)
    dic = store_key(fobj)
    for k in dic:
        print(k, dic[k])

    


