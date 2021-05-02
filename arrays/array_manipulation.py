#!/bin/python3

import math
import os
import random
import re
import sys

# hard

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # initialize a 0 filled array
    array = [0 for x in range(n + 1)]

    # for each query, update the start and end of change
    # O(1) operation
    for q in queries:
        lower, upper, count = q[0], q[1], q[2]
        array[lower] += count
        if upper + 1 <= n:
            array[upper + 1] -= count

    max = 0
    current = 0

    for k in array:
        current += k
        if current > max:
            max = current

    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
