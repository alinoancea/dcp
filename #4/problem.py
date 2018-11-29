#!/usr/bin/env python3

def lowest_positive_integer(l):
    if not l:
        return 1

    # I assume that the maximum value in array is 100
    # it would be much nicer if I check for each element to see if it fits in the result :)
    result = [0] * 100
    for el in l:
        if el > 0:
            result[el - 1] = 1

    for i, el in enumerate(result):
        if not el:
            return i + 1
    return len(result) + 1


print(lowest_positive_integer([3, 4, -1, 1]))
print(lowest_positive_integer([1, 2, 0]))
print(lowest_positive_integer([5]))
print(lowest_positive_integer([]))
