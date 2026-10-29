# Leetcode 48: Rotated Array
# Brute Force
"""
1 2 3
4 5 6
7 8 9

"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotetArray(matrix):

    row =len(matrix)
    column =len(matrix[0])
    result = [[0] * column for _ in range(row)]
    for i in range(0,row):
        for j in range(column):
            result[j][row - 1 - i] = matrix[i][j]

    matrix = result
    return matrix


print(rotetArray(matrix))


