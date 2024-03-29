# tuple - o'zgarmas elementlar ketma-ketligi

# t = tuple()
# t = ()

# t = (1,2,3,4,5)
# print(t[2])# 3
# t[2] = 5 # TypeError: 'tuple' object does not support item assignment


# set - unikal tartibsiz elementlar ko'pligi
# s = set()
# s = {1,2,3,4}
# print(set("python programming"))

# frozenset - unikal tartibsiz o'zgarmas elementlar ko'pligi
# print(frozenset("python programming"))

# dict - elementlariga indeks emas balki kalit so'z orqali murojaat qilinadigan to'plam

# d = dict(a=1,b=2)
# print(d)
# d = {"a":1,"b":2,"c":3}
# print(d)
# print(type(d)) # <class 'dict'>

person = {
    "name":"John Doe",
    "age":45,
    "work":"Driver",
    "salary":15000
}
# print(person.get("age")) # 45
# print(person["age"]) # 45

# person["age"] = 30 
# print(person["hobbies"]) # KeyError: 'hobbies'
# print(person)

# dict ustida amallar 
# get - kalit boyicha qiymatni oladi agar bunday element bolmasa None qaytaradi
# print(person.get("hobbies")) # None

# setdefault - korsatilgan kalit ostida element bolsa uni oladi aks holda shunday elementni hosil qiladi 

# print(person.setdefault("work")) # Driver
# print(person.setdefault("hobby","PS5")) #  PS5
# print(person)

# keys - dictni kalitlar ketma-ketligi (dict_keys)
# for i in person.keys():
#     print(i)
# print(person.keys()) # dict_keys(['name', 'age', 'work', 'salary'])
# # values - dictni qiymatlar ketma-ketligi (dict_values)
# for i in person.values():
#     print(i)
# print(person.values()) # dict_values(['John Doe', 45, 'Driver', 15000])
# # items - dictni elementlar ketma-ketligi (tuple)
# for i in person.items():
#     print(i)
# print(person.items()) # dict_items([('name', 'John Doe'), ('age', 45), ('work', 'Driver'), ('salary', 15000)])

# task 
# input:
a = "abcdefgh"
b = list(range(1,9))
# output:
# d = {"a":1,"b":2...}
c = {}
for i in range(len(a)):
    c.setdefault(a[i],b[i])
    
print(c) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

print({k:v for k,v in zip(a,b)}) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
