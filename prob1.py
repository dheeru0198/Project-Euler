# Project Euler
# Problem - 1 
# Add all the natural numbers below one thousand that are multiples of 3 or 5.

s = 0
i = 3

while i < 1000 :
    if (i%3 == 0 or i%5 == 0) :
        s = s + i
    i = i + 1
print "%d" % s
