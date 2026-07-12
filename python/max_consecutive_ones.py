# ======================================
# LeetCode Problem: max consecutive ones
# Language: python3
# Link: https://leetcode.com/problems/max-consecutive-ones/
# Synced by: LinkCode
# Date: 12/07/2026, 14:11:21
# ======================================


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
                while l < len(nums) and nums[l] == 0:
                    l += 1
                
            ans = max(ans, r - l + 1)
        
        return ans