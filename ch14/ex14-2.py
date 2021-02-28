from anagram_sets import all_anagrams, signature
import dbm


def store_anagram(filename):
    db = dbm.open('shelf', 'c')
    anagram_dic = all_anagrams(filename)
    for word in anagram_dic:
        db[word] = anagram_dic[word]

    db.close()

def read_anagram(word):
    db = dbm.open('shelf')
    sig = signature(word)
    try :
        return db[sig]
    except :
        return []
    



