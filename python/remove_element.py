# ======================================
# LeetCode Problem: remove element
# Language: python3
# Link: https://leetcode.com/problems/remove-element/
# Synced by: LinkCode
# Date: 05/08/2026, 11:50:20
# ======================================


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        
        return k