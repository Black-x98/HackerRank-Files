def stripAlpha(sub):
    lensub = len(sub)
    cons = ''
    for i in range(lensub):
        c = sub[i]
        if c not in cons:
            cons += c
    return cons

def merge_the_tools(s, k):
    lens = len(s)

    for i in range(0,lens,k):
        print(stripAlpha(s[i:i+k]))

if __name__ == '__main__':

    string, k = input(), int(input())
    merge_the_tools(string, k)
