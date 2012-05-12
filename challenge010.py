"""
 Project Euler Challenge 010

 The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

 Find the sum of all the primes below two million.
"""


from math import sqrt


def solution(n):
    primes = []
    primes.append(2)

    for i in range(3, n, 2):
        is_prime = True

        for j in range(3, int(sqrt(n)), 2):
            if (j > sqrt(i)):
                break

            if ((i % j) == 0):
                is_prime = False
                break

        if (is_prime == True):
            primes.append(i)

    return (primes)


if __name__ == '__main__':
    print (sum(solution(2000000)))
