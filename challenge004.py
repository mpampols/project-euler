"""
 Project Euler Challenge 004

 A palindromic number reads the same both ways.
 The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
 Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(i):
    try:
        if (str(i)[0] == str(i)[5] and
            str(i)[1] == str(i)[4] and
            str(i)[2] == str(i)[3]):
            return True
        else:
            return False
    except IndexError:
        print ("error: ", i)


if __name__ == '__main__':
    list_palindromes = []
    n = 0
    for i in range(100, 999):
        for j in range(100, 999):
            n = i * j
            if (len(str(n)) == 6):
                if (is_palindrome(n)):
                    list_palindromes.append(n)
    print (max(list_palindromes))
