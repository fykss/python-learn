# lambda arguments: expression


from functools import reduce


def greeting():
    print("hello")


(lambda: print("hello"))()


# Use of lambda() with filter()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)  # [5, 7, 97, 77, 23, 73, 61]


# Use of lambda() with map()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)  # [10, 14, 44, 194, 108, 124, 154, 46, 146, 122]


# Use of lambda() with reduce()
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)  # 193
