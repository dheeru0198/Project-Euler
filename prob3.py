# Project Euler
# Problem - 3
# Find the largest prime factor of a composite number.

from math import sqrt

c = int(raw_input("Enter any Composite number : "))
i = 3

def is_prime(n) :
    for j in range(2, int(sqrt(n)) + 1) :
        if (n % j == 0) :
            return 0
    return 1

while (i < c) :
    if  c % i == 0 :
        x = c / i
        if is_prime(x) :
            lpf = x
            break
    i += 1
print lpf
