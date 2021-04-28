#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_hash = {}
    for w in magazine:
        if w in mag_hash:
            mag_hash[w] += 1
        else:
            mag_hash[w] = 1

    for w in note:
        if w not in mag_hash:
            print("No")
            return
        elif w in mag_hash:
            if mag_hash[w] < 1:
                print("No")
                return
            else:
                mag_hash[w] -= 1 # remove 1 count
    
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
