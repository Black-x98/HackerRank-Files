#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    num_of_swaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                num_of_swaps += 1
    print("Array is sorted in " + str(num_of_swaps) + " swaps.\nFirst Element: " + str(a[0]) + "\nLast Element: " + str(a[n-1]))



if __name__ == '__main__':
    n = int(input())

    a = []

    for i in range(n):
        a.append(input())
    #a = list(map(int, input().rstrip().split()))

    countSwaps(a)
