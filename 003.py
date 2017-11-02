# https://www.facebook.com/ProjectEuler/
import math

n = 600851475143
uoc = 775146

def is_prime(x):
	d = math.floor(math.sqrt(x))
	for i in range(2,d):
		if x % i == 0:
			return False
	return True

# print(is_prime(100))
# print(is_prime(104729))

for i in range(775146,2,-1):
	if is_prime(i):
		if n % i == 0:
			print(i)
			break
