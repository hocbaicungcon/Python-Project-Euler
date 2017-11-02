# https://www.facebook.com/ProjectEuler/
result = 0
a = 1
b = 2
while b < 4000000:
	if b % 2 == 0:
		result += b
	a, b = b, a+b
	# print(b)
print(result)
