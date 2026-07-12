# ======================================
# LeetCode Problem: max consecutive ones iii
# Language: python3
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
# Synced by: LinkCode
# Date: 12/07/2026, 14:23:40
# ======================================


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        count = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
                while count > k:
                    if nums[l] == 0:
                        count -= 1
                    l += 1

            ans = max(ans, r - l + 1)
        
        return ans