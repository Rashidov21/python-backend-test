# for loop tasks

# k = 10
# n = 5

# for i in range(n):
#     print(k)
    
# task 2 
# a = int(input("A ni kirit"))
# b = int(input("B ni kirit"))
# count = 0
# if a < b:
#     for i in range(a,b+1):
#         print(i)
#         count += 1
#     print("Barcha sonlar ", count)
#     print("Barcha sonlar len orqali ", len(range(a,b+1)))

# task 4
# price = 15000
# for i in range(1,11):
#     print(i * price)

# task 5 
# userdan matn qabul qiling toki "z" harfi topilmagunicha barcha harflarini ekranga chiqaring
# input >> 'keldizku'
# output >> k,e,l,d,i,z

# text = input("Matn kirit \n")
# i = 0
# while i <= (len(text) - 1):
#     print(text[i])
#     i += 1
#     if text[i] == "z":
#         break
#***** task 1 ******
# 10 ta 2 xonalik butun son berilgan ulardan faqat 0 bilan tugaganlarini summasini hisoblang
import random 
nums = []
for i in range(10):
    nums.append(random.randint(10,99))

print(nums)
summa = 0
for x in nums:
    if str(x)[1] == "0":
        summa += x 
print(summa)
    


#***** task 2 ******
# stringda son berilgan  siz shuday kop xonali sonlarni xonalarini alohida alohida qilib oralarida bo'sh joylar bilan chiqaring
# input:"1437239000"
# output:1 437 239 000

#***** task 3 ******
# a = [1, 2, 4, 65, 8, 8, 6, 2, 6, 2, 2, 3]
# b = [4, 5, 65, 7, 98, 5, 12, 2, 65, 89, 47]
# ushbu massivlarda ishtirok etgan sonlardan iborat massiv hosil qiling
# hosil bo'lgan massivda faqat sondan bitta bo'lishi kerak , ya'ni massiv elementlari