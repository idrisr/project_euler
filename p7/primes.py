"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

import math

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

def main():
    """Tests to see if next number in sequence 6i+-1 is prime"""
    primes = [2, 3]
    i = 1
    switch = True 
    while len(primes) < 10001:
        if switch:
            n = 6*i - 1
            switch = False
        else:
            n = 6*i + 1
            switch = True
            i+=1
        if is_prime(n, primes):
            primes.append(n)
    return primes
        
if __name__ == '__main__':
    primes = main()
    print 'The 10001st prime is: %r' % (primes[-1])
