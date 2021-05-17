#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.


def triplets(a, b, c):
    # dedup and sort
    a = list(sorted(set(a))) 
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))

    ai = 0
    bi = 0
    ci = 0

    ans = 0

    while bi < len(b):
        # a very smart solution to cumulatively compute
        # count_a and count_c without rescaning list a and c
        while ai < len(a) and a[ai] <= b[bi]: # stop early
            ai += 1

        while ci < len(c) and c[ci] <= b[bi]: # stop early
            ci += 1

        ans += ai * ci
        bi += 1

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
