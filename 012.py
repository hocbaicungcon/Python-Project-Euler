# https://www.facebook.com/ProjectEuler/

import math

num_of_divisor = 1

def find_divisor(n):
	divisors = {1}
	max_range = math.floor(math.sqrt(n)) + 1
	for i in range(2, max_range):
			if n % i == 0:
				divisors.add(i)
				divisors.add(n // i)
	return divisors

# print(len(find_divisor(500000000)))

m = 31

while num_of_divisor <= 500:
	n = m*(m+1)//2
	num_of_divisor = len(find_divisor(n))
	m += 1
print(n)

