# ======================================
# LeetCode Problem: remove duplicates from sorted array
# Language: python3
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Synced by: LinkCode
# Date: 09/06/2026, 22:56:27
# ======================================


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            
            fast += 1
        
        return len(nums[:slow+1])
        