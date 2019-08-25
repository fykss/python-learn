import random
import math

print("All set. Get ready to rumble!")

N = int(input("Enter number of area shooting: "))
shooting_area = []
random_x = int(math.ceil(random.random() * N))
random_y = int(math.ceil(random.random() * N))
N += 1
flag_win = True


def show_area():
    for i in range(N):
        shooting_area.append(["-"] * N)
        shooting_area[i][0] = i
        shooting_area[0][i] = i

    # shooting_area[random_y][random_x] = "+"

    for i in range(N):
        print(' | '.join(map(str, shooting_area[i])))


show_area()

while flag_win:
    try:
        user_x = int(
            input("Enter your coordinate X from 1 to {}: ".format(N - 1)))
        user_y = int(
            input("Enter your coordinate Y from 1 to {}: ".format(N - 1)))
    except ValueError:
        print("That not an int! Try again.")
        continue

    shooting_area[user_y][user_x] = "*"

    if user_x == random_x and user_y == random_y:
        print("**** You have won! ****")
        flag_win = False

    show_area()
