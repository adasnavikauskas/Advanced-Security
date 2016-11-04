m = 11*19
xi = 14

def rng():
	global xi
	xi = (xi) % m
	return xi

for i in range(12):	
	print rng()
