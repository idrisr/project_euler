# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np
import math

total = 0
for x in xrange(0, 1000):
	if math.fmod(x, 3) == 0 or math.fmod(x, 5) == 0:
		total += x
print total
 
r = np.array(xrange(0,1000))

np_total = r[np.mod(r, 3)==0].sum() + r[np.mod(r, 5)==0].sum() - r[np.mod(r, 15)==0].sum()
print np_total
