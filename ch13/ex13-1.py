import string
import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)

## from ch 11
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, [])
        inverse[val].append(key)

    return inverse

punc = string.punctuation
wh_space = string.whitespace

def break_line(line):
    return line.split(' ')

def clean_up(word):
    new_word =word.strip(punc+wh_space)
    new_word = new_word.lower()
    return new_word

def make_organizer(line_f, word_f):
    def f(line):
        line_list = line_f(line)
        res = []
        for word in line_list:
            if word_f(word):
                res.append(word_f(word))
        
        return res
    
    return f

def make_file_organizer(org):
    def f(file_name):
        file_obj = open(file_name, encoding='utf-8')
        res = []
        for line in file_obj:
            if org(line):
                res.append(org(line))

        return res
    
    return f


def word_line(line):
    line_func = make_organizer(break_line, clean_up)
    return line_func(line)

def word_file(file_name):
    file_func = make_file_organizer(word_line)
    return file_func(file_name)
 
        

def count_word(t):
    '''
    recursion version
    But too many recursion makes it not work
    
    def recurse(t, res):
        if not t:
            return res
        elif isinstance(t[0], str):
            res.setdefault(t[0], 0)
            res[t[0]] += 1
            return recurse(t[1:], res)
        elif isinstance(t[0], list):
            res = recurse(t[0], res)
            return recurse(t[1:], res)
        else:
            raise("No more type to consider!")

    return recurse(t, {})
    '''
    
    
    ext_list = []
    for item in t:
        ext_list.extend(item)

    #print(ext_list)
    res = {}
    for word in ext_list:
        res.setdefault(word, 0)
        res[word] += 1
        #print(res)
    
    return res

def largest_n(dic, k):

    def max_word_list(d):
        '''
        d : dictionary
        '''
        key_list = list(d.keys())
        max_key = max(key_list)
        return max_key, d[max_key]

    def takeout_from(d, key):
        while True:
            if key in d:
                del d[key]
            else :
                break
        return d
    
    def recurse(inverted_dic, n, res):

        if not inverted_dic:
            return res
        elif not n:
            return res
        else:
            max_word = max_word_list(inverted_dic)
            inverted_dic = takeout_from(inverted_dic, max_word[0])
            res.append(max_word)
            return recurse(inverted_dic, n-1, res)

    return recurse(invert_dict(dic), k, [])



if __name__ == '__main__':
    text_name1 = 'frankenstein.txt'
    text_name2 = 'test.txt'
    #print(word_file(text_name2))
    word_list = word_file(text_name1)
    #print(word_list)
    result = count_word(word_list)
    count = 20
    print(largest_n(result, count))
