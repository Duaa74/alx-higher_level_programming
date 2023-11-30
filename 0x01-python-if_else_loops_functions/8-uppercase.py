#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            output += chr(ord(char) - 32)
        else:
            output += char

    print(output + "\n", end="")
print()
