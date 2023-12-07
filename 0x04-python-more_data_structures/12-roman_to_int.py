#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    for character in roman_string:
        if char not in roman_dict:
            return 0

    num = [roman_dict[x] for x in roman_string] + [0]
    conv = 0
    for y in range(len(num)-1):
        if num[y] >= num[y+1]:
            conv = conv + num[y]
        else:
            conv = conv - num[y]
    if 1 <= conv <= 3999:
        return conv
    else:
        return 0
