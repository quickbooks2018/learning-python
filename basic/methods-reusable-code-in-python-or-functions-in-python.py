# Method mean reusable code in python

# def add(x,y):
#     result = x+y
#     print('Result of Value x={} + Value y={} is equal to Value={}'.format(x,y,result))
#
# # Call the above function
#
# add(10,20)
#
# add (2,3)

#####################################################

# def add(x,y):
#     result = x+y
#     return result
#
# # call the above function
# result = add(10,20)
# print(result)


#######################################################

# Override the function value

def add(x=5,y=5):
    result = x+y
    return result

# now call the above function by overriding the values

result = add(x=10,y=20)
print(result)