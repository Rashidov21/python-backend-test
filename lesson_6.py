# for - takrorlanish (loop) 

# print(1)

# text = "python"
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])

# for i in text:
#     print(i)

# range - sonlar diapazoni - oralig'i (ketma-ketlik)
# range - start,stop,step 
# start - sonlar oraligini boshi 
# stop - sonlar oraligini oxiri
# step - oraliq sonlarni qadamlari 

# print(range(10)) # range(0, 10)
# print(type(range(10))) # <class 'range'>
# print(dir(range(10)))

# for i in range(10):
#     print(i, end=" ")
    
# sum - ketma-ketlik sonlarni yig'inisini qaytaradi
# print(sum((1,2,3))) # 6

# print(sum(range(2,8,2))) # 12
# count = 0
# for i in range(1,6):
#     count += 1
#     for x in range(10):
#        count += 1
#        if count == 50:
#            print("50 ta takrorlanish")
# print(count) # 55


# for x in range(5):print(x)
# for l in "Salom":
#     print(l)
#     if l == "o":
#         print("O topildi")
# else:
#     print("Sikl tugaganidan song ishlaydigan kod")

# n = 0
# for x in range(5):
#     n += x 
#     print(n)
# else:
#     print(n * 2)

# task 1 
# 1 dan 56 gacha bo'lgan sonlar ichida faqat juft sonlarni yig'indisini hisoblang

# task 2 
# "olomomo" so'zida nechta o harfi bor ekanini for sikli yordamida hisoblang

print("olomomo".count("o"))
count = 0
for i in "olomomo":
    if i == "o":
        count += 1
        
print(count) # 4