fin = open('words.txt')
for line in fin:
    word = line.strip()
    length = len(word)
    if length >= 20:
        print(word)


