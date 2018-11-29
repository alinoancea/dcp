#!/usr/bin/env python3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(p):
    def aux(a, b):
        return a
    return p(aux)

def cdr(p):
    def aux(a, b):
        return b
    return p(aux)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
