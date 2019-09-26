def bubble_sort(arr: int):
    iter = True
    while iter:
        for i in range(len(arr) - 1):
            iter = False
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                iter = True


def bubble_sort_test():
    list1 = [10, 2, 6, 3, 5, 9, 7]
    print("Source array: {}".format(list1))
    bubble_sort(list1)
    print("Sorted array: {}".format(list1))


bubble_sort_test()
