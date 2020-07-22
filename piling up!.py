import os
import sys
fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

def func():
    f = int(input())
    
    l= list(map(int, input().split(" ")))

    pick = (2<<31) + 1

    for i in range(len(l)):
        b, e = l[0], l[-1] 
        
        if b>pick and e>pick:
            fptr.write("No")
            break

        elif b>e:
            if b>pick:
                fptr.write("No")
                break
            pick = b
            #efptr.write(str(l) + "\n")
            l = l[1:]
            #efptr.write(str(l) + "\n")


        elif b<e:
            if e>pick:
                fptr.write("No")
                break
            pick = e
            #efptr.write(str(l) + "\n")
            l = l[:-1]
            #efptr.write(str(l) + "\n")


        elif b==e and e<=pick:
            pick = e
            #efptr.write(str(l) + "\n")
            l = l[:-1]
            #efptr.write(str(l) + "\n")

        if len(l)<=0:
            fptr.write("Yes")
            break

n = int(input())
for i in range(n):
    func()

'''2
6
4 3 2 1 3 4
3
1 3 2'''
