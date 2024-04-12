# function - kod bo'lagi , dasturni istalgan joyidan istalgan marta ishga tushirish mumkin 

# def funktsia_nomi(funktsiya qqabul qiluvchi qiymatlar):
#     funktsiyani tanasi 
#     return funktsiya qaytaruvchi natijani 

# def plus(number_1,number_2):
#     """Return summ of two numbers """
#     result = number_1 + number_2
#     return result

# for i in range(1,11):
#     print(plus(1,i)) 
    
# print(plus.__doc__) # Return summ of two numbers 
# print(plus(5,10)) # 15

# def minus(a,b):
#     return a - b 

# print(minus(10,2)) # 8


# def test(x=1,y=0,z=10):
#     return x

# print(test()) # missing 1 required positional argument: 'x
# print(test(2)) # 2
# print(test()) # 1

# def main_pow(x,y):
#     return x ** y
 
# print(main_pow(2,2)) # 4
# arr = [1,2,3,4,5,6,7,8,9,10]

# def main_pow(*args):
#     print(type(args)) # <class 'tuple'>
#     for i in args:
#         print(i)
        
# print(main_pow(1,2,3,4,"salom",True,7,[1,2,3],9,10))
    

# def check_kwargs(**kwargs):
#     print(type(kwargs)) # <class 'dict'>
#     for i in kwargs.items():
#         print(i)
#     print(kwargs.get("a")) # 1

# print(check_kwargs(a=1,b=2,c=3))

def super_func(*args,**kwargs):
    print(type(kwargs)) # <class 'dict'>
    for i in kwargs.items():
        print(i)
        
    print(type(args)) # <class 'tuple'>
    for i in args:
        print(i)

super_func(1,2,3,a=4,b=5)

# args = arguments 
# kwargs = keyword arguments 
