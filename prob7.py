# Project Euler
# Problem - 6
# What is the 10001st prime number?

from math import sqrt

count = 0
num = 2

def is_prime(n) :
    cnt = 0
    for i in range(1, int(sqrt(n)) + 1) :
        if (n % i == 0) :
            cnt = cnt + 1
    if (cnt == 1) :
        return 1
    else :
        return 0

while(1) :
    if is_prime(num) :
        count = count + 1
    if count >= 10001 :
        break
    num = num + 1

print num
