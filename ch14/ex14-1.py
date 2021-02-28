def file_IO(func, file_in, file_out):
    fin = open(file_in, 'r')
    fout = open(file_out, 'w')

    for line in fin:
        fout.wrtie(func(line))

    fin.close()
    fout.close()

def line_op(line):
    def replace_line(pattern, replace):
        new_line = line.replace(pattern, replace)
        return new_line

    return replace_line

    




    




