# time - vaqt uchun 
# datetime - sana va vaqt 
import datetime
import time
# Dasturni o'zbek tiliga olish 
import locale
locale.setlocale(locale.LC_ALL, "uz-UZ")

# joriy sana va vaqtni olish 
_now = datetime.datetime.now()
# print(_now) #2024-04-08 15:59:06.141114
# for action in dir(_now):
#     print(action)
# print(_now.today())
# print(_now.year)
# print(_now.month)
# print(_now.day)
# print(_now.hour)
# print(_now.minute)
# print(_now.second)

# birthday = datetime.date(2005,6,7)
# print(_now.year - birthday.year) # 19

# strftime - vaqtni str ko'rinishda olish 

# print(_now.strftime("%Y-%m-%d")) # 2024-04-08
# print(_now.strftime("%H:%M:%S")) # 16:39:17
# print(_now.strftime("%A")) # Monday
# print(_now.strftime("%a")) # Mon

print(_now.strftime("Bugun %d- %B , %Y-yil \nSoat %H dan %M minut o'tdi."))
# Bugun 08- Aprel , 2024-yil 
# Soat 16 dan 26 minut o'tdi.
while True:
    _now = datetime.datetime.now()
    print(_now.strftime("%H:%M:%S"))
    time.sleep(1)
    