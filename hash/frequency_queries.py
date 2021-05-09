#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    hash = Counter()
    count_hash = Counter()  # count => count of count
    result = []

    for q in queries:
        op, num = q[0], q[1]

        if op == 1:
            count_hash[hash[num]] -= 1
            hash[num] += 1
            count_hash[hash[num]] += 1
        elif op == 2:
            if hash[num] > 0: # count can be 0
                count_hash[hash[num]] -= 1
                hash[num] -= 1
                count_hash[hash[num]] += 1
        elif op == 3:
            if count_hash[num] > 0: # count can be 0
                result.append(1)
            else:
                result.append(0)

        # print(op, num, hash, count_hash)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
