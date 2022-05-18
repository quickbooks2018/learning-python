filename = "Temperature.csv"
observations = []
count = 0
with open(filename, 'r') as tempfile:
    # Since our first value is header, we used this method to skip it.
    header = tempfile.__next__()
    for row in tempfile:
        # strip removes '\n' at the end of each observation
        observations.append(row.strip('\n'))
        count += 1
tempfile.close()

print(observations)
print('The count of rows is: ', count)
