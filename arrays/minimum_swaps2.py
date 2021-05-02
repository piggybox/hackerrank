#!/bin/python3

import math
import os
import random
import re
import sys

# medium

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0

    for i in range(len(arr)):
        # swap arr[i] to where it should be
        # loop until arr[i] is right

        # the main difference between this and general sorting is that we do know where the final position should be
        while arr[i] != i + 1:
            correct_index = arr[i] - 1
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            swap_count += 1

    return swap_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
