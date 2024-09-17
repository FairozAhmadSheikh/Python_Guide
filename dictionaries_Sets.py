
mem1={
    "name":"Sheikh Feroz",
    "phone_No":7889521098,
    "age":23
}
mem2={
    "name":"Sameer ahmad",
    "phone_No":7888,
    "age":21
}
data_nested={
      "member1":mem1,
      "member2":mem2    
}

print(mem1)
print(mem2)
print(data_nested)

# printing specific item
print(data_nested["member1"]["name"],",", data_nested["member2"]["name"])

dict={"place":"Srinagar",
      "address":"Botakadal",
      "pin":190011,
      "password":"126eftr"
      }

# Change a value in  dictionary two approaches
dict["pin"]=190023
dict.update({"password":"7006TFF"})

print(dict)

# Print specific values two approaches
print(dict["address"])
print(dict.get('password'))
# Print keys and values and key value pairs as tuples
print(dict.keys())
print(dict.values())
print(dict.items())

# Verify if some key exists in the dictionary

print("place" in dict)
print("phone" in dict)

# Remove items in dictionary

# dict.pop("password")
# print(dict)

# Remove last item added

# dict.popitem()
# print(dict)

# Delete and clear dictionary
dicter={
    "name":"ali abid",
    "age":22
}
print(dicter)
# del dicter["age"]
# dicter.clear()
print(dicter)


print("")

title="Sets start From Here"
print(title.center(40,"="))

# Sets do not allow duplicate values
nums={1,2,3,4,5,6,6}
nums1={1,2,7,8,9}
print(nums)

# Adding value in nums
nums.add(63)
print(nums)

# Everything without duplicates

nums.symmetric_difference_update(nums1)
print(nums)

#Merging Two sets using union

print(nums.union(nums1))

