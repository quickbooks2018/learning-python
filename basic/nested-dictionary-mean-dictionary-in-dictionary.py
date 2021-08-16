# {} Sets
# [] lists
         # key                  # value
Employee={"Name":"Muhammad Asim","Skills":["AWS","DevOps","Docker"]}

#print(Employee)

# for i in Employee.keys():
#     print(i)
#
# for i in Employee.values():
#     print(i)

value_1=(Employee["Skills"][0])

value_2=(Employee["Skills"][1])

output=("{} {}").format(value_1,value_2)

print(output)

print(Employee["Skills"][0:1])

print(Employee["Skills"][::2])