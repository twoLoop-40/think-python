import string

punc = string.punctuation
wh_sp = string.whitespace
def get_word(book):
    fp = open(book, encoding='utf-8')
    res = []
    for line in fp:
        word_list = get_word_line(line)
        #print(word_list)
        if word_list != '':
            res += word_list
    return res

def get_word_line(line):
    line = line.strip(punc+wh_sp)
    line_list = line.split(' ')
    res = []
    for word in line_list:
        if word != '':
            res.append(word)
    
    return res


def difference_set(t, b):
    '''
    t : list
    b : book
    '''
    set_book = set(b)
    set_list = set(t)
    return list(set_book - set_list)


if __name__ == '__main__':
    book_name = 'frankenstein.txt'
    book_name2 = 'test.txt'
    word_list = set(get_word(book_name))
    print(len(word_list))

