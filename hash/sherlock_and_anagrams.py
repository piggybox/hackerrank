#!/bin/python3

import math
import os
import random
import re
import sys

# medium

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    count = 0
    hash = {}

    # get all permutations of substring pairs out of s
    # from 1 char substring to  n-1 char substring, where n = len(s)
    for i in range(len(s)):
        for j in range(len(s) - i):
            # sort each substring and store the occurance in hash
            substring = ''.join(sorted(s[j:j + i + 1]))
            hash[substring] = hash.get(substring, 0) + 1

    # count through the hash on the number of anagrams using combination math
    for k in hash:
        count += (hash[k]-1) * hash[k] // 2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
