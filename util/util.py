import math

def get_nth_digit(n, digit):
    """returns digit of n, where ones places is digit 1, tens place is digit 2, etc"""
    n = n / 10**(digit-1)
    return n % 10

def get_digits(n):
    try:
        if n > 0:
            return int(math.log10(n)) + 1
        if n == 0:
            return 1
    except ValueError:
        print 'n: %r' % (n,)

def get_first_digit(n):
    return get_nth_digit(n, 1)
