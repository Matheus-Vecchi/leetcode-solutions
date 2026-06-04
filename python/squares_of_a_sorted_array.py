# ======================================
# LeetCode Problem: squares of a sorted array
# Language: python3
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Synced by: LinkCode
# Date: 04/06/2026, 15:08:46
# ======================================


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [0] * len(nums)
        last = r
        
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                ans[last] = nums[l] ** 2
                last -= 1
                l += 1
            else:
                ans[last] = nums[r] ** 2
                last -= 1
                r -= 1
        
        return ans