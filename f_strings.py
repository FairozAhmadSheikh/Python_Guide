# # F strings helps us with formating the strings 
# # Traditional Approches first


# person="David"
# coins=10

# # Approach one    %s 
# message="\n name of the person is %s , coins are %s"%(person,coins)
# print(message)

# # Approach second format and {}
# message="\n name of person is {} , coin balance is {}".format(person,coins)
# print(message)

# # Approach Three   index
# message="\n coin balance is {1} , for user {0}".format(person,coins)
# print(message)


# # Approach fourth 
# message="\n name of person is {person} , coin balance is :{coins} ".format(person=person,coins=coins)
# print(message)

# # Access values of a dictionary
# dictionary={
#     "user":"Feroz",
#     "coins":100
# }

# message="\n name of user is {user} , coin balance is ::  {coins}   ".format(**dictionary)
# print(message)
# print("")

title='F-String From Here'

print(title.center(40,"="))

personal="Sheikh Feroz"
coin_bal=6664

message=f"\n {personal} with {coin_bal} Rs"
print(message)

# Dictionary 

dictionary2={
    "personal":"Sameer Mir",
    "coin_bal":774
}

# Access dictionary using f-strings
message=f"\n {dictionary2['coin_bal']}  amount in wallet of {dictionary2['personal']}"
print(message)


# Formatting Options 
num=0

message=f"\n 2.5 times {num} is {2.25 * num :.2f}"
print(message)

# Printing table using f strings and a loop

for num in range(1,11):
    print(f"\n 2 * {num} : {2*num:.2f}")


# Dividing now 

for num in range(1,11):
    print(f"\n {num} divided by 4.52 is {num/4.52:.2%}")