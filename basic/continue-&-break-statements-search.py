# Continue Statements STOPS the iteration
# Breaks Statments BREAKS completly STOP the loop


# data = [1,2,0,5,10]

# a = 1
# for x in data:
#     a = a*x    # a multiply x ---> note x is every value in array
#    # print('a')
#    # print('The value of a is {}'.format(a))
# print('The value of a is {}'.format(a))

# # In mentioned below loop, if we want to ignore the value of ZERO
#
# data = [1,2,0,5,10]
# a=1
# for x in data:
#     if x == 0:
#         continue
#
#     a = a*x
# print('The value of a is {}'.format(a))

# Break will stop the LOOP
data = [1,2,0,5,10]

search = 0

for x in data:
    if search == x:
        print('Value of search is {}, this is found in array'.format(search))
        break

