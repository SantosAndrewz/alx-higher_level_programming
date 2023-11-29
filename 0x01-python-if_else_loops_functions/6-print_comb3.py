#!/usr/bin/python3
for n in range(10):
    for k in range(n + 1, 10):
        print("{:d}{:d}".format(n, k), end="\n" if n == 8 and k == 9 else ", ")
