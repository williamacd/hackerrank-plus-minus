#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    neg = 0
    zero = 0
    pos = 0

    for x in arr:
        if x < 0:
            neg += 1
        elif x == 0:
            zero += 1
        else:
            pos += 1

    print(f'{pos / len(arr):.5f}')
    print(f'{neg / len(arr):.5f}')
    print(f'{zero / len(arr):.5f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
