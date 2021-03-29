# Dictionary in python
# Dictionary is data structure, it is a KEY VALUE architecture.
# Dictionary is equal to maps in java
# Dictionary is also immutable, mean we can update and modify dictionary.

# map example


data={"Apple":30000, "Oranage":50, "Bannana":150}

for x in data.keys():
    print(x)

for y in data.values():
    print(y)

print(data['Apple'])

data['Mangoes'] = 50000

print(data['Mangoes'])