# Mutable ---> Modify
# Immutable ---> can not modify

family=["Abujan", "Amijan", "Asim", "Fiza", "Qasim", "2.5", "Pakistan", "Lahore" ]


print(family)


family[5]="Taha"      # List Updated with single item

print(family)


print(len(family))

family[6:]  = ["Zoha", "Hala", "Duwa"]                            # List Updated with multiple items

print(family)

family[0] = []                                                  # Abujan passed away so remove from the list

family[0] = "Abujan"

print(family)

family.remove("Abujan")                                         # This will find the value from the list & remove that value no need to provide index

print(family[1:])                                                # From Index 1 till End


# Append in the list

family.append("Faisalabad")

print(family)


# Adding list with list list + list

family += [50,50]

print(family)

combine_two_lists=family + [10,11]

print(combine_two_lists)