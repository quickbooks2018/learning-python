# Writing to a file
write_data = ["Alpha", "Beta", 'Gamma']
with open("Greek-letters.txt", 'w') as g:
    for value in write_data:
        g.write(value)
        g.write('\n')  # use to indicate next write statement, starts from next line
g.close()

# Appending to a file
append_data = ['Zeta', "Eta", 'theta']
with open("Greek-letters.txt", 'a') as h:
    for value in append_data:
        h.write(value)
        h.write('\n')
h.close()
