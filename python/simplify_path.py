# ======================================
# LeetCode Problem: simplify path
# Language: python3
# Link: https://leetcode.com/problems/simplify-path/
# Synced by: LinkCode
# Date: 27/07/2026, 22:22:50
# ======================================


class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = "/"
        stack = []
        
        directories = path.split("/")

        for i in directories:
            if stack and i == "..":
                stack.pop()
            elif i != "" and i != "." and i != "..":
                stack.append(i)

        for d in range(len(stack)):
            if d < len(stack) - 1:
                ans += stack[d]
                ans += "/"
            else:
                ans += stack[d]
        
        return ans
