#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    av_list = []
    for x in range(0, list_length):
        try:
            _div = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            _div = 0
        except ZeroDivisionError:
            print("division by 0")
            _div = 0
        except IndexError:
            print("out of range")
            _div = 0
        finally:
            av_list.append(_div)
    return av_list
