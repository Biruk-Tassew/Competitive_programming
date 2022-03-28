#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    nav = 0
    trav = 0
    down = False
    travCounter = 0
    for i in path:
        if i == "D":
            nav -= 1
        else:
            nav += 1
            
        if nav < 0:
            if i == "D":
                down = True
                trav -= 1
            else:
                trav += 1
        if nav == 0 and trav == -1:
            trav += 1
        if trav == 0 and down:
            down = False
            travCounter += 1
    return travCounter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
