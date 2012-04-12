# Project Euler
# Problem - 8
# Calculate the sum of all the primes below two million.

from math import sqrt

s = 2

def is_prime(n) :
    for j in range(2, int(sqrt(n)) + 1) :
        if (n % j == 0) :
            return 0
    return 1

for i in range(3, 2000000) :
    if is_prime(i) :
        s = s + i
print s
