# https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/ - using numpy library
# A basic code for matrix input from user


def create_matrix():
    matrix = []
    row = int(input("Enter the number of rows: "))
    column = int(input("Enter the number of columns: "))

    for i in range(row):
        a = []
        for j in range(column):
            print("Enter number of row={}, column={}: ".format(i, j), end="")
            a.append(int(input()))
        matrix.append(a)
    return matrix


def get_dimension_matrix(matrix):
    # row = len(matrix); column = len(matrix[0])
    print("Dimension of the matrix: {}x{}".format(len(matrix), len(matrix[0])))


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


def addition_matrix(*matrix):
    # TODO: impl addition matrix (any quantity)
    # not implement yet
    count = 0
    for i in zip(*matrix):
        count += 1
        print("Count:", count)

        for j in range(len(i)):
            print(i[j])


a = create_matrix()
b = create_matrix()
print(a)
get_dimension_matrix(a)
print_matrix(a)

# addition_matrix(a, b)

# one-liner logic to take input for rows and columns
# mat = [[int(input()) for x in range(column)] for y in range(row)]
