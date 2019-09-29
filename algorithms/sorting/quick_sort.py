# Quick sort visualized https://www.youtube.com/watch?time_continue=202&v=3ApI8aiW784

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        # sub-array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]

        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]

        print("Less arr: {}".format(less))
        print("Greater arr: {}".format(greater))
        print("Pivot: {}".format(pivot))
        print("\a")

        return quick_sort(less) + [pivot] + quick_sort(greater)


list1 = [10, 2, 6, 3, 5, 9, 7, 10, 4]
print(quick_sort(list1))




