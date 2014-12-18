def natureGen():
	num = 0
	while True:
		num = num + 1
		yield num
gen = natureGen()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()