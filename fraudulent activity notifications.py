#!/bin/python3

import math
import bisect

# Complete the activityNotifications function below.
# Complete the activityNotifications function below.
def activityNotifications(exp, d):
    d=int(d)
    n = len(exp)
    notice = 0
    freq = [0]*201
    '''m = max(exp)
    odd = False
    even = False
    if d%2==0:
        even = True
    else:
        odd = True'''

    for i in range(0,d):
        freq[exp[i]] += 1

    for i in range(d,n):
        count = 0
        median = 0
        j = 0
        while count <= int(d/2):
            count += freq[j]
            median = j
            j += 1
        #print("median: " + str(median))

        if exp[i]>=2*median:
            notice += 1

        freq[exp[i-d+1]] -= 1
        freq[exp[i]] += 1

    return notice

if __name__ == '__main__':

    inp = open("fraud_inp.txt",'r')

    n = inp.readline().split()

    #p = list(map(int, input().rstrip().split()))
    #p = int(inp.readline().split())
    p = [int(s) for s in inp.readline().split()]
    result = activityNotifications(p,n[1])

    print(result)
'''
    9 5
    2 3 4 2 3 6 8 4 5
'''
'''
fraud_inp.txt 
expected output 633
'''
