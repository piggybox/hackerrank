#!/bin/python3

import math
import os
import random
import re
import sys

# medium 

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    total = 0
    
    # sort c from big to low
    sorted_c = sorted(c, reverse=True)
    
    # get biggest first then lower       
    for i in range(len(sorted_c)):
        total += sorted_c[i] * (i // k + 1)
        
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
