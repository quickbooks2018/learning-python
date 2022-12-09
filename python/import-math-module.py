import math
import random

n1 = int(input('Enter fist number, must be integer: '))

n2 = int(input('Enter fist number, must be integer: '))

n3 = n1 + n2

print(n1)
print(n2)
# spacing
print()
print(f'Sum of n1 & n2 is {n3}')
print('Sum of n1 and n2 is:', n1+n2)
print('Multiple of n1 and n2 is:', n1*n2)
# Generating random numbers
print()
print('Generating random number between 0-20, to perform mathematical operations')
random_numbers = random.randint(0,20)
print()
print(f'Random number generated is: {random_numbers}')
print()
print('Factorial of random number is:', math.factorial(n3))
print()
print('Square of randon number:', math.pow(random_numbers,2))
