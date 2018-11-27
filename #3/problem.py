#!/usr/bin/env python3

import re


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def deserialize(s):
    e = re.split('[;|]', s, 1)
    if len(e) != 2:
        return Node(e[0])

    l = r = None
    if s[len(e[0])] == ';':
        l = deserialize(e[1])
    else:
        r = deserialize(e[1])
    return Node(e[0], l, r)


def serialize(node):
    if node:
        l = r = ''
        if node.left:
            l = ';' + serialize(node.left)
        if node.right:
            r = '|' + serialize(node.right)
        return str(node.val) + l + r


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

node = Node('root')
assert deserialize(serialize(node)).val == 'root'

node = Node('root', Node('left', Node('left.left')))
assert deserialize(serialize(node)).left.left.val == 'left.left'

node = Node('root', right=Node('right', right=Node('right.right')))
assert deserialize(serialize(node)).right.right.val == 'right.right'