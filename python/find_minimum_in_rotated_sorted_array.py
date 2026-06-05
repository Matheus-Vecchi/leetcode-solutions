# ======================================
# LeetCode Problem: find minimum in rotated sorted array
# Language: python3
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Synced by: LinkCode
# Date: 05/06/2026, 15:52:37
# ======================================


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]