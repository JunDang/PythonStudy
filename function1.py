def clip(lo, x, hi):
	y = max(x, lo)
	z = min(y, hi)
	return z
