#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    alert = 0

    # use count sorting to compute medium in a moving window
    cs = [0 for x in range(201)]
    for i in range(d):
        cs[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        # get median using count sorting array

        two_median = 0
        if d % 2 == 1:
            # aggregate count to find out median
            k, j = 0, 0
            while k < (d // 2 + 1):
                k += cs[j]
                j += 1

            two_median = 2 * (j - 1)  # ugly patch
        else:
            k, j = 0, 0
            while k < (d // 2):
                k += cs[j]
                j += 1

            k, q = 0, 0
            while k < (d // 2 + 1):
                k += cs[q]
                q += 1

            two_median = j + q - 2  # ugly patch

        if expenditure[i] >= two_median:
            alert += 1

        # update count sort array
        cs[expenditure[i]] += 1
        cs[expenditure[i - d]] -= 1

    return alert


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
