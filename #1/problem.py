#!/usr/bin/env python3

def check(lst, k):
    d = set()
    for n in lst:
        if k - n in d:
            return True
        d.add(n)
    return False

print(check([10, 15, 3, 7], 17))
print(check([10, 15, 3, 7], 11))