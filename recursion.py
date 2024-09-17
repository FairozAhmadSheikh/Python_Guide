# Recursion means function calling itself repeatedly untill a specific condition gets full filled example below 


def add_one(num1):
    if num1>=9:
        return num1+1;
    total = num1+1
    print(total)
    return add_one(total)  # Recursive call
total_value=add_one(0)     
print(total_value)      # Returns 10 



# Complex Issue for my mind 

value ="u"
count=0;

while value:
    count+=1;
    print(count)
    if count==5:
        break;
    else:
        value=0
        continue