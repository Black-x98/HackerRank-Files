# Enter your code here. Read input from STDIN. ##print output to STDOUT
#import sys

n = int(input())
###print n
stack = []
S = ''
inp = file("input_ste.txt",'r')
n = int(inp.readline().split()[0])
#print n
#cmnds = [[1,'aaaa'],[1,'tttt'],[2,2],[3,1],[4]]
#n=len(cmnds)
##print(n)
for i in range(n):
    command = input().split()#sys.stdin.readline().split()
    command = inp.readline().split()
    #command = cmnds[i]
    #print(str(command))
    ##print(stack)
    string = ''
    ###print(str(command))
    ##print(S)
    if command[0] == '1':
        ##print("1111111111111111")
        string = command[1]
        ##print("##print string")
        ##print(string)
        stack.append([1,len(string)])
        S += string
        ##print(S)
    elif command[0] == '2':
        ##print("22222222222")
        ##print("````````````")
        ##print(command[1])
        num_pop = int(command[1])
        string = S[-num_pop:]
        stack.append([2,string])
        S = S[:-int(command[1])]
        ##print(S)
    elif command[0] == '3':
        ##print("33333333333333")
        pos = int(command[1])-1
        print(S[pos])
        ##print(S)
    elif command[0] == '4':
        ##print("44444444444444")
        undo_pop = stack.pop()
        if undo_pop[0]==1:
            S = S[:-undo_pop[1]]
        elif undo_pop[0]==2:
            S += undo_pop[1]
        ##print(S)
