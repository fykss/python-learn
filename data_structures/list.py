colors = ['red', 'blue', 'green']
print(colors[0])  # red
print(colors[2])  # green
print(len(colors))  # 3


list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print('yay')


# List Methods:

list.count('larry')  # return 1
list.append('shemp')  # append elem at end
list.insert(0, 'xxx')  # insert elem at index 0
list.extend(['yyy', 'zzz'])  # add list of elems at end
list.index('curly')  # 2
list.remove('curly')  # search and remove that element
list.pop(1)  # removes and returns 'larry'


# List Slices

list1 = ['a', 'b', 'c', 'd']

list1[1:-1]  # ['b', 'c']
list1[0:2] = 'z'  # replace ['a', 'b'] with ['z']
