def is_palindrome(word):
    return word == word[::-1]

def check_palindrome(digits, start, end):
    word = str(digits)
    subword = word[start-1:end]
    return is_palindrome(subword)

def test_palindrome_four(digits):
    if check_palindrome(digits, 3, 6) and check_palindrome(digits+1, 2, 6) and check_palindrome(digits+2, 2, 5) and check_palindrome(digits+3, 1, 6):
        return digits
    else :
        return '0'

if __name__ == '__main__':
    start = 100000
    end = 1000000-4
    
    for i in range(start, end):
        if test_palindrome_four(i) != '0':
            print(test_palindrome_four(i))
            
    
    


