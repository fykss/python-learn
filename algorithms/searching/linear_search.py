def linear_search(A: list, item_search: int):
    for k in range(len(A)):
        if A[k] == item_search:
            return k
    return -1


def test_linear_search():
    A1 = [1, 2, 3, 4, 8]
    result = linear_search(A1, 5)
    if result == -1:
        print("Test1 - passed")
    else:
        print("Test1 - failed")

    A2 = [-1, -2, -3, -4, -8]
    result = linear_search(A2, -3)
    if result == 2:
        print("Test2 - passed")
    else:
        print("Test2 - failed")

    A3 = [10, 20, 20, 40, 30]
    result = linear_search(A3, 30)
    if result == 4:
        print("Test3 - passed")
    else:
        print("Test3 - failed")


test_linear_search()
