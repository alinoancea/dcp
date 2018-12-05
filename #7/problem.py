#!/usr/bin/env python3


def count_decode_ways(message):
    if not message:
        return 0

    temp = [1] + [0] * len(message)
    for i in range(1, len(message) + 1):
        temp[i] += temp[i - 1]
        if i != 1 and int(message[i - 2:i]) > 9 and int(message[i - 2:i]) < 27:
            temp[i] += temp[i - 2]
    return temp[len(message)]


assert count_decode_ways('111') == 3
assert count_decode_ways('12') == 2
