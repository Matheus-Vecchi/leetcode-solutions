# ======================================
# LeetCode Problem: search a 2d matrix ii
# Language: python3
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Synced by: LinkCode
# Date: 26/07/2026, 14:54:35
# ======================================


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr > target:
                col -= 1
            else:
                row += 1

        return False
