products=["shirts","shoes","caps"]

print(products)

products[1] = "jogers"

print(products)

for data in products:
    print(products,len(data))


products.append("paints")

print(products)

products.insert(0, "For Men")

print(products)

# Take last value from a list

lastvalue=products.pop()
print(lastvalue)

# Clear the list
clear=products.clear()

print(clear)