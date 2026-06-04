# ======================================
# LeetCode Problem: contains duplicate
# Language: python3
# Link: https://leetcode.com/problems/contains-duplicate/
# Synced by: LinkCode
# Date: 03/06/2026, 23:27:35
# ======================================


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        
        return False