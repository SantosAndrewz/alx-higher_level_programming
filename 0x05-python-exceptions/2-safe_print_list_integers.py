#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_int = 0
    try:
        for c in range(x):
            try:
                if isinstance(my_list[c], int):
                    print("{:d}".format(my_list[c]), end="")
                    count_int += 1
            except IndexError:
                break
        print()
    except TypeError:
        pass
    return count_int
