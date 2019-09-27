# factorial with loop
def factorial(n: int):
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result


# factorial with recursion
def factorial_recursion(n: int):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


def factorial_test(func):
    n1 = 0
    if func(n1) == 1:
        print("Test1 passed. Factorial({}) = {}".format(n1, 1))
    else:
        print("Test failed")

    n2 = 1
    if func(n2) == 1:
        print("Test2 passed. Factorial({}) = {}".format(n2, 1))
    else:
        print("Test failed")

    n3 = 2
    if func(n3) == 2:
        print("Test3 passed. Factorial({}) = {}".format(n3, 2))
    else:
        print("Test failed")

    n4 = 5
    if func(n4) == 120:
        print("Test4 passed. Factorial({}) = {}".format(n4, 120))
    else:
        print("Test failed")

    n5 = 6
    if func(n5) == 720:
        print("Test4 passed. Factorial({}) = {}".format(n5, 720))
    else:
        print("Test failed")


factorial_test(factorial)
print("\n")
factorial_test(factorial_recursion)
