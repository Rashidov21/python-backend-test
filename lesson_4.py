# if  elif else - instruksiyalari 

# if - agar 
# elif - boshqa bo'lsa , aks holda boshqa 
# else - aks holda , boshqa 

user_age = int(input("Yoshingizni kiriting: "))
if user_age ==  18:        
    print("Assalomu alaykum !")
    name = input("Ismingiz nima ?")
    if len(name) > 3:
        print("Qalaysiz ,", name)
        if name.lower().startswith("a"):
            print("Meni ismim ham A harfi bilan boshlanadi")
elif user_age > 30 and user_age < 60:
    print("Qanday ishda ishlaysiz ?")
elif user_age > 60 and user_age < 100:
    surname = input("Familyangizni kiriting:")
    if surname.endswith("va"):
        print("Yaxshimisz Buvi !")
    else:
        print("Yaxshimisz Bobo !")
else:
    print("Salyut !")
    
# if shart:
#     agar shart True bo'lsa ishlaydigan kod
# elif shart:
#     agar shart True bo'lsa ishlaydigan kod
# else:
#     agar shart False bo'lsa ishlaydigan kod