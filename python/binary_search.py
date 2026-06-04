# ======================================
# LeetCode Problem: binary search
# Language: python3
# Link: https://leetcode.com/problems/binary-search/
# Synced by: LinkCode
# Date: 04/06/2026, 14:41:59
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