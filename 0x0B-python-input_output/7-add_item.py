#!/usr/bin/python3
'''
Module adds all arguments to a Python list, and then save them to a file.
'''

import os
import sys



save_jsn = __import__('5-save_to_json_file').save_to_json_file
load_jsn = __import__('6-load_from_json_file').load_from_json_file


fn = 'add_item.json'


if os.path.exists(fn):
    list_loaded = load_jsn(fn)
else:
    list_loaded = []

list_loaded.extend(sys.argv[1:])
save_jsn(list_loaded, fn)
