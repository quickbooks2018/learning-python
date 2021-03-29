# What is exception?
# Exception mean an error occur at the execution of a code, which stops the execution of a code

# For example terraform unable to read from state file

# try:
#     pass
# except:
#     pass
# finally:
#     pass

# No Exception
# try:
#     data= {'A':1,'B':2}
#     print(data['A'])
# except:
#     print('Exception in the code')
# finally:
#     print('Finally Called ...')

# Exception Note: finally block will always execute, here we are using a Key, which is not present in dictionary
# try:
#     data={'A':1,'B':2}
#     print(data['C'])
# except:
#     print('Exception in the code')
# finally:
#     print('Finally Called ...')

# Key Error & ZeroDivision Error
try:
    data={'A':1,'B':2}
   # print(data['C'])
    print(10/0)
except KeyError:
    print('Exception in the code')
except ZeroDivisionError:
    print('Zero Division Error Asim')
finally:
    print('Finally Called ...')



