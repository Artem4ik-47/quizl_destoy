def linedit(ln, inp):
	prf = open("pref.txt", "r")
	lines = prf.readlines()
	prf.close()
	lines[ln] = inp
	prf = open("pref.txt", "w")
	for line in lines:
		prf.write(line)
	prf.close()