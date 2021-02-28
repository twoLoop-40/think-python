
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else :
        return is_palindrome(middle(word))


if __name__ == '__main__':
    print(first('이준호'))
    print(last('이준호'))
    print(middle('이준호김미진'))
    if is_palindrome('이준이'):
        print('성공')
    else : 
        print('실패')




