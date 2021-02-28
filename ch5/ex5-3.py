import math

def max_num(a, b, c):
    if a > b:
        if a > c:
            return a
        else :
            return c
    elif b > c:
        return b
    else :
        return c

def is_triangle(a, b, c):
    max = max_num(a, b, c)
    if a+ b + c > 2 * max:
        return True
    else :
        return False

if __name__ == '__main__':
    first = int(input("첫번째 숫자 입력!\n"))
    second = int(input("두번째 숫자 입력!\n"))
    last = int(input("마지막 숫자 입력!\n"))

    if is_triangle(first, second, last):
        print("\n\n주어진 세개의 숫자로 삼각형 만들 수 있음!")
    else : 
        print("\n\n삼각형 못 만듦 ㅠㅠ")

    






