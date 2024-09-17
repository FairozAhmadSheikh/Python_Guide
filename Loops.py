# Syntax for While Loop
value =1
while value<=10:
    print("counter is " +str(value))
    value+=1


# Syntax for For Loop

listed=["ali","hasssan","roz","apple","mango"]
addresses=["gulshan bagh","botakadal","amira kadal","habba kadal","lal bazar"]

for name in listed:
    print(name)

 # Specific range  starts from 0 to 9
for i in range(10):
    print(i)
for i in range(1,4): #starts form 1 to 3
    print(i)

for i in range(5,25,5): # starts from 1 to 100 with itration of +5
    print(i)

# now going for break and continue

for i in range(12):
    if i%2==0:
        continue;
    else:
        print(i)

data=["dave","david","miller"]
addr=["codes","eats","sleeps","repeats same"]
for name in data:
    if name=="david":
        continue;
    else:
        print(name)

# Nested Loops         
for name in data:
    for add in addr:
        print(name +" "+ add+".")