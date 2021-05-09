#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):

    # build frequency map
    hash = {}  # char => frequency
    for char in s:
        hash[char] = hash.get(char, 0) + 1

    # validate frequency distribution
    count_hash = {}  # freq => count of freq
    for freq in hash.values():
        count_hash[freq] = count_hash.get(freq, 0) + 1

    if len(count_hash.keys()) == 1:  # only 1 kind of freq, no need to remove
        return "YES"
    elif len(count_hash.keys()) == 2:  # only 2 kinds, how to make it to 1?
        print(count_hash)

        k1, k2 = count_hash.keys()
        # work on that count of freq == 1 kind,
        # either remove char completely or reduce freq to another
        if count_hash[k1] == 1 and (k1 == 1 or (k1 - 1 == k2)):
            return "YES"
        elif count_hash[k2] == 1 and (k2 == 1 or (k2 - 1 == k1)):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
