# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

"""
Pick any such m and n, where m > n 
Then this will create a pythagorean triple
a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

a+b+c = 1000:
(2mn) + (2m^2) = 1000
Therefore, the maximum value of m is where n=1,
2m+2m**2 = 1000
2(m+m**2) = 1000
(m**2+m) = 500
m^2 + 2m - 500 = 0
...max of m is somewhere around 30-ish

Therefore only need to test m up to 30 and values of m from 1 to n
"""

def main():
    for m in xrange(1, 30):
        for n in xrange(1, m):
            if  2*m*n + 2*(m**2) == 1000:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                print 'a=%s' % (a)
                print 'b=%s' % (b)
                print 'c=%s' % (c)
                print 'm=%s' % (m)
                print 'n=%s' % (n)
                print 'abc=%r' % (a*b*c)

if __name__ == '__main__':
    main()


