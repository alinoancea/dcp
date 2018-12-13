#!/usr/bin/env python3


def longest_substring(s, k):
    old_longest_s = ''
    current_longest_s = ''

    for c in s:
        if c not in current_longest_s and len(set(current_longest_s)) < k:
            current_longest_s += c
        elif c in current_longest_s:
            current_longest_s += c
        else:
            if len(current_longest_s) > len(old_longest_s):
                old_longest_s = current_longest_s
            while len(set(current_longest_s)) == k:
                current_longest_s = current_longest_s[1:]
            current_longest_s += c
    else:
        if len(current_longest_s) > len(old_longest_s):
            old_longest_s = current_longest_s
    return len(old_longest_s)


assert longest_substring('abcba', 2) == 3
assert longest_substring('bbaaaacd', 1) == 4
assert longest_substring('a', 2) == 1
