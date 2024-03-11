# task 1 
# num = int(input("Son kiriting :"))
# if num < 0:
#     num += 1
#     print(num)
# else:
#     print(num)
    
    
# task 2 
# n = 10
# if n < 0:
#     n += 1
# elif n == 0:
#     n = 10
# else:
#     n -= 2
# print(n)

# task 3
# userdan obhavo haroratini butun sonda qabul qiling , agar harorat 20 baland bolsa "Issiq"
# aks holda "Biroz sovuq" matni ekranga chiqsin
# temp = int(input())
# if temp > 20:
#     print("Issiq")
# else:
#     print("Biroz sovuq")
    
# task 4 
# userdan matn qabul qiling agar matnda yoki so'zda "o" harfi qatnashgan bo'lsa "a" harfiga
# almashtiring
# input : >> olma
# output: alma
# print("olma".replace("o","a")) # alma
# word = input("Sozni kiriting")
# if "o" in word:
#     result = word.replace("o","a")
#     print(result)

# task 5
# userdan so'z qabul qiling agar sozda son ishtirok etgan bolsa ekranga "True" chiqadi
# aks holda so'zni o'zi ekranga chiqadi 
# input : >> apple1
# output: True
# input : >> apple
# output: apple
# word = input("Sozni kiriting \n:")
# if word.isalnum(): # soz va sonlardan iborat matn
#     print("true")
# if word.isalpha(): # faqat alfavit harflaridan iborat matn
#     print(word)
    

# print(any([x.isdigit() for x in list(word)]))