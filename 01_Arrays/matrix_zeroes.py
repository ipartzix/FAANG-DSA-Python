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


# optimal


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_track = [0] * rows
        col_track = [0] * cols

        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1

        for i in range(0, rows):
            for j in range(0, cols):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0

        return matrix


# Time complexity: O(m×n)O(m×n), because you traverse the matrix twice.
# Space complexity: O(m+n)O(m+n), because you use two tracking arrays


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_track = [0] * rows
        col_track = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1

        for i in range(rows):
            for j in range(cols):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0

# optimzed both time and *space* 
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark rows and columns using the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle the first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle the first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Time: O(m×n)O(m×n)
# Extra space: O(1))