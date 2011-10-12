# What is the largest prime factor of the number
# 600851475143
import math

def find_divisor(n):
	i = 3
	while i < n/2:
		if math.fmod(n, i) == 0:
			print 'i:%r n:%r' % (i, n,)
			find_divisor(n/i)
		i += 2

def dumb_divisor(n):
	i = 3
	while i < n/2:
		if math.fmod(n, i) == 0:
			n = n / i
			print 'i:%r n:%r' % (i, n,)
		i += 2

def main():
	divs = []
	n = 600851475143
	#div = find_divisor(n)
	#divs.append(div)
	dumb_divisor(n)

if __name__ == '__main__':
	main()
