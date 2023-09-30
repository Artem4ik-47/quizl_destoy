import pytesseract
import time
from PIL import ImageGrab
from PIL import Image
import pyautogui
import codecs
viv = (0, 0, 0)

dela = 0.1
listc = []
sccf = open("pref.txt", "r")
plines = sccf.readlines()
scc = plines[0]
lstadd = ""
for smb in scc:
	if smb != ",":
		lstadd = lstadd + smb
	else:
		lstadd = int(lstadd)
		listc.append(lstadd)
		lstadd = ""
lstadd = int(lstadd)
listc.append(lstadd)
lstadd = ""
sccf.close()
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
	print("Input s to manual edit clicks delay (basic: 0.1): ", end = "")
	m_delay = input()
	if m_delay == "s":
		print("Enter delay: ", end = "")
		dela = float(input())
		print("Done")
	print("#")
	nw = ""
	for cco in listc:
		nw = nw + str(cco) + " "
	nw = nw[:-1]
	print("Input r to change screenshot box (now: " + nw + "): ", end = "")
	m_scrbox = input()
	if m_scrbox == "r":
		print("Enter screenshot box coordinates: ", end = "")
		listinp = input()
		listinp = listinp.split()
		listc = list(map(int, listinp))
		sccf = open("pref.txt", "r")
		plines = sccf.readlines()
		sccf.close()
		plines[0] = str(listc[0]) + "," + str(listc[1]) + "," + str(listc[2]) + "," + str(listc[3]) + "\n"
		sccf = open("pref.txt", "w")
		for cline in plines:
			sccf.write(cline)
		sccf.close()
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
	time.sleep(dela)
	pyautogui.click(dcl[an[1]])
	time.sleep(dela)
