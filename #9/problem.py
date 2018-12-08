#!/usr/bin/env python3


def get_max_sum(l):
    """
    Create a list of lists - every sublist has on each 'i' position the maximum sum that can be made 
    [with, without] the 'i' element

    Observations:
        1) if the list contains only negative numbers => sum = 0
        2) could be completed using only 3 variables
    """
    if not len(l):
        return None
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)

    f = [[l[0], 0], [l[1], max([l[0], 0])]]
    for e in l[2:]:
        f.append([e + max(f[-2]), max(f[-1])])

    return max(f[-1])


l = [2, 4, 6, 2, 5]
assert get_max_sum(l) == 13

l = [5, 1, 1, 5]
assert get_max_sum(l) == 10

l = [-1, -2, -3]
assert get_max_sum(l) == 0
