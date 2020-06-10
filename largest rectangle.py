

def largestRectangle(h):
    s = []
    ans = len(h)
    h.append(0)
    print("state of h: " + h.__str__())

    for i in range(len(h)):
        print("iteration i: " + i.__str__())
        left_index = i
        print("state of left_index: " + h.__str__())
        print("s: " + s.__str__())
        while len(s) > 0 and s[-1][0] > h[i]:
            print("inside while loop. ")
            print("s: " + s.__str__())
            last = s.pop()
            print("last: " + last.__str__())
            left_index = last[1]
            print("left_index or last(1): " + last[1].__str__())
            prev_ans = ans
            ans = max(ans, last[0] * (i - last[1]))
            print(ans.__str__() + " = max(" + prev_ans.__str__() + "," + str(last[0]) + "*" + str(i-last[1])  + ")")
        s.append((h[i], left_index))

    return ans

if __name__ == '__main__':

    inp = open("largest_rectangle_inp.txt",'r')

    n = int(inp.readline())

    p = [int(s) for s in inp.readline().split()]

    result = largestRectangle(p)

    print(result)
