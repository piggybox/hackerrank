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
    for i in range(len(s)//2):
        if s[i] == s[len(s)-i-1] :
            continue
        else:
            return False
        
    return True

def palindromeIndex(s):
    # if it's already a palindrome
    if checkPalindrome(s):
        return -1

    # otherwise scan through the string
    for i in range(len(s)):
        substring = s[0:i] + s[i+1:]
        if checkPalindrome(substring) :
            return i

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
