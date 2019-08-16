list = ["vlad", 1, 2, "dada"]

name = list[0]


# Decision Making

if type(name) == str:
    print("str")

list = [2, 3, 4, 5, 6, 4]

print(list)


# For Loop

for i in range(len(list)):
    list[i] = i
    break

for count, item in enumerate(list, start=1):   # default is zero
    print(item)

print(list)
print(count)

print('there were {} items printed'.format(count))


# While Loop

count = 0
while count < 9:
    print('The count is:', count)
    count += 1

print("Good bye!")
