#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = []
    for key, value in a_dictionary.items():
        dict_keys.append(key)
    dict_keys = sorted(dict_keys)
    for key in dict_keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
