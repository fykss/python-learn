def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


printme("Vlad")


# Keyword arguments

def printme1(str):
    "This prints a passed string into this function"
    print(str)
    return


printme1(str="My string")


# Default arguments

def printinfo(name, age=35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


printinfo(age=50, name="miki")
printinfo(name="miki")


# Variable-length arguments

def printinfo1(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo1(10)
printinfo1(70, 60, 50)


# The Anonymous Functions

def sum(arg1, arg2): return arg1 + arg2


print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))


# Global vs. Local variables

total1 = 0  # This is global variable.


def sum1(arg1, arg2):
    # Add both the parameters and return them."
    total1 = arg1 + arg2  # Here total is local variable.
    global total2  # Here total is local variable.
    total2 = arg1 + arg2
    print("Inside the function local total : ", total1)
    print("Inside the function local total : ", total2)
    return total1


sum1(10, 20)
print("Outside the function global total : ", total1)
print("Outside the function global total : ", total2)
