# ======================================
# LeetCode Problem: removing stars from a string
# Language: python3
# Link: https://leetcode.com/problems/removing-stars-from-a-string/
# Synced by: LinkCode
# Date: 12/06/2026, 15:15:21
# ======================================


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "*":
                stack.append(i)
            else:
                stack.pop()
        
        return "".join(stack)