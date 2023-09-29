from PIL import Image
def ksf(x, ys, yf, np, msc):
	xf = x
	ff = (255, 255, 255)
	while ff[0] > 230 and ff[1] > 230 and ff[2] > 240:
		for i in range(ys, yf):
			ff = msc[xf, i]
			if ff[0] < 230 and ff[1] < 230 and ff[2] < 240:
				break
		if np == "F":
			xf += 1
		else:
			xf -= 1
	if np == "F":
		xf -= 4
	else:
		xf += 4
	return xf
def kud(y, xs, xf, np, msc):
	yf = y
	ff = (255, 255, 255)
	while ff[0] > 230 and ff[1] > 230 and ff[2] > 240:
		for i in range(xs, xf):
			ff = msc[i, yf]
			if ff[0] < 230 and ff[1] < 230 and ff[2] < 240:
				break
		if np == "D":
			yf += 1
		else:
			yf -= 1
	if np == "D":
		yf -= 4
	else:
		yf += 4
	return yf
def krt(xs, xf, ys, yf, nmb, scrn, msc):
	xxs = ksf(xs, ys, yf, "F", msc)
	xxf = ksf(xf, ys, yf, "R", msc)
	yys = kud(ys, xxs, xxf, "D", msc)
	yyf = kud(yf, xxs, xxf, "U", msc)
	#print(xxs, end = " ")
	#print(yys, end = "\n")
	#print(xxf, end = " ")
	#print(yyf, end = "\n")
	t = scrn.crop((xxs, yys, xxf, yyf))
	width, height = t.size
	#t = t.resize((int(0.7 * width), int(0.7 * height)))
	t.save("t" + nmb + ".png")