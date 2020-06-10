

def flippingBits(n):

    b = format(n, '32b')
    inv = ''
    for i in range(len(b)):
        inv += int(str(1)) ^ int(b[i])
    print(inv)
    return inv


print(flippingBits(2147483647))
