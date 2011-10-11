# Consider the terms in the Fibonacci sequence starting with 1, 2...
# Sum the even ones whose value does not exceed four million

import math

#% timeit brute = 67.1 micro seconds
def brute():
	x1 = 1
	x2 = 2
	total_even = 0
	while x2 <= 4000000:
		temp = x2
		x2 = x1 + x2
		x1 = temp
		if math.fmod(x1, 2) == 0:
			total_even += x1
	return total_even

# Uses idea that every 3rd member is even	
# %timeit smart = 15.5 micro seconds
def smart():
	x = y = 1
	sum = 0
	while (sum < 4000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum

def main():
	print smart()
	print brute()

if __name__ == '__main__':
	main()
