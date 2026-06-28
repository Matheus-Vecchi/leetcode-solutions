# ======================================
# LeetCode Problem: max consecutive ones iii
# Language: python3
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
# Synced by: LinkCode
# Date: 27/06/2026, 23:58:45
# ======================================


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        lifes = k
        ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                lifes -= 1
            
            while lifes < 0:
                if nums[l] == 0:
                    lifes += 1
                l += 1

            ans = max(ans, r - l + 1)


        return ans
        