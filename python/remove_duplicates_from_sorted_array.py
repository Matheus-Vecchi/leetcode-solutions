# ======================================
# LeetCode Problem: remove duplicates from sorted array
# Language: python3
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Synced by: LinkCode
# Date: 05/08/2026, 15:13:20
# ======================================


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k], nums[i] = nums[i], nums[k]
        
        return k + 1