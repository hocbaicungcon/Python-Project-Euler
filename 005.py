# https://www.facebook.com/ProjectEuler/
check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
max_divisior = len(check_list)
for i in range(1, max_divisior):
	for j in range(1, i):
		if check_list[i] % check_list[j] == 0:
			check_list[j] = 1
print(check_list)


def com_div(a, b):
	while a != b:
		if a > b:
			a, b = b, a-b
		else:
			a, b = a, b-a
	return a

# print(com_div(125,75))

n = 1
for i in check_list:
	if n % i != 0:
		n = n*i // com_div(n,i)
print(n)
