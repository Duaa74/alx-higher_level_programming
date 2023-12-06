#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    n1 = sorted(a_dictionary.keys())
    for key in n1:
        print("{}: {}".format(key, a_dictionary[key]))
