# ======================================
# LeetCode Problem: longest substring without repeating characters
# Language: python3
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Synced by: LinkCode
# Date: 04/06/2026, 23:20:00
# ======================================


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
        
            ans = max(ans, r - l + 1)            
            hashset.add(s[r])
        
        return ans
        