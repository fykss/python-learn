# Logarithm is the inverse of exponentiation (Логарифм - операция, обратная возведению в степень)


def binary_search(list, search_item):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        # mid = left + (right - left) // 2

        if search_item == list[mid]:
            return mid
        elif search_item > list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return None


my_list1 = [1, 3, 5, 7, 9]
my_list2 = [1, 2, 3, 4, 5]

print(binary_search(my_list1, 5))
