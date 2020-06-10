def isBalanced(s):
    mylist = []

    for i in range(len(s)):
        ch = s[i]
        ##print "Inside function loop. i = " + str(i)
        if ch=='(' or ch== '{' or ch == '[':
            mylist.append(ch)
            ##print("Pushing " + ch + " in the stack.")
        elif len(mylist)==0:
            return "NO"
        else:
            if ch==')' and mylist[-1]=='(':
                #print("Before popping (, list: ")
                #print '[%s]' % ', '.join(map(str, mylist))
                mylist.pop()
                ##print("Succesful popping () .")
                #print("After popping ), list: ")
                #print '[%s]' % ', '.join(map(str, mylist))

            elif ch=='}' and mylist[-1]=='{':
                #print("Before popping {, list: ")
                #print '[%s]' % ', '.join(map(str, mylist))
                mylist.pop()
                ##print("Succesful popping {} .")
                #print("After popping }, list: ")
                #print '[%s]' % ', '.join(map(str, mylist))

            elif ch==']' and mylist[-1]=='[':
                #print("Before popping [, list: ")
                #print '[%s]' % ', '.join(map(str, mylist))
                mylist.pop()
                ##print("Succesful popping [] .")
                #print("After popping [, list: ")
                #print '[%s]' % ', '.join(map(str, mylist))

            else:
                #print("Found " + ch)
                #print("Not succesful popping, end bracket residue.")
                return "NO"

    if len(mylist)==0:
        #print("BINGO. IT MATCHED!!")
        return "YES"
    else:
        #print("Not succesful popping, front bracket residue.")
        return "NO"

stringlist = ["}][}}(}][))]","[](){()}","()","({}([][]))[]()","({}([][]))[]()", "]([[]])"]

for ind in range(0,len(stringlist)):

    print(isBalanced(stringlist[ind]))
    #print(stringlist[ind])
##print isBalanced("{[()]}")
