#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

# medium

from collections import deque


class Node:
    def __init__(self, d):
        self.data = d


def build_tree(indexes):
    f = lambda x: None if x == -1 else Node(x)
    children = [list(map(f, x)) for x in indexes]
    nodes = {n.data: n for n in filter(None, sum(children, []))}
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        nodes[idx + 1].left = child_pair[0]
        nodes[idx + 1].right = child_pair[1]
    return nodes[1]


def inorder(root):
    # DFS

    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.data
            curr = curr.right


def swapNodes(indexes, queries):
    # BFS

    # convert input to tree structure
    root = build_tree(indexes)

    for k in queries:
        level = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()  # queue
                if level % k == 0:
                    # swap
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            level += 1

        yield inorder(root)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
