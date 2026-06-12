# ======================================
# LeetCode Problem: number of zero filled subarrays
# Language: python3
# Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Synced by: LinkCode
# Date: 11/06/2026, 22:50:15
# ======================================


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 1
        ans = 0

        while i < len(nums):
            count = 1
            while i < len(nums) and nums[i] == 0:
                ans += count 
                count += 1
                
                i += 1
            
            i += 1
        
        return ans
