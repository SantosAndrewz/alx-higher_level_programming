#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum_arg = 0

    for arg in argv[1:]:
        sum_arg = sum_arg + (int(arg))

    print(sum_arg)
