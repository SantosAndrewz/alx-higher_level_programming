#!/usr/bin/python3
def safe_print_integer(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        print()
        return True
    except (TypeError, ValueError):
        return False
