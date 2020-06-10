import random

sum = 0
gum = 0
lim = 100000000
for i in range(1000):
    for j in range(1000):
        val = random.randint(0,lim)
        if val >= lim-500:
            sum += 1
        if val < lim-500:
            gum += 1
print "The yes ratio is: " + (sum*1.0/1000000).__str__()
print "The no ratio is: " + (gum*1.0/1000000).__str__()
