data=['John',"doe","Ara","Naya","doe"]
data2=['data',"data good"]


new_data=data.copy()
print(new_data)

data.append("Ali Mohd")
print(data)

data.append(data2)
print(data)

print(data.index("Naya"))
print(str(data.count("doe"))+" Times Found")

data.remove("John")
print(data)

data.pop()
print(data)

# Deletes whole data list
# del data 
# print(data)  # Returns error

# Deletes index 1 for data2 
del data2[1]
print(data2)

list1=["Zaid","ali","Abid"]

list1+=['Feroz']

# Sort in the alphabetic order priority for upper case first
list1.sort()
print(list1)

# Sort in every alphabetic order not priority to only uppercase

list1.sort(key=str.lower)
print(list1)


# Clear a list 
list1.clear()
print(list1)     # Returns empty list


info="Numerical Data Here"
print("")
print(info.center(40,"="))

numbers_list=[99,88,60,555,1070]

print(numbers_list)

# Sorts Numbers in ascending order
numbers_list.sort()
print(numbers_list)

# In decending order
numbers_list.sort(reverse=True)
print(numbers_list)




info="Tupple Data"
# Tuple can not be changed util you have some creativity like below after line Number 79
print("")
print(info.center(40,"="))

tup=(1,1,2,3,4,5,5,6)
print(tup)
print(tup.count(1)," Times Found")

print("Found at index",tup.index(4))

# Indirect operations on Tupples
list_tup=list(tup)
list_tup.append(22)
print(list_tup)

# Now convert back to tuple
# Also known as Packing Tupple
list_tup=tuple(list_tup)
print(type(list_tup))


# Unpacking a tupple

(one,two,three,*remaining)=list_tup
print(one)
print(two)
print(three)
print(remaining)
