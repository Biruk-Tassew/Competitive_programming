#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    count = 0
    should_restart = True
    while should_restart:
        should_restart = False
        for i in range(len(a)-1):
            if(a[i] > a[i+1]):
                (a[i], a[i+1]) = (a[i+1], a[i])
                count +=1
                if (a[i] < a[i-1]):
                    should_restart = True
    print("Array is sorted in %d swaps." % count)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

