# https://www.facebook.com/ProjectEuler/
for a in range(3, 995):
	for b in range(a+1, 995):
		if 1000*a+1000*b-a*b==500000:
			print(a, b, 1000 - a - b)
			print(a*b*(1000 - a - b))