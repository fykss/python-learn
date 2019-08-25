import math
import random

print("Let the game begin!")

random_number = int(math.ceil(random.random() * 100))
name = input("Enter your name: ")
user_number = ""
history_number = []

print(random_number)

while random_number != user_number and user_number != int:
    try:
        user_number = int(input("Enter your number from 1 to 100: "))
    except ValueError:
        print("That not an int! Try again.")
        continue

    history_number.append(user_number)

    if user_number < random_number:
        print("Your number is too small. Please, try again.")
    elif user_number > random_number:
        print("Your number is too big. Please, try again.")

print("Congratulations, {name}!".format(name=name))
print("Your numbers: {history_number}".format(
    history_number=sorted(history_number, reverse=True)))
