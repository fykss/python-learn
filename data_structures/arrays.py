# documentation https://www.geeksforgeeks.org/python-arrays/ , https://docs.python.org/3/library/array.html


import array as arr

# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

print("The new created array is:", end=" ")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print("The new created array is:", end=" ")
for i in b:
    print(i, end=" ")
print()

b.append()
