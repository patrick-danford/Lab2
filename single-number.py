"""
Lab 2 assignment - Single number
Patrick Danford

This script inputs a list of numbers and identifies 
the number that only occurs once in the list

"""

numbers_list = [2, 3, 2, 3, 5, 5, 6, 6, 7]


def find_unique(numbers):
    for x in numbers:
        if numbers.count(x) is 1:
            return x


print "The unique number is %d" % find_unique(numbers_list)



