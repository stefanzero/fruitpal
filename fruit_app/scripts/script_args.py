'''
python manage.py runscript script_args --script-args a b c
'''
from functools import reduce
import re

# def run(*args):
#     print(args)

def add_keywords(a, b):
    matches = re.match(r'(\w)+\s*=\s*(\w)+', b)
    if matches and len(matches.groups()) == 2:
        a[matches.group(1)] = matches.group(2)
    return a

def run(*args):
    # create dictionary from pseudo keyword arguments
    arg_dict = reduce(add_keywords, args, {})
    # print(args)
    print(arg_dict)