# Project Euler
# Problem - 6
# What is the difference between the sum of the squares and the square of the sums?

from math import pow

n = int(raw_input("Enter n : "))

sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
square_of_sums = pow(n, 2) * pow(n + 1, 2) / 4

print "\nThe difference between the sum of the squares and the square of the sums of first %d natural numbers is : %d" % (n, square_of_sums - sum_of_squares)
