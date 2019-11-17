# https://www.geeksforgeeks.org/decorators-in-python/


# First example
# defining a decorator
def hello_decorator(func):

    def wrapper():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")

    return wrapper


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()
print()


# Second example

import time
import math


def calculate_time(func):

    def wrapper(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in:", func.__name__, end - begin)

    return wrapper


@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print("Factorial number:", math.factorial(num))


factorial(10)
print()


# Third example


def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Lead time: {} seconds.'.format(end-start))
    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()
