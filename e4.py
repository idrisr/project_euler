# Project Euler problem 4
# What is the largest palindrome you can make which is the product of two 3
# digit numbers?
# Ans: 906609 = 913 * 993

import math

def get_digits(n):
    try:
        if n > 0:
            return int(math.log10(n)) + 1
        if n == 0:
            return 1
    except ValueError:
        print 'n: %r' % (n,)

def is_pal(number):
    digits = get_digits(number)
    while digits > 1:
        first = number / 10**(digits-1)
        last = number % 10
        if first == last:
            s = first * 10**(digits-1) + last
            number = (number-s) / 10
            digit_diff = digits - get_digits(number)
            if digit_diff > 2:
                p = number / 10**(digit_diff - 2)
                if float(number) / 10**(digit_diff - 2) == p:
                    number = p
                else:
                    return False
            digits = get_digits(number)
        else:
            return False
    return True 

def main():
    maxpal = (0, 0, 0)
    for first in xrange(100, 1000):
        for last in xrange(first, 1000):
            if is_pal(first * last):
                if first*last > maxpal[0]:
                    maxpal = (first*last, first, last)
    print maxpal

if __name__ == '__main__':
    main()

