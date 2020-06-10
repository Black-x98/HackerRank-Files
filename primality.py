#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):

    if n==1:
        return 'Not prime'
    elif n==2:
        return 'Prime'

    root = int(pow(n,0.5))
    #print root
    for i in range(2,root+1):
        #print(i)
        if n%i == 0:
            print("yes divved")
            return 'Not prime'

    return 'Prime'

if __name__ == '__main__':
    inp = open('primality_inp.txt','r')

    p = int(inp.readline())

    for p_itr in range(p):

        n = int(inp.readline())

        print n,

        result = primality(n)

        print(result + '\n')

    inp.close()
    #print primality(9)


'''
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Not prime
Prime

'''
