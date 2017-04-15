a = list(range(10))


def changeLst(a):
    a[::] = list(range(10, 20))  # initialized a new list
    # old a is shadowed because new a initialized


if __name__ == '__main__':
    print a
    changeLst(a)  # new a shadowed old a
    # new a out of scope, old a back in scope again
    # print b is a # different list
    print a
