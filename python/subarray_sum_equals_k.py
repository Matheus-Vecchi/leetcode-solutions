# ======================================
# LeetCode Problem: subarray sum equals k
# Language: python3
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Synced by: LinkCode
# Date: 13/07/2026, 22:57:39
# ======================================


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        current_sum = 0
        count = 0

        for i in nums:
            current_sum += i
            if current_sum - k in prefix:
                count += prefix[current_sum - k]
            
            if current_sum in prefix:
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1
        
        return count
