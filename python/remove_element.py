# ======================================
# LeetCode Problem: remove element
# Language: python3
# Link: https://leetcode.com/problems/remove-element/
# Synced by: LinkCode
# Date: 07/07/2026, 14:42:53
# ======================================


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        
        return k