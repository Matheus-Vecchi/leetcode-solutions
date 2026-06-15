# ======================================
# LeetCode Problem: find the index of the first occurrence in a string
# Language: python3
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Synced by: LinkCode
# Date: 15/06/2026, 16:38:13
# ======================================


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        l = 0

        for r in range(len(needle)-1, len(haystack)):
            if haystack[l:r+1] == needle:
                return l
            l += 1
        
        return -1

        