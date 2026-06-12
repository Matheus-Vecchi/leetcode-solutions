# ======================================
# LeetCode Problem: number of zero filled subarrays
# Language: python3
# Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Synced by: LinkCode
# Date: 11/06/2026, 22:36:04
# ======================================


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                if nums[l] != 0:
                    l = r
            
                ans += r - l + 1
            else:
                l = r
        
        return ans
                