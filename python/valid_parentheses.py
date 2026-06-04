# ======================================
# LeetCode Problem: valid parentheses
# Language: python3
# Link: https://leetcode.com/problems/valid-parentheses/
# Synced by: LinkCode
# Date: 04/06/2026, 00:13:45
# ======================================


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if stack:
                    if i == ")" and stack[-1] != "(":
                        return False
                    elif i == "]" and stack[-1] != "[":
                        return False
                    elif i == "}" and stack[-1] != "{":
                        return False
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
            
        return True