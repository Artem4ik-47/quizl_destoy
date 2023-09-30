def scrnsize():
	prf = open("pref.txt", "r")
	lines = prf.readlines()
	prf.close()
	line = lines[0]
	lstadd = ""
	listoutp = []
	for a in line:
		if a != ",":
			lstadd = lstadd + a
		else:
			lstadd = int(lstadd)
			listoutp.append(lstadd)
			lstadd = ""
	lstadd = int(lstadd)
	listoutp.append(lstadd)
	return listoutp
def delay():
	prf = open("pref.txt", "r")
	lines = prf.readlines()
	prf.close()
	line = lines[1]
	return float(line)