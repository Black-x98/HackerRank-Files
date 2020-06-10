#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqList = ['' for i in range(n)]
    lastAnswer = 0
    resultArray = []
    print "the length of queries is: " + str(len(queries))
    for i in range(len(queries)):
        q_type = queries[i][0]
        #print queries[i][1]
        x = int(queries[i][1])
        #print queries[i][2]
        y = int(queries[i][2])
        #print "q_type is " + str(q_type)
        print(q_type==1)
        print(q_type==2)

        if q_type=='1':
            print "in option 1"
            index = (x^lastAnswer)%n
            seqList[index] += str(y)
            print seqList[(x^lastAnswer)%n]
            #print seqList
        elif q_type=='2':
            print "in option 1"
            index = (x^lastAnswer)%n
            seq = seqList[index]
            lastAnswer = int(seqList[index][y % len(seq)])
            resultArray.append(lastAnswer)
            print "result array: ",
            print resultArray
    #print "returning the resultArray. "
    return resultArray

n = 2
num_q = 5
q = []
queries = []
n = int(raw_input())
num_q = int(raw_input())

for i in range(num_q):
    q = raw_input()
    q = q.split(" ")
    queries.append(q)
#queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]

print dynamicArray(n,queries)
