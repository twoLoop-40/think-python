def check_twin(word, times, start):
    length = len(word)
    if times == 0:
        return True
    elif length <= 1:
        return False
    elif word[0] == word[1]:
        return check_twin(word[2:], times-1, start)
    else :
        return check_twin(word[1:], start, start)
    
if __name__ == '__main__':
    print(check_twin('lmmooee',3, 3))
    print(check_twin('committee',3, 3))

    