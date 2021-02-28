def chop(t):
    del t[0]
    del t[-1]
    return 

if __name__ == '__main__':
    t = [1, 2, 3, 5, 4]
    chop(t)
    print(t)
    