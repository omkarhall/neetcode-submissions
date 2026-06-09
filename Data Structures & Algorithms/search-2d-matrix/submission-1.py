class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            midCol = (l + r) // 2
            if target == matrix[midRow][midCol]:
                return True
            elif target > matrix[midRow][midCol]:
                l = midCol + 1
            else:
                r = midCol - 1
        return False
