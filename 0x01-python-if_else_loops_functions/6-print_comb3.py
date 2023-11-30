#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if j == 10:
            print("0{}{}".format(i, j))
        else:
            print("0{}{}, ".format(i, j), end="")
