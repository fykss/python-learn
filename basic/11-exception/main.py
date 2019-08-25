#  This example opens a file, writes content in the, file and comes out gracefully because there is no problem at all

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()


#  This example tries to open a file where you do not have write permission, so it raises an exception

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")


#  The try-finally Clause

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print("Error: can\'t find file or read data")
