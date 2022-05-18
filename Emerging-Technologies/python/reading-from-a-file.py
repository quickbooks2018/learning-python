data = []
f = open('myfile.txt', 'r')  # r is a reade mode
for row in f:
    r = row.strip('\n')
    data.append(r)
f.close()

print(data)