#!/usr/bin/python3
def uppercase(str):
    ucase_str = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            ucase_c = chr(ord(c) - 32)
            ucase_str = ucase_str + ucase_c
        else:
            ucase_str = ucase_str + c
    print("{}".format(ucase_str))
