# ======================================
# LeetCode Problem: find k closest elements
# Language: python3
# Link: https://leetcode.com/problems/find-k-closest-elements/
# Synced by: LinkCode
# Date: 12/07/2026, 15:18:37
# ======================================


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k
        mid = (l + r) // 2

        while l < r:
            mid = (l + r) // 2

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        
        return arr[l:l+k]
