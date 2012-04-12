# Project Euler
# Problem - 4
# Find the largest palindrome made from the product of two 3-digit numbers.

p = 0

for a in range(100, 1000) :
    for b in range(100, a) :
        c = a * b
        if c > p :
            s = str(a * b)
            if s == s[::-1] :
                p = a * b
print p
