# Dictionary is a key value pair

# {} sets

# [] list or array

# Dictionaries order is not guaranteed

# Dictionaries are mutable, which means you can modify dictionary.

ages={"Qasim":38, "Asim":39}

print(ages)

Qasim_age=ages["Qasim"]

print(Qasim_age)


# Update the Dictionaries

ages["Asim"] = 40             # Asim age is updated

print(ages)

# Deletion in Dictionaries
#del ages["Qasim"]

print(ages)

# You can use POP to the value from list

# Remove_Asim=ages.pop("Asim")
#
# print(Remove_Asim)

ages.pop("Asim")

print(ages)