#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count_args = len(argv) - 1

    if count_args == 0:
        print("0 arguments.", end="\n")
    elif count_args == 1:
        print("1 argument:", end="\n")
    else:
        print("{} arguments:".format(count_args), end="\n")
    for i in range(len(argv) - 1):
        print("{}: {}".format(i + 1, argv[i + 1]), end="\n")
