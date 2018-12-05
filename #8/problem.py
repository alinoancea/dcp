#!/usr/bin/env python3


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_unival_trees(tree, unival):
    if not tree:
        unival[0] = 1
        return 0

    univals = [[0], [0]]
    sm = check_unival_trees(tree.left, univals[0]) + check_unival_trees(tree.right, univals[1])
    if univals[0][0] and univals[1][0]:
        if not tree.left or tree.left.val == tree.val:
            if not tree.right or tree.right.val == tree.val:
                    sm += 1
                    unival[0] = 1
    return sm


t = Node(0, None, Node(1, Node(1, Node(1)), Node(0)))
assert check_unival_trees(t, [0]) == 3

t = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert check_unival_trees(t, [0]) == 5

t = None
assert check_unival_trees(t, [0]) == 0

t = Node(0)
assert check_unival_trees(t, [0]) == 1
