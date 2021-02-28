def is_anagram(s, t):
    return sorted(s) == sorted(s)

if __name__ == '__main__':
    s = 'LeeJHo'
    t = 'JHoeeL'
    print(is_anagram(s, t))
