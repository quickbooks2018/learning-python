products="A,B,C"

type=type(products)


print(type)
print(products)


# Now we will convert string in to a list

productslist=products.split(',')

type2=type(productslist)

#print(type2)

print(productslist)

for data in productslist:
    print(data, len(data))


listdefinition=["C", "B", "T"]

#type3=type(listdefinition)

print(listdefinition)