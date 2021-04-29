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


def isAnagrams(s1, s2):
    # convert s2 to hash for fast lookup
    hash = {}
    for c in s2:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1

    # check s1 against hash
    for c in s1:
        if c in hash and hash[c] > 0:
            hash[c] -= 1
        elif c in hash and hash[c] == 0:
            return False
        else:
            return False

    return True


def sherlockAndAnagrams(s):
    count = 0

    # get all permutations of substring pairs out of s
    # from 1 char substring to  n-1 char substring, where n = len(s)
    for i in range(1, len(s)):
        for j in range(len(s) - i):
            for k in range(j+1, len(s) - i+1):
                s1 = s[j:j + i]
                s2 = s[k:k + i]

                # print(s1, s2, isAnagrams(s1, s2))

                # check each of them if they are anagrams
                if isAnagrams(s1, s2):
                    count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
