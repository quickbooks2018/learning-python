# [] list

data=[1,2,3,0,4,5]

a=1

for i in data:
    if i ==0:
        continue
    a=a*i
    print("The value of is {}".format(a))