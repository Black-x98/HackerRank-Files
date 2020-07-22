def merge_the_tools(s, k):
    # your code goes here
    lens = len(s)

    for i in range(0,lens,k):

        print(s[i:i+k])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
