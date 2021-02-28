import do_twice from ex2.py
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