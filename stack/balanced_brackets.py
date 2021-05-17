#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# medium

def isBalanced(s):
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            # unmatching
            if len(stack) == 0:
                return 'NO'

            temp = stack.pop()
            if temp == '{' and i != '}':
                return 'NO'
            if temp == '[' and i != ']':
                return 'NO'
            if temp == '(' and i != ')':
                return 'NO'

    # check what's left in stack
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
