# [ expression for item in list if conditional ]


new_list = []
list = [i for i in range(10) if i % 2 == 0]
new_list = [print(i) for i in list]


words = ["giN", "Zen", "gIg", "mSg"]

letters_lower = [letter.lower() for word in words for letter in word if letter.isupper()]

print(letters_lower)


list1 = [10, 2, 6, 3, 5, 9, 7, 1]

# new list number less then 5
new_list1 = [i for i in list1 if i < 5]
print(new_list1)