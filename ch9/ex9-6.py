def ascends_two(former, latter):
    former_lower = former.lower()
    latter_lower = latter.lower()

    if former_lower <= latter_lower:
        return True
    else:
        return False

def is_abecedarian(word):
    length = len(word) -1 
    for i in range(length):
        if not ascends_two(word[i], word[i+1]):
            return False

    return True


