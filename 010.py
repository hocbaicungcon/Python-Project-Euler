# https://www.facebook.com/ProjectEuler/
import math

sum_of_primes = 2

def is_prime(n):
	max_range = math.floor(math.sqrt(n)) + 1
	for i in range(2, max_range):
		if n % i == 0:
			return False
	return True

for x in range(3,1999999,2):
	if is_prime(x):
		sum_of_primes += x
print(sum_of_primes)