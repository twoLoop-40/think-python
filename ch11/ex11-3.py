known = {}


def ack_memo(m, n):
    if m == 0:
        return n + 1
    elif (m, n) in known:
        return  known[(m, n)]
    elif n == 0:
        known[(m, n)] = ack_memo(m-1,1)
        return known[(m, n)]
        
    else :
        known[(m, n)] = ack_memo(m-1, ack_memo(m, n-1))
        return known[(m, n)]

if __name__ == '__main__':
    print(ack_memo(4, 1))
    print(len(known))



        
