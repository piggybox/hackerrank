#!/bin/python3

import math
import os
import random
import re
import sys


# a specialized version of merge sort that counts inversion
def sort(arr):
    mid = len(arr) // 2
    if len(arr) >= 2:
        sorted_left, counts_left = sort(arr[:mid])
        sorted_right, counts_right = sort(arr[mid:])
        result, counts_merge = merge(sorted_left, sorted_right)
        return result, counts_merge + counts_left + counts_right
    else:
        return arr, 0


def merge(arr_left, arr_right):
    counts = 0
    result = []  # this version is not very memeory efficient
    pl = 0  # pointer left
    pr = 0  # pointer right
    lenl = len(arr_left) # len or pop operation in python is O(n)!
    lenr = len(arr_right)

    # specialized python version using list pop without using index
    while pl < lenl and pr < lenr:
        if arr_left[pl] <= arr_right[pr]:
            result.append(arr_left[pl])  # pop the head
            pl += 1
        else:
            counts += lenl - pl  # number of inversions
            result.append(arr_right[pr])  # pop the head
            pr += 1

    # deal with what's left
    if lenl == pl:
        result += arr_right[pr:]
    elif lenr == pr:
        result += arr_left[pl:]

    return result, counts


# Complete the countInversions function below.
def countInversions(arr):
    # this is a merge sort question!

    result, counts = sort(arr)
    # print(result)

    return counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
