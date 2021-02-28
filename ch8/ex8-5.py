def rotate_word(word, n=0):
    
    def rotate_letter(letter):
        return chr(ord(letter) + n)
    
    newWord=''
    for letter in word:
        newWord = newWord + rotate_letter(letter)
    
    return newWord




if __name__ == '__main__':
    print(rotate_word('LeeJHo', 3))


        

