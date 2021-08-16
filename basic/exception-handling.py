# try:
#     pass
# except:
#     pass
# finally:
#     pass

# {} sets
# [] list

# # No Exception
# try:
#     data={"A":1,"B":2}
#     print(data["A"])
# except:
#     print("Exception in the code")
# finally:
#     print("Finaly called ...")

# # Exception
# try:
#     data={"A":1,"B":2}
#     print(data["T"])       # This key is not available in SET
# except:
#     print("Exception in the code")
# finally:
#     print("Finaly called ...")


# # Exception (Key Exception)
# try:
#     data={"A":1,"B":2}
#     print(data["T"])       # This key is not available in SET
#     print(10/0)
# except KeyError:
#     print("Exception in the code")
# finally:
#     print("Finaly called ...")

# Multiple Except Blocks

# Exception (Key Exception)
try:
    data={"A":1,"B":2}
    #print(data["T"])       # This key is not available in SET
    print(10/0)            # This is Zero Division Error
except KeyError:
    print("Exception in the code")
except ZeroDivisionError:
    print("Zero Division Error")
finally:
    print("Finaly called ...")

