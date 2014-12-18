def recurPower(base, exp):
	if exp == 0:
		return 1
	elif exp > 0 and exp % 2 == 0:
		return base*base*recurPower(base*base, (exp-1)/2)
	elif exp > 0 and exp % 2 != 0:
		return base*recurPower(base, exp-1)
print recurPower(2, 4)