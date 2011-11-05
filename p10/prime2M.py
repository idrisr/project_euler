#Sum all the primes less than 2,000,000

import sys
import numpy as np
import pdb
path_add = '/home/id/project_euler/util'
sys.path.insert(0, path_add)

# general helper functions I'm starting a library for 
from util import is_prime

def main(ceiling):
    """Tests to see if next number in sequence 6i+-1 is prime"""
    primes = [2, 3]
    i = 1
    switch = True 
    while primes[-1] <= ceiling:
        if switch:
            n = 6*i - 1
            switch = False
        else:
            n = 6*i + 1
            switch = True
            i+=1
        if is_prime(n, primes):
            primes.append(n)
            #print primes[-1]
    return primes

def sieve_eras(limit):
    is_prime = np.ones(limit + 1, dtype=bool)
    for n in xrange(2, int(limit**0.5 + 1.5)):
        if is_prime[n]:
            # keep the first n, its prime
            # the next multiple of n still around is n*n
            # the ::n matches every nth item
            is_prime[n*n::n] = 0
    return np.nonzero(is_prime)[0][2:]

if __name__ == '__main__':
    try:
        ceiling = int(sys.argv[1])
    except NameError, IndexError:
        ceiling = 10
    #primes = main(ceiling)
    #primes.pop(-1)
    # default int32 causes overflow and no error, and wrong answer!
    primes = sieve_eras(ceiling)
    npprimes = np.array(primes, dtype='int64')
    print "sum of primes below:%s is %s" % (ceiling, npprimes.sum())
