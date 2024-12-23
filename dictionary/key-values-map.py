# dictionary in python is a key-value pair
# key is unique and immutable
# value can be any data type
# key-value pair is separated by colon(:)
# dictionary is mutable means we can change the value of key or add new key-value pair

data = {"Apple": 10, "Banana": 20, "Orange": 30}

data["Mango"] = 40

# Iterate over dictionary keys
for i in data.keys():
    print(i)

# Iterate over dictionary values
for j in data.values():
    print(j)

print('end of program')
