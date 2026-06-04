# ======================================
# LeetCode Problem: valid palindrome
# Language: python3
# Link: https://leetcode.com/problems/valid-palindrome/
# Synced by: LinkCode
# Date: 03/06/2026, 23:47:22
# ======================================


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True