

def largestRectangle(h):
    s = []
    ans = len(h) #at least the number of buildings is the minimum possible maximum area
    h.append(0) #to terminate the last building

    for i in range(len(h)):

        left_index = i

        while len(s)>0 and h[i]<=s[-1][0]: # while loop to keep popping until you go to the leftest one of valid starting points
            last = s.pop() # last[0] = h[i] and last[1] is the left_index for that area calculation
            left_index = last[1]
            area = (i-last[1]) * last[0]
            ans = max(ans,area) # we never want to forget the maximum possible area

        s.append((h[i],left_index))

    return ans

if __name__ == '__main__':

    inp = open("largest_rectangle_inp.txt",'r')

    n = int(inp.readline())

    p = [int(s) for s in inp.readline().split()]

    result = largestRectangle(p)

    print(result)
