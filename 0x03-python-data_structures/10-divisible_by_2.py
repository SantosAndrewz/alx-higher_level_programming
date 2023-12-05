#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_list = []

    for x in my_list:
        divisible_list.append(x % 2 == 0)
    return divisible_list
