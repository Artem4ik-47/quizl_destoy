import pytesseract
import time
from PIL import ImageGrab
from PIL import Image
import pyautogui
import codecs
import math
import prefedit
import getpref
viv = (0, 0, 0)

listc = getpref.scrnsize()
dela = getpref.delay()

debug_mode = ""
print("You can use enter to skip dialog")
print("Input p to enter preferences: ", end = "")
pref = input()
if pref == "p":
	print("\n__________PREFERENCES__________")
	print("Input d to enter debug mode: ", end = "")
	debug_mode = input()
	if debug_mode == "d":
		print("You are in debug mode")
	print("#")
	print("Input s to edit clicks delay (now: " + str(dela) + "): ", end = "")
	m_delay = input()
	if m_delay == "s":
		print("Enter delay: ", end = "")
		delayinp = float(input())
		dela = delayinp
		delayinp = str(delayinp)
		prefedit.linedit(1, delayinp)
		print("Done")
	print("#")
	nw = ""
	for cco in listc:
		nw = nw + str(cco) + " "
	nw = nw[:-1]
	print("Input r to edit screenshot box (now: " + nw + "): ", end = "")
	m_scrbox = input()
	if m_scrbox == "r":
		print("Enter screenshot box coordinates: ", end = "")
		listinp = input()
		listinp = listinp.split()
		listc = list(map(int, listinp))
		toline = str(listc[0]) + "," + str(listc[1]) + "," + str(listc[2]) + "," + str(listc[3]) + "\n"
		prefedit.linedit(0, toline)
		print("Done")
	print("_______________________________")
print("Press Enter to start", end = "")
prog = input()
print("Started\n")

while viv != (255, 255, 255):
	scrn = ImageGrab.grab(bbox = (listc[0], listc[1], listc[2], listc[3]))
	msc = scrn.load()
	viv = msc[listc[0], listc[1]]
scrn.save("scrnf.png")

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

rf = []
nows = ""
for now in res:
	if (now != " " or len(nows) > 0) and now != "\n":
		nows += now
	if debug_mode == "d":
		print(nows)
	if nows in ltd:
		rf.append(nows)
		nows = ""

print("==========Recognised words===========\n")
for an in rf:
	print(an)
print("\n=================End=================\n")
it = 0
ans = []
for vv in rf:
	if vv in d:
		it2 = 0
		for vv2 in rf:
			if vv2 == d[vv]:
				ans.append((it, it2))
			it2 += 1
	it += 1

dcl = []
dcl.append((math.floor((listc[2] - listc[0]) / 8) + listc[0], math.floor((listc[3] - listc[1]) / 6) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 3) + listc[0], math.floor((listc[3] - listc[1]) / 6) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 5) + listc[0], math.floor((listc[3] - listc[1]) / 6) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 7) + listc[0], math.floor((listc[3] - listc[1]) / 6) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 3) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 3) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 3) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 5) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 3) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 7) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 3) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 5) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 3) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 5) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 5) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 5) + listc[1]))
dcl.append((math.floor((listc[2] - listc[0]) / 8 * 7) + listc[0], math.floor((listc[3] - listc[1]) / 6 * 5) + listc[1]))
time.sleep(0.005)
for an in ans:
	pyautogui.click(dcl[an[0]])
	time.sleep(dela)
	pyautogui.click(dcl[an[1]])
	time.sleep(dela)
