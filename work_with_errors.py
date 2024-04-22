# Syntax - yozishda xatolik
# Logical - mantiqiy xatolar
# Runtime - dastur ishlash vaqtida vujudga keladigan xatolar

# print "salom" - 2 versiya 
# print() - 3 verisiya 

# print("salom" + 10) # TypeError: can only concatenate str (not "int") to str
try:
    print("salom" + 10)
except Exception as error:
    print(f"Xato bor ! {error}")
else:
    print("Xatolik yoq, davom etish mumkin.")
finally:
    print("Xato bormi yoqmi farqi yoq ishlayi")


# try:
#     xatolik vujudga kelishi mumkin bolgan kod
# except:
#     xatolik bolsa ishlaydigan kod 
# else:
#     xatolik bolmasa ishlaydigan kod 
# finally:
#     xato bormi yoqmi farqi yoq ishlayidigan kod