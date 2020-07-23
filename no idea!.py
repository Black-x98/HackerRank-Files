# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
fptr = sys.stdout


n,m = input().split()

arr = input().split()

a = set(input().split())

b = set(input().split())

score = 0

lena = len(arr)

for i in range(lena):
    if arr[i] in a:
        score+=1
    elif arr[i] in b:
        score-=1

print(score)

'''
3 2
1 5 3
3 1
5 7
'''
