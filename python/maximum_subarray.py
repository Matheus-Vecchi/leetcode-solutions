# ======================================
# LeetCode Problem: maximum subarray
# Language: python3
# Link: https://leetcode.com/problems/maximum-subarray/
# Synced by: LinkCode
# Date: 27/07/2026, 20:06:41
# ======================================


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for i in nums:
            current_sum = max(i, current_sum + i)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
            