#!/usr/bin/env python3

# in the dictionary I save every new node which I create, so I can find it with his id
d = {}


class Node:

    def __init__(self, value, prev, nxt):
        self.value = value
        self.both = prev ^ nxt


class XORLinkedList:

    def __init__(self):
        self.first = self.last = None
        self.length = 0

    def add(self, element):
        if not self.first:
            new_node = Node(element, 0, 0)
            self.first = new_node
        else:
            new_node = Node(element, id(self.last), 0)
            self.last.both ^= id(new_node)
            if not self.first.both:
                self.first.both = 0 ^ id(new_node)
        d[id(new_node)] = new_node
        self.last = new_node
        self.length += 1

    def get(self, index):
        if index < 0:
            return
        elif index >= self.length:
            return
        elif index == 0:
            return id(self.first)
        prev = 0
        node = self.first
        while index:
            nxt = prev ^ node.both
            prev = id(node)
            node = d[nxt]
            index -= 1
        return id(node)


lst = XORLinkedList()
lst.add(1)
lst.add(2)
lst.add(3)

print(d.get(lst.get(1)).value)
print(d.get(lst.get(0)).value)
print(d.get(lst.get(2)).value)
print(d.get(lst.get(3)))
