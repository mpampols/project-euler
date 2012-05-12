"""
 Project Euler Challenge 009

 A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

 a^2 + b^2 = c^2
 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

 There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 Find the product abc.
"""

import math


def solution():
    limit = 300
    for i in range(1, limit):
        for j in range(i + 1, i * i):
            c = isTriplet(i, j)
            if (int(c)):
                tripletsum = i + j + round(c)
                if (tripletsum == 1000):
                    print (i * j * round(c))
                    break
    return "end"


# Returns True if a + b + c = 1000
def sumIsThousand(a, b, c):
    if isTriplet(a, b, c):
        result = a + b + c
        if (result == 1000):
            print (result)
    return 1


# Returns True if number is natural
def isNatural(x):
    if ((x >= 1) and (x % 1) == 0):
        return True
    else:
        return False


# Returns True if a^2 + b^2 = c^2
def isTriplet(a, b):
    sqrtof = (a ** 2) + (b ** 2)
    result = math.sqrt(sqrtof)
    if (isNatural(result)):
        return result
    else:
        return False

if __name__ == '__main__':
    print (solution())
