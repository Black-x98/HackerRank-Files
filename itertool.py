import itertools as it

n,s,k = input(), input().split(), int(input())

c = list(it.combinations(s,k))

# filtering, lambda is a function,
# each element of which has 'a' in it and is among elements of c

f = list(filter(lambda t: 'a' in t, c))

print("{0:.3}".format(len(f)/len(c)))
