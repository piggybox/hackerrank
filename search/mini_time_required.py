#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
def minTime(machines, goal):
    import math

    # estimate lower bound and upper bound
    speed = sum([1 / x for x in machines])
    low = math.floor(goal / speed)

    slowest_speed = 1 / max(machines) * len(machines)
    high = math.floor(goal / slowest_speed) + 1

    print(low, high)

    # binary search
    while low < high:
        mid = (low + high) // 2

        if sum([mid // x for x in machines]) < goal:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
