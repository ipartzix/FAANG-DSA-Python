matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# brout force solution 

def makeinfinity(matrix, row, column):
    for i in range(len(matrix)):
        if matrix[i][column] != 0:
            matrix[i][column] = float("-inf")

    for j in range(len(matrix[0])):
        if matrix[row][j] != 0:
            matrix[row][j] = float("-inf")


def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zeros = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for i, j in zeros:
        makeinfinity(matrix, i, j)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float("-inf"):
                matrix[i][j] = 0

    return matrix


print(setZeroes(matrix))
