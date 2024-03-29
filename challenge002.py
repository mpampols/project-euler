"""
 Project Euler Challenge 002

 Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def fib(i):
    if i == 1:
        return 1
    if i == 2:
        return 2
    if i > 2:
        return fib(i - 1) + fib(i - 2)


if __name__ == '__main__':
    max_value = 4000000
    total = 0
    actual_value = 1
    fibonacci = None
    while(1):
        if (fib(actual_value) > max_value):
            break
        else:
            fibonacci = fib(actual_value)
            if (fibonacci % 2) == 0:
                total += fib(actual_value)
        actual_value += 1
    print (total)
