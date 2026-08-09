# ======================================
# LeetCode Problem: number of zero filled subarrays
# Language: python3
# Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Synced by: LinkCode
# Date: 09/08/2026, 11:59:41
# ======================================


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        acc = 0 # 1
        ans = 0 # 3
        l = 0 # 5
        for r in range(len(nums)):
            if nums[r] == 0:
                if nums[l] != 0:
                    l = r
                acc = acc + r - l + 1
            else:
                ans += acc
                acc = 0
                l = r
        
        if acc != 0:
            ans += acc
            
        return ans
