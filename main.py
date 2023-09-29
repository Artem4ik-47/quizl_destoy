import easyocr
import pposs
import time
from PIL import ImageGrab
from PIL import Image
import pyautogui
rdr = easyocr.Reader(["ru", "en"], gpu = False)
viv = (0, 0, 0)
print("Started")
while viv != (255, 255, 255):
	scrn = ImageGrab.grab()
	msc = scrn.load()
	viv = msc[1130, 1010]
	#print(viv)
scrn.save("scrnf.png")
scrn = Image.open("scrnf.png")
msc = scrn.load()
start_time = time.monotonic()

rf = []
pposs.krt(285, 285 + 460, 380, 420, "1", scrn, msc)#1st LINE
res = rdr.readtext("t1.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(785, 785 + 480, 380, 420, "2", scrn, msc)
res = rdr.readtext("t2.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(1290, 1290 + 480, 385, 420, "3", scrn, msc)
res = rdr.readtext("t3.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(1795, 1795 + 480, 380, 420, "4", scrn, msc)
res = rdr.readtext("t4.png", detail = 0, paragraph = True)
rf = rf + res

pposs.krt(285, 285 + 460, 770, 805, "5", scrn, msc)#2nd LINE
res = rdr.readtext("t5.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(785, 785 + 480, 770, 805, "6", scrn, msc)
res = rdr.readtext("t6.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(1290, 1290 + 480, 770, 805, "7", scrn, msc)
res = rdr.readtext("t7.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(1795, 1795 + 480, 770, 805, "8", scrn, msc)
res = rdr.readtext("t8.png", detail = 0, paragraph = True)
rf = rf + res

pposs.krt(285, 285 + 460, 1150, 1185, "9", scrn, msc)#3rd LINE
res = rdr.readtext("t9.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(785, 785 + 480, 1150, 1185, "10", scrn, msc)
res = rdr.readtext("t10.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(1290, 1290 + 480, 1150, 1185, "11", scrn, msc)
res = rdr.readtext("t11.png", detail = 0, paragraph = True)
rf = rf + res
pposs.krt(1795, 1795 + 480, 1150, 1185, "12", scrn, msc)
res = rdr.readtext("t12.png", detail = 0, paragraph = True)
rf = rf + res
end_time = time.monotonic()
vivtime = float(end_time - start_time)
vivtime = round(vivtime, 3)
print(vivtime)

d = {"белок": "Protein", "газированные напитки": "Fizzy drinks", "МЯСО ПТИЦЫ": "poultry", "обработанная пища": "processed food", "бобовые": "pulses", "насыщенные жиры, транс жиры": "saturated fats", "цельнозерновые": "wholegrain", "потреблять": "Consume", "питательные вещества": "Nutrients", "питание": "Nutrition", "уменьшать; сокращать": "reduce", "углеводы": "Carbohydrates", "переваривать": "digest", "зарядиться энергией": "boost energy", "разнообразие": "variety", "содержать": "contain", "клетчатка": "fibre", "избегать": "avoid", "сжигать калории": "burn calories", "оставаться прежним": "remain the same", "оставаться сильным": "stay strong", "Добавки и консерванты": "additives and preservatives", "холестерин": "Cholesterol", "молочные продукты": "dairy products"}
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
