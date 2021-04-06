#!/usr/bin/python3
'''
Note: sys.argv[0] is always the name of the script, regardless of the invocation
a. Create the script and import the sys module

'''

# Modules
import sys



# Fail to run if sys.args < 2
if len(sys.argv) < 2:
    print("AT LEAST ONE PARAMETER IS REQUIRED")
    exit(2)

# RUN Script
print(sys.argv)  # List of CLI Args
print(len(sys.argv)) # print NUM of sys.argv elements




# End