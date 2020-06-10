#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    #n = len(p)
    days = 0
    max_days = 0
    print(str(p))
    start = 0
    max_days = 0
    days = 0
    untouched = True
    for i in range(len(p)-1):
        print("start = " + str(start))
        print("p[start] < p[i+1]: " + str(p[start]) + " < " + str(p[i+1]) + " : " + str(int(p[start]) < int(p[i+1])))
        if p[i]==p[i+1]:
            start = i+1
            print("transfering the start to: p[" + str(start) + "] = " + str(p[start]))
            days = 0
            untouched = True
        elif p[i] < p[i+1]:
            print("p[i] < p[i+1]: " + str(p[i]) + " < " + str(p[i+1]) + " : " + str(p[i] < p[i+1]))
            print("continue")
            if untouched:
                days = 1
                print("days: " + str(days))
                untouched = False
                if max_days<days:
                    max_days=days
                    print("max days: " + str(max_days))
        elif p[start] > p[i+1]:
            start= i+1
            days = 0
            untouched = True
            print("transfering the start to: p[" + str(start) + "] = " + str(p[start]))
        else:
            days+=1
            print("days: " + str(days))
            print("toggling num of days at: " + str(i+1) + "] = " + str(p[i+1]))
            if max_days<days:
                max_days=days
                print("max days: " + str(max_days))

    return max_days

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    inp = open("poison_plant_inp.txt",'r')
    #n = int(input())
    n = int(inp.readline())
    #p = list(map(int, input().rstrip().split()))
    #p = int(inp.readline().split())
    p = [int(s) for s in inp.readline().split()]
    print p[0]+p[2]
    result = poisonousPlants(p)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
