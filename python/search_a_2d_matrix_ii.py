# ======================================
# LeetCode Problem: search a 2d matrix ii
# Language: python3
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Synced by: LinkCode
# Date: 26/07/2026, 12:53:20
# ======================================


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l = 0
            r = len(matrix[row]) - 1

            while l <= r:
                mid = (l+r) // 2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return False
