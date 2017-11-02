# https://www.facebook.com/ProjectEuler/
def is_pal(n):
	n = str(n)
	# num_digits = len(n)
	if n == n[::-1]:
		return True
	else:
		return False
list_pal = []
for i in range(999,100,-1):
	for j in range(999,100,-1):
		if is_pal(i*j):
			list_pal.append(i*j)

print(max(list_pal))
