"""
 Project Euler Challenge 003

 The prime factors of 13195 are 5, 7, 13 and 29.
 What is the largest prime factor of the number 600851475143 ?
"""

import math


def largest_prime_factor(i):
    num1 = 0
    num1 = i
    result = 0

    # check if 2 is a factor of i
    while (num1 % 2 == 0):
        result = 2
        num1 = num1 / 2

    # try odd numbers, starting from 3
    count = 3
    r = 0
    r = math.sqrt(num1)

    while (count <= r and num1 > 1):
        if (num1 % count == 0):
            result = count
            num1 = num1 / count
        else:
            count = count + 2

    if (num1 > 1):
        result = num1

    return result

if __name__ == '__main__':
    print (largest_prime_factor(600851475143))
