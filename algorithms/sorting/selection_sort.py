def selection_sort(arr: int):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        swap(arr, i, min_index)

# def selection_sort_short(arr: int):
#     arr = [swap(arr, i, j) for i in range(len(arr) for j in range(i + 1, len(arr) if arr[i] > arr[j]]


def swap(arr: int, index1: int, index2: int):
     # short form: arr[index1], arr[index2] = arr[index2], arr[index1]
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp


list1 = [10, 2, 6, 3, 5, 9, 7]
# list1 = [3, 5, 2]

print("Source array:", list1)

selection_sort(list1)
print("Sorted array:", list1)

# list2 = [3, 5, 2]
# selection_sort_short(list2)
# print("Sorted array:", list2)
