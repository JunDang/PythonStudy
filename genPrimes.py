def genPrimes():
	primes = [2]
	while True:
		num = primes[-1]
		while True:
			num = num + 1
			divided = False
			for p in primes:
				if num % p == 0:
					divided = True
					break
			if not divided:
				break
		yield num
		primes.append(num)

gen = genPrimes()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
print gen.next()
