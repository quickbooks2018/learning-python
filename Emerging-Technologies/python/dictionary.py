dictionary = {key: value for key, value in [['Apple', 12], ['Orange', 20], ['Banana', 24]]}

print(dictionary)

print(dictionary['Apple'])

print(dictionary['Orange'])

print(dictionary['Banana'])

dictionary['Peach'] = 32

print(dictionary)

print(dictionary['Peach'])

# 2nd dictionary Vegetable list

vegetables = {'Potato': 12, 'Tomato': 24, 'Peach': 1}

# Merge two dictionaries

dictionary.update(vegetables)

print(dictionary)