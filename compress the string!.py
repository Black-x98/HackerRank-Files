# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
fptr = sys.stdout


s = input()
lens = len(s)
i = 0

while i < lens:
    curr = s[i]
    count = 1
    while(i<lens-1 and curr==s[i+1]):
        count+=1
        i+=1
    i+=1
    print("(" + str(count) + ", " + curr + ") ", end ='')

