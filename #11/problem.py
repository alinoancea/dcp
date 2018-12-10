#!/usr/bin/env python3


def preprocess_initial_list(l):
    # if we want just the unique element we can change the list from values key to a set
    d = {}
    for c in l:
        dc = d
        for cc in c:
            exists = dc.get(cc)
            if not exists:
                dc[cc] = {'values': [c]}
            else:
                dc[cc]['values'].append(c)
            dc = dc[cc]
    return d


def get_matches(d, query_s):
    for c in query_s:
        d = d.get(c)
        if not d:
            return None
    return d.get('values')


lp = preprocess_initial_list(['dog', 'deer', 'deal'])

assert get_matches(lp, 'de') == ['deer', 'deal']
assert get_matches(lp, 'e') == None
