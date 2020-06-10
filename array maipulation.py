#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    m = len(queries)
    arr = (n+1)*[0]
    for i in range(m):
        #print(str(int(queries[i][0])))
        arr[int(queries[i][0])-1] += int(queries[i][2])
        arr[int(queries[i][1])] -= int(queries[i][2])

    max_val = -1
    for i in range(1,n):
        arr[i] = arr[i] + arr[i-1]
        if arr[i] > max_val:
            max_val = arr[i]
    #print("MAX VAL " + str(max_val))
    return max_val

if __name__ == '__main__':

    inp = file("array_manipulation.txt",'r')
    line = inp.readline().split()
    n = int(line[0])
    m = int(line[1])
    #print n,m
    queries = []
    for _ in range(m):
        q = inp.readline().split()
        #print q
        queries.append(q)

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')

# expected output for array_manipulation.txt input: 2484930878
