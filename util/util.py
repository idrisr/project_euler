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

def is_div(n, m):
    """tests to see if n is evenly divisible by m"""
    # check if remainder
    return math.fmod(n, m)==0

def is_prime(n, primes=[]):
    """takes a number n to see if its primes, and an optional parameter known primes"""
    # max possible factor is the square root
    rootn = math.sqrt(n)
    # test all known primes first
    for prime in primes:
        if prime <= rootn:
            if is_div(n, prime):
                return False
        else:
            return True

    x = prime[-1] + 1
    max_i = (rootn - 1) / 6
        
    # if not yet at max keep going with 6*i-1 and 6*i+1
    for i in xrange(x, max_i):
        m = 6*i - 1
        l = 6*i + 1
        if is_div(n, m):
            return False
        if is_div(n, l):
            return False
    return True
