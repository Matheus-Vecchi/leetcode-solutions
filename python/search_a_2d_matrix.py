# ======================================
# LeetCode Problem: search a 2d matrix
# Language: python3
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Synced by: LinkCode
# Date: 17/05/2026, 19:25:22
# ======================================


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = (low+high) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False