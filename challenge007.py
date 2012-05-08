"""
 Project Euler Challenge 007

 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 What is the 10 001st prime number?
"""


import math


def solution(y):
    primes = []
    for i in range(1, y):
        s = round(math.sqrt(i))
        if (checkSquareUpTo(i, s) == False):
            primes.append(i)
    print (primes[10001])


def checkSquareUpTo(j, n):
    isDivisible = False
    for i in range(2, n + 1):
        if (j % i == 0):
            isDivisible = True
    return isDivisible


if __name__ == '__main__':
    print (solution(150000))
