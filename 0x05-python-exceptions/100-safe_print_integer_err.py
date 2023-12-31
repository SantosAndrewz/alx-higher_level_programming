#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (TypeError, ValueError) as x:
        print(f"Exception: {x}", file=sys.stderr)
        return False
