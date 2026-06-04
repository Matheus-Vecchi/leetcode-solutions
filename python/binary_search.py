# ======================================
# LeetCode Problem: binary search
# Language: python3
# Link: https://leetcode.com/problems/binary-search/
# Synced by: LinkCode
# Date: 03/06/2026, 23:55:36
# ======================================


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1