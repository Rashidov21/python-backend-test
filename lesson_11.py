# cut - qirqish 
# arr = [1,2,3,4,5]
# print(arr[:3]) # [1, 2, 3]

# arr_2 = arr[2:4]
# print(arr_2) # [3, 4]

# # arr[start_index:end_index] 
# print("programming"[4:8]) # ramm
# print("teskari"[::-1]) # irakset

# append - list oxiriga element qoshish 
# arr = [1,2,3]
# arr.append(4)
# print(arr) # [1, 2, 3, 4]

# extend - listni boshqa bir list bilan kengaytirish
# a = ["a","b","c"]
# b = [1,2,3]
# a.extend(b)
# print(a) # ['a', 'b', 'c', 1, 2, 3]

# insert - siz korsatgan elementni siz korsatgan indexga joylaydi
# a = ["a","b","c"]
# a.insert(1,"b") # 1 indexga "b" qoshiladi
# print(a) # ['a', 'b', 'b', 'c']

# pop - list elementlarini index boyicha ochirish uchun 
# a = ["a","b","c"]
# a.pop() # oxirgi elementni ochirish 
# a.pop(1) # 1 - indexdagi elementni ochirish 
# print(a) # ['a']

# remove - korsatilgan elementchi ochiradi
# a = ["a","b","c"]
# a.remove("b")
# print(a) #['a', 'c']

# clear - listni tozalaydi
# a = ["a","b","c"]
# a.clear()
# print(a) # []

# index - siz korsatgan elementni indexini qaytaradi
# a = ["a","b","c"]
# print(a.index("c")) # 2
# print(a.index("a")) # 0
# print(a.index("a") + 2) # 2

# count - siz korsatgan elementni listda nechta ekanini qaytaradi

# arr = [1,22,3,1,54,3,21,1,3,1,2]
# print(arr.count(1))# 4

# print("ananas".count("a")) # 3

# any - listni qabul qilib ichida bir dona bo'lsa ham True qiymat bo'lsa True aks holda False qaytaradi
# a = [0,"",45,False]
# print(any(a)) # True

# all - listni qabul qilib ichida barcha elementlar True bolsa True qaytaradi aks holda False 
# print(all([1,2,0])) # False
# print(all([1,2,3])) # True

# reverse - listni teskari qilish 
# arr = [1,2,3]
# arr.reverse()
# print(arr) #[3, 2, 1]

# sort - list elementlarini saralash

# arr = [1,22,3,1,54,3,21,1,3,1,2]
# arr.sort()
# print(arr) # [1, 1, 1, 1, 2, 3, 3, 3, 21, 22, 54]
# arr.sort(reverse=True)
# print(arr) # [54, 22, 21, 3, 3, 3, 2, 1, 1, 1, 1]

# sorted - ketma-ketlik elementlarini saralash

# students = [
#     ["John","A",16],
#     ["Mike","B",18],
#     ["Sara","C",12],
#     ["David","A",13],
# ]

# print(sorted(students,reverse=True, key=lambda item:item[2]))

# text = "python"

# sorted_text = sorted(text)
# result = "".join(sorted_text)
# print(result) # hnopty


# print("".join(sorted(list(text)))) # hnopty

# task 
# 1 dan 50 gacha bolsan sonlar ichida 5 ta tasodify sondan iborat list hosil qiling 
# va ularni kamayish tartibida saralab ekranga chiqaring 
import random
nums = []

for i in range(5):
    n = random.randint(1,50)
    nums.append(n)
print(sorted(nums, reverse=True))
# task 
# "Assalomu alaykum" - ushbu satr elementlarini alfavit harflari tartibida saralang
# va barcha "a" harflarini o'chirib yuboring

# task 
text = "Assalomu alaykum"
text = sorted(list(text))
result = []
for i in text:
    if i.lower() == "a":
        continue
    else:
        result.append(i)
print("".join(result))   # kllmmossuuy 