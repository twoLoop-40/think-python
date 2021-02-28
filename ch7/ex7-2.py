import math
def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(eval(line))
    
    print('Done!')


if __name__ == '__main__':
    eval_loop()
