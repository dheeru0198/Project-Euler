# Project Euler
# Problem - 3
# Find the largest prime factor of a composite number.

c = int(raw_input("Enter any Composite number : "))
i = 2
j = 1
cnt = 0

while i < c :
    if  c % i == 0 :
        x = c / i
        while j < x :
            if x % j == 0 :
                cnt = cnt + 1
            j = j + 1
        j = 1
        if (cnt == 1) :
            lpf = x
            break
        cnt = 0
    i = i + 1
print lpf
