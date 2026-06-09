class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target > matrix[mid][-1]:
                lo = mid+1
            elif target < matrix[mid][0]:
                hi = mid-1
            else:
                break

        searchRow = mid
        
        lo = 0
        hi = len(matrix[searchRow]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == matrix[searchRow][mid]:
                return True
            elif target > matrix[searchRow][mid]:
                lo = mid+1
            else:
                hi = mid-1
        return False