import os

def check_ext(filename, ext):
    flist = filename.sep('.')
    if flist[1] == ext:
        return True
    else:
        return False

def getname_ext(dname, ext):
    def recurse(name, res):
        dlist = os.listdir(name)
        for item in dlist:
            if os.path.isfile(item):
                if check_ext(item, ext):
                    res.append(os.path.abspath(item))
            elif os.path.isdir(item):
                recurse(item, res)

        return res

    recurse(dname, [])

            



  