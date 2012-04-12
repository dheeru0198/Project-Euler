# Project Euler
# Problem - 5
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

i = 20
cnt = 0
while i > 0 :
    for j in range(1, 21) :
        if ( i % j == 0 ) :
            cnt = cnt + 1
    if (cnt == 20) :
        break
    cnt = 0
    i = i + 1
print i
