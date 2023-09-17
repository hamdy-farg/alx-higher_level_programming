#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    b = 0
    for i in my_list:
       seen.add(i)
    for i in seen:
        b += i
    return (b)
