"""   Functions
Functions are Resuable peices of code 
Functions sometimes receive data and this data is called parameter if it is passed at function decleration,
Arguments : are the values to the function when called 
Note : Parameters can not change Whereas Arguments can change 
"""
# Simple greeting function
name = input("Enter Your name please: ") or "Asif"
def hello():
    return "Hello World"+"  "+name
print(hello())
# Addition function 
def addition(num1,num2):
    sum1=num1+num2
    return sum1;
print("The sum of the numebers is ",addition(10,45))



# Handling the case of strings instead of numbers early returns and passing default params value

def sub(num1=0,num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0; # early return
    return num1-num2;

print(sub(10,49))
print(sub())
print(sub("a",20))


# If we are unsure about how many params we will be using in our function we handle that as shown below by :    *(name of params) 
# Here data would be stored in the tuple  

def multiple_data(*args):
    print(type(args))
    return args;

print(multiple_data("John","Doe","Kenedy"))

# We can also store data in dictionary format using **(name of params   generally kwargs)


def mult_named(**kwargs):
    print(type(kwargs))
    return kwargs
print(mult_named(first="Feroz", last="Sheikh", between="Ahmad"))