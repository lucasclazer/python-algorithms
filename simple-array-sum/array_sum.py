#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(ar):
    # Write your code here
    sum=0
    for i in ar:
        sum = sum + i
    
    print("Simple Sum result", sum)
    return sum


def arraySum(ar):
    # Write your code here
    ans = sum(ar)
    print("ArraySum Sum result", ans)
    return ans

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 10, 11]
    simpleArraySum(arr)
    arraySum(arr)