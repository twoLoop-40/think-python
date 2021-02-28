import random
def choose_from_hist(d):
    def replicate_word(word, count):
        res = []
        while count > 0:
            res.append(word)
            count -= 1
        return res
    
    result = []
    for key in d:
        rep = replicate_word(key, d[key])
        result.extend(rep)
    
    #print(result)

    return random.choice(result)

if __name__ == '__main__':
    hist = {'mijin':43, 'hankyum':13, 'joonho':44, 'haneum':9}
    print(choose_from_hist(hist))
