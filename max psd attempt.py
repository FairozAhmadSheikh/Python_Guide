# # #Fake Database
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
#     if min_chance>max_chances:
#         print("contact Admin! ")


# LMS
print("")
print("welcome to our Library!".center(40,"="))
print("Genere of Books".ljust(14,"."))
print("\n 1 for Medical \n 2 For Engineering \n 3 for Arts ")

choice=int(input("Enter your choice : "))

Medical=["Human Anatomy", "physiology","Bones"]
Engineering=["Python", " Earth science ","Mechanis"]
Arts=["Sociology","Eniviornment Science","Political science"]

if choice==1:
    for i in Medical:
        print(i)
    selc=input("Enter which you want to issue :")
    for i in range(len(Medical))
elif choice==2:
    for i in Engineering:
        print(i)
      
    
elif choice==3:
    for i in Arts:
        print(Arts)
      
   
        

