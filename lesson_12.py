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
print(person.get("age")) # 45
print(person["age"]) # 45