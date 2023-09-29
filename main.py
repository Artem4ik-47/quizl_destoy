import pytesseract
import time
from PIL import ImageGrab
from PIL import Image
import pyautogui
viv = (0, 0, 0)
print("Started")
while viv != (255, 255, 255):
	scrn = ImageGrab.grab(bbox = (285, 320, 2270, 1300))
	msc = scrn.load()
	viv = msc[150, 150]
	#print(viv)
scrn.save("scrnf.png")
start_time = time.monotonic()

ltd = ["белок", "Protein", "газированные напитки", "Fizzy drinks", "мясо ПТИЦЫ", "poultry", "обработанная пища", "processed food", "бобовые", "pulses", "насыщенные жиры, транс Жиры", "saturated fats", "цельнозерновые", "wholegrain", "потреблять", "Consume", "питательные вещества", "Nutrients", "питание", "Nutrition", "уменьшать, сокращать", "reduce", "углеводы", "Carbohydrates", "переваривать", "digest", "зарядиться энергией", "boost energy", "разнообразие", "variety", "содержать", "contain", "клетчатка", "fibre", "избегать", "avoid", "сжигать калории", "burn calories", "оставаться прежним", "remain the same", "оставаться сильным", "stay strong", "Добавки и консерванты", "additives and preservatives", "холестерин", "Cholesterol", "молочные продукты", "dairy products"]
rf = []

my_conf = r"--psm 4 --oem 1"
res = pytesseract.image_to_string(scrn, lang = "rus+eng", config = my_conf)
print(res)
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

d = {"белок": "Protein", "газированные напитки": "Fizzy drinks", "мясо ПТИЦЫ": "poultry", "обработанная пища": "processed food", "бобовые": "pulses", "насыщенные жиры, транс Жиры": "saturated fats", "цельнозерновые": "wholegrain", "потреблять": "Consume", "питательные вещества": "Nutrients", "питание": "Nutrition", "уменьшать, сокращать": "reduce", "углеводы": "Carbohydrates", "переваривать": "digest", "зарядиться энергией": "boost energy", "разнообразие": "variety", "содержать": "contain", "клетчатка": "fibre", "избегать": "avoid", "сжигать калории": "burn calories", "оставаться прежним": "remain the same", "оставаться сильным": "stay strong", "Добавки и консерванты": "additives and preservatives", "холестерин": "Cholesterol", "молочные продукты": "dairy products"}
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
