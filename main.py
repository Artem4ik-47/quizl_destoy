import pytesseract
import time
from PIL import ImageGrab
from PIL import Image
import pyautogui
import codecs
viv = (0, 0, 0)
print("Started")
while viv != (255, 255, 255):
	scrn = ImageGrab.grab(bbox = (285, 320, 2270, 1300))
	msc = scrn.load()
	viv = msc[150, 150]
	#print(viv)
scrn.save("scrnf.png")
start_time = time.monotonic()

ltd = []
d = {}
dfile = codecs.open("dict.txt", "r", encoding = "utf-8")
lines = dfile.readlines()
for line in lines:
	nl = line.strip()
	j = 0
	word = ""
	while nl[j] != ':':
		word = word + nl[j]
		j += 1
	j += 1
	defi = nl[j:]
	ltd.append(word)
	ltd.append(defi)
	d[word] = defi
dfile.close()

my_conf = r"--psm 4 --oem 1"
res = pytesseract.image_to_string(scrn, lang = "rus+eng", config = my_conf)
print(res)

rf = []
nows = ""
for now in res:
	if (now != " " or len(nows) > 0) and now != "\n":
		nows += now
	print(nows)
	if nows in ltd:
		rf.append(nows)
		nows = ""

end_time = time.monotonic()
vivtime = float(end_time - start_time)
vivtime = round(vivtime, 3)
print(vivtime)

for an in rf:
	print(an)
it = 1
ans = []
for vv in rf:
	if vv in d:
		it2 = 1
		for vv2 in rf:
			if vv2 == d[vv]:
				ans.append((it, it2))
			it2 += 1
	it += 1

dcl = {1: (300, 400), 2: (800, 400), 3: (1400, 400), 4: (1900, 400), 5: (300, 790), 6: (800, 790), 7: (1400, 790), 8: (1900, 790), 9: (300, 1170), 10: (800, 1170), 11: (1400, 1170), 12: (1900, 1170)}
time.sleep(0.005)
for an in ans:
	pyautogui.click(dcl[an[0]])
	time.sleep(0.075)
	pyautogui.click(dcl[an[1]])
	time.sleep(0.075)
