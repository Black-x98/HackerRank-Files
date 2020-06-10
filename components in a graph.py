'''
input
10
1 17
5 13
7 12
5 17
5 12
2 17
1 18
8 13
2 15
5 20

expected output:
11
'''

#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
#
def componentsInGraph(gb):

    n = len(gb)
    #print(gb)
    setofset1 = []
    setofset2 = []

    for i in range(len(gb)):
        #print("*************** This turn: " + str(gb[i]))
        #print("current setofset1: " + str(setofset1) + "```````````````")
        #print("current setofset2: " + str(setofset2) + "```````````````")
        if len(setofset1) != 0:
            flag = False
            setsToUnion = []
            size1 = len(setofset1)
            size2 = len(setofset2)
            sizem = max(size1,size2)
            for j in range(sizem):
                if gb[i][0] in setofset1[min(size1-1,j)] or gb[i][1] in setofset2[min(size2-1,j)]:
                    #print("Yes, " + str(gb[i][0]) + " or " + str(gb[i][1])  +" matched in set: " + str(setofset[j]))
                    setsToUnion.append(j)
                    #print("Size of sets to union: "+ str(len(setsToUnion)))
                    flag = True

            if flag == False:
                setofset1.append(set()) # appending
                setofset2.append(set()) # appending
                setofset1[len(setofset1)-1].add(gb[i][0])
                setofset2[len(setofset2)-1].add(gb[i][1])
                #print("adding " + str(gb[i]) + " in new set " + str(len(setofset)-1))

            elif len(setsToUnion)>=1:
                for k in range(1,len(setsToUnion)):
                    #print("Unioning " + str(setofset[setsToUnion[0]]) + " and " + str(setofset[setsToUnion[k]]))
                    #print(" setToUnion[k] : " + str(setsToUnion[k]) + " length of setofset1: " + str(len(setofset1)) + " length of setofset2: " + str(len(setofset2)) )
                    setofset1[setsToUnion[0]] = setofset1[setsToUnion[0]].union(setofset1[setsToUnion[k]])
                    setofset2[setsToUnion[0]] = setofset2[setsToUnion[0]].union(setofset2[setsToUnion[k]])
                    #print("end result: " + str(setofset[setsToUnion[0]]))
                    if k>0:
                        #print("popping: " + str(setsToUnion[k]) +": " + str(setsToUnion[k]))
                        setofset1.pop(setsToUnion[k])
                        setofset2.pop(setsToUnion[k])
                #setofset1[setsToUnion[0]] = setofset1[setsToUnion[0]].union(gb[i][0])
                setofset1[setsToUnion[0]].add(gb[i][0])
                #setofset2[setsToUnion[0]] = setofset2[setsToUnion[0]].union(gb[i][1])
                setofset2[setsToUnion[0]].add(gb[i][1])
        else:
            myset1 = set()
            myset2 = set()
            myset1.add(gb[0][0])
            myset2.add(gb[0][1])
            setofset1.append(myset1) # appending
            setofset2.append(myset2) # appending
            #print("adding " + str(gb[i]) + " in set 0")

    #print(str(setofset1))
    #print(str(setofset2))
    #print("*************")
    max_size = 0
    min_size = 15001
    for l in range(len(setofset1)):
        current_size = len(setofset1[l]) + len(setofset2[l])
        if current_size > max_size:
            max_size = current_size
        if current_size >= 2 and current_size < min_size:
            min_size = current_size
    res = []
    res.append(min_size)
    res.append(max_size)
    #print("returning this list: " + str(res))
    return res

if __name__ == '__main__':

    gb=[]
    #gb = [[1,17],[5,13],[7,12],[5,17],[5,12],[2,17],[1,18],[8,13],[2,15],[5,20]]

    inp = file("input.txt",'r')
    n = int(inp.readline().split()[0])
    for _ in range(int(n)):
        gbs = inp.readline().split()
        gb.append(gbs)

    # input.txt er expected output: 1196 1196
    result = componentsInGraph(gb)

    print(str(result[0]) + " " + str(result[1]))
