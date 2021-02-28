def is_safe_letter(word, letter):
    for l in word:
        if l == letter:
            return False
    return True

def avoids(word, str):
    for letter in str:
        if is_safe_letter(word, letter):
            return False
    
    return True

if __name__ == '__main__':
    fin = open('words.txt')
    input_str = input('금지하는 단어(영어)를 입력하세요. \n')
    count = 0
    for line in fin:
        word = line.strip()
        if avoids(word, input_str):
            count = count +1
    
    count = str(count)
    print('금지하는 문자열은 '+input_str+' 이고 이 문자열의 문자가 포함되지 않은 단어의 갯수는 '+count+' 입니다.')






