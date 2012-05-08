"""
 Project Euler Challenge 005

 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def search_num():
    for i in range(2520, 999999999, 2520):
        result = True
        for dn in range(1, 20):
            if (i % dn != 0):
                result = False
        if (result == True):
            return i


if __name__ == '__main__':
    print (search_num())
