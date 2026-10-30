# Leetcode 54: Print the Matrix in Spiral Order


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        counter = 0

        result = []

        while counter <= min(row, col) // 2:

            if counter <= col - counter:
                for i in range(counter, col - counter + 1):
                    result.append(matrix[counter][i])
                if counter + 1 <= row - counter:
                    for i in range(counter + 1, row - counter + 1):
                        result.append(matrix[i][col - counter])
                    if col - counter - 1 >= counter:
                        for i in range(col - counter - 1, -1 + counter, -1):
                            result.append(matrix[row - counter][i])
                        if row - counter - 1 >= counter + 1:
                            for i in range(row - counter - 1, counter, -1):
                                result.append(matrix[i][counter])

            counter += 1
        return result
