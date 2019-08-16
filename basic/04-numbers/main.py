import random
import math

number = 10

del number

# Number Type Conversion

str = "1"

if str.isdigit():
    print(int(str))
else:
    print(str, " isn't digit")


# Random Number Functions

print(int(math.ceil(random.random() * 10)))
