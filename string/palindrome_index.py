#!/bin/python3

import math
import os
import random
import re
import sys

# easy

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def checkPalindrome(s):
    if len(s) % 2 == 1:
        first_half = s[: len(s) // 2]
        second_half = s[len(s)//2 + 1:]
    else:
        first_half = s[: len(s) // 2]
        second_half = s[len(s)//2:]

    if first_half == second_half[::-1]:  # reversed
        return True
    else:
        return False


def palindromeIndex(s):
    # if it's already a palindrome
    if checkPalindrome(s):
        return -1

    # otherwise scan through the string
    for i in range(len(s)):
        substring = s[0:i] + s[i+1:]
        if checkPalindrome(substring):
            return i

    # whether it's already a palindrome or not
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
