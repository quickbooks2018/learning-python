# {} set
# [] list
          # key value    key value  key value
fruits={ "Apple":40, "Mango":100, "Orange":200 }

# Update the Value of apples in Dictionary
fruits["Apple"] = 500

for i in fruits.keys():         # keys
    print(i)

for i in fruits.values():       # values
    print(i)

ApplePrice=(fruits["Apple"])

print(ApplePrice)

apples="Price of Apple is {}".format(ApplePrice)

print(apples)