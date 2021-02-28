def sub_list(t, k):
    '''
    t : list
    k : number where to cut
    '''
    return t[:k]

def cum_sum(t):
    result = []
    for i in range(1,len(t)+1):
        result.append(sum(sub_list(t, i)))
    
    return result



if __name__ =='__main__':
    t = [1, 2, 3, 4, 5]
    print(cum_sum(t))

    
