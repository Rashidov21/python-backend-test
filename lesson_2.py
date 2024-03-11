
# def main(x):
#     return x ** 2

# print(main(2)) # 4

# print(main)  # <function main at 0x000001A5F4968B80>

# x = 10

# O'zgaruvchi bu RAM operativ xotiradagi katakchaga olib boruvchi manzil
# name = "John"


# kun.uz >> 91.190.159.34


# Pythonda o'zgaruvchilarni nomlashda qonun qoidalar 
# 1 - Ingliz tilida (lotin harflari)
# 2 - Mantiqan to'g'ri nom 
# user_name = "John"
# user_surname = "Doe"
# 3 - birinchi belgisi raqam bo'lishi mumkin emas 
# 1user >> xato 
# user1 >> tog'ri
# 4 - faqat lotin harflari , sonlar va _ belgisini ishlatish mumkin xolos 


# Data type  
# int , float , complex 
# str, bool, None

# Data structure 
# list , tuple , dict 
# set, frozenset, range 


# n = 1
# fn = 1.3
# cn = 2n 

# str - belgilar ketma-ketligi 

# text = "Python is better"
# print(text[0]) # ketma-ketlikdagi 1-element
# print(text[-1]) # ketma-ketlikdagi oxirgi element
# print(len(text)) # belgilar sonini butun son qiymatida qaytaradi


# string methods - stringlar ustida bajarish mumkin bo'lgan amallar

# text = "Python is better"
# print(text.title()) # birinchi belgi katta harf
# print(text.upper()) # hammasi katta
# print(text.lower()) # hammasi kichik
# print("javascript".capitalize()) # Javascript

# isalpha - str da barcha belgilar alfavit harflari ekaniga tekshirish
# print("abc".isalpha()) # True
# print("abc12".isalpha()) # False

# isalnum - str da barcha belgilar alfavit harflari va sonlar ekaniga tekshirish
# print("abc12".isalnum()) #True

# isnumeric - faqat son ekaniga tekshirish
# print("abc123".isnumeric()) #False
# print("123".isnumeric()) #True

# isdigit - faqat butun sonlarga tekshirish
# print("1.2".isdigit()) # False
# print("1".isdigit()) # True

# str ni hisoblash metodlari 
# print(len("Python")) # 6
#count - berilgan str da berilgan belgi nechi marta ishtirok etgani qaytaradi
# print("Python,down,town".count("o")) # 3

# print(len("Javascript") + len("is ") + "oooiiioouuii".count("i")) # 18

# belgilarni qidirish 
# print("abc".startswith("c")) # False
# print("abc".endswith("c")) # True

# find - berilgan belgini str dagi indexini qaytaradi 
# print("fortran".find("a")) # 5
# print("fortran"["fortran".find("a")]) # a

# rfind - ongdan chapga qarab

# index - berilgan belgi yoki strni indexini qaytardi
# s1 = "assambler,algol and fortran"
# print(s1.index("and")) #10



# text = "lorem ipsum dolor amet sit"
# split - qatorni siz ko'rsatgan belgi bo'yicha bo'ladi va massiv hosil qiladi
# print(text.split()) #['lorem', 'ipsum', 'dolor', 'amet', 'sit']

# print("as.sa.sa.sa.sa.saaas.sssaa".split("."))
# ['as', 'sa', 'sa', 'sa', 'sa', 'saaas', 'sssaa']

# task 1 
# foydalanuchi matn kiritadi va siz shu matnda nechta soz qatnashganini toping 
# user = input("Matnni kiriting:")
# print(len(user.split()))

# s = "Python programming language"
# print(s.split()[-1]) # language

# print("Akbarova".endswith("va")) # True
# print("Akbarov".endswith("va")) # false

# print("Pythonjon".replace("o","a")) # Pythanjan

# task 2
# qatordagi keraksil belgilarni o'chirib tashlang 
# text = "Pyt$oN# i@s a B^et0Ter"
# >>> "Python is a better"

# res1 = text.replace("$","")
# print(res1) # PytoN# i@s a B^et0Ter
# res2 = res1.replace("#","")
# print(res2) # PytoN i@s a B^et0Te

# print(text.replace("$","").replace("#","").replace("@","").replace("^","").replace("0","").capitalize()) #Pyton is a better


# print(len("a" * 2) * (1 + int("10") - 5) // 2) # 6

