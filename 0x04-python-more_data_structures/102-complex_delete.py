#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    n1 = [key for key, val in a_dictionary.items() if val == value]
    for key in n1:
        del a_dictionary[key]
    return a_dictionary
