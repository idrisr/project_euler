#Sum all the primes less than 2,000,000

import sys
import numpy as np
import pdb
path_add = '/home/id/project_euler/util'
sys.path.insert(0, path_add)

# general helper functions I'm starting a library for 
from util import is_prime

def main():
    """Tests to see if next number in sequence 6i+-1 is prime"""
    primes = [2, 3]
    i = 1
    switch = True 
    while primes[-1] <= 2*10**6:
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
    primes.pop(-1)
    primes = np.array(primes)
    print primes.sum()



