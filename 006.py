# https://www.facebook.com/ProjectEuler/
sum_of_square = 0
square_of_sum = 0

for i in range(101):
	sum_of_square += i**2

for i in range(101):
	square_of_sum += i

square_of_sum = square_of_sum**2
print(square_of_sum - sum_of_square)
