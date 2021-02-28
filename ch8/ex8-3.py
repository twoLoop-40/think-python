def reverse_str(word):
    return word[::-1]

def is_palindrome(word):
    return word == word[::-1]


if __name__ == '__main__':
    print(reverse_str('leehankyum'))
    print(is_palindrome('hello'))

