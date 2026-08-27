# ======================================
# LeetCode Problem: longest substring without repeating characters
# Language: python3
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Synced by: LinkCode
# Date: 27/08/2026, 13:43:14
# ======================================


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        ans = 0

        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[r])
            
            ans = max(ans, r - l + 1)
        
        return ans
