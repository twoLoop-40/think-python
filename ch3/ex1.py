def right_justify(str):
    str_len = len(str)
    blank_num = 70 - str_len
    blank = ' ' * blank_num
    print(blank + str)


def draw_line(arg1, arg2):
    arg2_5 = arg2 * 5
    print(arg1 + arg2_5 + arg1 + arg2_5 + arg1)

def draw_window():
    draw_line('+', '-')
    draw_line(' ', ' ')
    do_twice(draw_line, '|', ' ')
    draw_line(' ', ' ')
    do_twice(draw_line, '|', ' ')
    draw_line(' ', ' ')
    do_twice(draw_line, '|', ' ')
    draw_line(' ', ' ')
    do_twice(draw_line, '|', ' ')
    draw_line(' ', ' ')
    draw_line('+', '-')




    



