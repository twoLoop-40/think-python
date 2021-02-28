import math
wrong_formula = '공식이 틀렸네요'
wrong_fermat = '페르마 선생님이 실수하신 겁니다. ^^'
def check_input(a, b, c):
    if a < 0 or b < 0 or c < 0 :
        return False
    else:
        return True

def check_fermat(a, b, c):
    def check_iter(n):
        if (a ** n) + (b ** n) < (c ** n):
            print(wrong_formula)
            return
        elif (a ** n) + (b ** n) == (c ** n):
            print(wrong_fermat)
            return 
        else :
            check_iter(n+1)
    
    check_iter(3)


if __name__ == '__main__':
    if check_input(3, 4, 5):
        check_fermat(3, 4, 5)
    else : 
        print("잘못된 입력입니다.")






    