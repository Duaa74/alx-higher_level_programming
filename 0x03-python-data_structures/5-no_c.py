#!/usr/bin/python3
def no_c(my_string):
    i = ""
    for char in my_string:
        if char != "c" and char != "C":
            i += char
    return i
