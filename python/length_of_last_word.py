# ======================================
# LeetCode Problem: length of last word
# Language: python3
# Link: https://leetcode.com/problems/length-of-last-word/
# Synced by: LinkCode
# Date: 15/06/2026, 22:22:52
# ======================================


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while s[i] == " ":
            i -= 1
        
        ans = 0

        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        
        return ans