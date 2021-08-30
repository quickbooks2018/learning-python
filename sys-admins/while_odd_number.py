count=5

while count < 10:
    if count % 2 == 0:
        count += 1
        continue                                                # break/continue ---> you can use break by putting odd number vice versa
    print("We are counting odd numbers %s" % count)
    count += 1


# By using break, you can break the loop, if condition met

# By using continue, you can continue in loop, if condition met