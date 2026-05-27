# ======================================
# LeetCode Problem: longest substring without repeating characters
# Language: python3
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Synced by: LinkCode
# Date: 26/05/2026, 21:47:38
# ======================================


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]] + 1, l)
                hashmap[s[r]] = r
                
            hashmap[s[r]] = r
            ans = max(ans, r - l + 1)
        
        return ans
