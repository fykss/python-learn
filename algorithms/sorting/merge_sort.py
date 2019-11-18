# https://www.youtube.com/watch?v=qf82-r9hl2Y&t=992s
# https://www.geeksforgeeks.org/python-program-for-merge-sort/


def merge(A: list, B: list):
    C = [0] * (len(A) + len(B))

    # i - index for list A
    # k - index for list B
    # n - index for list C
    i = k = n = 0

    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1

    # Copy the remaining elements of A[], if there are any
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    # Copy the remaining elements of B[], if there are any
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C


def merge_sort(A: list):
    if len(A) <= 1:
        return

    middle = len(A) // 2
    L = [A[i] for i in range(middle)]
    R = [A[i] for i in range(middle, len(A))]

    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)

    for i in range(len(A)):
        A[i] = C[i]


B = [5, 2, 7, 3, 1]
merge_sort(B)
print(*B)
