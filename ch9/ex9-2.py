
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False

    return True

if __name__ == '__main__':
    fin = open('words.txt')
    count = 0
    count_no_e = 0
    for line in fin:
        count = count + 1
        word = line.strip()
        if has_no_e(word):
            count_no_e = count_no_e + 1
        
    print(count_no_e, count, count_no_e/count)

