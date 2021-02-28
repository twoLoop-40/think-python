
def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False

def is_power(a, b):
    if abs(a) == abs(b):
        return True
    elif not is_divisible(a, b):
        return False
    else :
        return is_power(a/b , b)



if __name__ == '__main__':
    if is_divisible(6, 2):
        print('성공')
    else : 
        print('실패')
    
    if is_power(8, 2):
        print('거듭제곱!')
    else:
        print('거듭제곱 아님!')
