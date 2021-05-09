#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternatingCharacters(s):
    count = 0
    l = len(s) - 1
    i = 0

    while i < l:
        if s[i] == s[i + 1]:  # found dup
            s = s[:i] + s[i + 1:]  # remove the original s[i]
            l -= 1
            count += 1
        else:
            i += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
