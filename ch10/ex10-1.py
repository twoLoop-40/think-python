from __future__ import print_function, division


def type_check(target, given_type):
    type_str = str(type(target))
    return (type_str == "<class '"+given_type+"'>")

def is_type_num(target):
    return type_check(target, 'int') or type_check(target, 'float')

def nested_sum(t):
    if not len(t):
        return 0
    elif is_type_num(t[0]):
        return t[0] + nested_sum(t[1:])
    else :
        return nested_sum(t[0]) + nested_sum(t[1:])



def main():
    t = [[1,2], 3, [4, 5, 6]]
    print(nested_sum(t))



if __name__ == '__main__':
    main()

    




    

