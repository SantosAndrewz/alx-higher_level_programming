#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_elmt = 0
    for c in range(x):
        try:
            print("{}".format(my_list[c]), end=" ")
            count_elmt += 1
        except IndexError:
            break
        print()
        return count_elmt
