# Global scoped is something that is accessible everywhere
# Local scope is something that is accessible locally like inside function

"""Note : We should always try to keep global space unpolluted that is try to declare variables and things locally mostly when dealing with functions"""

name="IUST"

def name_call():
    return(name)

print(name_call())

# how can we change it from a function inside

def name_changer():
    global name
    name="Awantipora"
    return name;
print(name_changer())


# Nesting Functions 

count=1

def another():
    color="blue"  # we will try to access it from child function
    global count  # here we access global count
    count+=2      # Modifying global count variable 
    print(count)

    def greeting(name):
        nonlocal color # Accessing parent function variable named color
        color="Green"  # Modifying parent function variable
        print(color)
        print(name)
    greeting("Fairoz")
another()