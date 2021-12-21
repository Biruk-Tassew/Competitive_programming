import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    newArr = [0]
    newArr+=arr
    for i in range(1, int(n)+1):
        if newArr[-i] < newArr[-i - 1]:
            temp = newArr[-i]
            newArr[-i] = newArr[-i - 1]
            print(*(newArr[1:]))
            newArr[-i - 1] = temp
        else:
            print(*(newArr[1:]))
            return 0

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)