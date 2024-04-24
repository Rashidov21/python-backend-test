# time - vaqt uchun 
# datetime - sana va vaqt 
# import datetime
# import time
# import calendar
# Dasturni o'zbek tiliga olish 
# import locale
# locale.setlocale(locale.LC_ALL, "uz-UZ")

# joriy sana va vaqtni olish 
# _now = datetime.datetime.now()
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

# print(_now.strftime("Bugun %d- %B , %Y-yil \nSoat %H dan %M minut o'tdi."))
# Bugun 08- Aprel , 2024-yil 
# Soat 16 dan 26 minut o'tdi.
# while True:
#     _now = datetime.datetime.now()
#     print(_now.strftime("%H:%M:%S"))
#     time.sleep(1)


# timedelta - ikki sana yoki vaqt oraligini hisoblash 

# time1 = datetime.timedelta(days=105,hours=10,minutes=50)
# time2 = datetime.timedelta(days=2,hours=5,minutes=25)
# print(time1 - time2) # 103 days, 5:25:00

# print(datetime.timedelta(weeks=2) - datetime.timedelta(days=10)) # 4 days, 0:00:00

# date - sana obyekti 
# d1 = datetime.date(2024,4,10)
# print(d1) # 2024-04-10

# print(datetime.date.today()) # 2024-04-12
# print(datetime.date.today().year) # 2024
# print(datetime.date.today().month) # 04
# print(datetime.date.today().day) # 12
# print(datetime.date.today().weekday()) # 4
# print(datetime.date.today().strftime("%A").title()) # Juma

# c = calendar.TextCalendar()
# print(c.formatyear(2024))
# print(c.formatmonth(theyear=2024,themonth=4))
# html_calendar = calendar.HTMLCalendar()
# print(html_calendar.formatyear(theyear=2024))
