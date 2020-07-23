import os
import sys
fptr = sys.stdout

def func():

    f = int(input())
    
    l= list(map(int, input().split(" ")))

    count = 0

    i = 0
    while i<f-1 and l[i] >= l[i+1]:
        count += 1
        i += 1

    while i<f-1 and l[i] <= l[i+1]:
        count += 1
        i += 1

    if count == f-1:
        print("Yes")

    else:
        print("No")

n = int(input())
for i in range(n):
    func()

'''2
6
4 3 2 1 3 4
3
1 3 2'''
