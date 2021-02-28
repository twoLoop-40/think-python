def reverse(word):
    return word[::-1]

def is_reverse(fo, la):
    if reverse(fo) == la:
        return True
    else:
        return False

def is_reverse_digit(n1, n2):
    if n1 < 100:
        n1_str = str(n1).zfill(2)
        n2_str = str(n2).zfill(2)
    else :
        n1_str = str(n1).zfill(3)
        n2_str = str(n2).zfill(3)
    
    return is_reverse(n1_str, n2_str)

def age_rev(mom, standard_cnt):
    
    def recurse(mom, son, count):
        if mom > 200:
            return False
        elif is_reverse_digit(mom, son):
            count = count + 1
            if count == standard_cnt:
                print(mom)
                return son
            else: 
                return recurse(mom+1, son+1, count)
        else :
            return recurse(mom+1, son+1, count)

    return recurse(mom, 1, 0)

    

def get_rev_age(start):
    for mom in range(start, 200):
        if age_rev(mom, 8):
            return age_rev(mom, 6)

  
if __name__ == '__main__':
    print(get_rev_age(19))

    
    

        
    

        





