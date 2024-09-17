import math
# #Fake Database
# username_db="feroz"
# password_db="1234"

# #Maximum attempts
# max_chances=4
# min_chance=1

# while min_chance<max_chances:
#     username=input("Enter Username : ");
#     password=input("enter Your Password : ");
#     if username==username_db and password==password_db:
#         print("Login Successful ")
#         break;
#     else:
#         print("Invalid Credentials Attempts left : ",max_chances-min_chance)
#         min_chance+=1
#     if min_chance==max_chances:
#         print("dafa javo ")
    

sentance="I love eou"    
print(sentance.title())
print(sentance.replace("eou",'you'))

print("")
title="PARSA'S"
print(title.center(20,"="))
print("Momo".upper().ljust(16,".")+"$1".rjust(4))
print("idli".upper().ljust(16,".")+"$2".rjust(4))
print("khuska".upper().ljust(16,".")+"$3".rjust(4))
print("Rice".upper().ljust(16,".")+"$3".rjust(4))

# Complex Type in Engineering
cmp_no=19+16j;
print(type(cmp_no))
print(cmp_no.imag)
print(cmp_no.real)



#Built in Functions for numbers

number=5.28
print(abs(number)) # Absolute number
print(round(number)) # Rounds to nearest integer
print(round(number,1))


# Math Functions for numbers

print(math.sqrt(64))
print(math.floor(number))
print(math.ceil(number))

# Casting a string to number
zipcode="190011"
print(type(zipcode))

casted=int(zipcode)
print(type(casted))
