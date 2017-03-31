"""
Lab 2 assignment - Power Function
Patrick Danford

This script demonstrates the pow function by squaring a number input
"""


def power(x, n):
    result = pow(x, n)
    return result


def square(num):
    num_squared = pow(num, 2)
    return num_squared

test1, test2 = 2,2
assert (power(test1, test2) == 4)

print "The square of that number is: %d" % square(input("Enter a number: "))


