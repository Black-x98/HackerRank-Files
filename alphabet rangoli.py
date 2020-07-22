def print_rangoli(size):
    # your code goes here
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    loopsize = size + size - 1
    for i in range(0, loopsize):
        t = abs(size-1-i)
        #print(t)
        for j in range(0, t): # 5 to 1

            print('-',end='')

            print('-', end='')

        for j in range(0, size-t): # 5 to 1

            print(alpha[size-j-1], end='')
            if j!=size-t-1:
                print('-', end='')

        for j in range(size-t-2 , -1, -1): # 2 to 5
            print('-' + alpha[size-j-1], end='')

        for j in range(0, t): # 2 to 5
            print('-', end='')

            print('-', end='')

        print("")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


'''    
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
