#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    seen = set()
    for num in my_list:
        if num not in seen:
            seen.add(num)
            uniq_sum += num
    return uniq_sum
