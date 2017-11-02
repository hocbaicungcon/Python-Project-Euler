# https://www.facebook.com/ProjectEuler/
import math

def is_prime(n):
	max_range = math.floor(math.sqrt(n))
	for i in range(2, max_range + 1):
		if n % i == 0:
			return False
	return True
# print(is_prime(1001))
counter = 2
current_prm = 3
while counter < 10001:
	current_prm += 2
	if is_prime(current_prm):	
		counter += 1
		print(counter, current_prm)