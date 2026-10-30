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


# better and easy approch
# LeetCode 54: Spiral Matrix


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        column = len(matrix[0])

        top = 0
        left = 0
        bottom = row - 1
        right = column - 1

        result = []

        while top <= bottom and left <= right:

            # 1. Left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 2. Top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 3. Right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # 4. Bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
