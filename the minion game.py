def minion_game(s):
    # your code goes here
    cons = 0
    vow = 0
    lens = len(s)

    for i in range(lens):

        if(s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U"):
            vow += lens - i
        else:
            cons += lens - i

    if(vow>cons):
        print("Kevin " + str(vow))
    elif(cons>vow):
        print("Stuart " + str(cons))
    else:
        print("Draw")

if __name__ == '__main__':
    #s = input()
    s = 'BANANA'
    minion_game(s)


# Stuart - consonant
# Kevin - vowel
