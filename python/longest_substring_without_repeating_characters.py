# ======================================
# LeetCode Problem: longest substring without repeating characters
# Language: python3
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Synced by: LinkCode
# Date: 27/08/2026, 13:49:25
# ======================================


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        ans = 0

        l = 0
        for r in range(len(s)):
            if s[r] in hashmap and hashmap[s[r]] >= l:
                l = hashmap[s[r]] + 1
                hashmap[s[r]] = r
            
            hashmap[s[r]] = r
            
            ans = max(ans, r - l + 1)
        
        return ans
