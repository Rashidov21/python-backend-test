# 1-task
#Qoldiksiz bolishni tekshirish
# numbers = ['1', '2', '3', '4', '5', '6', '7']

# for number in numbers:
#     if int(number) % 2 == 0:
#         print(number)
 
# 2-task
#Soz uzunligini tekshirish for yordamida        
# words = ['apple', 'watermelon', 'melon', "banana", 'orange']

# for word in words:
#     if len(word) > 6:
#         print(word)
        
# 3-task
#Diapozon oraligida son chiqarish

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# for number in numbers:
#     if 3 <= int(number) and int(number) <= 7:
#         print(number)


# number = int(input("Soni kiriting: "))

# if number > 0:
#     print("Musbat son!")
# elif number < 0:
#     print('Manfiy son!')
# else:
#     print("Nol soni !")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#     31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#     51, 52, 53, 54, 55, 56
# ]

# juft_sonlar = [son for son in numbers if son % 2 == 0]
# yigindi = sum(juft_sonlar)
# print("Juft onlar royhati" , juft_sonlar)
# print("Yigindisi", yigindi)

# print(sum(range(0,57,2)))

# count = 1
# while count <= 10:
#     if count >= 15000:
#         break
#     count += 1
    
    
    
    
# n = 0
# number = int(input("Soni kiriting(sikl ni tohtatish uchun manfiy son kiriting) "))
# while number >= 0:
#     n += number
#     number = int(input("Soni kiriting(sikl ni tohtatish uchun manfiy son kiriting) "))
# print("Umumiy son yegindisi: ", 
#     n)

    
    
    
    
# import random

# print("men 1 dan 10 gacha son oyladim. Topa olasizmi")
# number_to_guess = random.randint(1,10)
# attempts = 0

# while True:
#     guessed_number = int(input("Soni kiriting: "))
#     attempts += 1
    
#     if guessed_number == number_to_guess:
#         print(f"Tabriklayman!. Siz {attempts} shuncha urinishda topdingiz!")
#         break
        
#     elif guessed_number < number_to_guess:
#         print("O'ylangan son kattaroq.")
        
#     else:
#         print("O'ylangan son kichikroq.")
    
    
    
    
    
    
    
    
    
# import random
# target_password = '1111' 
# chars = "0123456789"


# password = ''


# while password != target_password:
    
#     password = ''.join(random.choice(chars) for _ in range(len(target_password)))
#     print("Generatsiya qilingan parol:", password)

# print("Manbani topilgan parol:", password)
